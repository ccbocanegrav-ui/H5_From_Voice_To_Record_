"""Verificación literal: TODO valor extraído debe existir en la transcripción; si no, queda `sin_verificar`.

La verificación es independiente de quién extrajo el valor (reglas o LLM): mira el valor y la transcripción,
nada más. "seis mil quinientos" en el texto verifica 6500 porque ambos pasan por la misma normalización
(metrics/numeros.py); sin esa capa, 6500 jamás aparecería "literalmente" en un texto hablado.

Reglas por campo:
  texto (puesto, dirección)  -> la frase normalizada está en el texto
  lista (tecnologías)        -> cada elemento está en el texto; los que no, se descartan y se avisa
  número (salario, total)    -> el número, como dígitos, es un token del texto
  años                       -> "N años" / "N años y medio" / "N meses" está en el texto
  disponibilidad             -> 'inmediata' o una fecha que se obtiene de una expresión que SÍ está en el texto
  categórico (nivel_ingles)  -> alguno de sus sinónimos está en el texto
"""
from __future__ import annotations

from datetime import date

from .t1_rules import fechas_en_texto
from .t2_rules import _menu, _rx_alias
from .util import contiene, norm

import re


def verificar_anios(t: str, v) -> bool:
    if v is None:
        return False
    v = float(v)
    formas = []
    if v == int(v):
        formas += [f"{int(v)} años", f"{int(v)} año"]
    if (v * 2) == int(v * 2) and v != int(v):
        formas += [f"{int(v)} años y medio", f"{int(v)} año y medio"]
    m = round(v * 12)
    if abs(v * 12 - m) < 0.05 and m < 24:
        formas += [f"{m} meses", f"{m} mes"]
    return any(contiene(t, f) for f in formas)


def verificar_t1(campo: str, valor, t: str, cfg: dict):
    """Devuelve (verificado: bool, valor_conservado). Para listas, conserva solo lo verificado."""
    if valor is None or valor == "" or valor == []:
        return False, valor
    if campo == "ultimo_puesto":
        return contiene(t, norm(str(valor), cfg)), valor
    if campo == "tecnologias":
        buenos = [x for x in valor if contiene(t, norm(str(x), cfg))]
        return len(buenos) == len(valor), buenos
    if campo == "pretension_salarial":
        return contiene(t, str(int(valor)) if float(valor) == int(valor) else str(valor)), valor
    if campo == "anios_experiencia":
        return verificar_anios(t, valor), valor
    if campo == "disponibilidad":
        ref = date.fromisoformat(cfg["extraction"]["reference_date"])
        return str(valor) in {f for _, f in fechas_en_texto(t, ref)}, valor
    if campo == "nivel_ingles":
        sin = cfg["extraction"]["english_synonyms"].get(str(valor), [])
        return any(contiene(t, norm(s, cfg)) for s in sin), valor
    return False, valor


def verificar_item(item: dict, t: str, cfg: dict) -> bool:
    """Un ítem se verifica si su producto Y su precio unitario aparecen literalmente en la transcripción."""
    prod = next((p for p in _menu(cfg) if norm(p["producto"], cfg) == norm(str(item.get("producto", "")), cfg)), None)
    if prod is None or item.get("precio_unitario") is None:
        return False
    esta = any(re.search(rf"(?<!\S){_rx_alias(a, cfg)}(?!\S)", t) for a in prod["alias"])
    p = item["precio_unitario"]
    return esta and contiene(t, str(int(p)) if float(p) == int(p) else str(p))


def verificar_t2(campo: str, valor, t: str, cfg: dict):
    if campo == "promocion":
        return True, valor                                    # None = "no se aplicó promoción": nada que verificar
    if valor is None or valor == "" or valor == []:
        return False, valor
    if campo == "items":
        marcados = [{**i, "verificado": verificar_item(i, t, cfg)} for i in valor]
        return all(i["verificado"] for i in marcados), marcados
    if campo == "direccion_entrega":
        if norm(str(valor), cfg) == "recojo en tienda":
            return any(contiene(t, norm(r, cfg)) for r in cfg["extraction"]["t2"]["recojo"]), valor
        toks = set(t.split())
        return all(w in toks for w in norm(str(valor), cfg).split()), valor
    if campo == "metodo_pago":
        sins = cfg["extraction"]["t2"]["pagos"].get(str(valor), [])
        return any(contiene(t, norm(s, cfg)) for s in sins), valor
    if campo == "total_dicho":
        return contiene(t, str(int(valor)) if float(valor) == int(valor) else str(valor)), valor
    if campo == "promocion":
        return True, valor
    return False, valor
