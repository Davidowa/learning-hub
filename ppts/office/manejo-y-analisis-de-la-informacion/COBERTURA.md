# Cobertura de TIA501 contra las dos certificaciones

Se compararon las 34 sesiones del syllabus vigente contra los objetivos publicados de MO-200 (Excel Associate) y MO-201 (Excel Expert), y contra los temarios de Microsoft 365 que los sustituyen, MO-210 y MO-211. También se inventariaron los 25 ejercicios del profesor para ver qué hueco tapa cada uno. La cifra corta: de los 107 objetivos que suman los dos exámenes de Office 2019, el syllabus cubre 44 hoy, es decir el 41 por ciento. El plan de abajo lleva 100 de esos 107 a una sesión concreta sin mover una sola semana. Los otros 7 no caben, y dónde ponerlos es una de las tres decisiones que este documento deja sobre la mesa.

## El veredicto

**MO-200, Excel Associate.** El PDF trae 59 objetivos numerados, no 58: son 18 en el dominio 1, 17 en el 2, y 8 en cada uno de los tres restantes. De esos, 38 están cubiertos porque alguna sesión nombra el comando, 14 quedan a medias y 7 no aparecen en ninguna de las 34 sesiones.

**MO-201, Excel Expert.** El PDF trae 48 objetivos, no 44. La confusión es de Certiport: en el dominio 2 numera 2.3.1, 2.3.2 y 2.3.4, y se salta el 2.3.3, así que el último número no coincide con la cuenta. De los 48, hay 6 cubiertos, 21 parciales y 21 huérfanos.

| Examen | Objetivos | Cubiertos | Parciales | Huérfanos |
|---|---|---|---|---|
| MO-200 Associate | 59 | 38 | 14 | 7 |
| MO-201 Expert | 48 | 6 | 21 | 21 |
| **Suma** | **107** | **44** | **35** | **28** |

La diferencia entre los dos exámenes no es de grado, es de otra naturaleza. El syllabus se escribió para el Associate y se le nota en cada renglón: la columna Topic dice literalmente MO-210 en las diecisiete semanas y nunca menciona el Expert. Para el Associate el curso está cerca, faltan sub-habilidades sueltas dentro de temas que ya se enseñan. Para el Expert falta materia entera. El dominio 4 del Expert, tablas dinámicas y gráficos dinámicos, tiene 12 objetivos y solo uno cubierto: la semana 14 le da dos sesiones a «subtotals and PivotTables» y ahí se acaba. El bloque 3.5, depuración de fórmulas, tiene 4 objetivos colgados de una sola frase de la sesión 6, «formula auditing (show formulas)», que nombra el grupo de la cinta y un solo botón. Y las macros, que son 5 objetivos del Expert contando 1.1.1 y 1.1.3, no existen: la palabra «macro» aparece cero veces en las 597 líneas del syllabus, igual que «VBA» y «Visual Basic».

Los 25 ejercicios cambian la foto y la cambian a favor. Veinte cubren su objetivo completo, cuatro quedan parciales y uno no tiene semana asignada en el syllabus. Varios son un regalo: el ejercicio 17 construye veinte tipos de gráfico y con eso cierra solo el objetivo 4.1.2 del Expert, que el syllabus resume como «different chart styles»; el ejercicio 23 versión 2, con 26,608 líneas de comandas de restaurante, cubre casi todo el bloque 4.2 y 4.3 del Expert, campo calculado, segmentación, escala de tiempo y gráfico dinámico incluidos; el 25 usa PAGO, que es el 3.4.4 y no está en ninguna línea del syllabus. O sea que buena parte del hueco del Expert ya tiene material listo y lo que falta es tiempo de clase, no archivos.

Con las adiciones repartidas como propone la sección «Semana por semana», el resultado queda así: los 59 objetivos del Associate quedan dentro de las 34 sesiones, y del Expert quedan 41 dentro y 7 fuera. Esos 7 tienen nombre y están en la última sección.

Dos advertencias sobre el propio documento fuente. El PDF del syllabus tiene dos celdas cortadas a media frase: la sesión 8 termina en «COUNTA, COUNTBLANK and» y la sesión 26 en «VLOOKUP, HLOOKUP and». Con extracción en crudo se recuperó la primera, cierra con LEFT, pero la segunda se perdió al generar el archivo y no hay forma de leerla. Si la sesión 26 decía INDEX o MATCH, el objetivo 3.2.1 del Expert sube de estatus sin tocar nada. Conviene reparar el PDF antes de repartirlo a los alumnos.

## La discrepancia de versión

El syllabus dice MO-210 en las diecisiete filas de la columna Topic y en Course Resources. Los PDF que hay en el repositorio son MO-200 y MO-201, de Office 2019. No son el mismo examen, y el propio syllabus ya lo admite en la bibliografía: «Written for the Office 2019 edition of the same skill set; the current exam is MO-210».

La brecha real es chica. Se descargaron los temarios de 365 desde el CDN de credenciales de Microsoft y se cotejaron contra una segunda copia con derechos de Certiport de 2022, que coincide objetivo por objetivo. MO-210 agrega cinco cosas sobre MO-200: importar de orígenes en línea, generar datos con RANDBETWEEN y SEQUENCE, dar formato a varias hojas agrupándolas, ordenar con SORT y obtener valores únicos con UNIQUE. MO-211 agrega seis sobre MO-201: RANDARRAY, LET dentro de la lista de funciones anidadas, XLOOKUP dentro de la lista de búsqueda, FILTER, SORTBY y «configure value field settings» en tablas dinámicas. Once objetivos nuevos sobre ciento doce.

Ocho de esos once son funciones de matriz dinámica que no existen en Office 2019: SEQUENCE, SORT, UNIQUE, RANDARRAY, FILTER, SORTBY, XLOOKUP y LET. Esto no se arregla con material. Si las máquinas del laboratorio corren Office 2019, esas ocho funciones no se pueden practicar, y da igual cuántos decks se autoricen. Hay que confirmar qué versión de Excel está instalada antes de planear las semanas 4, 9, 13 y 15.

MO-210 y MO-211 también quitan cosas, y una de ellas conviene tenerla presente porque toca la semana 11. Los comentarios bajaron del Expert al Associate: en 2019 «manage comments» era el objetivo 1.2.5 de MO-201, y en 365 es objetivo del Associate, con la distinción entre comentario con hilo y nota que en 2019 no existía. MO-211 además elimina el dominio completo de opciones de idioma, borra el gráfico de Mapa de la lista de tipos avanzados y sustituye «Format data» por «configure value field settings» en tablas dinámicas.

Sobre vigencia, consultado en las páginas de examen de Microsoft Learn: MO-200, MO-201 y MO-211 dicen «Retirement date: none». La página de MO-210 redirige a la de certificación, que no anuncia retiro y fue actualizada el 31 de julio de 2026. El único retiro anunciado en la familia MOS es el de 2016, que termina el 30 de junio de 2026. Los cuatro exámenes se pueden presentar hoy.

Hay un dato que probablemente decida la versión y que no tiene que ver con el temario: el idioma. MO-210 se ofrece en quince idiomas, español incluido. MO-211 se ofrece únicamente en inglés. En cambio MO-201, el Expert de 2019, sí está en español. Si la meta es que el alumno salga capaz para las dos certificaciones y el grupo presenta en español, el Expert de 365 los deja presentando en inglés.

**Recomendación.** Apuntar a MO-210 para el Associate, que es lo que el syllabus ya declara, existe, está vigente y tiene español. Para el Expert, presentar MO-201 mientras el grupo trabaje en español, porque el temario apenas cambia y el idioma cambia mucho. Los PDF de 2019 pasan a ser respaldo, no fuente: conviene bajar los dos temarios de 365 y guardarlos junto a los de 2019 en el repositorio, porque el de MO-210 vive en una URL mal nombrada de Microsoft que en cualquier momento corrigen y rompen.

## Semana por semana

Cada semana lleva primero lo que el syllabus manda, que no se toca, y debajo lo adicional con su número de objetivo. Los códigos sin prefijo son de MO-200; los que llevan «Expert» son de MO-201; los que llevan «365» solo existen en MO-210 o MO-211 y dependen de la versión instalada.

### Semana 1, sesiones 1 y 2

Introducción al curso y procesadores de texto. La sesión 2 trabaja «indentation and line spacing, styles, portrait and landscape layout, section breaks, find and replace, headers and footers». CLO01, evidencia diagnóstica inicial.

Sin adicionales. Ninguna de las dos sesiones toca Excel y no hay objetivo de certificación que colocar aquí.

Aviso de material: no hay un solo ejercicio de Word en el paquete. Los 25 son de Excel. Las sesiones 1 a 4 se quedan sin práctica preparada.

### Semana 2, sesiones 3 y 4

La sesión 3 sigue en Word con tabla de contenido, tablas, vínculos, bibliografía y plantillas. La sesión 4 es el primer contacto con Excel: «font, alignment, number, clipboard, styles (apply and clear), insert and delete cells, merge cells, fit cells, AutoFill». CLO02 y CLO03. Con eso ya quedan cubiertos 2.1.2, 2.1.4, 2.2.1, 2.2.5, 2.2.7 y 2.2.8.

ADICIONAL:

- **2.2.6**, el cuadro de diálogo Formato de celdas con Ctrl+1. La sesión nombra los grupos de la cinta, no el cuadro. Bordes, relleno y formato de número personalizado solo viven ahí, y el examen separa este objetivo del 2.2.5 justamente por eso.
- **2.2.4**, Ajustar texto escrito con todas sus letras. «Fit cells» es ambiguo, también se lee como autoajustar el ancho de columna, que es el objetivo 1.3.2.
- **2.2.3**, Copiar formato. La sesión nombra el grupo Portapapeles, que es donde vive el botón, pero el examen pide usar la brocha.
- **2.2.2**, orientación y sangría. La sesión cubre alineación y deja fuera los otros dos sub-skills que Certiport nombra en el mismo objetivo.
- **1.4.1**, barra de herramientas de acceso rápido. Es el único momento del curso en que la interfaz misma es el tema. Después de la sesión 4 el curso ya no vuelve a mirar la cinta.

Ejercicio 1, formato de celdas y rangos. Cubre por sí solo el cuadro Formato de celdas, ajustar texto, Copiar formato de la fila 8 a la 9-12, alineación, autorrelleno, combinar y centrar, estilo de celda, bordes y Borrar todo. Cuatro de las cinco adiciones ya están practicadas ahí.

Carga: es la sesión más apretada del plan. La sesión 4 es media sesión de Excel, comparte semana con Word, y recibe cinco adiciones. La barra de acceso rápido son cinco minutos y la orientación y sangría otros cinco, pero el cuadro Formato de celdas necesita quince. Si algo se cae, que se caiga la barra de acceso rápido y se recupere en la semana 17, donde la sesión 33 también toca configuración del entorno.

### Semana 3, sesiones 5 y 6

La sesión 5 administra hojas: «add, copy and move, rename, insert and delete columns and rows, adjust height and width, hide and unhide». La sesión 6 abre la pestaña Fórmulas: «function library, defined names (naming ranges), formula auditing (show formulas); valid data types, precedence of mathematical operators, relative and absolute references». CLO03 y CLO04, evidencia «Workbook with organised sheets and named ranges». Quedan cubiertos 1.3.2, 2.1.3, 1.4.6 y 2.3.1.

ADICIONAL, sesión 5:

- **365, MO-210 2.2.9**, dar formato a varias hojas agrupándolas. Es la sesión donde ya se copian y mueven hojas, y funciona igual en Office 2019 aunque el objetivo solo esté en el temario de 365.
- **Expert 2.1.2**, el cuadro Series con tendencia, incremento, unidades de fecha y listas personalizadas. La semana 2 enseñó el arrastre básico; aquí se abre la caja.

ADICIONAL, sesión 6:

- **1.2.1**, buscar datos dentro del libro. Ninguna de las 34 sesiones lo nombra. El único «find and replace» del syllabus es el de Word en la sesión 2. Tiene que estar antes de que arranquen las fórmulas.
- **1.2.2**, navegar a celdas y rangos con nombre. Definir nombres y navegar a ellos son dos objetivos distintos, 2.3.1 y 1.2.2. Falta el Cuadro de nombres y el comando Ir a especial.
- **4.1.1**, referencia mixta. La sesión enseña relativa y absoluta y deja fuera A$1 y $A1. Es un hueco caro: sin mixtas, una tabla de multiplicar se rompe al arrastrar en dos direcciones.
- **Expert 1.2.4**, opciones de cálculo automático y manual. Cinco minutos en la misma pestaña Fórmulas. Vuelve a importar en la semana 16, porque las tablas de datos dependen del modo de cálculo.
- **Expert 3.5.1**, rastrear precedentes y dependientes.
- **Expert 3.5.2**, Ventana de inspección.

Ejercicios 2, administrar hojas, rangos con nombre e inmovilizar paneles, y 5, precedencia de operadores, referencias y nombres definidos. El 2 ya practica el cuadro Series y el Administrador de nombres. El 5 hace referencia absoluta con F4 y un nombre definido usado como absoluta, pero nunca abre las herramientas de auditoría: eso hay que agregarlo al ejercicio o resolverlo en clase.

Carga: son ocho adiciones repartidas en dos sesiones, unos cincuenta minutos sobre ciento ochenta. Aguanta, pero la sesión 6 queda llena. Los otros dos objetivos de auditoría, comprobación de errores y evaluar fórmula, se van a la semana 7 por eso.

### Semana 4, sesiones 7 y 8

La sesión 7 hace «SUM, AVERAGE, MAX, MIN, CONCAT; using range names in formulas; LARGE and SMALL». La sesión 8 hace «text functions UPPER, LOWER, PROPER and TEXT; DAY, MONTH and YEAR; COUNTA, COUNTBLANK and LEFT», donde LEFT solo se recupera extrayendo el PDF en crudo. CLO05, evidencia «Workbook with statistical, text and date functions». Queda cubierto 4.2.1.

ADICIONAL:

- **4.2.2**, COUNT. Está COUNTA y está COUNTBLANK, falta contar solo números, que es la función que distingue celda con dato de celda con número y el examen la pide por nombre.
- **4.3.1**, RIGHT y MID. LEFT ya está en la sesión 8; las otras dos no aparecen en ninguna de las 34 sesiones.
- **4.3.2**, LEN. UPPER y LOWER están, LEN no. PROPER y TEXT, que sí se enseñan, pertenecen a otro objetivo y no compensan el hueco.
- **4.3.3**, TEXTJOIN. CONCAT está en la sesión 7. TEXTJOIN pide delimitador y omisión de vacíos, cosa que CONCAT no hace.
- **Expert 3.3.1**, NOW y TODAY, junto a DAY, MONTH y YEAR que ya están.
- **Expert 2.2.1**, formatos de número personalizados con sus códigos y secciones.

Ejercicios 6, funciones estadísticas y CONTAR.SI, y 13, funciones de texto y fecha con formatos personalizados. El 13 ya hace IZQUIERDA, TEXTO, CONCAT, MAYUSC, NOMPROPIO, DIA, MES, AÑO y los formatos de número personalizados sobre 60 alumnos. El 6 hace CONTARA y CONTAR.BLANCO sobre 39 pedidos.

Carga: seis funciones nuevas a tres o cuatro minutos cada una son treinta minutos, y la sesión 8 ya venía llena. Se sostiene porque el ejercicio 13 practica la mitad fuera de clase. Lo que no cabe aquí son WEEKDAY y WORKDAY, que están en la última sección.

Aviso de material: K.ESIMO.MAYOR y K.ESIMO.MENOR, que el syllabus manda en la sesión 7, no aparecen en ninguno de los 25 ejercicios ni en las 23 tareas.

### Semana 5, sesiones 9 y 10

La sesión 9 hace «conditional formatting, icon sets, sparklines, hyperlinks» y la sesión 10 abre «the IF function». CLO07 y CLO05, evidencia «Workbook with conditional formatting and sparklines». Quedan cubiertos 1.2.3, 2.4.1, 2.4.2 y 4.2.3.

ADICIONAL:

- **2.4.3**, quitar formato condicional. Certiport lo cuenta aparte del 2.4.2, así que borrar reglas de las celdas seleccionadas y de toda la hoja se evalúa por separado.
- **Expert 2.3.4**, Administrador de reglas: editar, borrar, reordenar prioridad y Detener si es verdad.
- **Expert 2.3.1**, crear reglas propias desde Nueva regla, con sus rangos y criterios elegidos.
- **Expert 2.3.2**, reglas basadas en fórmula. Es lo que separa al Expert del Associate en este punto y ninguno de los 25 ejercicios lo hace. Aquí sí hace falta material nuevo.
- **2.1.1**, pegado especial por opciones: valores, formatos, transponer, pegar vínculo. El examen pide elegir opción, no pegar y ya.

Ejercicios 3, formato condicional completo con minigráficos e hipervínculos, y 7, función SI con nombres definidos y pegado como valores. El 3 aplica reglas de resaltado, 10 superiores, 10 por ciento inferiores, por encima del promedio, semáforos, barra de datos, escala de color, minigráfico de línea y de columna, y cuatro tipos de hipervínculo. El 7 practica pegar como valores y de paso usa ALEATORIO.ENTRE, que cubre la mitad del objetivo 2.1.5 de MO-210.

Carga: cinco adiciones sobre dos sesiones, pero cuatro salen del mismo cuadro de diálogo. Cabe.

### Semana 6, sesiones 11 y 12

«Session 11: the IF function in depth. Session 12: first midterm exam.» CLO05.

Sin adicionales. Solo hay una sesión de clase y el primer parcial evalúa Word y el primer bloque de Excel: formato, administración de hojas, referencias, funciones estadísticas, de texto y de fecha, formato condicional y SI. Meterle temas nuevos a la semana del parcial es la forma más rápida de perder el 30 por ciento de la calificación.

Ejercicio: repaso de los ejercicios 1 a 7. No entra ninguno nuevo.

### Semana 7, sesiones 13 y 14

«Session 13: operators and wildcards; the AND and OR functions. Session 14: nested IF.» CLO05, evidencia «Exercises with AND, OR and nested IF».

ADICIONAL:

- **Expert 3.1.1**, NOT. El syllabus nombra Y y O y se salta NO, que va en la misma tabla de verdad.
- **Expert 3.1.1**, IFS. La función SI.CONJUNTO no aparece en ninguna línea del syllabus. Ojo con la colisión de nombres: la semana 8 enseña la familia *.SI.CONJUNTO, que es otra cosa.
- **Expert 3.1.1**, SWITCH. Cinco minutos pegados a IFS, con el mismo caso resuelto de las dos formas.
- **Expert 3.5.4**, Evaluar fórmula. El SI anidado de la sesión 14 es exactamente lo que uno depura paso a paso con esa herramienta.
- **Expert 3.5.3**, comprobación de errores y sus reglas configurables.

Ejercicios 8, SI anidado en tres escenarios con 84 fórmulas grabadas; 10, Y, O, NO y comodines con tabla de verdad completa de 16 filas y nueve criterios con comodines; y 12, SI.CONJUNTO frente a SI anidado, que compara en columnas paralelas y usa VERDADERO como último criterio para dar valor por defecto. El 12 es el único ejercicio huérfano del paquete y esta es su semana: el contraste que plantea es justo el de la sesión 14.

Carga: cinco adiciones en dos sesiones. Tres son funciones lógicas que caben en la clase que ya las enseña y dos son botones de la pestaña Fórmulas. Cabe.

### Semana 8, sesiones 15 y 16

«Sessions 15 and 16: the *IFS family, SUMIFS, COUNTIFS, AVERAGEIFS, MINIFS and MAXIFS.» CLO05, evidencia «Workbook that summarises data with the *IFS functions».

ADICIONAL:

- **Expert 3.1.1**, las formas singulares SUMIF, COUNTIF y AVERAGEIF. Van antes que las de conjunto, no después, y el syllabus solo nombra la familia plural.

Ejercicios 9, SUMAR.SI, CONTAR.SI y PROMEDIO.SI de un solo criterio sobre 520 registros de spa y 88 ventas de laptops; y 11, la familia *.SI.CONJUNTO sobre 25 órdenes de transporte y un reporte de depósitos por sucursal y mes.

Carga: dos sesiones completas para cinco funciones plurales más tres singulares. Es de las pocas semanas con holgura real del semestre.

Aviso de material: el ejercicio 11 solo practica SUMAR.SI.CONJUNTO, CONTAR.SI.CONJUNTO y PROMEDIO.SI.CONJUNTO. MAX.SI.CONJUNTO y MIN.SI.CONJUNTO, que el syllabus nombra explícitamente, se quedan sin ejercicio. Con la holgura de esta semana, agregarlas al ejercicio 11 es barato.

### Semana 9, sesiones 17 y 18

La sesión 17 hace «get and transform data; sorting by multiple columns; removing duplicates; inspecting workbooks, modifying basic properties, removing personal information». La sesión 18 hace filtros. CLO06 y CLO09, evidencia «Imported, deduplicated and inspected data set». Quedan cubiertos 1.1.2, 1.4.5, 3.3.1, 3.3.2 y Expert 2.2.5.

ADICIONAL:

- **1.1.1**, importar desde .txt. Obtener y transformar cubre el .csv por la ruta From Text/CSV, pero falta la rama del asistente que el examen pide: delimitado contra ancho fijo, elección de delimitador y codificación.
- **Expert 2.2.2**, validación de datos. Cero apariciones de «validation» en el syllabus. Va en la misma pestaña Datos donde ya se está trabajando.
- **Expert 2.1.1**, Relleno rápido. No es lo mismo que el AutoFill de la semana 2: aquel rellena series, este deduce el patrón. Va donde se separan y limpian columnas.
- **Expert 1.1.4**, administrar versiones y recuperar libros sin guardar. Vive en el mismo panel Archivo, Información, que la sesión ya abre para inspeccionar el libro y modificar propiedades. Cinco minutos.
- **365, MO-210 1.1.2**, importar de orígenes en línea.

Ejercicios 14, quitar duplicados, importar y transformar, ordenar y validación de datos, con Students_data.csv de siete columnas; y 15, autofiltro sobre 408 ventas de electrodomésticos con formato condicional previo. El 14 ya trae las cinco reglas de validación que pide el objetivo Expert 2.2.2, incluida la fórmula personalizada para que el bono no pase el 10 por ciento del sueldo. El 15 filtra por trimestre, por mes, por color, por texto, por icono y por diez mejores.

Carga: cinco adiciones en dos sesiones, unos cuarenta minutos. La validación de datos es la más cara, quince minutos, pero el ejercicio 14 la practica completa fuera de clase.

### Semana 10, sesiones 19 y 20

La sesión 19 administra tablas: «apply table format, name a table, banded rows, total rows, convert a table to a range». La sesión 20 hace gráficos: «create charts, create chart sheets, switch rows and columns in the source data, chart elements (title, axis titles, legend, data labels), quick layout, styles, colours, alternative text». CLO06 y CLO07, evidencia «Workbook with named tables and charts». Es la semana que más objetivos cierra de todo el curso: 2.3.2, 3.1.1, 3.1.2, 3.1.3, 3.2.2, 3.2.3, 5.1.1, 5.1.2, 5.2.2, 5.2.3, 5.3.1, 5.3.2 y 5.3.3.

ADICIONAL:

- **3.2.1**, agregar y quitar filas y columnas de la tabla. La sesión 5 enseñó a insertarlas en la hoja, pero la tabla se comporta distinto: expansión automática, controlador de tamaño, fórmula que se propaga sola.
- **4.1.2**, referencias estructuradas, Tabla1[@Columna] y Tabla1[Columna]. La sesión 19 nombra la tabla y nunca la usa en una fórmula.
- **5.2.1**, agregar series de datos al gráfico. El cambio de filas y columnas que la sesión ya enseña se hace en el cuadro Seleccionar datos, que es la misma pantalla donde se agrega o quita una serie. Dos minutos si se hace ahí.

Ejercicios 16, tablas de Excel con referencias estructuradas y fila de totales sobre 30 pedidos de ropa, con las fórmulas escritas en referencia estructurada sobre la tabla «Lorena»; y 17, veinte tipos de gráfico sobre cinco hojas de datos.

Carga: tres adiciones cortas sobre la semana más cargada del syllabus. Cabe porque las tres se hacen dentro de la pantalla que ya está abierta.

Dos avisos de material. El ejercicio 17 construye veinte gráficos y no pide hoja de gráfico, ni cambiar filas por columnas, ni texto alternativo, que son las tres cosas que el syllabus manda literalmente en la sesión 20. Y las fórmulas SI.CONJUNTO del ejercicio 16 están guardadas como _xlfn.IFS, o sea escritas en una versión más nueva: en Office 2019 abren bien, en cualquier build anterior salen como #¿NOMBRE?.

### Semana 11, sesiones 21 y 22

La sesión 21 es crítica de gráficos, «different chart styles and when each one fits». La sesión 22 prepara el libro para distribución: «spelling, accessibility checker, comments, protecting the worksheet and the workbook». CLO07 y CLO09, evidencia «Workbook with reviewed charts, comments and protection». Quedan cubiertos Expert 1.2.3 y 1.2.5.

ADICIONAL, sesión 21:

- **Expert 4.1.2**, los tipos avanzados: cajas y bigotes, combinado, embudo, histograma, proyección solar y cascada. El ejercicio 17 los construye todos en la semana 10, así que aquí solo hay que criticarlos y decir cuándo se usa cada uno, que es exactamente lo que la sesión ya hace. Costo casi cero.
- **Expert 4.1.1**, eje secundario y gráfico combinado. Esta sí necesita quince minutos de explicación propia.

ADICIONAL, sesión 22:

- **Expert 1.2.2**, proteger rangos con permiso de edición y bloqueo selectivo de celdas. La hoja y el libro ya están en el syllabus; los rangos no.
- **Expert 1.2.1**, restringir edición: Marcar como final, contraseña de apertura, abrir siempre como solo lectura.
- **365, MO-210**, la diferencia entre comentario con hilo y nota. En 365 los comentarios son objetivo del Associate y la distinción se evalúa; en 2019 no existía.

Ejercicio 18, accesibilidad, comentarios y protección de celdas, hoja y libro, sobre 115 empleados. El trabajo real es calcular la edad en la columna J, ocultar y proteger esa fórmula, proteger las celdas de sueldo y proteger la hoja.

Carga: es la segunda semana más apretada del plan y solo se sostiene porque el bloque de gráficos avanzados llega ya practicado desde la semana 10. Aquí es donde se decidió no meter macros ni opciones de idioma, aunque el mapeo inicial las proponía: con eso encima, la sesión 22 no cierra.

Dos avisos de material. La revisión ortográfica que el syllabus manda no la practica ningún ejercicio. Y el libro del ejercicio 18 arrastra nombres definidos muertos de un ejercicio viejo de filtros avanzados, BD, CRITERIOO, CRITERIOY, RESULTADOS, Criteria y Extract, todos apuntando a #REF!. Conviene limpiarlo antes de repartirlo.

### Semana 12, sesiones 23 y 24

«Session 23: second midterm exam. Session 24: INNOVATIQ certification mock exam; VLOOKUP.» CLO08. El segundo parcial evalúa comodines, Y y O, SI anidado, la familia *IFS, obtener y transformar, filtros, tablas y gráficos.

Sin adicionales. Media sesión de clase, y esa media sesión abre BUSCARV.

Ejercicio 19, BUSCARV dentro de un modelo de nómina, que se deja de tarea y se recoge en la semana 13. Trae tres tablas de referencia y diez vendedores con 19 columnas por llenar: BUSCARV exacto para sueldo base y comisión, BUSCARV aproximado para el tramo de bono, aritmética de fechas para la antigüedad, formato condicional y dos decisiones con SI combinado con Y y con O.

Esta es la semana donde entra el componente autogestivo de INNOVATIQ, que vale 5 por ciento y se completa antes de la semana 16. Es el único espacio del curso que no consume sesiones, y por eso la última sección lo propone como ancla para parte del sobrante.

### Semana 13, sesiones 25 y 26

«Session 25: VLOOKUP in depth. Session 26: VLOOKUP, HLOOKUP and», con la celda cortada en el PDF. El led es «Guided practice consolidating data across sheets». CLO08, evidencia «Workbook that consolidates data with lookup functions».

ADICIONAL:

- **Expert 3.2.1**, INDEX y MATCH. No aparecen en ninguna línea legible del syllabus y son la mitad del objetivo de búsqueda del Expert. Si la celda cortada de la sesión 26 decía INDEX o MATCH, esto deja de ser adición y pasa a ser lo que el syllabus siempre quiso.
- **Expert 3.4.1**, la herramienta Datos, Consolidar. El CLO08 dice «Consolidates information with lookup functions, subtotals, PivotTables and what-if analysis tools» y enumera todos los medios menos ese.
- **Expert 1.1.2**, referencias a otros libros. La práctica guiada consolida entre hojas del mismo libro; el objetivo pide vínculos externos.
- **365, MO-211 3.2.1**, XLOOKUP, si el laboratorio corre Microsoft 365.

Ejercicios 20, BUSCARV puro con lista desplegable como clave, exacto, aproximado y manejo de #N/A sobre 288 alumnos; y 21, búsquedas mixtas sobre 2,585 artículos de ferretería. El 21 es el único ejercicio del paquete que obliga a ÍNDICE y COINCIDIR, y lo hace sin nombrarlos: la tabla 2 avisa que el rango de búsqueda no está en la primera columna, y con eso BUSCARV deja de servir.

Carga: tres adiciones en dos sesiones dedicadas a búsqueda. INDEX y MATCH necesitan veinte minutos, Consolidar diez, referencias externas diez. Cabe.

Aviso de nombres: los ejercicios 19 y 20 se llaman los dos «BuscarV» y enseñan cosas distintas, y el 21 se llama «BuscarH» aunque solo una de sus tres tablas es horizontal. Vale la pena renombrarlos antes de repartirlos.

### Semana 14, sesiones 27 y 28

«Sessions 27 and 28: subtotals and PivotTables.» CLO08, evidencia «Workbook with subtotals and PivotTables». Quedan cubiertos Expert 2.2.4 y 4.2.1.

ADICIONAL:

- **Expert 2.2.3**, agrupar y desagrupar, niveles de esquema. Los subtotales ya generan el esquema sin que nadie lo explique.
- **Expert 4.2.2**, configuración de campo: resumir por, mostrar valores como, diseño del informe.
- **Expert 4.2.4**, agrupar datos de la tabla dinámica por fechas, por rangos numéricos y por selección.
- **Expert 4.2.5**, campos calculados.
- **Expert 4.2.6**, formato de la tabla dinámica. En 365 este objetivo se reescribió como «configure value field settings», que es la misma pantalla del 4.2.2.

Ejercicios 22, subtotales automáticos y niveles de esquema sobre 576 registros de población de la Ciudad de México, con cuatro copias de la hoja y un subtotal distinto en cada una; y 23 versión 1, tablas dinámicas sobre 31 filas de reclutamiento, que sirve como calentamiento.

Carga: esta es la semana que más se estira. Dos sesiones tienen que absorber subtotales, tablas dinámicas y cinco adiciones. Se sostiene solo porque las segmentaciones y los gráficos dinámicos se movieron a la semana 15, que tiene holgura, y porque el ejercicio 23 versión 2 hace todo el trabajo fino fuera de clase. Si el profesor prefiere no partir el bloque, la alternativa es dejar aquí segmentaciones y gráficos dinámicos y sacar los campos calculados, pero eso deja el objetivo 4.2.5 huérfano y no lo recomiendo.

### Semana 15, sesiones 29 y 30

«Sessions 29 and 30: advanced filters in Excel.» CLO06, evidencia «Workbook with advanced filters and extracted results». El independiente ya incluye trabajo de proyecto.

ADICIONAL:

- **Expert 4.2.3**, segmentación de datos. Es la sesión de filtrado y una segmentación es un filtro con botones.
- **Expert 4.3.1**, crear gráficos dinámicos. Gráficos y tablas dinámicas se enseñan por separado en las semanas 10, 11 y 14 y nunca se juntan.
- **Expert 4.3.2**, opciones del gráfico dinámico: botones de campo, cambiar tipo, filtros del gráfico.
- **Expert 4.3.3**, estilos del gráfico dinámico.
- **Expert 4.3.4**, profundizar en el detalle, expandir y contraer niveles.
- **365, MO-211 3.4.5 y 3.4.6**, FILTER y SORTBY, si el laboratorio corre Microsoft 365. Caen naturales aquí porque hacen con fórmula lo que el filtro avanzado hace con menús.

Ejercicios 24, filtros avanzados con quince filtros de dificultad creciente sobre 27 empleados, incluidos comodines en cuatro variantes y el criterio calculado contra el promedio; y 23 versión 2, tablas dinámicas sobre 26,608 líneas de comandas de restaurante, que trae campo calculado, segmentación por mesero y por tipo, escala de tiempo mensual y gráfico dinámico por mes y tipo.

Carga: dos sesiones para filtros avanzados son generosas, y por eso esta semana recibe el bloque de gráficos dinámicos que no cabía en la 14. Aun así son cinco objetivos nuevos más los dos de 365. Es el reparto más tenso del plan después de la semana 14, y funciona porque el ejercicio 23 versión 2 ya está armado.

Decisión pendiente sobre material: el ejercicio 23 viene por duplicado. La versión 1 es introductoria, la versión 2 es la que cubre el Expert. Hay que declarar cuál es la oficial.

### Semana 16, sesiones 31 y 32

«Sessions 31 and 32: Goal Seek, data tables and scenario analysis», con presentaciones de proyecto encima. CLO08, evidencia «What-if analysis workbook. Final project delivered and presented». Queda cubierto Expert 3.4.2.

ADICIONAL:

- **Expert 3.4.4**, PAGO. No hay una sola función financiera en el syllabus. Una tabla de amortización cae sola aquí y además alimenta el caso de decisión que el led ya pide.
- **Expert 3.4.3**, NPER. Con AND e IF ya vistos en la semana 7 y el pronóstico del what-if, NPER es el tercio que falta del objetivo.
- El Administrador de escenarios se practica, no solo se explica. El syllabus lo pide en «scenario analysis» y el ejercicio 25 lo describe pero no lo usa en ninguno de sus tres casos.

Ejercicio 25, análisis de hipótesis con Buscar objetivo, tablas de datos de una y dos variables y PAGO. Tres modelos: producto de limpieza con punto de equilibrio, automotriz con PAGO y validación de datos para la tasa y el plazo, y compraventa de dólares con tabla de dos variables.

Carga: las presentaciones de proyecto se comen buena parte de una de las dos sesiones. PAGO y NPER son quince minutos juntos si se enseñan sobre el mismo modelo de crédito. El Administrador de escenarios son otros quince. Cabe, apretado.

Aviso de material: el ejercicio 25 solo trae docx, sin xlsx. Los tres modelos los arma el alumno desde cero, lo cual está bien como reto pero cuesta tiempo de clase que esta semana no tiene. Conviene preparar el libro con los datos ya capturados.

### Semana 17, sesiones 33 y 34

La sesión 33 hace «page setup, print area, repeating row and column titles, sheet options; workbook views, zoom, window, freeze panes, split». La sesión 34 es el examen final. CLO09, evidencia «Workbook ready for printing. Final exam». Quedan cubiertos 1.3.1, 1.4.2, 1.4.3, 1.4.4, 1.5.1 y 1.5.3.

ADICIONAL:

- **1.3.3**, encabezados y pies de página de Excel. Los únicos «headers and footers» del syllabus son los de Word en la sesión 2. En Excel viven en la misma caja de diálogo de Configurar página que la sesión ya abre, pegados al área de impresión.
- **1.5.2**, guardar el libro en otros formatos: PDF, CSV, plantilla .xltx, libro habilitado para macros. Las menciones a .pdf y .docx del syllabus son reglas de entrega, no contenido enseñado. El led de la sesión es «Preparing a workbook for printing and distribution», y exportar es distribuir.
- **1.5.4**, Comprobador de compatibilidad. La semana 9 cubrió el Inspector de documento y la 11 el de accesibilidad; falta la tercera pata del objetivo.

Ejercicio 4, configuración de página, área de impresión y vistas del libro, sobre una base de 196 países y 35 columnas que ocupa veinte páginas al imprimir y baja a ocho al fijar el área de impresión.

Carga: solo hay una sesión de clase porque la 34 es el examen final. Tres adiciones cortas, unos veinticinco minutos, todas dentro del cuadro Configurar página o del menú Archivo. Cabe.

Aviso de material: el ejercicio 4 cubre área de impresión, títulos repetidos, orientación, escala, inmovilizar, dividir, cuadrícula y salto de página, pero no toca zoom, ventana nueva ni organizar ventanas, que el syllabus manda literalmente. Tampoco los encabezados y pies de Excel.

## Lo que no cabe

Con el reparto de arriba, 100 de los 107 objetivos de MO-200 y MO-201 quedan dentro de las 34 sesiones. Estos son los que no. No están escondidos en ninguna semana porque no caben en ninguna semana.

### 1. Macros, cinco objetivos del Expert

**Expert 3.6.1** grabar macros simples, **3.6.2** nombrarlas, **3.6.3** editarlas, **1.1.1** copiar macros entre libros y **1.1.3** habilitar macros en un libro.

La palabra «macro» aparece cero veces en las 597 líneas del syllabus. «VBA» y «Visual Basic», cero también. El único falso positivo del grep fue el correo vbalbuena@up.edu.mx. Grabar una macro y leer lo que la grabadora escribió es una sesión completa, no un añadido de diez minutos, y las cuatro semanas con algo de holgura ya recibieron carga: la 8 los *IF singulares, la 15 los gráficos dinámicos, la 11 la protección de rangos y la 17 el bloque de impresión. No hay sesión 35.

**Propuesta.** Un taller de noventa minutos fuera de las 34 sesiones, en la ventana de trabajo independiente de la semana 15, armado con material que ya existe. El deck w01 de TIA503, en `ppts/vba/analisis-y-procesamiento-de-la-informacion/es/w01.es.yaml`, tiene exactamente lo que se necesita y nada más: la lámina de pasos «Cuatro pasos para dejar el entorno listo», con pestaña Programador, guardar como .xlsm, habilitar macros al abrir y Alt+F11, que resuelve el 1.1.3 completo; la lámina de código «Una macro que nadie escribió a mano», con el Sub de dos renglones que la grabadora escribió sola, que es el 3.6.1 con la lectura del código incluida; la tabla «Objeto, propiedad y valor»; la comparación «La grabadora arranca el trabajo, tú lo terminas», donde se quita el renglón que deshace lo que acaba de hacerse, y eso es el 3.6.3 en una sola lámina; los errores de «Cuatro formas de perder la macro»; y el laboratorio «Graba tu primera macro», al que solo hay que cambiarle el archivo por el libro que el alumno ya trae de la semana 9 o 10.

Falta un detalle para el 3.6.2: w01 no tiene lámina de nombres. La regla está en w02.es.yaml, «sin espacios, y no puede empezar con número», que es literalmente la regla del cuadro Grabar macro. Es un renglón que se pega en la lámina de grabación, no una lámina nueva. Para el 1.1.1, w02 también aporta «Botón derecho sobre el módulo, Exportar archivo, y sale el .bas», que resuelve la mitad del objetivo; faltan el Libro de macros personal y arrastrar el módulo entre proyectos en el editor, que TIA503 no toca en ninguna semana.

Lo que no hay que traer de TIA503: todo w03 en adelante, o sea tipos y variables, operaciones, formularios de captura, If, For, For Each, procedimientos, funciones, clases y eventos. MO-201 pide grabar, nombrar y editar macros simples, no programar. w06, «Editar lo grabado», es buen material y es tentador, pero es una sesión entera de VBA y se pasa del objetivo.

Si el taller no se autoriza, la salida honesta es decirlo en el syllabus del siguiente ciclo: el curso prepara para el Associate completo y para el Expert menos el dominio de macros.

### 2. Opciones de idioma, dos objetivos del Expert

**Expert 1.3.1** configurar idiomas de edición y presentación, y **1.3.2** usar características específicas del idioma.

Cero apariciones de «language» o «idioma» en el syllabus. Son dos objetivos de configuración que no requieren demostración en clase y que además desaparecen en MO-211: el temario de 365 elimina el dominio completo. Si el grupo presenta el Expert de 365, estos dos objetivos dejan de existir y no hay nada que hacer. Si presenta MO-201 en español, van anclados al curso autogestivo de INNOVATIQ, que ya vale 5 por ciento del curso y corre todo el semestre.

### 3. Funciones de matriz dinámica, ocho objetivos que dependen de la versión

**MO-210 2.1.5** SEQUENCE, **4.2.4** SORT, **4.2.5** UNIQUE, **MO-211 2.1.3** RANDARRAY, **3.1.1** LET, **3.2.1** XLOOKUP, **3.4.5** FILTER y **3.4.6** SORTBY.

Estas ocho no existen en Office 2019. Están asignadas a semana en la sección de arriba, las semanas 4, 9, 13 y 15, pero con la marca «365» porque su viabilidad no depende del plan sino del laboratorio. Si las máquinas corren Office 2019, no se pueden practicar y el grupo no puede presentar MO-210 ni MO-211 con garantía, por más decks que se autoricen. Esta no es una decisión pedagógica, es una verificación de infraestructura, y hay que hacerla antes de comprar vouchers.

### 4. Dos funciones de fecha del Expert

**Expert 3.3.2**, WEEKDAY y WORKDAY.

La semana 4 ya recibe seis funciones nuevas encima de las diez que el syllabus manda en la sesión 8. Meter dos más de cálculo de días hábiles, que además necesitan explicar el argumento de festivos, revienta la sesión. Propuesta: tarea con solución comentada, sobre el mismo archivo del ejercicio 13, que ya tiene 60 alumnos con fecha de nacimiento y ya practica DIA, MES y AÑO. Son quince minutos de trabajo del alumno y cierran el objetivo sin costo de clase.

### 5. Huecos de material, que no son huecos de cobertura

Estos temas sí tienen semana en el syllabus y sí quedan cubiertos por una sesión, pero ningún ejercicio los practica. Si se autorizan decks, estos son los que además necesitan archivo:

- Word completo, sesiones 1 a 4. No hay un solo ejercicio de Word en el paquete. Cuatro sesiones sin práctica preparada, y el primer parcial evalúa Word con 30 por ciento del curso.
- K.ESIMO.MAYOR y K.ESIMO.MENOR, sesión 7.
- MAX.SI.CONJUNTO y MIN.SI.CONJUNTO, semana 8. El ejercicio 11 solo trae las otras tres.
- Auditoría de fórmulas, sesión 6. El ejercicio 5 cubre precedencia, referencias y nombres, y nunca abre las herramientas.
- Revisión ortográfica, sesión 22.
- Hoja de gráfico, cambiar filas por columnas y texto alternativo, sesión 20. El ejercicio 17 construye veinte gráficos y no pide ninguna de las tres.
- Zoom, ventana nueva y organizar ventanas, sesión 33.
- Administrador de escenarios, semana 16. El ejercicio 25 lo explica en la teoría y no lo usa en ninguno de sus tres casos.
- Tareas faltantes: la carpeta de tareas trae 23 archivos numerados 1 a 15, 17 y 19 a 24. No hay tarea para el 16, tablas; el 18, protección; ni el 25, análisis de hipótesis. Son tres de los temas más pesados.

### 6. Reparaciones del propio material

- El PDF del syllabus tiene dos celdas cortadas: sesión 8, «COUNTA, COUNTBLANK and», y sesión 26, «VLOOKUP, HLOOKUP and». La primera se recuperó con extracción en crudo y cierra con LEFT. La segunda se perdió al generar el archivo. Hay que regenerar el PDF.
- El libro del ejercicio 18 arrastra seis nombres definidos muertos apuntando a #REF!.
- Las fórmulas del ejercicio 16 están guardadas como _xlfn.IFS.
- El ejercicio 23 viene por duplicado y hay que declarar cuál versión es la oficial.
- Los ejercicios 19, 20 y 21 tienen nombres que no dicen lo que enseñan, y los 9, 11 y 12 tienen nombres de carpeta casi idénticos para tres temas distintos.
- El ejercicio 3 tiene la carpeta sin nombre después del guion bajo.
- El archivo de datos del ejercicio 24 se llama «Excel24_instructions(Advanced Filters).xlsx» y no contiene instrucciones.
