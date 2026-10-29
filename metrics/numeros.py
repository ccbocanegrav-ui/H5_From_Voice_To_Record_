"""Números hablados en español -> dígitos.

Problema que resuelve (específico del audio): el guion dice "seis mil quinientos" y Whisper puede
escribir "6500", "6.500" o "seis mil quinientos". Sin normalizar, el WER lo cuenta como error y la
verificación literal de la Fase 3 falla aunque todo esté bien.

Reglas (documentadas para el README):
  1. Un número hablado es una secuencia [centena] [decena [y unidad] | especial | unidad] con "mil"
     y "millón" como multiplicadores. "ciento cuarenta y ocho" -> 148; "mil doscientos diez" -> 1210.
  2. "y" solo se consume entre una decena (30-90) y una unidad (1-9): "treinta y cinco".
  3. Dos números seguidos NO se suman: "dos tres" -> 2 3 (cada número se lee por separado).
  4. "un/uno/una" se convierten en 1 en ambos textos que se comparan (referencia e hipótesis), por lo
     que el efecto sobre el WER es simétrico.
"""
from __future__ import annotations

import unicodedata


def sin_acentos(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


UNIDADES = {"cero": 0, "un": 1, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9}
ESPECIALES = {"diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
              "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
              "veintiun": 21, "veintiuno": 21, "veintiuna": 21, "veintidos": 22, "veintitres": 23,
              "veinticuatro": 24, "veinticinco": 25, "veintiseis": 26, "veintisiete": 27,
              "veintiocho": 28, "veintinueve": 29}
DECENAS = {"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
           "ochenta": 80, "noventa": 90}
CENTENAS = {"cien": 100, "ciento": 100, "doscientos": 200, "doscientas": 200, "trescientos": 300,
            "trescientas": 300, "cuatrocientos": 400, "cuatrocientas": 400, "quinientos": 500,
            "quinientas": 500, "seiscientos": 600, "seiscientas": 600, "setecientos": 700,
            "setecientas": 700, "ochocientos": 800, "ochocientas": 800, "novecientos": 900,
            "novecientas": 900}
MILLONES = {"millon", "millones"}

# Todas las palabras que el normalizador debe convertir (sin acentos). Útil para tests de integridad.
PALABRAS_NUMERICAS = (set(UNIDADES) | set(ESPECIALES) | set(DECENAS) | set(CENTENAS)
                      | MILLONES | {"mil"})


def _clasificar(token: str) -> tuple[str | None, int]:
    t = sin_acentos(token.lower())
    if t in UNIDADES:
        return "u", UNIDADES[t]
    if t in ESPECIALES:
        return "e", ESPECIALES[t]
    if t in DECENAS:
        return "d", DECENAS[t]
    if t in CENTENAS:
        return "c", CENTENAS[t]
    if t == "mil":
        return "mil", 1000
    if t in MILLONES:
        return "mill", 1_000_000
    return None, 0


def leer_numero(tokens: list[str], i: int) -> tuple[int, int] | None:
    """Lee un número hablado desde tokens[i]. Devuelve (valor, siguiente_indice) o None."""
    total = 0
    bloque = 0
    estado = "ini"          # ini | c (centena) | d (decena) | dy (decena + 'y') | fin
    visto_mil = False
    j = i
    n = len(tokens)
    while j < n:
        tipo, val = _clasificar(tokens[j])
        if tipo == "c" and estado == "ini":
            bloque += val
            estado = "c"
        elif tipo == "e" and estado in ("ini", "c"):
            bloque += val
            estado = "fin"
        elif tipo == "d" and estado in ("ini", "c"):
            bloque += val
            estado = "d"
        elif tipo == "u" and estado in ("ini", "c", "dy"):
            bloque += val
            estado = "fin"
        elif (tokens[j] == "y" and estado == "d" and j + 1 < n
              and _clasificar(tokens[j + 1])[0] == "u" and _clasificar(tokens[j + 1])[1] >= 1):
            estado = "dy"
            j += 1
            continue
        elif tipo == "mil" and not visto_mil and estado != "dy":
            total += (bloque or 1) * 1000
            bloque = 0
            estado = "ini"
            visto_mil = True
        elif tipo == "mill" and estado != "dy":
            total = ((total + bloque) or 1) * 1_000_000
            bloque = 0
            estado = "ini"
            visto_mil = False
        else:
            break
        j += 1
    if j == i:
        return None
    return total + bloque, j


def palabras_a_digitos(tokens: list[str]) -> list[str]:
    """Reemplaza cada secuencia de palabras numéricas por su valor en dígitos."""
    out: list[str] = []
    i = 0
    while i < len(tokens):
        r = leer_numero(tokens, i)
        if r is None:
            out.append(tokens[i])
            i += 1
        else:
            valor, j = r
            out.append(str(valor))
            i = j
    return out
