# Evaluación T1 — extracción rules — ASR large-v3__cuda__float16__plano

## Capa de texto y capa de registro por nivel

| Nivel | Clips | WER (IC95) | CER | Campos correctos | Registros perfectos |
|---|---|---|---|---|---|
| L0 | 5 | 3.1 % (2.0 %–4.2 %) | 1.5 % | 25/30 | 1/5 |

## Exactitud por campo — L0

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| anios_experiencia | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |
| ultimo_puesto | 2/5 | 40.0 % (11.8 %–76.9 %) | 0 |  |
| tecnologias | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| pretension_salarial | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 | error abs. medio 120.00 |
| disponibilidad | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| nivel_ingles | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | F1 macro 1.00 |

## WER vs calidad del registro

- WER alto (≥ mediana 3.0 %) pero registro perfecto: —
- WER bajo pero registro con errores: t1_05
