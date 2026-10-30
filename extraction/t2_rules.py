"""Tarea 2 — extracción por REGLAS del registro de una llamada de venta (restaurante).

La parte difícil es el pedido: el registro debe guardar el pedido FINAL cuando el cliente se corrige.
Algoritmo de ítems (ver README): se recorren las menciones de producto con cantidad, en orden; una mención
posterior sustituye a la anterior del mismo producto, y si hay una señal de corrección ("espera", "perdón",
"mejor"...) cerca, se descartan antes todas las entradas previas de ese producto.
"""
from __future__ import annotations

import re

from .util import contiene, norm, plural

SIZE_EXTRA = {"1.5 litros": ["litro y medio", "1.5 litros", "1.5 litro"]}     # cómo se dice hablado
PRE_CANTIDAD = {"medio", "cuarto", "entero"}                                 # tamaños que implican cantidad 1
PRE_TAMANOS = ("medio", "cuarto", "entero", "jarra", "vaso")


def _rx_palabra(w: str) -> str:
    return plural(w) if len(w) > 3 else re.escape(w)


def _rx_alias(alias: str, cfg: dict) -> str:
    return r"\s+".join(_rx_palabra(w) for w in norm(alias, cfg).split())


def _variantes_tamano(tam: str, cfg: dict) -> list[str]:
    v = [norm(tam, cfg)] + [norm(x, cfg) for x in SIZE_EXTRA.get(tam, [])]
    return v + [x + ("s" if x[-1] in "aeiou" else "es") for x in v]


def _menu(cfg: dict) -> list[dict]:
    out = []
    for p in cfg["extraction"]["t2"]["menu"]:
        tams = {str(k): v for k, v in p["tamanos"].items()}
        out.append({"producto": p["producto"], "alias": p["alias"], "tamanos": tams,
                    "unico": list(tams) == ["unico"]})
    return out


def _tamano_en(texto: str, tamanos: dict, cfg: dict) -> str | None:
    """Busca en `texto` (normalizado) alguno de los tamaños válidos del producto."""
    mejor = None
    for tam in tamanos:
        if tam == "unico":
            continue
        for v in _variantes_tamano(tam, cfg):
            m = re.search(rf"(?<!\S){re.escape(v)}(?!\S)", texto)
            if m and (mejor is None or m.start() < mejor[0]):
                mejor = (m.start(), tam)
    return mejor[1] if mejor else None


def _tamanos_previos(menu: list[dict], cfg: dict) -> list[str]:
    """Palabras de tamaño que pueden ir ANTES del producto: las de la carta (jarra, vaso, porción…) + medio/cuarto/entero."""
    uni = {norm(k, cfg) for p in menu for k in p["tamanos"] if k != "unico" and " " not in norm(k, cfg)}
    return sorted(uni | PRE_CANTIDAD, key=len, reverse=True)


def _rx_previo(menu: list[dict], cfg: dict) -> re.Pattern:
    alt = "|".join(plural(w) for w in _tamanos_previos(menu, cfg))
    return re.compile(rf"(?:(?P<q>\d+)\s+)?(?:(?:solo|sola)\s+)?(?:(?P<s>{alt})\s+(?:de\s+)?)?$")


def extraer_items(t: str, cfg: dict) -> list[dict]:
    menu = _menu(cfg)
    cues = [norm(c, cfg) for c in cfg["extraction"]["t2"]["correcciones"]]
    cue_pos = sorted(m.start() for c in cues for m in re.finditer(rf"(?<!\S){re.escape(c)}(?!\S)", t))

    alt = []
    for i, p in enumerate(menu):
        for a in p["alias"]:
            alt.append((len(a), i, _rx_alias(a, cfg)))
    alt.sort(reverse=True)                                           # alias largos primero
    rx = re.compile(r"(?<!\S)(?:" + "|".join(f"(?P<p{i}_{k}>{r})" for k, (_, i, r) in enumerate(alt)) + r")(?!\S)")

    rx_previo = _rx_previo(menu, cfg)
    bases_previas = _tamanos_previos(menu, cfg)
    entradas: list[dict] = []
    limpiados: set[tuple[str, int]] = set()
    for m in rx.finditer(t):
        idx = next(alt[k][1] for k in range(len(alt)) if m.group(f"p{alt[k][1]}_{k}") is not None)
        prod = menu[idx]
        pre = rx_previo.search(t[:m.start()])
        qty = int(pre.group("q")) if pre.group("q") else None
        if qty is not None and re.search(r"\bpor\s*$", t[:pre.start("q")]):
            continue                                                  # "dos por 1 chicha": la promo "2 por 1", no una cantidad
        pre_size = next((w for w in bases_previas if pre.group("s") and re.fullmatch(plural(w), pre.group("s"))), None)
        if qty is None and pre_size not in PRE_CANTIDAD:
            continue                                                  # mención sin cantidad ("el pollo viene con…")
        qty = qty or 1
        tam = None
        if pre_size and pre_size in {norm(k, cfg) for k in prod["tamanos"]}:
            tam = pre_size
        if tam is None:
            post = " ".join(t[m.end():].split()[:6])
            tam = _tamano_en(post, prod["tamanos"], cfg)
        elif tam not in prod["tamanos"]:
            tam = next((k for k in prod["tamanos"] if norm(k, cfg) == tam), None)
        if prod["unico"]:
            tam = None
        ult = max((c for c in cue_pos if c < m.start() and m.start() - c <= 160), default=None)
        if ult is not None and (prod["producto"], ult) not in limpiados:
            entradas = [e for e in entradas if e["producto"] != prod["producto"]]
            limpiados.add((prod["producto"], ult))
        if tam is None and not prod["unico"]:
            previos = [e for e in entradas if e["producto"] == prod["producto"]]
            if len(previos) == 1:
                tam = previos[0]["tamano"]                            # "4 chichas" hereda "vaso" de la mención anterior
        for e in entradas:
            if e["producto"] == prod["producto"] and e["tamano"] == tam:
                e["cantidad"] = qty
                break
        else:
            entradas.append({"producto": prod["producto"], "tamano": tam, "cantidad": qty})

    for e in entradas:
        p = next(x for x in menu if x["producto"] == e["producto"])
        clave = "unico" if p["unico"] else e["tamano"]
        e["precio_unitario"] = p["tamanos"].get(clave)
    return entradas


# -------------------------------------------------------------------------------------------- promoción
_NEG_PROMO = re.compile(r"no aplica|no califica|no hay promoci|no tenemos promoci|ninguna promoci")


def extraer_promocion(t: str, cfg: dict) -> str | None:
    encontradas = []
    for p in cfg["extraction"]["t2"]["promos"]:
        for pat in p["patrones"]:
            pn = norm(pat, cfg)
            for m in re.finditer(rf"(?<!\S){re.escape(pn)}(?!\S)", t):
                ventana = t[max(0, m.start() - 90):m.end() + 110]
                if _NEG_PROMO.search(ventana):
                    continue
                conf = bool(re.search(r"califica|aplica|entonces|gratis|su pedido|me sale|al precio", t[m.end():m.end() + 140]))
                encontradas.append((not conf, m.start(), p["etiqueta"]))
    return sorted(encontradas)[0][2] if encontradas else None


# --------------------------------------------------------------------------------------------- dirección
UNIDADES = {"interior", "departamento", "dpto", "piso", "int"}


def _unidad(resto: list[str], i: int) -> tuple[list[str], int]:
    """Lee 'interior 3', 'departamento 4 b', 'piso 4' desde resto[i]. Devuelve (palabras, nuevo_i)."""
    out: list[str] = []
    while i + 1 < len(resto) and resto[i] in UNIDADES and resto[i + 1].isdigit():
        out += [resto[i], resto[i + 1]]
        i += 2
        if i < len(resto) and re.fullmatch(r"[a-f]", resto[i]):
            out.append(resto[i])
            i += 1
    return out, i


def extraer_direccion(t: str, cfg: dict) -> str | None:
    """Prefijo de calle + nombre + número [+ unidad] [+ distrito]. Se exige distrito o unidad después del número:
    sin eso, "dejar el auto en la calle. Genial, gracias. Una cosa…" se leería como una dirección."""
    c2 = cfg["extraction"]["t2"]
    pref = "|".join(re.escape(norm(p, cfg)) for p in c2["prefijos_calle"])
    distritos = sorted((norm(d, cfg) for d in cfg["extraction"]["distritos"]), key=len, reverse=True)
    rx = re.compile(rf"(?<!\S)({pref})\s+((?:[^\W\d_]+\s+){{0,4}}?)(\d+)(?!\S*\d)")
    for m in rx.finditer(t):
        partes = [m.group(1)] + m.group(2).split() + [m.group(3)]
        resto = t[m.end():].split()
        unidad, i = _unidad(resto, 0)
        partes += unidad
        if i < len(resto) and resto[i] == "en":
            i += 1
        distrito = None
        for salto in (0, 1) if i < len(resto) and resto[i] in {"el", "la"} else (0,):
            cola = " ".join(resto[i + salto:i + salto + 5])
            distrito = next((d for d in distritos if cola.startswith(d + " ") or cola == d), None)
            if distrito:
                i += salto + len(distrito.split())
                break
        if distrito is None and not unidad:
            continue                                                  # ni distrito ni unidad: no parece una dirección
        if distrito:
            partes.append(distrito)
        u2, _ = _unidad(resto, i + next((k for k, w in enumerate(resto[i:i + 6]) if w in UNIDADES), 99))
        if u2 and not unidad:
            partes += u2                                              # "…Los Olivos, edificio de oficinas, piso 4"
        return " ".join(partes)
    return None


def hay_recojo(t: str, cfg: dict) -> bool:
    return any(contiene(t, norm(r, cfg)) for r in cfg["extraction"]["t2"]["recojo"])


# -------------------------------------------------------------------------------------------- método de pago
def extraer_pago(t: str, cfg: dict) -> str | None:
    pagos = {k: [norm(s, cfg) for s in v] for k, v in cfg["extraction"]["t2"]["pagos"].items()}
    menciones = []
    for metodo, sins in pagos.items():
        for s in sins:
            for m in re.finditer(rf"(?<!\S){re.escape(s)}(?!\S)", t):
                menciones.append((m.start(), metodo))
    menciones.sort()
    # "Aceptamos efectivo, tarjeta y Yape" es una LISTA de opciones (unidas solo por "y"/"o"), no la respuesta: se ignora.
    # "…y Yape. En efectivo…" NO es lista: entre ambas hay otra palabra ("en").
    grupos: list[list[tuple[int, str]]] = []
    for pos_m, met in menciones:
        if grupos:
            ult = grupos[-1][-1]
            medio = t[ult[0]:pos_m].split()[1:]          # palabras entre la mención anterior y esta
            if all(w in {"y", "o", "e"} for w in medio) and len(medio) <= 2:
                grupos[-1].append((pos_m, met))
                continue
        grupos.append([(pos_m, met)])
    validas = [g_item for g in grupos if len({m for _, m in g}) < 2 for g_item in g]
    if not validas:
        return None
    cue = re.search(r"pag(?:o|ar|ará|aré|ar[eé]|ará)|forma de pago|cómo desea|cómo va", t)
    despues = [v for v in validas if cue and v[0] >= cue.start()]
    return (despues or validas)[0][1]


# ---------------------------------------------------------------------------------------------- total
_RE_SOLES = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s+soles\b")


def extraer_total(t: str) -> float | None:
    cands = []
    for m in _RE_SOLES.finditer(t):
        v = float(m.group(1))
        cue = "total" in t[max(0, m.start() - 30):m.start()] or "total" in t[m.end():m.end() + 14]
        cands.append((cue, v))
    if not cands:
        return None
    con = [v for c, v in cands if c]
    v = (con or [cands[-1][1]])[-1]
    return int(v) if v == int(v) else v


def extraer_t2(transcript: str, cfg: dict) -> dict:
    t = norm(transcript, cfg)
    direccion = extraer_direccion(t, cfg)
    if direccion is None and hay_recojo(t, cfg):
        direccion = "recojo en tienda"
    return {
        "items": extraer_items(t, cfg) or None,
        "promocion": extraer_promocion(t, cfg),
        "direccion_entrega": direccion,
        "metodo_pago": extraer_pago(t, cfg),
        "total_dicho": extraer_total(t),
    }
