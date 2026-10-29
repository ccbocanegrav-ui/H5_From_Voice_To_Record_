import csv
from pathlib import Path

import pytest

from metrics import numeros, texto

ROOT = Path(__file__).resolve().parent.parent


@pytest.mark.parametrize("entrada,esperado", [
    ("seis mil quinientos soles", "6500 soles"),
    ("ciento cuarenta y ocho soles", "148 soles"),
    ("mil doscientos diez", "1210"),
    ("tres mil cuatrocientos veinte", "3420"),
    ("noventa y cuatro soles", "94 soles"),
    ("setenta y dos", "72"),
    ("ocho mil doscientos soles", "8200 soles"),
    ("once mil quinientos", "11500"),
    ("cuatro mil ochocientos", "4800"),
    ("cinco mil trescientos cincuenta", "5350"),
    ("mil ciento treinta", "1130"),
    ("novecientos dólares", "900 dólares"),
    ("dos tres", "2 3"),                       # no se suman números independientes
    ("cinco mil perdón cinco mil trescientos cincuenta", "5000 perdón 5350"),   # autocorrección
])
def test_palabras_a_digitos(entrada, esperado):
    assert texto.normalizar(entrada) == esperado


@pytest.mark.parametrize("hipotesis,referencia", [
    ("S/ 6,500", "seis mil quinientos soles"),
    ("S/6.500", "seis mil quinientos soles"),
    ("6500 soles", "seis mil quinientos soles"),
    ("$900", "novecientos dólares"),
    ("1,200 dólares", "mil doscientos dólares"),
    ("departamento 4B", "departamento cuatro B"),
    ("nivel C1", "nivel c uno"),
    ("el 1º de diciembre", "el primero de diciembre"),
    ("30 %", "treinta por ciento"),
    ("Avenida Brasil 1210.", "avenida brasil mil doscientos diez"),
    ("Power BI.", "power bi"),
])
def test_formatos_equivalentes(hipotesis, referencia):
    assert texto.normalizar(hipotesis) == texto.normalizar(referencia)


def test_decimales_se_conservan():
    assert texto.normalizar("3,5 años") == "3.5 años"


def test_wer_identico_es_cero_y_vacio_es_uno():
    t = texto.tasas("Hola, buenos días.", "hola buenos dias".replace("dias", "días"))
    assert t["wer"] == 0
    assert texto.tasas("hola mundo", "")["wer"] == 1


def test_wer_no_penaliza_formato_de_numeros():
    t = texto.tasas("Mi pretensión es de seis mil quinientos soles mensuales.",
                    "Mi pretensión es de S/ 6.500 mensuales.")
    assert t["wer"] == 0


def test_bootstrap_reproducible_y_ordenado():
    lo, hi = texto.bootstrap_ci([2, 3, 5, 1, 4], [100, 100, 120, 90, 110], n=500, seed=1)
    lo2, hi2 = texto.bootstrap_ci([2, 3, 5, 1, 4], [100, 100, 120, 90, 110], n=500, seed=1)
    assert (lo, hi) == (lo2, hi2) and 0 <= lo <= hi <= 1
    obs, a, b = texto.bootstrap_diff([5, 5], [100, 100], [2, 2], [100, 100], n=500)
    assert obs == pytest.approx(0.03) and a <= obs <= b


def test_glosario_recall():
    hits, total = texto.glosario_recall("Uso Python con pandas y Power BI", "uso pitón con pandas y power bi",
                                        ["Python", "pandas", "Power BI"])
    assert (hits, total) == (2, 3)


def _referencias():
    for nombre in ("t1_entrevistas.csv", "t2_llamadas.csv"):
        ruta = ROOT / "data" / "ground_truth" / nombre
        if ruta.exists():
            with open(ruta, encoding="utf-8") as f:
                for fila in csv.DictReader(f):
                    yield fila["clip_id"], fila["transcripcion_referencia"]


def test_ninguna_palabra_numerica_sobrevive_en_las_referencias():
    """Integridad: tras normalizar, las referencias del corpus no deben conservar números en palabras."""
    pendientes = {}
    for clip, ref in _referencias():
        sobrantes = [t for t in texto.normalizar(ref).split()
                     if numeros.sin_acentos(t) in numeros.PALABRAS_NUMERICAS]
        if sobrantes:
            pendientes[clip] = sorted(set(sobrantes))
    assert not pendientes, f"Palabras numéricas sin convertir: {pendientes}"
