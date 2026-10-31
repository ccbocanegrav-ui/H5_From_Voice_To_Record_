# Evaluación T2 — extracción rules — ASR large-v3__cuda__float16__plano

## Capa de texto y capa de registro por nivel

| Nivel | Clips | WER (IC95) | CER | Campos correctos | Registros perfectos |
|---|---|---|---|---|---|
| L0 | 5 | 5.1 % (4.2 %–6.1 %) | 2.7 % | 24/25 | 4/5 |
| L1 | 5 | 5.7 % (4.8 %–7.0 %) | 3.0 % | 24/25 | 4/5 |
| L2 | 5 | 5.4 % (4.5 %–6.5 %) | 2.7 % | 22/25 | 2/5 |
| L3 | 5 | 6.5 % (5.0 %–7.9 %) | 3.4 % | 24/25 | 4/5 |

## Exactitud por campo — L0

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| items | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| promocion | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| direccion_entrega | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| metodo_pago | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| total_dicho | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |

## Exactitud por campo — L1

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| items | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| promocion | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| direccion_entrega | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| metodo_pago | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| total_dicho | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |

## Exactitud por campo — L2

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| items | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| promocion | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| direccion_entrega | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| metodo_pago | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| total_dicho | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |

## Exactitud por campo — L3

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| items | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| promocion | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| direccion_entrega | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| metodo_pago | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| total_dicho | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |

## Validadores: registros malos atrapados vs perdidos

| Nivel | Registros malos | Atrapados por aritmética | Atrapados por verificación literal | Atrapados (alguna) | Perdidos | Diagnóstico (ok/asr/hablante) |
|---|---|---|---|---|---|---|
| L0 | 1 | 1 | 0 | 1 | 0 | 2/0/3 |
| L1 | 1 | 1 | 0 | 1 | 0 | 2/0/3 |
| L2 | 3 | 1 | 1 | 2 | 1 | 2/0/3 |
| L3 | 1 | 1 | 0 | 1 | 0 | 2/0/3 |

## WER vs calidad del registro

- WER alto (≥ mediana 5.3 %) pero registro perfecto: t2_03, t2_04, t2_03@L1, t2_04@L1, t2_04@L2, t2_03@L3, t2_04@L3
- WER bajo pero registro con errores: t2_02, t2_02@L1, t2_05@L2
