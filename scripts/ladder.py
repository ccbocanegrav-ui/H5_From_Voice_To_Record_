"""Construye la escalera de degradación de T2 a partir de los audios originales (L0).

    python scripts/ladder.py            # lee data/audio/t2_*, escribe data/audio_ladder/t2_XX__L1.ogg ...

  L0  original (no se copia)
  L1  nota de voz tipo WhatsApp: Opus 16 kbps mono
  L2  llamada telefónica: banda 300-3400 Hz, 8 kHz
  L3  L1 + ruido rosa a SNR 10 dB. El ruido se mezcla ANTES del códec; la SNR se mide sobre los tramos
      con voz (no sobre todo el clip, que incluye silencios) y se guarda en data/audio_ladder/snr.json.

Requiere ffmpeg en el PATH. Es determinista (semilla en config). data/audio_ladder/ no se sube a git.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine.config import load_config, resolver_ruta   # noqa: E402

SR = 16000
EXTS = {".m4a", ".wav", ".mp3", ".ogg", ".flac", ".aac", ".opus", ".mp4", ".webm"}


def _ffmpeg(*args: str) -> None:
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(f"ffmpeg falló: {r.stderr.strip()}")


def decodificar(ruta: Path) -> np.ndarray:
    """Audio mono 16 kHz float32 en [-1, 1]."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(ruta), "-ac", "1", "-ar", str(SR),
                        "-f", "f32le", "pipe:1"], capture_output=True)
    if r.returncode:
        raise RuntimeError(f"no se pudo decodificar {ruta}: {r.stderr.decode()}")
    return np.frombuffer(r.stdout, dtype=np.float32).copy()


def potencia_activa(x: np.ndarray, ventana_db: float, trama_ms: int = 30) -> float:
    """Potencia media de las tramas con voz: las que están a menos de `ventana_db` dB de la trama más fuerte."""
    n = int(SR * trama_ms / 1000)
    k = len(x) // n
    tramas = x[: k * n].reshape(k, n)
    p = (tramas ** 2).mean(axis=1)
    if k == 0 or p.max() <= 0:
        raise ValueError("audio vacío o en silencio")
    db = 10 * np.log10(np.maximum(p, 1e-12) / p.max())
    return float(p[db >= -ventana_db].mean())


def ruido_rosa(n: int, rng: np.random.Generator) -> np.ndarray:
    """Ruido rosa (densidad ∝ 1/f) por modelado espectral; media 0, potencia 1."""
    esp = np.fft.rfft(rng.standard_normal(n))
    f = np.arange(len(esp), dtype=float)
    f[0] = 1.0
    r = np.fft.irfft(esp / np.sqrt(f), n)
    return (r - r.mean()) / r.std()


def mezclar_snr(voz: np.ndarray, snr_db: float, semilla: int, ventana_db: float) -> tuple[np.ndarray, float]:
    """Devuelve (mezcla, SNR medida sobre tramas activas en dB)."""
    rng = np.random.default_rng(semilla)
    p_voz = potencia_activa(voz, ventana_db)
    ruido = ruido_rosa(len(voz), rng) * np.sqrt(p_voz / 10 ** (snr_db / 10))
    mezcla = voz + ruido
    pico = np.abs(mezcla).max()
    if pico > 0.99:                                             # evita recorte; la SNR no cambia al escalar ambos
        mezcla = mezcla * (0.99 / pico)
        voz_e, ruido_e = voz * (0.99 / pico), ruido * (0.99 / pico)
    else:
        voz_e, ruido_e = voz, ruido
    medida = 10 * np.log10(potencia_activa(voz_e, ventana_db) / float((ruido_e ** 2).mean()))
    return mezcla.astype(np.float32), float(medida)


def main() -> int:
    cfg = load_config("config.yaml")
    lad = cfg["ladder"]
    origen = resolver_ruta(cfg, cfg["paths"]["audio_dir"])
    destino = resolver_ruta(cfg, lad["dir"])
    destino.mkdir(parents=True, exist_ok=True)
    clips = sorted(p for p in origen.iterdir() if p.stem.startswith("t2_") and p.suffix.lower() in EXTS)
    if not clips:
        print(f"No hay audios t2_* en {origen}")
        return 1
    snr_json: dict[str, dict] = {}
    for p in clips:
        l1 = destino / f"{p.stem}__L1.{lad['L1']['ext']}"
        _ffmpeg("-i", str(p), "-ac", str(lad["L1"]["canales"]), "-c:a", lad["L1"]["codec"], "-b:a", lad["L1"]["bitrate"], str(l1))
        l2 = destino / f"{p.stem}__L2.{lad['L2']['ext']}"
        _ffmpeg("-i", str(p), "-ac", "1", "-af", f"highpass=f={lad['L2']['lowcut_hz']},lowpass=f={lad['L2']['highcut_hz']}",
                "-ar", str(lad["L2"]["sample_rate"]), str(l2))
        mezcla, medida = mezclar_snr(decodificar(p), lad["L3"]["snr_db"], lad["L3"]["semilla"], lad["L3"]["ventana_activa_db"])
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "mezcla.wav"
            sf.write(tmp, mezcla, SR)
            l3 = destino / f"{p.stem}__L3.{lad['L1']['ext']}"
            _ffmpeg("-i", str(tmp), "-ac", "1", "-c:a", lad["L1"]["codec"], "-b:a", lad["L1"]["bitrate"], str(l3))
        snr_json[p.stem] = {"snr_objetivo_db": lad["L3"]["snr_db"], "snr_medida_db": round(medida, 2)}
        print(f"{p.stem}: L1, L2, L3 listos · SNR medida (tramas con voz) = {medida:.2f} dB")
    (destino / "snr.json").write_text(json.dumps(snr_json, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Escalera en {destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
