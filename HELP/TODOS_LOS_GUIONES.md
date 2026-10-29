# TODOS LOS GUIONES — De la voz al registro

Paquete único con los dos sets de guiones. **Cada persona graba SOLO su set** (corpus propio; el enunciado prohíbe corpus idénticos).

## Cantidad pedida por el caso → cumplida

- 4 a 5 clips por tarea → **5 clips** en cada tarea.
- 2 a 4 minutos por clip → todos entre **3.1 y 3.6 min** (estimado a 140 palabras/min + pausas).
- ~16 a 20 minutos de audio por tarea → **~16 a 17 min** por tarea.

## Set A — tuyo (T2: Cevichería Marea Norte (inventada))

| Tarea | Clips | Minutos por clip (est.) | Total (est.) |
|---|---|---|---|
| T1 Entrevistas | 5 | 3.4 · 3.6 · 3.4 · 3.6 · 3.5 | **17.4 min** |
| T2 Llamadas | 5 | 3.3 · 3.2 · 3.3 · 3.1 · 3.2 | **16.2 min** |

## Set B — compañera (T2: Chifa Dragón Dorado (inventado))

| Tarea | Clips | Minutos por clip (est.) | Total (est.) |
|---|---|---|---|
| T1 Entrevistas | 5 | 3.3 · 3.3 · 3.3 · 3.3 · 3.4 | **16.6 min** |
| T2 Llamadas | 5 | 3.4 · 3.2 · 3.2 · 3.3 · 3.3 | **16.4 min** |

> Los minutos son una estimación. Cronometra tu primer clip: si lees más rápido o más lento, el total cambia. El margen es amplio (cada clip está lejos de 2 y de 4 min), pero si algún clip te queda fuera de 2–4 min, avísame y lo ajusto.

## Orden de lectura

1. `guia_grabacion.md` (checklist de la sesión).
2. Tu set: primero T1 (entrevistas), luego T2 (llamadas).
3. Si improvisas algo que cambia un valor, corrige `scripts/guiones_data.py` de tu set y corre `python scripts/build_ground_truth.py` (regenera los CSV y verifica que sigues cumpliendo el caso).

---

# [SET A (tuyo)] Guiones — Tarea 1: Entrevistas

A = entrevistador/a · B = candidato/a. Todo lo dicho es INVENTADO.
Fecha ficticia de las entrevistas: **2026-11-02** (sirve para resolver 'en quince días', 'en un mes').
Lee con naturalidad, a ritmo normal. Si improvisas, corrige el texto en `scripts/guiones_data.py` y regenera.

## Cómo varié el corpus (reportar en el README)

| Clip | Orden en que aparecen los campos |
|---|---|
| t1_01 | puesto → años → tecnologías → inglés → (proyecto) → disponibilidad → salario (al final) |
| t1_02 | salario (al inicio) → disponibilidad → años → puesto → tecnologías → inglés (al final) |
| t1_03 | años → puesto → tecnologías → inglés → disponibilidad → (dificultad) → salario |
| t1_04 | años + puesto (juntos, en la primera respuesta) → tecnologías → inglés → disponibilidad → salario → (remoto) |
| t1_05 | (contexto) → años + puesto → tecnologías → inglés → salario (con autocorrección) → disponibilidad → (Python aprendiendo) |

---

## t1_01  (entrevista)

- Palabras: 441 · duración estimada: ~3.4 min
- Orden de campos: puesto → años → tecnologías → inglés → (proyecto) → disponibilidad → salario (al final)
- Trampas: Distractores numéricos: 'tres días', 'cuatro horas', 'ocho personas'. Disponibilidad relativa.

**A:** Buenos días, Lucía, gracias por venir. Cuéntame brevemente quién eres y a qué te dedicas.

**B:** Buenos días. Soy Lucía Paredes, y actualmente trabajo como analista de datos en Cóndor Analytics, una consultora de Lima.

**A:** ¿Y cuánto tiempo llevas trabajando en análisis de datos?

**B:** En total llevo cinco años. Empecé haciendo reportes de ventas y poco a poco pasé a modelos predictivos.

**A:** Interesante. ¿Qué herramientas y tecnologías usas en tu día a día?

**B:** Uso Python con pandas para limpiar y analizar datos, SQL para consultar las bases, y Power BI para los tableros. Últimamente también he trabajado con Docker para empaquetar mis proyectos.

**A:** Muy bien. ¿Cómo describirías tu nivel de inglés?

**B:** Intermedio. Puedo leer documentación técnica sin problema, pero todavía me cuesta hablar con fluidez en reuniones largas.

**A:** Entendido. Cuéntame un proyecto del que te sientas orgullosa.

**B:** Claro. Rediseñé el reporte semanal de ventas de un cliente de retail. Antes tardaba tres días en armarse a mano y ahora se genera en cuatro horas. Trabajé con un equipo de ocho personas y presentamos los resultados a la gerencia.

**A:** Excelente. ¿Y cómo manejas los plazos ajustados?

**B:** Divido el trabajo en entregas pequeñas y aviso con anticipación si algo se complica. Prefiero avisar temprano que llegar tarde con una sorpresa.

**A:** Cuéntame cómo es un día normal en tu trabajo.

**B:** Empiezo revisando que los procesos de la noche hayan terminado bien. Después atiendo los pedidos de información de las otras áreas y dejo las tardes más libres para los análisis largos, que necesitan concentración.

**A:** ¿Y cómo priorizas cuando varias personas te piden algo al mismo tiempo?

**B:** Pregunto para qué lo necesitan y cuándo lo van a usar. Muchas veces algo que parece urgente puede esperar, y otras cosas que parecen pequeñas son las que más pesan en la decisión de alguien.

**A:** ¿Recuerdas algún desacuerdo con un compañero sobre cómo medir un resultado?

**B:** Sí, y lo resolvimos sentándonos con los datos delante. Probamos las dos formas, vimos cuál respondía mejor a la pregunta del cliente y terminamos usando una mezcla de ambas.

**A:** ¿Por qué quieres cambiar de empleo?

**B:** Busco más responsabilidad y trabajar en problemas de mayor escala. Siento que ya aprendí lo que podía en mi puesto actual.

**A:** Hablemos de condiciones. ¿Cuándo podrías incorporarte?

**B:** Tendría que dar un preaviso en mi trabajo, así que estaría disponible en quince días.

**A:** Perfecto. ¿Y cuál es tu pretensión salarial?

**B:** Mi pretensión es de seis mil quinientos soles mensuales.

**A:** Gracias, Lucía. ¿Tienes alguna pregunta para nosotros?

**B:** Sí, me gustaría saber cómo está conformado el equipo y qué proyectos se priorizarían en los primeros meses.

**A:** Te lo contamos en la siguiente etapa. Muchas gracias por tu tiempo.

**B:** Gracias a ustedes.

---

## t1_02  (entrevista)

- Palabras: 462 · duración estimada: ~3.6 min
- Orden de campos: salario (al inicio) → disponibilidad → años → puesto → tecnologías → inglés (al final)
- Trampas: Años con fracción ('tres años y medio'). Distractor 'cinco años' (instituto de inglés) y 'quince minutos'. Disponibilidad inmediata.

**A:** Hola, Marco, bienvenido. Antes de empezar, para alinear expectativas: ¿cuál es tu pretensión salarial?

**B:** Hola, gracias. Buscaría algo alrededor de cuatro mil ochocientos soles al mes.

**A:** Anotado. ¿Y desde cuándo podrías empezar?

**B:** De inmediato. Ya terminé mi contrato anterior la semana pasada, así que tengo disponibilidad inmediata.

**A:** Perfecto. Cuéntame de tu experiencia. ¿Cuántos años llevas en desarrollo?

**B:** Tres años y medio. Comencé como practicante y luego me contrataron de forma fija.

**A:** ¿Cuál fue tu último puesto?

**B:** Fui desarrollador backend en Pampa Digital, una empresa de pagos en línea.

**A:** ¿Con qué tecnologías trabajabas?

**B:** Principalmente Python con Django y PostgreSQL para el servidor. También usaba Docker y Git todos los días, y algo de AWS para el despliegue.

**A:** ¿Y cómo es tu nivel de inglés?

**B:** Avanzado. Estudié cinco años en un instituto y mantengo reuniones con clientes de otros países sin problema.

**A:** Muy bien. Cuéntame cómo manejas un error en producción.

**B:** Lo primero es revisar los registros y reproducir el problema en un ambiente de pruebas. Si es crítico, aviso al equipo y se hace una corrección rápida. Después escribimos un informe para que no se repita.

**A:** Me parece un buen enfoque. ¿Cómo trabajas en equipo?

**B:** Me gusta revisar el código de mis compañeros y que revisen el mío. En Pampa Digital hacíamos reuniones cortas todas las mañanas, de quince minutos, para coordinar las tareas.

**A:** ¿Prefieres trabajo remoto o presencial?

**B:** Me da igual, puedo ir a la oficina o trabajar desde casa, siempre que haya buena comunicación.

**A:** ¿Qué esperas aprender en esta posición?

**B:** Quiero conocer mejor cómo se diseñan sistemas que atienden a muchos usuarios a la vez. En mi trabajo anterior vimos algo de eso, pero siempre en pequeño, y me gustaría trabajar con más volumen.

**A:** ¿Tienes alguna duda sobre el proceso?

**B:** Solo si hay una prueba técnica antes de la decisión final.

**A:** Sí, sería una prueba corta, de un par de horas, la próxima semana.

**B:** Perfecto, me parece bien.

**A:** Antes de cerrar, cuéntame cómo recibes los comentarios sobre tu trabajo.

**B:** Los escucho con calma y trato de no defenderme de inmediato. Si alguien me señala algo en mi código, primero intento entender qué ve esa persona que yo no vi, y después decido qué cambiar.

**A:** ¿Y cuando tú tienes que dar un comentario difícil a un compañero?

**B:** Lo hablo en privado y empiezo por lo que está bien. Después explico el problema con un ejemplo concreto y propongo una alternativa, para que no suene como una crítica a la persona.

**A:** ¿Qué haces cuando sientes que un plazo no es realista?

**B:** Lo digo cuanto antes y con razones. Prefiero proponer una entrega más pequeña y a tiempo que prometer todo y llegar con algo a medias. Casi siempre el equipo lo agradece.

**A:** Gracias, Marco. Ya tenemos tu información. Te contactaremos pronto.

**B:** Muchas gracias.

---

## t1_03  (entrevista)

- Palabras: 445 · duración estimada: ~3.4 min
- Orden de campos: años → puesto → tecnologías → inglés → disponibilidad → (dificultad) → salario
- Trampas: Salario en DÓLARES (moneda distinta). Años 'un año y medio'. Inglés básico. Distractores: 'doce puntos', 'cuatro semanas'. Fecha absoluta 'primero de diciembre'.

**A:** Buenas tardes, Valeria. Gracias por venir. Para empezar, ¿cuánta experiencia tienes?

**B:** Buenas tardes. Tengo un año y medio de experiencia, todo en prácticas y en un par de proyectos de la universidad.

**A:** ¿Qué hacías en tu último puesto?

**B:** Fui practicante de ciencia de datos en Mercado Sur, una cadena de supermercados. Ayudaba a preparar bases de datos y a probar modelos sencillos de predicción de demanda.

**A:** Perfecto. ¿Qué herramientas manejas?

**B:** Excel para casi todo al inicio, luego Python y la librería scikit-learn para los modelos. Para las visualizaciones usé Tableau.

**A:** Una consulta: ¿cómo calificarías tu inglés?

**B:** Básico. Entiendo algunas frases escritas, pero hablar todavía me cuesta mucho. Estoy llevando un curso los sábados para mejorarlo.

**A:** Está bien, es una buena iniciativa. ¿Cuándo podrías empezar a trabajar?

**B:** Termino mis exámenes finales en noviembre, así que podría empezar a partir del primero de diciembre.

**A:** Entendido. Cuéntame una dificultad que hayas enfrentado.

**B:** En mi práctica, los datos de las tiendas llegaban con muchos errores, como precios en blanco y fechas mal escritas. Aprendí a validar los datos antes de usarlos y armé una lista de revisión para el equipo, de doce puntos.

**A:** ¿Y qué fue lo que más disfrutaste de tu práctica?

**B:** Ver que lo que hacía servía. Un día el jefe de compras usó una de mis tablas para decidir cuánto pedir de un producto, y después me contó que se evitó un faltante. Eso me motivó muchísimo a seguir en esta área.

**A:** ¿Cómo te organizas entre la universidad y el trabajo?

**B:** Tengo un calendario semanal y reservo bloques fijos para estudiar y para trabajar. Los fines de semana descanso para no cansarme demasiado.

**A:** Cuéntame cómo aprendes cosas nuevas cuando no conoces el tema.

**B:** Primero busco ejemplos sencillos y los copio para entender cómo funcionan. Luego intento hacer algo parecido por mi cuenta, sin mirar, y si me atasco, regreso a revisar. Así lo que aprendo se me queda.

**A:** ¿Qué haces cuando un compañero te explica algo y no lo entiendes del todo?

**B:** Se lo digo con sinceridad y le pido un ejemplo. Antes me daba vergüenza, pero ahora sé que preguntar a tiempo me ahorra errores y me hace aprender más rápido.

**A:** ¿Cómo te gustaría que fueran tus primeros días en un trabajo nuevo?

**B:** Me gustaría conocer al equipo, entender para qué sirve lo que hago y tener a alguien a quien preguntar sin miedo. Con eso me siento segura y empiezo a aportar antes.

**A:** Qué bien. ¿Y qué esperas ganar mensualmente?

**B:** Estaba pensando en mil doscientos dólares al mes.

**A:** Anotado. ¿Tienes alguna pregunta?

**B:** Sí, ¿habría capacitación durante los primeros meses?

**A:** Sí, tenemos un programa de inducción de cuatro semanas. Muchas gracias, Valeria.

**B:** Gracias a ustedes.

---

## t1_04  (entrevista)

- Palabras: 464 · duración estimada: ~3.6 min
- Orden de campos: años + puesto (juntos, en la primera respuesta) → tecnologías → inglés → disponibilidad → salario → (remoto)
- Trampas: Inglés dicho como 'fluido, certificación C1' (la palabra 'avanzado' NO aparece: requiere mapa de sinónimos). Tecnologías poco comunes (Airflow, dbt). Distractores: 'catorce', 'tres áreas'.

**A:** Buenos días, Rocío. Háblame de ti y de tu trayectoria.

**B:** Buenos días. Tengo ocho años de experiencia en datos. Mi último puesto fue ingeniera de datos en Andes Logística, donde construía y mantenía los flujos de información de toda la empresa.

**A:** ¿Con qué tecnologías trabajabas?

**B:** Mucho Python, Airflow para programar los procesos, dbt para transformar los datos, y todo corría en AWS con Kubernetes.

**A:** ¿Y cuántas personas había en tu equipo?

**B:** Éramos catorce, divididos en tres áreas: ingestión, transformación y publicación.

**A:** ¿Por qué dejaste Andes Logística?

**B:** La empresa se reestructuró y el área de datos se redujo a la mitad. Fue una decisión de ellos, no mía, pero me dejó con ganas de buscar un proyecto más estable.

**A:** Entiendo. ¿Cómo es tu inglés?

**B:** Fluido, tengo certificación C1. Escribo la documentación técnica en inglés y he dado presentaciones a clientes de Chile y México.

**A:** Muy bien. ¿Cuándo podrías incorporarte?

**B:** Me gustaría tomarme un tiempo para descansar, así que estaría lista en un mes.

**A:** Perfecto. Ahora, ¿qué pretensión salarial tienes?

**B:** Siete mil quinientos soles mensuales.

**A:** ¿Es negociable?

**B:** Un poco, depende de los beneficios y del esquema de trabajo remoto.

**A:** ¿Qué esquema prefieres: remoto, presencial o mixto?

**B:** Me acomoda un esquema híbrido, dos días en la oficina y tres desde casa.

**A:** Cuéntame un reto técnico que hayas resuelto.

**B:** Teníamos un proceso nocturno que tardaba mucho y a veces fallaba a mitad de camino. Lo dividí en etapas más pequeñas, agregué reintentos automáticos y avisos cuando algo fallaba. Con eso el proceso dejó de romperse y el equipo pudo dormir tranquilo.

**A:** ¿Cómo mides que un proceso está funcionando bien?

**B:** Reviso que los datos lleguen completos y a tiempo, y que los totales cuadren con la fuente original. Si algo no coincide, lo investigo antes de que alguien más lo note.

**A:** Has liderado equipos antes. ¿Cómo repartes el trabajo cuando alguien está sobrecargado?

**B:** Primero hablo con la persona para entender qué la está agobiando. A veces el problema es la cantidad de tareas, y otras veces es que le tocó algo para lo que no se siente preparada. Según el caso, redistribuyo o acompaño.

**A:** ¿Qué haces cuando un integrante nuevo no rinde como esperabas?

**B:** Reviso primero si le expliqué bien lo que esperaba de su trabajo, porque muchas veces el problema es de comunicación. Después acordamos metas pequeñas y nos vemos con frecuencia para ver cómo va.

**A:** ¿Cómo celebras los logros del equipo?

**B:** Me gusta reconocer en público lo que cada persona hizo bien, con detalles. Decir gracias por el trabajo del equipo suena bonito, pero mencionar qué hizo cada uno es lo que realmente motiva.

**A:** Está bien. ¿Algo más que quieras agregar?

**B:** Que me motiva liderar a otras personas y compartir lo que he aprendido. Quisiera crecer hacia un rol de jefatura técnica.

**A:** Muchas gracias, Rocío.

**B:** A ustedes.

---

## t1_05  (entrevista)

- Palabras: 454 · duración estimada: ~3.5 min
- Orden de campos: (contexto) → años + puesto → tecnologías → inglés → salario (con autocorrección) → disponibilidad → (Python aprendiendo)
- Trampas: Autocorrección del salario ('cinco mil… perdón, cinco mil trescientos cincuenta'). TRAMPA de tecnologías: Python se menciona pero NO lo usa (está aprendiendo) y NO va en el ground truth. Fecha absoluta 'quince de enero' (año siguiente). Distractor 'diez por ciento'.

**A:** Buenas, Sebastián. Gracias por venir. Cuéntame cómo llegaste a este rubro.

**B:** Buenas. Estudié administración y en la universidad me gustaron los números. Hace dos años entré a trabajar como analista de inteligencia comercial en Brisa Retail.

**A:** ¿O sea que ese fue tu último puesto?

**B:** Sí, analista de inteligencia comercial, y sigo ahí hasta fin de año.

**A:** ¿Y qué herramientas usas?

**B:** Eh, básicamente SQL para sacar la información, Excel para los cálculos rápidos, Power BI y también Looker Studio para los tableros que ven los gerentes.

**A:** ¿Cuál es tu nivel de inglés?

**B:** Intermedio, más o menos. Entiendo bien cuando escucho, pero al escribir cometo errores.

**A:** Hablemos de la parte económica. ¿Cuánto pretendes ganar?

**B:** Pretendo cinco mil… perdón, cinco mil trescientos cincuenta soles al mes.

**A:** ¿Y cuándo podrías empezar?

**B:** Mi contrato termina en diciembre, entonces podría incorporarme el quince de enero.

**A:** Entiendo. Cuéntame cómo explicas un resultado a personas que no son técnicas.

**B:** Trato de empezar por la conclusión y usar un gráfico simple. Por ejemplo, el mes pasado mostré que el diez por ciento de los productos generaba la mayor parte de las ventas, y con eso el área comercial cambió su plan de promociones.

**A:** Muy bien. ¿Y qué esperas del equipo al que te incorpores?

**B:** Que haya espacio para preguntar y aprender, y que se revisen los análisis entre todos antes de presentarlos.

**A:** Cuéntame un error que hayas cometido en un análisis.

**B:** Una vez presenté un promedio sin ver que había datos duplicados. Un compañero lo notó antes de la reunión y pudimos corregirlo. Desde entonces reviso los duplicados y los valores raros antes de calcular cualquier cosa.

**A:** ¿Qué te gusta hacer fuera del trabajo?

**B:** Me gusta correr los fines de semana y cocinar. A veces preparo cena para mis amigos y tratamos de probar recetas nuevas.

**A:** Cuéntame cómo te preparas cuando tienes que presentar resultados a la gerencia.

**B:** Primero imagino qué preguntas me harían y preparo respuestas cortas. Después ensayo la presentación en voz alta con un compañero, que me ayuda a ver dónde me enredo y qué parte sobra.

**A:** ¿Y si alguien cuestiona tus conclusiones en plena reunión?

**B:** Escucho la objeción completa antes de responder. Si tiene razón, lo reconozco y me comprometo a revisar. Si no, explico con calma de dónde sale el resultado y ofrezco enseñar los datos después.

**A:** ¿Qué es lo que más valoras de un buen jefe o jefa?

**B:** Que confíe en mí, pero que también esté cerca cuando lo necesito. Me gusta que me den libertad para organizarme, siempre que sepa claramente qué resultados se esperan.

**A:** ¿Y te interesa aprender más programación?

**B:** Sí, de hecho estoy aprendiendo Python por mi cuenta, aunque todavía no lo uso en el trabajo.

**A:** Gracias, Sebastián. Te avisaremos pronto.

**B:** Gracias, un gusto.

---


---

# [SET A (tuyo)] Guiones — Tarea 2: Llamadas de venta (restaurante)

Dominio: **Restaurante** — Cevichería Marea Norte (inventada). A = vendedor/a · B = cliente/a.
Todo lo dicho es INVENTADO.

## Carta y promociones (para el validador aritmético)

| Producto | Tamaño | Precio (S/) |
|---|---|---|
| pollo a la brasa | cuarto | 22 |
| pollo a la brasa | medio | 40 |
| pollo a la brasa | entero | 75 |
| lomo saltado | unico | 30 |
| ceviche clásico | personal | 28 |
| ceviche clásico | para dos | 48 |
| arroz con mariscos | unico | 32 |
| chicha morada | vaso | 6 |
| chicha morada | jarra | 16 |
| gaseosa Inca Kola | 1.5 litros | 12 |

- **P1:** descuento de diez soles en pedidos desde ochenta soles (resta 10 si el subtotal es ≥ 80).
- **P2:** dos por uno en chicha morada en vaso (cada 2 vasos, uno gratis).

## Trampas plantadas

| Clip | Autocorrección | Total incorrecto | Dirección con dígitos | Total dicho | Total correcto |
|---|---|---|---|---|---|
| t2_01 | — | — | sí | 76 | 76 |
| t2_02 | sí | sí | sí | 96 | 86 |
| t2_03 | sí | — | sí | 94 | 94 |
| t2_04 | sí | sí | — | 108 | 98 |
| t2_05 | — | sí | sí | 108 | 96 |

---

## t2_01  (llamada)

- Palabras: 423 · duración estimada: ~3.3 min
- Trampas: Ninguna de tiempo (llamada base, total correcto). Dirección con dígitos.

**A:** Cevichería Marea Norte, buenas tardes, ¿en qué le puedo ayudar?

**B:** Buenas tardes, quisiera hacer un pedido para delivery.

**A:** Claro, dígame qué desea.

**B:** Quiero medio pollo a la brasa, un lomo saltado y una jarra de chicha morada.

**A:** Perfecto. Medio pollo a la brasa, cuarenta soles; lomo saltado, treinta soles; y la jarra de chicha morada, dieciséis soles. ¿Algo más?

**B:** No, eso es todo por ahora. Una pregunta: ¿el lomo viene con papas y arroz?

**A:** Sí, con papas fritas y arroz blanco. El pollo viene con papas y ensalada fresca, y con sus cremas: ají, mayonesa y ketchup.

**B:** Perfecto. ¿Y la chicha es casera?

**A:** Sí, la preparamos todos los días con maíz morado, piña y canela.

**B:** Qué rico. ¿Aceptan pedidos con anticipación? Me gustaría programar uno para el domingo.

**A:** Sí, pero tendría que llamarnos ese día; los pedidos del fin de semana los tomamos desde las diez de la mañana.

**B:** Entendido, lo tendré en cuenta. ¿Tienen postres?

**A:** Sí, tenemos suspiro a la limeña y flan de la casa.

**B:** No, gracias, así está bien.

**A:** Si lo desea, puede dejar una indicación para el repartidor, por ejemplo cómo reconocer su casa.

**B:** Sí, gracias. El portón es de color gris y hay un árbol grande en la entrada. Si no encuentra el número, que llame al celular que les dejé.

**A:** Perfecto, lo anoto en la hoja del pedido. El repartidor es de la zona y conoce bien las calles.

**B:** Qué bien, porque la última vez que pedí a otro lugar el repartidor se perdió y la comida llegó fría.

**A:** Lamentamos que le haya pasado. Nosotros usamos bolsas térmicas y revisamos todo el pedido antes de que salga del local.

**B:** Eso me tranquiliza mucho, gracias por explicármelo con tanta paciencia.

**A:** Le comento que tenemos una promoción: descuento de diez soles en pedidos desde ochenta soles, y su pedido califica.

**B:** Qué bien, gracias.

**A:** ¿Me indica su dirección de entrega?

**B:** Avenida Los Pinos doscientos cuarenta y cinco, en San Miguel, a una cuadra del parque.

**A:** Avenida Los Pinos doscientos cuarenta y cinco, San Miguel. ¿Y cómo va a pagar?

**B:** En efectivo, por favor. ¿Cuánto sería en total?

**A:** La suma es ochenta y seis soles, menos diez de descuento, son setenta y seis soles en total.

**B:** Setenta y seis soles, entendido. Pagaré con un billete de cien, ¿el repartidor lleva vuelto?

**A:** Sí, el repartidor llevará vuelto. Repito su pedido: medio pollo, un lomo saltado y una jarra de chicha morada, por setenta y seis soles.

**B:** Perfecto. ¿Cuánto demora?

**A:** Aproximadamente cuarenta y cinco minutos.

**B:** Está bien, gracias.

**A:** A usted, que lo disfrute.

> Nota para el validador: Total correcto: 40 + 30 + 16 = 86; menos 10 = 76.

---

## t2_02  (llamada)

- Palabras: 410 · duración estimada: ~3.2 min
- Trampas: AUTOCORRECCIÓN (2 ceviches personales → 1 ceviche para dos). TOTAL INCORRECTO (dice 96, correcto 86). Dirección con dígitos. Promo 2x1.

**A:** Cevichería Marea Norte, buenas noches, ¿en qué puedo ayudarle?

**B:** Buenas noches, quiero hacer un pedido para delivery.

**A:** Claro. ¿Es la primera vez que nos llama?

**B:** Sí, un amigo me recomendó la cevichería. Dijo que el arroz con mariscos es lo mejor.

**A:** Muchas gracias por la recomendación, esperamos que le guste. ¿Qué le gustaría pedir?

**B:** Mmm, quiero dos ceviches clásicos personales y un arroz con mariscos.

**A:** Anotado. ¿Algo para tomar?

**B:** Sí, dos chichas moradas en vaso. Ah, y espera, sobre los ceviches: mejor un solo ceviche, pero para dos personas, así es más abundante.

**A:** Perfecto, entonces un ceviche clásico para dos, un arroz con mariscos y dos chichas en vaso.

**B:** Sí, eso. ¿El ceviche es picante?

**A:** Lleva ají limón, es medio picante. Si desea, se lo ponemos aparte.

**B:** Mejor aparte, por favor. ¿Y tienen ají aparte para el arroz?

**A:** Sí, le enviamos un sobrecito con ají amarillo.

**B:** Perfecto.

**A:** Mientras preparamos todo, ¿desea que le avisemos cuando el repartidor salga del local?

**B:** Sí, por favor, con un mensaje al celular. Así bajo a recibir el pedido y no lo dejo esperando en la puerta.

**A:** Perfecto, así lo haremos. También puede seguir el avance llamándonos a este mismo número.

**B:** Qué bueno. Es que tengo una reunión por videollamada más tarde y no quiero perder el pedido.

**A:** Entiendo. Le avisaremos con anticipación para que esté pendiente y pueda conectarse tranquila.

**B:** Muchas gracias, qué amable, se lo agradezco de verdad.

**A:** Le comento que el local atiende hasta tarde, así que si necesita algo más, puede volver a llamarnos.

**B:** Gracias, lo tendré presente. Es bueno saber que atienden hasta tan tarde.

**A:** Listo. Los precios son: ceviche para dos, cuarenta y ocho soles; arroz con mariscos, treinta y dos soles; y cada vaso de chicha, seis soles. Además, hoy tenemos dos por uno en chicha morada en vaso.

**B:** Excelente, entonces los dos vasos al precio de uno.

**A:** Así es. ¿Cuál es su dirección?

**B:** Jirón Ayacucho mil ciento treinta, en Magdalena, frente a la farmacia.

**A:** Jirón Ayacucho mil ciento treinta, Magdalena. ¿Cómo desea pagar?

**B:** Con tarjeta. ¿El repartidor lleva el aparato para pasar la tarjeta?

**A:** Sí, lo lleva. El total sería noventa y seis soles.

**B:** ¿Noventa y seis soles? Está bien.

**A:** Sí, noventa y seis soles en total. Su pedido llegará en cincuenta minutos aproximadamente.

**B:** Gracias. ¿El ceviche viene con camote y choclo?

**A:** Sí, con camote, choclo y cancha.

**B:** Perfecto. ¿Pueden poner cubiertos descartables?

**A:** Claro, le incluimos cubiertos, servilletas y salsas.

**B:** Perfecto, muchas gracias.

**A:** A usted. Buenas noches.

> Nota para el validador: Correcto: 48 + 32 + 2x6 = 92; promo 2x1 resta un vaso (6) = 86. El vendedor dice 96 y el cliente lo repite (error del HABLANTE, no del ASR).

---

## t2_03  (llamada)

- Palabras: 422 · duración estimada: ~3.3 min
- Trampas: AUTOCORRECCIÓN (pollo entero → medio + cuarto). Total CORRECTO. Dirección con dígitos. Pago por Yape.

**A:** Cevichería Marea Norte, buenas tardes.

**B:** Hola, buenas tardes. Quiero un pollo entero a la brasa, un lomo saltado y una gaseosa Inca Kola de litro y medio.

**A:** Muy bien, pollo entero, lomo saltado y gaseosa de litro y medio.

**B:** Mmm, no, espera. El pollo entero es mucho para nosotros. Mejor un medio pollo y un cuarto de pollo. El lomo y la gaseosa sí se quedan.

**A:** Entendido, cambio el pedido: medio pollo, un cuarto de pollo, un lomo saltado y la gaseosa de litro y medio.

**B:** Correcto. ¿El pollo viene con ensalada?

**A:** Sí, con papas fritas y ensalada fresca, y las cremas que usted quiera.

**B:** Genial, con ají y mayonesa, por favor.

**A:** ¿Prefiere que las cremas vayan en recipientes aparte o directamente sobre la ensalada?

**B:** Aparte, por favor, porque a mi hijo no le gusta el picante y así cada uno se sirve lo que quiere.

**A:** Entendido, las enviamos en recipientes pequeños y cerrados para que no se derramen en el camino.

**B:** Qué bueno. Y también necesito servilletas y cubiertos suficientes, porque vienen invitados a la casa.

**A:** Claro, incluimos servilletas y cubiertos para todos. Si necesita más, avísenos ahora y lo agregamos.

**B:** Con eso está bien, muchas gracias por la atención.

**A:** Si le gustó la atención, puede dejarnos su opinión en nuestras redes cuando guste. Siempre nos ayuda a mejorar.

**B:** Claro, con gusto. Siempre recomiendo los lugares que me tratan bien.

**A:** Anotado. Los precios son: medio pollo, cuarenta soles; cuarto de pollo, veintidós soles; lomo saltado, treinta soles; y la gaseosa, doce soles. Hoy hay descuento de diez soles en pedidos desde ochenta soles, y su pedido califica.

**B:** Qué bueno.

**A:** ¿Desea agregar alguna entrada o postre?

**B:** No, gracias. Es para una cena en casa con unos familiares que vienen de visita, y con esto alcanza.

**A:** Perfecto, que lo disfruten.

**B:** Gracias. Ojalá llegue caliente, porque vivimos un poco lejos.

**A:** Lo empacamos en bolsas térmicas para que llegue bien caliente. La suma es ciento cuatro soles, menos diez, son noventa y cuatro soles en total.

**B:** Noventa y cuatro soles. Perfecto.

**A:** ¿Cuál es su dirección?

**B:** Calle Las Begonias ochenta y siete, en Surco, casa de reja blanca.

**A:** Calle Las Begonias ochenta y siete, Surco. ¿Cuál será la forma de pago?

**B:** Voy a pagar por Yape antes de que llegue el pedido.

**A:** Perfecto, le enviaremos el código para el pago por mensaje. Repito: medio pollo, cuarto de pollo, lomo saltado y gaseosa, por noventa y cuatro soles.

**B:** Así es. ¿Y cuánto demoran?

**A:** Unos cuarenta minutos.

**B:** Muy bien, muchas gracias.

**A:** Gracias a usted, que tenga buena tarde.

> Nota para el validador: Correcto: 40 + 22 + 30 + 12 = 104; menos 10 = 94. Total dicho 94 (correcto).

---

## t2_04  (llamada)

- Palabras: 397 · duración estimada: ~3.1 min
- Trampas: AUTOCORRECCIÓN (3 lomos → 2 lomos). TOTAL INCORRECTO (dice 108 = olvidó aplicar el descuento; correcto 98). Recojo en tienda (sin dirección).

**A:** Cevichería Marea Norte, buenas tardes, ¿en qué le ayudo?

**B:** Buenas tardes. Voy a recoger un pedido en tienda, ¿puedo hacerlo por teléfono ahora?

**A:** Claro, dígame.

**B:** Quiero tres lomos saltados, un arroz con mariscos y una jarra de chicha morada. Perdón, me equivoqué, son dos lomos saltados, no tres. Somos pocos hoy.

**A:** Perfecto, dos lomos saltados, un arroz con mariscos y una jarra de chicha morada.

**B:** Eso es. ¿El arroz con mariscos es para una persona?

**A:** Es una porción generosa, alcanza bien para una persona con buen apetito.

**B:** Está bien.

**A:** Mientras tanto, ¿viene con mucho apetito hoy?

**B:** Sí, muchísimo. Hoy tuve un día larguísimo en el trabajo y casi no tuve tiempo de almorzar.

**A:** Entonces lo vamos a atender rápido. Si quiere, puedo avisar a la cocina para que prioricen su pedido.

**B:** No hace falta, gracias. Prefiero tener hambre para disfrutar todo cuando llegue a la tienda.

**A:** Muy bien. Le comento que la cocina está tranquila en este momento, así que no debería demorar nada.

**B:** Qué buena noticia, justo lo que necesitaba escuchar después de un día así.

**A:** ¿Es la primera vez que nos visita o ya es cliente frecuente?

**B:** Vine una vez con unos amigos hace tiempo y me gustó mucho, por eso decidí volver hoy.

**A:** Qué bueno saberlo. Siempre estamos mejorando la atención y la cocina, así que esperamos que note la diferencia.

**B:** Seguro que sí. Ojalá mantengan el mismo sabor, que es lo que más me gustó.

**A:** Los precios son: lomo saltado, treinta soles cada uno; arroz con mariscos, treinta y dos soles; jarra de chicha, dieciséis soles. Y tenemos un descuento de diez soles en pedidos desde ochenta soles.

**B:** Mi pedido supera eso, ¿verdad?

**A:** Sí. Veamos… el total sería ciento ocho soles.

**B:** ¿Ciento ocho? Bueno, está bien.

**A:** Sí, ciento ocho soles. ¿A nombre de quién será el pedido?

**B:** A nombre de Jorge.

**A:** Jorge, listo. ¿Cómo pagará? Aceptamos efectivo, tarjeta y Yape.

**B:** En efectivo, cuando llegue a la tienda.

**A:** Perfecto. Su pedido estará listo en veinte minutos. Total, ciento ocho soles.

**B:** Gracias. ¿Hasta qué hora atienden hoy?

**A:** Hasta las diez de la noche.

**B:** Entonces paso en un rato.

**A:** Perfecto. Si viene en auto, tenemos espacio para seis autos al costado del local.

**B:** Genial, voy en auto. Ah, y por favor, que el arroz salga bien caliente, que lo voy a comer en el auto.

**A:** Anotado, saldrá recién servido. Lo esperamos, Jorge. Hasta luego.

**B:** Hasta luego.

> Nota para el validador: Correcto: 2x30 + 32 + 16 = 108; menos 10 = 98. El vendedor menciona el descuento pero dice 108 y lo repite (error del HABLANTE).

---

## t2_05  (llamada)

- Palabras: 408 · duración estimada: ~3.2 min
- Trampas: TOTAL INCORRECTO (dice 108, olvida el dos por uno; correcto 96). Dirección con dígitos y letra ('departamento cuatro B'). Promo 2x1 con cantidad par.

**A:** Cevichería Marea Norte, buenas tardes, ¿en qué puedo servirle?

**B:** Buenas tardes. Es para el almuerzo en mi oficina, quiero pedir tres ceviches clásicos personales.

**A:** Muy bien, tres ceviches clásicos personales. ¿Algo para tomar?

**B:** Sí, cuatro chichas moradas en vaso.

**A:** Perfecto. Le comento que hoy tenemos dos por uno en chicha morada en vaso.

**B:** Qué bien, qué conveniente. Entonces cuatro vasos.

**A:** Así es, cuatro vasos. Los precios son: ceviche personal, veintiocho soles cada uno, y el vaso de chicha, seis soles.

**B:** De acuerdo. ¿Los ceviches vienen con camote y choclo?

**A:** Sí, con camote, choclo y cancha, como siempre.

**B:** Perfecto. Es la tercera vez que les pido y siempre llega todo muy bien.

**A:** Muchas gracias por su preferencia, nos alegra saberlo.

**B:** Sí, siempre llega bien. Por eso lo recomendé en mi oficina y varios compañeros se animaron a probar.

**A:** Muchas gracias por la recomendación. Si quiere, le puedo enviar nuestro número de contacto para que se lo pase a ellos.

**B:** Sí, mejor. A veces quieren pedir por su cuenta y no saben a quién llamar.

**A:** Con gusto. También atendemos pedidos grandes para eventos, si alguna vez lo necesitan, con anticipación.

**B:** Lo tendré en cuenta, porque en diciembre hacemos una reunión de fin de año en la oficina.

**A:** Qué bueno, ojalá podamos atenderlos. Con tiempo, le ayudamos a organizar todo.

**B:** Por cierto, ¿tienen una carta que pueda mostrarles a mis compañeros?

**A:** Sí, le puedo enviar la carta completa por mensaje, con fotos de cada plato, para que la compartan.

**B:** Perfecto. ¿Pueden ponerle poco picante a todos?

**A:** Claro, lo anotamos para cocina. ¿Cuántos son, para ponerles los cubiertos?

**B:** Somos tres personas, cada uno con su ceviche, y las chichas las compartimos.

**A:** Perfecto, le enviamos cubiertos para todos. ¿Cuál es su dirección de entrega?

**B:** Pasaje Los Cedros trescientos doce, departamento cuatro B, en Jesús María.

**A:** Pasaje Los Cedros trescientos doce, departamento cuatro B, Jesús María. ¿Y cómo va a pagar?

**B:** Con tarjeta, por favor.

**A:** ¿Desea boleta o factura?

**B:** Boleta, por favor.

**A:** Listo, se la enviamos con el pedido. Entendido. Tres ceviches, ochenta y cuatro soles, más cuatro chichas, veinticuatro soles. El total sería ciento ocho soles.

**B:** Ciento ocho soles, de acuerdo.

**A:** Sí, ciento ocho soles en total. Llegará en unos cincuenta minutos.

**B:** ¿Las chichas llegan frías?

**A:** Sí, las enviamos en una bolsa con hielo para que lleguen bien frías.

**B:** ¿Se puede mandar antes de la una? Tenemos reunión después.

**A:** Haremos lo posible, lo anotamos como prioridad.

**B:** Muchas gracias.

**A:** Gracias a usted, buenas tardes.

> Nota para el validador: Correcto: 3x28 + 4x6 = 108; promo 2x1 con 4 vasos regala 2 (12) = 96. El vendedor dice 108 (no aplicó la promo).

---


---

# [SET B (compañera)] Guiones — Tarea 1: Entrevistas (SET B)

A = entrevistadora · B = candidata. Todo lo dicho es INVENTADO.
Fecha ficticia de las entrevistas: **2026-11-02** (resuelve 'a fin de mes', 'en dos semanas'…).
Lean con naturalidad, a ritmo normal. Si improvisan, corrijan el texto en `scripts/guiones_data.py` y regeneren.

## Cómo varía el corpus (reportar en el README)

| Clip | Orden en que aparecen los campos |
|---|---|
| t1_01 | puesto → tecnologías → años → (proyecto) → salario → disponibilidad → inglés (al final) |
| t1_02 | años → salario (al inicio) → inglés → tecnologías → puesto → disponibilidad (al final) |
| t1_03 | tecnologías (primera pregunta) → años → puesto → inglés → disponibilidad → salario → (cierre) |
| t1_04 | inglés (primera pregunta) → salario (con autocorrección) → años + puesto → tecnologías → disponibilidad |
| t1_05 | años + puesto (juntos, al inicio) → tecnologías → inglés → (modelo) → disponibilidad → salario → (motivación) |

---

## t1_01  (entrevista)

- Palabras: 435 · duración estimada: ~3.3 min
- Orden de campos: puesto → tecnologías → años → (proyecto) → salario → disponibilidad → inglés (al final)
- Trampas: Distractores: 'dos primeros… otros dos' (años), 'tres pasos', 'quince personas'. Disponibilidad 'a fin de mes' (relativa → 2026-11-30).

**A:** Buenas tardes, Fiorella, bienvenida. Gracias por venir. Cuéntame qué has estado haciendo últimamente.

**B:** Buenas tardes, Karina. Mi último puesto fue diseñadora UX en Nube Creativa, una agencia digital de Lima. Diseñaba aplicaciones y páginas web para clientes de distintos rubros.

**A:** ¿Con qué herramientas trabajas?

**B:** Principalmente Figma para los prototipos, Adobe XD cuando el cliente lo pedía, e Illustrator para los íconos y las ilustraciones.

**A:** ¿Cuántos años de experiencia tienes en diseño?

**B:** Cuatro años. Los dos primeros como diseñadora gráfica y los otros dos ya enfocada en experiencia de usuario.

**A:** Cuéntame un proyecto del que estés orgullosa.

**B:** Rediseñé la aplicación de una clínica para que los pacientes pudieran sacar citas en tres pasos. Antes necesitaban llamar por teléfono. Hicimos pruebas con quince personas y la mayoría terminó el proceso en menos de un minuto.

**A:** ¡Qué buen resultado! ¿Y cómo recibes las críticas a tu trabajo?

**B:** Las tomo como información. Si varias personas se confunden en la misma pantalla, el problema no es de ellas, es del diseño. Prefiero escuchar temprano para corregir a tiempo.

**A:** Cuéntame cómo investigas lo que necesitan las personas que van a usar un producto.

**B:** Empiezo conversando con ellas, sin mostrarles nada todavía. Les pregunto cómo resuelven hoy ese problema y dónde se frustran. Con esas historias dibujo un primer boceto y recién ahí lo pruebo.

**A:** ¿Y qué haces cuando lo que piden los clientes choca con lo que ven los usuarios?

**B:** Llevo ejemplos reales a la mesa. Un comentario de un usuario de carne y hueso pesa más que mi opinión. Casi siempre, el cliente cambia de idea cuando escucha cómo se confunde la gente.

**A:** ¿Qué haces cuando un diseño tuyo no funciona en las pruebas?

**B:** Me alegro de haberlo descubierto antes de que se publique. Anoto qué falló, rehago esa parte y lo vuelvo a probar. Aprendí que el primer diseño casi nunca es el definitivo.

**A:** Hablemos de condiciones. ¿Cuál es tu pretensión salarial?

**B:** Estoy pensando en cinco mil doscientos soles mensuales.

**A:** ¿Y cuándo podrías incorporarte?

**B:** Puedo empezar a fin de mes, cuando termine un proyecto pendiente con mi cliente actual.

**A:** Perfecto. ¿Y cómo describirías tu nivel de inglés?

**B:** Intermedio. Puedo conversar con clientes en reuniones cortas, pero para presentaciones largas todavía me preparo mucho.

**A:** ¿Trabajas mejor sola o en equipo?

**B:** En equipo, sobre todo con desarrolladoras. Me gusta sentarme con ellas desde el inicio para que el diseño se pueda construir sin sorpresas.

**A:** Muy bien. ¿Tienes alguna pregunta para nosotras?

**B:** Sí, quisiera saber si el equipo de diseño participa en las decisiones de producto o solo recibe los requerimientos.

**A:** Participa desde el inicio. Muchas gracias, Fiorella.

**B:** Gracias a ustedes, Karina.

---

## t1_02  (entrevista)

- Palabras: 429 · duración estimada: ~3.3 min
- Orden de campos: años → salario (al inicio) → inglés → tecnologías → puesto → disponibilidad (al final)
- Trampas: Salario 'ocho mil doscientos' dicho temprano. Distractor 'cinco personas' a su cargo. Fecha absoluta 'primero de febrero' (año siguiente: 2027-02-01). Inglés básico.

**A:** Hola, Mariana, gracias por venir. Para empezar, ¿cuántos años de experiencia tienes?

**B:** Hola, Yesenia. Tengo diez años de experiencia en finanzas, casi todos en el sector bancario y los últimos en una empresa de seguros.

**A:** Entiendo. Y para ir aclarando, ¿cuál sería tu pretensión salarial?

**B:** Mi pretensión es de ocho mil doscientos soles al mes, con los beneficios de ley.

**A:** Anotado. ¿Cómo está tu inglés?

**B:** Básico, la verdad. Leo informes sencillos, pero no me siento cómoda conversando. Quiero mejorarlo y por eso me inscribí en clases virtuales.

**A:** Muy bien. ¿Qué herramientas usas en tu trabajo?

**B:** Excel todos los días, con macros en VBA para automatizar los reportes. También uso SAP para los registros contables, y Power BI para presentar los resultados a la gerencia.

**A:** ¿Cuál fue tu último puesto?

**B:** Analista financiera senior en Seguros Horizonte. Preparaba proyecciones, controlaba el presupuesto y revisaba los cierres de cada mes.

**A:** ¿Cuántas personas estaban a tu cargo?

**B:** Dirigía a un equipo de cinco personas, y respondía a la gerente de finanzas.

**A:** ¿Por qué te interesa este cambio?

**B:** Quisiera trabajar en una empresa más pequeña, donde mi trabajo tenga más impacto directo. En la aseguradora grande yo era una pieza más.

**A:** ¿Cómo manejas un cierre de mes cuando los números no cuadran?

**B:** Primero comparo contra el mes anterior para ver dónde cambió algo. Luego voy por partes, por cuenta, hasta encontrar la diferencia. Casi siempre es un registro duplicado o una fecha mal puesta.

**A:** Cuéntame cómo explicas los resultados financieros a personas que no son del área.

**B:** Evito los términos técnicos y uso comparaciones cotidianas. Por ejemplo, explico el flujo de caja como el dinero que realmente hay en la cuenta al cierre, aunque todavía falte cobrar algunas facturas.

**A:** ¿Qué haces cuando la gerencia te pide una cifra que no se puede sostener con los datos?

**B:** Les explico con calma qué se puede afirmar y qué no. Prefiero decir que no tengo ese dato todavía y ofrecer una estimación clara, antes que dar una cifra que después tenga que corregir.

**A:** ¿Cómo te mantienes al día con los cambios en las normas?

**B:** Leo los boletines del colegio profesional y converso con colegas de otras empresas. Además, anoto en un cuaderno compartido los cambios que afectan a mi equipo, para que nadie los olvide.

**A:** Bien. ¿Y cuándo podrías empezar?

**B:** Quisiera terminar el año con mi equipo actual, así que podría incorporarme el primero de febrero.

**A:** Entendido. ¿Tienes alguna pregunta?

**B:** Sí, ¿cómo es el proceso de cierre contable en esta empresa y quiénes participan en él?

**A:** Lo vemos en la siguiente reunión. Gracias, Mariana.

**B:** Gracias a ti.

---

## t1_03  (entrevista)

- Palabras: 426 · duración estimada: ~3.3 min
- Orden de campos: tecnologías (primera pregunta) → años → puesto → inglés → disponibilidad → salario → (cierre)
- Trampas: Experiencia menor a un año ('seis meses' = 0.5). Distractor 'un año en Canadá'. Salario en DÓLARES. Disponibilidad 'en tres semanas' (→ 2026-11-23).

**A:** Buenos días, Ximena. Cuéntame qué tecnologías manejas, para empezar.

**B:** Buenos días, Pamela. Trabajo con React y JavaScript, y recientemente empecé a usar TypeScript. Para el control de versiones uso Git todos los días.

**A:** ¿Cuánta experiencia laboral tienes?

**B:** Seis meses. Soy recién egresada, pero hice proyectos propios durante la universidad y publiqué una página para una tienda de ropa.

**A:** ¿Cuál fue tu último puesto?

**B:** Desarrolladora frontend junior en Latido Software, donde estuve en un equipo que construía una aplicación de reservas.

**A:** ¿Qué hacías en ese equipo?

**B:** Armaba las pantallas, corregía errores que reportaban los usuarios y escribía pruebas para los componentes. Aprendí mucho de las revisiones de código de mis compañeras.

**A:** ¿Y tu nivel de inglés?

**B:** Avanzado. Viví un año en Canadá con una beca y desde entonces leo y escribo en inglés a diario. Tengo certificación.

**A:** Excelente. ¿Cuándo podrías incorporarte?

**B:** En tres semanas, porque primero debo entregar mis pendientes y despedirme del equipo.

**A:** Perfecto. ¿Cuál es tu pretensión salarial?

**B:** Novecientos dólares al mes, aunque soy flexible según el paquete de beneficios.

**A:** Entiendo. ¿Cómo te mantienes al día con las tecnologías nuevas?

**B:** Sigo cursos cortos en línea y leo documentación oficial. También participo en un grupo de mujeres desarrolladoras donde compartimos ejercicios y nos ayudamos con dudas.

**A:** ¿Qué te gustaría construir en esta empresa?

**B:** Me gustaría trabajar en productos que use mucha gente, y aprender cómo se cuida el rendimiento de una aplicación cuando crece.

**A:** ¿Cómo manejas un error que no logras resolver?

**B:** Primero intento reproducirlo en un ejemplo pequeño. Si después de un rato no avanzo, pido ayuda a una compañera y le explico lo que ya probé. Explicarlo en voz alta me ayuda a encontrar la respuesta.

**A:** ¿Cómo te aseguras de que lo que construyes sea fácil de usar para todas las personas?

**B:** Pruebo con el teclado, sin usar el ratón, y reviso que los textos se lean bien con letras grandes. También pido a una amiga con poca vista que lo pruebe y me cuente dónde se pierde.

**A:** Qué interesante. ¿Qué valoras en la revisión del trabajo de otras personas?

**B:** Que se comente con respeto y con una razón. Si me piden que cambie algo, me gusta entender por qué. Y cuando reviso a otras, intento comenzar por lo que me gustó antes de señalar mejoras.

**A:** ¿Cómo imaginas tu crecimiento dentro de un tiempo?

**B:** Me gustaría ser alguien en quien el equipo confíe para tareas difíciles, y también ayudar a las personas que recién empiezan. Cuando yo llegué, me ayudaron mucho, y quiero devolverlo.

**A:** Muchas gracias, Ximena. Te escribiremos pronto.

**B:** Gracias a ti, Pamela.

---

## t1_04  (entrevista)

- Palabras: 427 · duración estimada: ~3.3 min
- Orden de campos: inglés (primera pregunta) → salario (con autocorrección) → años + puesto → tecnologías → disponibilidad
- Trampas: Inglés dicho como 'intermedio alto, nivel B2' (clase = intermedio). Autocorrección del salario ('cuatro mil… ay, no, tres mil novecientos'). Distractor 'treinta por ciento'. Fecha absoluta 'quince de noviembre'.

**A:** Hola, Brenda, bienvenida. Antes que nada, ¿cómo describirías tu nivel de inglés?

**B:** Hola, Lorena. Intermedio alto, tengo nivel B2. Puedo participar en reuniones y escribir correos sin problema, aunque a veces busco palabras.

**A:** Gracias. Ahora la pregunta que suele incomodar: ¿cuál es tu pretensión salarial?

**B:** Pretendo cuatro mil… ay, no, tres mil novecientos soles mensuales.

**A:** Muy bien. Cuéntame sobre tu experiencia.

**B:** Tengo dos años y medio de experiencia en marketing digital. Mi último puesto fue especialista en marketing digital en Sabor Andino, una marca de alimentos.

**A:** ¿Qué hacías allí?

**B:** Planificaba campañas, manejaba las redes sociales y medía los resultados cada semana. Por ejemplo, lanzamos una campaña de recetas que aumentó las visitas a la tienda en línea en un treinta por ciento.

**A:** ¿Con qué herramientas trabajabas?

**B:** Google Analytics para medir el tráfico, Meta Ads para los anuncios, HubSpot para organizar los contactos y Canva para las piezas gráficas.

**A:** ¿Cómo decides si una campaña funcionó?

**B:** Defino antes qué quiero lograr, por ejemplo más suscripciones, y comparo contra la semana anterior. Si no mejoró, pruebo otro mensaje o cambio al público al que le llega.

**A:** ¿Cuándo podrías empezar?

**B:** A partir del quince de noviembre. Ya conversé con mi jefa y acepta que me vaya.

**A:** Perfecto. ¿Prefieres trabajar con metas mensuales o por proyecto?

**B:** Me gustan las metas mensuales, porque me ayudan a priorizar, pero también me gustan los proyectos grandes cuando hay tiempo para planificarlos.

**A:** Cuéntame cómo trabajas con diseñadoras y redactoras cuando tienen ideas distintas a las tuyas.

**B:** Les pido que me expliquen su idea completa y cuál es el objetivo detrás. Muchas veces coincidimos en lo que queremos lograr y solo cambia el camino, así que probamos ambos y vemos qué funciona mejor.

**A:** ¿Qué haces cuando una campaña no da el resultado que esperabas?

**B:** Dejo pasar un poco de tiempo para no reaccionar con prisa y luego reviso qué cambió. A veces fue el mensaje, a veces el momento. Lo importante es aprender algo y compartirlo con el equipo.

**A:** ¿Cómo te gusta que te den seguimiento en tu trabajo?

**B:** Con reuniones cortas y frecuentes, y con comentarios concretos. Si me dicen qué salió bien y qué ajustar, puedo corregir rápido sin esperar a una evaluación larga.

**A:** ¿Qué esperas de tu jefa o jefe directo?

**B:** Que me dé objetivos claros y comentarios sinceros. Prefiero que me digan pronto qué debo mejorar, aunque no sea agradable de escuchar.

**A:** ¿Alguna pregunta para nosotras?

**B:** ¿Cuántas personas conforman el equipo de marketing y cómo se reparten las marcas?

**A:** Son seis personas, y cada una lleva dos marcas. Gracias, Brenda.

**B:** A ti, Lorena.

---

## t1_05  (entrevista)

- Palabras: 448 · duración estimada: ~3.4 min
- Orden de campos: años + puesto (juntos, al inicio) → tecnologías → inglés → (modelo) → disponibilidad → salario → (motivación)
- Trampas: Tecnología de una sola letra: 'R' (erre). Inglés básico. Distractor 'tres métodos'. Salario alto 'once mil quinientos'. Disponibilidad 'en dos semanas' (→ 2026-11-16).

**A:** Buenas tardes, Jimena. Gracias por venir. Cuéntame cuál ha sido tu recorrido.

**B:** Buenas tardes, Renata. Tengo seis años de experiencia. Mi último puesto fue científica de datos en Caja Valle Verde, en el área de riesgo crediticio.

**A:** ¿Con qué tecnologías trabajabas?

**B:** Programaba en R y en Python, usaba Stata para algunos modelos estadísticos más tradicionales, y SQL para extraer la información de la base de datos.

**A:** ¿Cómo es tu nivel de inglés?

**B:** Básico. Puedo leer artículos técnicos con ayuda de un traductor, pero no he practicado hablar. Es mi punto débil y lo sé.

**A:** Gracias por ser sincera. Cuéntame un modelo que hayas construido.

**B:** Construí un modelo para estimar la probabilidad de que un cliente no pagara su crédito. Probé tres métodos y escogí el que mejor funcionaba con clientes nuevos, porque eran los más difíciles de evaluar. Redujo las pérdidas del área, según el informe interno.

**A:** ¿Cómo explicas un modelo complejo a personas del negocio?

**B:** Con ejemplos concretos. En vez de hablar de coeficientes, muestro dos clientes parecidos y explico por qué el modelo le da más riesgo a uno que al otro.

**A:** ¿Cuándo podrías incorporarte?

**B:** En dos semanas. Ya avisé en mi trabajo y estoy entregando mis pendientes.

**A:** ¿Y cuál es tu pretensión salarial?

**B:** Once mil quinientos soles mensuales.

**A:** ¿Qué te motiva de esta oferta?

**B:** Que el equipo trabaja con datos propios y no solo con reportes. Quiero participar desde la idea hasta que el modelo se use de verdad.

**A:** ¿Cómo trabajas con personas de otras áreas que no conocen de estadística?

**B:** Con paciencia y sin jerga. Al inicio del proyecto me reúno con ellas para entender qué decisión quieren tomar, porque de eso depende el tipo de modelo que conviene construir.

**A:** ¿Cómo te aseguras de que un modelo no perjudique injustamente a ciertas personas?

**B:** Reviso cómo se comporta con distintos grupos antes de llevarlo a producción. Si veo diferencias que no se explican por el riesgo real, vuelvo a revisar las variables y consulto con el área legal.

**A:** Importante. ¿Qué haces cuando los datos que tienes no son suficientes?

**B:** Lo digo desde el inicio y propongo recoger más información o usar un modelo más sencillo. Prefiero un resultado modesto pero honesto que uno impresionante que no se sostiene.

**A:** ¿Cómo compartes lo que aprendes con el resto del equipo?

**B:** Escribo notas cortas después de cada proyecto con lo que funcionó y lo que no, y organizo una charla informal para que cualquiera pueda preguntar. Así no se pierde lo aprendido.

**A:** Muy bien, ¿tienes alguna pregunta?

**B:** Sí, quisiera saber cómo se evalúa el trabajo de ciencia de datos aquí, y cada cuánto se revisan los modelos en producción.

**A:** Se revisan cada trimestre. Muchas gracias, Jimena.

**B:** Gracias, Renata.

---


---

# [SET B (compañera)] Guiones — Tarea 2: Llamadas de venta (restaurante) — SET B

Dominio: **Restaurante** — Chifa Dragón Dorado (inventado). A = vendedora · B = clienta. Todo lo dicho es INVENTADO.

## Carta y promociones (para el validador aritmético)

| Producto | Tamaño | Precio (S/) |
|---|---|---|
| arroz chaufa | personal | 18 |
| arroz chaufa | familiar | 34 |
| tallarín saltado | unico | 22 |
| wantán frito | porción | 12 |
| sopa de wantán | unico | 16 |
| gaseosa | personal | 5 |
| limonada | jarra | 14 |

- **Q1:** descuento de quince soles en pedidos desde noventa soles (resta 15 si el subtotal es >= 90).
- **Q2:** tres por dos en gaseosas personales (por cada 3 gaseosas personales, 1 es gratis (resta 5)).

## Trampas plantadas

| Clip | Autocorrección | Total incorrecto | Dirección con dígitos | Total dicho | Total correcto |
|---|---|---|---|---|---|
| t2_01 | — | — | sí | 68 | 68 |
| t2_02 | sí | sí | sí | 72 | 62 |
| t2_03 | sí | — | — | 113 | 113 |
| t2_04 | — | sí | sí | 76 | 71 |
| t2_05 | sí | sí | sí | 148 | 143 |

---

## t2_01  (llamada)

- Palabras: 426 · duración estimada: ~3.4 min
- Trampas: Llamada base, total correcto. SIN promoción aplicada (se menciona que no aplica: promocion = null). Dirección con dígitos.

**A:** Chifa Dragón Dorado, buenas tardes, ¿en qué le puedo ayudar?

**B:** Buenas tardes, quisiera hacer un pedido para delivery, por favor.

**A:** Claro que sí, cuénteme qué desea pedir.

**B:** Quiero un arroz chaufa familiar, un tallarín saltado y una porción de wantán frito.

**A:** Perfecto. El arroz chaufa familiar cuesta treinta y cuatro soles, el tallarín saltado veintidós soles y la porción de wantán frito doce soles. ¿Algo más?

**B:** No, eso es todo. Una consulta, ¿el tallarín saltado lleva carne o pollo?

**A:** Puede ser de pollo, de carne o mixto. ¿Cuál prefiere?

**B:** Mixto, por favor. ¿Y el wantán frito viene con salsa?

**A:** Sí, con salsa de tamarindo, que es agridulce.

**B:** Perfecto. ¿El chaufa familiar alcanza para tres personas?

**A:** Sí, alcanza bien para tres, y si comen poco hasta para cuatro.

**B:** Genial. ¿Y pueden enviarme también salsa de ají y sillao?

**A:** Claro, con gusto, le incluimos sobrecitos de sillao y de ají.

**B:** Gracias.

**A:** Si lo desea, también podemos enviar cucharas y tenedores descartables, además de los palitos.

**B:** Sí, por favor, ambos, porque en casa hay niños que todavía no usan bien los palitos.

**A:** Con gusto, así todos podrán comer cómodos. También incluimos servilletas en cantidad suficiente.

**B:** Qué amable. Una duda: ¿los recipientes se pueden meter al microondas?

**A:** Sí, son aptos para microondas, aunque recomendamos retirar la tapa antes de calentar la comida.

**B:** Entendido, gracias por avisarme, así evito cualquier accidente.

**A:** Y si algún día quiere hacer un pedido más grande, para una reunión o una celebración, lo ideal es llamarnos con anticipación para preparar todo con calma.

**B:** Buena idea, lo voy a tener en cuenta. Hay una celebración familiar más adelante y seguro necesitaremos algo así.

**A:** También puede guardar nuestro número en su teléfono, así la próxima vez la atendemos todavía más rápido.

**B:** Buena idea, lo guardo ahora mismo para no tener que buscarlo después.

**A:** Le comento que por el monto de su pedido no aplica ninguna promoción hoy, porque el descuento empieza desde noventa soles.

**B:** Está bien, no hay problema.

**A:** ¿Cuál es su dirección?

**B:** Calle Los Naranjos ciento cincuenta y seis, en Pueblo Libre, casa de portón verde.

**A:** Calle Los Naranjos ciento cincuenta y seis, Pueblo Libre. ¿Cómo pagará?

**B:** Con Yape, ahora mismo, si me envía el código.

**A:** Claro, se lo enviaremos por mensaje. El total es sesenta y ocho soles.

**B:** Sesenta y ocho soles, correcto. ¿Atienden hasta tarde?

**A:** Hasta las once de la noche. Repito su pedido: un chaufa familiar, un tallarín saltado mixto y un wantán frito, por sesenta y ocho soles.

**B:** Así es. ¿Cuánto demoran?

**A:** Aproximadamente treinta y cinco minutos.

**B:** Muchas gracias.

**A:** A usted, buen provecho.

> Nota para el validador: Correcto: 34 + 22 + 12 = 68. El pedido no llega a 90, así que no aplica Q1 (la vendedora lo menciona: trampa para el extractor de promoción).

---

## t2_02  (llamada)

- Palabras: 409 · duración estimada: ~3.2 min
- Trampas: AUTOCORRECCIÓN (2 sopas de wantán → 1). TOTAL INCORRECTO (dice 72, correcto 62: 'sesenta y dos' vs 'setenta y dos', parece error de ASR pero es del hablante porque lo repite). Dirección con dígitos. Promo 3x2.

**A:** Chifa Dragón Dorado, buenas noches, ¿qué desea pedir?

**B:** Buenas noches. Quiero dos arroces chaufa personales y dos sopas de wantán.

**A:** Anotado. ¿Algo más?

**B:** Sí, tres gaseosas personales. Ah, y perdón, sobre las sopas: mejor una sola sopa de wantán, no dos. Solo una persona la quiere.

**A:** Entendido, entonces dos chaufas personales, una sopa de wantán y tres gaseosas personales.

**B:** Correcto. ¿Las gaseosas son de sabores variados?

**A:** Sí, tenemos de cola, de naranja y de limón.

**B:** Dos de cola y una de naranja, por favor.

**A:** Listo. Los precios son: el chaufa personal, dieciocho soles; la sopa de wantán, dieciséis soles; y cada gaseosa personal, cinco soles. Además, hoy tenemos tres por dos en gaseosas personales, o sea que por tres paga solo dos.

**B:** Qué bien, entonces las tres gaseosas me salen al precio de dos.

**A:** Así es. ¿Cuál es su dirección de entrega?

**B:** Avenida Brasil mil doscientos diez, en Breña, al lado del banco.

**A:** Avenida Brasil mil doscientos diez, Breña. ¿Y cómo va a pagar?

**B:** En efectivo. ¿Me puede avisar cuando esté llegando?

**A:** Claro, el repartidor la llamará. El total sería setenta y dos soles.

**B:** ¿Setenta y dos soles? Bueno, está bien.

**A:** Sí, setenta y dos soles en total. Llegará en cuarenta minutos más o menos.

**B:** Perfecto. ¿Pueden enviar palitos chinos?

**A:** Con gusto, le ponemos palitos, servilletas y sobrecitos de sillao.

**B:** Una cosa más: mi vecina me dijo que su pedido anterior llegó rápido. ¿Cómo hacen para que no demore?

**A:** Tenemos varios repartidores por zona y preparamos el pedido apenas termina la llamada, así que sale de la cocina en pocos minutos.

**B:** Qué eficiente. Y si llueve, ¿también llega a tiempo?

**A:** Con lluvia puede demorar un poco más, pero le avisaremos si eso pasa, para que no se preocupe.

**B:** Gracias por la sinceridad, se agradece mucho.

**A:** A usted por su paciencia. Nos esforzamos para que el pedido llegue siempre en buen estado.

**B:** Otra pregunta: ¿ustedes preparan la comida en el momento o ya la tienen lista de antes?

**A:** La preparamos en el momento, apenas recibimos el pedido. Los ingredientes llegan frescos cada mañana y por eso el sabor es distinto al de un plato recalentado.

**B:** Muchas gracias. ¿La sopa de wantán viene caliente?

**A:** Sí, la enviamos en un envase térmico para que llegue bien caliente.

**B:** Excelente, gracias.

**A:** ¿Desea agregar un postre? Tenemos helado frito, recién hecho.

**B:** No, gracias, solo eso. Es una cena sencilla en casa.

**A:** Perfecto, entonces queda tal cual. Que lo disfruten.

**B:** Igualmente.

**A:** Gracias a usted. Buenas noches.

> Nota para el validador: Correcto: 2x18 + 16 + 3x5 = 67; promo 3x2 resta una gaseosa (5) = 62. La vendedora dice 72 y la cliente lo repite igual (error del HABLANTE). Ojo: 62 vs 72 es una confusión fonética plausible del ASR: sirve para probar tu regla de diagnóstico.

---

## t2_03  (llamada)

- Palabras: 413 · duración estimada: ~3.2 min
- Trampas: AUTOCORRECCIÓN (3 chaufas familiares → 2). Total CORRECTO. Recojo en tienda (sin dirección). Pago con tarjeta.

**A:** Chifa Dragón Dorado, buenas tardes, ¿en qué le ayudo?

**B:** Buenas tardes. Quiero hacer un pedido grande para una reunión familiar, y lo voy a recoger en la tienda.

**A:** Con gusto, dígame.

**B:** Quiero tres arroces chaufa familiares, un tallarín saltado y dos porciones de wantán frito. Y una jarra de limonada.

**A:** Perfecto.

**B:** Mmm, espera, tres chaufas familiares es demasiado. Mejor dos chaufas familiares. Lo demás está igual.

**A:** Entendido: dos chaufas familiares, un tallarín saltado, dos porciones de wantán frito y una jarra de limonada.

**B:** Exacto. ¿La limonada es con hielo?

**A:** Sí, y se la preparamos con el hielo aparte para que no se diluya.

**B:** Mejor aparte, gracias.

**A:** Los precios son: chaufa familiar, treinta y cuatro soles cada uno; tallarín saltado, veintidós soles; wantán frito, doce soles cada porción; y la jarra de limonada, catorce soles. Y hoy tenemos un descuento de quince soles en pedidos desde noventa soles.

**B:** Mi pedido califica, ¿verdad?

**A:** Sí. La suma es ciento veintiocho soles, menos quince, son ciento trece soles en total.

**B:** Ciento trece soles. Perfecto.

**A:** ¿A nombre de quién será el pedido?

**B:** A nombre de Milagros.

**A:** Milagros, listo. ¿Cómo pagará?

**B:** Con tarjeta, cuando lo recoja.

**A:** Perfecto. Estará listo en treinta minutos.

**B:** Gracias. ¿Hasta qué hora atienden?

**A:** Hasta las once de la noche.

**B:** Entonces paso en un rato. ¿Tienen estacionamiento?

**A:** Sí, hay espacio al costado del local, y si está lleno puede dejar el auto en la calle.

**B:** Genial, gracias. Una cosa más: ¿pueden poner las porciones de wantán en un envase aparte para que no se humedezcan?

**A:** Claro, las empacamos aparte con su salsa de tamarindo, así llegan bien crocantes.

**B:** Perfecto, muchas gracias.

**A:** Antes de despedirnos, ¿desea que le dejemos el contacto de la tienda, por si hay algún cambio?

**B:** Sí, por favor, para avisar si tengo algún retraso en llegar.

**A:** Claro. Nuestro teléfono es el mismo desde el que usted está llamando ahora.

**B:** Ah, entonces no hace falta, queda registrado en mi teléfono.

**A:** Exacto. Y si llega antes de la hora indicada, avísenos desde la puerta y lo atendemos primero.

**B:** Qué amable, así lo haré. Gracias por todo.

**A:** Si necesita que le guardemos el pedido en un lugar tibio mientras llega, no se preocupe, lo dejamos en la zona de entrega del local con su nombre.

**B:** Muchas gracias, qué detalle. Hoy el tráfico está pesado y no sé exactamente cuánto me voy a demorar en llegar.

**A:** Repito: dos chaufas familiares, un tallarín saltado, dos wantanes fritos y una limonada, ciento trece soles. La esperamos, Milagros.

**B:** Hasta luego.

> Nota para el validador: Correcto: 2x34 + 22 + 2x12 + 14 = 128; menos 15 = 113. Total dicho 113 (correcto).

---

## t2_04  (llamada)

- Palabras: 421 · duración estimada: ~3.3 min
- Trampas: TOTAL INCORRECTO (dice 76 = olvidó el tres por dos; correcto 71). Dirección con dígitos, interior y distrito. Cantidad 4 en promo 3x2.

**A:** Chifa Dragón Dorado, buenas tardes, ¿qué desea?

**B:** Hola, buenas tardes. Quiero pedir para mi casa, para delivery.

**A:** Claro, dígame su pedido.

**B:** Un arroz chaufa personal, un tallarín saltado, una sopa de wantán y cuatro gaseosas personales.

**A:** Perfecto. ¿Las gaseosas de qué sabor?

**B:** Dos de cola y dos de naranja.

**A:** Anotado. ¿Desea algo más?

**B:** No, con eso estamos bien. Es para el almuerzo con mis sobrinos.

**A:** Qué bien. Los precios son: chaufa personal, dieciocho soles; tallarín saltado, veintidós soles; sopa de wantán, dieciséis soles; y la gaseosa personal, cinco soles cada una. Hoy tenemos tres por dos en gaseosas personales.

**B:** Entonces con cuatro gaseosas, una me sale gratis, ¿no?

**A:** Así es, por cada tres paga dos, entonces en cuatro una es gratis.

**B:** ¿Y las gaseosas llegan frías?

**A:** Sí, salen de la refrigeradora y las enviamos en una bolsa aparte para que no se golpeen.

**B:** Perfecto.

**A:** ¿Quiere que le enviemos los palitos y los cubiertos en bolsas separadas?

**B:** Sí, por favor, porque mis sobrinos no usan palitos y prefieren tenedor.

**A:** Anotado. También podemos enviar los sobrecitos de sillao y de ají, por si alguien los desea.

**B:** Perfecto, mándelos todos. A mis sobrinos les encanta mezclar la salsa con toda la comida.

**A:** Qué lindo. Entonces los incluimos. Si hay algún ingrediente que alguien en la mesa no coma, avísenos para tener cuidado.

**B:** No hay ninguno, gracias, en mi casa comemos de todo.

**A:** Un detalle más: si alguien de la familia prefiere comida menos grasosa, la cocina puede prepararla con menos aceite, solo avíseme.

**B:** Qué amable. Mi hermana siempre pide eso, así que le diré que lo tienen. Gracias por avisarme.

**A:** Con eso ya estaría todo anotado. Si recuerda algo más, todavía estamos a tiempo de agregarlo al pedido.

**B:** Creo que no me falta nada, pero se lo agradezco, es usted muy atenta.

**A:** ¿Cuál es su dirección de entrega?

**B:** Jirón Lampa ciento ochenta y cinco, interior tres, en el Cercado de Lima.

**A:** Jirón Lampa ciento ochenta y cinco, interior tres, Cercado de Lima. ¿Cómo pagará?

**B:** En efectivo. ¿Tiene sencillo el repartidor? Voy a pagar con un billete de cien.

**A:** Sí, llevará vuelto. El total sería setenta y seis soles.

**B:** ¿Setenta y seis soles? Está bien.

**A:** Sí, setenta y seis soles. Su pedido llegará en cuarenta y cinco minutos.

**B:** Gracias. ¿El tallarín viene con verduras?

**A:** Sí, con verduras salteadas, cebolla china y pimiento.

**B:** Perfecto. ¿Y el chaufa lleva huevo?

**A:** Sí, lleva huevo, cebolla china y trocitos de pollo o cerdo, según prefiera.

**B:** De pollo, por favor.

**A:** Anotado, de pollo. Gracias por su pedido.

**B:** Gracias a usted.

> Nota para el validador: Correcto: 18 + 22 + 16 + 4x5 = 76; promo 3x2 con 4 gaseosas regala 1 (5) = 71. La vendedora dice 76 (no aplicó la promo) y lo repite.

---

## t2_05  (llamada)

- Palabras: 417 · duración estimada: ~3.3 min
- Trampas: AUTOCORRECCIÓN (2 tallarines → 3). TOTAL INCORRECTO (dice 148, correcto 143: la vendedora restó 10 en vez de 15; 'cuarenta y ocho' vs 'cuarenta y tres' es una confusión plausible de ASR). Dirección con dígitos y piso.

**A:** Chifa Dragón Dorado, buenas tardes, ¿cómo puedo ayudarle?

**B:** Buenas tardes, quiero hacer un pedido para el almuerzo de mi oficina, para delivery.

**A:** Claro, dígame.

**B:** Quiero dos arroces chaufa familiares, dos tallarines saltados y dos porciones de wantán frito.

**A:** Perfecto.

**B:** Pensándolo bien, mejor tres tallarines saltados, porque somos nueve personas y los chaufas no alcanzan para todos.

**A:** Entendido, dos chaufas familiares, tres tallarines saltados y dos porciones de wantán frito.

**B:** Así es. ¿Pueden hacer los tallarines sin picante?

**A:** Sin problema, los anotamos sin ají.

**B:** Una consulta: ¿el wantán frito viene caliente o hay que recalentarlo?

**A:** Sale recién hecho, pero si el reparto demora, se puede pasar unos minutos por la sartén para que quede crocante.

**B:** Entendido. Y los tallarines, ¿vienen con carne o con pollo?

**A:** Si no nos dice nada, los preparamos mixtos, con carne y pollo.

**B:** Gracias.

**A:** Los precios son: chaufa familiar, treinta y cuatro soles cada uno; tallarín saltado, veintidós soles cada uno; y la porción de wantán frito, doce soles. Hoy tenemos descuento de quince soles en pedidos desde noventa soles, y su pedido califica.

**B:** Qué bien.

**A:** ¿Cuál es su dirección?

**B:** Avenida La Marina tres mil cuatrocientos veinte, en Los Olivos, edificio de oficinas, piso cuatro.

**A:** Avenida La Marina tres mil cuatrocientos veinte, Los Olivos, piso cuatro. ¿Cómo desea pagar?

**B:** Con Yape.

**A:** Perfecto, le enviaremos el código. El total sería ciento cuarenta y ocho soles.

**B:** ¿Ciento cuarenta y ocho? De acuerdo.

**A:** Sí, ciento cuarenta y ocho soles. Llegará en cincuenta minutos, más o menos.

**B:** ¿Se puede entregar antes de las doce? Tenemos una reunión.

**A:** Haremos lo posible, lo ponemos como prioridad.

**B:** ¿Y pueden enviar platos descartables para todos?

**A:** Claro, le enviamos platos, cubiertos y servilletas para nueve personas.

**B:** Una cosa más: en el edificio hay vigilante en la entrada. ¿El repartidor puede avisar desde la portería?

**A:** Claro, le pedimos que pregunte por usted en la portería y que la llame por teléfono para que baje a recoger el pedido.

**B:** Perfecto, porque la oficina queda dentro de un edificio grande y a veces no se escucha el timbre.

**A:** Entendido. Lo anotamos en la hoja del pedido para que no haya confusión.

**B:** Y si llega antes de lo previsto, ¿puede esperar abajo unos minutos?

**A:** Sí, sin problema. Esperará en la entrada hasta que usted baje.

**B:** Otra cosa: como somos varios, ¿pueden mandar todo bien separado por bolsas para repartirlo más fácil?

**A:** Claro, separamos todo en bolsas y marcamos cada una por contenido, para que se repartan fácil sin abrir todas.

**B:** Muchas gracias.

**A:** Gracias a usted, buenas tardes.

> Nota para el validador: Correcto: 2x34 + 3x22 + 2x12 = 158; menos 15 = 143. La vendedora dice 148 y la cliente lo repite (error del HABLANTE).

---


---
