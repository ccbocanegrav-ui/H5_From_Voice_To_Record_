"""Pruebas que NO necesitan pesos de Whisper ni GPU: usan un modelo falso para validar la lógica."""
import importlib.util
import re
import sys
from pathlib import Path

import pytest

from engine import asr
from engine.config import load_config

ROOT = Path(__file__).resolve().parent.parent


def test_motor_no_importa_librerias_de_ui():
    """Equivale al comando del README: grep -rEn "streamlit|gradio|tkinter|flask" engine/"""
    prohibidas = re.compile(r"^\s*(import|from)\s+(streamlit|gradio|tkinter|flask|dash|nicegui|PyQt\d?|PySide\d?)\b", re.M)
    for py in (ROOT / "engine").rglob("*.py"):
        assert not prohibidas.search(py.read_text(encoding="utf-8")), f"{py} importa una librería de UI"


def test_cuda_sin_gpu_es_error_no_fallback():
    pytest.importorskip("ctranslate2")
    import ctranslate2
    if ctranslate2.get_cuda_device_count() == 0:
        with pytest.raises(RuntimeError, match="no se hace fallback"):
            asr.resolver_dispositivo("cuda", "float16")
        assert asr.resolver_dispositivo("auto", "float16") == ("cpu", "int8")


def test_process_audio_no_lanza_y_reporta_error():
    from engine import process_audio
    r = process_audio("no_existe.m4a", "t1")
    assert r["error"] and "FileNotFoundError" in r["error"]
    assert {"transcript", "fields", "verified", "device", "elapsed_s", "error"} <= set(r)
    r2 = process_audio("no_existe.m4a", "t9")
    assert "schema desconocido" in r2["error"]


def test_cache_only_sin_cache_da_error_claro():
    from engine import process_audio
    r = process_audio("data/audio/t1_01.m4a", "t1", cache_only=True)
    assert r["error"] and "caché" in r["error"]


class _SegFalso:
    def __init__(self, t): self.start, self.end, self.text = 0.0, 1.0, t


def _cargar_benchmark():
    spec = importlib.util.spec_from_file_location("benchmark_asr", ROOT / "scripts" / "benchmark_asr.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["benchmark_asr"] = m
    spec.loader.exec_module(m)
    return m


class ModeloFalso:
    """Imita a faster-whisper: devuelve la referencia con ruido controlado según la 'calidad' del modelo."""
    def __init__(self, calidad): self.calidad = calidad


class AsrFalso:
    refs: dict = {}

    @staticmethod
    def cargar_modelo(nombre, device, compute, cfg):
        calidad = {"small": 3, "large-v3": 1}[nombre]
        return ModeloFalso(calidad), {"modelo": nombre, "device_pedido": device, "compute_pedido": compute,
                                       "device_leido": device, "compute_leido": compute, "carga_s": 0.1,
                                       "fallback_silencioso": False}

    @staticmethod
    def transcribir(modelo, audio_path, cfg, glosario=None):
        clip = Path(audio_path).stem
        palabras = AsrFalso.refs[clip].split()
        for i in range(0, len(palabras), 40 // modelo.calidad):   # más error con 'small'
            palabras[i] = "xxx"
        return {"texto": " ".join(palabras), "segmentos": [], "duracion_audio_s": 200.0,
                "tiempo_transcripcion_s": 10.0 * modelo.calidad, "mecanismo_glosario": "hotwords" if glosario else None}


def test_benchmark_de_punta_a_punta_con_modelo_falso(tmp_path):
    bm = _cargar_benchmark()
    cfg = load_config()
    cfg["_root"] = str(tmp_path)
    (tmp_path / "data" / "audio").mkdir(parents=True)
    src = load_config()
    AsrFalso.refs = bm.cargar_referencias(src, "t1")
    for clip in AsrFalso.refs:
        (tmp_path / "data" / "audio" / f"{clip}.m4a").write_bytes(b"")
    cfg["paths"]["ground_truth_t1"] = str(ROOT / cfg["paths"]["ground_truth_t1"])
    # el 'mundo' sin GPU: se cae a que gpu_verificada sea False (sin nvidia-smi), pero todo lo demás corre
    out = bm.ejecutar(cfg, "t1", solo=["small_gpu_fp16", "small_gpu_int8", "large_gpu_fp16", "small_cpu_int8"],
                      sin_cpu=False, mod_asr=AsrFalso, salida=tmp_path / "results")
    por_id = {e["id"]: e for e in out["experimentos"]}
    assert por_id["large_gpu_fp16"]["wer"] < por_id["small_gpu_fp16"]["wer"]          # el modelo 'mejor' tiene menos WER
    lo, hi = por_id["small_gpu_fp16"]["wer_ic95"]
    assert lo <= por_id["small_gpu_fp16"]["wer"] <= hi
    assert por_id["small_cpu_int8"]["n_clips"] == 2                                   # max_clips respetado
    assert por_id["small_gpu_fp16"]["gpu_verificada"] is False                         # sin nvidia-smi no se afirma que hubo GPU
    comp = out["comparaciones"]["dispositivo"][0]
    assert comp["n_clips"] == 2 and comp["clips_con_texto_distinto"] == 0
    assert (tmp_path / "results" / "asr_benchmark_t1.md").exists()
    assert (tmp_path / "data" / "cache" / "asr" / "small__cuda__float16__plano" / "t1_01.json").exists()
