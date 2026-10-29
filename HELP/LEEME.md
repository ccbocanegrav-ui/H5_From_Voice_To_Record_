# Paquete de guiones — De la voz al registro

| Archivo / carpeta | Para qué sirve |
|---|---|
| `TODOS_LOS_GUIONES.md` | **Todo junto en un solo documento**: resumen de cantidades + los 4 grupos de guiones (Set A T1/T2, Set B T1/T2). |
| `guia_grabacion.md` | Checklist de grabación. |
| `SET_A_tuyo/` | Guiones, ground truth (CSV) y scripts del set A. |
| `SET_B_companera/` | Guiones, ground truth (CSV) y scripts del set B. |

Cada set se regenera con `python scripts/build_ground_truth.py` (desde dentro de la carpeta del set). El script
también verifica la cantidad del caso: 4–5 clips por tarea, 2–4 min por clip y ~16–20 min por tarea.

**Importante:** cada persona usa SOLO su set en su repo. No mezclen los sets en un mismo repo ni graben el mismo set las dos.
