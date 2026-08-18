# Lo que queda, y el estado en que lo dejo

Estado al cerrar: rama `main`, local y remoto en el mismo commit, árbol limpio salvo una
carpeta que está fuera a propósito. Ocho cursos, 317 decks, 765 ejercicios, 40 capturas de
Excel. Los cuatro chequeos del kit en cero sobre todo el repositorio.

Lo que sigue está en orden de lo que más rinde primero.

## 1. Las imágenes no están en los ejercicios de Excel

Es lo más importante y es lo que el profesor pidió por nombre.

`ppts/office/manejo-y-analisis-de-la-informacion/labs/` tiene 49 archivos markdown, 25
ejercicios y 23 tareas más el README, y **ninguno referencia una sola imagen**. Hay 84 PNG
en `ppts/img/en/`, 40 de ellos capturas reales de diálogos de Excel tomadas para esto.

Cada ejercicio tiene una sección `## Exam routes used here` escrita en texto. Ahí es donde
va la imagen del cuadro que la ruta describe. La correspondencia es directa: un ejercicio que
usa Formato de celdas lleva `format-cells-dialog.png`, uno de filtros avanzados lleva
`advanced-filter.png`, uno de dinámicas lleva `create-pivottable.png` y
`pivottable-fields-pane.png`.

Los nombres de archivo dicen qué contienen. Léelos antes de asignarlos y no inventes
correspondencias: `go-to-dialog.png` es el cuadro Ir a, no Ir a Especial, y está nombrado así
justamente porque la captura de Especial no se logró.

## 2. Español de TIA501

Es el único curso que no es bilingüe. Faltan:

- Los 17 decks. La fuente está en `ppts/office/manejo-y-analisis-de-la-informacion/en/`.
- Los ejercicios, `exercises.en.md` y `solutions.en.md`, 51 ejercicios.
- Los 49 archivos de `labs/`.

`procedures.es.md` ya existe y **es un andamio deliberado, no una traducción**: 107 huecos con
la ruta en inglés arriba de cada uno como texto fuente, más el glosario inglés-español. El
profesor dijo que eso lo haría un becario. Si en su lugar lo hace un agente, el andamio sigue
siendo el punto de partida correcto.

Ojo con una cosa medida: el español corre más largo que el inglés y revienta topes que el
inglés no tocaba. En Unity hubo que rehacer nueve elementos por eso, cuatro títulos de
`pitfalls` que solo aceptan un renglón y cinco celdas de tabla con tope de 36 caracteres. Se
arregla acortando el español, nunca bajando el tamaño de tipo, y `preflight` y `lint` lo
cazan.

## 3. Los 82 pendientes de las rutas

`procedures.en.md` cierra con una sección `Still to confirm` de 82 elementos, casi todos
nombres de campos dentro de cuadros de diálogo, que es lo que una ruta cita más. Se cierran
con un Excel enfrente en una sesión. Cuarenta son leyendas en inglés y se pueden confirmar en
la máquina del profesor; los otros necesitan un Excel con paquete de idioma español.

Nada calificable en los ejercicios se apoya hoy en una línea marcada así, y conviene que siga
siendo cierto.

## 4. Capturas que faltan

Cinco, y `ppts/kit/SCREENSHOTS.md` documenta la técnica completa y por qué estas resisten.

- `save-as-xlsm` y `from-text-csv-preview` dependen del cuadro común de archivos de Windows,
  clase `#32770`. `PrintWindow` lo devuelve 92 a 95 por ciento oscuro y la ventana que
  enumera bajo esa clase reporta un rectángulo de 1280x720 en el origen de la pantalla, que
  no es donde está el diálogo.
- `go-to-special`, `custom-views` y `paste-special` fallaron por causas más simples. El botón
  `Special...` no se invocó, Vistas personalizadas probablemente pide el libro guardado, y
  `Ctrl+Shift+V` en Excel moderno pega directo en vez de abrir el cuadro.

Y todas las capturas existentes son de **interfaz en inglés**, porque el idioma de edición de
esa máquina lo es. Los decks en español necesitan las suyas desde una máquina con el paquete
de idioma, con los mismos scripts, escritas a `ppts/img/es/`.

## 5. La carpeta Excel, 124 archivos sin rastrear

`ppts/office/manejo-y-analisis-de-la-informacion/Excel/` sigue fuera de git a propósito. Son
los `.xlsx` y `.docx` originales, ya convertidos a markdown y CSV en `labs/`. Los tres PDF de
ahí quedan fuera solos por la regla de material de terceros de `ppts/.gitignore`.

**No la borres sin leer antes `labs/README.md`.** Ahí está escrito qué se pierde: formato de
celda, reglas de formato condicional, gráficos, diseños de tabla dinámica, listas de
validación y protección de hoja no sobreviven a un CSV, y varios ejercicios enseñan justamente
eso. Esa decisión es del profesor, no de quien tome la sesión.

## 6. Ejercicios de Unity

Los tres tracks tienen 16 decks en inglés y 16 en español, y **cero ejercicios** en cualquier
idioma. Los otros siete cursos tienen 51 por idioma. Si se escriben, el formato de esos siete
es el modelo, con una diferencia: Unity se evalúa sobre un proyecto que corre, no sobre una
salida de consola, así que la rúbrica tiene que decir qué se ve en pantalla.

Y la regla dura del track sigue viva: el material está **basado en** los pathways de Unity
Learn, se acredita en portada y cierre de cada deck, y ni una frase viene de
`learn.unity.com`. Esas páginas no publican licencia de reutilización. Los repos de ejemplo de
Unity sí traen la Unity Companion License, cuya cláusula 3.2 cede a Unity cualquier obra
derivada del Work, así que se enlaza a los repos para que el alumno los clone y no se pega su
código.

## 7. Dos huecos declarados, no olvidados

**Word.** El syllabus de TIA501 da las sesiones 1 a 4 parcialmente a Word y el primer parcial
lo evalúa con 30 por ciento del curso. El profesor lo sacó de alcance a propósito. Está
anotado en `COBERTURA.md` y en los decks de las semanas 1 y 2, que cubren solo su mitad de
Excel y lo dicen de frente.

**Cuadernos.** Solo dos de los ocho cursos tienen notebooks, Análisis de Datos y POO. Nunca se
retomó en esta sesión.

## Cómo se trabaja aquí

    cd ppts
    ../.venv/Scripts/python.exe -m kit.preflight <carpeta>
    ../.venv/Scripts/python.exe -m kit.build     <carpeta>
    ../.venv/Scripts/python.exe -m kit.lint      <carpeta>
    ../.venv/Scripts/python.exe -m kit.sizes     <carpeta>

Los cuatro tienen que volver en cero, y un renglón del build que empiece con `!` cuenta como
problema aunque el archivo se escriba igual. Se arregla partiendo el ejemplo o acortando el
título, nunca bajando el tipo bajo el piso de 18 pt.

Los `.pptx` no se commitean, `ppts/.gitignore` los ignora porque se reconstruyen del YAML.

Prohibido el guion largo en todo el material. Español de México. Y la regla que atraviesa todo
el repositorio: **el ejercicio de la semana N solo usa lo que las semanas 1 a N enseñaron.**
