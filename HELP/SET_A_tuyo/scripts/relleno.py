"""Relleno conversacional (SET A) para llevar cada clip a ~3.3-3.7 min.

Alinea el corpus con lo que pide el caso: 4-5 clips de 2-4 min y ~16-20 min de audio por tarea.
Regla: el relleno NO menciona valores de ningún campo (puestos, años, tecnologías, salarios,
disponibilidad, inglés / productos, precios, cantidades, promos, direcciones, pagos), para que
el ground truth no cambie.

Formato:  id_clip -> (linea_ancla, [(hablante, texto), ...])
El bloque se inserta justo DESPUÉS de la línea ancla (igualdad exacta, o prefijo si es larga).
"""

RELLENO = {
    # ---------------------------------------------------------------- T1 (A entrevista, B candidata/o)
    "t1_01": ("Divido el trabajo en entregas pequeñas", [
        ("A", "Cuéntame cómo es un día normal en tu trabajo."),
        ("B", "Empiezo revisando que los procesos de la noche hayan terminado bien. Después atiendo los pedidos de información de las otras áreas y dejo las tardes más libres para los análisis largos, que necesitan concentración."),
        ("A", "¿Y cómo priorizas cuando varias personas te piden algo al mismo tiempo?"),
        ("B", "Pregunto para qué lo necesitan y cuándo lo van a usar. Muchas veces algo que parece urgente puede esperar, y otras cosas que parecen pequeñas son las que más pesan en la decisión de alguien."),
        ("A", "¿Recuerdas algún desacuerdo con un compañero sobre cómo medir un resultado?"),
        ("B", "Sí, y lo resolvimos sentándonos con los datos delante. Probamos las dos formas, vimos cuál respondía mejor a la pregunta del cliente y terminamos usando una mezcla de ambas."),
    ]),
    "t1_02": ("Perfecto, me parece bien.", [
        ("A", "Antes de cerrar, cuéntame cómo recibes los comentarios sobre tu trabajo."),
        ("B", "Los escucho con calma y trato de no defenderme de inmediato. Si alguien me señala algo en mi código, primero intento entender qué ve esa persona que yo no vi, y después decido qué cambiar."),
        ("A", "¿Y cuando tú tienes que dar un comentario difícil a un compañero?"),
        ("B", "Lo hablo en privado y empiezo por lo que está bien. Después explico el problema con un ejemplo concreto y propongo una alternativa, para que no suene como una crítica a la persona."),
        ("A", "¿Qué haces cuando sientes que un plazo no es realista?"),
        ("B", "Lo digo cuanto antes y con razones. Prefiero proponer una entrega más pequeña y a tiempo que prometer todo y llegar con algo a medias. Casi siempre el equipo lo agradece."),
    ]),
    "t1_03": ("Tengo un calendario semanal", [
        ("A", "Cuéntame cómo aprendes cosas nuevas cuando no conoces el tema."),
        ("B", "Primero busco ejemplos sencillos y los copio para entender cómo funcionan. Luego intento hacer algo parecido por mi cuenta, sin mirar, y si me atasco, regreso a revisar. Así lo que aprendo se me queda."),
        ("A", "¿Qué haces cuando un compañero te explica algo y no lo entiendes del todo?"),
        ("B", "Se lo digo con sinceridad y le pido un ejemplo. Antes me daba vergüenza, pero ahora sé que preguntar a tiempo me ahorra errores y me hace aprender más rápido."),
        ("A", "¿Cómo te gustaría que fueran tus primeros días en un trabajo nuevo?"),
        ("B", "Me gustaría conocer al equipo, entender para qué sirve lo que hago y tener a alguien a quien preguntar sin miedo. Con eso me siento segura y empiezo a aportar antes."),
    ]),
    "t1_04": ("Reviso que los datos lleguen completos", [
        ("A", "Has liderado equipos antes. ¿Cómo repartes el trabajo cuando alguien está sobrecargado?"),
        ("B", "Primero hablo con la persona para entender qué la está agobiando. A veces el problema es la cantidad de tareas, y otras veces es que le tocó algo para lo que no se siente preparada. Según el caso, redistribuyo o acompaño."),
        ("A", "¿Qué haces cuando un integrante nuevo no rinde como esperabas?"),
        ("B", "Reviso primero si le expliqué bien lo que esperaba de su trabajo, porque muchas veces el problema es de comunicación. Después acordamos metas pequeñas y nos vemos con frecuencia para ver cómo va."),
        ("A", "¿Cómo celebras los logros del equipo?"),
        ("B", "Me gusta reconocer en público lo que cada persona hizo bien, con detalles. Decir gracias por el trabajo del equipo suena bonito, pero mencionar qué hizo cada uno es lo que realmente motiva."),
    ]),
    "t1_05": ("Me gusta correr los fines de semana", [
        ("A", "Cuéntame cómo te preparas cuando tienes que presentar resultados a la gerencia."),
        ("B", "Primero imagino qué preguntas me harían y preparo respuestas cortas. Después ensayo la presentación en voz alta con un compañero, que me ayuda a ver dónde me enredo y qué parte sobra."),
        ("A", "¿Y si alguien cuestiona tus conclusiones en plena reunión?"),
        ("B", "Escucho la objeción completa antes de responder. Si tiene razón, lo reconozco y me comprometo a revisar. Si no, explico con calma de dónde sale el resultado y ofrezco enseñar los datos después."),
        ("A", "¿Qué es lo que más valoras de un buen jefe o jefa?"),
        ("B", "Que confíe en mí, pero que también esté cerca cuando lo necesito. Me gusta que me den libertad para organizarme, siempre que sepa claramente qué resultados se esperan."),
    ]),

    # ---------------------------------------------------------------- T2 (A vende, B compra)
    "t2_01": ("No, gracias, así está bien.", [
        ("A", "Si lo desea, puede dejar una indicación para el repartidor, por ejemplo cómo reconocer su casa."),
        ("B", "Sí, gracias. El portón es de color gris y hay un árbol grande en la entrada. Si no encuentra el número, que llame al celular que les dejé."),
        ("A", "Perfecto, lo anoto en la hoja del pedido. El repartidor es de la zona y conoce bien las calles."),
        ("B", "Qué bien, porque la última vez que pedí a otro lugar el repartidor se perdió y la comida llegó fría."),
        ("A", "Lamentamos que le haya pasado. Nosotros usamos bolsas térmicas y revisamos todo el pedido antes de que salga del local."),
        ("B", "Eso me tranquiliza mucho, gracias por explicármelo con tanta paciencia."),
    ]),
    "t2_02": ("Perfecto.", [
        ("A", "Mientras preparamos todo, ¿desea que le avisemos cuando el repartidor salga del local?"),
        ("B", "Sí, por favor, con un mensaje al celular. Así bajo a recibir el pedido y no lo dejo esperando en la puerta."),
        ("A", "Perfecto, así lo haremos. También puede seguir el avance llamándonos a este mismo número."),
        ("B", "Qué bueno. Es que tengo una reunión por videollamada más tarde y no quiero perder el pedido."),
        ("A", "Entiendo. Le avisaremos con anticipación para que esté pendiente y pueda conectarse tranquila."),
        ("B", "Muchas gracias, qué amable, se lo agradezco de verdad."),
        ("A", "Le comento que el local atiende hasta tarde, así que si necesita algo más, puede volver a llamarnos."),
        ("B", "Gracias, lo tendré presente. Es bueno saber que atienden hasta tan tarde."),
    ]),
    "t2_03": ("Genial, con ají y mayonesa, por favor.", [
        ("A", "¿Prefiere que las cremas vayan en recipientes aparte o directamente sobre la ensalada?"),
        ("B", "Aparte, por favor, porque a mi hijo no le gusta el picante y así cada uno se sirve lo que quiere."),
        ("A", "Entendido, las enviamos en recipientes pequeños y cerrados para que no se derramen en el camino."),
        ("B", "Qué bueno. Y también necesito servilletas y cubiertos suficientes, porque vienen invitados a la casa."),
        ("A", "Claro, incluimos servilletas y cubiertos para todos. Si necesita más, avísenos ahora y lo agregamos."),
        ("B", "Con eso está bien, muchas gracias por la atención."),
        ("A", "Si le gustó la atención, puede dejarnos su opinión en nuestras redes cuando guste. Siempre nos ayuda a mejorar."),
        ("B", "Claro, con gusto. Siempre recomiendo los lugares que me tratan bien."),
    ]),
    "t2_04": ("Está bien.", [
        ("A", "Mientras tanto, ¿viene con mucho apetito hoy?"),
        ("B", "Sí, muchísimo. Hoy tuve un día larguísimo en el trabajo y casi no tuve tiempo de almorzar."),
        ("A", "Entonces lo vamos a atender rápido. Si quiere, puedo avisar a la cocina para que prioricen su pedido."),
        ("B", "No hace falta, gracias. Prefiero tener hambre para disfrutar todo cuando llegue a la tienda."),
        ("A", "Muy bien. Le comento que la cocina está tranquila en este momento, así que no debería demorar nada."),
        ("B", "Qué buena noticia, justo lo que necesitaba escuchar después de un día así."),
        ("A", "¿Es la primera vez que nos visita o ya es cliente frecuente?"),
        ("B", "Vine una vez con unos amigos hace tiempo y me gustó mucho, por eso decidí volver hoy."),
        ("A", "Qué bueno saberlo. Siempre estamos mejorando la atención y la cocina, así que esperamos que note la diferencia."),
        ("B", "Seguro que sí. Ojalá mantengan el mismo sabor, que es lo que más me gustó."),
    ]),
    "t2_05": ("Muchas gracias por su preferencia, nos alegra saberlo.", [
        ("B", "Sí, siempre llega bien. Por eso lo recomendé en mi oficina y varios compañeros se animaron a probar."),
        ("A", "Muchas gracias por la recomendación. Si quiere, le puedo enviar nuestro número de contacto para que se lo pase a ellos."),
        ("B", "Sí, mejor. A veces quieren pedir por su cuenta y no saben a quién llamar."),
        ("A", "Con gusto. También atendemos pedidos grandes para eventos, si alguna vez lo necesitan, con anticipación."),
        ("B", "Lo tendré en cuenta, porque en diciembre hacemos una reunión de fin de año en la oficina."),
        ("A", "Qué bueno, ojalá podamos atenderlos. Con tiempo, le ayudamos a organizar todo."),
        ("B", "Por cierto, ¿tienen una carta que pueda mostrarles a mis compañeros?"),
        ("A", "Sí, le puedo enviar la carta completa por mensaje, con fotos de cada plato, para que la compartan."),
    ]),
}
