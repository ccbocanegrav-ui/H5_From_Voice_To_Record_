# Evaluación T2 — extracción llm — ASR large-v3__cuda__float16__plano

## Capa de texto y capa de registro por nivel

| Nivel | Clips | WER (IC95) | CER | Campos correctos | Registros perfectos |
|---|---|---|---|---|---|
| L0 | 5 | 5.1 % (4.2 %–6.1 %) | 2.7 % | 16/25 | 0/5 |

## Exactitud por campo — L0

| Campo | Aciertos | Exactitud (Wilson 95 %) | sin_verificar | Extra |
|---|---|---|---|---|
| items | 4/5 | 80.0 % (37.6 %–96.4 %) | 0 |  |
| promocion | 1/5 | 20.0 % (3.6 %–62.4 %) | 0 |  |
| direccion_entrega | 1/5 | 20.0 % (3.6 %–62.4 %) | 0 |  |
| metodo_pago | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 |  |
| total_dicho | 5/5 | 100.0 % (56.6 %–100.0 %) | 0 | error abs. medio 0.00 |

## Validadores: registros malos atrapados vs perdidos

| Nivel | Registros malos | Atrapados por aritmética | Atrapados por verificación literal | Atrapados (alguna) | Perdidos | Diagnóstico (ok/asr/hablante) |
|---|---|---|---|---|---|---|
| L0 | 5 | 4 | 1 | 4 | 1 | 0/2/3 |

## WER vs calidad del registro

- WER alto (≥ mediana 4.8 %) pero registro perfecto: —
- WER bajo pero registro con errores: t2_01, t2_05
