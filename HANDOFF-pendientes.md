# Lo que queda, y el estado en que lo dejo

Estado al cerrar: rama `main`, local y remoto en el mismo commit, árbol limpio salvo una
carpeta que está fuera a propósito. Ocho cursos, 317 decks, 765 ejercicios, 47 capturas de
Excel y 91 figuras colocadas en los ejercicios. Los cuatro chequeos del kit en cero sobre
todo el repositorio.

Lo que sigue está en orden de lo que más rinde primero.

## 1. Las imágenes en los ejercicios de Excel · hecho

Los 34 archivos de `labs/` que tienen sección `## Exam routes used here` llevan ya sus
capturas: 91 figuras, 35 imágenes distintas, cada una dentro del bloque de la ruta que
describe el cuadro. Los otros 15 archivos de tareas, `hw10` en adelante, no tienen esa
sección y por eso no llevan figura; remiten a su ejercicio gemelo, que sí la tiene.

Una ruta lleva imagen cuando la captura es de la ventana que esa ruta abre, y no lleva
ninguna cuando no lo es. Las galerías de la cinta, el controlador de relleno, inmovilizar
paneles y el Inspector de documento no tienen captura y se quedaron sin ella a propósito.
Doce capturas del catálogo no se usaron: siete son de macros y del entorno de VBA, que estos
ejercicios no tocan, y las otras cinco no tienen ruta que las pida.

Tres pies de figura declaran una aproximación en vez de esconderla. `find-and-replace.png`
se tomó con la pestaña Reemplazar al frente, `insert-chart.png` abre en Gráficos
recomendados, y `function-arguments-if.png` es el cuadro de argumentos cargado con SI. Donde
alguna de las tres acompaña a una ruta que habla de la otra pestaña o de otra función, el pie
lo dice y dice qué verá el alumno en su lugar.

**Lo que salió de revisar el catálogo imagen por imagen.** Tres archivos estaban mal y
ninguno se notaba en un listado de carpeta:

- `format-cells-border.png` era una copia byte a byte de `format-cells-font.png`. La captura
  de la pestaña Bordes nunca se tomó, y un deck llevaba desde entonces la imagen equivocada.
- `subtotal-outline.png` era una segunda toma del cuadro Subtotales, no el esquema en la hoja
  con sus botones 1 2 3.
- `name-manager.png` traía quince píxeles de otra ventana pegados al borde inferior, con una
  frase legible dentro.

Los tres se volvieron a tomar. De paso salieron cuatro capturas más, tres de ellas de la
lista de imposibles del punto 4. Todo está escrito en `ppts/kit/SCREENSHOTS.md`.

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

Quedan dos, no cinco. `go-to-special`, `custom-views` y `paste-special` ya están tomadas, y
además hay una nueva, `format-cells-protection`, que salió del mismo barrido. El catálogo va
en 47 capturas del producto, sin cuadros oscuros y sin duplicados.

Cómo cayeron las tres, por si vuelve a hacer falta. `Paste Special` quiere `Ctrl+Alt+V`, no
`Ctrl+Shift+V`, que en el Excel moderno pega directo. `Go To Special` se alcanza con un clic
calculado sobre el rectángulo de la ventana, porque el botón `Special...` es de dibujo propio
y la automatización de interfaz no lo ve. `Custom Views` sí pedía el libro guardado, como
estaba anotado aquí.

Las dos que siguen resistiendo son `save-as-xlsm` y `from-text-csv-preview`, las dos del
cuadro común de archivos de Windows, clase `#32770`. `PrintWindow` lo devuelve 92 a 95 por
ciento oscuro y la ventana que enumera bajo esa clase reporta un rectángulo de 1280x720 en el
origen de la pantalla, que no es donde está el diálogo. Ninguna ruta de `labs/` las necesita
hoy.

Y todas las capturas existentes son de **interfaz en inglés**, porque el idioma de edición de
esa máquina lo es. Los decks en español necesitan las suyas desde una máquina con el paquete
de idioma, con los mismos scripts, escritas a `ppts/img/es/`. Los 91 lugares donde van ya
están marcados: son las figuras de `labs/`, que al traducirse cambian de `img/en/` a
`img/es/`.

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
