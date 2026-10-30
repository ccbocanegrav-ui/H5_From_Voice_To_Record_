"""Tarea 1 — extracción por REGLAS (expresiones regulares) del registro de la entrevista.

Cada función recibe el texto ya normalizado y devuelve el valor o None. Las heurísticas están pensadas para
los fallos que se esperan del audio: números dichos en palabras, autocorrecciones y distractores numéricos.
"""
from __future__ import annotations

import calendar
import re
from datetime import date, timedelta

from .util import contiene, norm, posiciones

MESES = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
         "septiembre": 9, "setiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12}

HEADS = {"analista", "desarrollador", "desarrolladora", "ingeniero", "ingeniera", "practicante", "diseñador",
         "diseñadora", "científico", "científica", "especialista", "gerente", "jefe", "jefa", "consultor",
         "consultora", "asistente", "coordinador", "coordinadora", "programador", "programadora", "arquitecto",
         "arquitecta", "administrador", "administradora", "contador", "contadora", "vendedor", "vendedora",
         "técnico", "técnica", "director", "directora", "supervisor", "supervisora", "pasante", "auditor",
         "auditora", "investigador", "investigadora", "operario", "operaria", "docente", "profesor", "profesora"}
EN_OK = {"especialista", "consultor", "consultora", "asistente", "experto", "experta", "coordinador", "coordinadora"}
STOP = {"en", "donde", "que", "para", "con", "y", "hasta", "sigo", "una", "un", "la", "el", "los", "las", "desde",
        "por", "cuando", "pero", "a", "al", "e", "o", "mientras", "cuya", "cuyo", "ahí"}
CUE_FUERTE = {"fui", "soy", "fue", "actualmente", "último", "puesto", "era"}      # "fui desarrollador", "mi último puesto fue"
CUE_DEBIL = {"como", "trabajo", "trabajaba"}
NO_ACTUAL = {"comencé", "empecé", "comence", "empece", "inicié", "inicie", "primeros", "pasé", "pase", "luego"}  # "comencé como practicante"

# ---------------------------------------------------------------------------------------------- años
_RE_ANIOS = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s+(años?|meses)(\s+y\s+medio)?")


def extraer_anios(t: str) -> float | None:
    mejor, mejor_score = None, 0
    for m in _RE_ANIOS.finditer(t):
        v = float(m.group(1))
        if m.group(2) == "meses":
            v = v / 12
        elif m.group(3):
            v += 0.5
        pre, post = t[max(0, m.start() - 75):m.start()], t[m.end():m.end() + 40]
        ctx = f"{pre} {m.group(0)} {post}"
        s = 0
        if "experiencia" in ctx:
            s += 3
        if re.search(r"\bllev(?:o|as|amos)\b", pre[-45:]):
            s += 2
        if re.search(r"cuántos años|cuánto tiempo|cuánta experiencia", pre):
            s += 2
        if re.search(r"\btengo\b", pre[-25:]):
            s += 1
        if pre.rstrip().endswith("hace") and re.search(r"trabaj|entr[eé]|empec|comenc", post):
            s += 2
        cerca = f"{pre[-35:]} {m.group(0)} {post[:30]}"
        if re.search(r"estudi|instituto|vivi|beca|canad[aá]|universidad|colegio|curso", cerca):
            s -= 4
        if s > mejor_score:
            mejor, mejor_score = round(v, 4), s
    return mejor


# ----------------------------------------------------------------------------------------- último puesto
def extraer_puesto(t: str) -> str | None:
    tokens = t.split()
    candidatos = [i for i, w in enumerate(tokens) if w in HEADS]
    if not candidatos:
        return None
    def puntaje(i: int) -> int:
        previos = set(tokens[max(0, i - 4):i])
        return 3 * bool(CUE_FUERTE & previos) + 1 * bool(CUE_DEBIL & previos) - 3 * bool(NO_ACTUAL & previos)

    i = max(candidatos, key=lambda k: (puntaje(k), -k))      # mayor puntaje; a igualdad, el primero
    palabras = [tokens[i]]
    j = i + 1
    while j < len(tokens) and len(palabras) < 5:
        w = tokens[j]
        if w == "en" and j == i + 1 and tokens[i] in EN_OK:
            palabras.append(w)
        elif w in STOP:
            break
        else:
            palabras.append(w)
        j += 1
    while palabras and palabras[-1] in {"de", "en", "del"}:
        palabras.pop()
    return " ".join(palabras)


# ------------------------------------------------------------------------------------------ tecnologías
_NEG_PRE = re.compile(r"aprend|quiero|me gustaría|estoy empezando|curso")
_NEG_POST = re.compile(r"no lo uso|todavía no|aún no|no la uso|no lo utilizo")


def extraer_tecnologias(t: str, cfg: dict) -> list[str]:
    """Busca el léxico de tecnologías. Descarta una tecnología si SOLO aparece como algo que se está aprendiendo
    o que aún no se usa (heurística de negación; las reglas no entienden el significado, el LLM sí)."""
    out = []
    for term in cfg["extraction"]["lexicon_tecnologias"]:
        tn = norm(term, cfg)
        pos = posiciones(t, tn)
        if not pos:
            continue
        validas = [p for p in pos
                   if not (_NEG_PRE.search(t[max(0, p - 50):p]) or _NEG_POST.search(t[p + len(tn):p + len(tn) + 70]))]
        if validas:
            out.append((min(validas), term))
    return [term for _, term in sorted(out)]


# --------------------------------------------------------------------------------------------- salario
_RE_MONTO = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s+(?:(?:por\s+)?mes\s+)?(soles|sol|dólares|dolares|dólar|usd)\b")
_CUE_SALARIO = re.compile(r"pretensi|ganar|alrededor|pensando|sueldo|salario|remuneraci|esperas|buscar[ií]a|pretendo|mensual")


def extraer_salario(t: str) -> tuple[float | None, str | None]:
    cands = []
    for m in _RE_MONTO.finditer(t):
        cue = bool(_CUE_SALARIO.search(t[max(0, m.start() - 90):m.end() + 40]))
        cands.append((cue, m.start(), float(m.group(1)), "USD" if m.group(2) in ("dólares", "dolares", "dólar", "usd") else "PEN"))
    if not cands:
        return None, None
    con_cue = [c for c in cands if c[0]]
    _, _, monto, moneda = (con_cue or cands)[-1]          # la ÚLTIMA mención gana: así se respeta la autocorrección
    return (int(monto) if monto == int(monto) else monto), moneda


# ------------------------------------------------------------------------------------------ disponibilidad
_RE_INMEDIATA = re.compile(r"de inmediato|inmediata|inmediatamente|desde ya|ya mismo|cuanto antes")
_RE_RELATIVA = re.compile(r"\b(?:en|dentro de)\s+(\d+)\s+(días|dias|día|dia|semanas|semana|meses|mes)\b")
_RE_ABSOLUTA = re.compile(r"\b(\d{1,2})\s+de\s+(" + "|".join(MESES) + r")\b")
_CUE_DISP = re.compile(r"empez|incorpor|disponib|podría|estaría|a partir|cuando podrías|desde cuándo")


def _sumar_meses(d: date, n: int) -> date:
    m = d.month - 1 + n
    y, m = d.year + m // 12, m % 12 + 1
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def fechas_en_texto(t: str, ref: date) -> list[tuple[int, str]]:
    """Todas las disponibilidades expresables en el texto: [(posición, 'inmediata' | 'AAAA-MM-DD')]."""
    out: list[tuple[int, str]] = []
    for m in _RE_INMEDIATA.finditer(t):
        out.append((m.start(), "inmediata"))
    for m in _RE_RELATIVA.finditer(t):
        n, u = int(m.group(1)), m.group(2)
        if u.startswith("d"):
            d = ref + timedelta(days=n)
        elif u.startswith("s"):
            d = ref + timedelta(weeks=n)
        else:
            d = _sumar_meses(ref, n)
        out.append((m.start(), d.isoformat()))
    for m in _RE_ABSOLUTA.finditer(t):
        dia, mes = int(m.group(1)), MESES[m.group(2)]
        for anio in (ref.year, ref.year + 1):             # la próxima vez que ocurre esa fecha
            try:
                d = date(anio, mes, dia)
            except ValueError:
                break
            if d >= ref:
                out.append((m.start(), d.isoformat()))
                break
    for m in re.finditer(r"\ba fin de mes\b|\bfinales de mes\b", t):
        out.append((m.start(), date(ref.year, ref.month, calendar.monthrange(ref.year, ref.month)[1]).isoformat()))
    return sorted(out)


def extraer_disponibilidad(t: str, ref: date) -> str | None:
    fs = fechas_en_texto(t, ref)
    if not fs:
        return None
    con_cue = [f for f in fs if _CUE_DISP.search(t[max(0, f[0] - 90):f[0] + 50])]
    return (con_cue or fs)[0][1]


# ------------------------------------------------------------------------------------------ nivel de inglés
def extraer_ingles(t: str, cfg: dict) -> str | None:
    sin = cfg["extraction"]["english_synonyms"]
    anclas = [m.start() for m in re.finditer(r"\bingl[eé]s\b", t)]
    encontrados = []
    for clase, sinonimos in sin.items():
        for s in sinonimos:
            for p in posiciones(t, norm(s, cfg)):
                dist = min((abs(p - a) for a in anclas), default=9999) if anclas else 9999
                encontrados.append((dist, p, clase))
    if not encontrados:
        return None
    cerca = [e for e in encontrados if e[0] <= 220] or encontrados
    return sorted(cerca)[0][2]


# ----------------------------------------------------------------------------------------------- todo
def extraer_t1(transcript: str, cfg: dict) -> dict:
    t = norm(transcript, cfg)
    ref = date.fromisoformat(cfg["extraction"]["reference_date"])
    monto, moneda = extraer_salario(t)
    return {
        "anios_experiencia": extraer_anios(t),
        "ultimo_puesto": extraer_puesto(t),
        "tecnologias": extraer_tecnologias(t, cfg) or None,
        "pretension_salarial": monto,
        "moneda": moneda,
        "disponibilidad": extraer_disponibilidad(t, ref),
        "nivel_ingles": extraer_ingles(t, cfg),
    }
