"""Transcribe todos los clips de una tarea con el motor (process_audio) y deja las transcripciones en caché.

    python scripts/transcribir_corpus.py --task t2 --model large-v3 --device cuda --compute float16

Úsalo en Colab con la MISMA configuración que `asr.cache_corpus` de config.yaml, para que la app
muestre el corpus sin re-transcribir.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from engine import process_audio                       # noqa: E402
from engine.config import load_config, resolver_ruta   # noqa: E402

EXTS = {".m4a", ".wav", ".mp3", ".ogg", ".flac", ".aac", ".opus", ".mp4", ".webm"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--task", choices=["t1", "t2"], required=True)
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--model")
    ap.add_argument("--device")
    ap.add_argument("--compute")
    ap.add_argument("--glosario", action="store_true")
    a = ap.parse_args()

    cfg = load_config(a.config)
    audio_dir = resolver_ruta(cfg, cfg["paths"]["audio_dir"])
    clips = sorted(p for p in audio_dir.iterdir() if p.stem.startswith(a.task + "_") and p.suffix.lower() in EXTS)
    if not clips:
        print(f"No hay audios {a.task}_* en {audio_dir}")
        return 1
    errores = 0
    for p in clips:
        r = process_audio(str(p), a.task, a.config, model_name=a.model, device=a.device, compute_type=a.compute,
                          glosario=True if a.glosario else None)
        estado = f"ERROR {r['error']}" if r["error"] else f"ok · {len(r['transcript'].split())} palabras"
        print(f"{p.name}: dispositivo leído={r['device']} · {r['elapsed_s']} s · caché={'sí' if r['cache_hit'] else 'no'} · {estado}")
        errores += bool(r["error"])
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
