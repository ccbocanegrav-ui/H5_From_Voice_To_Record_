# Guiones — Tarea 1: Entrevistas

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

**A:** Hola, Alejandra, bienvenido. Antes de empezar, para alinear expectativas: ¿cuál es tu pretensión salarial?

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
