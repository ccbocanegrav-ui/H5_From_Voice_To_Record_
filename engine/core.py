"""Motor único para T1 (entrevistas) y T2 (llamadas de venta).

Una sola función pública: process_audio(audio_path, schema). La app solo llama a esta función.
Regla del enunciado: este paquete NO importa ninguna librería de UI.
"""
from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import asr, cache
from .config import load_config

_MODELOS: dict[tuple, tuple] = {}     # (modelo, device, compute) -> (modelo, info); evita recargar


def _modelo(nombre: str, device: str, compute: str, cfg: dict[str, Any]):
    k = (nombre, device, compute)
    if k not in _MODELOS:
        _MODELOS[k] = asr.cargar_modelo(nombre, device, compute, cfg)
    return _MODELOS[k]


def process_audio(audio_path: str, schema: str = "t1", config_path: str = "config.yaml", *,
                  use_cache: bool = True, cache_only: bool = False, model_name: str | None = None,
                  device: str | None = None, compute_type: str | None = None,
                  glosario: bool | None = None) -> dict[str, Any]:
    """Transcribe y extrae un registro estructurado. NUNCA lanza: los errores van en result["error"].

    schema: "t1" (entrevista) o "t2" (llamada de venta): mismo motor, distinto esquema de registro.
    use_cache: lee/escribe data/cache/asr/... (para clips del corpus). Para un audio subido en la app
               usa use_cache=False (no escribe nada).
    cache_only: solo lee la caché de config.asr.cache_corpus; si no está, devuelve error. La app usa esto
                para mostrar el corpus sin re-transcribir.

    Devuelve: transcript, fields, verified (campo -> bool), device (leído de la librería), elapsed_s, error,
    más model, compute_type, cache_hit, schema y extraction (estado de la extracción).
    """
    t0 = time.perf_counter()
    res: dict[str, Any] = {
        "transcript": "", "fields": {}, "verified": {}, "device": None, "elapsed_s": 0.0, "error": None,
        "model": None, "compute_type": None, "cache_hit": False, "schema": schema,
        "extraction": "pendiente (Fase 3)",
    }
    try:
        cfg = load_config(config_path)
        a = cfg["asr"]
        p = Path(audio_path)
        if schema not in cfg["schemas"]:
            raise ValueError(f"schema desconocido: {schema!r} (opciones: {list(cfg['schemas'])})")

        if cache_only:
            cc = a["cache_corpus"]
            nombre, dev, comp, usar_glos = cc["model"], cc["device"], cc["compute_type"], cc.get("glossary", False)
        else:
            if not p.exists():
                raise FileNotFoundError(audio_path)
            nombre = model_name or a["default_model"]
            dev, comp = asr.resolver_dispositivo(device or a["device"], compute_type or a["compute_type"])
            usar_glos = a["use_glossary_default"] if glosario is None else glosario
        terminos = a["glossary"].get(schema, []) if usar_glos else None
        cpath = cache.ruta(cfg, nombre, dev, comp, bool(terminos), p.stem)

        if (use_cache or cache_only) and cpath.exists():
            data = cache.leer(cpath)
            res["cache_hit"] = True
        elif cache_only:
            raise FileNotFoundError(f"No hay transcripción en caché para {p.stem!r} con {cpath.parent.name}")
        else:
            modelo, info = _modelo(nombre, dev, comp, cfg)
            out = asr.transcribir(modelo, p, cfg, terminos)
            data = {
                "clip": p.stem, "audio": p.name, "texto": out["texto"], "segmentos": out["segmentos"],
                "duracion_audio_s": out["duracion_audio_s"],
                "tiempo_transcripcion_s": out["tiempo_transcripcion_s"],
                "modelo": nombre, "device_leido": info["device_leido"], "compute_leido": info["compute_leido"],
                "compute_pedido": comp, "glosario": bool(terminos), "mecanismo_glosario": out["mecanismo_glosario"],
                "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
            if use_cache:
                cache.escribir(cpath, data)

        res.update(transcript=data["texto"], device=data["device_leido"], model=data["modelo"],
                   compute_type=data.get("compute_leido") or comp)

        # Extracción + verificación literal (Fase 3). Si el módulo aún no existe, el registro queda vacío
        # y se indica en "extraction": no se inventan campos.
        try:
            from extraction import extraer
        except ImportError:
            pass
        else:
            ex = extraer(schema, res["transcript"], cfg)
            res["fields"], res["verified"], res["extraction"] = ex["fields"], ex["verified"], "ok"
    except Exception as e:
        res["error"] = f"{type(e).__name__}: {e}"
    finally:
        res["elapsed_s"] = round(time.perf_counter() - t0, 3)
    return res
