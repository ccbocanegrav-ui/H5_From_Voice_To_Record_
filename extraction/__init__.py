"""Extracción de campos (reglas o LLM) + verificación literal. Punto de entrada: extraer()."""
from __future__ import annotations

from typing import Any

from .llm import extraer_llm
from .t1_rules import extraer_t1
from .t2_rules import extraer_t2
from .util import norm
from .verificar import verificar_t1, verificar_t2


def _limpiar_llm(schema: str, d: dict) -> dict:
    """Pasa lo que devuelve el LLM a los mismos tipos que usan las reglas."""
    def num(x):
        try:
            return None if x is None else (int(float(x)) if float(x) == int(float(x)) else float(x))
        except (TypeError, ValueError):
            return None

    if schema == "t1":
        return {"anios_experiencia": num(d.get("anios_experiencia")), "ultimo_puesto": d.get("ultimo_puesto"),
                "tecnologias": d.get("tecnologias") or None, "pretension_salarial": num(d.get("pretension_salarial")),
                "moneda": d.get("moneda"), "disponibilidad": d.get("disponibilidad"), "nivel_ingles": d.get("nivel_ingles")}
    items = d.get("items") or []
    return {"items": [{"producto": i.get("producto"), "tamano": i.get("tamano"), "cantidad": num(i.get("cantidad")),
                       "precio_unitario": num(i.get("precio_unitario"))} for i in items] or None,
            "promocion": d.get("promocion"), "direccion_entrega": d.get("direccion_entrega"),
            "metodo_pago": d.get("metodo_pago"), "total_dicho": num(d.get("total_dicho"))}


def extraer(schema: str, transcript: str, cfg: dict, metodo: str | None = None, cliente_llm: Any = None) -> dict:
    """Devuelve {fields, candidatos, verified, metodo, error}.

    candidatos: lo que se propuso (antes de verificar). fields: lo que queda en el registro: cada valor verificado,
    o la etiqueta `sin_verificar` (config: extraction.unverified_label) si no existe literalmente en la transcripción.
    verified: campo -> bool.
    """
    ex = cfg["extraction"]
    metodo = metodo or ex["method"]
    etiqueta = ex["unverified_label"]
    t = norm(transcript, cfg)
    if metodo == "llm":
        cand = _limpiar_llm(schema, extraer_llm(schema, transcript, cfg, cliente_llm))
    elif metodo == "rules":
        cand = extraer_t1(transcript, cfg) if schema == "t1" else extraer_t2(transcript, cfg)
    else:
        raise ValueError(f"método de extracción desconocido: {metodo!r}")

    campos = cfg["schemas"][schema]
    ver = verificar_t1 if schema == "t1" else verificar_t2
    fields: dict[str, Any] = {}
    verified: dict[str, bool] = {}
    for c in campos:
        ok, valor = ver(c, cand.get(c), t, cfg)
        verified[c] = bool(ok)
        if cand.get(c) is None and c != "promocion":
            fields[c] = None                                   # no apareció: "sin dato", no "sin verificar"
        elif c in ("tecnologias", "items"):
            fields[c] = valor if valor else etiqueta
        else:
            fields[c] = valor if ok else etiqueta
    if schema == "t1":
        fields["moneda"] = cand.get("moneda") if verified["pretension_salarial"] else None
    return {"fields": fields, "candidatos": cand, "verified": verified, "metodo": metodo}
