# Sesión D · Reescribir los ejemplos de COM101 en clave de ingeniería

Corre en paralelo con las sesiones A, B y C. Tú vives en
`ppts/python/analisis-y-diseno-de-algoritmos/`. Nadie más toca esa carpeta.

## De dónde viene el encargo

COM101 se creó clonando Análisis de Datos (TIA502) y cambiándole el nombre, la
clave y la facultad. La estructura sirve y el syllabus ya se reescribió para que
la agenda semanal siga a lo que los decks enseñan de verdad.

Lo que no se tocó es **de qué hablan los ejemplos**. Siguen siendo los de una
materia de negocios.

## El encargo

Cambiar el dominio de los ejemplos, no la pedagogía ni la secuencia.

Los ejemplos de finanzas no están mal y no hay que exterminarlos. Un ingeniero
industrial calcula costos y un mecatrónico cotiza. Lo que falta es que el curso
se vea como lo que es: la primera materia de programación de **doce carreras de
ingeniería**, en primer semestre.

La diferencia práctica: hoy los ejemplos son cálculos sobre una tabla. Deberían
ser, cada vez más conforme avanza el semestre, **piezas de un sistema**.

## Lo que hay que medir antes de decidir

```bash
cd ppts
grep -rc "ventas\|campaña\|hoja de cálculo\|Excel" python/analisis-y-diseno-de-algoritmos/es/*.yaml
```

Hoy: 80 menciones de ventas, 36 de campaña, 21 de hoja de cálculo, 10 de Excel.
No es un `sed`. Cada una es un ejemplo con sus números y su explicación
alrededor, y los números tienen que seguir siendo ciertos después.

## Un hilo de dominio, no ejemplos sueltos

La tentación es cambiar "ventas" por "sensores" y seguir. Sale peor: quedan
veinte dominios distintos y ninguno se construye.

Propuesta, y si tienes una mejor, úsala y dilo: **un sistema hotelero como
espina dorsal**, que crece con el temario.

| Semanas | Tema | Qué es el ejemplo |
|---|---|---|
| 2–3 | Algoritmos, pseudocódigo | El check-in como diagrama de flujo |
| 4–5 | Tipos, entrada y salida | Una reservación: folio, noches, tarifa, ocupada |
| 6–7 | Selección | Tarifa por temporada, cupo, penalización por cancelar |
| 8–9 | Repetición | Recorrer las noches de una estancia, acumular el total |
| 10–11 | Funciones | `calcularTotal`, `hayDisponibilidad`, `aplicarDescuento` |
| 12–13 | Colecciones | Las habitaciones como lista, el catálogo de tarifas como diccionario |
| 14 | Archivos | El registro de transacciones del día, en CSV |
| 15–16 | pandas y gráficas | Ocupación por mes, ingreso por tipo de habitación |

Sirve porque en la semana 2 es un diagrama de flujo de tres cajas y en la 16 es
un sistema con transacciones, y el alumno vio crecer la misma cosa.

Otros que funcionan igual de bien, por si el hotel no te convence: préstamos de
biblioteca, órdenes de producción en una línea, tickets de soporte. Lo que
importa es que tenga **transacciones**, o sea eventos con fecha, monto y estado,
porque eso es lo que da material para las tres cosas a la vez: selección,
repetición y archivos.

## Lo que no se toca

**La secuencia.** El syllabus ya quedó alineado semana por semana con los decks.
Si cambias qué se enseña y cuándo, el syllabus vuelve a mentir.

**El nivel.** Primer semestre, sin prerrequisitos. El dominio tiene que
entenderse sin saber de hoteles. Si un ejemplo necesita explicar el negocio
antes de explicar el `if`, el ejemplo está mal.

**Los tres bloques por deck y el número de láminas.** Estás cambiando el
contenido de las tarjetas, no la arquitectura.

## Dos cosas que sí hay que replantear, no solo traducir

**El argumento de por qué existe la materia.** La semana 1 abre con el techo de
filas de Excel, 1,048,576, y con que un clic no deja rastro. Ese argumento es
buenísimo para Empresariales y flojo para COM101: un alumno de Mecatrónica en
primer semestre no llega quejándose de Excel. El argumento de esta materia es
otro, y está en su propio syllabus: aprender a analizar y diseñar algoritmos
como base de toda la programación que viene después.

**El puente desde Excel.** `w01.1` existe para decir "lo que ya sabes hacer en
hojas de cálculo, dicho en Python". Para TIA502 es el corazón del curso. Para
COM101 decide si sigue siendo un puente o si estorba. Los dos caminos son
defendibles; el que no lo es, es dejarlo por inercia.

## Los datos

Los CSV de las semanas 14 a 16 viven en
`docs/en/courses/python-course/06 - Advanced/data/` y se regeneran con
`make_datasets.py` desde una semilla fija, así que los números que digas en
clase siempre coinciden con el archivo.

Si cambias el dominio a hotel, hacen falta datos de hotel. Extiende ese
generador en vez de escribir CSV a mano, y consérvale la semilla fija. Si no,
cada rebuild cambia los números de las láminas y ninguna cifra se puede afirmar.

## Reglas de la casa que aplican

- **Los números se miden.** Si una lámina dice un resultado, córrelo antes.
  Todo COM103 se escribió así y ahí es donde salieron los hallazgos que valen.
- **Sin `notes:`.** Se quitaron de los cuatro cursos, 309 bloques.
- **El acento significa una cosa: esto es el riesgo.** Solo en anotación de
  código cuyo rótulo ya lo diga.
- **Sin em dashes.** El separador de la casa es el punto medio.
- **Español mexicano neutro.**
- **Subtítulo de portada: unos 130 caracteres.** Pasando de ahí se va a tres
  líneas y ningún chequeo se queja.
- **No etiquetes al lector.** Ya se quitó "por qué un alumno de negocios aprende
  a programar" de las portadas. No vuelvas a meter frases que le digan al
  alumno que esto no es lo suyo.

## Verificar

```bash
cd ppts
python -m kit.preflight python/analisis-y-diseno-de-algoritmos
python -m kit.build      python/analisis-y-diseno-de-algoritmos
python -m kit.lint       python/analisis-y-diseno-de-algoritmos
python -m kit.sizes      python/analisis-y-diseno-de-algoritmos
python -m kit.preview    python/analisis-y-diseno-de-algoritmos/es/w06.es.pptx w06 --cols 8
```

Los cuatro en cero, y mira la hoja de contactos antes de dar una semana por
buena. Borra el PNG después.

Cuidado con dos cosas al reescribir tarjetas de código: la línea más larga son
63 caracteres y el alto útil son 13.9 renglones. `preflight` te lo dice antes de
construir. Y una tabla de siete renglones solo cabe si ninguna celda se envuelve.

## Orden sugerido

De la 1 a la 17 en español, y el inglés detrás de cada semana, no al final. Los
dos idiomas divergen en longitud: el inglés desborda donde el español no, y es
más barato descubrirlo semana por semana.

## Lo que viene después, y no es tuyo todavía

COM101 no tiene cuadernos de Colab. Cuando los decks estén reescritos, alguien
va a clonarlos desde los de TIA502 igual que se clonaron los decks. Deja tu
HANDOFF de curso en condiciones para que esa sesión no tenga que adivinar qué
dominio elegiste.

## Al terminar

Reporta cuántas semanas quedaron reescritas, qué dominio elegiste y por qué, y
qué ejemplos de finanzas conservaste. Conservar algunos es correcto: la mezcla
es más honesta que un curso entero de hoteles.
