"""Evaluación de las DOS capas sobre transcripciones en caché: texto (WER/CER) y registro (campos).

Lee data/cache/asr/<config>/<clip>.json. Para la escalera, el clip se llama `t2_01__L1` etc.
"""
from __future__ import annotations

from pathlib import Path

from engine import cache
from engine.config import resolver_ruta
from extraction import extraer
from metrics import registro as mr
from metrics import texto as mt
from validation import diagnostico, validar


def transcripcion_en_cache(cfg: dict, nombre_cfg: str, clip: str) -> str | None:
    p = resolver_ruta(cfg, cfg["paths"]["cache_dir"]) / "asr" / nombre_cfg / f"{clip}.json"
    return cache.leer(p)["texto"] if p.exists() else None


def evaluar_clip(cfg: dict, schema: str, clip: str, nivel: str, texto_asr: str, real: dict, metodo: str | None,
                 cliente_llm=None) -> dict:
    t = mt.tasas(real["transcripcion_referencia"], texto_asr, cfg["normalization"])
    ex = extraer(schema, texto_asr, cfg, metodo, cliente_llm)
    comp = mr.comparar_registro(schema, ex["fields"], real, cfg)
    mal = [c for c, v in comp.items() if not v["ok"]]
    items = ex["fields"].get("items")
    items_sin_verif = sum(not i.get("verificado", True) for i in items) if isinstance(items, list) else 0
    fila = {"clip": clip, "nivel": nivel, "wer": t["wer"], "cer": t["cer"], "w_err": t["w_err"], "w_ref": t["w_ref"],
            "campos_total": len(comp), "campos_ok": len(comp) - len(mal), "campos_mal": mal,
            "registro_perfecto": not mal, "sin_verificar": sum(v["sin_verificar"] for v in comp.values()) + items_sin_verif,
            "comparacion": comp}
    if schema == "t2":
        f = ex["fields"]
        va = validar(f["items"], f["promocion"], f["total_dicho"], cfg)
        vr = validar(real["items"], real["promocion"], real["total_dicho"], cfg)
        fila.update(val_estado=va["estado"], val_ref_estado=vr["estado"], diagnostico=diagnostico(va, vr),
                    total_calculado=va["total_calculado"])
    return fila


def evaluar(cfg: dict, schema: str, config_cache: str, niveles: list[str], metodo: str | None = None,
            cliente_llm=None) -> tuple[list[dict], list[str]]:
    """Devuelve (filas, faltantes). Un clip sin transcripción en caché no se inventa: se lista como faltante."""
    gt = mr.cargar_gt(schema, resolver_ruta(cfg, cfg["paths"][f"ground_truth_{schema}"]))
    filas, faltantes = [], []
    for nivel in niveles:
        for clip, real in gt.items():
            nombre = clip if nivel == "L0" else f"{clip}__{nivel}"
            txt = transcripcion_en_cache(cfg, config_cache, nombre)
            if txt is None:
                faltantes.append(nombre)
                continue
            filas.append(evaluar_clip(cfg, schema, clip, nivel, txt, real, metodo, cliente_llm))
    return filas, faltantes


def resumen_nivel(filas: list[dict], schema: str, cfg: dict) -> dict:
    wer_ci = mt.bootstrap_ci([f["w_err"] for f in filas], [f["w_ref"] for f in filas])
    r = {"n_clips": len(filas),
         "wer": mt.agregado([f["w_err"] for f in filas], [f["w_ref"] for f in filas]), "wer_ic": wer_ci,
         "cer": float(sum(f["cer"] for f in filas) / len(filas)),
         "campos_ok": sum(f["campos_ok"] for f in filas), "campos_total": sum(f["campos_total"] for f in filas),
         "registros_perfectos": sum(f["registro_perfecto"] for f in filas),
         "por_campo": mr.agregar(schema, [f["comparacion"] for f in filas], cfg)}
    if schema == "t2":
        malos = [f for f in filas if not f["registro_perfecto"]]
        r["registros_malos"] = len(malos)
        r["atrapados_aritmetica"] = sum(f["val_estado"] == "inconsistente" for f in malos)
        r["atrapados_verificacion"] = sum(f["sin_verificar"] > 0 for f in malos)
        r["atrapados_alguna"] = sum(f["val_estado"] == "inconsistente" or f["sin_verificar"] > 0 for f in malos)
        r["perdidos"] = len(malos) - r["atrapados_alguna"]
        r["diagnosticos"] = {k: sum(f["diagnostico"] == k for f in filas) for k in ("ok", "asr", "hablante", "no_calculable")}
    return r


def contraste(filas: list[dict]) -> dict:
    """Clips donde WER y calidad del registro dicen cosas distintas (WER alto + registro perfecto, y al revés)."""
    if not filas:
        return {"wer_alto_registro_perfecto": [], "wer_bajo_registro_roto": []}
    ords = sorted(f["wer"] for f in filas)
    mediana = ords[len(ords) // 2]
    return {"mediana_wer": mediana,
            "wer_alto_registro_perfecto": [f["clip"] + ("" if f["nivel"] == "L0" else "@" + f["nivel"])
                                           for f in filas if f["wer"] >= mediana and f["registro_perfecto"]],
            "wer_bajo_registro_roto": [f["clip"] + ("" if f["nivel"] == "L0" else "@" + f["nivel"])
                                       for f in filas if f["wer"] < mediana and not f["registro_perfecto"]]}
