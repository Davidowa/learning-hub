# Fundamentos del comercio electrónico

Este curso organiza conceptos, implementación y evidencia en 17 sesiones. Cada práctica usa únicamente conceptos de la sesión y de las anteriores.

## Evaluación

| Componente | Peso | Entrega |
|---|---:|---|
| Parcial 1 | 20 % | w08 |
| Parcial 2 | 20 % | w13 |
| Proyecto integrador | 20 % | w16 |
| Examen final | 20 % | w17 |
| Tareas y laboratorios | 20 % | w01-w16 |

## Sesiones

### 01. Comercio digital: modelos, canales y quién controla qué

- Modelo de negocio: El modelo identifica quién vende a quién. El canal identifica dónde comienza la transacción.
- Control del canal: Precio, datos, cobro, entrega y atención pueden depender de participantes distintos. Asigna cada responsabilidad antes de elegir un canal.
- Recorrido del pedido: Rastrea descubrimiento, confianza, cobro, entrega y resolución de un pedido. Cada transferencia necesita responsable y evidencia.

Práctica: Mapa de 10 negocios: los equipos colocan diez tarjetas de negocios en una cuadrícula de modelo por canal y responden las cinco preguntas de control de cada uno. Cierran proponiendo dos posiciones de canal para Molienda y escribiendo, en una línea cada una, qué control les cuesta.

### 02. Cliente, propuesta de valor y evidencia

- Evidencia del cliente: Describe el comportamiento previo del cliente antes de proponer una solución. Distingue observaciones de supuestos.
- Propuesta de valor: Relaciona una necesidad con un beneficio específico y una razón para confiar en el vendedor. Prueba primero la parte incierta.
- Validación: Una declaración de interés, una acción y un pago representan compromisos diferentes. Define el umbral de decisión antes de reunir evidencia.

Práctica: Clínica de entrevistas en parejas: convierte preguntas malas en buenas e intercambia con otra pareja para marcar las inductivas. Después, diseña la prueba de una semana para la suscripción de Molienda con el umbral fijado de antemano, por ejemplo al menos 20 depósitos reembolsables de 400 visitas, y escribe qué harías si no se alcanza.

### 03. La economía de un pedido

- Base del ingreso: Separa el total al cliente del ingreso neto de impuestos. El ejercicio proporciona los supuestos de impuesto de cada producto.
- Margen y markup: El margen bruto divide la utilidad bruta entre ingreso. El markup divide esa utilidad entre costo. Sus denominadores son distintos.
- Contribución del pedido: Resta costo de producto y costos variables del pedido al ingreso neto. Un margen bruto positivo puede coexistir con una contribución negativa.

Práctica: En hoja de cálculo, el estado de resultados de tres canastas de Molienda: una bolsa de 250 g, el pedido #1001 (dos bolsas de 250 g a $289 y un molino de $1,490, total $2,068 MXN) y un mes de suscripción. Las líneas de comisión, pago y envío quedan marcadas para llenarse en w04, w07 y w10 con valores ilustrativos de hoy. Encuentra la canasta que pierde dinero, propón un ajuste (umbral, paquete o precio) y pruébalo con números.

### 04. Plataformas: rentar, comprar o construir

- Costo total de propiedad: Incluye suscripción, alojamiento, integración, soporte, actualizaciones y salida durante un periodo definido. Un precio inicial bajo puede ocultar trabajo posterior.
- Control de la plataforma: Compara control de datos, precios, políticas y relación con el cliente. Rentar software y rentar audiencia resuelven necesidades diferentes.
- Integración y salida: Define cómo entran y salen registros de productos, pedidos y clientes. Prueba una exportación antes de depender del proveedor.

Práctica: Tres caminos para Molienda: con una tabla de tarifas ilustrativa, calcula el costo mensual a 50, 300 y 2,000 pedidos para solo marketplace, tienda SaaS y código abierto. Grafica el punto de cruce, llena la línea de comisión del estado de resultados del pedido #1001 y completa la ficha de evaluación de la opción elegida, con plan de salida a 90 días.

### 05. Catálogo y datos de producto

- Producto y SKU: Un producto puede tener varias variantes vendibles. Cada SKU identifica una unidad de inventario y un paquete combina unidades.
- Atributos y taxonomía: Los atributos describen el artículo. Las categorías organizan su búsqueda. Usa valores consistentes para que funcionen filtros y comparaciones.
- Publicación de datos: Conserva una especificación revisada como fuente de descripciones, imágenes y feeds. Comprueba cada afirmación generada contra esa especificación.

Práctica: Construye el catálogo de Molienda (tres tuestes en grano o molido y en 250 g o 1 kg, más el molino y la suscripción) en una tabla de SKU con convención de nombres y GTIN de ejemplo; mapea un producto a dos taxonomías de canal y verifica línea por línea una descripción escrita con IA que trae tres errores sembrados.

### 06. Experiencia de compra, página de producto y embudo

- Incertidumbre de compra: La página debe explicar producto, precio total, promesa de entrega y condiciones de resolución. El cliente necesita esos datos antes de pagar.
- Denominadores del embudo: La conversión de una etapa usa como denominador a quienes entraron a ella. Compara por separado pérdida relativa y pedidos perdidos.
- Acceso y usabilidad: Comprueba operación con teclado, etiquetas, texto legible y recuperación de errores. Una revisión automática cubre solo parte de la experiencia.

Práctica: Desarma la página de producto para celular de Molienda (maqueta con defectos sembrados) con los datos de embudo dados: evaluación heurística, recorrido de accesibilidad con verificador y teclado, y una decisión escrita sobre qué paso arreglar primero y por qué.

### 07. Pagos: cómo se mueve el dinero

- Ciclo del pago: Autorización, captura, liquidación y abono al comercio son eventos distintos. El surtido depende del estado de confirmación requerido.
- Comisiones y tiempos: Compara comisión porcentual, cargo fijo y demora del abono. Usa el contrato del proveedor y la hoja de comisiones del ejercicio.
- Evidencia del pago: Una captura es una afirmación de pago. Concilia la notificación del proveedor y el movimiento acreditado antes de liberar el pedido.

Práctica: La mezcla de pagos de Molienda: con una tabla de segmentos (joven sin tarjeta de crédito, comprador de oficina que pide factura, cliente de molino) y una tabla de tarifas ilustrativa, elige métodos, calcula el costo de pago ponderado por pedido, llena la línea de pago del pedido #1001, decide si ofrecer MSI solo en molinos y completa la ficha de evaluación de un proveedor de pagos.

### 08. Checkout, confianza y optimización de conversión

- Información del checkout: Muestra el cargo completo, las condiciones de entrega y el contacto del vendedor antes de confirmar. Explica errores sin borrar entradas válidas.
- Diseño de la prueba: Define asignación aleatoria, métrica principal y regla de cierre antes de una prueba A/B. Estima los datos necesarios para el efecto de interés.
- Confianza y persuasión: Usa reseñas, inventario y ofertas veraces. Un aumento de conversión debe conservar margen y resultados para el cliente.

Práctica: El checkout de siete pasos de Molienda, con unas 6,000 sesiones al mes: rediséñalo, escribe dos hipótesis y comprueba con la tabla de tamaños de muestra si una prueba A/B es factible. El hallazgo esperado es que solo los efectos grandes se detectan, así que primero va una prueba de usabilidad. Lab corto por la semana de examen.

### 09. Pedidos, inventario y riesgo

- Estados del pedido: Registra pago y surtido por separado. Un pago reembolsado y un paquete devuelto describen partes distintas del pedido.
- Inventario disponible: El inventario disponible es existencia menos reservas e inventario de seguridad. Una sincronización tardía puede ofrecer la misma existencia en varios canales.
- Eventos duplicados: Guarda un identificador estable y atiende una notificación repetida sin repetir su efecto. Confirma el procesamiento antes de responder.

Práctica: El viaje del pedido #1001: una bitácora de eventos revuelta con un webhook duplicado y un conflicto de inventario entre la tienda y Mercado Libre. Reconstruye la historia del pedido en una tabla de traza, encuentra la sobreventa y decide qué hacer con tres pedidos sospechosos.

### 10. Fulfillment y última milla

- Flujo de surtido: Recibe, almacena, selecciona, empaca y envía con una comprobación en cada transferencia. La promesa depende de capacidad y horarios de corte.
- Peso cobrable: Compara peso físico y volumétrico según el contrato del transportista. El ejercicio proporciona dimensiones, divisor y reglas de redondeo.
- Recuperación de la entrega: Define quién atiende entrega fallida, daño y falta de actualización. Incluye estos costos en el cálculo del pedido.

Práctica: Para Molienda: elige el modelo de fulfillment a tres volúmenes, calcula el peso facturable de tres cajas, escribe promesas de entrega desde Coatepec para CDMX, Guadalajara, Monterrey y Mérida, lleva el envío al estado de resultados del pedido #1001 y completa la ficha de evaluación de un proveedor logístico.

### 11. Devoluciones, posventa y facturación

- Operación de devoluciones: Separa decisión del cliente, transporte de retorno, inspección y reembolso. Registra una causa útil para mejorar catálogo o surtido.
- Conciliación del reembolso: Concilia el monto reembolsado con pago y pedido originales. Un paquete devuelto no demuestra que el dinero se reembolsó.
- Evidencia de facturación: Relaciona factura, pedido, pago y documento del reembolso. Determina el tratamiento fiscal con reglas vigentes y hechos de la operación.

Práctica: El escritorio de posventa de Molienda resuelve seis casos: un molino dañado, una molienda equivocada, un arrepentimiento al día 3, una factura pedida un mes después, el reembolso de un pedido facturado y una reseña que se queja de entrega tardía. Para cada uno: derecho del cliente, acción, costo y documento CFDI.

### 12. Adquisición: llegar al cliente correcto

- Canales de adquisición: Separa canales del negocio, exposición obtenida y distribución pagada. Registra audiencia y propósito de cada campaña.
- CAC y ROAS: CAC divide gasto de adquisición entre clientes adquiridos. ROAS divide ingreso atribuido entre gasto publicitario. Ninguno representa utilidad de contribución.
- Publicidad en equilibrio: Con una proporción de contribución m antes de publicidad, el ROAS de equilibrio simple es 1/m. Declara costos incluidos y supuestos de atribución.

Práctica: La tabla de campañas de Molienda (Meta, Google, Mercado Ads y un creador): calcula CAC, ROAS y ROAS de equilibrio, reasigna el presupuesto, etiqueta tres enlaces y completa la ficha de evaluación de un canal de anuncios. Cierra con un acertijo abierto a propósito: Meta reporta 40 compras, la analítica 25 y la tienda 32. ¿Por qué? Se responde en w13.

### 13. Medición y decisiones

- Definición de métricas: Declara población, unidad de observación, periodo y denominador. Sesión, cliente, pedido y artículo son unidades distintas.
- Conciliación: Compara pedidos, pagos y eventos mediante identificadores estables. Investiga faltantes y duplicados antes de decidir.
- Atribución y causa: La atribución asigna crédito según una regla. Un experimento con grupo de control puede estimar impacto incremental. Cada pregunta necesita evidencia distinta.

Práctica: Explora la cuenta demo de GA4 (embudo y adquisición de tráfico por UTM). Escribe el plan de medición de Molienda y construye la tabla de conciliación que resuelve el acertijo de w12, incluido un evento de compra duplicado sembrado en los datos. Lab corto por la semana de examen.

### 14. Retención y valor del cliente

- Retención por cohorte: Compara clientes que comenzaron en el mismo periodo y tuvieron igual oportunidad de volver. Una cohorte reciente tiene menos tiempo observado.
- Contribución del cliente: Estima valor a partir de contribución de compras observadas o modeladas. Declara horizonte, costos e incertidumbre antes de compararlo con CAC.
- Mensajes del ciclo de vida: Relaciona cada mensaje con una necesidad y una finalidad de contacto permitida. Ofrece una forma funcional de detener mensajes promocionales.

Práctica: Con una exportación de 12 meses de pedidos de Molienda (unas 500 filas) construye la tabla de cohortes, los segmentos RFM y el LTV. Después diseña en papel un flujo de suscripción que cumpla la ley.

### 15. Ley, privacidad y ética

- Información al consumidor: Relaciona información de producto, precio completo, contacto y resolución con el punto de decisión. Revisa la ley de consumo vigente aplicable.
- Datos personales: Define finalidad, datos necesarios, acceso, conservación y atención de derechos. En México, revisa la ley vigente para particulares y su autoridad competente.
- Ley, política y ética: Una regla de plataforma y una obligación legal tienen fuentes distintas. Evalúa también el daño al cliente aunque un patrón esté permitido técnicamente.

Práctica: Auditoría legal de Molienda: quince capturas (checkout, banner de cookies, flujo de suscripción, página de producto, aviso de privacidad). Encuentra las violaciones y los patrones engañosos, reescribe cada uno y redacta los elementos del aviso de privacidad.

### 16. Evaluar la siguiente herramienta

- Responsabilidades de los sistemas: Asigna una fuente autorizada para productos, pedidos, inventario y clientes. Define cómo cruza cada cambio los límites del sistema.
- Evidencia de herramientas: Compara una afirmación del proveedor con una prueba en el contexto pertinente. Declara costo de integración, mantenimiento y ruta de salida.
- Piloto reversible: Define hipótesis, métrica, periodo y regla de suspensión. Conserva el flujo anterior hasta que el nuevo cumpla los criterios.

Práctica: Lab corto: cada equipo saca una tarjeta de tendencia (checkout dentro de un asistente, transmisiones en vivo, publicidad de marketplaces, llaves de acceso, marketplaces sociales) y produce para Molienda una ficha de evaluación y un plan piloto. Después vienen las presentaciones del proyecto.

### 17. Evaluación final

- Diagnóstico integrado: Explica un resultado con cálculo del pedido, embudo y evidencia operativa. Comprueba que la acción propuesta atienda la causa diagnosticada.
- Decisión con incertidumbre: Identifica qué respaldan los datos y qué sigue desconocido. Propón la siguiente medición cuando la incertidumbre cambie la decisión.
- Defensa individual: Reproduce un cálculo, explica una decisión e identifica un límite sin depender de una marca. Cada integrante debe comprender el trabajo entregado.

Práctica: Ronda de práctica en parejas: ocho reactivos, dos por fase.

## Reglas de entrega

Declara herramientas de asistencia y conserva evidencia reproducible. Cada integrante debe explicar el trabajo. El enunciado de cada examen define los materiales permitidos.
