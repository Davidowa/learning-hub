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

## 2. Español de TIA501 · a medias, y el resto depende de una decisión

Hecho:

- **Los 17 decks**, en `es/`. Estructura idéntica al inglés, diapositiva por diapositiva,
  con las mismas capas y las mismas listas. Los cuatro chequeos del kit en cero sobre los 34
  decks del curso, sin renglones de build que empiecen con `!`.
- **`procedures.es.md`**, las 107 rutas traducidas paso por paso. Ya no queda un solo hueco.

Lo que hay que saber de los decks. El español sí revienta topes que el inglés no tocaba, tal
como estaba anotado: se arregló acortando el español, nunca bajando el tipo. Las fórmulas van
con los nombres de función en español del glosario y con **la coma** como separador de
argumentos, que es lo que corresponde a es-MX, donde el punto es el separador decimal. Si las
máquinas del salón están en configuración de España, eso hay que cambiarlo a punto y coma en
los 17 decks. Las imágenes siguen apuntando a `img/en/`, porque no existe `img/es/`, y cada
diapositiva que muestra una captura lo dice.

**Lo que falta, y por qué está detenido.** Los ejercicios y los 49 archivos de `labs/` no se
tradujeron todavía. El bloqueo del glosario ya se destrabó a medias: la pasada contra la
documentación de Microsoft corrió completa el 20 de agosto de 2026, en dieciocho lotes con
escritura incremental, así que un corte de sesión ya no la pierde entera como la vez anterior.

El resultado vive en `GLOSARIO-DOC.es.md` del curso: **816 términos cerrados** de los 1,045
reales (la tabla vieja decía 969; estaba contada antes de la sustitución IMG), con URL y
confianza por fila. 235 en alta con dos páginas coincidentes, 491 en media con una página, y
90 en baja que **no se sustituyen sin un Excel en español enfrente**, porque la página que las
respalda huele a traducción automática. Quedan **229 términos en 364 apariciones** que ninguna
página de Microsoft nombra; están en `TERMINOS-PENDIENTES.md` con su candidato anotado, y solo
se cierran con el producto. La pasada también dejó siete trampas nuevas documentadas al frente
de `GLOSARIO-DOC.es.md` (Add/Sumar en Pegado especial, Tabulación/Tabulador, el cuadro Serie
traducido a máquina, entre otras). La clave de fuente `DOC` quedó registrada en el glosario de
`procedures.es.md`.

La sustitución de corchetes corrió el 21 de agosto de 2026: **1,468 reemplazos** de 673
términos alta y media en `procedures.es.md` y los 17 decks, con una lista de exclusión de 60
términos multi-contexto (Add/Sumar y compañía) que se quedan en corchete a propósito. Quedan
**654 corchetes**: los 229 sin evidencia (364 apariciones), las 90 filas baja y los excluidos.
Los cuatro chequeos del kit volvieron a cero después de acortar nueve renglones que el español
más largo reventó. Hay PDF de `GLOSARIO-DOC.es.md` y `TERMINOS-PENDIENTES.md` junto a sus
fuentes. El separador de argumentos queda confirmado en **coma**, es-MX, y no hay que tocar
los decks.

Esta máquina no puede cerrarlo: tiene el corrector en español pero no el paquete de idioma de
la interfaz. Está comprobado, no supuesto, y los tres renglones que lo prueban están en ese
mismo archivo. Traducir de oído está prohibido por el documento y por buenas razones.

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

## 5. La carpeta Excel · borrada, y qué se hizo antes

Ya no está. Los 72 .xlsx, los 49 .docx y los 3 PDF se borraron después de sacarles todo lo que
el markdown no tenía. Lo que se recuperó, en orden de cuánto costaba perderlo:

- **`Ejercicios anteriores/`**, que nunca se había convertido y era un tercio de los datos.
  Ahora son 28 archivos en `labs/legacy/` y 53 CSV con 34,776 renglones.
- **8,631 caracteres de instrucciones dentro de cuadros de texto flotantes.** Un cuadro de
  texto se dibuja encima de la hoja, no vive en una celda, así que la exportación a CSV nunca
  lo vio. Por eso varias tareas eran archivos de veinte renglones que describían los datos y
  se quedaban calladas.
- **Instrucciones en hojas con nombre engañoso.** La tarea 19 guarda su lista de tareas en una
  hoja llamada `Exercise1` que no tiene un solo dato, y la 10 guarda sus dos reglas de premio
  en la columna ancha de al lado. Buscar hojas llamadas Instructions no las encontraba.
- **10,272 fórmulas** de los libros resueltos, que son 27 patrones distintos llenados hacia
  abajo, en `labs/legacy/answer-key-formulas.en.md` con los nombres definidos de los que
  dependen.
- **Las reglas de formato condicional, validación, protección y las 5 gráficas** de los diez
  libros que las traían, escritas con rango, condición y color exacto.
- **Las seis fórmulas estadísticas de la tarea 4 anterior**, que venían como metarchivos de
  Windows. Se renderizaron, se leyeron y se transcribieron.
- **Tres imágenes** que ahora viven en `ppts/img/en/`: la hoja modelo de la tarea 1, la tabla
  del Marco Común Europeo de la tarea 19 y el logo del campus del ejercicio 3.
- **Dos CSV sueltos** que ninguna hoja contenía, `RealState_Database.csv` con 3,337 registros,
  que la tarea 14 nombra por su nombre, y el registro de tareas del ejercicio 2 anterior.
- **569 cadenas de interfaz en español**, leídas de las capturas del profesor. Ver el punto 2.

Las capturas mismas no se guardaron: están tomadas en la máquina de otra persona y traen su
nombre en la barra de título y su escritorio en el cuadro.

La comprobación antes de borrar: las 156 hojas de los 72 libros, contrastadas contra
`labs/`. Las ocho que el comparador no casó se revisaron a mano una por una y las ocho están
preservadas; el comparador falla ahí porque el markdown reescribe la prosa en vez de copiarla.
`labs/` guarda hoy 101,529 renglones de CSV y 77 archivos de markdown.

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
