# Guía de grabación (2 sesiones, ~1 h 15 min cada una)

## Antes de grabar (10 min)
- [ ] Imprime o abre en otro dispositivo `scripts/guiones_t1.md` y `scripts/guiones_t2.md`. Que ninguno lea desde el celular que graba.
- [ ] Decidan quién es A y quién es B en cada clip. **Tú debes aparecer en todos los clips**; alternen roles para que ambos practiquen. Los nombres de los personajes (Lucía, Marco…) son inventados: pueden cambiar el género sin tocar los campos.
- [ ] Cada persona confirma su consentimiento (una línea en el README, sin nombres de quien no acepte).
- [ ] Cierren ventanas, apaguen ventiladores, pongan el celular en modo avión (evita interferencia y notificaciones).

## Durante la grabación
- Celular a 20–30 cm de ambos, sobre una superficie estable. Grabadora de voz nativa; formato m4a/wav, da igual (se convierte después).
- **Un archivo por clip.** Nombres exactos: `t1_01.m4a … t1_05.m4a`, `t2_01.m4a … t2_05.m4a`.
- Lean con naturalidad y a ritmo normal; **no corran**. Pausas breves entre turnos (~1 s) son lo realista.
- Si se equivocan en una palabra, repitan el clip completo desde el inicio. Si improvisan algo que cambia un campo, corrijan `scripts/guiones_data.py` y regeneren (ver abajo).
- Duración objetivo: 2–4 min por clip. Si salió bajo 2 min, grábenlo de nuevo con más calma (no agreguen texto nuevo sin actualizar el guion).

## Regla anti-corpus-idéntico
El enunciado prohíbe que dos estudiantes entreguen los mismos audios. Tú grabas **tus** guiones y tu compañero/a graba **los suyos** (sus propios guiones). No le pases estos para que los grabe igual: aunque el audio sea distinto, el contenido sería idéntico.

## Tiempo
Cada tarea suma ~16–17 min de audio por set. Con repeticiones, cuenta ~1 h 15 min por sesión.

## Después de grabar
1. Copia los audios a `data/audio/` (está en `.gitignore`: nunca se suben).
2. Si cambiaste algún guion: `python scripts/build_ground_truth.py` regenera los CSV de ground truth.
3. Revisa cada clip: escucha 10 s del inicio y del final; confirma la duración (2–4 min).
4. Anota en el README: fecha, dispositivo de grabación y cómo variaste el corpus (tabla en `scripts/guiones_t1.md`).

## Qué NO hacer
- No uses datos reales (salarios, direcciones, teléfonos, nombres de empresas reales).
- No grabes con síntesis de voz: los audios sintéticos son demasiado limpios y no hay nada que medir (solo como augmentation separado).
- No uses subtítulos automáticos como ground truth: el ground truth es el guion.
