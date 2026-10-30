# Benchmark ASR — T1

Entorno: Tesla T4 · driver 580.178.04 · faster-whisper 1.2.1 · ctranslate2 4.8.4 · 2026-10-30T04:58:20+00:00

IC95% por bootstrap sobre clips. Con pocos clips los intervalos son anchos: léelos como orden de magnitud.

## Experimentos

| Experimento | Modelo | Dispositivo leído | Precisión | Clips | WER [IC95] | CER | s por min de audio | VRAM pico (MB) | GPU verificada |
|---|---|---|---|---|---|---|---|---|---|
| small_gpu_fp16 | small | cuda | float16 | 5 | 7.6% [6.4%–9.3%] | 3.3% | 1.9 | 884 | sí |
| small_gpu_int8 | small | cuda | int8_float16 | 5 | 7.8% [6.7%–9.4%] | 3.4% | 1.9 | 426 | sí |
| small_cpu_int8 | small | cpu | int8_float32 | 2 | 6.2% [6.2%–6.3%] | 2.5% | 22.6 | 0 | no |
| large_gpu_fp16 | large-v3 | cuda | float16 | 5 | 3.1% [2.0%–4.2%] | 1.5% | 6.1 | 4010 | sí |
| large_gpu_int8 | large-v3 | cuda | int8_float16 | 5 | 3.2% [2.2%–4.3%] | 1.5% | 6.0 | 2250 | sí |
| small_gpu_fp16_glos | small + glosario | cuda | float16 | 5 | 7.0% [5.9%–8.1%] | 2.8% | 2.0 | 746 | sí |
| large_gpu_fp16_glos | large-v3 + glosario | cuda | float16 | 5 | 3.3% [1.9%–4.6%] | 1.7% | 6.2 | 4010 | sí |

## Precisión numérica (¿cambió el texto?)

| A | B | Clips | WER A | WER B | A − B [IC95] | Clips con texto distinto | s/min A → B | VRAM A → B (MB) | Recall glosario A → B |
|---|---|---|---|---|---|---|---|---|---|
| small_gpu_fp16 | small_gpu_int8 | 5 | 7.6% | 7.8% | -0.27 pp [-0.53, +0.00] | 5 de 5 | 1.9 → 1.9 | 884 → 426 | 76.0% → 76.0% |
| large_gpu_fp16 | large_gpu_int8 | 5 | 3.1% | 3.2% | -0.04 pp [-0.18, +0.09] | 3 de 5 | 6.1 → 6.0 | 4010 → 2250 | 96.0% → 100.0% |

## CPU frente a GPU (mismos clips)

| A | B | Clips | WER A | WER B | A − B [IC95] | Clips con texto distinto | s/min A → B | VRAM A → B (MB) | Recall glosario A → B |
|---|---|---|---|---|---|---|---|---|---|
| small_gpu_int8 | small_cpu_int8 | 2 | 6.6% | 6.2% | +0.33 pp [+0.00, +0.68] | 2 de 2 | 1.9 → 22.6 | 426 → 0 | 63.6% → 63.6% |

## Glosario de dominio: plano (A) frente a con vocabulario (B)

| A | B | Clips | WER A | WER B | A − B [IC95] | Clips con texto distinto | s/min A → B | VRAM A → B (MB) | Recall glosario A → B |
|---|---|---|---|---|---|---|---|---|---|
| small_gpu_fp16 | small_gpu_fp16_glos | 5 | 7.6% | 7.0% | +0.58 pp [-0.57, +1.88] | 5 de 5 | 1.9 → 2.0 | 884 → 746 | 76.0% → 100.0% |
| large_gpu_fp16 | large_gpu_fp16_glos | 5 | 3.1% | 3.3% | -0.13 pp [-0.76, +0.31] | 4 de 5 | 6.1 → 6.2 | 4010 → 4010 | 96.0% → 100.0% |

## Tamaño de modelo

| A | B | Clips | WER A | WER B | A − B [IC95] | Clips con texto distinto | s/min A → B | VRAM A → B (MB) | Recall glosario A → B |
|---|---|---|---|---|---|---|---|---|---|
| small_gpu_fp16 | large_gpu_fp16 | 5 | 7.6% | 3.1% | +4.43 pp [+2.96, +5.95] | 5 de 5 | 1.9 → 6.1 | 884 → 4010 | 76.0% → 96.0% |

Lectura: «A − B» positivo en precisión/dispositivo significa que B es MEJOR (menos errores) que A; en glosario, positivo significa que el glosario (B) mejora. Si el IC incluye 0, no se distingue del azar.
