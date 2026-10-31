# Evaluación T1 — extracción rules — ASR large-v3__cuda__float16__plano

## Capa de texto y capa de registro por nivel

| Nivel | Clips | WER (IC95) | CER | Campos correctos | Registros perfectos |
|---|---|---|---|---|---|
| L0 | 5 | 3.1 % (2.0 %–4.2 %) | 1.5 % | 25/30 | 1/5 |
| L1 | 5 | 3.2 % (2.3 %–4.0 %) | 1.5 % | 27/30 | 2/5 |
| L2 | 5 | 3.1 % (2.1 %–4.1 %) | 1.4 % | 26/30 | 2/5 |
| L3 | 5 | 3.5 % (2.4 %–4.5 %) | 1.6 % | 28/30 | 3/5 |

## Exactitud por campo — L0

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| anios_experiencia | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |
| ultimo_puesto | 2/5 | 40.0 % (11.8 %–76.9 %) | 0 |  |
| tecnologias | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| pretension_salarial | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 | error abs. medio 120.00 |
| disponibilidad | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| nivel_ingles | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | F1 macro 1.00 |

## Exactitud por campo — L1

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| anios_experiencia | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |
| ultimo_puesto | 3/5 | 60.0 % (23.1 %–88.2 %) | 0 |  |
| tecnologias | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| pretension_salarial | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 | error abs. medio 120.00 |
| disponibilidad | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| nivel_ingles | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | F1 macro 1.00 |

## Exactitud por campo — L2

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| anios_experiencia | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |
| ultimo_puesto | 2/5 | 40.0 % (11.8 %–76.9 %) | 0 |  |
| tecnologias | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| pretension_salarial | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 | error abs. medio 120.00 |
| disponibilidad | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| nivel_ingles | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | F1 macro 1.00 |

## Exactitud por campo — L3

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| anios_experiencia | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |
| ultimo_puesto | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| tecnologias | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| pretension_salarial | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 | error abs. medio 120.00 |
| disponibilidad | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| nivel_ingles | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | F1 macro 1.00 |

## WER vs calidad del registro

- WER alto (≥ mediana 3.1 %) pero registro perfecto: —
- WER bajo pero registro con errores: t1_02, t1_05
