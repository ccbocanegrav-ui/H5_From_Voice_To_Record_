"""Transcripción con faster-whisper. Importa la librería de forma perezosa (los tests no la necesitan)."""
from __future__ import annotations

import inspect
import time
from pathlib import Path
from typing import Any

from .config import resolver_ruta


def resolver_dispositivo(device_cfg: str, compute_cfg: str) -> tuple[str, str]:
    """Decide dispositivo y precisión.

    - "cuda" sin GPU disponible -> ERROR. No hay fallback silencioso a CPU (corre ~40x más lento
      y el texto sale igual, así que nadie lo notaría).
    - "auto" usa GPU si existe y CPU si no; el dispositivo REAL se lee después del modelo.
    - float16 no existe en CPU: se baja a int8 (queda registrado en el resultado).
    """
    import ctranslate2

    n = ctranslate2.get_cuda_device_count()
    if device_cfg == "cuda" and n == 0:
        raise RuntimeError("Se pidió GPU (device: cuda) pero CUDA no está disponible; "
                           "no se hace fallback silencioso a CPU.")
    device = "cuda" if (device_cfg in ("auto", "cuda") and n > 0) else "cpu"
    compute = compute_cfg
    if device == "cpu" and compute in ("float16", "int8_float16"):
        compute = "int8"
    return device, compute


def mecanismo_glosario_disponible() -> str:
    """'hotwords' si esta versión de faster-whisper lo soporta; si no, 'initial_prompt'."""
    from faster_whisper import WhisperModel

    return "hotwords" if "hotwords" in inspect.signature(WhisperModel.transcribe).parameters else "initial_prompt"


def cargar_modelo(nombre: str, device: str, compute_type: str, cfg: dict[str, Any]):
    """Carga el modelo y devuelve (modelo, info). `device_leido` sale de la librería, no de la config."""
    from faster_whisper import WhisperModel

    models_dir = resolver_ruta(cfg, cfg["paths"]["models_dir"])
    models_dir.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()
    modelo = WhisperModel(nombre, device=device, compute_type=compute_type, download_root=str(models_dir))
    ct2 = modelo.model
    info = {
        "modelo": nombre,
        "device_pedido": device,
        "compute_pedido": compute_type,
        "device_leido": str(ct2.device),            # lo que ctranslate2 realmente está usando
        "compute_leido": str(ct2.compute_type),
        "carga_s": round(time.perf_counter() - t0, 3),
    }
    info["fallback_silencioso"] = info["device_leido"] != device
    return modelo, info


def transcribir(modelo, audio_path: str | Path, cfg: dict[str, Any], glosario: list[str] | None = None) -> dict:
    a = cfg["asr"]
    kwargs: dict[str, Any] = dict(
        language=a["language"], beam_size=a["beam_size"], temperature=a["temperature"],
        condition_on_previous_text=a["condition_on_previous_text"], vad_filter=a["vad_filter"],
    )
    mecanismo = None
    if glosario:
        mecanismo = mecanismo_glosario_disponible()
        kwargs["hotwords" if mecanismo == "hotwords" else "initial_prompt"] = ", ".join(glosario)
    t0 = time.perf_counter()
    segmentos, info = modelo.transcribe(str(audio_path), **kwargs)   # generador: se consume dentro del cronómetro
    lista = [{"inicio": round(s.start, 2), "fin": round(s.end, 2), "texto": s.text.strip()} for s in segmentos]
    dt = time.perf_counter() - t0
    return {
        "texto": " ".join(s["texto"] for s in lista),
        "segmentos": lista,
        "duracion_audio_s": float(info.duration),
        "tiempo_transcripcion_s": round(dt, 3),
        "mecanismo_glosario": mecanismo,
    }
