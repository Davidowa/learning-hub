# Los términos de interfaz que faltan en español

Lista de trabajo, no prosa. Sale de contar cada término que quedó entre corchetes en
`procedures.es.md` y en los diecisiete decks de `es/`, que es la marca que dejamos donde el
español no se pudo verificar.

Van **364 apariciones** de **229 términos distintos**, más cuatro asuntos que no son
términos sino decisiones. En los archivos quedan 654 corchetes en total: estos 229 términos,
las 90 filas de confianza baja de `GLOSARIO-DOC.es.md` que esperan producto, y unos sesenta
términos multi-contexto que la sustitución excluyó a propósito. Eran 2,977 de 1,209 al arrancar; las 92 capturas del profesor
cerraron 1,016 corchetes, y la pasada contra la documentación de Microsoft del 20 de agosto
de 2026 cerró 816 términos más, con 1744 apariciones. Esa pasada vive en
`GLOSARIO-DOC.es.md`, con URL y confianza por fila, y sus 90 filas de confianza baja
tampoco se sustituyen sin producto, así que cuentan como medio cerradas.

## Lo que cerró la diferencia

Los .docx de instrucciones del profesor traían 92 capturas de pantalla de **Excel corriendo
en español**. Se leyeron una por una antes de retirar la carpeta `Excel/` y salieron 569
cadenas de interfaz verificadas contra el producto, que es mejor fuente que la documentación
de Microsoft. Están en el glosario de `procedures.es.md`, en la sección con clave de fuente
`IMG`, y ya se sustituyeron en los archivos: 1,016 corchetes menos.

La pasada contra la documentación se hizo con dieciocho lotes temáticos y quedó escrita
a archivo por lote, así que un corte de sesión ya no pierde trabajo. El resto de este
archivo es lo que ninguna página pudo cerrar.

## Tres cosas que salieron mal en la sustitución por capturas, y cómo se arreglaron

Valen más que la lista, porque le van a volver a pasar a quien siga.

**El mismo inglés, dos controles distintos.** `Comma` es `Millares` cuando es el estilo de
celda, y es la coma cuando es el delimitador de un archivo de texto. La sustitución automática
puso `Millares` en la lista de delimitadores de tres lugares. Se revirtieron a corchete; la
pasada de documentación ya cerró el delimitador como `Coma`, con el contexto verificado.

**Excel corta sus propias listas.** `Automatic` se leyó como `Automat.` en las dos capturas
donde sale, porque el cuadro de lista lo trunca. Un truncamiento no es una traducción, así que
esas filas volvieron a corchete.

**El botón no dice la palabra.** `Bold` en la minibarra es la letra `N`, no `Negrita`. Para
prosa se usa `Negrita`, que sí aparece en la lista de estilos de fuente del cuadro Formato de
celdas. Lo mismo con `Italic`, `K` contra `Cursiva`.

La pasada de documentación dejó siete trampas más; están al frente de `GLOSARIO-DOC.es.md`.

## Cuatro decisiones que no son términos

- **`Quantity`, `@Quantity` y `Order Date`** son encabezados de columna de los libros de
  ejercicios, y **`Sales.xlsx`** es un nombre de archivo. Traducirlos significa renombrar
  columnas y archivos en los ejercicios, no llenar un glosario. Decisión del profesor.
- Un corchete en MO201 dice "En el Excel en español son Tabla1, Tabla2: confirmar."; es una
  nota editorial, no un término, y se confirma con el producto.

## Cómo se cierra lo que queda

Con un Excel en español enfrente. La documentación ya dio lo que tenía: cada término de la
lista de abajo se buscó y ninguna página de Microsoft lo nombra, o lo nombra en una
traducción a máquina que no se puede citar. La columna de nota trae el candidato que la
pasada dejó anotado, marcado sin evidencia; sirve para buscarlo rápido en el producto, no
para sustituirlo.

Esta máquina no puede cerrarlo sola. Tiene el corrector en español y no el paquete de idioma
de la interfaz:

    HKLM\SOFTWARE\Microsoft\Office\ClickToRun\Configuration  ClientCulture = en-us
    Office16\1033\XLINTL32.DLL                                 existe
    Office16\3082\                                             solo MSO.ACL, corrector

## La lista

229 términos, por número de apariciones.

| Término en inglés | Apariciones | Contexto | Candidato anotado, sin evidencia |
|---|---|---|---|
| `**Formula result =**` | 7 | Etiqueta inferior del cuadro de diálogo Argumentos de función | Ninguna página MS en español muestra la etiqueta; en el producto suele ser 'Resultado de la fórmula ='. DECIDIR HUMANO |
| `Group Field` | 7 | Boton de cinta, Analizar tabla dinamica > grupo Agrupar; abre el cuadro Agrupar | Las paginas es solo documentan el clic derecho 'Agrupar'; el boton de cinta no aparece nombrado. Probable 'Agrupar campo' (sin verificar en docs). |
| `Stop value` | 7 | Cuadro Stop value del diálogo Series | La única página encontrada dice 'Valor de detención' y es traducción automática dudosa; el producto suele decir 'Límite'. Sin evidencia confiable. DECIDIR HUMANO |
| `Field Buttons` | 5 | Boton de PivotChart Analyze, grupo Show/Hide, para los botones de campo del grafico | No aparece en las paginas es revisadas. Probable 'Botones de campo' (sin verificar). |
| `Always Open Read-Only` | 4 | opción de Archivo > Información > Proteger libro | sin evidencia limpia: la página de Word trae dos variantes automáticas ('Abrir siempre en modo de solo lectura', 'Abrir siempre solo lectura') y ninguna página de Excel cita el comando; verificar en el producto |
| `Apply` | 4 | Botón Aplicar del Administrador de reglas de formato condicional (confirma sin cerrar) | Ninguna página MS en español muestra el caption del botón; en el producto suele ser 'Aplicar'. DECIDIR HUMANO |
| `Confirm Password` | 4 | cuadro de diálogo de confirmación al poner contraseña | ninguna página es-es cita el título del cuadro; los artículos solo dicen 'Vuelva a escribir la contraseña'; verificar en el producto |
| `Delete Rule` | 4 | Botón del Administrador de reglas de formato condicional | La página de formato condicional consultada no contiene el caption textual; en el producto suele ser 'Eliminar regla'. DECIDIR HUMANO |
| `Excel Macro-Enabled Workbook (\*.xlsm)` | 4 | tipo de archivo en Guardar como | las páginas es lo muestran con traducciones automáticas incoherentes ('Libro de Excel (código)', 'Libro Macro-Enabled Excel (código)', 'Excel Macro-Enabled libro'); el nombre real del producto no se pudo confirmar |
| `Formula result` | 4 | Etiqueta inferior del cuadro Argumentos de función | Sin página MS que muestre la etiqueta; suele ser 'Resultado de la fórmula ='. DECIDIR HUMANO |
| `Formula result =` | 4 | Etiqueta inferior del cuadro Argumentos de función | Sin página MS que muestre la etiqueta; suele ser 'Resultado de la fórmula ='. DECIDIR HUMANO |
| `From Text (Legacy)` | 4 | Comando Datos > Obtener datos > Asistentes heredados para importar un archivo de texto | La única página (traducción automática) escribe 'a partir del texto (heredado)', que no es caption verosímil; el producto probablemente dice 'Desde el texto (heredado)'. DECIDIR HUMANO |
| `Math & Trig` | 4 | Botón de categoría del grupo Biblioteca de funciones | La categoría documentada es 'Funciones matemáticas y trigonométricas'; el botón de la cinta suele abreviarse 'Mat y trig' pero ninguna página MS lo muestra. DECIDIR HUMANO |
| `Password to modify` | 4 | cuadro de Opciones generales en Guardar como | el artículo es-es está traducido automáticamente y no cita la etiqueta del cuadro; verificar en el producto |
| `Protect Workbook Structure` | 4 | opción de Archivo > Información > Proteger libro | la página solo usa la frase en prosa 'proteger la estructura de un libro de Excel'; el nombre del comando no aparece citado |
| `Step value` | 4 | Cuadro Step value del diálogo Series | La única página encontrada dice 'Paso' y es traducción automática dudosa; el producto suele decir 'Incremento'. Sin evidencia confiable. DECIDIR HUMANO |
| `AutoFill` | 3 | Opción de la lista Tipo en el cuadro de diálogo Series (Lineal, Geométrica, Cronológica, Autorrellenar) | sin página de Microsoft que dé la etiqueta de la lista; forma de producto esperada 'Autorrellenar' |
| `Circle Invalid Data` | 3 | Menú de la flecha de Validación de datos, pestaña Datos | Las páginas es solo traen variantes automáticas que no concuerdan ("Círculo de validación de datos no válidos", "Círculo con datos no válidos"). El producto lee "Rodear con un círculo datos no válidos", pero sin página que lo imprima. Coincide con el NO SOURCE ya anotado en el glosario. |
| `Colorful` | 3 | Grupo de paletas de la galería Cambiar colores en gráficos | sin página que nombre los grupos de la galería; forma de producto esperada 'Multicolor' (y 'Monocromático' para la otra mitad) |
| `Date unit` | 3 | Grupo del cuadro de diálogo Series que se habilita con Tipo=Cronológica | Ninguna página MS muestra el caption ('Unidad de fecha' o 'Unidad de tiempo' según versión). DECIDIR HUMANO |
| `Day` | 3 | Opción de Unidad de fecha del cuadro de diálogo Series | Sin evidencia; OJO: en el diálogo Series en español esta opción podría aparecer como 'Fecha', no 'Día'. DECIDIR HUMANO |
| `Do not detect data types` | 3 | Opción de la lista Data Type Detection en Desde texto/CSV | Ninguna página de Microsoft en español trae el rótulo verbatim; el conector Text/CSV solo lo parafrasea ('desactivar la detección automática de tipos de datos'); necesita captura de pantalla |
| `Edit in Formula Bar` | 3 | Botón del cuadro de diálogo Comprobación de errores | La página de detectar errores confirma 'Omitir error' pero no transcribe este botón ('Modificar en la barra de fórmulas' no aparece). DECIDIR HUMANO |
| `Ending at` | 3 | Cuadro del diálogo Agrupar clásico de tabla dinámica | MS solo documenta el diálogo nuevo ('Desde'/'Hasta'); el clásico probablemente dice 'Terminar en' pero sin página MS que lo confirme. DECIDIR HUMANO |
| `Merge Across` | 3 | Opción del menú de la flecha de Combinar y centrar | la página es de combinar celdas es traducción automática y no la nombra; forma de producto esperada 'Combinar horizontalmente' |
| `Monochromatic` | 3 | Galería Cambiar colores de Estilos de gráfico, nombre de sección (par de [Colorful]) | ninguna página es de Microsoft nombra las secciones de la galería; probable 'Monocromático', sin evidencia; confirmar en producto |
| `Operation` | 3 | Cuadro de diálogo Pegado especial, sección de operaciones aritméticas | las páginas encontradas discrepan y huelen a traducción automática ('Funcionamiento' en una, 'Opciones de la operación' en la de Mac); probable 'Operación', sin página confiable; confirmar en producto |
| `Publish what` | 3 | Cuadro Opciones al publicar PDF/XPS, nombre de la sección | ninguna página es lo documenta; probable 'Publicar qué'; confirmar en producto |
| `Quantity` | 3 | Nombre de columna de las tablas de los archivos de ejercicio (referencias estructuradas como Orders[Quantity]) | NO es interfaz de Microsoft: es dato del curso; traducirlo exige renombrar la columna en los libros de ejercicio; DECISIÓN HUMANA |
| `Sales.xlsx` | 3 | Nombre de archivo dentro de fórmulas de referencia externa ([Sales.xlsx]Q1!$B$4) | NO es interfaz de Microsoft: es nombre de archivo del ejercicio; DECISIÓN HUMANA si se localiza el archivo |
| `Show/Hide` | 3 | Pestaña Analizar gráfico dinámico, grupo de la cinta | ninguna página es lo nombra; probable 'Mostrar u ocultar'; el archivo fuente ya trae TO CONFIRM en esta zona; confirmar en producto |
| `Year` | 3 | Cuadro de diálogo Series (Rellenar > Series), opción de Unidad de fecha | ninguna página es cita las opciones del cuadro Series; probable 'Año'; confirmar en producto |
| `+/- Buttons` | 2 | Pestaña Analizar tabla dinámica / gráfico dinámico, grupo Mostrar, botón de alternancia | ninguna página es nombra el botón de la cinta; probable 'Botones +/-'; la página de Opciones de tabla dinámica solo documenta la casilla 'Mostrar botones de expandir y contraer' (control distinto); el archivo fuente ya trae TO CONFIRM |
| `Add a description` | 2 | Panel Accesibilidad, Acciones recomendadas | ninguna página es lo cita; probable 'Agregar una descripción'; confirmar en producto |
| `Any value` | 2 | Validación de datos, primera entrada de la lista Permitir | ninguna página es lo cita (las páginas de validación omiten la primera entrada); probable 'Cualquier valor'; confirmar en producto |
| `Buttons` | 2 | Pestaña Segmentación de datos, grupo de la cinta con Columnas/Alto/Ancho | ninguna página es nombra el grupo; probable 'Botones'; confirmar en producto |
| `Cascade` | 2 | Cuadro de diálogo Organizar ventanas, opción | las páginas es dejan 'Cascade' sin traducir (traducción automática); probable 'Cascada'; confirmar en producto |
| `Change File Type` | 2 | Archivo > Exportar, segunda loseta | ninguna página es lo cita; probable 'Cambiar el tipo de archivo'; confirmar en producto |
| `Clear Formatting` | 2 | Opción del botón Opciones de inserción al insertar filas o columnas | sin página; forma de producto esperada 'Borrar formato' (el comando Borrar del grupo Edición usa 'Borrar formatos', es otro control) |
| `Comments and notes` | 2 | Configurar página, pestaña Hoja: nombre de la lista en Microsoft 365 | la página es-ES solo muestra la etiqueta 'Comentarios' (redacción 2019); el nombre 365 'Comentarios y notas' para ESTA lista no se encontró documentado; decidir con producto |
| `Distributed (Indent)` | 2 | Formato de celdas > Alineación, lista Horizontal | ninguna página es lista las opciones de la lista Horizontal; probable 'Distribuido (Sangría)'; confirmar en producto |
| `Document Properties` | 2 | el curso lo usa para dos cosas distintas: el cuadro de Propiedades avanzadas y el módulo del Inspector | ambiguo, necesita revisión humana; el módulo del Inspector se llama 'Propiedades del documento e información personal'; el título del cuadro de propiedades no está documentado en es |
| `Edit...` | 2 | Botón del Administrador de nombres y del Administrador de escenarios | las páginas es de ambos administradores describen la acción pero no citan el botón; probable 'Editar...'; confirmar en producto |
| `Entire workbook` | 2 | opción de Publicar qué en las Opciones al guardar PDF | sin página es que cite la casilla; el comando equivalente del menú de impresión documentado es 'Imprimir todo el libro' |
| `For all documents (default)` | 2 | Lista Personalizar barra de herramientas de acceso rápido (Archivo, Opciones) | no citado en la página oficial; probable 'Para todos los documentos (predeterminado)'; verificar en producto |
| `Greater Than...` | 2 | DOBLE contexto: Filtros de número (AutoFiltro) y galería Resaltar reglas de celdas (Formato condicional) | DECISIÓN HUMANA: Filtros de número = 'Mayor que...' (confirmado); en la galería de formato condicional las páginas también escriben 'Mayor que' pero el producto muestra 'Es mayor que...'. Verificar en producto. |
| `Group Selection` | 2 | Boton de cinta, Analizar tabla dinamica > grupo Agrupar | Las paginas es solo documentan el clic derecho 'Agrupar'. Probable 'Agrupar selección' (sin verificar en docs). |
| `Group1` | 2 | Nombre de elemento que Excel genera al agrupar una seleccion | Nombre generado por el producto; ninguna pagina es lo documenta. Probable 'Grupo1' (sin verificar). |
| `Help on this Error` | 2 | Opción del cuadro Comprobación de errores | No aparece impreso en las páginas es revisadas. El producto presumiblemente lee "Ayuda sobre este error"; sin fuente. |
| `Hide All` | 2 | Botones de campo de un gráfico dinámico (Analizar), opción para ocultarlos todos | no encontrado en ninguna página; probable 'Ocultar todo'; verificar en producto |
| `Ignore print areas` | 2 | casilla de las Opciones al publicar PDF | sin página es que cite la casilla; verificar en el producto |
| `Inside End` | 2 | Posición de etiquetas de datos de un gráfico | no citado en ninguna página recuperable; probable 'Extremo interno' (par del 'Extremo externo' indexado en la página es de etiquetas de datos); verificar en producto |
| `Justify` | 2 | Listas Horizontal y Vertical de Formato de celdas, pestaña Alineación | no citado en las páginas de alineación; probable 'Justificar'; verificar en producto |
| `Left (Indent)` | 2 | Lista Horizontal de Formato de celdas, pestaña Alineación | no citado en docs; probable 'Izquierda (sangría)'; verificar en producto |
| `Logicals` | 2 | Casilla bajo Fórmulas en el cuadro Ir a Especial | no citado en las páginas de Ir a Especial; probable 'Lógicos'; verificar en producto |
| `Maximum` | 2 | DOBLE contexto: cuadro de Validación de datos y regla de formato condicional (barras de datos/escalas) | DECISIÓN HUMANA: Validación de datos = 'Máximo'; Nueva regla de formato = 'Máxima' (género distinto según el cuadro) |
| `Minimum` | 2 | DOBLE contexto: cuadro de Validación de datos y regla de formato condicional (barras de datos/escalas) | DECISIÓN HUMANA: Validación de datos = 'Mínimo'; Nueva regla de formato = 'Mínima' |
| `More Rules...` | 2 | Último elemento de las galerías de Formato condicional (abre Nueva regla de formato) | ninguna página lo cita; probable 'Más reglas...'; verificar en producto |
| `New Range` | 2 | Título del cuadro que abre Nuevo en Permitir que los usuarios editen rangos | la página describe el botón 'Nuevo' pero nunca nombra el título del cuadro; probable 'Nuevo rango'; verificar en producto |
| `New worksheet` | 2 | Opción del cuadro Importar datos (¿Dónde desea situar los datos?) | DECISIÓN HUMANA: sin cita para el cuadro Importar datos; candidatos 'Hoja de cálculo nueva' (probable ahí) y 'Nueva hoja de cálculo' (confirmada solo en Crear tabla dinámica) |
| `Order Date` | 2 | Nombre de columna del dataset del ejercicio (tabla Lorena), usado en referencias estructuradas | DECISIÓN HUMANA: no es interfaz de Excel; es un encabezado de datos del libro del ejercicio. Traducirlo obliga a renombrar la columna en el libro (p. ej. 'Fecha de pedido'). |
| `Print settings` | 2 | casilla de Incluir en la vista, cuadro Agregar vista (vistas personalizadas) | el artículo de vistas personalizadas describe el paso pero no cita las casillas; verificar en el producto |
| `Protect worksheet and contents of locked cells` | 2 | casilla superior del cuadro Proteger hoja | la página describe el flujo pero no cita la casilla; verificar en el producto |
| `Right (Indent)` | 2 | Lista Horizontal de Formato de celdas, pestaña Alineación | no citado en docs; probable 'Derecha (sangría)'; verificar en producto |
| `Rule` | 2 | Columna del Administrador de reglas de formato condicional | ninguna página cita el encabezado; probable 'Regla (aplicada en el orden mostrado)'; la página lo describe en prosa como 'tipo de regla' |
| `Select Arguments` | 2 | Cuadro que aparece al insertar INDICE (función con varias formas) | ni la página de INDICE ni la búsqueda de soporte lo citan; probable 'Seleccionar argumentos'; verificar en producto |
| `Select versions to show` | 2 | Lista del Comprobador de compatibilidad | no citado; probable 'Seleccionar versiones para mostrar'; verificar en producto |
| `Selection` | 2 | DOBLE contexto: Configuración de Archivo, Imprimir y cuadro Opciones al publicar PDF/XPS (Publicar qué) | DECISIÓN HUMANA: en Imprimir el escritorio usa 'Imprimir selección' (la página moderna muestra 'Selección actual'); en el cuadro de PDF la opción es probablemente 'Selección'; ninguna página lo cita limpio |
| `Standard` | 2 | Pestaña del selector de colores que abre Más colores | no citado en las páginas de color de relleno; probable 'Estándar'; verificar en producto |
| `Status` | 2 | Columna del cuadro clásico Editar vínculos | la página moderna cita 'Actualizar valores' y 'Cambiar origen' pero no la columna; probable 'Estado'; verificar en producto |
| `Tab` | 2 | DOBLE contexto: casilla del Asistente para convertir texto en columnas y lista Delimitador de Power Query | DECISIÓN HUMANA: el asistente clásico usa 'Tabulación' (solo descrito en prosa como 'tabulaciones'); Power Query usa 'Tabulador' (confirmado como elemento de lista). Misma trampa que Comma/Millares. |
| `Table Column to the Right` | 2 | Menú contextual Insertar dentro de una tabla | DECISIÓN HUMANA: la página (traducción automática) escribe 'columnas de tabla a la derecha' en plural; el menú clásico probablemente 'Columna de la tabla a la derecha' (singular). Verificar en producto. |
| `Table Row Below` | 2 | Menú contextual Insertar dentro de una tabla | DECISIÓN HUMANA: la página (traducción automática) escribe 'Filas de tabla por debajo'; el menú clásico probablemente 'Fila de la tabla abajo' (singular). Verificar en producto. |
| `Table Rows Above` | 2 | Menú contextual Insertar dentro de una tabla | DECISIÓN HUMANA: la página (traducción automática) escribe 'Filas de la tabla superior' y 'Filas de tabla por encima'; el menú clásico probablemente 'Filas de la tabla arriba'. Verificar en producto. |
| `Validation` | 2 | Opción de la sección Pegar del cuadro Pegado especial | Ninguna página es imprime la lista completa de opciones del Pegado especial de Excel. El producto presumiblemente lee "Validación"; sin fuente. |
| `Where do you want to put the data?` | 2 | Pregunta del cuadro Importar datos tras el Asistente para importar texto | no documentado textualmente: la página solo parafrasea 'elija dónde desea colocar los datos'; candidatas '¿Dónde desea colocar los datos?' / '¿Dónde desea situar los datos?' — verificar en el producto |
| `Windows` | 2 | Casilla del cuadro Proteger estructura y ventanas (Revisar > Proteger libro); hoy aparece atenuada | no documentado: la página solo trae el pie de imagen 'Proteger estructura y Windows' (a medio traducir); la casilla del producto presumiblemente dice 'Ventanas' pero ninguna página lo confirma |
| `"Ctrl+click cells to select non-adjacent changing cells."` | 1 | Línea de ayuda del cuadro Agregar escenario (Administrador de escenarios) | no encontrado en páginas de Microsoft en español; texto interno del diálogo, transcribir del producto |
| `"Divide by Zero Error"` | 1 | Encabezado que muestra el cuadro Comprobación de errores | Texto de la interfaz no documentado. El producto presumiblemente lee "Error de división por cero"; sin fuente. |
| `"Enter values for each of the changing cells."` | 1 | Línea del cuadro Valores del escenario | no encontrado en páginas de Microsoft en español; transcribir del producto |
| `"Error in cell D1"` | 1 | Texto del cuadro Comprobación de errores que nombra la celda | Texto de la interfaz no documentado. El producto presumiblemente lee "Error en la celda D1"; sin fuente. |
| `"Green, Table Style Medium 7"` | 1 | Nombre de miniatura en la galería de estilos de tabla | los nombres de la galería no están documentados; forma esperada 'Verde, Estilo de tabla medio 7'; confirmar en el producto |
| `"No Scenarios defined. Choose Add to add scenarios."` | 1 | Texto del Administrador de escenarios en una hoja sin escenarios | Texto de la interfaz no documentado; sin fuente. |
| `"Select the cells that you would like to watch the value of:"` | 1 | Línea del cuadro Agregar inspección | Texto de la interfaz no documentado; sin fuente. |
| `"This function has multiple argument lists. Please select one of them."` | 1 | Línea del cuadro Seleccionar argumentos (INDICE) | no encontrado en páginas de Microsoft en español; transcribir del producto |
| `**Logical**` | 1 | Botón desplegable del grupo Biblioteca de funciones (pestaña Fórmulas) | no documentado: las páginas solo traen la categoría 'Funciones lógicas'; el botón de la cinta suele decir 'Lógicas' — confirmar en el producto |
| `**Properties**` | 1 | grupo de la pestaña Diseño de tabla | sin página es que cite el nombre del grupo; verificar en el producto |
| `@Quantity` | 1 | Referencia estructurada a la columna 'Quantity' de la tabla del ejercicio (Lorena) | decisión humana: no es control de Excel sino encabezado de los datos del curso; si los libros conservan encabezados en inglés queda '[@Quantity]', si se traducen sería '[@Cantidad]' |
| `Accept suggestions` | 1 | Entrada del botón Opciones de relleno rápido que aparece tras aplicar Relleno rápido | no documentado en las páginas en español (el propio procedimiento fuente lo marca TO CONFIRM); transcribir del producto |
| `Add current selection to filter` | 1 | Casilla bajo el cuadro de búsqueda del Autofiltro | Sin fuente es. El producto presumiblemente lee "Agregar la selección actual al filtro". |
| `Add Scenario` | 1 | Cuadro de diálogo tras el botón Agregar del Administrador de escenarios | El artículo es no imprime el título del cuadro. El producto presumiblemente lee "Agregar escenario"; sin fuente. |
| `Add View` | 1 | Título del cuadro que abre el botón Agregar... de Vistas personalizadas | no documentado: la página confirma 'Vistas personalizadas', el botón 'Agregar' y la sección 'Incluir en la vista', pero no imprime el título 'Agregar vista' |
| `Arguments:` | 1 | Lista del cuadro Seleccionar argumentos (INDICE) | no encontrado; el cuadro Seleccionar argumentos no está documentado en las páginas en español revisadas |
| `Arrange Windows` | 1 | Título del cuadro de diálogo que abre Vista > Ventana > Organizar todo | no documentado: las páginas solo nombran el botón 'Organizar todo'; el título probable del cuadro es 'Organizar ventanas' pero ninguna página lo imprime |
| `AutoRecover file location` | 1 | cuadro de Archivo > Opciones > Guardar | ninguna página es cita el cuadro; verificar en el producto |
| `Bar Appearance` | 1 | Sección del cuadro Nueva regla de formato para Barras de datos | no encontrado en páginas de Microsoft en español; transcribir del producto |
| `Blue, Table Style Medium 2` | 1 | Nombre de miniatura en la galería de estilos de tabla | los nombres de la galería no están documentados; forma esperada 'Azul, Estilo de tabla medio 2'; confirmar en el producto |
| `Bottom 10 Items...` | 1 | Formato condicional, menú Reglas superiores e inferiores | no documentado; la página solo imprime '10 elementos superiores' y '10% de valores inferiores'; el simétrico '10 elementos inferiores...' es probable pero sin evidencia |
| `Cells containing data types that couldn't refresh` | 1 | Regla 11 de comprobación de errores en Opciones de Excel (compilación 365) | Las páginas es-es y es-mx de 'Detectar errores en fórmulas' solo listan 9 reglas (falta la tanda 10-12 nueva); necesita captura o humano |
| `Cells containing years represented as 2 digits` | 1 | Regla de comprobación de errores en Opciones de Excel > Fórmulas | no encontrado: las páginas 'Detectar errores en fórmulas' en español devolvieron 403/404; candidata 'Celdas que contienen años representados con 2 dígitos' — transcribir del producto |
| `Check Compatibility` | 1 | Comando de Archivo > Información > Comprobar si hay problemas; abre el Comprobador de compatibilidad | no documentado textualmente: la página acredita el diálogo 'Comprobador de compatibilidad', pero ninguna página imprime el comando del menú (presumiblemente 'Comprobar compatibilidad') — verificar en el producto |
| `Choose Display and Help Languages` | 1 | título de bloque del panel Archivo > Opciones > Idioma en Office 2019 | la página vigente solo documenta la UI nueva ("Idioma de visualización de Office"); candidato probable "Elegir idiomas de la Ayuda y de presentación"; decidir con Office 2019 a la vista |
| `Choose Editing Languages` | 1 | título de bloque del panel Archivo > Opciones > Idioma en Office 2019 | misma situación; candidato probable "Elegir idiomas de edición"; decidir con Office 2019 a la vista |
| `Clear Rules from This PivotTable` | 1 | Opcion del submenu Borrar reglas del formato condicional | Las paginas es solo documentan 'Borrar reglas de celdas seleccionadas' y 'Borrar reglas de toda la hoja'. Probable 'Borrar reglas de esta tabla dinámica' (sin verificar). |
| `Clear Rules from This Table` | 1 | Inicio > Formato condicional > Borrar reglas (entrada en gris fuera de una tabla) | no citado en docs de MS; los hermanos sí están documentados; candidato "Borrar reglas de esta tabla"; confirmar en producto |
| `Column A` | 1 | lista Columnas del diálogo Quitar duplicados cuando no hay encabezados | sin cita en docs de MS; candidato "Columna A"; confirmar en producto |
| `Comment:` | 1 | cuadro del diálogo Agregar escenario (viene precargado con nombre y fecha) | sin cita en docs de MS; candidatos "Comentarios:" (probable, el diálogo español usa plural) o "Comentario:"; decidir humano |
| `Compare` | 1 | botón de la barra al abrir una versión del historial de versiones | sin cita textual en docs de MS (la página del historial solo cita "Restaurar"); candidato "Comparar"; confirmar en producto |
| `Convert to Comments` | 1 | Revisar > grupo Notas | los artículos de notas de MS no citan el comando; candidato "Convertir en comentarios" (así lo escriben guías de terceros); confirmar en producto |
| `Copies:` | 1 | contador superior del panel Archivo > Imprimir | sin cita en docs de MS; candidato "Copias:"; confirmar en producto |
| `Copy Cells` | 1 | menú contextual al arrastrar el controlador de relleno con el botón derecho | sin cita en docs de MS; candidato "Copiar celdas"; confirmar en producto |
| `Create` | 1 | botón del cuadro de diálogo Configuración de esquema (Datos > Esquema) | la página del esquema no nombra el botón (solo "Aceptar"); candidato "Crear"; confirmar en producto |
| `Current value:` | 1 | diálogo Estado de la búsqueda de objetivo | sin cita en docs de MS (el artículo de Buscar objetivo no describe el diálogo de estado); candidato "Valor actual:"; confirmar en producto |
| `Date` | 1 | tipo de serie en el diálogo Serie (Inicio > Rellenar > Series) | OJO: no traducir "Fecha" a ciegas; en el diálogo Serie del producto los tipos son Lineal/Geométrica/Cronológica/Autorrellenar, así que el candidato es "Cronológica"; las páginas es de MS traducen automáticamente ("Crecimiento" por Growth) y no citan este control; decidir humano |
| `Delete Watch` | 1 | Botón de la ventana Inspección | La página es corta el rótulo (imprime "Haga clic en la"). El producto presumiblemente lee "Eliminar inspección"; sin fuente legible. |
| `Display header` | 1 | casilla del cuadro Configuración de la segmentación de datos | el artículo de segmentaciones no cita la casilla; verificar en el producto |
| `Distributed` | 1 | lista Vertical en Formato de celdas > Alineación | sin cita en docs de MS; candidato "Distribuido"; confirmar en producto |
| `Document properties` | 1 | casilla de las Opciones al publicar PDF | sin página es que cite la casilla; verificar en el producto |
| `Double` | 1 | lista Subrayado en Formato de celdas > Fuente | sin cita en docs de MS; candidato "Doble" (hermanos: "Doble contabilidad"); confirmar en producto |
| `Edit Anyway` | 1 | botón de la barra amarilla "Marcado como final" | sin cita en docs de MS; candidato "Editar de todos modos"; confirmar en producto |
| `Empty reference` | 1 | abreviatura del curso (tabla de reglas de comprobación de errores en w07); no es una cadena de la UI | corresponde a la regla "Formulas referring to empty cells" = "Fórmulas que se refieran a celdas vacías"; decidir con un humano si la abreviatura del curso se traduce como "Referencia vacía" o se usa el nombre completo de la regla |
| `Encrypt Document` | 1 | nombre del cuadro de diálogo que abre Cifrar con contraseña | la página cita "Cifrar con contraseña" pero no el nombre del diálogo; candidato "Cifrar documento"; confirmar en producto |
| `Error Checking Options...` | 1 | Opción del menú del botón de error | No impreso en los docs es revisados. El producto presumiblemente lee "Opciones de comprobación de errores..."; sin fuente. |
| `Export File...` | 1 | menú contextual de un módulo en el Editor de Visual Basic | sin cita en docs de MS; candidato "Exportar archivo..." (el VBE en español localiza sus menús); confirmar en producto |
| `Fill & Line` | 1 | Pestaña del panel de formato de elementos de gráfico | sin página que la nombre; forma de producto esperada 'Relleno y línea' |
| `Fill Days` | 1 | Menú contextual del controlador de relleno (arrastre con botón derecho) y Opciones de autorrelleno | las páginas es de relleno no listan el menú; forma esperada 'Rellenar días' |
| `Fill Formatting Only` | 1 | Menú contextual del controlador de relleno y Opciones de autorrelleno | sin página; etiqueta del producto por confirmar (posible 'Rellenar formatos solo') |
| `Fill Months` | 1 | Menú contextual del controlador de relleno y Opciones de autorrelleno | sin página; forma esperada 'Rellenar meses' |
| `Fill Weekdays` | 1 | Menú contextual del controlador de relleno y Opciones de autorrelleno | sin página; forma esperada 'Rellenar días de la semana' |
| `Fill Without Formatting` | 1 | Menú contextual del controlador de relleno y Opciones de autorrelleno | sin página; forma esperada 'Rellenar sin formato' |
| `Fill Years` | 1 | Menú contextual del controlador de relleno y Opciones de autorrelleno | sin página; forma esperada 'Rellenar años' |
| `Fit All Columns on One Page` | 1 | opción de escala en Archivo > Imprimir | el artículo de escalado solo cita 'Ajustar hoja en una página'; esta opción no aparece citada |
| `Fit All Rows on One Page` | 1 | opción de escala en Archivo > Imprimir | el artículo de escalado solo cita 'Ajustar hoja en una página'; esta opción no aparece citada |
| `Fit selection` | 1 | opción del cuadro de diálogo Zoom (Vista > Zoom) | sin cita en docs de MS; candidato "Ajustar la selección a la ventana"; confirmar en producto |
| `Flash Fill Options` | 1 | Botón que aparece tras aplicar Relleno rápido | sin página; forma esperada 'Opciones de relleno rápido'; la característica sí está documentada como 'Relleno rápido' |
| `From` | 1 | lista de idioma de origen del panel Traductor (Revisar > Traducir) | sin cita en docs de MS; candidatos "De" o "Idioma de origen" según versión del panel; decidir humano |
| `General Options` | 1 | Comando del menú Herramientas del cuadro Guardar como (contraseñas de apertura/escritura) | REVISAR HUMANO: ninguna página es actual imprime el nombre; las páginas de contraseñas documentan solo Cifrar con contraseña. Probable 'Opciones generales', sin evidencia |
| `General Options...` | 1 | Mismo comando, con puntos suspensivos (Guardar como > Herramientas) | REVISAR HUMANO: igual que 'General Options'; probable 'Opciones generales...', sin evidencia |
| `Help on this error` | 1 | Opción del menú del botón de error (variante en minúscula) | Igual que Help on this Error: sin fuente es. |
| `Hidden rows` | 1 | Abreviatura en w17 de la casilla 'Hidden rows, columns and filter settings' del cuadro Agregar vista (Vistas personalizadas) | La página solo lo describe en prosa ('filas y columnas ocultas... configuración de filtro'); la etiqueta exacta de la casilla no aparece impresa en ninguna página |
| `Hidden rows, columns and filter settings` | 1 | Casilla del cuadro Agregar vista, vistas personalizadas | El artículo describe la opción pero no imprime el rótulo de la casilla; sin fuente. |
| `Hide Detail` | 1 | Botón del grupo Esquema, pestaña Datos | REVISAR HUMANO: la página de esquematizar no imprime el rótulo del botón; probable 'Ocultar detalle', sin evidencia |
| `Insert File Path` | 1 | Botón del cuadro de diálogo Encabezado/Pie de página (Configurar página) | REVISAR HUMANO: ningún artículo imprime el nombre del botón; el elemento de cinta relacionado es 'Ruta de acceso del archivo' (tampoco verificado) |
| `Insert Picture` | 1 | Botón del cuadro de diálogo Encabezado/Pie de página (Configurar página) | REVISAR HUMANO: probable 'Insertar imagen'; ninguna página lo imprime como botón de ese cuadro |
| `Inside Base` | 1 | Posición de etiquetas de datos en gráficos de columnas (Agregar elemento de gráfico > Etiquetas de datos) | REVISAR HUMANO: probable 'Base interior'; las páginas de etiquetas de datos no imprimen la lista de posiciones |
| `Keep the last AutoRecovered version if I close without saving` | 1 | casilla de Archivo > Opciones > Guardar | ninguna página es cita la casilla; verificar en el producto |
| `Layout 1` | 1 | Primer elemento de la galería Diseño rápido (Diseño de gráfico) | REVISAR HUMANO: 'Diseño rápido' sí está verificado en la página; los nombres 'Diseño 1..n' de la galería no aparecen en ninguna página; probable 'Diseño 1' |
| `Length` | 1 | Cuadro que aparece con el criterio Longitud del texto en Validación de datos | REVISAR HUMANO: probable 'Longitud'; ninguna página imprime la etiqueta del cuadro (el criterio sí: 'Longitud del texto') |
| `Less Than...` | 1 | Comando del submenú Formato condicional > Resaltar reglas de celdas | REVISAR HUMANO: probable 'Es menor que...'; las páginas solo imprimen 'menor que' como operador del cuadro Nueva regla de formato, que es otro control |
| `Lines` | 1 | Elemento del menú Agregar elemento de gráfico (líneas de mínimos/máximos, líneas verticales) | REVISAR HUMANO: probable 'Líneas'; ninguna página imprime el elemento del menú |
| `Link to content` | 1 | Casilla de la pestaña Personalizado de Propiedades avanzadas | La página de propiedades no imprime la casilla. El producto presumiblemente lee "Vincular al contenido"; sin fuente. |
| `Location Range:` | 1 | Cuadro del diálogo Crear minigráficos | REVISAR HUMANO: probable 'Rango de ubicación:'; 'Rango de datos' sí está verificado pero ninguna página imprime el segundo cuadro |
| `Magnification` | 1 | Sección de opciones del cuadro de diálogo Zoom (Vista > Zoom) | REVISAR HUMANO: probable 'Ampliación'; ninguna página localizada imprime la etiqueta |
| `Maximum Value Options` | 1 | Encabezado 'Vertical Axis Maximum Value Options' del menú Eje (Minigráfico > Grupo) | REVISAR HUMANO: las subopciones sí están verificadas ('Automático para cada minigráfico', 'Igual para todos los minigráficos', 'Personalizado'); el encabezado del menú no aparece impreso |
| `Merge` | 1 | Nombre informal del menú que abre la flecha de Combinar y centrar | ambiguo: el producto no rotula ese menú; las opciones son Combinar y centrar, Combinar horizontalmente, Combinar celdas, Separar celdas; decidir con una persona delante del producto |
| `Minimum Value Options` | 1 | Encabezado 'Vertical Axis Minimum Value Options' del menú Eje (Minigráfico > Grupo) | REVISAR HUMANO: igual que 'Maximum Value Options' |
| `Misleading number formats` | 1 | Regla de comprobación de errores en Opciones de Excel, Fórmulas (agregada en 365) | la página es-es de detección de errores lista nueve reglas y no incluye esta; forma esperada 'Formatos de número engañosos'; confirmar en el producto |
| `More Functions...` | 1 | Última entrada de la lista desplegable Autosuma | REVISAR HUMANO: probable 'Más funciones...'; la página de Autosuma no imprime los elementos de la lista |
| `New Workbook` | 1 | opción de Guardar macro en (cuadro Grabar macro) | ninguna página es cita la opción; verificar en el producto |
| `No Cell Icon` | 1 | Opción de icono en la regla de Conjunto de iconos (formato condicional) | REVISAR HUMANO: probable 'Sin icono de celda'; ninguna página localizada lo imprime |
| `No Scaling` | 1 | Lista de ajuste de escala en Archivo > Imprimir (Configuración) | REVISAR HUMANO: las páginas (aparente traducción automática) dan 'Sin escala'/'Sin escalado'; el producto probablemente dice 'Sin ajuste de escala' |
| `not between` | 1 | Operador de la lista Datos en Validación de datos | REVISAR HUMANO: probable 'no está entre'; la página de validación no enumera los operadores |
| `not equal to` | 1 | Operador de la lista Datos en Validación de datos | REVISAR HUMANO: probable 'no es igual a'; la página de validación no enumera los operadores |
| `Number of days` | 1 | Cuadro del diálogo Agrupar de tabla dinámica cuando Por es Días | la página es-es de agrupar tablas dinámicas no trae la cadena literal; forma esperada 'Número de días' |
| `Numbers as text` | 1 | Rótulo abreviado de una tabla del curso para la regla del triángulo verde | ambiguo: no es cadena exacta de la interfaz; la regla completa es 'Números con formato de texto o precedidos por un apóstrofo' y la marca inteligente se espera 'Número almacenado como texto'; decidir con una persona |
| `Open Source` | 1 | Botón del cuadro Editar vínculos (Datos > Consultas y conexiones) | REVISAR HUMANO: probable 'Abrir origen'; la página de vínculos localizada es de Mac y con traducción automática ('Romper eslabones'); 'Cambiar origen' sí aparece |
| `Other File Types` | 1 | Archivo > Exportar > Cambiar el tipo de archivo, lista de tipos | la página es de Guardar como usa el encabezado "Otros formatos de archivo" en una tabla, pero no documenta la lista del backstage Exportar; sin evidencia del caption |
| `Page range` | 1 | sección de las Opciones al publicar PDF | sin página es que la cite; verificar en el producto |
| `Password (optional)` | 1 | cuadro del diálogo Proteger estructura y ventanas | la página solo dice 'La contraseña es opcional' en prosa; la etiqueta del cuadro no aparece citada |
| `Password to open` | 1 | cuadro de Opciones generales en Guardar como | el artículo es-es está traducido automáticamente y no cita la etiqueta; verificar en el producto |
| `PivotTable from table or range` | 1 | Titulo nuevo (M365) del cuadro que Office 2019 titula Crear tabla dinamica | Las paginas es siguen llamando al cuadro 'Crear tabla dinámica'; el titulo nuevo no aparece. Probable 'Tabla dinámica de tabla o rango' (sin verificar). |
| `PivotTables, PivotCharts, Cube Formulas, Slicers, and Timelines` | 1 | Categoría del Inspector de documento (Archivo > Información > Comprobar si hay problemas) | No se encontró la cadena literal del diálogo en ninguna página en español. La ayuda MS agrupa en prosa 'tablas dinámicas, gráficos dinámicos, segmentaciones, escalas de tiempo o fórmulas de cubo'; la traducción esperada sería 'Tablas dinámicas, gráficos dinámicos, fórmulas de cubo, segmentaciones de datos y escalas de tiempo', pero sin evidencia literal. Confirmar contra el diálogo abierto. |
| `Point` | 1 | Modo de entrada de fórmulas que muestra la barra de estado al insertar referencias con las flechas (w05) | sin página en español que nombre el modo; requiere verificación en el producto (candidato: Señalar); decisión humana |
| `Proofing not installed` | 1 | Archivo > Opciones > Idioma, estado junto a cada idioma de creación | la página documenta "Corrección instalada", "Corrección disponible" y "Corrección no disponible"; ninguna página escribe "no instalada"; verificar en el producto |
| `Protect Current Sheet` | 1 | opción de Archivo > Información > Proteger libro | ninguna página es cita el comando; verificar en el producto |
| `Protect Structure and Windows` | 1 | título del cuadro de diálogo de Revisar > Proteger libro | la página lo muestra mal traducido ('Proteger estructura y Windows'); verificar en el producto |
| `Quick Explore` | 1 | Icono de lupa junto a un punto de datos de un gráfico dinámico (modelo de datos) | sin página en español encontrada; el propio curso lo tiene marcado TO CONFIRM; candidato: Exploración rápida; decisión humana |
| `Read-only recommended` | 1 | casilla de Opciones generales en Guardar como | ninguna página es cita la casilla; el artículo relacionado está traducido automáticamente; verificar en el producto |
| `Report type` | 1 | Grupo de opciones del cuadro Resumen del escenario | la página solo trae prosa ("informe de resumen de escenario", "informe de tabla dinámica de escenario"), no el caption; verificar en el producto |
| `Restrict Access` | 1 | Archivo > Información > Proteger libro, opción de menú (IRM) | ninguna página es encontrada cita el menú completo; candidato: Restringir acceso; verificar en el producto |
| `Resume` | 1 | Botón del diálogo Comprobación de errores tras Modificar en la barra de fórmulas | la página es de detección de errores no lo menciona; candidato: Reanudar; verificar en el producto |
| `Right section` | 1 | Tercer cuadro del diálogo Encabezado/Pie de página personalizado | sin página es accesible que cite las tres secciones; candidato: Sección derecha; verificar en el producto |
| `Right section:` | 1 | Tercer cuadro del diálogo Encabezado/Pie de página personalizado | sin página es accesible que cite las tres secciones; candidato: Sección derecha:; verificar en el producto |
| `Save preview picture` | 1 | casilla de la pestaña Resumen en Propiedades avanzadas | el artículo de propiedades no cita la casilla; verificar en el producto |
| `Set as Default` | 1 | Botón del panel de idioma de Office 2019 (la redacción moderna es Set as Preferred) | la página actual documenta "Configurar como preferido" para la redacción moderna; el botón de 2019 no está documentado; verificar en la instalación del laboratorio (el curso ya lo marca TO CONFIRM) |
| `Set Hyperlink ScreenTip` | 1 | Cuadro de diálogo tras el botón Información en pantalla de Insertar hipervínculo | Los docs solo muestran el botón "Información en pantalla"; el título del cuadro no aparece. Sin fuente. |
| `sheet tabs` | 1 | Pestañas de hojas en la parte inferior de la ventana (término descriptivo, no caption) | ver la entrada "sheet tab": la fuente solo da la forma singular "pestaña Hoja"; decisión editorial |
| `Shift right, down, row, column` | 1 | Resumen compuesto (w02) de las cuatro opciones del diálogo Insertar celdas | término compuesto del curso, no un control; fragmentos con evidencia: "Desplazar celdas a la derecha", "Desplazar celdas hacia abajo", "Toda la fila", "Toda la columna"; redacción final a decisión humana |
| `Show Axis Field Buttons` | 1 | Elemento del menú Botones de campo (pestaña Análisis de gráfico dinámico, grupo Mostrar u ocultar) | Solo se encontró el nombre del API de VBA ('botones de campo del eje'); ninguna página en español cita el texto literal del menú. Traducción esperada 'Mostrar botones de campo de eje', sin evidencia. Confirmar contra la UI. |
| `Show Calculation Steps...` | 1 | Elemento del menú del botón de error de la celda | la página es de detección de errores no lo cita; candidato: Mostrar pasos de cálculo...; verificar en el producto |
| `Show Detail` | 1 | Botón del grupo Esquema (pestaña Datos) | la página es describe los botones +/- sin caption textual; candidato: Mostrar detalle; verificar en el producto |
| `Show error alert after invalid data is entered` | 1 | Casilla de la pestaña Mensaje de error (Alerta de error) de Validación de datos | La pestaña "Alerta de error" sí está documentada; el rótulo de la casilla no se imprime en las páginas es. Sin fuente. |
| `Show Legend Field Buttons` | 1 | Elemento del menú Botones de campo (pestaña Análisis de gráfico dinámico, grupo Mostrar u ocultar) | Ninguna página en español cita el texto literal del menú. Traducción esperada 'Mostrar botones de campo de leyenda', sin evidencia. Confirmar contra la UI. |
| `Show Report Filter Field Buttons` | 1 | Opcion del menu Botones de campo en PivotChart Analyze | No documentado en las paginas es revisadas. Probable 'Mostrar botones de campo de filtro de informe' (sin verificar). |
| `Show Value Field Buttons` | 1 | Opcion del menu Botones de campo en PivotChart Analyze | No documentado en las paginas es revisadas. Probable 'Mostrar botones de campo de valor' (sin verificar). |
| `Single` | 1 | Lista Subrayado de Formato de celdas > Fuente | sin página es que enumere las opciones de subrayado; candidatos: Sencillo/Simple; decisión humana con el producto |
| `Size & Properties` | 1 | pestaña del panel Formato de un elemento de gráfico | ninguna página es cita la pestaña; verificar en el producto |
| `Slicer Caption` | 1 | Cuadro de texto del encabezado en la pestana Segmentacion de datos | No aparece en las paginas es. Probable 'Título de segmentación de datos' (sin verificar). |
| `Slicer Caption:` | 1 | El mismo cuadro, rotulado con dos puntos | Igual que Slicer Caption: sin documentacion es. |
| `Slicer Settings` | 1 | Cuadro de dialogo de la pestana Segmentacion de datos (nombre, titulo, orden, elementos sin datos) | Solo Excel web esta documentado, como 'Configuración del segmentador'. El cuadro de Windows/2019 no aparece nombrado; probable 'Configuración de la segmentación de datos' (sin verificar). |
| `Slicer Settings...` | 1 | La entrada de cinta/menu contextual que abre ese cuadro | Igual que Slicer Settings: sin documentacion es para Windows. |
| `Source` | 1 | Columna/lista del cuadro de diálogo Editar vínculos | ninguna página es cita la columna; candidato: Origen; verificar en el producto |
| `Standard Width` | 1 | Diálogo que abre Formato > Ancho predeterminado | la página es-es deja "Standard column width" sin traducir; candidato: Ancho estándar; verificar en el producto |
| `Style 1` | 1 | Información en pantalla de las miniaturas de la galería Estilos de gráfico | los nombres de las miniaturas no están documentados; forma esperada 'Estilo 1' |
| `Style 2` | 1 | Información en pantalla de las miniaturas de la galería Estilos de gráfico | los nombres de las miniaturas no están documentados; forma esperada 'Estilo 2' |
| `Subfolders of this location are also trusted` | 1 | casilla del cuadro para agregar una ubicación de confianza | el artículo de ubicaciones de confianza no cita la casilla; verificar en el producto |
| `Sum, Count, Average, Max, Min, Product, Count Numbers, StdDev, StdDevp, Var, Varp` | 1 | Lista Usar función del cuadro de diálogo Subtotales | la página es-es de subtotales confirma 'Usar función' pero no enumera la lista; formas esperadas 'Suma, Cuenta, Promedio, Máx, Mín, Producto, Contar números, Desvest, Desvestp, Var, Varp'; confirmar en el producto |
| `Sum, Count, Average, Max, Min, Product, Count Numbers, StdDev, Var` | 1 | La misma lista Usar función de Subtotales, citada corta en el curso | sin enumeración en docs; ver la entrada de la lista completa |
| `Summary rows below detail` | 1 | Diálogo Configuración de Esquema (Datos > Esquema) | la única página da "Resumen filas debajo del detalle", sintaxis rota típica de traducción automática; sin fuente confiable no se registra |
| `Summary...` | 1 | Botón del Administrador de escenarios que abre Resumen del escenario | ninguna página es cita el botón; candidato: Resumen...; verificar en el producto |
| `Target value:` | 1 | Diálogo Estado de la búsqueda de objetivo | no documentado en las páginas es (la de Buscar objetivo es traducción automática); candidato: Valor objetivo:; verificar en el producto |
| `Task Pane Add-ins` | 1 | Elemento de la lista del Inspector de documento | la página es del Inspector no lista este elemento; candidato: Complementos del panel de tareas; verificar en el producto |
| `Template:` | 1 | Propiedades del documento, pestaña Resumen | la página es de propiedades no lista este cuadro; candidato: Plantilla:; verificar en el producto |
| `Text that Contains...` | 1 | Formato condicional > Resaltar reglas de celdas | las páginas es muestran el caption fusionado por traducción automática "Igual a texto que contiene"; el elemento real (previsiblemente "Texto que contiene...") debe verificarse en el producto |
| `to` | 1 | Palabra entre los dos cuadros de Páginas en Archivo > Imprimir (Páginas: __ a __) | sin evidencia en páginas es; candidato: a; verificar en el producto |
| `To` | 1 | Lista de idioma de destino del panel Traductor (Revisar > Traducir) | página es del Traductor no accesible (403/404); candidato: A; verificar en el producto |
| `To value:` | 1 | Segundo cuadro del diálogo Buscar objetivo | la página es solo trae el texto roto por traducción automática "valor Para"; la redacción clásica indexada era "Con el valor"; decidir con el producto |
| `Top, Bottom, Do Not Show` | 1 | Resumen compuesto (w14) del menú Subtotales del Diseño de tabla dinámica | término compuesto del curso; la página solo da la variante parcial "Mostrar subtotales en la parte superior de cada grupo"; los tres elementos del menú requieren verificación; decisión humana |
| `Top, Center, Bottom, Justify` | 1 | Resumen compuesto (w02) de la lista Vertical en Formato de celdas > Alineación | término compuesto del curso; ninguna página es enumera las opciones del cuadro de diálogo; candidatos: Superior, Centrar, Inferior, Justificar; decisión humana |
| `Treat consecutive delimiters as one` | 1 | Casilla del paso 2 del asistente heredado | La única página MS trae una versión MT agramatical ('Trate los delimitadores consecutivos como un solo'); las capturas docentes muestran 'Considerar separadores consecutivos como uno solo'; necesita captura |
| `Undo Flash Fill` | 1 | Entrada del botón de opciones que aparece tras aplicar Relleno rápido | sin página; forma esperada 'Deshacer relleno rápido'; la característica sí está documentada como 'Relleno rápido' |
| `Unsaved Files` | 1 | carpeta del sistema (%LocalAppData%\Microsoft\Office\UnsavedFiles) que abre Recuperar libros no guardados | es un nombre de carpeta del sistema de archivos ('UnsavedFiles'); los artículos no lo localizan, probablemente no se traduce |
| `Up/Down Bars` | 1 | Elemento del menú Agregar elemento de gráfico (gráficos de líneas) | sin página es fiable encontrada; candidato: Barras ascendentes y descendentes; decisión humana con el producto |
| `Update` | 1 | Columna de modo de actualización (A/M) del cuadro Editar vínculos | ninguna página es cita la columna; candidato: Actualizar; verificar en el producto |
| `Use Relative References` | 1 | Botón Programador > grupo Código (grabadora de macros) | la página es de la grabadora no menciona el botón; candidato: Usar referencias relativas; verificar en el producto |
| `Views:` | 1 | Lista del cuadro de diálogo Vistas personalizadas | página es de vistas personalizadas no accesible (404); candidato: Vistas:; verificar en el producto |
| `Waterfall, Funnel, Stock, Surface and Radar` | 1 | Botón de galería Insertar > Gráficos (Insert Waterfall, Funnel, Stock, Surface, or Radar Chart) | término compuesto; las páginas es de cascada y embudo muestran el nombre revuelto por traducción automática; tipos individuales documentados: cascada, embudo, cotizaciones, superficie, radial; decisión humana con el producto |
| `Workbook` | 1 | en la tabla del curso aparece como abreviatura del alcance de impresión ([Active Sheets], [Workbook], [Selection]) | ambiguo, necesita revisión humana; la opción documentada del menú de impresión es 'Imprimir todo el libro' |
| `Workbook File Types` | 1 | lista de Archivo > Exportar > Cambiar el tipo de archivo | ninguna página es cita la lista; verificar en el producto |

Al contar con grep, tres cosas inflan el número: la sintaxis de lista de YAML usa corchetes,
en el markdown los enlaces igual, y una referencia estructurada de tabla dentro de una fórmula
se escribe `=SUMA(Sales[Q1])`. El extractor que descuenta esos casos está en el historial de
la pasada; un conteo ingenuo da más de 3,000 donde el real anda en 2,100.
