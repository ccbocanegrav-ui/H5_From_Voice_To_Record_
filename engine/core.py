"""Función única: process_audio(audio_path, schema) -> dict estructurado.

Esqueleto. Se completa en la tarea #7.
"""
from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import yaml


def load_config(path: str = "config.yaml") -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def process_audio(audio_path: str, schema: str = "t1", config_path: str = "config.yaml") -> dict[str, Any]:
    """Transcribe y extrae un registro estructurado.

    schema: "t1" (entrevista) o "t2" (llamada de venta). Mismo motor, distinto esquema.

    Devuelve:
        transcript: str
        fields: dict
        verified: dict[str, bool]   # True = el valor existe literalmente en la transcripción
        device: str                 # leído de la librería en runtime, no de la config
        elapsed_s: float
        error: str | None
    """
    t0 = time.perf_counter()
    result: dict[str, Any] = {
        "transcript": "",
        "fields": {},
        "verified": {},
        "device": "unknown",
        "elapsed_s": 0.0,
        "error": None,
    }
    try:
        cfg = load_config(config_path)
        if not Path(audio_path).exists():
            raise FileNotFoundError(audio_path)
        # TODO (#7): transcribir (faster-whisper), extraer (reglas / LLM), verificar literalmente.
        raise NotImplementedError("Motor pendiente: tarea #7")
    except Exception as e:  # el motor nunca lanza: devuelve el error en el resultado
        result["error"] = f"{type(e).__name__}: {e}"
    finally:
        result["elapsed_s"] = round(time.perf_counter() - t0, 3)
    return result
