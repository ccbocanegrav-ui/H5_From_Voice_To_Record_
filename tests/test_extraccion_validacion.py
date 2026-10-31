"""Extracción por reglas + verificación literal + validador aritmético + evaluación de dos capas + escalera."""
import json
import sys
from pathlib import Path

import numpy as np
import pytest

from engine.config import load_config
from extraction import extraer
from metrics import registro as mr
from metrics.evaluacion import contraste, evaluar, resumen_nivel
from validation import diagnostico, validar

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ladder  # noqa: E402

CFG = load_config("config.yaml")
GT = {s: mr.cargar_gt(s, f"data/ground_truth/{f}.csv") for s, f in (("t1", "t1_entrevistas"), ("t2", "t2_llamadas"))}


@pytest.mark.parametrize("schema", ["t1", "t2"])
def test_reglas_perfectas_sobre_transcripcion_de_referencia(schema):
    for cid, real in GT[schema].items():
        ex = extraer(schema, real["transcripcion_referencia"], CFG, "rules")
        mal = [c for c, v in mr.comparar_registro(schema, ex["fields"], real, CFG).items() if not v["ok"]]
        assert not mal, (cid, mal)


def test_valor_inventado_queda_sin_verificar():
    class LLM:                                                  # un "LLM" que alucina un salario
        def __init__(self): self.r = json.dumps({"pretension_salarial": 9999, "moneda": "PEN"})
        class messages:
            pass
    from extraction import llm
    ex = extraer("t1", "Mi pretensión es de seis mil quinientos soles.", CFG, "rules")
    assert ex["fields"]["pretension_salarial"] == 6500 and ex["verified"]["pretension_salarial"]
    from extraction.verificar import verificar_t1
    ok, _ = verificar_t1("pretension_salarial", 9999, "mi pretensión es de 6500 soles", CFG)
    assert not ok


def test_autocorreccion_deja_pedido_final():
    t = "Quiero dos pollos a la brasa y tres chichas moradas en vaso. Espera, perdón, mejor un pollo a la brasa entero."
    ex = extraer("t2", t, CFG, "rules")["candidatos"]["items"]
    pollo = [i for i in ex if i["producto"] == "pollo a la brasa"]
    assert len(pollo) == 1 and pollo[0]["tamano"] == "entero" and pollo[0]["cantidad"] == 1


def test_aritmetica_y_diagnostico():
    items = [{"producto": "ceviche clásico", "tamano": "para dos", "cantidad": 1, "precio_unitario": 48},
             {"producto": "chicha morada", "tamano": "vaso", "cantidad": 2, "precio_unitario": 6}]
    promo = "dos por uno en chicha morada en vaso"
    ok = validar(items, promo, 54, CFG)
    assert ok["total_calculado"] == 54 and ok["consistente"]
    mal = validar(items, promo, 60, CFG)
    assert mal["estado"] == "inconsistente" and mal["diferencia"] == 6
    assert diagnostico(mal, ok) == "asr"          # la referencia cuadra, el ASR no
    assert diagnostico(mal, mal) == "hablante"    # ya estaba mal en lo que se dijo
    assert validar("sin_verificar", None, 54, CFG)["estado"] == "no_calculable"
    p1 = validar([{"producto": "lomo saltado", "tamano": None, "cantidad": 3, "precio_unitario": 30}], CFG["extraction"]["t2"]["promos"][0]["etiqueta"], 80, CFG)
    assert p1["consistente"]                      # 90 - 10 = 80


def test_wilson_y_f1():
    lo, hi = mr.wilson(5, 5)
    assert hi == 1.0 and 0.5 < lo < 0.6
    assert mr.f1_macro(["a", "b"], ["a", "b"]) == 1.0


def _cache(tmp, nombre_cfg, clip, texto):
    d = tmp / "asr" / nombre_cfg
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{clip}.json").write_text(json.dumps({"texto": texto}), encoding="utf-8")


def test_evaluar_con_cache_sintetica_y_escalera(tmp_path):
    cfg = dict(CFG)
    cfg["paths"] = {**CFG["paths"], "cache_dir": str(tmp_path)}
    for cid, real in GT["t2"].items():
        _cache(tmp_path, "m", cid, real["transcripcion_referencia"])
    # L1 del clip 1: el ASR oye "un lomo saltado" como "dos lomos saltados" -> registro roto con WER muy bajo
    t1 = GT["t2"]["t2_01"]["transcripcion_referencia"].replace("un lomo saltado", "dos lomos saltados")
    _cache(tmp_path, "m", "t2_01__L1", t1)
    filas, faltantes = evaluar(cfg, "t2", "m", ["L0", "L1"])
    assert "t2_02__L1" in faltantes                           # no se inventa lo que no está en caché
    l0 = resumen_nivel([f for f in filas if f["nivel"] == "L0"], "t2", cfg)
    assert l0["registros_perfectos"] == 5 and l0["wer"] == 0
    l1 = [f for f in filas if f["nivel"] == "L1"]
    assert len(l1) == 1 and not l1[0]["registro_perfecto"]
    r = resumen_nivel(l1, "t2", cfg)
    assert r["registros_malos"] == 1 and r["atrapados_aritmetica"] == 1   # 40+60+16-10 = 106 ≠ 76 dicho
    assert l1[0]["diagnostico"] == "asr"
    c = contraste(filas)
    assert "t2_01@L1" in c["wer_bajo_registro_roto"] or "t2_01@L1" in c["wer_alto_registro_perfecto"] or c["mediana_wer"] >= 0


def test_snr_medida_y_determinismo():
    t = np.arange(16000 * 8) / 16000
    voz = (np.sin(2 * np.pi * 220 * t) * (np.sin(2 * np.pi * 0.5 * t) > 0) * 0.3).astype(np.float32)
    m1, snr = ladder.mezclar_snr(voz, 10, 0, 30)
    m2, _ = ladder.mezclar_snr(voz, 10, 0, 30)
    assert abs(snr - 10) < 0.1 and np.array_equal(m1, m2)


def test_gemini_rest_sin_red(monkeypatch):
    """El proveedor gemini llama por REST; se simula la respuesta y se comprueba que pasa por la verificación literal."""
    import io
    import urllib.request

    monkeypatch.setenv("GEMINI_API_KEY", "clave-falsa")
    visto = {}

    class R(io.BytesIO):
        def __enter__(self): return self
        def __exit__(self, *a): pass

    def falso(req, timeout=0):
        visto["clave"] = req.get_header("X-goog-api-key")
        cuerpo = {"candidates": [{"content": {"parts": [{"text": json.dumps({"pretension_salarial": 9999, "moneda": "PEN"})}]}}]}
        return R(json.dumps(cuerpo).encode())

    monkeypatch.setattr(urllib.request, "urlopen", falso)
    cfg = {**CFG, "extraction": {**CFG["extraction"], "llm_provider": "gemini", "llm_model": "gemini-x"}}
    ex = extraer("t1", "Mi pretensión es de seis mil quinientos soles.", cfg, "llm")
    assert visto["clave"] == "clave-falsa"
    assert ex["fields"]["pretension_salarial"] == cfg["extraction"]["unverified_label"]   # 9999 no está en el texto
