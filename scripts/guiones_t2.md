# Guiones — Tarea 2: Llamadas de venta (restaurante)

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
