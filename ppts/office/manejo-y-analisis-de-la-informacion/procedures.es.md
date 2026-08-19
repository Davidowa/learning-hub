# Rutas de examen · TIA501 · versión en español

## Antes de empezar: lee esto

Este archivo es el andamio de la versión en español de `procedures.en.md`. Ahí están documentados los 107 objetivos de la certificación Microsoft Office Specialist que cubre el curso: 59 del MO-200 Associate y 48 del MO-201 Expert. Aquí están los mismos 107, en el mismo orden y con la misma numeración, cada uno con su texto en inglés arriba y un hueco vacío abajo esperando la traducción. Los dos archivos se leen en paralelo, así que no cambies el orden ni la numeración de nada.

**Lo que se documenta es la ruta, no el resultado.** Este es el punto entero del documento y conviene entenderlo antes de traducir una sola línea. La certificación no califica cómo queda la hoja, califica cómo llegaste ahí. El ejemplo que dio el profesor: cambiar el color de letra y el relleno de una celda son dos clics en la cinta para cualquiera, y lo que el examen busca es otra cosa, que el alumno entre al menú extendido y aplique los dos formatos en una sola operación. La hoja se ve igual. La calificación no. Por eso cada objetivo trae la ruta larga primero y la ruta corta después, con el motivo por el que la corta no puntúa. Traduce las dos con el mismo cuidado: la ruta corta no es relleno, es lo que el alumno va a hacer en cuanto nadie lo esté calificando.

**Los nombres de la interfaz salen del glosario, no de tu criterio.** El glosario viene completo unas líneas más abajo y cada fila trae su fuente. Si una pestaña, un cuadro de diálogo, una casilla o una función está ahí, se escribe exactamente como dice el glosario. Si no está, no la inventes ni la traduzcas de oído: búscala en el Excel en español, y si tampoco aparece, pregunta antes de escribirla. Un nombre de menú mal traducido convierte una ruta en algo que el alumno no puede seguir, y es el tipo de error que nadie detecta hasta que alguien está sentado frente a la máquina.

Dos convenciones del glosario que hay que respetar. El español aparece con las mayúsculas de su fuente; los ejercicios del profesor escriben `Ajustar Texto` o `Estilos de Celda` donde el producto escribe `Ajustar texto` y `Estilos de celda`. En el documento en español usa siempre la forma del producto, en minúscula. Y los nombres de función son lo que se teclea en una celda: `INDICE` es lo que Excel acepta, `ÍNDICE` con acento es como se escribe en prosa. Deja el acento en la prosa y quítalo dentro de la fórmula.

**Lo marcado TO CONFIRM no se traduce todavía.** A lo largo del texto en inglés hay etiquetas **TO CONFIRM**: son captions que no se pudieron leer del producto y que pueden estar mal. Están todas juntas al final, en la sección "Still to confirm", junto con las 40 filas del glosario que dicen **NO SOURCE**. Nada de eso se traduce hasta que alguien lo verifique contra un Excel en español real. Si te topas con una etiqueta de esas mientras traduces, deja el término en inglés entre corchetes y sigue; ya se corregirá en una pasada aparte. Traducir un caption sin verificar es peor que dejarlo en inglés, porque el inglés se nota y una traducción inventada no.

## Cómo se llena este archivo

Cada objetivo tiene esta forma:

- el número y el título en inglés, que no cambian;
- **EN · texto fuente**, que es la ruta de examen tal como quedó en `procedures.en.md`. No lo edites: es la referencia contra la que se revisa tu traducción;
- **ES · ruta de examen**, un hueco entre las marcas `<!-- ES-INICIO ... -->` y `<!-- ES-FIN ... -->` que dice `_Pendiente._`. Ahí va tu texto, y ese `_Pendiente._` se borra.

Las marcas llevan el examen y el número (`MO200-2.2.6`, `MO201-4.2.3`) porque la numeración se repite entre los dos exámenes. No las toques: sirven para contar cuánto falta.

Traduce los pasos numerados como pasos numerados, uno por uno. Si un paso del inglés dice "sin cerrar el cuadro de diálogo", eso no es adorno, es la instrucción que hace que la operación cuente como una sola. Las secciones que en el inglés vienen después de la ruta (**Short route**, **Shortcut**, **How to check it**, **Where it lands**) se traducen en una segunda pasada, cuando las 107 rutas estén completas.

Enseguida vienen dos secciones que no son tuyas para traducir todavía, pero que hay que leer: "How to read a route", que explica las cinco partes que trae cada objetivo, y el glosario, que es la herramienta con la que se trabaja de aquí en adelante. Las dos conservan su título en inglés para que los dos archivos tengan los mismos encabezados y se puedan leer uno al lado del otro. En el glosario, la columna del centro es la que se copia al texto en español.

## How to read a route

Every objective carries the same five parts.

- **Exam route**: the graded sequence, click by click, naming the tab, the group, the dialog, the tab inside the dialog, the list and the check box literally. Numbered, no jumps.
- **Short route, not graded**: what an ordinary user does. Written out on purpose: the students will use it the moment nobody is grading them, and they need to know exactly where it stops earning marks.
- **Shortcut**: the keyboard route, when one exists. When there is none it says so, because "there is no shortcut" is itself worth knowing under time pressure.
- **How to check it**: what you look at afterwards to prove the graded route was the one taken.
- **Where it lands**: the syllabus week and session, from `COBERTURA.md`, with the exercise that practises it.

A note on repetition. Several objectives open the same dialog. The dialog is described in full the first time it appears and referred back to afterwards, so `Format Cells` is written out at Associate 2.2.6, `Page Setup` at Associate 1.3.1, `Function Arguments` at Associate 4.2.1, and so on. Follow the cross-reference rather than assuming the shorter entry is the whole route.

## Interface glossary

The English-to-Spanish table the Spanish version is built from. Every row is sourced. Rows that read **NO SOURCE** could not be traced to the professor's material or to Microsoft and must not be filled in by guessing; they are listed again under "Still to confirm".

Two conventions before anyone uses this table. Spanish is given in the capitalization its source uses: the professor's Exercise 1 title-cases some commands (`Ajustar Texto`, `Copiar Formato`, `Estilos de Celda`, `Aumentar Decimales`, `Eliminar Celdas`) where the product uses sentence case (`Ajustar texto`, `Copiar formato`, `Estilos de celda`). Normalize to sentence case in the Spanish document; both forms are recorded so the reason stays visible. And function names are what you type in a cell, not prose: `INDICE` is what Excel accepts, `ÍNDICE` with the accent is how COBERTURA.md writes it in running text. Keep the accent in prose, drop it inside a formula.

### Source key

| Key | Source |
|---|---|
| Ex N | The professor's exercise N, the `.docx` under `Excel/` |
| Ex 5-old | `Ejercicios anteriores/Ejercicio 5/Excel_Ejercicio5.docx`, the one legacy file written entirely in Spanish |
| Fold | The 25 exercise folder names |
| COB | `COBERTURA.md` |
| IMG | Read off the instructor's own screenshots of Excel running in Spanish, recovered from the `.docx` instruction files before the `Excel/` folder was retired |
| M1 | Microsoft, funciones de Excel por categoría |
| M2 | Microsoft, one Spanish page per function |
| M3 | Microsoft, métodos abreviados de teclado de Excel |
| M4 | Microsoft, settings in the Format Cells dialog box |
| M5 | Microsoft, formatos de número disponibles en Excel |
| M6 | Microsoft, create a custom number format |
| M7 | Microsoft, apply data validation to cells |
| M8 | Microsoft, more on data validation |
| M9 | Microsoft, usar formato condicional para resaltar información |
| M10 | Microsoft, filtrar por criterios avanzados |
| M11 | Microsoft, filtrar los datos de una tabla o un rango |
| M12 | Microsoft, insert subtotals in a list of data |
| M13 | Microsoft, outline (group) data in a worksheet |
| M14 | Microsoft, introduction to what-if analysis |
| M15 | Microsoft, create a PivotTable to analyze worksheet data |
| M16 | Microsoft, calculate values in a PivotTable |
| M17 | Microsoft, use slicers to filter data |
| M18 | Microsoft, create a PivotChart |
| M19 | Microsoft, protect a worksheet |
| M20 | Microsoft, protect a workbook |
| M21 | Microsoft, lock or unlock specific areas of a protected worksheet |
| M22 | Microsoft, advanced options |
| M23 | Microsoft, use the Name Manager in Excel |
| M24 | Microsoft, display the relationships between formulas and cells |
| M25 | Microsoft, ver una fórmula y su resultado con la ventana Inspección |
| M26 | Microsoft, detectar errores de fórmula en Excel |
| M27 | Microsoft, evaluate a nested formula one step at a time |
| M28 | Microsoft, display or hide formulas |
| M29 | Microsoft, change formula recalculation, iteration or precision |
| M30 | Microsoft, using Flash Fill in Excel |
| M31 | Microsoft, rellenar datos automáticamente en celdas |
| M32 | Microsoft, filter for unique values or remove duplicate values |
| M33 | Microsoft, sort data in a range or table |
| M34 | Microsoft, consolidate data in multiple worksheets |
| M35 | Microsoft, page setup |
| M36 | Microsoft, set or clear a print area |
| M37 | Microsoft, print rows with column headers on top of every page |
| M38 | Microsoft, save a workbook in another file format |
| M39 | Microsoft, freeze panes to lock rows and columns |
| M40 | Microsoft, overview of Excel tables |
| M41 | Microsoft, format an Excel table |
| M42 | Microsoft, total the data in an Excel table |
| M43 | Microsoft, tipos de gráficos disponibles en Office |
| M44 | Microsoft, create a chart from start to finish |
| M45 | Microsoft, mejorar la accesibilidad con el comprobador de accesibilidad |
| M46 | Microsoft, quitar datos ocultos e información personal |
| M47 | Microsoft, inicio rápido, crear una macro |
| M48 | Microsoft, mostrar la pestaña Programador |
| M49 | Microsoft, insertar comentarios y notas en Excel |
| M50 | Microsoft, personalizar la barra de herramientas de acceso rápido |
| M51 | Microsoft, crear o modificar un vínculo |
| M52 | Microsoft, move or copy cells, rows and columns |

### 1. Ribbon tabs

| English | Spanish | Source |
|---|---|---|
| File | Archivo | M3 |
| Home | Inicio | Ex 1, M3 |
| Insert | Insertar | Ex 1, M3 |
| Page Layout | Diseño de página | M3 |
| Formulas | Fórmulas | Ex 5, M3 |
| Data | Datos | M3 |
| Review | Revisar | M3 |
| View | Vista | Ex 3, M3 |
| Developer | Programador | COB, M48 |
| Table Design (contextual) | Diseño de tabla | M41, M42 |
| Chart Design (contextual) | Diseño de gráfico | M43, M44 |
| PivotTable Analyze (contextual) | Analizar tabla dinámica | M17 |
| PivotTable Tools (contextual, 2019) | Herramientas de tabla dinámica | M16 |
| Help | NO SOURCE |, |
| Draw | NO SOURCE |, |
| Sparkline (contextual) | NO SOURCE |, |
| Chart Tools (contextual, 2019) | NO SOURCE |, |

### 2. Ribbon groups the routes name

| English | Spanish | Source |
|---|---|---|
| Clipboard | Portapapeles | Ex 1 |
| Font | Fuente | Ex 1 |
| Alignment | Alineación | Ex 1 |
| Number | Número | Ex 1 |
| Styles | Estilos | Ex 1 |
| Cells | Celdas | Ex 1 |
| Editing | Edición | Ex 1 |
| Defined Names | Nombres definidos | Ex 5, COB |
| Formula Auditing | Auditoría de fórmulas | M24, M27 |
| Calculation | Cálculo | M29 |
| Sort & Filter | Ordenar y filtrar | M10 |
| Outline | Esquema | M12, M13 |
| Data Tools | NO SOURCE |, |
| Forecast | NO SOURCE |, |
| Page Setup | Configurar página | COB, M35 |
| Window | Ventana | Ex 2, Ex 4 |
| Workbook Views | NO SOURCE |, |
| Show | NO SOURCE |, |
| Tables | Tablas | Fold, M15 |
| Charts | Gráficos | M43 |
| Sparklines | Minigráficos | COB, M43 |
| Links | Vínculos | M51 |
| Comments | Comentarios | M49 |
| Protect | Proteger | M19, M20 |
| Table Style Options | Opciones de estilo de tabla | M41 |

### 3. Dialog boxes

**Format Cells**

| English | Spanish | Source |
|---|---|---|
| Format Cells (dialog) | Formato de celdas | COB, M4, M19 |
| Number (tab) | Número | M4 |
| Alignment (tab) | Alineación | M4 |
| Font (tab) | Fuente | M4 |
| Border (tab) | Borde | M4 |
| Fill (tab) | Relleno | M4 |
| Protection (tab) | Protección | M4, M19 |
| Locked (check box) | Bloqueada | M19 |
| Hidden (check box) | NO SOURCE |, |
| Category (list) | Categoría | M5 |
| Currency | Moneda | M5 |
| Accounting | Contabilidad | M5 |
| Percentage | Porcentaje | M5 |
| Custom | Personalizada | M5, M6 |
| Decimal places | Posiciones decimales | M5 |
| Custom number format | Formato de número personalizado | M6 |
| Wrap text | Ajustar texto / Ajustar Texto | M4 / Ex 1 |
| Merge cells | NO SOURCE |, |
| Orientation | NO SOURCE |, |
| Indent | NO SOURCE |, |

**Data Validation**

| English | Spanish | Source |
|---|---|---|
| Data Validation (dialog) | Validación de datos | COB, M7 |
| Settings (tab) | Configuración | M7 |
| Input Message (tab) | Mensaje de entrada | M7 |
| Error Alert (tab) | Mensaje de error | M7 |
| Allow (list) | Permitir | M7 |
| Source (box) | Origen | M8 |
| Drop-down list | Lista desplegable | M7 |
| Whole number | Número entero | M8 |
| Decimal | Decimal | M8 |
| Date | Fecha | M8 |
| Text length | Longitud del texto | M8 |
| Custom (formula) | Personalizada | M8 |
| Ignore blank | NO SOURCE |, |
| Circle Invalid Data | NO SOURCE |, |

**Conditional formatting and its rules manager**

| English | Spanish | Source |
|---|---|---|
| Conditional Formatting | Formato condicional | Fold, COB, M9 |
| Highlight Cells Rules | Resaltar reglas de celdas | M9 |
| Top/Bottom Rules | Reglas superiores e inferiores | M9 |
| Data Bars | Barras de datos | M9 |
| Color Scales | Escalas de color | M9 |
| Icon Sets | Conjuntos de iconos | M9 |
| New Rule | Nueva regla | COB, M9 |
| Clear Rules | Borrar reglas | M9 |
| Manage Rules | Administrar reglas | COB, M9 |
| Conditional Formatting Rules Manager (dialog) | Administrador de reglas de formato condicionales | M9 |
| New Formatting Rule (dialog) | Nueva regla de formato | M9 |
| Edit Formatting Rule (dialog) | Editar regla de formato | M9 |
| Select a Rule Type | Seleccionar un tipo de regla | M9 |
| Stop If True (check box) | Detener si es verdad | COB, M9 |
| Above Average | Por encima del promedio | M9 |
| Duplicate Values | Duplicar valores | M9 |
| Format (button) | Formato | M9 |
| Greater Than / Less Than | NO SOURCE |, |
| Top 10 Items / Bottom 10 % | NO SOURCE |, |

**Advanced Filter**

| English | Spanish | Source |
|---|---|---|
| Advanced Filter (dialog) | Filtro avanzado | Fold, M10 |
| Advanced (button) | Avanzadas | M10 |
| List range | Rango de la lista | M10 |
| Criteria range | Rango de criterios | M10 |
| Copy to | Copiar a | M10 |
| Copy to another location | Copiar a otra ubicación | M10, doc wording; the product is widely reported to read "Copiar a otro lugar". Confirm against Excel |
| Filter the list, in-place | Filtrar la lista, de forma local | M10, same caveat; the product is reported to read "Filtrar la lista sin moverla a otro lugar" |
| Unique records only | NO SOURCE |, |
| AutoFilter | Filtro automático / Autofiltro | M10 / M11 |

**Subtotal and outline**

| English | Spanish | Source |
|---|---|---|
| Subtotal (dialog and command) | Subtotal | M12 |
| Subtotals (as a topic) | Subtotales | Fold, M12 |
| At each change in | NO SOURCE |, |
| Use function | NO SOURCE |, |
| Add subtotal to | Agregar subtotal a | M12 |
| Replace current subtotals | Reemplazar subtotales actuales | M12 |
| Summary below data | Resumen debajo de los datos | M12 |
| Remove All | Quitar todos | M11 |
| Outline | Esquema | COB, M13 |
| Group | Agrupar | M13 |
| Ungroup | Desagrupar | M13 |

**What-if analysis**

| English | Spanish | Source |
|---|---|---|
| What-If Analysis | Análisis de hipótesis | Fold, COB, M14 |
| Goal Seek (dialog) | Buscar objetivo | COB, M14 |
| Scenario Manager (dialog) | Administrador de escenarios | COB, M14 |
| Scenario | Escenario | M14 |
| Data Table (dialog) | Tabla de datos | COB, M14 |
| Set cell | NO SOURCE |, |
| To value | NO SOURCE |, |
| By changing cell | NO SOURCE |, |
| Row input cell | NO SOURCE |, |
| Column input cell | NO SOURCE |, |

**PivotTable**

| English | Spanish | Source |
|---|---|---|
| PivotTable | Tabla dinámica | Fold, M15 |
| PivotChart | Gráfico dinámico | COB, M18, M43 |
| PivotTable Fields (pane) | NO SOURCE |, |
| Value Field Settings (dialog) | Configuración de campo de valor | M15 |
| Field Settings | Configuración de campo | M16 |
| Summarize Values By (tab) | Resumir valores por | M15 |
| Show Values As (tab) | Mostrar valores como | M15 |
| Calculated Field | Campo calculado | COB, M16 |
| Slicer | Segmentación de datos | COB, M17 |
| Timeline | Escala de tiempo | COB, M15, M18 |
| Refresh / Refresh All | Actualizar / Actualizar todo | M15 |
| Report Layout | NO SOURCE |, |
| Fields, Items & Sets | NO SOURCE |, |
| Grand Total | NO SOURCE |, |
| Drill down / Expand / Collapse | NO SOURCE |, |

**Protection**

| English | Spanish | Source |
|---|---|---|
| Protect Sheet (dialog) | Proteger hoja | M19 |
| Protect Workbook | Proteger libro | M20 |
| Allow all users of this worksheet to | Permitir a los usuarios de esta hoja de cálculo | M19 |
| Password to unprotect sheet | Contraseña para desproteger la hoja | M19 |
| Select locked cells | Seleccionar celdas bloqueadas | M19 |
| Select unlocked cells | Seleccionar celdas desbloqueadas | M19 |
| Allow Edit Ranges (dialog) | Permitir editar rangos | M21 |
| Allow users to edit ranges | Permitir que los usuarios editen rangos | M21 |
| Unlocked ranges | Rangos desbloqueados | M19, M21 |
| Mark as Final | Marcar como final | COB |
| Always Open Read-Only | NO SOURCE |, |

**Excel Options and the environment**

| English | Spanish | Source |
|---|---|---|
| Excel Options | Opciones de Excel | M29, M52 |
| Advanced (pane) | Avanzadas | M22 |
| Formulas (pane) | Fórmulas | M22 |
| Quick Access Toolbar | Barra de herramientas de acceso rápido | COB, M22, M50 |
| Customize the Quick Access Toolbar | Personalizar la barra de herramientas de acceso rápido | M50 |
| Fill handle | Controlador de relleno | M22, M31 |
| Calculation options | Opciones de cálculo | COB, M22, M29 |
| Customize Ribbon (pane) | NO SOURCE |, |
| Trust Center | NO SOURCE |, |
| Add-ins | NO SOURCE |, |

### 4. Commands and buttons the routes name

| English | Spanish | Source |
|---|---|---|
| Copy | Copiar | Ex 1 |
| Paste | Pegar | Ex 1 |
| Paste Special | Pegado especial | COB, M3, M52 |
| Paste Values | Pegar valores | M52 |
| Transpose | Transponer | M52 |
| Format Painter | Copiar formato / Copiar Formato | M9 / Ex 1 |
| Merge & Center | Combinar y centrar | Ex 1 |
| Wrap Text | Ajustar texto / Ajustar Texto | M4 / Ex 1 |
| Increase Decimal | Aumentar Decimales | Ex 1 |
| Borders | Bordes | Ex 1 |
| Cell Styles | Estilos de celda / Estilos de Celda | M11 / Ex 1 |
| Insert Sheet Columns | Insertar columnas de hoja | Ex 1 |
| Delete Cells | Eliminar Celdas | Ex 1 |
| Clear All | Borrar todo | Ex 1, M7 |
| Auto Fill | Autorrellenar | M31 |
| Fill Series | NO SOURCE |, |
| Flash Fill | Relleno rápido | COB, M22, M30 |
| Name Box | Cuadro de nombres | COB |
| Name Manager | Administrador de nombres | COB, M23 |
| Go To Special | Ir a Especial | COB, M9, M52 |
| Show Formulas | Mostrar fórmulas | M22, M28 |
| Trace Precedents | Rastrear precedentes | COB, M24 |
| Trace Dependents | Rastrear dependientes | COB, M24 |
| Remove Arrows | Quitar flechas | M24 |
| Watch Window | Ventana Inspección | COB ("Ventana de inspección"), M25 |
| Error Checking | Comprobación de errores | COB, M3, M26 |
| Evaluate Formula | Evaluar fórmula | COB, M26, M27 |
| Remove Duplicates | Quitar duplicados | Fold, M32 |
| Sort | Ordenar | Fold, M33 |
| Filter | Filtro | Fold, M10 |
| Text to Columns | Texto en columnas | M33 |
| Consolidate | Consolidar | COB, M34 |
| Freeze Panes | Inmovilizar paneles | COB, M39 |
| Split | Dividir | COB, M26 |
| Gridlines | Líneas de cuadrícula | COB ("cuadrícula"), M22 |
| Page Break Preview | Vista previa de salto de página | COB, M3 |
| Zoom | Zoom | M3, M22 |
| Print Area | Área de impresión | COB, M35, M36 |
| Print Titles | Imprimir títulos | M35, M37 |
| Rows to repeat at top | Repetir filas en extremo superior | M37 |
| Insert Hyperlink | Insertar hipervínculo | M3, M51 |
| Place in This Document | Lugar de este documento | M51 |
| Existing File or Web Page | Archivo o página web existente | M51 |
| E-mail Address | Dirección de correo electrónico | M51 |
| Sparkline | Minigráfico | COB, M43 |
| Format as Table | Dar formato como tabla | M11, M41 |
| Convert to Range | Convertir en rango | M33 |
| Total Row | Fila de totales | M12, M40 |
| Banded Rows | Filas con bandas | M40, M41 |
| Banded Columns | Columnas con bandas | M41 |
| Table Name | Nombre de la tabla | M3 |
| Structured references | Referencias estructuradas | COB, M40, M42 |
| Chart Elements | Elementos de gráfico | M22 |
| Chart Title | Título del gráfico | M44 |
| Axis Titles | Títulos de eje | M44 |
| Legend | Leyenda | M43 |
| Data Labels | Etiquetas de datos | M22, M43 |
| Quick Layout | Diseño rápido | M44 |
| Chart Styles | Estilos de gráfico | M44 |
| Switch Row/Column | Cambiar fila o columna | M44 |
| Chart sheet | Hoja de gráfico | M3 |
| Alt Text | Texto alternativo | M45 |
| Check Accessibility | Comprobador de accesibilidad | M45 |
| Check for Issues | Comprobar si hay problemas | M45, M46 |
| Document Inspector | Inspector de documento | COB, M46 |
| Compatibility Checker | Comprobador de compatibilidad | COB |
| New Comment | Nuevo comentario | M49 |
| New Note | Nueva nota | M49 |
| Record Macro | Grabar macro | M47 |
| Macro name | Nombre de la macro | M47 |
| Save As (other formats) | Guardar como | M38 |
| Select Data Source | NO SOURCE |, |
| New Window / Arrange All | NO SOURCE |, |
| Get & Transform / From Text-CSV | NO SOURCE |, |
| Series (dialog) | Serie | COB ("cuadro Series"), M22 |

### 5. Chart types

Exercise 17 builds every one of these, so this is the block the intern will use most.

| English | Spanish | Source |
|---|---|---|
| Column chart | Gráfico de columnas | M43 |
| Clustered column | Columnas agrupadas | M43 |
| Stacked column | Columna apilada | M43 |
| 100% stacked column | Columna 100 % apilada | M43 |
| Bar chart | Gráfico de barras | M43 |
| Line chart | Gráfico de líneas | M43 |
| Pie chart | Gráfico circular | M43 |
| Doughnut chart | Gráfico de anillos | M43 |
| Area chart | Gráfico de área | M43 |
| XY (Scatter) | Gráfico XY (dispersión) | M43 |
| Bubble | Gráfico de burbujas | M43 |
| Stock | Gráfico de cotizaciones | M43 |
| Surface | Gráfico de superficie | M43 |
| Radar | Gráficos radiales | M43 |
| Treemap | Gráfico de rectángulos | M43 |
| Sunburst | Gráfico de proyección solar | COB, M43 |
| Histogram | Gráficos de histograma | M43 |
| Pareto | Diagrama de pareto | M43 |
| Box & Whisker | Gráfico de cajas y bigotes | COB, M43 |
| Waterfall | Gráficos de cascada | COB, M43 |
| Funnel | Gráficos de embudo | COB, M43 |
| Combo | Gráficos combinados | COB, M43 |
| Map | Gráfico de mapa | COB, M43 |
| PivotChart | Gráficos dinámicos | M43 |

### 6. Functions named in MO-200 and MO-201

Where the professor's material names the same function, that citation comes first, because the cohort already writes it that way.

**Statistical and counting**

| English | Spanish | Source |
|---|---|---|
| SUM | SUMA | M1, M2, see the warning below |
| AVERAGE | PROMEDIO | Ex 6, M2 |
| MAX | MAX | Ex 6, M2 |
| MIN | MIN | Ex 6, M2 |
| COUNT | CONTAR | M2 |
| COUNTA | CONTARA | Ex 6, COB, M2 |
| COUNTBLANK | CONTAR.BLANCO | Ex 6, COB, M2 |
| LARGE | K.ESIMO.MAYOR | COB, M2 |
| SMALL | K.ESIMO.MENOR | COB, M2 |
| SUBTOTAL | SUBTOTALES | M2 |
| RANDBETWEEN | ALEATORIO.ENTRE | Ex 7, COB, M2 |
| RAND | ALEATORIO | M2 |

**Conditional aggregation**

| English | Spanish | Source |
|---|---|---|
| SUMIF | SUMAR.SI | Ex 9, Ex 11, M2 |
| COUNTIF | CONTAR.SI | Ex 6, Ex 9, Ex 5-old, M1 |
| AVERAGEIF | PROMEDIO.SI | Ex 9, Ex 11, M2 |
| SUMIFS | SUMAR.SI.CONJUNTO | Ex 11, M2 |
| COUNTIFS | CONTAR.SI.CONJUNTO | Ex 11, M2 |
| AVERAGEIFS | PROMEDIO.SI.CONJUNTO | Ex 11, M2 |
| MAXIFS | MAX.SI.CONJUNTO | COB, M2 |
| MINIFS | MIN.SI.CONJUNTO | COB, M2 |

**Logical**

| English | Spanish | Source |
|---|---|---|
| IF | SI | Fold, Ex 7, M2 |
| IFS | SI.CONJUNTO | Fold, Ex 12, Ex 16, M2 |
| SWITCH | CAMBIAR | M2 |
| AND | Y | Ex 10, Ex 5-old, M2 |
| OR | O | Ex 10, Ex 5-old, M2 |
| NOT | NO | Ex 5-old, COB, M2 |
| TRUE | VERDADERO | Ex 5-old |
| FALSE | FALSO | Ex 5-old |

**Lookup**

| English | Spanish | Source |
|---|---|---|
| VLOOKUP | BUSCARV | Fold (Ejercicio19_BuscarV), COB, M2, see the warning below |
| HLOOKUP | BUSCARH | Fold (Ejercicio21_BuscarH), M2 |
| INDEX | INDICE | COB (prose: ÍNDICE), M2 |
| MATCH | COINCIDIR | COB, M2 |
| XLOOKUP | BUSCARX | M2 |

**Text**

| English | Spanish | Source |
|---|---|---|
| LEFT | IZQUIERDA | Ex 13, COB, M2 |
| RIGHT | DERECHA | M2 |
| MID | EXTRAE | M2 |
| LEN | LARGO | M1 |
| UPPER | MAYUSC | Ex 13, COB, M2 |
| LOWER | MINUSC | M2 |
| PROPER | NOMPROPIO | Ex 13, COB, M2 |
| TEXT | TEXTO | Ex 13, COB, M2 |
| CONCAT | CONCAT | Ex 13, COB, M2 |
| TEXTJOIN | UNIRCADENAS | M2 |

**Date and time**

| English | Spanish | Source |
|---|---|---|
| NOW | AHORA | M2 |
| TODAY | HOY | M2 |
| DAY | DIA | Ex 13, COB, M2 |
| MONTH | MES | Ex 13, COB, M2 |
| YEAR | AÑO | Ex 13, COB, M2 |
| WEEKDAY | DIASEM | M2 |
| WORKDAY | DIA.LAB | M2 |

**Financial**

| English | Spanish | Source |
|---|---|---|
| PMT | PAGO | Ex 25, COB, M2 |
| NPER | NPER | M2 |

**Dynamic arrays, Microsoft 365 only.** All eight exist on the professor's machine and each returned without error. None of them exists in Office 2019.

| English | Spanish | Source |
|---|---|---|
| SEQUENCE | SECUENCIA | M2 |
| SORT | ORDENAR | M2 |
| SORTBY | ORDENARPOR | M2 |
| UNIQUE | UNICOS | M2 |
| FILTER | FILTRAR | M1, M2 |
| RANDARRAY | MATRIZALEAT | M2, not MATRIZALEATORIA, which is the guess people make |
| LET | LET | M2 |
| XLOOKUP | BUSCARX | M2 |

### 7. General vocabulary and error values

| English | Spanish | Source |
|---|---|---|
| Workbook | Libro | M20 |
| Worksheet | Hoja de cálculo | M19 |
| Cell | Celda | Ex 1 |
| Range | Rango | M10 |
| Row | Fila | Ex 1 |
| Column | Columna | Ex 1 |
| Sheet tab | NO SOURCE |, |
| Formula | Fórmula | Ex 5, M28 |
| Function | Función | Ex 5-old, M1 |
| Argument | NO SOURCE |, |
| Criteria | Criterio | Ex 5-old (CRITERIO), M10 |
| Wildcard | Comodín | Fold (Ex 10), Ex 5-old |
| Relative reference | Referencia relativa | COB |
| Absolute reference | Referencia absoluta | COB |
| Mixed reference | Referencia mixta | COB |
| Defined name | Nombre definido | COB |
| Dialog box launcher | NO SOURCE |, |
| Check box | Casilla | M19 |
| Ribbon | Cinta de opciones | M3 |
| #N/A | #N/D | M26 |
| #NAME? | #¿NOMBRE? | COB, M26 |
| #DIV/0! | #¡DIV/0! | Ex 9, M26 |
| #VALUE! | #¡VALOR! | Ex 9, M26 |
| #REF! | #¡REF! | COB, M26 |
| #NUM! | #¡NUM! | M26 |
| #NULL! | #¡NULO! | M26 |

### Read off the product, source key IMG

These 569 rows are different from every other row in this glossary: they were not taken from
a document, they were **read off screenshots of Excel actually running in Spanish**. The
instructor illustrated the exercise instructions with 92 captures of her own screen, the
pictures lived inside the `.docx` files, and they were harvested before that folder was
retired. For a control name that is a better source than Microsoft's Spanish support pages,
which are partly machine translated and which this glossary already records getting the
Format Cells time category wrong.

Rules applied when reading them. Only strings crisp enough to read were recorded, never a
guess at a blurred one. Nothing was translated or normalised; the capitalisation is the
product's. Strings that Excel itself had truncated with an ellipsis were dropped rather than
completed from memory, which is why `Automatic` is not here: every shot of it showed
`Automát.` cut off by the list box. Ribbon glyphs were dropped too, so `Bold` appears as
`Negrita` from the font style list and not as the `N` on the toolbar button.

Where two shots disagreed, the reading seen most often is given and the other is noted in the
third column. Most disagreements are context rather than error: `View` is `Vista` as a ribbon
tab and `Ver` as a menu verb, and both are correct where they were seen.

| English | Spanish | Also seen as |
|---|---|---|
| % normal size | % del tamaño normal |  |
| 100% | 100% |  |
| 20% - Accent1 | 20% - Énfasis1 |  |
| 20% - Accent2 | 20% - Énfasis2 |  |
| 20% - Accent3 | 20% - Énfasis3 |  |
| 20% - Accent4 | 20% - Énfasis4 |  |
| 20% - Accent5 | 20% - Énfasis5 |  |
| 20% - Accent6 | 20% - Énfasis6 |  |
| 3 Traffic Lights | 3 semáforos (sin marco) |  |
| 3D Map | Mapa 3D |  |
| 4 pages | 4 páginas |  |
| 40% - Accent1 | 40% - Énfasis1 |  |
| 40% - Accent2 | 40% - Énfasis2 |  |
| 40% - Accent3 | 40% - Énfasis3 |  |
| 40% - Accent4 | 40% - Énfasis4 |  |
| 40% - Accent5 | 40% - Énfasis5 |  |
| 40% - Accent6 | 40% - Énfasis6 |  |
| 5 pages | 5 páginas |  |
| 60% - Accent1 | 60% - Énfasis1 |  |
| 60% - Accent2 | 60% - Énfasis2 |  |
| 60% - Accent3 | 60% - Énfasis3 |  |
| 60% - Accent4 | 60% - Énfasis4 |  |
| 60% - Accent5 | 60% - Énfasis5 |  |
| 60% - Accent6 | 60% - Énfasis6 |  |
| 600 dpi | 600 ppp |  |
| A Date Occurring... | Una fecha... |  |
| Above Average... | Por encima del promedio... |  |
| Accent1 | Énfasis1 |  |
| Accent2 | Énfasis2 |  |
| Accent3 | Énfasis3 |  |
| Accent4 | Énfasis4 |  |
| Accent5 | Énfasis5 |  |
| Accent6 | Énfasis6 |  |
| Accessibility | Accesibilidad |  |
| Accessibility: Good to go | Accesibilidad: todo correcto |  |
| Accessibility: Investigate | Accesibilidad: es necesario investigar |  |
| Account | Cuenta |  |
| Action | Acción |  |
| Add subtotal to: | Agregar subtotal a: |  |
| Add-ins | Complementos |  |
| Additional Information | Información adicional |  |
| Address: | Dirección: |  |
| Adjust to: | Ajustar al: |  |
| Advanced | Avanzadas |  |
| Advanced Filter | Filtro avanzado |  |
| Align | Alinear |  |
| Alignment | Alineación |  |
| All Borders | Todos los bordes |  |
| Allow all users of this worksheet to: | Permitir a los usuarios de esta hoja de cálculo: |  |
| Allow Users to Edit Ranges | Permitir a usuarios modificar rangos |  |
| Analysis | Análisis |  |
| Analyze Data | Analizar datos |  |
| Arrange | Organizar |  |
| Arrange All | Organizar todo |  |
| At each change in: | Para cada cambio en: |  |
| Auto | Automático |  |
| Automate | Automatizar |  |
| AutoSave | Autoguardado |  |
| AutoSum | Autosuma |  |
| Average | Promedio |  |
| Average: | Promedio: |  |
| Background | Fondo |  |
| Bad | Incorrecto |  |
| Banded Columns | Columnas con bandas |  |
| Banded Rows | Filas con bandas |  |
| Before sheet: | Antes de la hoja: |  |
| Below Average... | Por debajo del promedio... |  |
| Between... | Entre... |  |
| Black and white | Blanco y negro |  |
| Blank workbook | Libro en blanco |  |
| Blue - White - Red Color Scale | Escala de colores azul, blanco y rojo |  |
| Bold Italic | Negrita Cursiva |  |
| Book1 | Libro1 |  |
| Book4 | Libro4 |  |
| Bookmark... | Marcador... |  |
| Border | Borde |  |
| Borders | Bordes |  |
| Bottom 10 Items... | 10 inferiores... |  |
| Bottom 10%... | 10% de valores inferiores... |  |
| Bottom Border | Borde inferior |  |
| Bottom Double Border | Borde doble inferior |  |
| Breaks | Saltos |  |
| Bring Forward | Traer adelante |  |
| Browsed Pages | Páginas consultadas |  |
| By changing cell: | Cambiando la celda: |  |
| Calculation | Cálculo |  |
| Cancel | Cancelar |  |
| Cell errors as: | Errores de celda como: |  |
| Cell Reference | Referencia de la celda |  |
| Cell Styles | Estilos de celda |  |
| Cell Value | Valor de la celda |  |
| Cells | Celdas |  |
| Center | Centrar |  |
| Changes | Cambios |  |
| Check Accessibility | Comprobar accesibilidad |  |
| Check Cell | Celda de co... |  |
| Choose the data that you want | Elija los datos para el grupo de minigráficos |  |
| Choose where you want the sparklines to be placed | Elija la ubicación donde se colocarán los minigráficos |  |
| Clear | Borrar |  |
| Clear All | Borrar todo |  |
| Clear Comments and Notes | Borrar comentarios y notas |  |
| Clear Contents | Borrar contenido |  |
| Clear Formats | Borrar formatos |  |
| Clear Hyperlinks | Borrar hipervínculos |  |
| Clear Print Area | Borrar área de impresión |  |
| Clear Rules | Borrar reglas |  |
| Clipboard | Portapapeles |  |
| Close | Cerrar |  |
| Collated | Intercaladas |  |
| Color Scales | Escalas de color |  |
| Color: | Color: |  |
| Colors | Colores |  |
| Column | Columna |  |
| Column input cell: | Celda de entrada (columna): |  |
| Column Width... | Ancho de columna... |  |
| Columns to repeat at left: | Repetir columnas a la izquierda: |  |
| Comma | Millares |  |
| Comma [0] | Millares [0] |  |
| Comment | Comentario |  |
| Comments | Comentarios |  |
| Comments: | Comentarios: |  |
| Conditional Formatting | Formato condicional |  |
| Context | Contexto |  |
| Copies: | Copias: |  |
| Copy | Copiar |  |
| Copy to another location | Copiar a otro lugar |  |
| Copy to: | Copiar a: |  |
| Count | Recuento |  |
| Count Numbers | Contar números |  |
| Count: | Recuento: |  |
| Create a copy | Crear una copia |  |
| Create from Selection | Crear desde la selección |  |
| Create New Document | Crear nuevo documento |  |
| Create Sparklines | Crear Minigráficos |  |
| Create Table | Crear tabla |  |
| Criteria range: | Rango de criterios: |  |
| Currency | Moneda |  |
| Currency [0] | Moneda [0] |  |
| Current Folder | Carpeta actual |  |
| Current value: | Valor actual: |  |
| Custom | Personalizada |  |
| Custom Format... | Formato personalizado... |  |
| Custom Views | Vistas personalizadas |  |
| Cut | Cortar |  |
| Dark | Oscuro |  |
| Data | Datos |  |
| Data and Model | Datos y modelo |  |
| Data Bars | Barras de datos |  |
| Data Range: | Rango de datos: |  |
| Data Table | Tabla de datos |  |
| Data Tools | Herramientas de datos |  |
| Define Name | Asignar nombre |  |
| Defined Names | Nombres definidos |  |
| Degrees | Grados |  |
| Delete | Eliminar |  |
| Delete columns | Eliminar columnas |  |
| Delete rows | Eliminar filas |  |
| Design | Diseño |  |
| Developer | Programador |  |
| Directional | Direccional |  |
| displayed | mostrado |  |
| Down, then over | Hacia abajo, luego hacia la derecha |  |
| Draft quality | Calidad de borrador |  |
| Draw | Dibujar |  |
| Draw Border | Dibujar borde |  |
| Draw Border Grid | Dibujar cuadrícula de borde |  |
| Draw Borders | Dibujar bordes |  |
| Duplicate Values... | Valores duplicados... |  |
| E-mail Address | Dirección de correo electrónico |  |
| E-mail address: | Dirección de correo electrónico: |  |
| Edit Hyperlink | Modificar hipervínculo |  |
| Edit Links | Editar vínculos |  |
| Edit the Rule Description: | Editar una descripción de regla: |  |
| Edit... | Modificar... |  |
| Editing | Edición |  |
| Effects | Efectos |  |
| Enter | Introducir |  |
| Entire column | Toda la columna |  |
| Entire row | Toda la fila |  |
| Equal To... | Es igual a... |  |
| Erase Border | Borrar borde |  |
| Errors | Errores |  |
| Existing Connections | Conexiones existentes |  |
| Existing File or Web Page | Archivo o página web existente |  |
| Explanatory Text | Texto explica... |  |
| Export | Exportar |  |
| Feedback | Comentarios |  |
| File | Archivo |  |
| Fill | Rellenar | Relleno |
| Filter | Filtro |  |
| Filter Button | Botón de filtro |  |
| Filter the list, in-place | Filtrar la lista sin moverla a otro lugar |  |
| Filters | Filtros |  |
| Financial | Financieras |  |
| Find & Select | Buscar y seleccionar |  |
| First Column | Primera columna |  |
| First page number: | Primer número de página: |  |
| First Point | Primer punto |  |
| Fit to: | Ajustar a: |  |
| Font | Fuente |  |
| Font style: | Estilo: |  |
| Font: | Fuente: |  |
| Fonts | Fuentes |  |
| Forecast | Previsión |  |
| Forecast Sheet | Previsión |  |
| Format | Formato |  |
| Format all cells based on their values | Aplicar formato a todas las celdas según sus valores |  |
| Format as Table | Dar formato como tabla |  |
| Format cells | Aplicar formato a celdas |  |
| Format Cells | Formato de celdas |  |
| Format cells that are LESS THAN: | Aplicar formato a las celdas que son MENORES QUE: |  |
| Format cells that contain the text: | Aplicar formato a las celdas que contengan el texto: |  |
| Format cells that rank in the TOP: | Aplicar formato a las celdas cuyo rango sea SUPERIOR: |  |
| Format Cells... | Formato de celdas... |  |
| Format columns | Aplicar formato a columnas |  |
| Format only cells that contain | Aplicar formato únicamente a las celdas que contengan |  |
| Format only cells with: | Dar formato únicamente a las celdas con: |  |
| Format only top or bottom ranked values | Aplicar formato únicamente a los valores con rango inferior o superior |  |
| Format only unique or duplicate values | Aplicar formato únicamente a los valores únicos o duplicados |  |
| Format only values that are above or below average | Aplicar formato únicamente a los valores que estén por encima o por debajo del promedio |  |
| Format Painter | Copiar formato |  |
| Format rows | Aplicar formato a filas |  |
| Format... | Formato... |  |
| Formula Bar | Barra de fórmulas |  |
| Formulas | Fórmulas |  |
| Freeze First Column | Inmovilizar primera columna |  |
| Freeze Panes | Inmovilizar | Inmovilizar paneles |
| Freeze Top Row | Inmovilizar fila superior |  |
| From Table/Range | Desde una tabla o rango |  |
| From Text/CSV | Desde el texto/CSV |  |
| From Web | Desde la web |  |
| Functions Translator | Traductor de funciones |  |
| General | General |  |
| Get & Transform Data | Obtener y transformar datos |  |
| Get Add-ins | Obtener complementos |  |
| Get Data | Obtener datos |  |
| Goal Seek | Buscar objetivo |  |
| Goal Seek Status | Estado de la búsqueda de objetivo |  |
| Gold, Accent4 | Oro, Énfasis4 |  |
| Good | Bueno |  |
| Good evening | Buenas noches |  |
| Good, Bad and Neutral | Bueno, malo y neutral |  |
| Gradient Fill | Relleno degradado |  |
| Grand Total | Total general |  |
| greater than or equal to | mayor o igual que |  |
| Greater Than... | Es mayor que... |  |
| Green Data Bar | Barra de datos verde |  |
| Green Fill with Dark Green Text | Relleno verde con texto verde oscuro |  |
| Gridlines | Líneas división | Líneas de división, Líneas de cuadrícula |
| Group | Agrupar |  |
| Header Row | Fila de encabezado |  |
| Header/Footer | Encabezado y pie de página |  |
| Heading 1 | Encabez... |  |
| Heading 2 | Título 2 |  |
| Heading 3 | Título 3 |  |
| Heading 4 | Encabezado 4 |  |
| Headings | Encabezados |  |
| Height: | Alto: |  |
| Height: 21.00 | Alto: 21.00 (28 píxeles) |  |
| Help | Ayuda |  |
| Hidden | Oculta |  |
| Hide | Ocultar |  |
| High Point | Punto alto |  |
| Highlight Cells Rules | Reglas para resaltar celdas |  |
| History | Historial |  |
| Home | Inicio |  |
| Horizontal: | Horizontal: |  |
| Icon Sets | Conjuntos de iconos |  |
| Illustrations | Ilustraciones |  |
| Indent: | Sangría: |  |
| Info | Información |  |
| Input | Entrada |  |
| Insert | Insertar |  |
| Insert Cells... | Insertar celdas... |  |
| Insert columns | Insertar columnas |  |
| Insert Function | Insertar función |  |
| Insert Hyperlink | Insertar hipervínculo |  |
| Insert hyperlinks | Insertar hipervínculos |  |
| Insert rows | Insertar filas |  |
| Insert Sheet | Insertar hoja |  |
| Insert Sheet Rows | Insertar filas de hoja |  |
| Insert... | Insertar... |  |
| Insights | Datos |  |
| Inspection Results | Resultados de la inspección |  |
| Justify distributed | Distribuido justificado |  |
| Landscape | Horizontal |  |
| Language | Idioma |  |
| Last Column | Última columna |  |
| Last Point | Último punto |  |
| Learn more | Más información |  |
| Left Border | Borde izquierdo |  |
| Less Than | Es menor que |  |
| Less Than... | Es menor que... |  |
| Letter | Carta |  |
| Light | Claro |  |
| Light Red Fill | Relleno rojo claro |  |
| Light Red Fill with Dark Red Text | Relleno rojo claro con texto rojo oscuro |  |
| Line | Línea |  |
| Line Color | Color de línea |  |
| Line Style | Estilo de línea |  |
| Link | Vínculo |  |
| Link to: | Vincular a: |  |
| Linked Cell | Celda vincul... |  |
| List range: | Rango de la lista: |  |
| Location Range: | Ubicación: |  |
| Locked | Bloqueada |  |
| Logical | Lógicas |  |
| Look in: | Buscar en: |  |
| Low Point | Punto bajo |  |
| Macros | Macros |  |
| Manage Rules... | Administrar reglas... |  |
| Maps | Mapas |  |
| Margins | Márgenes |  |
| Markers | Marcadores |  |
| Max: | Máx: |  |
| Medium | Medio |  |
| Merge & Center | Combinar y centrar |  |
| Merge cells | Combinar celdas |  |
| Merge Styles... | Combinar estilos... |  |
| Min: | Mín: |  |
| More | Más |  |
| More Colors... | Más colores... |  |
| More Functions... | Más funciones... |  |
| More Rules... | Más reglas... |  |
| Move or Copy | Mover o copiar |  |
| Move or Copy... | Mover o copiar... |  |
| Move selected sheets | Mover hojas seleccionadas |  |
| My Add-ins | Mis complementos |  |
| Name | Nombre |  |
| Name Manager | Administrador de nombres |  |
| Negative Points | Puntos negativos |  |
| Neutral | Neutral |  |
| New | Nuevo | Nueva |
| New Cell Style... | Nuevo estilo de celda... |  |
| New Comment | Nuevo comentario |  |
| New PivotTable Style... | Nuevo estilo de tabla dinámica... |  |
| New Rule... | Nueva regla... |  |
| New Table Style... | Nuevo estilo de tabla... |  |
| New Window | Nueva ventana |  |
| New... | Nuevo... |  |
| Next | Siguiente |  |
| No Border | Sin borde |  |
| No Color | Sin color |  |
| No Staples | Sin grapas |  |
| None | Ninguno |  |
| Normal | Normal |  |
| Normal font | Fuente normal |  |
| Note | Notas |  |
| Number | Número |  |
| Number Format | Formato de número |  |
| OK | Aceptar | ACEPTAR |
| Open | Abrir |  |
| Options | Opciones |  |
| Options... | Opciones... |  |
| Or select a place in this document: | O selecciona un lugar de este documento: |  |
| Orientation | Orientación |  |
| Outline | Esquema |  |
| Output | Salida |  |
| Outside Borders | Bordes externos |  |
| Over, then down | Hacia la derecha, luego hacia abajo |  |
| Page | Página |  |
| Page break between groups | Salto de página entre grupos |  |
| Page Layout | Diseño de página | Disposición de página |
| Page order | Orden de las páginas |  |
| Page Setup | Configurar página |  |
| page(s) wide by | páginas de ancho por |  |
| Pages: | Páginas: |  |
| Paper size: | Tamaño del papel: |  |
| Password to unprotect sheet: | Contraseña para desproteger la hoja: |  |
| Paste | Pegar |  |
| Paste Options: | Opciones de pegado: |  |
| Paste Special... | Pegado especial... |  |
| Pause | Pausa |  |
| Percent | Porcentaje |  |
| Pinned | Anclado |  |
| Place in This Document | Lugar de este documento |  |
| Portrait | Vertical |  |
| Portrait Orientation | Orientación vertical |  |
| Power Pivot | Power Pivot |  |
| Preview | Vista previa |  |
| Preview: | Vista previa: |  |
| Previous | Anterior |  |
| Print | Imprimir |  |
| Print Active Sheets | Imprimir hojas activas |  |
| Print Area | Área de impresión |  |
| Print area: | Área de impresión: |  |
| Print One Sided | Imprimir a una cara |  |
| Print Preview | Vista preliminar |  |
| Print quality: | Calidad de impresión: |  |
| Print Titles | Imprimir títulos |  |
| Print titles | Imprimir títulos |  |
| Print... | Imprimir... |  |
| Printer | Impresora |  |
| Printer Properties | Propiedades de impresora |  |
| Proofing | Revisión |  |
| Properties | Propiedades |  |
| Protect and Share Workbook | Proteger y compartir libro |  |
| Protect Sheet... | Proteger hoja... |  |
| Protect worksheet and contents of locked cells | Proteger hoja y contenido de celdas bloqueadas |  |
| Protection | Proteger |  |
| Publish | Publicar |  |
| Queries & Connections | Consultas y conexiones |  |
| Ratings | Valoración |  |
| Ready | Listo |  |
| Reapply | Volver a aplicar |  |
| Recent | Recientes |  |
| Recent Files | Archivos recientes |  |
| Recent Sources | Fuentes recientes |  |
| Recently Used | Usado recientemente |  |
| Recently used e-mail addresses: | Direcciones de correo utilizadas recientemente: |  |
| Recommended Charts | Gráficos recomendados |  |
| Recommended PivotTables | Tablas dinámicas recomendadas |  |
| Red Border | Borde rojo |  |
| Red Text | Texto rojo |  |
| Reference | Referencia |  |
| Refers To | Se refiere a |  |
| Refers to: | Se refiere a: |  |
| Refresh All | Actualizar todo |  |
| Regular | Normal |  |
| Remove All | Quitar todos |  |
| Remove Hyperlinks | Quitar hipervínculos |  |
| Remove Link | Quitar vínculo |  |
| Rename | Cambiar nombre |  |
| Replace current subtotals | Reemplazar subtotales actuales |  |
| Reset Window Position | Restablecer posición de la ventana |  |
| Review | Revisar |  |
| Right Border | Borde derecho |  |
| Right-to-left | De derecha a izquierda |  |
| Rotate | Girar |  |
| Row and column headings | Encabezados de filas y columnas |  |
| Row Height | Alto de fila |  |
| Row Height... | Alto de fila... |  |
| Row height: | Alto de fila: |  |
| Row input cell: | Celda de entrada (fila): |  |
| Rows to repeat at top: | Repetir filas en extremo superior: |  |
| Ruler | Regla |  |
| Save | Guardar |  |
| Save As | Guardar como |  |
| Scale to Fit | Ajustar área de impresión |  |
| Scale: | Escala: |  |
| Scaling | Ajuste de escala |  |
| Scope | Ámbito |  |
| ScreenTip... | Info. en pantalla... |  |
| Search | Buscar |  |
| Search menus | Buscar en los menús |  |
| Select a Rule Type: | Seleccionar un tipo de regla: |  |
| Select All Sheets | Seleccionar todas las hojas |  |
| Select locked cells | Seleccionar celdas bloqueadas |  |
| Select unlocked cells | Seleccionar celdas desbloqueadas |  |
| Selection Pane | Panel de selección |  |
| Send Backward | Enviar atrás |  |
| Sensitivity | Confidencialidad |  |
| Set cell: | Definir la celda: |  |
| Set Print Area | Establecer área de impresión |  |
| Settings | Configuración |  |
| Shapes | Formas |  |
| Share | Compartir |  |
| Share Workbook | Compartir libro |  |
| Shared with Me | Compartidos conmigo |  |
| Sheet | Hoja |  |
| Sheet Options | Opciones de la hoja |  |
| Sheet1 | Hoja1 |  |
| Sheet2 | Hoja2 |  |
| Sheet3 | Hoja3 |  |
| Shift cells left | Desplazar las celdas hacia la izquierda |  |
| Shift cells up | Desplazar las celdas hacia arriba |  |
| Show | Mostrar |  |
| Shrink to fit | Reducir hasta ajustar |  |
| Size | Tamaño |  |
| Size: | Tamaño: |  |
| Smart Lookup | Búsqueda inteligente |  |
| Sort | Ordenar |  |
| Sort & Filter | Ordenar y filtrar |  |
| Sort A to Z | Ordenar de A a Z |  |
| Sort by Color | Ordenar por color |  |
| Sort Z to A | Ordenar de Z a A |  |
| Sparkline Tools | Herramientas para minigráfico |  |
| Spelling | Ortografía |  |
| Split | Dividir |  |
| Standard Colors | Colores estándar |  |
| StdDev | Desvest |  |
| Step | Paso a paso |  |
| Steps To Fix: | Pasos de corrección: |  |
| Strikethrough | Tachado |  |
| Style | Estilo |  |
| Styles | Estilos |  |
| Subject: | Asunto: |  |
| Subscript | Subíndice |  |
| Subtotal | Subtotal | Subtotales |
| Sum | Suma |  |
| Sum: | Suma: |  |
| Summary below data | Resumen debajo de los datos |  |
| Superscript | Superíndice |  |
| Switch Windows | Cambiar ventanas |  |
| Symbols | Símbolos |  |
| Synchronous Scrolling | Desplazamiento sincrónico |  |
| Tab Color | Color de pestaña |  |
| TABLE | TABLA |  |
| Table | Tabla |  |
| Table Style Options | Opciones de estilo de tabla |  |
| Table Tools | Herramientas de tabla |  |
| tall | de alto |  |
| Target value: | Valor del objetivo: |  |
| Tell me more | Más información |  |
| Tell me what you want to do | ¿Qué desea hacer? |  |
| Text | Texto |  |
| Text alignment | Alineación del texto |  |
| Text control | Control del texto |  |
| Text direction: | Dirección del texto: |  |
| Text Filters | Filtros de texto |  |
| Text That Contains | Texto que contiene |  |
| Text that Contains... | Texto que contiene... |  |
| Text to Columns | Texto en columnas |  |
| Text to display: | Texto: |  |
| Theme Colors | Colores del tema |  |
| Themed Cell Styles | Estilos de celda temáticos |  |
| Themes | Temas |  |
| Thesaurus | Sinónimos |  |
| Thick Bottom Border | Borde inferior grueso |  |
| Thick Outside Borders | Borde exterior grueso |  |
| Title | Título |  |
| Titles and Headings | Títulos y encabezados |  |
| To book: | Al libro: |  |
| To value: | Con el valor: |  |
| Top 10 Items | 10 superiores |  |
| Top 10 Items... | 10 superiores... |  |
| Top 10%... | 10% de valores superiores... |  |
| Top and Bottom Border | Borde superior e inferior |  |
| Top and Double Bottom Border | Borde superior e inferior doble |  |
| Top and Thick Bottom Border | Borde superior e inferior grueso |  |
| Top Border | Borde superior |  |
| Top/Bottom Rules | Reglas superiores e inferiores |  |
| Total | Total |  |
| Total Row | Fila de totales |  |
| Tours | Paseos |  |
| Track Changes | Control de cambios |  |
| Translate | Traducir |  |
| Translator | Traductor |  |
| Type | Tipo |  |
| Type the cell reference: | Escriba la referencia de celda: |  |
| Underline: | Subrayado: |  |
| Unfreeze Panes | Movilizar paneles |  |
| Ungroup | Desagrupar |  |
| Unhide | Mostrar |  |
| Unhide... | Mostrar... |  |
| Unique records only | solo registros únicos |  |
| Use function: | Usar función: |  |
| Use in Formula | Utilizar en la fórmula |  |
| Value | Valor |  |
| Var | Var |  |
| Vertical: | Vertical: |  |
| View | Vista | Ver |
| View Code | Ver código |  |
| View Side by Side | Ver en paralelo |  |
| Warning Text | Texto de adv... |  |
| What-If Analysis | Análisis de hipótesis |  |
| Where is the data for your table? | ¿Dónde están los datos de la tabla? |  |
| Why Fix? | ¿Motivo de la corrección? |  |
| Width: | Ancho: |  |
| Win/Loss | Pérdidas y ganancias |  |
| Window | Ventana |  |
| with | con |  |
| Workbook | Libro |  |
| Workbook Views | Vistas de libro |  |
| Wrap Text | Ajustar texto |  |
| Wrap text | Ajustar texto |  |
| Yellow Fill with Dark Yellow Text | Relleno amarillo con texto amarillo oscuro |  |
| Zoom | Zoom |  |
| Zoom to Selection | Ampliar selección |  |

**Read but not used.** 15 strings were harvested and deliberately left out of the table:

- `Automatic`, seen as `Automát.`, truncated by Excel in the shot.
- `Bold`, seen as `N`, button glyph, not the string.
- `found a solution.`, seen as `ha encontrado una solución.`, truncated by Excel in the shot.
- `Italic`, seen as `K`, button glyph, not the string.
- `Keep rows and columns visible while the rest of the worksheet scrolls (based on current selection).`, seen as `Mantiene visibles las filas y columnas mientras el resto de la hoja de cálculo se desplaza (a partir de la selección actual).`, truncated by Excel in the shot.
- `Keep the first column visible while scrolling through the rest of the worksheet.`, seen as `Mantiene visible la primera columna a medida que se desplaza por el resto de la hoja de cálculo.`, truncated by Excel in the shot.
- `Keep the top row visible while scrolling through the rest of the worksheet.`, seen as `Mantiene visible la fila superior a medida que se desplaza por el resto de la hoja de cálculo.`, truncated by Excel in the shot.
- `Make it more inclusive.`, seen as `Hágalo lo más inclusivo posible.`, truncated by Excel in the shot.
- `Max`, seen as `Máx.`, truncated by Excel in the shot.
- `Min`, seen as `Mín.`, truncated by Excel in the shot.
- `My table has headers`, seen as `La tabla tiene encabezados.`, truncated by Excel in the shot.
- `Page Break Preview`, seen as `Ver salt. Pág.`, truncated by Excel in the shot.
- `Quickly change the visual style of the table.`, seen as `Cambia rápidamente el estilo visual de la tabla.`, truncated by Excel in the shot.
- `This is a TrueType font. The same font will be used on both your printer and your screen.`, seen as `Esta es una fuente TrueType. Se usará la misma fuente tanto en la impresora como en la pantalla.`, truncated by Excel in the shot.
- `Use a formula to determine which cells to format`, seen as `Utilice una fórmula que determine las celdas para aplicar formato.`, truncated by Excel in the shot.

### Three warnings about the glossary

**Exercise 6 carries a wrong function name.** Its instruction sheet writes `SUM (SUMAR)`. The Spanish function is `SUMA`; `SUMAR` does not exist, and a student who types it gets `#¿NOMBRE?`. The professor's material outranks Microsoft everywhere else in this table, but not here. Worth telling him so the exercise gets fixed.

**Microsoft's own Spanish page for VLOOKUP titles it `CONSULTAV`.** The body of that same page writes `=BUSCARV(` twelve times, the professor's folders are `Ejercicio19_BuscarV` and `Ejercicio21_BuscarH`, and `BUSCARV` is what Excel accepts. `CONSULTAV` is a documentation artifact. Ignore it.

**Several of Microsoft's Spanish support pages are machine-translated and it shows.** The Advanced Filter page renders the two option buttons as "Filtrar la lista, de forma local" and "Copiar a otra ubicación", where the shipping product is widely reported to read "Filtrar la lista sin moverla a otro lugar" and "Copiar a otro lugar". Those two rows are flagged in place. Any other row sourced to a single Microsoft page and naming a button rather than a feature deserves a look at the real product before it ships.

## MO-200 Associate · Domain 1, Manage worksheets and workbooks

### 1.1.1 Import data from .txt files

**EN · texto fuente, no editar**

The exam grades the wizard, not the result. A tab-delimited file opens on a double-click and looks fine, and that earns nothing, because the wizard is where the delimiter, the file origin and the per-column data type get chosen.

**Exam route**

1. Confirm the legacy wizard is available. Go to the **File** tab, click **Options**, and select the **Data** pane on the left.
2. Under the section for legacy data import wizards, tick the **From Text (Legacy)** check box. Click **OK**. (Section heading wording: **TO CONFIRM**. What is confirmed is that on this machine the setting is off, `HKCU\Software\Microsoft\Office\16.0\Excel\Options` carries no legacy-wizard value, and the value is only written once the box is ticked.)
3. Click the cell where the imported block is to start.
4. Go to the **Data** tab, **Get & Transform Data** group, and click **Get Data**.
5. Point at **Legacy Wizards** and click **From Text (Legacy)**.
6. In the **Import Text File** browser, select the .txt file and click **Import**.
7. **Text Import Wizard, Step 1 of 3.** Under **Original data type**, choose **Delimited** or **Fixed width**. Set **Start import at row:** to the first row you actually want. Open the **File origin:** list and pick the encoding, normally `65001 : Unicode (UTF-8)` or `Windows (ANSI)`. Tick **My data has headers** if row one holds field names. Click **Next**.
8. **Step 2 of 3.** Under **Delimiters**, tick every delimiter the file uses: **Tab**, **Semicolon**, **Comma**, **Space**, or **Other:** with the character typed in the box. Tick **Treat consecutive delimiters as one** only if the file pads with repeated separators. Set **Text qualifier:** to `"` when fields are quoted. Watch the **Data preview** pane split into columns before you continue. Click **Next**.
9. **Step 3 of 3.** Click a column in the **Data preview**, then set its **Column data format**: **General**, **Text**, **Date** with the order list beside it, or **Do not import column (skip)**. Repeat for every column the task names. For decimal or thousands separators that do not match the machine locale, click **Advanced...** and set them in the **Advanced Text Import Settings** dialog. Click **Finish**.
10. In the **Import Data** dialog, under **Where do you want to put the data?**, choose **Existing worksheet:** and confirm the reference, or **New worksheet**. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.1.1 -->

El examen califica el asistente, no el resultado. Un archivo delimitado por tabulaciones se abre con doble clic y se ve bien, y eso no da puntos, porque el asistente es donde se eligen el delimitador, el origen del archivo y el tipo de datos de cada columna.

**Ruta de examen**

1. Confirme que el asistente heredado está disponible. Vaya a la pestaña **Archivo**, haga clic en **Opciones** y seleccione el panel **Datos** de la izquierda.
2. En la sección de los asistentes heredados para importar datos, marque la casilla **[From Text (Legacy)]**. Haga clic en **Aceptar**. (Redacción del encabezado de la sección: **TO CONFIRM**. Lo que sí está confirmado es que en esta máquina la opción está desactivada, que `HKCU\Software\Microsoft\Office\16.0\Excel\Options` no guarda ningún valor de asistente heredado y que ese valor solo se escribe cuando se marca la casilla.)
3. Haga clic en la celda donde debe empezar el bloque importado.
4. Vaya a la pestaña **Datos**, grupo **Obtener y transformar datos**, y haga clic en **Obtener datos**.
5. Señale **[Legacy Wizards]** y haga clic en **[From Text (Legacy)]**.
6. En el explorador **[Import Text File]**, seleccione el archivo .txt y haga clic en **[Import]**.
7. **[Text Import Wizard, Step 1 of 3]**. En **[Original data type]**, elija **[Delimited]** o **[Fixed width]**. Ponga en **[Start import at row:]** la primera fila que de verdad le interesa. Abra la lista **[File origin:]** y elija la codificación, normalmente `65001 : Unicode (UTF-8)` o `Windows (ANSI)`. Marque **[My data has headers]** si la primera fila trae los nombres de los campos. Haga clic en **Siguiente**.
8. **[Step 2 of 3]**. En **[Delimiters]**, marque todos los delimitadores que use el archivo: **[Tab]**, **[Semicolon]**, **[Comma]**, **[Space]**, o **[Other:]** con el carácter escrito en el cuadro. Marque **[Treat consecutive delimiters as one]** solo si el archivo rellena con separadores repetidos. Ponga `"` en **[Text qualifier:]** cuando los campos vengan entre comillas. Vea cómo el panel **[Data preview]** se separa en columnas antes de continuar. Haga clic en **Siguiente**.
9. **[Step 3 of 3]**. Haga clic en una columna del **[Data preview]** y defina su **[Column data format]**: **General**, **Texto**, **Fecha** con la lista de orden que tiene al lado, o **[Do not import column (skip)]**. Repita con cada columna que mencione la tarea. Si los separadores de decimales o de miles no coinciden con la configuración regional de la máquina, haga clic en **[Advanced...]** y defínalos en el cuadro de diálogo **[Advanced Text Import Settings]**. Haga clic en **[Finish]**.
10. En el cuadro de diálogo **[Import Data]**, en **[Where do you want to put the data?]**, elija **[Existing worksheet:]** y confirme la referencia, o **[New worksheet]**. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.1.1 -->

---

### 1.1.2 Import data from .csv files

**EN · texto fuente, no editar**

**Exam route**

1. Click the cell where the data is to land.
2. Go to the **Data** tab, **Get & Transform Data** group, and click **From Text/CSV**.
3. In the browser dialog, select the .csv file and click **Import**.
4. The preview window opens with the file name as its title. Open the **File Origin** list and set the encoding. `65001: Unicode (UTF-8)` is the one that repairs accented characters arriving as mojibake.
5. Open the **Delimiter** list and set the separator: **Comma**, **Semicolon**, **Tab**, **Space**, **Colon**, or **Custom**. Watch the preview grid re-split before moving on.
6. Open the **Data Type Detection** list and choose **Based on first 200 rows**, **Based on entire dataset**, or **Do not detect data types**. Choose **Do not detect data types** whenever the task mentions codes, IDs or postal codes.
7. Click **Transform Data** if the task asks for any cleaning, which opens the Power Query Editor. Otherwise click the arrow beside **Load** and choose **Load To...**.
8. In the **Import Data** dialog, choose how to view the data (**Table**, **PivotTable Report**, **PivotChart**, or **Only Create Connection**) then, under **Where do you want to put the data?**, choose **Existing worksheet:** with the reference, or **New worksheet**. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.1.2 -->

**Ruta de examen**

1. Haga clic en la celda donde van a caer los datos.
2. Vaya a la pestaña **Datos**, grupo **Obtener y transformar datos**, y haga clic en **Desde el texto/CSV**.
3. En el cuadro de diálogo del explorador, seleccione el archivo .csv y haga clic en **[Import]**.
4. La ventana de vista previa se abre con el nombre del archivo como título. Abra la lista **[File Origin]** y defina la codificación. `65001: Unicode (UTF-8)` es la que arregla los caracteres acentuados que llegan convertidos en basura.
5. Abra la lista **[Delimiter]** y defina el separador: **[Comma]**, **[Semicolon]**, **[Tab]**, **[Space]**, **[Colon]** o **Personalizada**. Vea cómo la cuadrícula de vista previa se vuelve a separar antes de seguir.
6. Abra la lista **[Data Type Detection]** y elija **[Based on first 200 rows]**, **[Based on entire dataset]** o **[Do not detect data types]**. Elija **[Do not detect data types]** siempre que la tarea hable de códigos, identificadores o códigos postales.
7. Haga clic en **[Transform Data]** si la tarea pide alguna limpieza, lo que abre el editor de Power Query. Si no, haga clic en la flecha que está junto a **[Load]** y elija **[Load To...]**.
8. En el cuadro de diálogo **[Import Data]**, elija cómo ver los datos (**Tabla**, **[PivotTable Report]**, **Gráfico dinámico** o **[Only Create Connection]**) y luego, en **[Where do you want to put the data?]**, elija **[Existing worksheet:]** con la referencia, o **[New worksheet]**. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.1.2 -->

---

### 1.2.1 Search for data within a workbook

**EN · texto fuente, no editar**

**Exam route**

1. Click any single cell. Do not select a range unless the task confines the search to one, because a multi-cell selection silently restricts Find to that selection.
2. Go to the **Home** tab, **Editing** group, click **Find & Select**, and click **Find...**.
3. In the **Find and Replace** dialog, **Find** tab, click **Options >>** to expand the dialog. This click is the objective. The collapsed dialog cannot express anything that follows.
4. Type the search string in **Find what:**.
5. Open the **Within:** list and choose **Sheet** or **Workbook**. The word "workbook" in the task text means this list, set to **Workbook**.
6. Open the **Search:** list and choose **By Rows** or **By Columns**.
7. Open the **Look in:** list and choose **Formulas**, **Values**, **Notes** or **Comments**. **Formulas** finds text inside a formula, **Values** finds only what is displayed. (Office 2019 offered three entries, without the Notes / Comments split.)
8. Tick **Match case** and **Match entire cell contents** as the task requires.
9. To search by formatting rather than by content, click **Format...** and set the criteria in the **Find Format** dialog, or click the arrow beside **Format...** and choose **Choose Format From Cell...**.
10. Click **Find All**. The dialog grows a result list showing Book, Sheet, Name, Cell, Value and Formula for every hit. Click a row to jump to it, or press `Ctrl+A` inside the list to select every hit at once.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.2.1 -->

**Ruta de examen**

1. Haga clic en una sola celda, la que sea. No seleccione un rango a menos que la tarea limite la búsqueda a uno, porque una selección de varias celdas restringe la búsqueda a esa selección sin avisar.
2. Vaya a la pestaña **Inicio**, grupo **Edición**, haga clic en **Buscar y seleccionar** y haga clic en **[Find...]**.
3. En el cuadro de diálogo **[Find and Replace]**, pestaña **[Find]**, haga clic en **[Options >>]** para expandir el cuadro. Ese clic es el objetivo. El cuadro contraído no puede expresar nada de lo que sigue.
4. Escriba el texto que busca en **[Find what:]**.
5. Abra la lista **[Within:]** y elija **Hoja** o **Libro**. Cuando el enunciado de la tarea dice "libro", se refiere a esta lista puesta en **Libro**.
6. Abra la lista **[Search:]** y elija **[By Rows]** o **[By Columns]**.
7. Abra la lista **[Look in:]** y elija **Fórmulas**, **[Values]**, **[Notes]** o **Comentarios**. **Fórmulas** encuentra el texto que está dentro de una fórmula; **[Values]** encuentra solo lo que se muestra. (Office 2019 ofrecía tres entradas, sin la separación entre Notes y Comments.)
8. Marque **[Match case]** y **[Match entire cell contents]** según lo pida la tarea.
9. Para buscar por formato en lugar de por contenido, haga clic en **Formato...** y defina los criterios en el cuadro de diálogo **[Find Format]**, o haga clic en la flecha que está junto a **Formato...** y elija **[Choose Format From Cell...]**.
10. Haga clic en **[Find All]**. El cuadro crece y muestra una lista de resultados con Book, Sheet, Name, Cell, Value y Formula para cada coincidencia. Haga clic en un renglón para ir a él, o presione `Ctrl+A` dentro de la lista para seleccionar todas las coincidencias de una vez.

<!-- ES-FIN MO200-1.2.1 -->

---

### 1.2.2 Navigate to named cells, ranges, or workbook elements

**EN · texto fuente, no editar**

**Exam route**

1. Press `F5` or `Ctrl+G` to open the **Go To** dialog. Alternatively, go to the **Home** tab, **Editing** group, click **Find & Select**, and click **Go To...**.
2. In the **Go to:** list, click the defined name you want. Every workbook-scoped name appears there; sheet-scoped names appear only while their sheet is active.
3. Click **OK**. The named range is selected, not merely scrolled to.
4. To reach a cell that has no name, type the address into the **Reference:** box, for example `Sheet3!B47`, and click **OK**.
5. For workbook elements rather than named ranges, click **Special...** in the same dialog, or go to **Find & Select** and click **Go To Special...**.
6. In the **Go To Special** dialog, choose the element type: **Comments**, **Constants**, **Formulas** with its four sub-check-boxes **Numbers**, **Text**, **Logicals** and **Errors**, **Blanks**, **Current region**, **Current array**, **Objects**, **Row differences**, **Column differences**, **Precedents**, **Dependents**, **Last cell**, **Visible cells only**, **Conditional formats**, or **Data validation**. Click **OK**.

This dialog comes back three more times in the document: Expert 2.2.2 uses **Data validation**, Expert 2.3.4 uses **Conditional formats**, and Expert 3.5.1 uses **Precedents** and **Dependents** with the **Direct only** and **All levels** options that light up beneath them.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.2.2 -->

**Ruta de examen**

1. Presione `F5` o `Ctrl+G` para abrir el cuadro de diálogo **[Go To]**. También puede ir a la pestaña **Inicio**, grupo **Edición**, hacer clic en **Buscar y seleccionar** y hacer clic en **[Go To...]**.
2. En la lista **[Go to:]**, haga clic en el nombre definido que quiere. Ahí aparecen todos los nombres con ámbito de libro; los que tienen ámbito de hoja aparecen solo mientras su hoja está activa.
3. Haga clic en **Aceptar**. El rango con nombre queda seleccionado, no solo se desplaza la vista hasta él.
4. Para llegar a una celda que no tiene nombre, escriba la dirección en el cuadro **[Reference:]**, por ejemplo `Sheet3!B47`, y haga clic en **Aceptar**.
5. Para elementos del libro y no rangos con nombre, haga clic en **[Special...]** dentro del mismo cuadro, o vaya a **Buscar y seleccionar** y haga clic en **Ir a Especial...**.
6. En el cuadro de diálogo **Ir a Especial**, elija el tipo de elemento: **Comentarios**, **[Constants]**, **Fórmulas** con sus cuatro casillas secundarias **[Numbers]**, **Texto**, **[Logicals]** y **Errores**, **[Blanks]**, **[Current region]**, **[Current array]**, **[Objects]**, **[Row differences]**, **[Column differences]**, **[Precedents]**, **[Dependents]**, **[Last cell]**, **[Visible cells only]**, **[Conditional formats]** o **[Data validation]**. Haga clic en **Aceptar**.

Este cuadro de diálogo vuelve a aparecer tres veces más en el documento: Expert 2.2.2 usa **[Data validation]**, Expert 2.3.4 usa **[Conditional formats]** y Expert 3.5.1 usa **[Precedents]** y **[Dependents]** con las opciones **[Direct only]** y **[All levels]** que se encienden debajo.

<!-- ES-FIN MO200-1.2.2 -->

---

### 1.2.3 Insert and remove hyperlinks

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell that will carry the link.
2. Go to the **Insert** tab, **Links** group, and click **Link** (older builds and the right-click menu still read `Hyperlink...`).
3. The **Insert Hyperlink** dialog opens. Choose the destination type in the **Link to:** bar down the left side: **Existing File or Web Page**, **Place in This Document**, **Create New Document**, or **E-mail Address**. Those four buttons are four different dialog faces, and picking the right one is the objective.
4. For **Existing File or Web Page**, type or browse to the target in the **Address:** box, using **Current Folder**, **Browsed Pages** or **Recent Files** to locate it.
5. For **Place in This Document**, pick a sheet under **Cell Reference** and type the cell in **Type the cell reference:**, or pick an entry under **Defined Names**.
6. For **E-mail Address**, fill **E-mail address:** and **Subject:**.
7. Type the visible text in **Text to display:**.
8. Click **ScreenTip...**, type the hover text in the **Set Hyperlink ScreenTip** dialog, and click **OK**.
9. Click **OK** to close **Insert Hyperlink**.
10. To remove one link, right-click its cell and click **Remove Hyperlink**. To remove many at once, select the range, go to the **Home** tab, **Editing** group, click **Clear**, and click **Clear Hyperlinks** to strip the link but keep the blue underlined look, or **Remove Hyperlinks** to strip both.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.2.3 -->

**Ruta de examen**

1. Seleccione la celda que va a llevar el vínculo.
2. Vaya a la pestaña **Insertar**, grupo **Vínculos**, y haga clic en **Vínculo** (las compilaciones anteriores y el menú contextual todavía dicen `Hyperlink...`).
3. Se abre el cuadro de diálogo **Insertar hipervínculo**. Elija el tipo de destino en la barra **[Link to:]** del lado izquierdo: **Archivo o página web existente**, **Lugar de este documento**, **Crear nuevo documento** o **Dirección de correo electrónico**. Esos cuatro botones son cuatro caras distintas del cuadro, y elegir el correcto es el objetivo.
4. Para **Archivo o página web existente**, escriba el destino en el cuadro **[Address:]** o búsquelo con **Carpeta actual**, **Páginas consultadas** o **Archivos recientes**.
5. Para **Lugar de este documento**, elija una hoja en **Referencia de la celda** y escriba la celda en **[Type the cell reference:]**, o elija una entrada en **Nombres definidos**.
6. Para **Dirección de correo electrónico**, llene **[E-mail address:]** y **[Subject:]**.
7. Escriba el texto visible en **[Text to display:]**.
8. Haga clic en **[ScreenTip...]**, escriba el texto que aparece al pasar el puntero en el cuadro de diálogo **[Set Hyperlink ScreenTip]** y haga clic en **Aceptar**.
9. Haga clic en **Aceptar** para cerrar **Insertar hipervínculo**.
10. Para quitar un vínculo, haga clic derecho en su celda y haga clic en **[Remove Hyperlink]**. Para quitar varios de una vez, seleccione el rango, vaya a la pestaña **Inicio**, grupo **Edición**, haga clic en **Borrar** y haga clic en **Borrar hipervínculos** para quitar el vínculo pero dejar el aspecto azul subrayado, o en **Quitar hipervínculos** para quitar los dos.

<!-- ES-FIN MO200-1.2.3 -->

---

### 1.3.1 Modify page setup

**EN · texto fuente, no editar**

This is the first appearance of the **Page Setup** dialog, which 1.3.3, 1.5.1, 1.5.3 and Expert 1.2.5 all come back to. Its four tabs are described in full here.

**Exam route**

1. Select the worksheet, or select several sheet tabs with `Ctrl` to apply the same setup to a group.
2. Go to the **Page Layout** tab, **Page Setup** group, and click the dialog box launcher, the small arrow in the bottom right corner of the group.
3. The **Page Setup** dialog opens with four tabs: **Page**, **Margins**, **Header/Footer**, **Sheet**. Everything below happens without closing it.
4. On the **Page** tab, under **Orientation**, choose **Portrait** or **Landscape**. Under **Scaling**, choose **Adjust to: __ % normal size** or **Fit to: __ page(s) wide by __ tall**. Set **Paper size:** and **Print quality:**. Set **First page number:** if the task asks for numbering that does not start at 1.
5. Go to the **Margins** tab. Set **Top:**, **Bottom:**, **Left:**, **Right:**, and the **Header:** and **Footer:** distances. Under **Center on page**, tick **Horizontally** and **Vertically** as required.
6. Go to the **Sheet** tab. Under **Print titles**, set **Rows to repeat at top:** and **Columns to repeat at left:**. Under **Print**, tick **Gridlines**, **Black and white**, **Draft quality**, and **Row and column headings**. Set **Comments and notes:** and **Cell errors as:**. Under **Page order**, choose **Down, then over** or **Over, then down**. The **Print area:** box at the top of this tab is the second route to objective 1.5.1.
7. Click **Print Preview** inside the dialog to check the result before committing, then **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.3.1 -->

Aquí aparece por primera vez el cuadro de diálogo **Configurar página**, al que vuelven 1.3.3, 1.5.1, 1.5.3 y Expert 1.2.5. Sus cuatro pestañas se describen completas en este objetivo.

**Ruta de examen**

1. Seleccione la hoja de cálculo, o seleccione varias [sheet tabs] con `Ctrl` para aplicar la misma configuración a un grupo.
2. Vaya a la pestaña **Diseño de página**, grupo **Configurar página**, y haga clic en el [dialog box launcher], la flechita de la esquina inferior derecha del grupo.
3. Se abre el cuadro de diálogo **Configurar página** con cuatro pestañas: **Página**, **Márgenes**, **Encabezado y pie de página**, **Hoja**. Todo lo que sigue ocurre sin cerrarlo.
4. En la pestaña **Página**, en **Orientación**, elija **Vertical** o **Horizontal**. En **Ajuste de escala**, elija **[Adjust to: __ % normal size]** o **[Fit to: __ page(s) wide by __ tall]**. Defina **[Paper size:]** y **[Print quality:]**. Defina **[First page number:]** si la tarea pide una numeración que no empieza en 1.
5. Vaya a la pestaña **Márgenes**. Defina **[Top:]**, **[Bottom:]**, **[Left:]**, **[Right:]** y las distancias **[Header:]** y **[Footer:]**. En **[Center on page]**, marque **[Horizontally]** y **[Vertically]** según se pida.
6. Vaya a la pestaña **Hoja**. En **Imprimir títulos**, defina **Repetir filas en extremo superior:** y **[Columns to repeat at left:]**. En **Imprimir**, marque **Líneas de cuadrícula**, **Blanco y negro**, **Calidad de borrador** y **Encabezados de filas y columnas**. Defina **[Comments and notes:]** y **[Cell errors as:]**. En **Orden de las páginas**, elija **Hacia abajo, luego hacia la derecha** u **Hacia la derecha, luego hacia abajo**. El cuadro **Área de impresión:** que está hasta arriba de esta pestaña es la segunda ruta al objetivo 1.5.1.
7. Haga clic en **Vista preliminar** dentro del cuadro de diálogo para revisar el resultado antes de confirmar, y luego en **Aceptar**.

<!-- ES-FIN MO200-1.3.1 -->

---

### 1.3.2 Adjust row height and column width

**EN · texto fuente, no editar**

**Exam route**

1. Select the rows or columns by clicking their headings. Drag across headings, or `Ctrl`-click for a non-adjacent set.
2. Go to the **Home** tab, **Cells** group, and click **Format**.
3. For rows, click **Row Height...**, type the value in points in the **Row height:** box of the **Row Height** dialog, and click **OK**.
4. For columns, click **Format** again and click **Column Width...**, type the value in the **Column width:** box, and click **OK**. The unit is characters of the standard font, not points, which is why 20 is a wide column and 20 is a short row.
5. To size to content instead of to a number, click **Format** and click **AutoFit Row Height** or **AutoFit Column Width**.
6. To change the default for the whole sheet, click **Format** and click **Default Width...**, then type the value in the **Standard Width** dialog. On this machine the sheet defaults read `StandardHeight = 14.5` and `StandardWidth = 8.09`.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.3.2 -->

**Ruta de examen**

1. Seleccione las filas o las columnas haciendo clic en sus encabezados. Arrastre sobre los encabezados, o haga clic con `Ctrl` presionada para un conjunto no adyacente.
2. Vaya a la pestaña **Inicio**, grupo **Celdas**, y haga clic en **Formato**.
3. Para las filas, haga clic en **[Row Height...]**, escriba el valor en puntos en el cuadro **[Row height:]** del cuadro de diálogo **Alto de fila** y haga clic en **Aceptar**.
4. Para las columnas, haga clic otra vez en **Formato** y haga clic en **[Column Width...]**, escriba el valor en el cuadro **[Column width:]** y haga clic en **Aceptar**. La unidad son caracteres de la fuente estándar, no puntos, y por eso 20 es una columna ancha y 20 es una fila baja.
5. Para ajustar al contenido en lugar de a un número, haga clic en **Formato** y haga clic en **[AutoFit Row Height]** o **[AutoFit Column Width]**.
6. Para cambiar el valor predeterminado de toda la hoja, haga clic en **Formato**, haga clic en **[Default Width...]** y escriba el valor en el cuadro de diálogo **[Standard Width]**. En esta máquina los valores predeterminados de la hoja son `StandardHeight = 14.5` y `StandardWidth = 8.09`.

<!-- ES-FIN MO200-1.3.2 -->

---

### 1.3.3 Customize headers and footers

**EN · texto fuente, no editar**

**Exam route**

1. Open the **Page Setup** dialog as in 1.3.1: **Page Layout** tab, **Page Setup** group, dialog box launcher.
2. Go to the **Header/Footer** tab.
3. For a canned header, open the **Header:** list and pick one, and do the same with the **Footer:** list. For anything the task words specifically, do not use the lists.
4. Click **Custom Header...**. The **Header** dialog opens with three boxes: **Left section:**, **Center section:** and **Right section:**.
5. Click into the section the task names. Type any literal text.
6. Insert dynamic fields with the buttons above the boxes rather than typing the codes: **Format Text**, **Insert Page Number**, **Insert Number of Pages**, **Insert Date**, **Insert Time**, **Insert File Path**, **Insert File Name**, **Insert Sheet Name**, **Insert Picture**, **Format Picture**. Each writes its code into the box. Codes verified to round-trip through the object model: `&P` page number, `&N` number of pages, `&D` date, `&T` time, `&F` file name, `&A` sheet name.
7. Click **OK** to return to **Page Setup**.
8. Click **Custom Footer...** and repeat for the footer sections.
9. Back on the **Header/Footer** tab, tick the four check boxes as required: **Different odd and even pages**, **Different first page**, **Scale with Document**, **Align with page margins**. Verified defaults on a fresh sheet: the first two off, the last two on.
10. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.3.3 -->

**Ruta de examen**

1. Abra el cuadro de diálogo **Configurar página** como en 1.3.1: pestaña **Diseño de página**, grupo **Configurar página**, [dialog box launcher].
2. Vaya a la pestaña **Encabezado y pie de página**.
3. Para un encabezado predefinido, abra la lista **[Header:]** y elija uno, y haga lo mismo con la lista **[Footer:]**. Si la tarea pide algo con palabras específicas, no use las listas.
4. Haga clic en **[Custom Header...]**. Se abre el cuadro de diálogo **[Header]** con tres cuadros: **[Left section:]**, **[Center section:]** y **[Right section:]**.
5. Haga clic dentro de la sección que menciona la tarea. Escriba el texto literal que se pida.
6. Inserte los campos dinámicos con los botones que están arriba de los cuadros, en lugar de escribir los códigos: **[Format Text]**, **[Insert Page Number]**, **[Insert Number of Pages]**, **[Insert Date]**, **[Insert Time]**, **[Insert File Path]**, **[Insert File Name]**, **[Insert Sheet Name]**, **[Insert Picture]**, **[Format Picture]**. Cada uno escribe su código en el cuadro. Códigos verificados de ida y vuelta con el modelo de objetos: `&P` número de página, `&N` número de páginas, `&D` fecha, `&T` hora, `&F` nombre del archivo, `&A` nombre de la hoja.
7. Haga clic en **Aceptar** para volver a **Configurar página**.
8. Haga clic en **[Custom Footer...]** y repita con las secciones del pie de página.
9. De vuelta en la pestaña **Encabezado y pie de página**, marque las cuatro casillas según se pida: **[Different odd and even pages]**, **[Different first page]**, **[Scale with Document]**, **[Align with page margins]**. Valores predeterminados verificados en una hoja nueva: las dos primeras desactivadas, las dos últimas activadas.
10. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.3.3 -->

---

### 1.4.1 Customize the Quick Access toolbar

**EN · texto fuente, no editar**

**Exam route**

1. If the Quick Access Toolbar is not visible, right-click anywhere on the ribbon and click the command that shows it. (Caption **TO CONFIRM**: recent Microsoft 365 builds hide the toolbar by default and the ribbon context menu carries the toggle; the object model exposes no label for this control.)
2. Go to the **File** tab and click **Options**.
3. In the **Excel Options** dialog, select the **Quick Access Toolbar** pane on the left.
4. Open the **Customize Quick Access Toolbar:** list on the right and choose **For all documents (default)** or the current file by name. Choosing the file scopes the button to that workbook only, and tasks that say "for this workbook" mean this list.
5. Open the **Choose commands from:** list on the left and pick the source: **Popular Commands**, **Commands Not in the Ribbon**, **All Commands**, **Macros**, or a tab by name. **Commands Not in the Ribbon** is where the exam hides its awkward requests.
6. Click the command in the left list and click **Add >>**.
7. Order the toolbar with the **Move Up** and **Move Down** arrows at the right edge.
8. To change a button's icon or display name, select it in the right list and click **Modify...**.
9. To remove one, select it in the right list and click **Remove**.
10. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.1 -->

**Ruta de examen**

1. Si la barra de herramientas de acceso rápido no está visible, haga clic derecho en cualquier parte de la cinta de opciones y haga clic en el comando que la muestra. (Redacción del comando: **TO CONFIRM**. Las compilaciones recientes de Microsoft 365 ocultan la barra de forma predeterminada y el menú contextual de la cinta trae el interruptor; el modelo de objetos no expone ninguna etiqueta para ese control.)
2. Vaya a la pestaña **Archivo** y haga clic en **Opciones**.
3. En el cuadro de diálogo **Opciones de Excel**, seleccione el panel **Barra de herramientas de acceso rápido** de la izquierda.
4. Abra la lista **Personalizar la barra de herramientas de acceso rápido:** de la derecha y elija **[For all documents (default)]** o el archivo actual por su nombre. Elegir el archivo limita el botón a ese libro, y las tareas que dicen "para este libro" se refieren a esta lista.
5. Abra la lista **[Choose commands from:]** de la izquierda y elija el origen: **[Popular Commands]**, **[Commands Not in the Ribbon]**, **[All Commands]**, **Macros**, o una pestaña por su nombre. En **[Commands Not in the Ribbon]** es donde el examen esconde sus peticiones incómodas.
6. Haga clic en el comando de la lista de la izquierda y haga clic en **[Add >>]**.
7. Ordene la barra con las flechas **[Move Up]** y **[Move Down]** del borde derecho.
8. Para cambiar el icono o el nombre visible de un botón, selecciónelo en la lista de la derecha y haga clic en **[Modify...]**.
9. Para quitar uno, selecciónelo en la lista de la derecha y haga clic en **[Remove]**.
10. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.4.1 -->

---

### 1.4.2 Display and modify workbook content in different views

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **View** tab, **Workbook Views** group.
2. Click the view the task names: **Normal**, **Page Break Preview**, or **Page Layout**. In the object model these are `Window.View` values 1, 2 and 3, and all three were set and read back on this machine.
3. In **Page Break Preview**, drag a blue page-break line to move it. Dragging creates a manual break, drawn as a solid line where the automatic break was dashed. Right-click a cell and click **Reset All Page Breaks** to return to automatic breaks.
4. In **Page Layout**, click directly into the header and footer boxes to edit them, and drag the rulers to change margins.
5. To store a view rather than switch to one, set up the sheet exactly as it should be remembered, then click **Custom Views...** in the same group.
6. In the **Custom Views** dialog, click **Add...**.
7. In the **Add View** dialog, type a name in the **Name:** box. Under **Include in view**, tick **Print settings** and **Hidden rows, columns and filter settings**. Verified: `CustomViews.Add` takes exactly these two booleans and the view was created. Click **OK**.
8. To recall it later, open **Custom Views...**, select the name in the **Views:** list, and click **Show**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.2 -->

**Ruta de examen**

1. Vaya a la pestaña **Vista**, grupo **Vistas de libro**.
2. Haga clic en la vista que menciona la tarea: **Normal**, **Vista previa de salto de página** o **Diseño de página**. En el modelo de objetos son los valores 1, 2 y 3 de `Window.View`, y los tres se pudieron establecer y volver a leer en esta máquina.
3. En **Vista previa de salto de página**, arrastre una línea azul de salto de página para moverla. Al arrastrarla se crea un salto manual, dibujado como línea continua donde el salto automático era punteado. Haga clic derecho en una celda y haga clic en **[Reset All Page Breaks]** para volver a los saltos automáticos.
4. En **Diseño de página**, haga clic directamente en los cuadros del encabezado y del pie de página para editarlos, y arrastre las reglas para cambiar los márgenes.
5. Para guardar una vista en lugar de cambiar a una, deje la hoja exactamente como se debe recordar y haga clic en **[Custom Views...]** en el mismo grupo.
6. En el cuadro de diálogo **Vistas personalizadas**, haga clic en **[Add...]**.
7. En el cuadro de diálogo **[Add View]**, escriba un nombre en el cuadro **[Name:]**. En **[Include in view]**, marque **[Print settings]** y **[Hidden rows, columns and filter settings]**. Verificado: `CustomViews.Add` recibe exactamente esos dos booleanos y la vista se creó. Haga clic en **Aceptar**.
8. Para recuperarla después, abra **[Custom Views...]**, seleccione el nombre en la lista **[Views:]** y haga clic en **Mostrar**.

<!-- ES-FIN MO200-1.4.2 -->

---

### 1.4.3 Freeze worksheet rows and columns

**EN · texto fuente, no editar**

**Exam route**

1. Work out the anchor cell. Excel freezes everything above and everything to the left of the cell you select, so to freeze rows 1 and 2 plus column A the anchor is `B3`.
2. Click that single cell. Not the row heading, not the column heading, the cell.
3. Go to the **View** tab, **Window** group, and click **Freeze Panes**.
4. Click **Freeze Panes** in the drop-down. The two convenience entries below it, **Freeze Top Row** and **Freeze First Column**, ignore your selection entirely and freeze exactly one line each.
5. To release, click **Freeze Panes** again and click **Unfreeze Panes**.

Verified on this machine: selecting `B3` and freezing produced `SplitRow = 2` and `SplitColumn = 1`, which is the arithmetic the anchor rule describes.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.3 -->

**Ruta de examen**

1. Calcule la celda de anclaje. Excel inmoviliza todo lo que está arriba y todo lo que está a la izquierda de la celda que seleccione, así que para inmovilizar las filas 1 y 2 más la columna A la celda de anclaje es `B3`.
2. Haga clic en esa única celda. No en el encabezado de fila, no en el encabezado de columna: la celda.
3. Vaya a la pestaña **Vista**, grupo **Ventana**, y haga clic en **Inmovilizar paneles**.
4. Haga clic en **Inmovilizar paneles** dentro de la lista desplegable. Las dos entradas de conveniencia que están debajo, **Inmovilizar fila superior** y **Inmovilizar primera columna**, ignoran por completo su selección e inmovilizan exactamente una línea cada una.
5. Para liberarlos, haga clic otra vez en **Inmovilizar paneles** y haga clic en **Movilizar paneles**.

Verificado en esta máquina: seleccionar `B3` e inmovilizar produjo `SplitRow = 2` y `SplitColumn = 1`, que es la aritmética que describe la regla de la celda de anclaje.

<!-- ES-FIN MO200-1.4.3 -->

---

### 1.4.4 Change window views

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **View** tab, **Window** group.
2. Click **New Window** to open a second window onto the same workbook. Verified: the two window captions become `file.xlsx  -  1` and `file.xlsx  -  2`, and the number after the file name is how you tell them apart.
3. Click **Arrange All**.
4. In the **Arrange Windows** dialog, under **Arrange**, choose **Tiled**, **Horizontal**, **Vertical**, or **Cascade**. Tick **Windows of active workbook** to arrange only the windows onto the current file rather than every open workbook. Click **OK**. Verified: `Windows.Arrange(2)` for vertical executed without error.
5. To compare two workbooks, click **View Side by Side**, then **Synchronous Scrolling** to lock the two scroll positions together, and **Reset Window Position** to even them up again.
6. To split one window rather than open a second, click the cell where the split should fall and click **Split**. Click **Split** again to remove it.
7. To take a window out of the way, click **Hide**. To bring it back, click **Unhide...**, select the workbook in the **Unhide** dialog, and click **OK**.
8. To jump between open windows, click **Switch Windows** and pick from the numbered list.
9. For magnification, use the **Zoom** group: click **Zoom...** and choose a **Magnification** option (**200%**, **100%**, **75%**, **50%**, **25%**, **Fit selection**, or **Custom: __ %**) then **OK**. **Zoom to Selection** sizes the current selection to fill the window.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.4 -->

**Ruta de examen**

1. Vaya a la pestaña **Vista**, grupo **Ventana**.
2. Haga clic en **Nueva ventana** para abrir una segunda ventana sobre el mismo libro. Verificado: los títulos de las dos ventanas quedan como `file.xlsx  -  1` y `file.xlsx  -  2`, y el número que va después del nombre del archivo es la manera de distinguirlas.
3. Haga clic en **Organizar todo**.
4. En el cuadro de diálogo **[Arrange Windows]**, en **Organizar**, elija **[Tiled]**, **Horizontal**, **Vertical** o **[Cascade]**. Marque **[Windows of active workbook]** para organizar solo las ventanas del archivo actual y no todos los libros abiertos. Haga clic en **Aceptar**. Verificado: `Windows.Arrange(2)` para vertical se ejecutó sin error.
5. Para comparar dos libros, haga clic en **Ver en paralelo**, luego en **Desplazamiento sincrónico** para amarrar las dos posiciones de desplazamiento, y en **Restablecer posición de la ventana** para volver a emparejarlas.
6. Para dividir una ventana en lugar de abrir otra, haga clic en la celda donde debe caer la división y haga clic en **Dividir**. Haga clic otra vez en **Dividir** para quitarla.
7. Para quitar una ventana de en medio, haga clic en **Ocultar**. Para traerla de vuelta, haga clic en **[Unhide...]**, seleccione el libro en el cuadro de diálogo **Mostrar** y haga clic en **Aceptar**.
8. Para saltar entre las ventanas abiertas, haga clic en **Cambiar ventanas** y elija de la lista numerada.
9. Para la ampliación, use el grupo **Zoom**: haga clic en **Zoom...** y elija una opción de **[Magnification]** (**200%**, **100%**, **75%**, **50%**, **25%**, **[Fit selection]** o **[Custom: __ %]**), luego **Aceptar**. **Ampliar selección** ajusta la selección actual para que llene la ventana.

<!-- ES-FIN MO200-1.4.4 -->

---

### 1.4.5 Modify basic workbook properties

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Info**.
2. Look at the **Properties** panel down the right side. It lists Size, Title, Tags, Categories and the dates. Click a field value to edit it in place.
3. Click **Show All Properties** at the bottom of the panel to expose the rest: Comments, Template, Status, Subject, Hyperlink Base, Company, Manager, Author, Last Modified By.
4. For the fields the backstage panel does not expose, click **Properties** at the top of the panel and click **Advanced Properties** (the same control resolves in the object model as `View Document Properties...`).
5. In the **Document Properties** dialog, go to the **Summary** tab and fill the boxes: **Title:**, **Subject:**, **Author:**, **Manager:**, **Company:**, **Category:**, **Keywords:**, **Comments:**, **Hyperlink base:**, **Template:**. Verified: all of these exist as built-in properties on this build and were read back through the object model.
6. Tick **Save preview picture** if the task asks for a thumbnail.
7. To create a property that is not built in, go to the **Custom** tab. Type in **Name:** or pick one from the list above it, set **Type:** to Text, Date, Number or Yes or no, type the value in **Value:**, and click **Add**. Tick **Link to content** to bind the property to a defined name in the workbook.
8. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.5 -->

**Ruta de examen**

1. Vaya a la pestaña **Archivo** y haga clic en **Información**.
2. Vea el panel **Propiedades** del lado derecho. Ahí aparecen Size, Title, Tags, Categories y las fechas. Haga clic en el valor de un campo para editarlo ahí mismo.
3. Haga clic en **[Show All Properties]**, al fondo del panel, para mostrar el resto: Comments, Template, Status, Subject, Hyperlink Base, Company, Manager, Author, Last Modified By.
4. Para los campos que el panel de Backstage no muestra, haga clic en **Propiedades**, arriba del panel, y haga clic en **[Advanced Properties]** (el mismo control se resuelve en el modelo de objetos como `View Document Properties...`).
5. En el cuadro de diálogo **[Document Properties]**, vaya a la pestaña **[Summary]** y llene los cuadros: **[Title:]**, **[Subject:]**, **[Author:]**, **[Manager:]**, **[Company:]**, **[Category:]**, **[Keywords:]**, **Comentarios:**, **[Hyperlink base:]**, **[Template:]**. Verificado: todas existen como propiedades integradas en esta compilación y se pudieron leer con el modelo de objetos.
6. Marque **[Save preview picture]** si la tarea pide una miniatura.
7. Para crear una propiedad que no está integrada, vaya a la pestaña **Personalizada**. Escriba en **[Name:]** o elija uno de la lista que está arriba, ponga **[Type:]** en Text, Date, Number o Yes or no, escriba el valor en **[Value:]** y haga clic en **[Add]**. Marque **[Link to content]** para amarrar la propiedad a un nombre definido del libro.
8. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.4.5 -->

---

### 1.4.6 Display formulas

**EN · texto fuente, no editar**

**Exam route**

1. Click the sheet whose formulas are to be shown. The setting is per worksheet window, not per workbook.
2. Go to the **Formulas** tab, **Formula Auditing** group.
3. Click **Show Formulas**. Every cell now displays its formula instead of its result, and Excel widens the displayed columns to fit.
4. Click **Show Formulas** again to turn it off. Column widths return to their stored values.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.4.6 -->

**Ruta de examen**

1. Haga clic en la hoja cuyas fórmulas se van a mostrar. La opción es por ventana de hoja de cálculo, no por libro.
2. Vaya a la pestaña **Fórmulas**, grupo **Auditoría de fórmulas**.
3. Haga clic en **Mostrar fórmulas**. Cada celda muestra ahora su fórmula en lugar de su resultado, y Excel ensancha las columnas que se ven para que quepan.
4. Haga clic otra vez en **Mostrar fórmulas** para desactivarlo. Los anchos de columna vuelven a sus valores guardados.

<!-- ES-FIN MO200-1.4.6 -->

---

### 1.5.1 Set a print area

**EN · texto fuente, no editar**

**Exam route**

1. Select the range to print. For a print area in several blocks, `Ctrl`-click each additional block into the same selection.
2. Go to the **Page Layout** tab, **Page Setup** group, and click **Print Area**.
3. Click **Set Print Area**.
4. To extend an existing print area, select the extra range, click **Print Area** again, and click **Add to Print Area**. Each block added this way becomes its own page.
5. To remove it, click **Print Area** and click **Clear Print Area**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.5.1 -->

**Ruta de examen**

1. Seleccione el rango que se va a imprimir. Para un área de impresión de varios bloques, agregue cada bloque adicional a la misma selección haciendo clic con `Ctrl` presionada.
2. Vaya a la pestaña **Diseño de página**, grupo **Configurar página**, y haga clic en **Área de impresión**.
3. Haga clic en **Establecer área de impresión**.
4. Para ampliar un área de impresión que ya existe, seleccione el rango adicional, haga clic otra vez en **Área de impresión** y haga clic en **[Add to Print Area]**. Cada bloque agregado así se convierte en su propia página.
5. Para quitarla, haga clic en **Área de impresión** y haga clic en **Borrar área de impresión**.

<!-- ES-FIN MO200-1.5.1 -->

---

### 1.5.2 Save workbooks in alternative file formats

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Export**.
2. For PDF, click **Create PDF/XPS Document**, then click the **Create PDF/XPS** button.
3. In the **Publish as PDF or XPS** dialog, set the file name, choose **Optimize for: Standard (publishing online and printing)** or **Minimum size (publishing online)**, and tick **Open file after publishing** if wanted.
4. Click **Options...** and set **Page range**, then under **Publish what** choose **Selection**, **Active sheet(s)**, **Entire workbook** or **Table**, and tick **Ignore print areas**, **Document properties** and **Document structure tags for accessibility** as required. Click **OK**.
5. Click **Publish**.
6. For any other format, go back to **File**, **Export**, and click **Change File Type**.
7. Pick from the **Workbook File Types** and **Other File Types** lists, then click the **Save As** button below them.
8. In the **Save As** dialog, confirm the entry in the **Save as type:** list, set the file name, and click **Save**. Read the compatibility warning if one appears.

The formats behind the list entries were each written successfully on this machine: `.csv`, `.txt` tab delimited, `.xlsm`, `.xltx`, `.xls`, XML Spreadsheet 2003, and PDF. The list entries read **Excel Workbook (\*.xlsx)**, **Excel Macro-Enabled Workbook (\*.xlsm)**, **Excel Binary Workbook (\*.xlsb)**, **Excel 97-2003 Workbook (\*.xls)**, **CSV UTF-8 (Comma delimited) (\*.csv)**, **Excel Template (\*.xltx)**, **PDF (\*.pdf)**, **Text (Tab delimited) (\*.txt)**. Exact punctuation of each entry: **TO CONFIRM** against the open dialog.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.5.2 -->

**Ruta de examen**

1. Vaya a la pestaña **Archivo** y haga clic en **Exportar**.
2. Para PDF, haga clic en **[Create PDF/XPS Document]** y luego en el botón **[Create PDF/XPS]**.
3. En el cuadro de diálogo **[Publish as PDF or XPS]**, ponga el nombre del archivo, elija **[Optimize for: Standard (publishing online and printing)]** o **[Minimum size (publishing online)]**, y marque **[Open file after publishing]** si se quiere.
4. Haga clic en **[Options...]** y defina **[Page range]**; luego, en **[Publish what]**, elija **[Selection]**, **[Active sheet(s)]**, **[Entire workbook]** o **Tabla**, y marque **[Ignore print areas]**, **[Document properties]** y **[Document structure tags for accessibility]** según se pida. Haga clic en **Aceptar**.
5. Haga clic en **Publicar**.
6. Para cualquier otro formato, regrese a **Archivo**, **Exportar**, y haga clic en **[Change File Type]**.
7. Elija de las listas **[Workbook File Types]** y **[Other File Types]**, y luego haga clic en el botón **Guardar como** que está debajo.
8. En el cuadro de diálogo **Guardar como**, confirme la entrada de la lista **[Save as type:]**, ponga el nombre del archivo y haga clic en **Guardar**. Lea la advertencia de compatibilidad si aparece alguna.

Los formatos que están detrás de las entradas de la lista se escribieron todos con éxito en esta máquina: `.csv`, `.txt` delimitado por tabulaciones, `.xlsm`, `.xltx`, `.xls`, XML Spreadsheet 2003 y PDF. Las entradas de la lista dicen **[Excel Workbook (\*.xlsx)]**, **[Excel Macro-Enabled Workbook (\*.xlsm)]**, **[Excel Binary Workbook (\*.xlsb)]**, **[Excel 97-2003 Workbook (\*.xls)]**, **[CSV UTF-8 (Comma delimited) (\*.csv)]**, **[Excel Template (\*.xltx)]**, **[PDF (\*.pdf)]**, **[Text (Tab delimited) (\*.txt)]**. Puntuación exacta de cada entrada: **TO CONFIRM** contra el cuadro de diálogo abierto.

<!-- ES-FIN MO200-1.5.2 -->

---

### 1.5.3 Configure print settings

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Print**, or press `Ctrl+P`. The Print backstage opens with the settings column on the left and the preview on the right.
2. Set **Copies:** with the spinner at the top.
3. Choose the printer from the **Printer** list.
4. Open the first **Settings** list and choose **Print Active Sheets**, **Print Entire Workbook**, or **Print Selection**. If a print area exists and the task asks to bypass it, tick **Ignore Print Area** at the bottom of that same list.
5. Set **Pages:** __ **to** __ to limit the page range.
6. Open the next lists in turn and set **Print One Sided** or **Print on Both Sides**, **Collated** or **Uncollated**, **Portrait Orientation** or **Landscape Orientation**, the paper size, and **Normal Margins**, **Wide Margins**, **Narrow Margins** or **Custom Margins**.
7. Open the last list and choose the scaling: **No Scaling**, **Fit Sheet on One Page**, **Fit All Columns on One Page**, **Fit All Rows on One Page**, or **Custom Scaling Options...**, which opens the **Page Setup** dialog on its **Page** tab.
8. Check the page counter under the preview before printing.
9. Click **Print**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.5.3 -->

**Ruta de examen**

1. Vaya a la pestaña **Archivo** y haga clic en **Imprimir**, o presione `Ctrl+P`. Se abre la vista Backstage de impresión, con la columna de opciones a la izquierda y la vista previa a la derecha.
2. Defina **[Copies:]** con el control de número que está hasta arriba.
3. Elija la impresora en la lista **Impresora**.
4. Abra la primera lista de **Configuración** y elija **Imprimir hojas activas**, **[Print Entire Workbook]** o **[Print Selection]**. Si ya hay un área de impresión y la tarea pide saltársela, marque **[Ignore Print Area]** al final de esa misma lista.
5. Defina **[Pages:]** __ **[to]** __ para limitar el intervalo de páginas.
6. Abra las siguientes listas una por una y defina **Imprimir a una cara** o **[Print on Both Sides]**, **Intercaladas** o **[Uncollated]**, **Orientación vertical** o **[Landscape Orientation]**, el tamaño de papel, y **[Normal Margins]**, **[Wide Margins]**, **[Narrow Margins]** o **[Custom Margins]**.
7. Abra la última lista y elija el ajuste de escala: **[No Scaling]**, **[Fit Sheet on One Page]**, **[Fit All Columns on One Page]**, **[Fit All Rows on One Page]** o **[Custom Scaling Options...]**, que abre el cuadro de diálogo **Configurar página** en su pestaña **Página**.
8. Revise el contador de páginas que está debajo de la vista previa antes de imprimir.
9. Haga clic en **Imprimir**.

<!-- ES-FIN MO200-1.5.3 -->

---

### 1.5.4 Inspect workbooks for issues

**EN · texto fuente, no editar**

Three separate tools sit behind this objective, and the exam names them one at a time.

**Exam route**

1. Go to the **File** tab and click **Info**.
2. Click **Check for Issues**.

*Document Inspector.*

3. Click **Inspect Document**. Save the file first if prompted, because the removals cannot be undone.
4. In the **Document Inspector** dialog, tick only the categories the task names and untick the rest: **Comments and Notes**; **Document Properties and Personal Information**; **Data Model**; **Content Add-ins**; **Task Pane Add-ins**; **PivotTables, PivotCharts, Cube Formulas, Slicers, and Timelines**; **Custom XML Data**; **Headers and Footers**; **Hidden Rows and Columns**; **Hidden Worksheets**; **Invisible Content**. (Category wording: **TO CONFIRM** against the open dialog. The set is stable across recent builds but the object model does not expose the strings.)
5. Click **Inspect**.
6. Read the results. Each section that found something offers a **Remove All** button. Click it only for the sections the task names, because removal is permanent.
7. Click **Reinspect** to confirm, then **Close**.

*Accessibility Checker.* This is the tool Associate 5.3.3 comes back to for chart alt text.

8. Go back to **File**, **Info**, **Check for Issues**, and click **Check Accessibility**. The same command sits on the **Review** tab, **Accessibility** group.
9. The **Accessibility** pane opens on the right with **Inspection Results** grouped into **Errors**, **Warnings** and **Tips**.
10. Click an item to select the offending object, then use **Additional Information** at the bottom of the pane for the recommended fix. Tick **Keep accessibility checker running while I work** to leave it live.

*Compatibility Checker.*

11. Go back to **File**, **Info**, **Check for Issues**, and click **Check Compatibility**.
12. In the **Microsoft Excel - Compatibility Checker** dialog, click **Select versions to show** and tick the versions to test against: **Excel 97-2003**, **Excel 2007**, **Excel 2010**, **Excel 2013**.
13. Read the **Summary** list, which reports significant loss of functionality and minor loss of fidelity with an occurrence count and a **Find** link for each.
14. Click **Copy to New Sheet** to write the report into the workbook as evidence.
15. Tick **Check compatibility when saving this workbook** if the task asks for it. Verified: this is the `Workbook.CheckCompatibility` property, and it reads `False` on a new workbook.
16. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-1.5.4 -->

Detrás de este objetivo hay tres herramientas distintas, y el examen las menciona una por una.

**Ruta de examen**

1. Vaya a la pestaña **Archivo** y haga clic en **Información**.
2. Haga clic en **Comprobar si hay problemas**.

*Inspector de documento.*

3. Haga clic en **[Inspect Document]**. Guarde el archivo primero si se lo pide, porque lo que se quita no se puede deshacer.
4. En el cuadro de diálogo **Inspector de documento**, marque solo las categorías que menciona la tarea y desmarque el resto: **[Comments and Notes]**; **[Document Properties and Personal Information]**; **[Data Model]**; **[Content Add-ins]**; **[Task Pane Add-ins]**; **[PivotTables, PivotCharts, Cube Formulas, Slicers, and Timelines]**; **[Custom XML Data]**; **[Headers and Footers]**; **[Hidden Rows and Columns]**; **[Hidden Worksheets]**; **[Invisible Content]**. (Redacción de las categorías: **TO CONFIRM** contra el cuadro de diálogo abierto. El conjunto es estable en las compilaciones recientes, pero el modelo de objetos no expone las cadenas.)
5. Haga clic en **[Inspect]**.
6. Lea los resultados. Cada sección que encontró algo ofrece un botón **Quitar todos**. Haga clic en él solo para las secciones que menciona la tarea, porque quitar es permanente.
7. Haga clic en **[Reinspect]** para confirmar, y luego en **Cerrar**.

*Comprobador de accesibilidad.* Es la herramienta a la que vuelve Associate 5.3.3 para el texto alternativo de los gráficos.

8. Regrese a **Archivo**, **Información**, **Comprobar si hay problemas**, y haga clic en **Comprobador de accesibilidad**. El mismo comando está en la pestaña **Revisar**, grupo **Accesibilidad**.
9. El panel **Accesibilidad** se abre a la derecha con **Resultados de la inspección** agrupados en **Errores**, **[Warnings]** y **[Tips]**.
10. Haga clic en un elemento para seleccionar el objeto que lo provoca, y use **Información adicional**, al fondo del panel, para ver la corrección recomendada. Marque **[Keep accessibility checker running while I work]** para dejarlo activo.

*Comprobador de compatibilidad.*

11. Regrese a **Archivo**, **Información**, **Comprobar si hay problemas**, y haga clic en **[Check Compatibility]**.
12. En el cuadro de diálogo **[Microsoft Excel - Compatibility Checker]**, haga clic en **[Select versions to show]** y marque las versiones contra las que se va a probar: **Excel 97-2003**, **Excel 2007**, **Excel 2010**, **Excel 2013**.
13. Lea la lista **[Summary]**, que reporta la pérdida importante de funcionalidad y la pérdida menor de fidelidad, con un conteo de apariciones y un vínculo **[Find]** para cada una.
14. Haga clic en **[Copy to New Sheet]** para escribir el reporte dentro del libro como evidencia.
15. Marque **[Check compatibility when saving this workbook]** si la tarea lo pide. Verificado: es la propiedad `Workbook.CheckCompatibility`, y en un libro nuevo se lee `False`.
16. Haga clic en **Aceptar**.

<!-- ES-FIN MO200-1.5.4 -->

---

## MO-200 Associate · Domain 2, Manage data cells and ranges

Four objectives in this domain (2.2.1, 2.2.2, 2.2.4 and 2.2.6) run through the **Format Cells** dialog. The dialog itself (how it opens, its six tabs, and why one trip through it beats three clicks on the ribbon) is written out in full at **2.2.6**. The three earlier entries give only the tab they need and point there.

### 2.1.1 Paste data by using special paste options

**EN · texto fuente, no editar**

**Exam route**

1. Select the source range.
2. Go to the **Home** tab, **Clipboard** group, and click **Copy**. A marching border appears around the source. Do not press Ctrl+X unless the task says move: cut disables most of the Paste Special options.
3. Select the destination. One cell is enough, Excel uses it as the top left corner.
4. Go to the **Home** tab, **Clipboard** group, and click the **arrow under the Paste button**, not the button face. The Paste gallery opens.
5. At the bottom of the gallery click **Paste Special...**. The **Paste Special** dialog opens.
6. In the **Paste** section, select the option the task names: **All**, **Formulas**, **Values**, **Formats**, **Comments and Notes**, **Validation**, **All using Source theme**, **All except borders**, **Column widths**, **Formulas and number formats**, **Values and number formats**, **All merging conditional formats**.
7. If the task asks for arithmetic against what is already in the destination, go to the **Operation** section and select **None**, **Add**, **Subtract**, **Multiply** or **Divide**. This section exists only here.
8. Select the **Skip blanks** check box if empty source cells must not overwrite destination values.
9. Select the **Transpose** check box if rows must become columns.
10. Click **OK**. To paste a live link instead, click the **Paste Link** button at the bottom left rather than OK.
11. Press **Esc** to clear the marching border.

The Paste section, the Operation section and the two check boxes are all applied in a single operation. Values plus Transpose plus Skip blanks is one paste, not three.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.1.1 -->

**Ruta de examen**

1. Selecciona el rango de origen.
2. Ve a la pestaña **Inicio**, grupo **Portapapeles**, y haz clic en **Copiar**. Aparece un borde punteado en movimiento alrededor del origen. No presiones Ctrl+X a menos que la tarea pida mover: cortar desactiva casi todas las opciones de Pegado especial.
3. Selecciona el destino. Basta con una celda, Excel la toma como esquina superior izquierda.
4. Ve a la pestaña **Inicio**, grupo **Portapapeles**, y haz clic en la **flecha que está debajo del botón Pegar**, no en el botón mismo. Se abre la galería de pegado.
5. Hasta abajo de la galería, haz clic en **Pegado especial...**. Se abre el cuadro de diálogo **Pegado especial**.
6. En la sección **Pegar**, selecciona la opción que nombra la tarea: **[All]**, **Fórmulas**, **[Values]**, **[Formats]**, **[Comments and Notes]**, **[Validation]**, **[All using Source theme]**, **[All except borders]**, **[Column widths]**, **[Formulas and number formats]**, **[Values and number formats]**, **[All merging conditional formats]**.
7. Si la tarea pide una operación aritmética contra lo que ya está en el destino, ve a la sección **[Operation]** y selecciona **Ninguno**, **[Add]**, **[Subtract]**, **[Multiply]** o **[Divide]**. Esta sección solo existe aquí.
8. Selecciona la casilla **[Skip blanks]** si las celdas vacías del origen no deben sobrescribir los valores del destino.
9. Selecciona la casilla **Transponer** si las filas deben convertirse en columnas.
10. Haz clic en **Aceptar**. Si lo que quieres es pegar un vínculo activo, haz clic en el botón **[Paste Link]** de la esquina inferior izquierda y no en Aceptar.
11. Presiona **Esc** para quitar el borde punteado.

La sección Pegar, la sección [Operation] y las dos casillas se aplican en una sola operación. [Values] más Transponer más [Skip blanks] es un solo pegado, no tres.

<!-- ES-FIN MO200-2.1.1 -->

---

### 2.1.2 Fill cells by using Auto Fill

**EN · texto fuente, no editar**

**Exam route**

1. Type the first value. If the step is not 1, type the second value too and select both.
2. Select the seed cell or cells **together with the whole range to be filled**. The selection defines the extent, so include the destination.
3. Go to the **Home** tab, **Editing** group, and click **Fill**.
4. For a straight copy, click **Down**, **Right**, **Up** or **Left**.
5. For a pattern, click **Series...**. The **Series** dialog opens.
6. In **Series in**, select **Rows** or **Columns**.
7. In **Type**, select **Linear**, **Growth**, **Date** or **AutoFill**.
8. If Type is Date, set **Date unit** to **Day**, **Weekday**, **Month** or **Year**.
9. Type the **Step value**. Type a **Stop value** if the task gives an end instead of a range.
10. Select the **Trend** check box only if the task asks for a trend fitted to the existing values.
11. Click **OK**.

The Series dialog is the Associate half of this; its Growth, Stop value, Trend and custom-list behaviour are Expert 2.1.2 and are written out there.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.1.2 -->

**Ruta de examen**

1. Escribe el primer valor. Si el paso no es 1, escribe también el segundo valor y selecciona los dos.
2. Selecciona la celda o las celdas semilla **junto con todo el rango que se va a rellenar**. La selección define la extensión, así que incluye el destino.
3. Ve a la pestaña **Inicio**, grupo **Edición**, y haz clic en **Rellenar**.
4. Para una copia directa, haz clic en **[Down]**, **[Right]**, **[Up]** o **[Left]**.
5. Para un patrón, haz clic en **Serie...**. Se abre el cuadro de diálogo **Serie**.
6. En **[Series in]**, selecciona **[Rows]** o **[Columns]**.
7. En **Tipo**, selecciona **[Linear]**, **[Growth]**, **Fecha** o **[AutoFill]**.
8. Si Tipo es Fecha, pon **[Date unit]** en **[Day]**, **[Weekday]**, **[Month]** o **[Year]**.
9. Escribe el **[Step value]**. Escribe un **[Stop value]** si la tarea da un final en lugar de un rango.
10. Selecciona la casilla **[Trend]** solo si la tarea pide una tendencia ajustada a los valores que ya están.
11. Haz clic en **Aceptar**.

El cuadro de diálogo Serie es la mitad Associate de este objetivo; su comportamiento de [Growth], [Stop value], [Trend] y listas personalizadas es el Expert 2.1.2 y ahí está escrito completo.

<!-- ES-FIN MO200-2.1.2 -->

---

### 2.1.3 Insert and delete multiple columns or rows

**EN · texto fuente, no editar**

**Exam route**

1. Decide how many rows or columns are needed. Excel inserts exactly as many as are selected.
2. Select that many **whole rows** by dragging down the row headings, or that many **whole columns** by dragging across the column headings. To insert three rows above row 5, select rows 5, 6 and 7.
3. Go to the **Home** tab, **Cells** group, and click the **arrow on the Insert button**, not the button face.
4. Click **Insert Sheet Rows** or **Insert Sheet Columns**.
5. To delete, select the whole rows or columns, go to the **Home** tab, **Cells** group, click the **arrow on the Delete button**, and click **Delete Sheet Rows** or **Delete Sheet Columns**.
6. New rows inherit the formatting of the row above. If the task wants them clean, click the **Insert Options** paintbrush that appears next to the insertion and choose **Clear Formatting**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.1.3 -->

**Ruta de examen**

1. Decide cuántas filas o columnas hacen falta. Excel inserta exactamente tantas como estén seleccionadas.
2. Selecciona esa cantidad de **filas completas** arrastrando hacia abajo sobre los encabezados de fila, o esa cantidad de **columnas completas** arrastrando a lo ancho sobre los encabezados de columna. Para insertar tres filas arriba de la fila 5, selecciona las filas 5, 6 y 7.
3. Ve a la pestaña **Inicio**, grupo **Celdas**, y haz clic en la **flecha del botón Insertar**, no en el botón mismo.
4. Haz clic en **Insertar filas de hoja** o en **Insertar columnas de hoja**.
5. Para eliminar, selecciona las filas o columnas completas, ve a la pestaña **Inicio**, grupo **Celdas**, haz clic en la **flecha del botón Eliminar** y haz clic en **[Delete Sheet Rows]** o **[Delete Sheet Columns]**.
6. Las filas nuevas heredan el formato de la fila de arriba. Si la tarea las quiere limpias, haz clic en el pincel **[Insert Options]** que aparece junto a la inserción y elige **[Clear Formatting]**.

<!-- ES-FIN MO200-2.1.3 -->

---

### 2.1.4 Insert and delete cells

**EN · texto fuente, no editar**

**Exam route**

1. Select a **range of cells**, not whole rows and not whole columns. That is what separates 2.1.4 from 2.1.3.
2. Go to the **Home** tab, **Cells** group, and click the **arrow on the Insert button**.
3. Click **Insert Cells...**. The **Insert** dialog opens.
4. Select **Shift cells right**, **Shift cells down**, **Entire row** or **Entire column**.
5. Click **OK**.
6. To delete, select the range, go to the **Home** tab, **Cells** group, click the **arrow on the Delete button**, and click **Delete Cells...**. The **Delete** dialog opens.
7. Select **Shift cells left**, **Shift cells up**, **Entire row** or **Entire column**.
8. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.1.4 -->

**Ruta de examen**

1. Selecciona un **rango de celdas**, no filas completas ni columnas completas. Eso es lo que separa el 2.1.4 del 2.1.3.
2. Ve a la pestaña **Inicio**, grupo **Celdas**, y haz clic en la **flecha del botón Insertar**.
3. Haz clic en **[Insert Cells...]**. Se abre el cuadro de diálogo **Insertar**.
4. Selecciona **[Shift cells right]**, **[Shift cells down]**, **Toda la fila** o **Toda la columna**.
5. Haz clic en **Aceptar**.
6. Para eliminar, selecciona el rango, ve a la pestaña **Inicio**, grupo **Celdas**, haz clic en la **flecha del botón Eliminar** y haz clic en **Eliminar celdas...**. Se abre el cuadro de diálogo **Eliminar**.
7. Selecciona **Desplazar las celdas hacia la izquierda**, **Desplazar las celdas hacia arriba**, **Toda la fila** o **Toda la columna**.
8. Haz clic en **Aceptar**.

<!-- ES-FIN MO200-2.1.4 -->

---

### 2.2.1 Merge and unmerge cells

**EN · texto fuente, no editar**

**Exam route**

1. Select the range to merge. Only the **top left** cell keeps its value; everything else is discarded.
2. Go to the **Home** tab, **Alignment** group, and click the **arrow on Merge & Center**, not the button face. The **Merge** menu opens.
3. Click the one the task names:
   - **Merge & Center** merges the whole selection into one cell and centres the content.
   - **Merge Across** merges each row of the selection separately, so a three-row selection gives three merged cells, not one.
   - **Merge Cells** merges into one cell and leaves the alignment alone.
4. If Excel warns that merging keeps only the upper left value, read the warning before clicking **OK**.
5. To unmerge, select the merged cell, click the **arrow on Merge & Center**, and click **Unmerge Cells**.

The dialog route, worth knowing because it combines with 2.2.6: select the range, press **Ctrl+1**, go to the **Alignment** tab, select the **Merge cells** check box in the **Text control** section, set Horizontal and Vertical in the same visit, and click **OK**. Clearing that same check box unmerges. One operation instead of three.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.1 -->

**Ruta de examen**

1. Selecciona el rango que vas a combinar. Solo la celda **superior izquierda** conserva su valor; todo lo demás se descarta.
2. Ve a la pestaña **Inicio**, grupo **Alineación**, y haz clic en la **flecha de Combinar y centrar**, no en el botón mismo. Se abre el menú **[Merge]**.
3. Haz clic en la opción que nombra la tarea:
   - **Combinar y centrar** une toda la selección en una sola celda y centra el contenido.
   - **[Merge Across]** combina cada fila de la selección por separado, así que una selección de tres filas da tres celdas combinadas, no una.
   - **Combinar celdas** une en una sola celda y deja la alineación como estaba.
4. Si Excel avisa que al combinar solo se conserva el valor superior izquierdo, lee el aviso antes de hacer clic en **Aceptar**.
5. Para separar, selecciona la celda combinada, haz clic en la **flecha de Combinar y centrar** y haz clic en **[Unmerge Cells]**.

La ruta por cuadro de diálogo, que conviene conocer porque se combina con el 2.2.6: selecciona el rango, presiona **Ctrl+1**, ve a la pestaña **Alineación**, selecciona la casilla **Combinar celdas** de la sección **Control del texto**, define Horizontal y Vertical en la misma pasada y haz clic en **Aceptar**. Al desmarcar esa misma casilla, las celdas se separan. Una operación en lugar de tres.

<!-- ES-FIN MO200-2.2.1 -->

---

### 2.2.2 Modify cell alignment, orientation, and indentation

**EN · texto fuente, no editar**

Certiport bundles three sub-skills into one objective, and only one place in Excel holds all three. That place is the graded route.

**Exam route**

1. Select the range.
2. Press **Ctrl+1**, or go to the **Home** tab, **Alignment** group, and click the dialog box launcher. **Format Cells** opens on the **Alignment** tab.
3. In the **Text alignment** section, open the **Horizontal** list and pick from **General**, **Left (Indent)**, **Center**, **Right (Indent)**, **Fill**, **Justify**, **Center Across Selection**, **Distributed (Indent)**.
4. Open the **Vertical** list and pick from **Top**, **Center**, **Bottom**, **Justify**, **Distributed**.
5. Set the **Indent** spin box. It is only enabled when Horizontal is Left (Indent), Right (Indent) or Distributed (Indent), so set Horizontal first.
6. In the **Orientation** section on the right, either drag the red diamond marker on the half dial or type the angle into the **Degrees** box. The range is -90 to 90. For stacked letters running down the cell, click the tall narrow box that reads **Text** vertically, to the left of the dial.
7. Set anything else the task asks for while the dialog is open: **Wrap text**, **Shrink to fit**, **Merge cells** in the **Text control** section.
8. Click **OK**. All of it lands as one operation.

**Center Across Selection** is worth naming out loud. It centres a title over several columns and looks exactly like Merge & Center, and it does not merge, so sorting and filtering still work. Exam items that say "centre the title across A1:F1 without merging" want this list entry.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.2 -->

Certiport junta tres subhabilidades en un solo objetivo, y en Excel hay un solo lugar que tiene las tres. Ese lugar es la ruta que se califica.

**Ruta de examen**

1. Selecciona el rango.
2. Presiona **Ctrl+1**, o ve a la pestaña **Inicio**, grupo **Alineación**, y haz clic en el [dialog box launcher]. **Formato de celdas** se abre en la pestaña **Alineación**.
3. En la sección **Alineación del texto**, abre la lista **Horizontal** y elige entre **General**, **[Left (Indent)]**, **Centrar**, **[Right (Indent)]**, **Rellenar**, **[Justify]**, **[Center Across Selection]**, **[Distributed (Indent)]**.
4. Abre la lista **Vertical** y elige entre **[Top]**, **Centrar**, **[Bottom]**, **[Justify]**, **[Distributed]**.
5. Ajusta el control **Sangría**. Solo se habilita cuando Horizontal está en [Left (Indent)], [Right (Indent)] o [Distributed (Indent)], así que define Horizontal primero.
6. En la sección **Orientación**, del lado derecho, arrastra el rombo rojo del semicírculo o escribe el ángulo en el cuadro **Grados**. El rango va de -90 a 90. Para las letras apiladas que bajan por la celda, haz clic en el cuadro alto y angosto que dice **Texto** en vertical, a la izquierda del semicírculo.
7. Define lo demás que pida la tarea mientras el cuadro de diálogo sigue abierto: **Ajustar texto**, **Reducir hasta ajustar**, **Combinar celdas** en la sección **Control del texto**.
8. Haz clic en **Aceptar**. Todo eso entra como una sola operación.

**[Center Across Selection]** merece mención aparte. Centra un título sobre varias columnas y se ve igualito que Combinar y centrar, y no combina, así que ordenar y filtrar siguen funcionando. Los reactivos que dicen "centra el título en A1:F1 sin combinar" quieren esta entrada de la lista.

<!-- ES-FIN MO200-2.2.2 -->

---

### 2.2.3 Format cells by using Format Painter

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell or range that already carries the formatting to be copied. One cell is enough if the format is uniform.
2. Go to the **Home** tab, **Clipboard** group, and click **Format Painter**. The pointer gains a paintbrush and the source picks up a marching border.
3. Drag across the destination range, or click its top left cell. The formatting transfers; values, formulas and comments do not.
4. The brush switches itself off after one use.

For several destinations that are not next to each other:

5. Select the source.
6. **Double-click** Format Painter. The brush locks on.
7. Drag over each destination in turn. The brush stays armed between them.
8. Press **Esc**, or click Format Painter again, to release it.

The double-click is the part the exam is looking for whenever the task names more than one target area.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.3 -->

**Ruta de examen**

1. Selecciona la celda o el rango que ya trae el formato que se va a copiar. Basta con una celda si el formato es uniforme.
2. Ve a la pestaña **Inicio**, grupo **Portapapeles**, y haz clic en **Copiar formato**. El puntero se convierte en brocha y el origen queda con un borde punteado en movimiento.
3. Arrastra sobre el rango de destino, o haz clic en su celda superior izquierda. El formato se transfiere; los valores, las fórmulas y los comentarios no.
4. La brocha se apaga sola después de un uso.

Para varios destinos que no están juntos:

5. Selecciona el origen.
6. Haz **doble clic** en Copiar formato. La brocha se queda fija.
7. Arrastra sobre cada destino por turno. La brocha sigue activa entre uno y otro.
8. Presiona **Esc**, o haz clic otra vez en Copiar formato, para soltarla.

El doble clic es lo que el examen busca cuando la tarea nombra más de una zona de destino.

<!-- ES-FIN MO200-2.2.3 -->

---

### 2.2.4 Wrap text within cells

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell or range.
2. Press **Ctrl+1**, or go to the **Home** tab, **Alignment** group, and click the dialog box launcher.
3. Click the **Alignment** tab if it is not already in front.
4. In the **Text control** section, select the **Wrap text** check box.
5. While the dialog is open, set anything else the task pairs with it: **Vertical** to **Top** so wrapped lines start at the top of the cell, **Horizontal**, **Shrink to fit** if the task wants shrinking instead of wrapping, **Merge cells**.
6. Click **OK**.

**Shrink to fit** and **Wrap text** are mutually exclusive; selecting one clears the other. Tasks that say "make the text fit without changing the row height" want Shrink to fit, not Wrap text.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.4 -->

**Ruta de examen**

1. Selecciona la celda o el rango.
2. Presiona **Ctrl+1**, o ve a la pestaña **Inicio**, grupo **Alineación**, y haz clic en el [dialog box launcher].
3. Haz clic en la pestaña **Alineación** si no está ya al frente.
4. En la sección **Control del texto**, selecciona la casilla **Ajustar texto**.
5. Con el cuadro de diálogo abierto, define lo demás que la tarea pida junto con eso: **Vertical** en **[Top]** para que el texto ajustado empiece en la parte de arriba de la celda, **Horizontal**, **Reducir hasta ajustar** si la tarea quiere encoger en lugar de ajustar, **Combinar celdas**.
6. Haz clic en **Aceptar**.

**Reducir hasta ajustar** y **Ajustar texto** se excluyen entre sí; al seleccionar uno se desmarca el otro. Las tareas que dicen "haz que el texto quepa sin cambiar el alto de la fila" quieren Reducir hasta ajustar, no Ajustar texto.

<!-- ES-FIN MO200-2.2.4 -->

---

### 2.2.5 Apply number formats

**EN · texto fuente, no editar**

This objective is the ribbon one on purpose. Certiport separates it from 2.2.6 precisely so that one item tests the Number group and the other tests the dialog. Do not answer this one from Format Cells unless the task says so.

**Exam route**

1. Select the range. Select the numbers only, not the header.
2. Go to the **Home** tab, **Number** group.
3. Open the **Number Format** list at the top of the group. It reads **General** by default.
4. Pick the format: **General**, **Number**, **Currency**, **Accounting**, **Short Date**, **Long Date**, **Time**, **Percentage**, **Fraction**, **Scientific**, **Text**.
5. Adjust with the buttons underneath: **Accounting Number Format** with its arrow for the currency symbol, **Percent Style**, **Comma Style**, **Increase Decimal**, **Decrease Decimal**.
6. If the task names decimal places, click Increase Decimal or Decrease Decimal until the count is right rather than retyping the numbers.

**Currency** and **Accounting** are not the same and the exam knows it. Currency puts the symbol tight against the digits and shows negatives in the style chosen in the dialog. Accounting lines the symbols up on the left edge of the cell, lines the decimal points up, shows zero as a dash, and puts negatives in parentheses.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.5 -->

Este objetivo es el de la cinta, a propósito. Certiport lo separa del 2.2.6 justo para que un reactivo evalúe el grupo Número y el otro evalúe el cuadro de diálogo. No resuelvas este objetivo desde Formato de celdas a menos que la tarea lo diga.

**Ruta de examen**

1. Selecciona el rango. Selecciona solo los números, no el encabezado.
2. Ve a la pestaña **Inicio**, grupo **Número**.
3. Abre la lista **Formato de número** de la parte de arriba del grupo. Por defecto dice **General**.
4. Elige el formato: **General**, **Número**, **Moneda**, **Contabilidad**, **[Short Date]**, **[Long Date]**, **[Time]**, **Porcentaje**, **[Fraction]**, **[Scientific]**, **Texto**.
5. Ajusta con los botones de abajo: **[Accounting Number Format]** con su flecha para el símbolo de moneda, **[Percent Style]**, **[Comma Style]**, **Aumentar decimales**, **[Decrease Decimal]**.
6. Si la tarea nombra posiciones decimales, haz clic en Aumentar decimales o en [Decrease Decimal] hasta que la cuenta quede bien, en lugar de reescribir los números.

**Moneda** y **Contabilidad** no son lo mismo y el examen lo sabe. Moneda pega el símbolo a los dígitos y muestra los negativos con el estilo que se haya elegido en el cuadro de diálogo. Contabilidad alinea los símbolos en el borde izquierdo de la celda, alinea los puntos decimales, muestra el cero como un guion y pone los negativos entre paréntesis.

<!-- ES-FIN MO200-2.2.5 -->

---

### 2.2.6 Apply cell formats from the Format Cells dialog box

**EN · texto fuente, no editar**

This is the objective the whole document is built around, and this is where the dialog is written out in full. Certiport lists it separately from 2.2.5 for one reason: the result is reachable two ways and only one of them is graded. The dialog is a single operation across six tabs. The ribbon is one operation per button. Same picture, different route, different score.

**Exam route**

1. Select the cell or range.
2. Press **Ctrl+1**. With the mouse, go to the **Home** tab and click the dialog box launcher of the group you need, the small diagonal arrow in the bottom right corner of the **Font**, **Alignment** or **Number** group. All three open the same **Format Cells** dialog, only on a different tab.
3. The dialog has six tabs across the top: **Number**, **Alignment**, **Font**, **Border**, **Fill**, **Protection**.
4. **Font tab.** Set **Font**, **Font style** (Regular, Italic, Bold, Bold Italic), **Size**. Open the **Underline** list for **None**, **Single**, **Double**, **Single Accounting**, **Double Accounting**. Open the **Color** list and pick the font colour, or click **More Colors...** for one that is not on the palette. The **Effects** check boxes are **Strikethrough**, **Superscript**, **Subscript**.
5. **Do not click OK.** Click the **Fill** tab.
6. **Fill tab.** Click a swatch under **Background Color**. **No Color** removes a fill. **Fill Effects...** builds a gradient with two colours and a shading style. **More Colors...** opens the Standard and Custom colour picker. **Pattern Color** and **Pattern Style** add a hatch on top of the background. The **Sample** box previews the result.
7. Still without closing, click the **Border** tab if borders are also asked for. **Order matters on this tab and it is the most common way to lose the item.** Choose the **Style** from the Line box and the **Color** from the Color list **first**, then click a **Presets** button (**None**, **Outline**, **Inside**) or click the individual edges in the **Border** preview box. A border drawn before the style is set comes out in the previous style, and clicking the style afterwards does nothing to it.
8. Click the **Number** tab if a number format is also asked for. Pick from the **Category** list: **General**, **Number**, **Currency**, **Accounting**, **Date**, **Time**, **Percentage**, **Fraction**, **Scientific**, **Text**, **Special**, **Custom**. Then set the options on the right, which change per category: **Decimal places**, **Use 1000 Separator (,)**, **Negative numbers**, **Symbol**, or the **Type** box for **Custom**.
9. Click the **Alignment** tab for **Horizontal**, **Vertical**, **Indent**, **Orientation** and the **Text control** check boxes.
10. Click the **Protection** tab for the **Locked** and **Hidden** check boxes, which do nothing until the sheet is protected. Expert 1.2.2 is the objective that uses them.
11. Click **OK** once. Every tab that was touched is applied in a single operation.

**Why the route is the whole point.** Do it from the dialog and one press of **Ctrl+Z** takes back the font colour and the fill together. Do it from the ribbon and it takes two presses. That single undo is the visible proof of which route was taken, and it is the fastest way to check yourself in the exam.

**What the ribbon simply cannot reach.** Single Accounting and Double Accounting underline. Shrink to fit. Diagonal borders. Pattern fills and gradient fills. The **Special** and **Custom** number categories. The **Protection** tab. Negative numbers in red parentheses. If a task names any of these, there is no short route to fall back on.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.6 -->

Este es el objetivo sobre el que está construido todo el documento, y aquí es donde el cuadro de diálogo queda escrito completo. Certiport lo lista aparte del 2.2.5 por una razón: al resultado se llega por dos caminos y solo uno se califica. El cuadro de diálogo es una sola operación repartida en seis pestañas. La cinta es una operación por botón. Misma imagen, distinta ruta, distinta calificación.

**Ruta de examen**

1. Selecciona la celda o el rango.
2. Presiona **Ctrl+1**. Con el mouse, ve a la pestaña **Inicio** y haz clic en el [dialog box launcher] del grupo que necesites, la flecha diagonal pequeña de la esquina inferior derecha del grupo **Fuente**, **Alineación** o **Número**. Los tres abren el mismo cuadro de diálogo **Formato de celdas**, nada más que en una pestaña distinta.
3. El cuadro de diálogo tiene seis pestañas arriba: **Número**, **Alineación**, **Fuente**, **Borde**, **Relleno**, **Protección**.
4. **Pestaña Fuente.** Define **Fuente**, **Estilo** (Normal, K, N, Negrita Cursiva) y **Tamaño**. Abre la lista **Subrayado** para **Ninguno**, **[Single]**, **[Double]**, **[Single Accounting]**, **[Double Accounting]**. Abre la lista **Color** y elige el color de letra, o haz clic en **[More Colors...]** para uno que no esté en la paleta. Las casillas de **Efectos** son **Tachado**, **Superíndice** y **Subíndice**.
5. **No hagas clic en Aceptar.** Haz clic en la pestaña **Relleno**.
6. **Pestaña Relleno.** Haz clic en una muestra de **[Background Color]**. **Sin color** quita el relleno. **[Fill Effects...]** arma un degradado con dos colores y un estilo de sombreado. **[More Colors...]** abre el selector de color, con sus pestañas [Standard] y Personalizada. **[Pattern Color]** y **[Pattern Style]** ponen una trama encima del fondo. El cuadro **[Sample]** muestra la vista previa del resultado.
7. Todavía sin cerrar el cuadro de diálogo, haz clic en la pestaña **Borde** si también piden bordes. **En esta pestaña el orden importa y es la forma más común de perder el reactivo.** Elige **primero** el **Estilo** en el cuadro de línea y el **Color** en la lista de color, y después haz clic en un botón de **[Presets]** (**Ninguno**, **Esquema**, **[Inside]**) o haz clic en cada borde dentro del cuadro de vista previa **Borde**. Un borde dibujado antes de definir el estilo sale con el estilo anterior, y hacer clic en el estilo después no le hace nada.
8. Haz clic en la pestaña **Número** si también piden un formato de número. Elige de la lista **Categoría**: **General**, **Número**, **Moneda**, **Contabilidad**, **Fecha**, **[Time]**, **Porcentaje**, **[Fraction]**, **[Scientific]**, **Texto**, **[Special]**, **Personalizada**. Luego define las opciones de la derecha, que cambian según la categoría: **Posiciones decimales**, **[Use 1000 Separator (,)]**, **[Negative numbers]**, **[Symbol]**, o el cuadro **Tipo** para **Personalizada**.
9. Haz clic en la pestaña **Alineación** para **Horizontal**, **Vertical**, **Sangría**, **Orientación** y las casillas de **Control del texto**.
10. Haz clic en la pestaña **Protección** para las casillas **Bloqueada** y **Oculta**, que no hacen nada hasta que la hoja esté protegida. El objetivo que las usa es el Expert 1.2.2.
11. Haz clic en **Aceptar** una sola vez. Todas las pestañas que hayas tocado se aplican en una sola operación.

**Por qué la ruta lo es todo.** Hazlo desde el cuadro de diálogo y una sola presión de **Ctrl+Z** deshace el color de letra y el relleno juntos. Hazlo desde la cinta y hacen falta dos. Ese deshacer único es la prueba visible de qué ruta se tomó, y es la forma más rápida de revisarte a ti mismo en el examen.

**Lo que la cinta simplemente no alcanza.** El subrayado [Single Accounting] y [Double Accounting]. Reducir hasta ajustar. Los bordes diagonales. Los rellenos de trama y los rellenos con degradado. Las categorías de número **[Special]** y **Personalizada**. La pestaña **Protección**. Los números negativos en rojo y entre paréntesis. Si una tarea nombra cualquiera de estas, no hay ruta corta a la que recurrir.

<!-- ES-FIN MO200-2.2.6 -->

---

### 2.2.7 Apply cell styles

**EN · texto fuente, no editar**

**Exam route**

1. Select the range.
2. Go to the **Home** tab, **Styles** group, and click **Cell Styles**.
3. The gallery opens in sections: **Good, Bad and Neutral**; **Data and Model**; **Titles and Headings**; **Themed Cell Styles**; **Number Format**.
4. Hover over a style to live-preview it on the selection.
5. Click the style. The task will name it, **Heading 1**, **Total**, **Input**, **Currency [0]**.

To change a style everywhere it is used:

6. Open **Cell Styles**, right-click the style, and click **Modify...**. The **Style** dialog opens.
7. Click **Format...**, which opens **Format Cells** (2.2.6). Change what is needed, click **OK**, click **OK** again. Every cell carrying that style updates at once.

To build one:

8. Open **Cell Styles** and click **New Cell Style...** at the bottom. The **Style** dialog opens.
9. Type a name in **Style name**.
10. Clear any of the **Style Includes** check boxes the style must not carry: **Number**, **Alignment**, **Font**, **Border**, **Fill**, **Protection**.
11. Click **Format...**, set the formats, click **OK**, click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.7 -->

**Ruta de examen**

1. Selecciona el rango.
2. Ve a la pestaña **Inicio**, grupo **Estilos**, y haz clic en **Estilos de celda**.
3. La galería se abre en secciones: **Bueno, malo y neutral**; **Datos y modelo**; **Títulos y encabezados**; **Estilos de celda temáticos**; **Formato de número**.
4. Pasa el puntero sobre un estilo para verlo en vista previa sobre la selección.
5. Haz clic en el estilo. La tarea lo va a nombrar: **Encabez**, **Total**, **Entrada**, **[Currency [0]]**.

Para cambiar un estilo en todos los lugares donde se usa:

6. Abre **Estilos de celda**, haz clic derecho en el estilo y haz clic en **[Modify...]**. Se abre el cuadro de diálogo **Estilo**.
7. Haz clic en **Formato...**, que abre **Formato de celdas** (2.2.6). Cambia lo que haga falta, haz clic en **Aceptar** y vuelve a hacer clic en **Aceptar**. Todas las celdas que traigan ese estilo se actualizan de golpe.

Para crear uno:

8. Abre **Estilos de celda** y haz clic hasta abajo en **[New Cell Style...]**. Se abre el cuadro de diálogo **Estilo**.
9. Escribe un nombre en **[Style name]**.
10. Desmarca las casillas de **[Style Includes]** que el estilo no deba cargar: **Número**, **Alineación**, **Fuente**, **Borde**, **Relleno**, **Protección**.
11. Haz clic en **Formato...**, define los formatos, haz clic en **Aceptar** y haz clic en **Aceptar**.

<!-- ES-FIN MO200-2.2.7 -->

---

### 2.2.8 Clear cell formatting

**EN · texto fuente, no editar**

**Exam route**

1. Select the range.
2. Go to the **Home** tab, **Editing** group, and click **Clear**, the eraser icon on the right of the group.
3. The menu offers **Clear All**, **Clear Formats**, **Clear Contents**, **Clear Comments and Notes**, **Clear Hyperlinks**, **Remove Hyperlinks**.
4. Click **Clear Formats**. Formatting goes, values stay.
5. Click **Clear All** only when the task wants the cells emptied of everything: values, formats, comments and conditional formatting rules.

Know which one does what before clicking. **Clear Contents** removes the values and keeps the formatting, which is the exact opposite of **Clear Formats**, and the two sit next to each other on the same short menu.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.2.8 -->

**Ruta de examen**

1. Selecciona el rango.
2. Ve a la pestaña **Inicio**, grupo **Edición**, y haz clic en **Borrar**, el icono de borrador que está a la derecha del grupo.
3. El menú ofrece **Borrar todo**, **Borrar formatos**, **Borrar contenido**, **Borrar comentarios y notas**, **Borrar hipervínculos**, **Quitar hipervínculos**.
4. Haz clic en **Borrar formatos**. El formato se va, los valores se quedan.
5. Haz clic en **Borrar todo** solo cuando la tarea quiera las celdas vacías de todo: valores, formatos, comentarios y reglas de formato condicional.

Ten claro cuál hace qué antes de hacer clic. **Borrar contenido** quita los valores y conserva el formato, que es exactamente lo contrario de **Borrar formatos**, y los dos están uno junto al otro en el mismo menú corto.

<!-- ES-FIN MO200-2.2.8 -->

---

### 2.3.1 Define a named range

**EN · texto fuente, no editar**

This is the first appearance of the **New Name** dialog and the **Name Manager**; 1.2.2, 4.1.2 and Expert 1.1.2 all refer back here.

**Exam route**

1. Select the range to be named.
2. Go to the **Formulas** tab, **Defined Names** group, and click **Define Name**.
3. The **New Name** dialog opens.
4. In the **Name** box, type the name. It must start with a letter, an underscore or a backslash. No spaces, use an underscore. It cannot be a cell address such as `A1` or `R1C1`, and it cannot be a single letter `C` or `R`. Excel is not case sensitive here, so `Sales` and `sales` are the same name.
5. Open the **Scope** list and pick **Workbook**, so the name works from any sheet, or a specific sheet name, so it works only there. The task will say which.
6. Type into the **Comment** box if the task asks for a description.
7. Check the **Refers to** box. It must hold an absolute reference such as `=Sheet1!$A$1:$A$20`. To reselect on the sheet, click the small collapse arrow at the right of the box, drag the range, and click the arrow again.
8. Click **OK**.

To name several ranges at once from their headers:

9. Select the block including its header row or label column.
10. Go to the **Formulas** tab, **Defined Names** group, and click **Create from Selection**.
11. In the **Create Names from Selection** dialog, select **Top row**, **Left column**, **Bottom row** or **Right column**.
12. Click **OK**. Spaces in the headers become underscores automatically.

To edit or delete:

13. Go to the **Formulas** tab, **Defined Names** group, and click **Name Manager**. Use **New...**, **Edit...**, **Delete**, and the **Filter** button. The **Refers to** box sits at the bottom with its own tick and cross. Close with **Close**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.3.1 -->

Aquí aparecen por primera vez el cuadro de diálogo **[New Name]** y el **Administrador de nombres**; el 1.2.2, el 4.1.2 y el Expert 1.1.2 remiten a esta entrada.

**Ruta de examen**

1. Selecciona el rango que vas a nombrar.
2. Ve a la pestaña **Fórmulas**, grupo **Nombres definidos**, y haz clic en **Asignar nombre**.
3. Se abre el cuadro de diálogo **[New Name]**.
4. En el cuadro **Nombre**, escribe el nombre. Tiene que empezar con una letra, un guion bajo o una barra invertida. Sin espacios, usa un guion bajo. No puede ser una dirección de celda como `A1` o `R1C1`, y no puede ser una sola letra `C` ni `R`. [Estos dos literales cambian en el Excel en español: el estilo de referencia se llama F1C1 y las letras reservadas serían F y C. Confirmar contra el producto antes de que esto llegue al grupo.] Aquí Excel no distingue mayúsculas de minúsculas, así que `Sales` y `sales` son el mismo nombre.
5. Abre la lista **Ámbito** y elige **Libro**, para que el nombre sirva desde cualquier hoja, o el nombre de una hoja específica, para que sirva solo ahí. La tarea va a decir cuál.
6. Escribe en el cuadro **Comentario** si la tarea pide una descripción.
7. Revisa el cuadro **Se refiere a**. Tiene que traer una referencia absoluta como `=Sheet1!$A$1:$A$20` [en el Excel en español la hoja se llama Hoja1: confirmar]. Para volver a seleccionar sobre la hoja, haz clic en la flecha pequeña de contraer que está a la derecha del cuadro, arrastra el rango y haz clic otra vez en la flecha.
8. Haz clic en **Aceptar**.

Para nombrar varios rangos de una sola vez a partir de sus encabezados:

9. Selecciona el bloque incluyendo su fila de encabezados o su columna de etiquetas.
10. Ve a la pestaña **Fórmulas**, grupo **Nombres definidos**, y haz clic en **Crear desde la selección**.
11. En el cuadro de diálogo **[Create Names from Selection]**, selecciona **[Top row]**, **[Left column]**, **[Bottom row]** o **[Right column]**.
12. Haz clic en **Aceptar**. Los espacios de los encabezados se vuelven guiones bajos automáticamente.

Para editar o eliminar:

13. Ve a la pestaña **Fórmulas**, grupo **Nombres definidos**, y haz clic en **Administrador de nombres**. Usa **[New...]**, **[Edit...]**, **Eliminar** y el botón **Filtro**. El cuadro **Se refiere a** está hasta abajo con su propia palomita y su propia tacha. Ciérralo con **Cerrar**.

<!-- ES-FIN MO200-2.3.1 -->

---

### 2.3.2 Name a table

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the table. A table is a range converted with **Format as Table** or **Insert > Table** (3.1.1), and it shows filter arrows in its header row.
2. The **Table Design** contextual tab appears at the right end of the ribbon. Click it.
3. Look at the **Properties** group, the leftmost group on that tab. It holds a box labelled **Table Name:**.
4. Click in the box and select the whole of the existing name. Excel names tables `Table1`, `Table2` and so on.
5. Type the new name. The rules are the same as for a defined name: start with a letter or an underscore, no spaces, not a cell address, and unique across the whole workbook.
6. Press **Enter**. Nothing is committed until Enter is pressed; clicking away can discard it.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.3.2 -->

**Ruta de examen**

1. Haz clic en cualquier celda dentro de la tabla. Una tabla es un rango convertido con **Dar formato como tabla** o con **Insertar > Tabla** (3.1.1), y muestra flechas de filtro en su fila de encabezados.
2. La pestaña contextual **Diseño de tabla** aparece en el extremo derecho de la cinta de opciones. Haz clic en ella.
3. Mira el grupo **Propiedades**, el grupo que está más a la izquierda de esa pestaña. Ahí hay un cuadro con la etiqueta **Nombre de la tabla:**.
4. Haz clic en el cuadro y selecciona todo el nombre que ya tiene. Excel nombra las tablas `Table1`, `Table2` y así. [En el Excel en español son Tabla1, Tabla2: confirmar.]
5. Escribe el nombre nuevo. Las reglas son las mismas que para un nombre definido: empezar con letra o guion bajo, sin espacios, que no sea una dirección de celda y que sea único en todo el libro.
6. Presiona **Enter**. Nada queda confirmado hasta presionar Enter; hacer clic en otro lado puede descartarlo.

<!-- ES-FIN MO200-2.3.2 -->

---

### 2.4.1 Insert Sparklines

**EN · texto fuente, no editar**

**Exam route**

1. Select the cells that will **hold** the sparklines, one cell per row of data. Usually the empty column to the right of the data.
2. Go to the **Insert** tab, **Sparklines** group.
3. Click **Line**, **Column** or **Win/Loss**, whichever the task names.
4. The **Create Sparklines** dialog opens with two boxes.
5. In **Data Range:**, drag over the numbers on the sheet, or type the reference. Select the data only; headers and totals break the scale.
6. Check **Location Range:**. It is already filled with the cells selected in step 1, and it must have the same number of rows as the Data Range.
7. Click **OK**.

Formatting, on the **Sparkline** contextual tab that appears once a sparkline cell is selected. In Office 2019 the same tab is called **Sparkline Tools > Design**.

8. **Show** group: select **High Point**, **Low Point**, **Negative Points**, **First Point**, **Last Point**, **Markers**. Markers is available for Line sparklines only.
9. **Style** group: pick from the gallery, or set **Sparkline Color** and **Marker Color**.
10. **Group** group: click **Axis** for **Show Axis** and for the **Minimum Value Options** and **Maximum Value Options**, where **Same for All Sparklines** puts every row on one common scale. Without it, each row is scaled to itself and the rows cannot be compared, which is what most tasks are really testing.
11. **Group** and **Ungroup** tie the sparklines together or break them apart. **Clear** removes them, with **Clear Selected Sparklines** and **Clear Selected Sparkline Groups**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.4.1 -->

**Ruta de examen**

1. Selecciona las celdas que van a **contener** los minigráficos, una celda por cada fila de datos. Normalmente la columna vacía que está a la derecha de los datos.
2. Ve a la pestaña **Insertar**, grupo **Minigráficos**.
3. Haz clic en **Línea**, **Columna** o **Pérdidas y ganancias**, el que nombre la tarea.
4. Se abre el cuadro de diálogo **Crear Minigráficos** con dos cuadros.
5. En **[Data Range:]**, arrastra sobre los números de la hoja o escribe la referencia. Selecciona solo los datos; los encabezados y los totales rompen la escala.
6. Revisa **[Location Range:]**. Ya viene lleno con las celdas seleccionadas en el paso 1, y tiene que tener el mismo número de filas que Rango de datos.
7. Haz clic en **Aceptar**.

El formato se da en la pestaña contextual **Minigráfico**, que aparece en cuanto se selecciona una celda con minigráfico. En Office 2019 esa misma pestaña se llama **[Sparkline Tools > Design]**.

8. Grupo **Mostrar**: selecciona **Punto alto**, **Punto bajo**, **Puntos negativos**, **Primer punto**, **Último punto**, **Marcadores**. Marcadores solo está disponible para los minigráficos de Línea.
9. Grupo **Estilo**: elige de la galería, o define **[Sparkline Color]** y **[Marker Color]**.
10. Grupo **Agrupar**: haz clic en **[Axis]** para **[Show Axis]** y para las **[Minimum Value Options]** y **[Maximum Value Options]**, donde **[Same for All Sparklines]** pone todas las filas en una escala común. Sin eso, cada fila se escala consigo misma y las filas no se pueden comparar, que es lo que en realidad evalúan casi todas las tareas.
11. **Agrupar** y **Desagrupar** amarran los minigráficos entre sí o los separan. **Borrar** los quita, con **[Clear Selected Sparklines]** y **[Clear Selected Sparkline Groups]**.

<!-- ES-FIN MO200-2.4.1 -->

---

### 2.4.2 Apply built-in conditional formatting

**EN · texto fuente, no editar**

**Exam route**

1. Select the range the rule applies to. Data cells only. Including the header row is the most common cause of a rule that formats the wrong cells, because a text header counts as smaller than every number.
2. Go to the **Home** tab, **Styles** group, and click **Conditional Formatting**.
3. The menu holds **Highlight Cells Rules**, **Top/Bottom Rules**, **Data Bars**, **Color Scales**, **Icon Sets**, **New Rule...**, **Clear Rules**, **Manage Rules...**. The last three belong to Expert 2.3.1, 2.4.3 and Expert 2.3.4 respectively.
4. For a threshold, point at **Highlight Cells Rules** and click **Greater Than...**, **Less Than...**, **Between...**, **Equal To...**, **Text that Contains...**, **A Date Occurring...** or **Duplicate Values...**.
5. In the small dialog, type the value in the left box, or click the collapse arrow and pick the cell that holds it. Pointing at a cell rather than typing the number is what makes the rule follow the data when the number changes.
6. Open the **with** list on the right and pick the format: **Light Red Fill with Dark Red Text**, **Yellow Fill with Dark Yellow Text**, **Green Fill with Dark Green Text**, **Light Red Fill**, **Red Text**, **Red Border**, **Custom Format...**.
7. **Custom Format...** opens **Format Cells** cut down to four tabs, **Number**, **Font**, **Border**, **Fill**. It is the same dialog as 2.2.6 minus Alignment and Protection, because a rule cannot change either.
8. Click **OK**.

For a rank rule:

9. Point at **Top/Bottom Rules** and click **Top 10 Items...**, **Top 10 %...**, **Bottom 10 Items...**, **Bottom 10 %...**, **Above Average...** or **Below Average...**. The **10** is an editable spin box, so "top 5" still starts from the Top 10 Items entry.

For a graphic rule:

10. Point at **Data Bars**, **Color Scales** or **Icon Sets**. Hover the gallery for live preview and click the variant.
11. Click **More Rules...** at the bottom of any of those three galleries to open **New Formatting Rule**, where the graded variants live: **Show Bar Only**, **Reverse Icon Order**, **Show Icon Only**, and thresholds typed as **Number**, **Percent**, **Formula** or **Percentile** instead of the automatic ones. That dialog is written out at Expert 2.3.1.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.4.2 -->

**Ruta de examen**

1. Selecciona el rango al que aplica la regla. Solo celdas de datos. Incluir la fila de encabezados es la causa más común de una regla que da formato a las celdas equivocadas, porque un encabezado de texto cuenta como menor que cualquier número.
2. Ve a la pestaña **Inicio**, grupo **Estilos**, y haz clic en **Formato condicional**.
3. El menú tiene **Resaltar reglas de celdas**, **Reglas superiores e inferiores**, **Barras de datos**, **Escalas de color**, **Conjuntos de iconos**, **Nueva regla...**, **Borrar reglas** y **Administrar reglas...**. Los últimos tres son el Expert 2.3.1, el 2.4.3 y el Expert 2.3.4 respectivamente.
4. Para un umbral, apunta a **Resaltar reglas de celdas** y haz clic en **[Greater Than...]**, **[Less Than...]**, **[Between...]**, **[Equal To...]**, **[Text that Contains...]**, **[A Date Occurring...]** o **Duplicar valores...**.
5. En el cuadro de diálogo chico, escribe el valor en el cuadro de la izquierda, o haz clic en la flecha de contraer y elige la celda que lo tiene. Apuntar a una celda en lugar de escribir el número es lo que hace que la regla siga a los datos cuando el número cambia.
6. Abre la lista **con** de la derecha y elige el formato: **Relleno rojo claro con texto rojo oscuro**, **Relleno amarillo con texto amarillo oscuro**, **Relleno verde con texto verde oscuro**, **Relleno rojo claro**, **Texto rojo**, **Borde rojo**, **[Custom Format...]**.
7. **[Custom Format...]** abre **Formato de celdas** recortado a cuatro pestañas, **Número**, **Fuente**, **Borde** y **Relleno**. Es el mismo cuadro de diálogo del 2.2.6 menos Alineación y Protección, porque una regla no puede cambiar ninguna de las dos.
8. Haz clic en **Aceptar**.

Para una regla de rango:

9. Apunta a **Reglas superiores e inferiores** y haz clic en **[Top 10 Items...]**, **[Top 10 %...]**, **[Bottom 10 Items...]**, **[Bottom 10 %...]**, **Por encima del promedio...** o **[Below Average...]**. El **10** es un control editable, así que "los 5 de arriba" también empieza desde la entrada 10 superiores.

Para una regla gráfica:

10. Apunta a **Barras de datos**, **Escalas de color** o **Conjuntos de iconos**. Pasa el puntero por la galería para la vista previa y haz clic en la variante.
11. Haz clic en **[More Rules...]** hasta abajo de cualquiera de esas tres galerías para abrir **Nueva regla de formato**, donde viven las variantes que se califican: **[Show Bar Only]**, **[Reverse Icon Order]**, **[Show Icon Only]** y los umbrales escritos como **Número**, **Porcentaje**, **Fórmula** o **[Percentile]** en lugar de los automáticos. Ese cuadro de diálogo está escrito completo en el Expert 2.3.1.

<!-- ES-FIN MO200-2.4.2 -->

---

### 2.4.3 Remove conditional formatting

**EN · texto fuente, no editar**

Certiport counts this separately from 2.4.2, because removing from a selection and removing from a whole sheet are two different commands. Read the task wording for which scope it wants before touching anything.

**Exam route**

1. If the scope is part of the sheet, select that range first. If the scope is the whole sheet, the selection does not matter.
2. Go to the **Home** tab, **Styles** group, and click **Conditional Formatting**.
3. Point at **Clear Rules**. The submenu offers **Clear Rules from Selected Cells**, **Clear Rules from Entire Sheet**, **Clear Rules from This Table**, **Clear Rules from This PivotTable**. The last two are greyed out unless the cursor is inside a table or a PivotTable.
4. Click the one the task names.

To remove one rule and leave the others alone, use the **Conditional Formatting Rules Manager**, which is written out at Expert 2.3.4. In short: **Conditional Formatting > Manage Rules...**, set **Show formatting rules for** to **This Worksheet** (it opens on **Current Selection**, which hides every rule you are not standing in), select the rule, confirm it by its description, its **Format** preview and its **Applies to** range, click **Delete Rule**, then **OK**. The same dialog is where a rule's range is trimmed instead of deleted: edit the **Applies to** box to a smaller range and the formatting leaves the cells that drop out of it while the rule survives.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-2.4.3 -->

Certiport lo cuenta aparte del 2.4.2 porque quitar de una selección y quitar de una hoja entera son dos comandos distintos. Lee la redacción de la tarea para saber qué alcance pide antes de tocar nada.

**Ruta de examen**

1. Si el alcance es una parte de la hoja, selecciona ese rango primero. Si el alcance es la hoja entera, la selección da igual.
2. Ve a la pestaña **Inicio**, grupo **Estilos**, y haz clic en **Formato condicional**.
3. Apunta a **Borrar reglas**. El submenú ofrece **[Clear Rules from Selected Cells]**, **[Clear Rules from Entire Sheet]**, **[Clear Rules from This Table]** y **[Clear Rules from This PivotTable]**. Los dos últimos están en gris a menos que el cursor esté dentro de una tabla o de una tabla dinámica.
4. Haz clic en el que nombre la tarea.

Para quitar una sola regla y dejar las demás en paz, usa el **Administrador de reglas de formato condicionales**, que está escrito completo en el Expert 2.3.4. En corto: **Formato condicional > Administrar reglas...**, pon **[Show formatting rules for]** en **[This Worksheet]** (se abre en **[Current Selection]**, que esconde todas las reglas en las que no estás parado), selecciona la regla, confírmala por su descripción, por su vista previa de **Formato** y por su rango de **[Applies to]**, haz clic en **[Delete Rule]** y luego en **Aceptar**. Ese mismo cuadro de diálogo es donde se recorta el rango de una regla en lugar de eliminarla: edita el cuadro **[Applies to]** a un rango más chico y el formato se va de las celdas que quedan fuera mientras la regla sobrevive.

<!-- ES-FIN MO200-2.4.3 -->

---

## MO-200 Associate · Domain 3, Manage tables and table data

### 3.1.1 Create Excel tables from cell ranges

**EN · texto fuente, no editar**

**Exam route**

1. Click any single cell inside the block of data. Do not select the whole range by hand yet.
2. Go to the **Insert** tab, **Tables** group, and click **Table**.
3. The **Create Table** dialog opens. Read the box under **Where is the data for your table?** and check that the address covers the header row and the last row of data. If it is wrong, drag on the sheet to reselect, or type the address.
4. Select the **My table has headers** check box. Clear it only when the first row is data, in which case Excel writes headers called Column1, Column2 and so on.
5. Click **OK**.
6. Confirm the contextual **Table Design** tab appeared on the ribbon. The table takes the default name `Table1` and the default style Blue, Table Style Medium 2, and filter buttons appear in the header row.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.1.1 -->

**Ruta de examen**

1. Haz clic en una sola celda dentro del bloque de datos. Todavía no selecciones el rango completo a mano.
2. Ve a la pestaña **Insertar**, grupo **Tablas**, y haz clic en **Tabla**.
3. Se abre el cuadro de diálogo **Crear tabla**. Lee el cuadro que está debajo de **¿Dónde están los datos de la tabla?** y comprueba que la dirección abarque la fila de encabezados y la última fila de datos. Si está mal, arrastra sobre la hoja para volver a seleccionar, o escribe la dirección.
4. Selecciona la casilla **La tabla tiene encabezados.**. Desactívala solo cuando la primera fila sea de datos, en cuyo caso Excel escribe encabezados llamados [Column1], [Column2] y así sucesivamente.
5. Haz clic en **Aceptar**.
6. Confirma que apareció la pestaña contextual **Diseño de tabla** en la cinta de opciones. La tabla toma el nombre predeterminado [`Table1`] y el estilo predeterminado [Blue, Table Style Medium 2], y aparecen botones de filtro en la fila de encabezados.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.1.1 -->

---

### 3.1.2 Apply table styles

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the table.
2. Go to the contextual **Table Design** tab.
3. In the **Table Styles** group, click the **More** arrow at the bottom right corner of the gallery to open the full gallery.
4. The gallery is split into **Light**, **Medium** and **Dark** sections. Point at a style and read the tooltip, which gives the literal name, for example "Green, Table Style Medium 7". Excel previews it live on the sheet while you hover.
5. Click the style the task names.
6. Do not leave the tab yet if the task also names style options, those are 3.2.2 and they live in the group immediately to the left.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.1.2 -->

**Ruta de examen**

1. Haz clic en cualquier celda de la tabla.
2. Ve a la pestaña contextual **Diseño de tabla**.
3. En el grupo **[Table Styles]**, haz clic en la flecha **Más** de la esquina inferior derecha de la galería para abrir la galería completa.
4. La galería está dividida en las secciones **Claro**, **Medio** y **Oscuro**. Apunta a un estilo y lee la etiqueta emergente, que da el nombre literal, por ejemplo ["Green, Table Style Medium 7"]. Excel muestra la vista previa en la hoja mientras pasas el puntero.
5. Haz clic en el estilo que pida la tarea.
6. No salgas de la pestaña todavía si la tarea también nombra opciones de estilo, esas son las del 3.2.2 y están en el grupo que está inmediatamente a la izquierda.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.1.2 -->

---

### 3.1.3 Convert tables to cell ranges

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the table.
2. Go to the **Table Design** tab, **Tools** group, and click **Convert to Range**.
3. A message box asks whether you want to convert the table to a normal range. Click **Yes**.
4. Confirm what changed: the filter buttons disappear, the **Table Design** tab disappears, and every structured reference in the workbook rewrites itself into ordinary A1 references, `=SUM(Sales[Q1])` becomes `=SUM(B2:B31)`.
5. Note what did not change: the table style stays behind as direct formatting. If the task asks for a plain range, clear it with **Home** tab, **Editing** group, **Clear**, **Clear Formats**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.1.3 -->

**Ruta de examen**

1. Haz clic en cualquier celda de la tabla.
2. Ve a la pestaña **Diseño de tabla**, grupo **[Tools]**, y haz clic en **Convertir en rango**.
3. Un cuadro de mensaje pregunta si quieres convertir la tabla en un rango normal. Haz clic en **[Yes]**.
4. Confirma lo que cambió: desaparecen los botones de filtro, desaparece la pestaña **Diseño de tabla** y todas las referencias estructuradas del libro se reescriben solas como referencias A1 normales, `=SUMA(Sales[Q1])` se convierte en `=SUMA(B2:B31)`.
5. Fíjate en lo que no cambió: el estilo de la tabla se queda ahí como formato directo. Si la tarea pide un rango sin formato, bórralo con la pestaña **Inicio**, grupo **Edición**, **Borrar**, **Borrar formatos**.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.1.3 -->

---

### 3.2.1 Add or remove table rows and columns

**EN · texto fuente, no editar**

**Exam route, insert**

1. Right-click a cell in the row or column next to where the new one goes.
2. Point to **Insert**. Inside a table the submenu offers four commands, not the worksheet ones: **Table Columns to the Left**, **Table Column to the Right**, **Table Rows Above**, **Table Row Below**.
3. Click the one the task names.
4. The new row or column joins the table: it inherits the banding, the header naming and any calculated column formula.

**Exam route, delete**

1. Right-click a cell in the row or column to remove.
2. Point to **Delete**. Inside a table the submenu offers **Table Columns** and **Table Rows**.
3. Click the one you need. The rest of the worksheet outside the table is untouched, which is the whole point of using these commands instead of the sheet ones.

**Exam route, resize the whole table at once**

1. Click any cell in the table.
2. Go to the **Table Design** tab, **Properties** group, and click **Resize Table**.
3. In the **Resize Table** dialog, under **Select the new data range for your table**, drag on the sheet or type the new address. The header row must stay in the same row.
4. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.2.1 -->

**Ruta de examen, insertar**

1. Haz clic con el botón derecho en una celda de la fila o la columna que esté junto al lugar donde va la nueva.
2. Apunta a **Insertar**. Dentro de una tabla el submenú ofrece cuatro comandos, no los de la hoja de cálculo: **[Table Columns to the Left]**, **[Table Column to the Right]**, **[Table Rows Above]**, **[Table Row Below]**.
3. Haz clic en el que pida la tarea.
4. La fila o la columna nueva se integra a la tabla: hereda las bandas, el nombre del encabezado y cualquier fórmula de columna calculada.

**Ruta de examen, eliminar**

1. Haz clic con el botón derecho en una celda de la fila o la columna que vas a quitar.
2. Apunta a **Eliminar**. Dentro de una tabla el submenú ofrece **[Table Columns]** y **[Table Rows]**.
3. Haz clic en el que necesites. El resto de la hoja de cálculo, fuera de la tabla, queda intacto, que es justo el motivo para usar estos comandos y no los de la hoja.

**Ruta de examen, cambiar el tamaño de toda la tabla de una vez**

1. Haz clic en cualquier celda de la tabla.
2. Ve a la pestaña **Diseño de tabla**, grupo **Propiedades**, y haz clic en **[Resize Table]**.
3. En el cuadro de diálogo **[Resize Table]**, debajo de **[Select the new data range for your table]**, arrastra sobre la hoja o escribe la dirección nueva. La fila de encabezados tiene que quedarse en la misma fila.
4. Haz clic en **Aceptar**.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.2.1 -->

---

### 3.2.2 Configure table style options

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the table.
2. Go to the **Table Design** tab, **Table Style Options** group.
3. The group holds seven check boxes, all of them literal: **Header Row**, **Total Row**, **Banded Rows**, **First Column**, **Last Column**, **Banded Columns**, **Filter Button**.
4. Select or clear every one the task names before you leave the group. Each is a separate graded action, and each redraws the table as you click it.
5. Read the result: **First Column** and **Last Column** bold and shade the edge columns; **Banded Rows** and **Banded Columns** stripe the body; clearing **Header Row** hides the header text and disables the filter buttons; clearing **Filter Button** keeps the header and removes only the arrows.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.2.2 -->

**Ruta de examen**

1. Haz clic en cualquier celda de la tabla.
2. Ve a la pestaña **Diseño de tabla**, grupo **Opciones de estilo de tabla**.
3. El grupo tiene siete casillas, todas literales: **Fila de encabezado**, **Fila de totales**, **Filas con bandas**, **Primera columna**, **Última columna**, **Columnas con bandas**, **Botón de filtro**.
4. Selecciona o desactiva todas las que pida la tarea antes de salir del grupo. Cada una es una acción calificada aparte, y cada una vuelve a dibujar la tabla en cuanto le das clic.
5. Lee el resultado: **Primera columna** y **Última columna** ponen en negritas y sombrean las columnas de los extremos; **Filas con bandas** y **Columnas con bandas** rayan el cuerpo; si desactivas **Fila de encabezado** se oculta el texto del encabezado y se desactivan los botones de filtro; si desactivas **Botón de filtro** el encabezado se queda y solo se quitan las flechas.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.2.2 -->

---

### 3.2.3 Insert and configure total rows

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the table.
2. Go to the **Table Design** tab, **Table Style Options** group, and select the **Total Row** check box.
3. A row appears at the bottom of the table. Its first cell reads `Total` and its last column already carries `=SUBTOTAL(109,[Q1])`, which is SUM ignoring hidden rows. Verified default behaviour.
4. Click the total cell under the column you need to total.
5. A drop-down arrow appears on the right edge of that cell. Click it.
6. Pick the function from the list: **None**, **Average**, **Count**, **Count Numbers**, **Max**, **Min**, **Sum**, **StdDev**, **Var**, **More Functions**.
7. Excel writes the matching SUBTOTAL. Average gives `=SUBTOTAL(101,[Q1])`, Sum gives `=SUBTOTAL(109,[Q1])`. Both verified in the product.
8. Repeat for every column the task names. Set **None** on a column that must stay empty.

Expert 2.2.4 is the same control seen from the other side, where the `1xx` and `9` SUBTOTAL codes matter; the difference between them is written out there.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.2.3 -->

**Ruta de examen**

1. Haz clic en cualquier celda de la tabla.
2. Ve a la pestaña **Diseño de tabla**, grupo **Opciones de estilo de tabla**, y selecciona la casilla **Fila de totales**.
3. Aparece una fila al final de la tabla. Su primera celda dice `Total` y su última columna ya trae `=SUBTOTALES(109,[Q1])`, que es SUMA sin contar las filas ocultas. Comportamiento predeterminado verificado.
4. Haz clic en la celda de total que está debajo de la columna que necesitas totalizar.
5. En el borde derecho de esa celda aparece una flecha desplegable. Haz clic en ella.
6. Elige la función de la lista: **Ninguno**, **Promedio**, **Recuento**, **Contar números**, **Máx**, **Mín**, **Suma**, **Desvest**, **Var**, **Más funciones**.
7. Excel escribe la función SUBTOTALES que corresponde. Promedio da `=SUBTOTALES(101,[Q1])`, Suma da `=SUBTOTALES(109,[Q1])`. Los dos verificados en el producto.
8. Repite en cada columna que pida la tarea. Pon **Ninguno** en la columna que deba quedarse vacía.

El objetivo 2.2.4 del Expert es este mismo control visto desde el otro lado, donde sí importan los códigos `1xx` y `9` de SUBTOTALES; la diferencia entre unos y otros está escrita ahí.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.2.3 -->

---

### 3.3.1 Filter records

**EN · texto fuente, no editar**

**Exam route, value filter**

1. Click any cell in the table. In a plain range, first go to the **Data** tab, **Sort & Filter** group, and click **Filter** to put the arrows on the header row.
2. Click the filter arrow in the header of the column to filter.
3. Clear the **(Select All)** check box. Every value clears with it.
4. Select only the values the task names. Use the **Search** box above the list when the list is long, then select **Add current selection to filter** if you are building the selection in passes.
5. Click **OK**.

**Exam route, criteria filter**

1. Click the filter arrow in the column header.
2. Point to **Number Filters**, **Text Filters** or **Date Filters**. Excel offers the one that matches the column's data type.
3. Click the operator the task names, for example **Greater Than...**, **Between...**, **Top 10...**, **Begins With...**, **Contains...**.
4. In the **Custom AutoFilter** dialog, type the value in the box to the right of the operator.
5. For a second condition, select the **And** or the **Or** option button and fill the second row. Use `?` for one character and `*` for any run of characters.
6. Click **OK**.

**Exam route, clearing**

1. To clear one column, click that column's filter arrow and click **Clear Filter From "Column name"**.
2. To clear every filter and keep the arrows, go to the **Data** tab, **Sort & Filter** group, and click **Clear**.
3. To remove the arrows as well, click **Filter** in the same group.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.3.1 -->

**Ruta de examen, filtro por valores**

1. Haz clic en cualquier celda de la tabla. En un rango normal, primero ve a la pestaña **Datos**, grupo **Ordenar y filtrar**, y haz clic en **Filtro** para poner las flechas en la fila de encabezados.
2. Haz clic en la flecha de filtro del encabezado de la columna que vas a filtrar.
3. Desactiva la casilla **[(Select All)]**. Con ella se desactivan todos los valores.
4. Selecciona solo los valores que pida la tarea. Usa el cuadro **Buscar** que está arriba de la lista cuando la lista sea larga, y luego selecciona **[Add current selection to filter]** si vas armando la selección en varias pasadas.
5. Haz clic en **Aceptar**.

**Ruta de examen, filtro por criterios**

1. Haz clic en la flecha de filtro del encabezado de la columna.
2. Apunta a **[Number Filters]**, **Filtros de texto** o **[Date Filters]**. Excel ofrece el que corresponde al tipo de dato de la columna.
3. Haz clic en el operador que pida la tarea, por ejemplo **[Greater Than...]**, **[Between...]**, **[Top 10...]**, **[Begins With...]**, **[Contains...]**.
4. En el cuadro de diálogo **[Custom AutoFilter]**, escribe el valor en el cuadro que está a la derecha del operador.
5. Para una segunda condición, selecciona el botón de opción **[And]** o el **[Or]** y llena el segundo renglón. Usa `?` para un carácter y `*` para cualquier cantidad de caracteres.
6. Haz clic en **Aceptar**.

**Ruta de examen, borrar el filtro**

1. Para borrar una sola columna, haz clic en la flecha de filtro de esa columna y haz clic en **[Clear Filter From "Column name"]**.
2. Para borrar todos los filtros y dejar las flechas, ve a la pestaña **Datos**, grupo **Ordenar y filtrar**, y haz clic en **Borrar**.
3. Para quitar también las flechas, haz clic en **Filtro** en el mismo grupo.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.3.1 -->

---

### 3.3.2 Sort data by multiple columns

**EN · texto fuente, no editar**

**Exam route**

1. Click any single cell inside the range or table. Do not preselect one column, which is how you tear the rows apart.
2. Go to the **Data** tab, **Sort & Filter** group, and click **Sort**.
3. The **Sort** dialog opens. Select the **My data has headers** check box so the header row stays put and the lists show column names instead of letters.
4. Fill the first level: open the **Sort by** list and pick the column; open the **Sort On** list and pick **Cell Values**, **Cell Color**, **Font Color** or **Conditional Formatting Icon**; open the **Order** list and pick **A to Z**, **Smallest to Largest**, **Oldest to Newest** or **Custom List...**.
5. Click **Add Level**.
6. Fill the second level the same way. Its first list is labelled **Then by**.
7. Repeat for every level the task names. Use the arrow buttons at the top of the dialog to move a level up or down, because the order of the levels is the priority.
8. Click **Options...** if the task asks for case sensitivity or for left-to-right sorting.
9. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-3.3.2 -->

**Ruta de examen**

1. Haz clic en una sola celda dentro del rango o de la tabla. No preselecciones una columna, que es la forma de romper las filas.
2. Ve a la pestaña **Datos**, grupo **Ordenar y filtrar**, y haz clic en **Ordenar**.
3. Se abre el cuadro de diálogo **Ordenar**. Selecciona la casilla **[My data has headers]** para que la fila de encabezados se quede en su lugar y las listas muestren nombres de columna en vez de letras.
4. Llena el primer nivel: abre la lista **[Sort by]** y elige la columna; abre la lista **[Sort On]** y elige **[Cell Values]**, **[Cell Color]**, **[Font Color]** o **[Conditional Formatting Icon]**; abre la lista **[Order]** y elige **[A to Z]**, **[Smallest to Largest]**, **[Oldest to Newest]** o **[Custom List...]**.
5. Haz clic en **[Add Level]**.
6. Llena el segundo nivel igual. Su primera lista se llama **[Then by]**.
7. Repite en cada nivel que pida la tarea. Usa los botones de flecha de la parte superior del cuadro de diálogo para subir o bajar un nivel, porque el orden de los niveles es la prioridad.
8. Haz clic en **[Options...]** si la tarea pide distinguir mayúsculas y minúsculas o si pide ordenar de izquierda a derecha.
9. Haz clic en **Aceptar**.

_Los términos entre corchetes se quedan en inglés porque no están en el glosario y no se pudieron leer de un Excel en español. **TO CONFIRM**._

<!-- ES-FIN MO200-3.3.2 -->

---

## MO-200 Associate · Domain 4, Perform operations by using formulas and functions

### 4.1.1 Insert relative, absolute, and mixed references

**EN · texto fuente, no editar**

**Exam route**

1. Click the cell that will hold the formula and type `=`.
2. Click the cell you want to refer to, or type its address. It arrives relative, as `B2`.
3. Leave the insertion point touching that reference and press `F4`. Each press cycles one step: `B2`, `$B$2`, `B$2`, `$B2`, back to `B2`.
4. Stop on the form the task needs. `$B$2` locks column and row. `B$2` locks the row only, so the reference slides sideways when filled right and stays on row 2 when filled down. `$B2` locks the column only.
5. Press `Enter`.
6. Fill the formula in both directions, right and down, with the fill handle or `Ctrl+R` and `Ctrl+D`.
7. Click a cell in the far corner of the filled block and read the formula bar to confirm the locked part did not move.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.1.1 -->

**Ruta de examen**

1. Haz clic en la celda donde va la fórmula y escribe `=`.
2. Haz clic en la celda a la que quieres hacer referencia, o escribe su dirección. Se inserta como relativa, en la forma `B2`.
3. Deja el punto de inserción tocando esa referencia y presiona `F4`. Cada vez que lo presionas avanza un paso: `B2`, `$B$2`, `B$2`, `$B2`, y de regreso a `B2`.
4. Detente en la forma que pide la tarea. `$B$2` fija la columna y la fila. `B$2` fija solo la fila, así que la referencia se recorre de lado al rellenar hacia la derecha y se queda en la fila 2 al rellenar hacia abajo. `$B2` fija solo la columna.
5. Presiona `Entrar`.
6. Rellena la fórmula en las dos direcciones, a la derecha y hacia abajo, con el controlador de relleno o con `Ctrl+R` y `Ctrl+D` (**TO CONFIRM**: las letras de estos dos métodos abreviados cambian en el Excel en español).
7. Haz clic en una celda de la esquina más lejana del bloque rellenado y lee la barra de fórmulas para confirmar que la parte fijada no se movió.

<!-- ES-FIN MO200-4.1.1 -->

---

### 4.1.2 Reference named ranges and named tables in formulas

**EN · texto fuente, no editar**

**Exam route, named range**

1. Create the name as in 2.3.1: **Formulas** tab, **Defined Names** group, **Define Name**, fill **Name**, **Scope** and **Refers to**, click **OK**.
2. In the formula, start typing the first letters of the name. Formula AutoComplete lists it with a tag icon; press `Tab` to insert it.
3. Alternatively press `F3` to open the **Paste Name** dialog, select the name, click **OK**.

**Exam route, named table**

1. Click any cell inside the table.
2. Go to the **Table Design** tab, **Properties** group. The first control is the box labelled **Table Name:** (2.3.2).
3. Select the contents, type the new name, press `Enter`.
4. In a formula written outside the table, type `=SUM(` then the table name, then `[`. Excel lists the columns. Pick one and close the brackets: `=SUM(Sales[Q1])`.
5. In a formula written inside the table, the same reference is written `=SUM([@Q1],[@Q2])`. Excel drops the table name because you are already in it, and `@` means this row. Both forms verified in the product.
6. For the header text of a column, the reference is `=Sales[[#Headers],[Q1]]`. The other special items are `[#Data]`, `[#Totals]` and `[#All]`.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.1.2 -->

**Ruta de examen, rango con nombre**

1. Crea el nombre como en 2.3.1: pestaña **Fórmulas**, grupo **Nombres definidos**, [**Define Name**], llena [**Name**], [**Scope**] y [**Refers to**], y haz clic en [**OK**].
2. En la fórmula, empieza a escribir las primeras letras del nombre. [**Formula AutoComplete**] lo enlista con un icono de etiqueta; presiona `Tab` para insertarlo.
3. La otra vía es presionar `F3` para abrir el cuadro de diálogo [**Paste Name**], seleccionar el nombre y hacer clic en [**OK**].

**Ruta de examen, tabla con nombre**

1. Haz clic en cualquier celda dentro de la tabla.
2. Ve a la pestaña **Diseño de tabla**, grupo [**Properties**]. El primer control es el cuadro rotulado **Nombre de la tabla:** (2.3.2).
3. Selecciona el contenido, escribe el nombre nuevo y presiona `Entrar`.
4. En una fórmula escrita fuera de la tabla, escribe `=SUMA(`, luego el nombre de la tabla y luego `[`. Excel enlista las columnas. Elige una y cierra los corchetes: `=SUMA(Sales[Q1])`.
5. En una fórmula escrita dentro de la tabla, esa misma referencia se escribe `=SUMA([@Q1],[@Q2])`. Excel quita el nombre de la tabla porque ya estás dentro de ella, y `@` significa esta fila. Las dos formas están verificadas en el producto.
6. Para el texto del encabezado de una columna, la referencia es `=Sales[[#Headers],[Q1]]`. Los otros elementos especiales son `[#Data]`, `[#Totals]` y `[#All]` (**TO CONFIRM**: el Excel en español localiza estos elementos especiales y el glosario no los trae).

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.1.2 -->

---

### 4.2.1 Perform calculations by using the AVERAGE(), MAX(), MIN(), and SUM() functions

**EN · texto fuente, no editar**

This is the first appearance of **Insert Function** and the **Function Arguments** dialog. Every other function objective in both exams goes through them, so the walkthrough here is the one the rest refer back to.

**Exam route, from the ribbon**

1. Click the cell for the result. Put it directly under the column or to the right of the row you are summarising, so Excel guesses well.
2. Go to the **Formulas** tab, **Function Library** group, and click the arrow under **AutoSum**.
3. Pick **Sum**, **Average**, **Max**, **Min** or **Count Numbers** from the list. The plain button face applies **Sum**.
4. Excel writes the function and proposes a range with a moving dashed border.
5. If the proposal is wrong, drag over the correct range now, while the function is still open. Excel replaces the argument.
6. Press `Enter`.

**Exam route, through the dialog**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, and click **Insert Function**.
3. In the **Insert Function** dialog, open the **Or select a category** list and pick **Math & Trig** for SUM or **Statistical** for AVERAGE, MAX and MIN. Or type what you want in **Search for a function** and click **Go**.
4. Select the function in the **Select a function** list. Read the syntax line under the list.
5. Click **OK**.
6. In the **Function Arguments** dialog, click in the **Number1** box and drag over the range on the sheet. Use the collapse button at the right of the box if the dialog covers the data.
7. Read **Formula result =** at the bottom left before committing.
8. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.2.1 -->

Aquí aparecen por primera vez [**Insert Function**] y el cuadro de diálogo [**Function Arguments**]. Todos los demás objetivos de funciones de los dos exámenes pasan por ellos, así que el recorrido de aquí es al que remiten los otros.

**Ruta de examen, desde la cinta de opciones**

1. Haz clic en la celda del resultado. Colócala justo debajo de la columna o a la derecha de la fila que estás resumiendo, para que Excel adivine bien.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], y haz clic en la flecha que está debajo de [**AutoSum**].
3. Elige [**Sum**], [**Average**], [**Max**], [**Min**] o [**Count Numbers**] de la lista. Si haces clic en el botón y no en la flecha, se aplica [**Sum**].
4. Excel escribe la función y propone un rango con un borde punteado en movimiento.
5. Si la propuesta está mal, arrastra sobre el rango correcto en ese momento, mientras la función sigue abierta. Excel reemplaza el argumento.
6. Presiona `Entrar`.

**Ruta de examen, por el cuadro de diálogo**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], y haz clic en [**Insert Function**].
3. En el cuadro de diálogo [**Insert Function**], abre la lista [**Or select a category**] y elige [**Math & Trig**] para SUMA o [**Statistical**] para PROMEDIO, MAX y MIN. O escribe lo que buscas en [**Search for a function**] y haz clic en [**Go**].
4. Selecciona la función en la lista [**Select a function**]. Lee la línea de sintaxis que aparece debajo de la lista.
5. Haz clic en [**OK**].
6. En el cuadro de diálogo [**Function Arguments**], haz clic en el cuadro [**Number1**] y arrastra sobre el rango en la hoja. Usa el botón de contraer que está a la derecha del cuadro si el cuadro de diálogo tapa los datos.
7. Lee [**Formula result =**] en la esquina inferior izquierda antes de confirmar.
8. Haz clic en [**OK**].

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.2.1 -->

---

### 4.2.2 Count cells by using the COUNT(), COUNTA(), and COUNTBLANK() functions

**EN · texto fuente, no editar**

**Exam route**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, click **More Functions**, point to **Statistical**, and click **COUNT**, **COUNTA** or **COUNTBLANK**. COUNT is also on the **AutoSum** list under the name **Count Numbers**, which is the same function under a friendlier label.
3. In the **Function Arguments** dialog, click in the **Value1** box for COUNT and COUNTA, or the **Range** box for COUNTBLANK, and drag over the range.
4. Read **Formula result =** at the bottom of the dialog.
5. Click **OK**.
6. Choose deliberately, because the three do not overlap the way people assume. Verified on a four-cell range holding a number, a text string, a formula returning `""` and one truly empty cell: COUNT returns 1, COUNTA returns 3, COUNTBLANK returns 2. COUNTA and COUNTBLANK both count the cell holding `""`, so the two results add up to more cells than the range has.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.2.2 -->

**Ruta de examen**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], haz clic en [**More Functions**], apunta a [**Statistical**] y haz clic en **CONTAR**, **CONTARA** o **CONTAR.BLANCO**. CONTAR también está en la lista de [**AutoSum**] con el nombre [**Count Numbers**], que es la misma función con una etiqueta más amable.
3. En el cuadro de diálogo [**Function Arguments**], haz clic en el cuadro [**Value1**] para CONTAR y CONTARA, o en el cuadro **Rango** para CONTAR.BLANCO, y arrastra sobre el rango.
4. Lee [**Formula result =**] en la parte inferior del cuadro de diálogo.
5. Haz clic en [**OK**].
6. Elige a conciencia, porque las tres no se traslapan como la gente supone. Verificado sobre un rango de cuatro celdas con un número, una cadena de texto, una fórmula que devuelve `""` y una celda realmente vacía: CONTAR devuelve 1, CONTARA devuelve 3 y CONTAR.BLANCO devuelve 2. CONTARA y CONTAR.BLANCO cuentan las dos la celda que tiene `""`, así que los dos resultados suman más celdas de las que tiene el rango.

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.2.2 -->

---

### 4.2.3 Perform conditional operations by using the IF() function

**EN · texto fuente, no editar**

**Exam route**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, click **Logical**, and click **IF**.
3. In the **Function Arguments** dialog, click in the **Logical_test** box and build the comparison, for example click cell B2 and type `>=70`.
4. Click in the **Value_if_true** box and type the text without quotation marks. The dialog adds them for you and shows the finished value to the right of the box.
5. Click in the **Value_if_false** box and do the same. Leaving it empty returns FALSE, which is almost never what the task wants.
6. Read **Formula result =** at the bottom of the dialog.
7. Click **OK**.
8. Lock any reference that must not move before filling down: put the insertion point on it in the formula bar and press `F4`.
9. Fill down and spot check one row on each side of the boundary.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.2.3 -->

**Ruta de examen**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], haz clic en [**Logical**] y haz clic en **SI**.
3. En el cuadro de diálogo [**Function Arguments**], haz clic en el cuadro [**Logical_test**] y arma la comparación, por ejemplo haz clic en la celda B2 y escribe `>=70`.
4. Haz clic en el cuadro [**Value_if_true**] y escribe el texto sin comillas. El cuadro de diálogo las agrega por ti y muestra el valor terminado a la derecha del cuadro.
5. Haz clic en el cuadro [**Value_if_false**] y haz lo mismo. Si lo dejas vacío devuelve FALSO, que casi nunca es lo que pide la tarea.
6. Lee [**Formula result =**] en la parte inferior del cuadro de diálogo.
7. Haz clic en [**OK**].
8. Fija cualquier referencia que no deba moverse antes de rellenar hacia abajo: pon el punto de inserción sobre ella en la barra de fórmulas y presiona `F4`.
9. Rellena hacia abajo y revisa una fila de cada lado del límite.

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.2.3 -->

---

### 4.3.1 Format text by using RIGHT(), LEFT(), and MID() functions

**EN · texto fuente, no editar**

**Exam route**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, click **Text**, and click **LEFT**, **RIGHT** or **MID**.
3. For **LEFT** and **RIGHT**, the **Function Arguments** dialog shows two boxes. Click in **Text** and select the source cell; click in **Num_chars** and type how many characters to take. Leaving **Num_chars** empty returns one character.
4. For **MID**, the dialog shows three boxes: **Text**, **Start_num**, **Num_chars**. **Start_num** counts from 1 at the first character. Verified: `=MID("2026-08-18",6,2)` returns `08`.
5. Read **Formula result =** at the bottom of the dialog.
6. Click **OK** and fill down.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.3.1 -->

**Ruta de examen**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], haz clic en [**Text**] y haz clic en **IZQUIERDA**, **DERECHA** o **EXTRAE**.
3. Para **IZQUIERDA** y **DERECHA**, el cuadro de diálogo [**Function Arguments**] muestra dos cuadros. Haz clic en [**Text**] y selecciona la celda de origen; haz clic en [**Num_chars**] y escribe cuántos caracteres tomar. Si dejas [**Num_chars**] vacío devuelve un carácter.
4. Para **EXTRAE**, el cuadro de diálogo muestra tres cuadros: [**Text**], [**Start_num**] y [**Num_chars**]. [**Start_num**] cuenta desde 1 en el primer carácter. Verificado: `=EXTRAE("2026-08-18",6,2)` devuelve `08`.
5. Lee [**Formula result =**] en la parte inferior del cuadro de diálogo.
6. Haz clic en [**OK**] y rellena hacia abajo.

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.3.1 -->

---

### 4.3.2 Format text by using UPPER(), LOWER(), and LEN() functions

**EN · texto fuente, no editar**

**Exam route**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, and click **Text**.
3. Click **UPPER**, **LOWER** or **LEN**. **PROPER** sits in the same list and belongs to a different objective, so read the name before clicking.
4. In the **Function Arguments** dialog, click in the **Text** box and select the source cell. All three take exactly one argument.
5. Read **Formula result =** and click **OK**.
6. Fill down.
7. Remember what LEN counts: every character, spaces and punctuation included. Verified: `=LEN("Ana Luz ")` returns 8, counting the trailing space.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.3.2 -->

**Ruta de examen**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], y haz clic en [**Text**].
3. Haz clic en **MAYUSC**, **MINUSC** o **LARGO**. **NOMPROPIO** está en la misma lista y pertenece a otro objetivo, así que lee el nombre antes de hacer clic.
4. En el cuadro de diálogo [**Function Arguments**], haz clic en el cuadro [**Text**] y selecciona la celda de origen. Las tres toman exactamente un argumento.
5. Lee [**Formula result =**] y haz clic en [**OK**].
6. Rellena hacia abajo.
7. Acuérdate de qué cuenta LARGO: todos los caracteres, espacios y signos de puntuación incluidos. Verificado: `=LARGO("Ana Luz ")` devuelve 8, contando el espacio final.

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.3.2 -->

---

### 4.3.3 Format text by using the CONCAT() and TEXTJOIN() functions

**EN · texto fuente, no editar**

**Exam route, CONCAT**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, click **Text**, and click **CONCAT**.
3. In the **Function Arguments** dialog, click in **Text1**. CONCAT takes a whole range in one box, so drag over `A2:C2` rather than filling one box per cell. Verified: `=CONCAT(E1:G1)` over Ana, empty, Luz returns `AnaLuz`.
4. Add literal text in the next box, including its spaces, for example `" "`. In the dialog you type the space and the dialog adds the quotation marks.
5. Read **Formula result =** and click **OK**.

**Exam route, TEXTJOIN**

1. Click the result cell.
2. Go to the **Formulas** tab, **Function Library** group, click **Text**, and click **TEXTJOIN**.
3. In the **Function Arguments** dialog, click in **Delimiter** and type the separator, for example a comma and a space.
4. Click in **Ignore_empty** and type `TRUE`. This is the box that matters. Verified over Ana, empty, Luz: `TRUE` returns `Ana, Luz`, and `FALSE` returns `Ana, , Luz` with the double delimiter showing.
5. Click in **Text1** and drag over the range.
6. Read **Formula result =** and click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-4.3.3 -->

**Ruta de examen, CONCAT**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], haz clic en [**Text**] y haz clic en **CONCAT**.
3. En el cuadro de diálogo [**Function Arguments**], haz clic en [**Text1**]. CONCAT toma un rango completo en un solo cuadro, así que arrastra sobre `A2:C2` en lugar de llenar un cuadro por celda. Verificado: `=CONCAT(E1:G1)` sobre Ana, vacía y Luz devuelve `AnaLuz`.
4. Agrega el texto literal en el cuadro siguiente, con sus espacios, por ejemplo `" "`. Ahí escribes el espacio y el cuadro de diálogo agrega las comillas.
5. Lee [**Formula result =**] y haz clic en [**OK**].

**Ruta de examen, UNIRCADENAS**

1. Haz clic en la celda del resultado.
2. Ve a la pestaña **Fórmulas**, grupo [**Function Library**], haz clic en [**Text**] y haz clic en **UNIRCADENAS**.
3. En el cuadro de diálogo [**Function Arguments**], haz clic en [**Delimiter**] y escribe el separador, por ejemplo una coma y un espacio.
4. Haz clic en [**Ignore_empty**] y escribe `VERDADERO`. Este es el cuadro que importa. Verificado sobre Ana, vacía y Luz: `VERDADERO` devuelve `Ana, Luz` y `FALSO` devuelve `Ana, , Luz`, con el separador doble a la vista.
5. Haz clic en [**Text1**] y arrastra sobre el rango.
6. Lee [**Formula result =**] y haz clic en [**OK**].

**TO CONFIRM**: los nombres entre corchetes no están en el glosario. Se quedan en inglés hasta leerlos en un Excel en español.

<!-- ES-FIN MO200-4.3.3 -->

---

## MO-200 Associate · Domain 5, Manage charts

### 5.1.1 Create charts

**EN · texto fuente, no editar**

This is the first appearance of the **Insert Chart** dialog; Expert 4.1.1 and 4.1.2 come back to it for the advanced types.

**Exam route**

1. Select the source data including the header row and the category column. For non-adjacent columns, select the first block, hold `Ctrl` and select the second.
2. Go to the **Insert** tab, **Charts** group, and click the dialog box launcher, the small arrow in the bottom right corner of the group.
3. The **Insert Chart** dialog opens with two tabs, **Recommended Charts** and **All Charts**. Click **All Charts**.
4. In the list on the left, click the family: **Column**, **Bar**, **Line**, **Pie**, **Doughnut**, **Area**, **X Y (Scatter)**, **Map**, **Stock**, **Surface**, **Radar**, **Treemap**, **Sunburst**, **Histogram**, **Box & Whisker**, **Waterfall**, **Funnel**, **Combo**.
5. Along the top of the right pane, click the subtype icon, for Column, **Clustered Column**, **Stacked Column**, **100% Stacked Column** and their 3-D versions. Point at each and read the tooltip.
6. Check the preview in the pane below. It draws with your real data.
7. Click **OK**.
8. The chart lands on the sheet as a floating object, selected, with the contextual **Chart Design** and **Format** tabs on the ribbon.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.1.1 -->

Aquí aparece por primera vez el cuadro de diálogo **[Insert Chart]**; los objetivos 4.1.1 y 4.1.2 del Expert regresan a él para los tipos avanzados.

**Ruta de examen**

1. Selecciona los datos de origen, incluidas la fila de encabezados y la columna de categorías. Si las columnas no están juntas, selecciona el primer bloque, mantén presionada `Ctrl` y selecciona el segundo.
2. Ve a la pestaña **Insertar**, grupo **Gráficos**, y haz clic en el [dialog box launcher], la flecha pequeña de la esquina inferior derecha del grupo.
3. Se abre el cuadro de diálogo **[Insert Chart]** con dos pestañas, **Gráficos recomendados** y **[All Charts]**. Haz clic en **[All Charts]**.
4. En la lista de la izquierda, haz clic en la familia: **Gráfico de columnas**, **Gráfico de barras**, **Gráfico de líneas**, **Gráfico circular**, **Gráfico de anillos**, **Gráfico de área**, **Gráfico XY (dispersión)**, **Gráfico de mapa**, **Gráfico de cotizaciones**, **Gráfico de superficie**, **Gráficos radiales**, **Gráfico de rectángulos**, **Gráfico de proyección solar**, **Gráficos de histograma**, **Gráfico de cajas y bigotes**, **Gráficos de cascada**, **Gráficos de embudo**, **Gráficos combinados**.
5. En la parte superior del panel derecho, haz clic en el icono del subtipo; para las columnas, **Columnas agrupadas**, **Columna apilada**, **Columna 100 % apilada** y sus versiones en 3D. Apunta a cada uno y lee el nombre que aparece.
6. Revisa la vista previa en el panel de abajo. Se dibuja con tus datos reales.
7. Haz clic en **Aceptar**.
8. El gráfico queda en la hoja como un objeto flotante, seleccionado, con las pestañas contextuales **Diseño de gráfico** y **Formato** en la cinta de opciones.

<!-- ES-FIN MO200-5.1.1 -->

---

### 5.1.2 Create chart sheets

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart once on its border or on an empty part of the chart area, so the whole chart object is selected. If a title or a series is selected instead, press `Esc` and click again on the border.
2. Go to the **Chart Design** tab, **Location** group, and click **Move Chart**.
3. In the **Move Chart** dialog, select the **New sheet:** option button.
4. Type the sheet name in the box beside it. Do not leave the default `Chart1` when the task names a sheet.
5. Click **OK**.
6. The chart moves onto its own sheet. That sheet has no cells and no grid, and its tab sits in the workbook tab bar like any other.
7. To send it back to a worksheet, repeat and select **Object in:**, then pick the worksheet from the list.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.1.2 -->

**Ruta de examen**

1. Haz clic una vez en el borde del gráfico o en una parte vacía del área del gráfico, de modo que quede seleccionado todo el objeto. Si en lugar de eso queda seleccionado un título o una serie, presiona `Esc` y vuelve a hacer clic en el borde.
2. Ve a la pestaña **Diseño de gráfico**, grupo **[Location]**, y haz clic en **[Move Chart]**.
3. En el cuadro de diálogo **[Move Chart]**, selecciona el botón de opción **[New sheet:]**.
4. Escribe el nombre de la hoja en el cuadro que está a un lado. No dejes el nombre predeterminado `Chart1` cuando la tarea nombra una hoja.
5. Haz clic en **Aceptar**.
6. El gráfico se mueve a su propia hoja. Esa hoja de gráfico no tiene celdas ni cuadrícula, y su pestaña queda en la barra de pestañas del libro como cualquier otra.
7. Para devolverlo a una hoja de cálculo, repite el procedimiento y selecciona **[Object in:]**, luego elige la hoja de cálculo de la lista.

<!-- ES-FIN MO200-5.1.2 -->

---

### 5.2.1 Add data series to charts

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border to select the whole chart.
2. Go to the **Chart Design** tab, **Data** group, and click **Select Data**.
3. The **Select Data Source** dialog opens. The top box is **Chart data range**. The left list is **Legend Entries (Series)**. The right list is **Horizontal (Category) Axis Labels**.
4. To add a series, click **Add** under **Legend Entries (Series)**.
5. In the **Edit Series** dialog, click in **Series name** and select the header cell of the new column. Do not type the text: selecting the cell keeps the legend linked.
6. Click in **Series values**, delete the placeholder `={1}`, and drag over the new data range.
7. Click **OK** to close **Edit Series**.
8. Back in **Select Data Source**, use the up and down arrow buttons to set the plotting order, **Edit** to correct a series, **Remove** to delete one.
9. If the categories are wrong, click **Edit** under **Horizontal (Category) Axis Labels** and select the label range.
10. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.2.1 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para seleccionar todo el gráfico.
2. Ve a la pestaña **Diseño de gráfico**, grupo **Datos**, y haz clic en **[Select Data]**.
3. Se abre el cuadro de diálogo **[Select Data Source]**. El cuadro de arriba es **[Chart data range]**. La lista de la izquierda es **[Legend Entries (Series)]**. La de la derecha es **[Horizontal (Category) Axis Labels]**.
4. Para agregar una serie, haz clic en **Agregar** debajo de **[Legend Entries (Series)]**.
5. En el cuadro de diálogo **[Edit Series]**, haz clic en **[Series name]** y selecciona la celda de encabezado de la columna nueva. No escribas el texto: seleccionar la celda mantiene la leyenda vinculada.
6. Haz clic en **[Series values]**, borra el marcador de posición `={1}` y arrastra sobre el rango de datos nuevo.
7. Haz clic en **Aceptar** para cerrar **[Edit Series]**.
8. De vuelta en **[Select Data Source]**, usa los botones de flecha hacia arriba y hacia abajo para fijar el orden de trazado, **Editar** para corregir una serie y **Quitar** para eliminar una.
9. Si las categorías están mal, haz clic en **Editar** debajo de **[Horizontal (Category) Axis Labels]** y selecciona el rango de las etiquetas.
10. Haz clic en **Aceptar**.

<!-- ES-FIN MO200-5.2.1 -->

---

### 5.2.2 Switch between rows and columns in source data

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border to select the whole chart.
2. Go to the **Chart Design** tab, **Data** group, and click **Switch Row/Column**.
3. The legend and the category axis trade places. Verified on a three-region by two-quarter block: plotted by column the chart holds 2 series, plotted by row it holds 3.
4. When the task also changes the series, do it inside the dialog instead: **Chart Design** tab, **Data** group, **Select Data**, click the **Switch Row/Column** button that sits between the two lists in the **Select Data Source** dialog, then **OK**. Same result, and you are already where the next edit happens.
5. The button is unavailable while the chart is not selected, and greyed for chart types that accept only one series, such as Pie.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.2.2 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para seleccionar todo el gráfico.
2. Ve a la pestaña **Diseño de gráfico**, grupo **Datos**, y haz clic en **Cambiar fila o columna**.
3. La leyenda y el eje de categorías intercambian lugares. Verificado sobre un bloque de tres regiones por dos trimestres: trazado por columna el gráfico tiene 2 series, trazado por fila tiene 3.
4. Cuando la tarea también cambia la serie, hazlo mejor dentro del cuadro de diálogo: pestaña **Diseño de gráfico**, grupo **Datos**, **[Select Data]**, haz clic en el botón **Cambiar fila o columna** que está entre las dos listas del cuadro de diálogo **[Select Data Source]** y luego en **Aceptar**. El resultado es el mismo, y ya estás donde ocurre la siguiente edición.
5. El botón no está disponible mientras el gráfico no esté seleccionado, y aparece atenuado en los tipos de gráfico que solo aceptan una serie, como el gráfico circular.

<!-- ES-FIN MO200-5.2.2 -->

---

### 5.2.3 Add and modify chart elements

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border to select the whole chart.
2. Go to the **Chart Design** tab, **Chart Layouts** group, and click **Add Chart Element**.
3. Point to the element the task names. The menu holds **Axes**, **Axis Titles**, **Chart Title**, **Data Labels**, **Data Table**, **Error Bars**, **Gridlines**, **Legend**, **Lines**, **Trendline** and **Up/Down Bars**, and which of them are available depends on the chart type.
4. Click the position from the submenu, not just the element. **Chart Title** offers **Above Chart** and **Centered Overlay**. **Legend** offers **Right**, **Top**, **Left**, **Bottom**. **Data Labels** offers **Center**, **Inside End**, **Inside Base**, **Outside End**, **Data Callout**. **Axis Titles** offers **Primary Horizontal** and **Primary Vertical**. **None** removes the element.
5. To set the text, click the element once to select it, click a second time to put the insertion point inside, and type. To tie the text to a cell instead, select the element, type `=` in the formula bar, click the cell, press `Enter`.
6. To format an element, right-click it and click **Format ...**, which opens the task pane on the right of the window. The pane carries the element's own tabs, for example **Fill & Line**, **Effects**, **Size & Properties**, **Label Options**.
7. To remove an element, select it and press `Delete`, or return to **Add Chart Element** and click **None**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.2.3 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para seleccionar todo el gráfico.
2. Ve a la pestaña **Diseño de gráfico**, grupo **[Chart Layouts]**, y haz clic en **[Add Chart Element]**.
3. Apunta al elemento que nombra la tarea. El menú tiene **[Axes]**, **Títulos de eje**, **Título del gráfico**, **Etiquetas de datos**, **Tabla de datos**, **[Error Bars]**, **Líneas de cuadrícula**, **Leyenda**, **[Lines]**, **[Trendline]** y **[Up/Down Bars]**, y cuáles están disponibles depende del tipo de gráfico.
4. Haz clic en la posición dentro del submenú, no solo en el elemento. **Título del gráfico** ofrece **[Above Chart]** y **[Centered Overlay]**. **Leyenda** ofrece **[Right]**, **[Top]**, **[Left]** y **[Bottom]**. **Etiquetas de datos** ofrece **Centrar**, **[Inside End]**, **[Inside Base]**, **[Outside End]** y **[Data Callout]**. **Títulos de eje** ofrece **[Primary Horizontal]** y **[Primary Vertical]**. **Ninguno** quita el elemento.
5. Para escribir el texto, haz clic una vez en el elemento para seleccionarlo, haz clic una segunda vez para poner el punto de inserción dentro y escribe. Si en vez de eso quieres vincular el texto a una celda, selecciona el elemento, escribe `=` en la barra de fórmulas, haz clic en la celda y presiona `Entrar`.
6. Para dar formato a un elemento, haz clic derecho en él y haz clic en **[Format ...]**, que abre el panel de tareas a la derecha de la ventana. El panel trae las pestañas propias del elemento, por ejemplo **[Fill & Line]**, **Efectos**, **[Size & Properties]**, **[Label Options]**.
7. Para quitar un elemento, selecciónalo y presiona `Supr`, o vuelve a **[Add Chart Element]** y haz clic en **Ninguno**.

<!-- ES-FIN MO200-5.2.3 -->

---

### 5.3.1 Apply chart layouts

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border to select the whole chart.
2. Go to the **Chart Design** tab, **Chart Layouts** group, and click **Quick Layout**.
3. The gallery opens with the layouts available for that chart type, numbered from **Layout 1** upward. Point at each and read the tooltip, which gives the number, and watch the live preview on the chart.
4. Click the layout the task names by number.
5. Read what it did. A layout is a package: it can add a data table, move the legend to the bottom, remove the gridlines, or add axis titles as placeholder text. It overwrites element positions you set by hand earlier.
6. Apply the layout first, then add or edit individual elements. Doing it the other way round throws the work away.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.3.1 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para seleccionar todo el gráfico.
2. Ve a la pestaña **Diseño de gráfico**, grupo **[Chart Layouts]**, y haz clic en **Diseño rápido**.
3. La galería se abre con los diseños disponibles para ese tipo de gráfico, numerados desde **[Layout 1]** en adelante. Apunta a cada uno y lee el nombre que aparece, que trae el número, y observa la vista previa en vivo sobre el gráfico.
4. Haz clic en el diseño que la tarea nombra por número.
5. Lee lo que hizo. Un diseño es un paquete: puede agregar una tabla de datos, mover la leyenda hacia abajo, quitar las líneas de cuadrícula o agregar títulos de eje como texto de marcador de posición. Sobrescribe las posiciones de los elementos que hayas fijado a mano antes.
6. Aplica el diseño primero y después agrega o edita los elementos individuales. Al revés, tiras el trabajo.

<!-- ES-FIN MO200-5.3.1 -->

---

### 5.3.2 Apply chart styles

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border to select the whole chart.
2. Go to the **Chart Design** tab, **Chart Styles** group.
3. Click the **More** arrow at the bottom right corner of the gallery to open the whole set rather than the three or four thumbnails the ribbon has room for.
4. Point at each thumbnail. The tooltip reads **Style 1**, **Style 2** and so on, and the chart previews live.
5. Click the style the task names.
6. For the colour set, stay on the **Chart Design** tab, **Chart Styles** group, and click **Change Colors**. Pick a row from **Colorful** or from **Monochromatic**. This is a separate graded action from the style.
7. If earlier hand formatting is fighting the style, select the element, go to the **Format** tab, **Current Selection** group, and click **Reset to Match Style**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.3.2 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para seleccionar todo el gráfico.
2. Ve a la pestaña **Diseño de gráfico**, grupo **Estilos de gráfico**.
3. Haz clic en la flecha **Más** de la esquina inferior derecha de la galería para abrir el conjunto completo, en lugar de las tres o cuatro miniaturas que caben en la cinta de opciones.
4. Apunta a cada miniatura. El nombre que aparece dice **[Style 1]**, **[Style 2]** y así, y el gráfico se previsualiza en vivo.
5. Haz clic en el estilo que la tarea nombra.
6. Para el juego de colores, quédate en la pestaña **Diseño de gráfico**, grupo **Estilos de gráfico**, y haz clic en **[Change Colors]**. Elige una fila de **[Colorful]** o de **[Monochromatic]**. Es una acción que se califica aparte del estilo.
7. Si el formato que aplicaste a mano antes pelea con el estilo, selecciona el elemento, ve a la pestaña **Formato**, grupo **[Current Selection]**, y haz clic en **[Reset to Match Style]**.

<!-- ES-FIN MO200-5.3.2 -->

---

### 5.3.3 Add alternative text to charts for accessibility

**EN · texto fuente, no editar**

**Exam route**

1. Click the chart border so the whole chart object is selected. Handles must show around the outside of the chart, not around a series or a title.
2. Right-click the border and click **Alt Text...**. **TO CONFIRM**: on some builds this entry reads **Edit Alt Text...**. The **Alt Text** pane opens on the right of the window.
3. Type the description in the box. Write what the chart shows and what the reader is meant to take from it, in one or two sentences, not the word "chart".
4. If the chart is decorative and carries no information, select the **Mark as decorative** check box instead. The description box greys out.
5. Close the pane. There is no OK button: the text is stored as you type.

**Exam route through the Accessibility Checker** (the same tool as 1.5.4)

1. Go to the **Review** tab, **Accessibility** group, and click **Check Accessibility**.
2. The **Accessibility** pane lists errors under **Missing alternative text**.
3. Click the chart in the list. Excel selects it on the sheet.
4. Under **Recommended Actions**, click **Add a description**, which opens the same **Alt Text** pane.
5. Type the description and close the pane.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO200-5.3.3 -->

**Ruta de examen**

1. Haz clic en el borde del gráfico para que quede seleccionado todo el objeto. Los controladores deben verse por fuera del gráfico, no alrededor de una serie o de un título.
2. Haz clic derecho en el borde y haz clic en **Texto alternativo...**. **TO CONFIRM**: en algunas versiones esta entrada dice **[Edit Alt Text...]**. Se abre el panel **Texto alternativo** a la derecha de la ventana.
3. Escribe la descripción en el cuadro. Di qué muestra el gráfico y qué se espera que el lector saque de él, en una o dos oraciones, no la palabra "gráfico".
4. Si el gráfico es decorativo y no lleva información, selecciona mejor la casilla **[Mark as decorative]**. El cuadro de la descripción se atenúa.
5. Cierra el panel. No hay botón Aceptar: el texto se guarda mientras escribes.

**Ruta de examen con el Comprobador de accesibilidad** (la misma herramienta del 1.5.4)

1. Ve a la pestaña **Revisar**, grupo **Accesibilidad**, y haz clic en **Comprobador de accesibilidad**.
2. El panel **Accesibilidad** enumera los errores bajo **[Missing alternative text]**.
3. Haz clic en el gráfico dentro de la lista. Excel lo selecciona en la hoja.
4. En **[Recommended Actions]**, haz clic en **[Add a description]**, que abre el mismo panel **Texto alternativo**.
5. Escribe la descripción y cierra el panel.

<!-- ES-FIN MO200-5.3.3 -->

---

## MO-201 Expert · Domain 1, Manage workbook options and settings

### 1.1.1 Copy macros between workbooks

**EN · texto fuente, no editar**

**Exam route**

1. Open both workbooks in the same Excel window. The source must be `.xlsm`, `.xlsb` or `.xlam`; a `.xlsx` cannot hold a module.
2. Go to the **Developer** tab, **Code** group, and click **Visual Basic**. If the Developer tab is not on the ribbon, put it there first, the three clicks are step 1 of objective 1.1.3.
3. In the Visual Basic Editor, open the **View** menu and click **Project Explorer**. The Project pane docks on the left.
4. Expand the source project, `VBAProject (Source.xlsm)`, then expand its **Modules** folder.
5. Drag `Module1` from the source project and drop it onto the destination project node, `VBAProject (Destination.xlsm)`. Dragging copies the module; it does not move it.
6. Alternative graded route, and the one to use when the two files cannot be open together: right-click `Module1`, click **Export File...**, save the `.bas`. Then right-click the destination `VBAProject` node, click **Import File...**, select the `.bas`, click **Open**.
7. Return to Excel with Alt+F11.
8. Go to the **File** tab, click **Save As**, open the **Save as type** list and choose **Excel Macro-Enabled Workbook (\*.xlsm)**. Save.
9. To make a macro available to every workbook instead of one, record or move it into `PERSONAL.XLSB`: in the **Record Macro** dialog set **Store macro in** to **Personal Macro Workbook**, or drag the module onto `VBAProject (PERSONAL.XLSB)` in the Project pane.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.1.1 -->

**Ruta de examen**

1. Abre los dos libros en la misma ventana de Excel. El origen tiene que ser `.xlsm`, `.xlsb` o `.xlam`; un `.xlsx` no puede contener un módulo.
2. Ve a la pestaña **Programador**, grupo **[Code]**, y haz clic en **Visual Basic**. Si la pestaña Programador no está en la cinta de opciones, ponla ahí primero: esos tres clics son el paso 1 del objetivo 1.1.3.
3. En el editor de Visual Basic, abre el menú **Vista** y haz clic en **[Project Explorer]**. El panel de proyecto se acopla del lado izquierdo.
4. Expande el proyecto de origen, `VBAProject (Source.xlsm)`, y luego expande su carpeta **[Modules]**.
5. Arrastra `Module1` del proyecto de origen y suéltalo sobre el nodo del proyecto de destino, `VBAProject (Destination.xlsm)`. Arrastrar copia el módulo, no lo mueve.
6. Ruta alterna que también puntúa, y la que se usa cuando los dos archivos no pueden estar abiertos al mismo tiempo: haz clic derecho en `Module1`, haz clic en **[Export File...]** y guarda el `.bas`. Después haz clic derecho en el nodo `VBAProject` de destino, haz clic en **[Import File...]**, selecciona el `.bas` y haz clic en **Abrir**.
7. Regresa a Excel con Alt+F11.
8. Ve a la pestaña **Archivo**, haz clic en **Guardar como**, abre la lista **[Save as type]** y elige **[Excel Macro-Enabled Workbook (\*.xlsm)]**. Guarda.
9. Para que una macro esté disponible en todos los libros y no en uno solo, grábala o muévela a `PERSONAL.XLSB`: en el cuadro de diálogo **Grabar macro** pon **[Store macro in]** en **[Personal Macro Workbook]**, o arrastra el módulo hasta `VBAProject (PERSONAL.XLSB)` en el panel de proyecto.

<!-- ES-FIN MO201-1.1.1 -->

---

### 1.1.2 Reference data in other workbooks

**EN · texto fuente, no editar**

**Exam route**

1. Open the source workbook and the destination workbook.
2. Click the destination cell and type `=`.
3. Go to the **View** tab, **Window** group, click **Switch Windows**, and pick the source workbook from the list.
4. Click the cell or drag the range you want. Excel writes the reference for you.
5. Press Enter. Excel jumps back to the destination workbook and finishes the formula.
6. While the source is open the reference reads `=[Source.xlsx]Sheet1!$A$1`. Close the source and the same formula rewrites itself as `='C:\Folder\[Source.xlsx]Sheet1'!$A$1`, with the path inside the single quotes. Both are correct, and that rewrite is the product telling you the link is real.
7. To give the external range a name, go to the **Formulas** tab, **Defined Names** group, click **Define Name** (Associate 2.3.1), type the **Name**, and in **Refers to** type `='C:\Folder\[Source.xlsx]Sheet1'!$A$1:$A$10`. Click **OK**. The name now works in any formula in the destination.
8. To manage the links, go to the **Data** tab, **Queries & Connections** group, and click **Edit Links**. The **Edit Links** dialog lists each **Source** with its **Type**, **Update** mode and **Status**, and carries the buttons **Update Values**, **Change Source...**, **Open Source**, **Break Link** and **Check Status**.
9. Click **Startup Prompt...** in that dialog to choose whether the user is asked to update on open.
10. **Break Link** converts every formula that points at that source into its current value, permanently. Use it only when asked.

The label **Edit Links** was read back from the product on the professor's build. Recent Microsoft 365 builds relabel the Data tab button **Workbook Links** and open a task pane instead of the dialog. **TO CONFIRM** which of the two the lab machines show.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.1.2 -->

**Ruta de examen**

1. Abre el libro de origen y el libro de destino.
2. Haz clic en la celda de destino y escribe `=`.
3. Ve a la pestaña **Vista**, grupo **Ventana**, haz clic en **Cambiar ventanas** y elige el libro de origen de la lista.
4. Haz clic en la celda o arrastra el rango que quieras. Excel escribe la referencia por ti.
5. Presiona Entrar. Excel regresa al libro de destino y termina la fórmula.
6. Mientras el origen está abierto, la referencia se lee `=[Source.xlsx]Sheet1!$A$1`. Cierra el origen y esa misma fórmula se reescribe sola como `='C:\Folder\[Source.xlsx]Sheet1'!$A$1`, con la ruta dentro de las comillas simples. Las dos formas son correctas, y esa reescritura es la forma en que el producto te avisa que el vínculo es real.
7. Para darle un nombre al rango externo, ve a la pestaña **Fórmulas**, grupo **Nombres definidos**, haz clic en **Asignar nombre** (Associate 2.3.1), escribe el **Nombre** y en **Se refiere a** escribe `='C:\Folder\[Source.xlsx]Sheet1'!$A$1:$A$10`. Haz clic en **Aceptar**. El nombre ya sirve en cualquier fórmula del libro de destino.
8. Para administrar los vínculos, ve a la pestaña **Datos**, grupo **Consultas y conexiones**, y haz clic en **Editar vínculos**. El cuadro de diálogo **Editar vínculos** lista cada **[Source]** con su **Tipo**, su modo de **[Update]** y su **[Status]**, y trae los botones **[Update Values]**, **[Change Source...]**, **[Open Source]**, **[Break Link]** y **[Check Status]**.
9. Haz clic en **[Startup Prompt...]** dentro de ese cuadro de diálogo para decidir si al abrir se le pregunta al usuario si quiere actualizar.
10. **[Break Link]** convierte cada fórmula que apunta a ese origen en su valor actual, de forma permanente. Úsalo solo cuando te lo pidan.

La etiqueta **Editar vínculos** se leyó del producto en la máquina del profesor. Las versiones recientes de Microsoft 365 le cambian el nombre a ese botón de la pestaña Datos por **[Workbook Links]** y abren un panel de tareas en lugar del cuadro de diálogo. **TO CONFIRM** cuál de los dos muestran las máquinas del laboratorio.

<!-- ES-FIN MO201-1.1.2 -->

---

### 1.1.3 Enable macros in a workbook

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Options**. In the **Excel Options** dialog click **Customize Ribbon**. In the **Main Tabs** list on the right, select the **Developer** check box. Click **OK**. This is the step 1.1.1 and 3.6.1 both depend on.
2. Go to the **Developer** tab, **Code** group, and click **Macro Security**. The Trust Center opens directly on the **Macro Settings** pane.
3. Select **Disable all macros with notification**. This is the setting the exam expects, because it blocks by default and still lets you enable per file. Current Microsoft 365 builds word the same option **Disable VBA macros with notification**. **TO CONFIRM** which wording the lab build shows.
4. Click **OK**.
5. Close the macro-enabled workbook and open it again. A Message Bar appears under the ribbon reading SECURITY WARNING Macros have been disabled, with an **Enable Content** button. Click it. The decision is remembered for that file.
6. If the file came from the internet or from email, the banner is red, it reads that macros are blocked, and there is no Enable Content button. Close the file. In File Explorer, right-click it, click **Properties**, and on the **General** tab select the **Unblock** check box at the bottom. Click **OK** and reopen.
7. To stop the prompt for a folder you control, go to the **File** tab, **Options**, **Trust Center**, and click **Trust Center Settings...**. Click **Trusted Locations**, then **Add new location...**. Click **Browse...**, select the folder, select **Subfolders of this location are also trusted**, click **OK** three times.
8. Save the file so the macro survives: **File** tab, **Save As**, **Save as type**, **Excel Macro-Enabled Workbook (\*.xlsm)**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.1.3 -->

**Ruta de examen**

1. Ve a la pestaña **Archivo** y haz clic en **Opciones**. En el cuadro de diálogo **Opciones de Excel** haz clic en **[Customize Ribbon]**. En la lista **[Main Tabs]** de la derecha, selecciona la casilla **Programador**. Haz clic en **Aceptar**. Este es el paso del que dependen tanto 1.1.1 como 3.6.1.
2. Ve a la pestaña **Programador**, grupo **[Code]**, y haz clic en **[Macro Security]**. El [Trust Center] se abre directo en el panel **[Macro Settings]**.
3. Selecciona **[Disable all macros with notification]**. Esta es la opción que espera el examen, porque bloquea de forma predeterminada y aun así te deja habilitar archivo por archivo. Las versiones actuales de Microsoft 365 escriben esa misma opción como **[Disable VBA macros with notification]**. **TO CONFIRM** cuál de las dos redacciones muestra la instalación del laboratorio.
4. Haz clic en **Aceptar**.
5. Cierra el libro habilitado para macros y ábrelo otra vez. Debajo de la cinta de opciones aparece una barra de mensajes que dice SECURITY WARNING Macros have been disabled, con un botón **[Enable Content]**. Haz clic en él. La decisión queda guardada para ese archivo.
6. Si el archivo llegó de internet o de un correo, el aviso es rojo, dice que las macros están bloqueadas y no trae botón [Enable Content]. Cierra el archivo. En el Explorador de archivos, haz clic derecho en él, haz clic en **Propiedades** y, en la pestaña **General**, selecciona la casilla **[Unblock]** que está hasta abajo. Haz clic en **Aceptar** y vuelve a abrirlo.
7. Para que deje de preguntar en una carpeta que tú controlas, ve a la pestaña **Archivo**, **Opciones**, **[Trust Center]**, y haz clic en **[Trust Center Settings...]**. Haz clic en **[Trusted Locations]** y luego en **[Add new location...]**. Haz clic en **[Browse...]**, selecciona la carpeta, selecciona **[Subfolders of this location are also trusted]** y haz clic en **Aceptar** tres veces.
8. Guarda el archivo para que la macro sobreviva: pestaña **Archivo**, **Guardar como**, **[Save as type]**, **[Excel Macro-Enabled Workbook (\*.xlsm)]**.

<!-- ES-FIN MO201-1.1.3 -->

---

### 1.1.4 Manage workbook versions

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Info**.
2. Read the **Manage Workbook** section. Each autosaved version is listed with its time stamp, and the ones Excel kept because the file was closed without saving carry the label (when I closed without saving).
3. Click a version. It opens read-only in a second window with a Message Bar carrying **Restore** and **Compare**. Click **Restore** to overwrite the current file with that version, and click **OK** on the confirmation.
4. For a file that was never saved at all, go to the **File** tab, **Open**, click **Recent**, scroll to the bottom of the list and click **Recover Unsaved Workbooks**. The Unsaved Files folder opens. Select the `.xlsb` draft, click **Open**, and click **Save As** on the Message Bar.
5. The same command sits at **File** tab, **Info**, **Manage Workbook**, **Recover Unsaved Workbooks**.
6. To control how often versions are made, go to the **File** tab, **Options**, and click **Save**. Set **Save AutoRecover information every N minutes**, and select **Keep the last AutoRecovered version if I close without saving**. Read the **AutoRecover file location** box, which is where the drafts live.
7. Click **OK**.
8. On a file stored on OneDrive or SharePoint in Microsoft 365 the same place on the Info pane reads **Version History** instead of **Manage Workbook**, and it opens a task pane on the right rather than a list. **TO CONFIRM** which of the two the lab machines show for a local file.

Read back from the professor's build: AutoRecover is enabled and the interval is 10 minutes, so the Options pane is already set to a value the class can watch change.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.1.4 -->

**Ruta de examen**

1. Ve a la pestaña **Archivo** y haz clic en **Información**.
2. Lee la sección **[Manage Workbook]**. Cada versión guardada de forma automática aparece con su hora, y las que Excel conservó porque el archivo se cerró sin guardar traen la etiqueta (when I closed without saving).
3. Haz clic en una versión. Se abre como solo lectura en una segunda ventana, con una barra de mensajes que trae **[Restore]** y **[Compare]**. Haz clic en **[Restore]** para sobrescribir el archivo actual con esa versión, y haz clic en **Aceptar** en la confirmación.
4. Para un archivo que nunca se guardó, ve a la pestaña **Archivo**, **Abrir**, haz clic en **Recientes**, baja hasta el final de la lista y haz clic en **[Recover Unsaved Workbooks]**. Se abre la carpeta Unsaved Files. Selecciona el borrador `.xlsb`, haz clic en **Abrir** y haz clic en **Guardar como** en la barra de mensajes.
5. El mismo comando está en la pestaña **Archivo**, **Información**, **[Manage Workbook]**, **[Recover Unsaved Workbooks]**.
6. Para controlar cada cuánto se generan las versiones, ve a la pestaña **Archivo**, **Opciones**, y haz clic en **Guardar**. Ajusta **[Save AutoRecover information every N minutes]** y selecciona **[Keep the last AutoRecovered version if I close without saving]**. Lee el cuadro **[AutoRecover file location]**, que es donde viven los borradores.
7. Haz clic en **Aceptar**.
8. En un archivo guardado en OneDrive o en SharePoint con Microsoft 365, ese mismo lugar del panel Información dice **[Version History]** en vez de **[Manage Workbook]**, y abre un panel de tareas a la derecha en lugar de una lista. **TO CONFIRM** cuál de los dos muestran las máquinas del laboratorio con un archivo local.

Leído de la máquina del profesor: la recuperación automática está activada y el intervalo es de 10 minutos, así que el panel de opciones ya trae un valor que el grupo puede ver cambiar.

<!-- ES-FIN MO201-1.1.4 -->

---

### 1.2.1 Restrict editing

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Info**.
2. Click **Protect Workbook**. The menu lists **Always Open Read-Only**, **Encrypt with Password**, **Protect Current Sheet**, **Protect Workbook Structure**, **Restrict Access**, **Add a Digital Signature** and **Mark as Final**.
3. *Mark as Final:* click **Mark as Final**. Click **OK** on the message that says the workbook will be marked as final and then saved, and **OK** on the second message that explains what marking as final does.
4. *Password to open the file:* **Protect Workbook**, **Encrypt with Password**. In the **Encrypt Document** dialog type the password in the **Password** box and click **OK**. Retype it in the **Reenter password** box and click **OK**. Then save the file, the password only exists once the file is written.
5. *Always Open Read-Only:* **Protect Workbook**, **Always Open Read-Only**. Save.
6. *Password to modify,* which is a different thing from the password to open: **File** tab, **Save As**, **Browse**. In the **Save As** dialog click the **Tools** button next to Save and click **General Options...**. Type in **Password to modify**, and in **Password to open** if both are wanted. Select **Read-only recommended**. Click **OK**, retype each password in **Confirm Password**, click **Save**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.2.1 -->

**Ruta de examen**

1. Ve a la pestaña **Archivo** y haz clic en **Información**.
2. Haz clic en **Proteger libro**. El menú lista **[Always Open Read-Only]**, **[Encrypt with Password]**, **[Protect Current Sheet]**, **[Protect Workbook Structure]**, **[Restrict Access]**, **[Add a Digital Signature]** y **Marcar como final**.
3. *Marcar como final:* haz clic en **Marcar como final**. Haz clic en **Aceptar** en el mensaje que dice que el libro se va a marcar como final y luego se va a guardar, y **Aceptar** en el segundo mensaje, el que explica qué hace marcarlo como final.
4. *Contraseña para abrir el archivo:* **Proteger libro**, **[Encrypt with Password]**. En el cuadro de diálogo **[Encrypt Document]** escribe la contraseña en el cuadro **[Password]** y haz clic en **Aceptar**. Vuelve a escribirla en el cuadro **[Reenter password]** y haz clic en **Aceptar**. Después guarda el archivo: la contraseña solo existe una vez que el archivo se escribe.
5. *[Always Open Read-Only]:* **Proteger libro**, **[Always Open Read-Only]**. Guarda.
6. *Contraseña para modificar,* que no es lo mismo que la contraseña para abrir: pestaña **Archivo**, **Guardar como**, **[Browse]**. En el cuadro de diálogo **Guardar como** haz clic en el botón **[Tools]** que está junto a Guardar y haz clic en **[General Options...]**. Escribe en **[Password to modify]**, y en **[Password to open]** si quieres las dos. Selecciona **[Read-only recommended]**. Haz clic en **Aceptar**, vuelve a escribir cada contraseña en **[Confirm Password]** y haz clic en **Guardar**.

<!-- ES-FIN MO201-1.2.1 -->

---

### 1.2.2 Protect worksheets and cell ranges

**EN · texto fuente, no editar**

**Exam route**

1. Click the **Select All** button at the corner where the row and column headers meet, or press Ctrl+A.
2. Press Ctrl+1, or go to the **Home** tab, **Font** group, and click the dialog box launcher.
3. In **Format Cells** (Associate 2.2.6) go to the **Protection** tab and clear the **Locked** check box. Click **OK**. Nothing visible happens. Every cell is now unlocked, which is the opposite of Excel's default and the step nobody remembers.
4. Select only the cells that must stay locked, for example the column of formulas.
5. Press Ctrl+1 again. On the **Protection** tab select **Locked**, and select **Hidden** as well if the formula must not show in the formula bar. Click **OK**. Both check boxes were set in one visit to the dialog.
6. Go to the **Review** tab, **Protect** group, and click **Allow Edit Ranges**.
7. In the **Allow Users to Edit Ranges** dialog click **New...**. In the **New Range** dialog type the **Title**, set **Refers to cells** to the range, and type a **Range password**. Click **OK**, retype the password in **Confirm Password**, click **OK**.
8. Click **Permissions...** in New Range if named Windows users should edit without typing a password at all.
9. Back in **Allow Users to Edit Ranges**, click the **Protect Sheet...** button at the bottom. That button is the graded way into the next dialog, because it proves the two settings belong to one operation.
10. In the **Protect Sheet** dialog select **Protect worksheet and contents of locked cells**. Type a **Password to unprotect sheet**.
11. In the **Allow all users of this worksheet to** list, select the operations to permit: **Select locked cells**, **Select unlocked cells**, **Format cells**, **Format columns**, **Format rows**, **Insert columns**, **Insert rows**, **Insert hyperlinks**, **Delete columns**, **Delete rows**, **Sort**, **Use AutoFilter**, **Use PivotTable and PivotChart**, **Edit objects**, **Edit scenarios**. Clear **Select locked cells** if the locked cells must not even be clicked.
12. Click **OK**, retype the password in **Confirm Password**, click **OK**.

The check box list above matches the properties Excel exposes for a protected sheet, which were set and read back on the professor's build: AllowFormattingCells, AllowSorting, AllowFiltering, AllowUsingPivotTables, AllowInsertingRows and the rest. The Allow Edit Ranges entry was created with Title, Range and Password and read back intact.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.2.2 -->

**Ruta de examen**

1. Haz clic en el botón **[Select All]**, el de la esquina donde se juntan los encabezados de fila y de columna, o presiona Ctrl+A.
2. Presiona Ctrl+1, o ve a la pestaña **Inicio**, grupo **Fuente**, y haz clic en el [dialog box launcher].
3. En **Formato de celdas** (Associate 2.2.6) ve a la pestaña **Protección** y desmarca la casilla **Bloqueada**. Haz clic en **Aceptar**. No pasa nada visible. Ahora todas las celdas están desbloqueadas, que es lo contrario de como viene Excel de fábrica y el paso que nadie recuerda.
4. Selecciona solo las celdas que deben quedar bloqueadas, por ejemplo la columna de fórmulas.
5. Presiona Ctrl+1 otra vez. En la pestaña **Protección** selecciona **Bloqueada**, y selecciona también **Oculta** si la fórmula no debe verse en la barra de fórmulas. Haz clic en **Aceptar**. Las dos casillas quedaron marcadas en una sola visita al cuadro de diálogo.
6. Ve a la pestaña **Revisar**, grupo **Proteger**, y haz clic en **Permitir editar rangos**.
7. En el cuadro de diálogo **Permitir que los usuarios editen rangos** haz clic en **[New...]**. En el cuadro de diálogo **[New Range]** escribe el **Título**, pon **[Refers to cells]** en el rango y escribe una **[Range password]**. Haz clic en **Aceptar**, vuelve a escribir la contraseña en **[Confirm Password]** y haz clic en **Aceptar**.
8. Haz clic en **[Permissions...]** dentro de [New Range] si quieres que ciertos usuarios de Windows editen sin escribir ninguna contraseña.
9. De regreso en **Permitir que los usuarios editen rangos**, haz clic en el botón **Proteger hoja...** que está hasta abajo. Ese botón es la forma que puntúa de entrar al siguiente cuadro de diálogo, porque demuestra que las dos configuraciones son una sola operación.
10. En el cuadro de diálogo **Proteger hoja** selecciona **[Protect worksheet and contents of locked cells]**. Escribe una **Contraseña para desproteger la hoja**.
11. En la lista **Permitir a los usuarios de esta hoja de cálculo**, selecciona las operaciones que quieres permitir: **Seleccionar celdas bloqueadas**, **Seleccionar celdas desbloqueadas**, **Formato de celdas**, **Aplicar formato a columnas**, **Aplicar formato a filas**, **Insertar columnas**, **Insertar filas**, **Insertar hipervínculos**, **Eliminar columnas**, **Eliminar filas**, **Ordenar**, **[Use AutoFilter]**, **[Use PivotTable and PivotChart]**, **[Edit objects]**, **[Edit scenarios]**. Desmarca **Seleccionar celdas bloqueadas** si en las celdas bloqueadas ni siquiera se debe poder hacer clic.
12. Haz clic en **Aceptar**, vuelve a escribir la contraseña en **[Confirm Password]** y haz clic en **Aceptar**.

La lista de casillas de arriba corresponde a las propiedades que Excel expone para una hoja protegida, que se configuraron y se volvieron a leer en la máquina del profesor: AllowFormattingCells, AllowSorting, AllowFiltering, AllowUsingPivotTables, AllowInsertingRows y las demás. La entrada de Permitir editar rangos se creó con Title, Range y Password, y se leyó de vuelta intacta.

<!-- ES-FIN MO201-1.2.2 -->

---

### 1.2.3 Protect workbook structure

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **Review** tab, **Protect** group, and click **Protect Workbook**.
2. The **Protect Structure and Windows** dialog opens. Select the **Structure** check box.
3. Type a password in the **Password (optional)** box.
4. Click **OK**. Retype the password in the **Confirm Password** dialog and click **OK**.
5. The same dialog is also reached from **File** tab, **Info**, **Protect Workbook**, **Protect Workbook Structure**. Either entry counts.
6. To lift it, click **Protect Workbook** again on the Review tab and type the password.

The **Windows** check box in the same dialog is dimmed on current Microsoft 365 builds; window protection is retired there. On the professor's build the structure flag was set and read back as protected while the windows flag stayed off, so plan the demonstration around Structure only.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.2.3 -->

**Ruta de examen**

1. Ve a la pestaña **Revisar**, grupo **Proteger**, y haz clic en **Proteger libro**.
2. Se abre el cuadro de diálogo **[Protect Structure and Windows]**. Selecciona la casilla **[Structure]**.
3. Escribe una contraseña en el cuadro **[Password (optional)]**.
4. Haz clic en **Aceptar**. Vuelve a escribir la contraseña en el cuadro de diálogo **[Confirm Password]** y haz clic en **Aceptar**.
5. Al mismo cuadro de diálogo se llega también desde la pestaña **Archivo**, **Información**, **Proteger libro**, **[Protect Workbook Structure]**. Cualquiera de las dos entradas cuenta.
6. Para quitarla, haz clic otra vez en **Proteger libro** en la pestaña Revisar y escribe la contraseña.

La casilla **[Windows]** de ese mismo cuadro de diálogo aparece atenuada en las versiones actuales de Microsoft 365; ahí la protección de ventanas ya no existe. En la máquina del profesor la marca de estructura se puso y se leyó de vuelta como protegida mientras la de ventanas se quedó apagada, así que arma la demostración solo con [Structure].

<!-- ES-FIN MO201-1.2.3 -->

---

### 1.2.4 Configure formula calculation options

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **Formulas** tab, **Calculation** group, and click **Calculation Options**.
2. Pick one of the three entries: **Automatic**, **Automatic Except for Data Tables**, **Manual**.
3. With Manual set, nothing recalculates until you ask. Press F9 to recalculate every open workbook, or Shift+F9 for the active sheet only.
4. The same two commands sit on the ribbon beside the menu: **Formulas** tab, **Calculation** group, **Calculate Now** and **Calculate Sheet**.
5. To reach the same three options from the settings side, go to the **File** tab, **Options**, and click **Formulas**. The **Calculation options** section at the top of the pane holds the same radio buttons plus the check box **Recalculate workbook before saving**.
6. For iterative calculation, stay on **File** tab, **Options**, **Formulas**. Select **Enable iterative calculation**. Set **Maximum Iterations** and **Maximum Change**. Click **OK**.
7. For rounding to what is displayed, go to the **File** tab, **Options**, **Advanced**, and scroll to the **When calculating this workbook** section. Select **Set precision as displayed**. Excel warns that data will permanently lose accuracy. Click **OK**, then **OK** again.

Read back from the professor's build: calculation mode Automatic, iterative calculation off, Maximum Iterations 100, Maximum Change 0.001.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.2.4 -->

**Ruta de examen**

1. Ve a la pestaña **Fórmulas**, grupo **Cálculo**, y haz clic en **Opciones de cálculo**.
2. Elige una de las tres entradas: **[Automatic]**, **[Automatic Except for Data Tables]**, **[Manual]**.
3. Con Manual puesto, nada se recalcula hasta que tú lo pidas. Presiona F9 para recalcular todos los libros abiertos, o Mayús+F9 para recalcular solo la hoja activa.
4. Los mismos dos comandos están en la cinta de opciones, junto al menú: pestaña **Fórmulas**, grupo **Cálculo**, **[Calculate Now]** y **[Calculate Sheet]**.
5. Para llegar a las mismas tres opciones por el lado de la configuración, ve a la pestaña **Archivo**, **Opciones**, y haz clic en **Fórmulas**. La sección **Opciones de cálculo**, hasta arriba del panel, trae los mismos botones de opción más la casilla **[Recalculate workbook before saving]**.
6. Para el cálculo iterativo, quédate en la pestaña **Archivo**, **Opciones**, **Fórmulas**. Selecciona **[Enable iterative calculation]**. Ajusta **[Maximum Iterations]** y **[Maximum Change]**. Haz clic en **Aceptar**.
7. Para redondear a lo que se muestra, ve a la pestaña **Archivo**, **Opciones**, **Avanzadas**, y baja hasta la sección **[When calculating this workbook]**. Selecciona **[Set precision as displayed]**. Excel advierte que los datos van a perder precisión de forma permanente. Haz clic en **Aceptar** y luego otra vez en **Aceptar**.

Leído de la máquina del profesor: modo de cálculo en [Automatic], cálculo iterativo apagado, [Maximum Iterations] en 100 y [Maximum Change] en 0.001.

<!-- ES-FIN MO201-1.2.4 -->

---

### 1.2.5 Manage comments

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell.
2. Go to the **Review** tab, **Comments** group, and click **New Comment**. A box opens anchored to the cell.
3. Type the text and click the **Post** button, the small arrow at the bottom right of the box, or press Ctrl+Enter.
4. To answer one, click the comment and type in the **Reply** box, then click **Post**. The thread grows downward. This is what makes it a comment and not a note.
5. To change your own text, point at the comment, click the **...** button at its top right, and click **Edit comment**.
6. To close a thread without deleting it, click **...** and click **Resolve thread**. The thread greys out and stays.
7. To remove it, click **...** and click **Delete thread**. **TO CONFIRM** whether this build words it Delete thread or Delete comment.
8. To walk the sheet, use **Review** tab, **Comments** group, **Previous Comment** and **Next Comment**.
9. To see them all in one list, go to the **Review** tab, **Comments** group, and click **Show Comments**. The **Comments** pane opens on the right and lists every thread on the sheet in order.
10. Notes are the older yellow boxes and live on a separate button. Go to the **Review** tab, **Notes** group, and use **New Note**, **Edit Note**, **Previous Note**, **Next Note**, **Show All Notes** and **Convert to Comments**.
11. To print them, open the **Page Setup** dialog (Associate 1.3.1) and on the **Sheet** tab open the **Comments and notes** list and choose **At end of sheet** or **As displayed on sheet**. **TO CONFIRM** the list caption on this build; in Office 2019 it reads Comments.

Threaded comments and notes were both created on the professor's build and counted in two separate collections, which is the hard proof that a note is not a comment on this version.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.2.5 -->

**Ruta de examen**

1. Selecciona la celda.
2. Ve a la pestaña **Revisar**, grupo **Comentarios**, y haz clic en **Nuevo comentario**. Se abre un cuadro anclado a la celda.
3. Escribe el texto y haz clic en el botón **[Post]**, la flechita de la esquina inferior derecha del cuadro, o presiona Ctrl+Entrar.
4. Para responder uno, haz clic en el comentario y escribe en el cuadro **[Reply]**, luego haz clic en **[Post]**. El hilo crece hacia abajo. Eso es lo que lo hace un comentario y no una nota.
5. Para cambiar tu propio texto, coloca el puntero sobre el comentario, haz clic en el botón **...** de su esquina superior derecha y haz clic en **[Edit comment]**.
6. Para cerrar un hilo sin borrarlo, haz clic en **...** y haz clic en **[Resolve thread]**. El hilo se pone gris y se queda ahí.
7. Para quitarlo, haz clic en **...** y haz clic en **[Delete thread]**. **TO CONFIRM** si esta instalación lo llama Delete thread o Delete comment.
8. Para recorrer la hoja, usa la pestaña **Revisar**, grupo **Comentarios**, **[Previous Comment]** y **[Next Comment]**.
9. Para verlos todos en una sola lista, ve a la pestaña **Revisar**, grupo **Comentarios**, y haz clic en **[Show Comments]**. El panel **Comentarios** se abre a la derecha y lista en orden todos los hilos de la hoja.
10. Las notas son los cuadros amarillos de antes y viven en otro botón. Ve a la pestaña **Revisar**, grupo **[Notes]**, y usa **Nueva nota**, **[Edit Note]**, **[Previous Note]**, **[Next Note]**, **[Show All Notes]** y **[Convert to Comments]**.
11. Para imprimirlos, abre el cuadro de diálogo **Configurar página** (Associate 1.3.1) y, en la pestaña **Hoja**, abre la lista **[Comments and notes]** y elige **[At end of sheet]** o **[As displayed on sheet]**. **TO CONFIRM** el nombre de esa lista en esta instalación; en Office 2019 dice Comments.

En la máquina del profesor se crearon comentarios con hilo y notas, y se contaron en dos colecciones distintas, que es la prueba dura de que en esta versión una nota no es un comentario.

<!-- ES-FIN MO201-1.2.5 -->

---

### 1.3.1 Configure editing and display languages

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **File** tab and click **Options**.
2. In the **Excel Options** dialog click **Language** in the left column.
3. Under **Office display Language**, select the language in the list and click **Set as Preferred**. If the language you need is not listed, click **Install additional display languages from Office.com** and follow the download.
4. Under **Office authoring languages and proofing**, click **Add a Language...**. Select the language in the list, click **Add**. Then select it in the pane and click **Set as Preferred** to make it the editing language.
5. Read the **Proofing** column in that same list. Each authoring language reads **Proofing installed** or **Proofing not installed**. Installing a display language and having proofing for it are two different things, and the exam separates them.
6. Click **OK**. A message says the change takes effect the next time you start Office.
7. Close Excel completely and reopen it.

Office 2019 words the same pane differently: two blocks headed **Choose Editing Languages** and **Choose Display and Help Languages**, each with a **Set as Default** button rather than **Set as Preferred**. **TO CONFIRM** which wording the lab build shows, since MO-201 is the 2019 exam.

Read back from the professor's build: display language 1033, install language 2058, help 1033. That machine already has the two settings pulling in different directions, which makes it the right one to demonstrate on.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.3.1 -->

**Ruta de examen**

1. Ve a la pestaña **Archivo** y haz clic en **Opciones**.
2. En el cuadro de diálogo **Opciones de Excel** haz clic en **Idioma**, en la columna de la izquierda.
3. En **[Office display Language]**, selecciona el idioma de la lista y haz clic en **[Set as Preferred]**. Si el idioma que necesitas no aparece, haz clic en **[Install additional display languages from Office.com]** y sigue la descarga.
4. En **[Office authoring languages and proofing]**, haz clic en **[Add a Language...]**. Selecciona el idioma de la lista y haz clic en **[Add]**. Luego selecciónalo en el panel y haz clic en **[Set as Preferred]** para volverlo el idioma de edición.
5. Lee la columna **Revisión** de esa misma lista. Cada idioma de creación dice **[Proofing installed]** o **[Proofing not installed]**. Instalar un idioma de presentación y tener corrección para ese idioma son dos cosas distintas, y el examen las separa.
6. Haz clic en **Aceptar**. Un mensaje avisa que el cambio se aplica la próxima vez que inicies Office.
7. Cierra Excel por completo y vuelve a abrirlo.

Office 2019 redacta ese mismo panel de otra forma: dos bloques con los títulos **[Choose Editing Languages]** y **[Choose Display and Help Languages]**, cada uno con un botón **[Set as Default]** en lugar de **[Set as Preferred]**. **TO CONFIRM** cuál de las dos redacciones muestra la instalación del laboratorio, porque MO-201 es el examen de 2019.

Leído de la máquina del profesor: idioma de presentación 1033, idioma de instalación 2058, ayuda 1033. Esa máquina ya trae las dos configuraciones jalando para lados distintos, y por eso es la indicada para la demostración.

<!-- ES-FIN MO201-1.3.1 -->

---

### 1.3.2 Use language-specific features

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell or the text inside it.
2. Go to the **Review** tab, **Language** group, and click **Translate**. The Translator pane opens on the right. Set the **From** list and the **To** list, and read the result in the lower box. **TO CONFIRM** whether this build labels the button Translate or Translate Selection.
3. To set the language the spell checker uses, go to the **Review** tab, **Language** group, click **Language**, then **Set Proofing Language...**. Select the language, click **OK**. **TO CONFIRM**: on some Excel builds this command sits only under **File** tab, **Options**, **Language** and not on the Review tab.
4. Go to the **Review** tab, **Proofing** group, and click **Spelling**, or press F7. The **Spelling** dialog shows a **Dictionary language** list; confirm it holds the language you set.
5. For a date or a currency that belongs to a locale rather than to your own, press Ctrl+1. On the **Number** tab select **Date** in the **Category** list, open the **Locale (location)** list and pick the locale, then pick the pattern in the **Type** list. Click **OK**.
6. For a currency symbol from another locale, press Ctrl+1, **Number** tab, **Category** **Currency**, then open the **Symbol** list and choose. Set **Negative numbers** in the same visit to the dialog.
7. To read what Excel stored, press Ctrl+1 again and click **Custom** in the **Category** list. The **Type** box now shows the locale code in square brackets at the front of the format.

Verified on the professor's build: `[$-es-MX]dddd, d "de" mmmm "de" yyyy` displayed `lunes, 9 de marzo de 2026` on an English UI, and Excel stored the code back as `[$-80A]...`, replacing the language tag with its hexadecimal locale id. `[$-en-US]dddd, mmmm d, yyyy` on the same date displayed `Monday, March 9, 2026`.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-1.3.2 -->

**Ruta de examen**

1. Selecciona la celda o el texto que está dentro de ella.
2. Ve a la pestaña **Revisar**, grupo **Idioma**, y haz clic en **Traducir**. El panel Traductor se abre a la derecha. Ajusta la lista **[From]** y la lista **[To]**, y lee el resultado en el cuadro de abajo. **TO CONFIRM** si esta instalación llama al botón Translate o Translate Selection.
3. Para fijar el idioma que usa el corrector ortográfico, ve a la pestaña **Revisar**, grupo **Idioma**, haz clic en **Idioma** y luego en **[Set Proofing Language...]**. Selecciona el idioma y haz clic en **Aceptar**. **TO CONFIRM**: en algunas instalaciones de Excel este comando solo está en la pestaña **Archivo**, **Opciones**, **Idioma**, y no en la pestaña Revisar.
4. Ve a la pestaña **Revisar**, grupo **Revisión**, y haz clic en **Ortografía**, o presiona F7. El cuadro de diálogo **Ortografía** muestra una lista **[Dictionary language]**; confirma que tenga el idioma que fijaste.
5. Para una fecha o una moneda que pertenecen a otra configuración regional y no a la tuya, presiona Ctrl+1. En la pestaña **Número** selecciona **Fecha** en la lista **Categoría**, abre la lista **[Locale (location)]** y elige la configuración regional, luego elige el patrón en la lista **Tipo**. Haz clic en **Aceptar**.
6. Para un símbolo de moneda de otra configuración regional, presiona Ctrl+1, pestaña **Número**, **Categoría** **Moneda**, abre la lista **[Symbol]** y elige. Ajusta **[Negative numbers]** en esa misma visita al cuadro de diálogo.
7. Para leer lo que Excel guardó, presiona Ctrl+1 otra vez y haz clic en **Personalizada** en la lista **Categoría**. El cuadro **Tipo** ahora muestra el código de la configuración regional entre corchetes, al inicio del formato.

Verificado en la máquina del profesor: `[$-es-MX]dddd, d "de" mmmm "de" yyyy` mostró `lunes, 9 de marzo de 2026` con la interfaz en inglés, y Excel guardó el código de vuelta como `[$-80A]...`, cambiando la etiqueta de idioma por su identificador regional en hexadecimal. `[$-en-US]dddd, mmmm d, yyyy` en esa misma fecha mostró `Monday, March 9, 2026`.

<!-- ES-FIN MO201-1.3.2 -->

---

## MO-201 Expert · Domain 2, Manage and format data

### 2.1.1 Fill cells by using Flash Fill

**EN · texto fuente, no editar**

**Exam route**

1. Put the column you are filling immediately beside the column that holds the source text. Flash Fill reads the neighbouring columns and nothing further away.
2. Give the data a header row. Flash Fill uses it to decide where the data starts.
3. In the first cell of the empty column, type the answer for the first row exactly as it should end up, including the capitalisation and the separators. Press Enter.
4. Start typing the answer for the second row. After two or three characters Excel shows the whole column in grey as a preview.
5. Press Enter to accept the preview. The grey turns solid and the rest of the column fills.
6. If no preview appears, select the cell under the one you typed and go to the **Data** tab, **Data Tools** group, and click **Flash Fill**.
7. The same command also sits at **Home** tab, **Editing** group, **Fill**, **Flash Fill**.
8. After the fill, a small **Flash Fill Options** button appears beside the range. Open it to **Undo Flash Fill** or to **Accept suggestions**. **TO CONFIRM** the exact entries on this build.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.1.1 -->

**Ruta de examen**

1. Coloca la columna que vas a rellenar justo al lado de la columna que tiene el texto de origen. El relleno rápido lee las columnas vecinas y nada que esté más lejos.
2. Dale a los datos una fila de encabezado. El relleno rápido la usa para decidir dónde empiezan los datos.
3. En la primera celda de la columna vacía, escribe la respuesta de la primera fila tal como debe quedar, con sus mayúsculas y sus separadores. Presiona Entrar.
4. Empieza a escribir la respuesta de la segunda fila. Después de dos o tres caracteres, Excel muestra la columna completa en gris como vista previa.
5. Presiona Entrar para aceptar la vista previa. El gris se vuelve sólido y el resto de la columna se llena.
6. Si no aparece la vista previa, selecciona la celda que está debajo de la que escribiste y ve a la pestaña **Datos**, grupo **Herramientas de datos**, y haz clic en **Relleno rápido**.
7. El mismo comando también está en la pestaña **Inicio**, grupo **Edición**, **Rellenar**, **Relleno rápido**.
8. Después del relleno aparece un botón pequeño, **[Flash Fill Options]**, junto al rango. Ábrelo para **[Undo Flash Fill]** o para **[Accept suggestions]**. **TO CONFIRM**: las entradas exactas en esta instalación.

<!-- ES-FIN MO201-2.1.1 -->

---

### 2.1.2 Fill cells by using advanced Fill Series options

**EN · texto fuente, no editar**

The Associate half of this dialog is at 2.1.2 in MO-200; what follows is everything the drag cannot do.

**Exam route**

1. Type the starting value in the first cell.
2. Select the range that will hold the series, beginning with that cell.
3. Go to the **Home** tab, **Editing** group, click **Fill**, then click **Series...**. The **Series** dialog opens.
4. Under **Series in**, select **Rows** or **Columns** to match the direction of the selection. Excel guesses, and it guesses wrong when the selection is a single cell.
5. Under **Type**, select **Linear**, **Growth**, **Date** or **AutoFill**. Linear adds the step, Growth multiplies by it.
6. If you chose Date, the **Date unit** group becomes available. Select **Day**, **Weekday**, **Month** or **Year**. Weekday skips Saturday and Sunday.
7. Type the **Step value**.
8. Type the **Stop value** when the series must end at a number rather than at the end of the selection. With a Stop value you can select a single cell and let Excel decide how far to go.
9. Select **Trend** to fit a line, for Linear, or a curve, for Growth, through values already in the selection, instead of using Step value.
10. Click **OK**.
11. Alternative graded route, and the fast one: point at the fill handle, hold the RIGHT mouse button, drag, and release. The shortcut menu offers **Copy Cells**, **Fill Series**, **Fill Formatting Only**, **Fill Without Formatting**, **Fill Days**, **Fill Weekdays**, **Fill Months**, **Fill Years**, **Linear Trend**, **Growth Trend** and **Series...**, where Series... opens the same dialog.
12. For a custom list: go to the **File** tab, **Options**, **Advanced**, scroll to the **General** section and click **Edit Custom Lists...**. In the **Custom Lists** dialog type the entries in the **List entries** box, one per line, and click **Add**. Or click in the **Import list from cells** box, select the range on the sheet and click **Import**. Click **OK**, then **OK**.
13. Type any member of that list in a cell and drag the fill handle. The list continues in its own order and wraps.

Verified on the professor's build: Growth from 2 with a step of 3 produced 2, 6, 18, 54. A Date series with the Month unit stepped 31 January 2026 to February, March and April. Trend through 1, 3, 5 extended to 7, 9, 11. That machine already carries eight built-in custom lists rather than four (English `Sun`/`Sunday`/`Jan`/`January` and Spanish `Dom.`/`Domingo`/`ene`/`enero`) because the install language is Spanish Mexico while the interface is English. Drag a cell holding `enero` and the Spanish months follow.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.1.2 -->

La mitad Associate de este cuadro de diálogo está en el 2.1.2 del MO-200; lo que sigue es todo lo que el arrastre no puede hacer.

**Ruta de examen**

1. Escribe el valor inicial en la primera celda.
2. Selecciona el rango que va a llevar la serie, empezando por esa celda.
3. Ve a la pestaña **Inicio**, grupo **Edición**, haz clic en **Rellenar** y luego en **Serie...**. Se abre el cuadro de diálogo **Serie**.
4. En **[Series in]**, selecciona **Filas** o **Columnas** según la dirección de la selección. Excel adivina, y adivina mal cuando la selección es una sola celda.
5. En **Tipo**, selecciona **[Linear]**, **[Growth]**, **Fecha** o **[AutoFill]**. [Linear] suma el incremento, [Growth] multiplica por él.
6. Si elegiste Fecha, se habilita el grupo **[Date unit]**. Selecciona **[Day]**, **[Weekday]**, **[Month]** o **[Year]**. [Weekday] salta sábado y domingo.
7. Escribe el **[Step value]**.
8. Escribe el **[Stop value]** cuando la serie tenga que terminar en un número y no al final de la selección. Con un [Stop value] puedes seleccionar una sola celda y dejar que Excel decida hasta dónde llega.
9. Selecciona **[Trend]** para ajustar una recta, con [Linear], o una curva, con [Growth], a los valores que ya están en la selección, en lugar de usar [Step value].
10. Haz clic en **Aceptar**.
11. Ruta alternativa que también puntúa, y la rápida: apunta al controlador de relleno, mantén presionado el botón DERECHO del mouse, arrastra y suelta. El menú contextual ofrece **[Copy Cells]**, **[Fill Series]**, **[Fill Formatting Only]**, **[Fill Without Formatting]**, **[Fill Days]**, **[Fill Weekdays]**, **[Fill Months]**, **[Fill Years]**, **[Linear Trend]**, **[Growth Trend]** y **Serie...**, donde Serie... abre el mismo cuadro de diálogo.
12. Para una lista personalizada: ve a la pestaña **Archivo**, **Opciones**, **Avanzadas**, baja hasta la sección **General** y haz clic en **[Edit Custom Lists...]**. En el cuadro de diálogo **[Custom Lists]** escribe las entradas en el cuadro **[List entries]**, una por línea, y haz clic en **[Add]**. O haz clic en el cuadro **[Import list from cells]**, selecciona el rango en la hoja y haz clic en **[Import]**. Haz clic en **Aceptar** y otra vez en **Aceptar**.
13. Escribe cualquier miembro de esa lista en una celda y arrastra el controlador de relleno. La lista continúa en su propio orden y da la vuelta.

Verificado en la instalación del profesor: [Growth] desde 2 con un incremento de 3 produjo 2, 6, 18, 54. Una serie de tipo Fecha con la unidad [Month] llevó el 31 de enero de 2026 a febrero, marzo y abril. [Trend] sobre 1, 3, 5 se extendió a 7, 9, 11. Esa máquina ya trae ocho listas personalizadas integradas en lugar de cuatro (en inglés `Sun`/`Sunday`/`Jan`/`January` y en español `Dom.`/`Domingo`/`ene`/`enero`) porque el idioma de instalación es español de México mientras que la interfaz está en inglés. Arrastra una celda que contenga `enero` y siguen los meses en español.

<!-- ES-FIN MO201-2.1.2 -->

---

### 2.2.1 Create custom number formats

**EN · texto fuente, no editar**

**Exam route**

1. Select the cells.
2. Press Ctrl+1, or go to the **Home** tab, **Number** group, and click the dialog box launcher. **Format Cells** opens on the **Number** tab (Associate 2.2.6).
3. Build the closest match first with a real category. Select **Number**, set **Decimal places**, select **Use 1000 Separator (,)**, and choose an entry under **Negative numbers**. This step is not decoration: Excel remembers the code it just built.
4. Now select **Custom** at the bottom of the **Category** list. The **Type** box already shows the code from step 3, ready to edit.
5. Edit the code in the **Type** box. A custom format has up to four sections separated by semicolons, in this order: positive; negative; zero; text. Write two sections and Excel uses the second for everything negative and the first for zero. Write one and it applies to everything numeric.
6. Click **OK**.
7. To delete a code you no longer want, reopen Ctrl+1, **Custom**, select the code in the **Type** list and click **Delete**. Only custom codes can be deleted; the built-in ones have no Delete.

Codes that repay memorising, every one of them applied and read back on the professor's build:

- `#,##0.00 "kg"` puts a unit after the number and leaves the value a number. 1234.5 shows as `1,234.50 kg`.
- `#,##0.00;[Red](#,##0.00);"-";@` four sections: negatives red and in parentheses, zero as a dash, text passed through.
- `#,##0.00;[Red](#,##0.00);"-";"Note: "@` the fourth section can add its own text; `hello` shows as `Note: hello`.
- `[>=1000000]0.0,,"M";[>=1000]0.0,"K";0` two conditions in square brackets and a default. Each trailing comma divides by a thousand, so 12345678 shows as `12.3M`.
- `000-00-0000` fixed-width identifier. A zero placeholder keeps leading zeros; 42 shows as `000-00-0042`.
- `# ??/??` fractions with aligned denominators. 0.5 shows as `1/2`.
- `[h]:mm` elapsed time past 24 hours. The square brackets are what stop it wrapping.
- `;;;` three empty sections and nothing else hides the cell on screen while the value stays live in the formula bar.
- `[$-en-US]dddd, mmmm d, yyyy` a date in a named locale. Excel stores it back as `[$-409]...`.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.1 -->

**Ruta de examen**

1. Selecciona las celdas.
2. Presiona Ctrl+1, o ve a la pestaña **Inicio**, grupo **Número**, y haz clic en el [dialog box launcher]. **Formato de celdas** se abre en la pestaña **Número** (2.2.6 del Associate).
3. Arma primero la aproximación más cercana con una categoría real. Selecciona **Número**, ajusta **Posiciones decimales**, selecciona **[Use 1000 Separator (,)]** y elige una entrada en **[Negative numbers]**. Este paso no es adorno: Excel recuerda el código que acaba de construir.
4. Ahora selecciona **Personalizada**, hasta abajo de la lista **Categoría**. El cuadro **Tipo** ya muestra el código del paso 3, listo para editarse.
5. Edita el código en el cuadro **Tipo**. Un formato personalizado tiene hasta cuatro secciones separadas por punto y coma, en este orden: positivo; negativo; cero; texto. Si escribes dos secciones, Excel usa la segunda para todo lo negativo y la primera para el cero. Si escribes una, se aplica a todo lo numérico.
6. Haz clic en **Aceptar**.
7. Para borrar un código que ya no quieres, vuelve a abrir con Ctrl+1, ve a **Personalizada**, selecciona el código en la lista **Tipo** y haz clic en **Eliminar**. Solo se pueden borrar los códigos personalizados; los integrados no tienen Eliminar.

Códigos que vale la pena memorizar, todos aplicados y vueltos a leer en la instalación del profesor:

- `#,##0.00 "kg"` pone una unidad después del número y deja el valor como número. 1234.5 se muestra como `1,234.50 kg`.
- `#,##0.00;[Red](#,##0.00);"-";@` cuatro secciones: negativos en rojo y entre paréntesis, cero como un guion, el texto pasa tal cual.
- `#,##0.00;[Red](#,##0.00);"-";"Note: "@` la cuarta sección puede agregar su propio texto; `hello` se muestra como `Note: hello`.
- `[>=1000000]0.0,,"M";[>=1000]0.0,"K";0` dos condiciones entre corchetes y un valor predeterminado. Cada coma final divide entre mil, así que 12345678 se muestra como `12.3M`.
- `000-00-0000` identificador de ancho fijo. Un marcador de posición de cero conserva los ceros a la izquierda; 42 se muestra como `000-00-0042`.
- `# ??/??` fracciones con los denominadores alineados. 0.5 se muestra como `1/2`.
- `[h]:mm` tiempo transcurrido más allá de 24 horas. Los corchetes son lo que impide que dé la vuelta.
- `;;;` tres secciones vacías y nada más oculta la celda en pantalla mientras el valor sigue vivo en la barra de fórmulas.
- `[$-en-US]dddd, mmmm d, yyyy` una fecha en una configuración regional con nombre. Excel lo guarda de vuelta como `[$-409]...`.

<!-- ES-FIN MO201-2.2.1 -->

---

### 2.2.2 Configure data validation

**EN · texto fuente, no editar**

**Exam route**

1. Select the cells that will carry the rule.
2. Go to the **Data** tab, **Data Tools** group, and click **Data Validation**, the top half of the split button, which opens **Data Validation...**.
3. The dialog opens on the **Settings** tab. Open the **Allow** list: **Any value**, **Whole number**, **Decimal**, **List**, **Date**, **Time**, **Text length**, **Custom**.
4. Choose the type. A **Data** list appears with **between**, **not between**, **equal to**, **not equal to**, **greater than**, **less than**, **greater than or equal to**, **less than or equal to**. Fill the boxes it produces: **Minimum** and **Maximum**, or **Start date** and **End date**, or **Length**.
5. For **List**, type the entries in the **Source** box separated by commas, or click the collapse button at the right of the box and select the range on the sheet, or type `=` followed by a defined name. Keep the **In-cell dropdown** check box selected or there is no list to pick from.
6. For **Custom**, type a formula in the **Formula** box that returns TRUE for what is allowed. Write it for the top left cell of the selection and Excel shifts it across the rest, exactly as a copied formula shifts. Example: `=B2<=A2*0.1` to cap a bonus at a tenth of the salary.
7. Leave **Ignore blank** selected unless empty cells must be rejected too.
8. WITHOUT closing the dialog, go to the **Input Message** tab. Keep **Show input message when cell is selected**. Type a **Title** and an **Input message**.
9. WITHOUT closing the dialog, go to the **Error Alert** tab. Keep **Show error alert after invalid data is entered**. Open the **Style** list and pick **Stop**, **Warning** or **Information**, Stop refuses the entry, Warning asks, Information only tells. Type a **Title** and an **Error message**.
10. Click **OK**. Three tabs were configured in one operation, which is the point of the objective.
11. To push a change onto every cell that already shares the rule, reopen the dialog on one of them and select **Apply these changes to all other cells with the same settings** on the Settings tab before clicking OK.
12. To expose values typed before the rule existed, go to the **Data** tab, **Data Tools** group, click the **Data Validation** arrow, and click **Circle Invalid Data**. Red ovals appear around every offender. Clear them with **Clear Validation Circles** on the same menu.
13. To remove a rule, select the cells, open the dialog and click **Clear All**, then **OK**.

Everything above was set through the object model on the professor's build and read back: type, alert style, source, Ignore blank, In-cell dropdown, input title and message, error title and message.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.2 -->

**Ruta de examen**

1. Selecciona las celdas que van a llevar la regla.
2. Ve a la pestaña **Datos**, grupo **Herramientas de datos**, y haz clic en **Validación de datos**, la mitad superior del botón dividido, que abre **Validación de datos...**.
3. El cuadro de diálogo se abre en la pestaña **Configuración**. Abre la lista **Permitir**: **[Any value]**, **Número entero**, **Decimal**, **[List]**, **Fecha**, **[Time]**, **Longitud del texto**, **Personalizada**.
4. Elige el tipo. Aparece una lista **Datos** con **Entre**, **[not between]**, **Es igual a**, **[not equal to]**, **Es mayor que**, **Es menor que**, **mayor o igual que**, **[less than or equal to]**. Llena los cuadros que produce: **[Minimum]** y **[Maximum]**, o **[Start date]** y **[End date]**, o **[Length]**.
5. Para **[List]**, escribe las entradas en el cuadro **Origen** separadas por comas, o haz clic en el botón de contraer que está a la derecha del cuadro y selecciona el rango en la hoja, o escribe `=` seguido de un nombre definido. Deja seleccionada la casilla **[In-cell dropdown]** o no habrá lista de dónde elegir.
6. Para **Personalizada**, escribe en el cuadro **Fórmula** una fórmula que devuelva VERDADERO para lo que sí se permite. Escríbela para la celda superior izquierda de la selección y Excel la desplaza al resto, igual que se desplaza una fórmula copiada. Ejemplo: `=B2<=A2*0.1` para topar un bono en la décima parte del sueldo.
7. Deja seleccionada **[Ignore blank]** salvo que las celdas vacías también tengan que rechazarse.
8. SIN cerrar el cuadro de diálogo, ve a la pestaña **Mensaje de entrada**. Deja seleccionada la casilla **[Show input message when cell is selected]**. Escribe un **Título** y un **Mensaje de entrada**.
9. SIN cerrar el cuadro de diálogo, ve a la pestaña **Mensaje de error**. Deja seleccionada la casilla **[Show error alert after invalid data is entered]**. Abre la lista **Estilo** y elige **[Stop]**, **[Warning]** o **[Information]**: [Stop] rechaza la entrada, [Warning] pregunta, [Information] solo avisa. Escribe un **Título** y un **Mensaje de error**.
10. Haz clic en **Aceptar**. Se configuraron tres pestañas en una sola operación, que es el punto del objetivo.
11. Para empujar un cambio a todas las celdas que ya comparten la regla, vuelve a abrir el cuadro de diálogo en una de ellas y selecciona **[Apply these changes to all other cells with the same settings]** en la pestaña Configuración antes de hacer clic en Aceptar.
12. Para sacar a la luz los valores que se escribieron antes de que existiera la regla, ve a la pestaña **Datos**, grupo **Herramientas de datos**, haz clic en la flecha de **Validación de datos** y haz clic en **[Circle Invalid Data]**. Aparecen óvalos rojos alrededor de cada infractor. Quítalos con **[Clear Validation Circles]** en el mismo menú.
13. Para quitar una regla, selecciona las celdas, abre el cuadro de diálogo y haz clic en **Borrar todo**, luego en **Aceptar**.

Todo lo anterior se configuró desde el modelo de objetos en la instalación del profesor y se volvió a leer: tipo, estilo de alerta, origen, [Ignore blank], [In-cell dropdown], título y mensaje de entrada, título y mensaje de error.

<!-- ES-FIN MO201-2.2.2 -->

---

### 2.2.3 Group and ungroup data

**EN · texto fuente, no editar**

**Exam route**

1. Sort the data by the column you are about to group on. Groups made on unsorted data interleave and cannot be fixed afterwards.
2. Select the whole rows by dragging across their row headers, not the cells inside them.
3. Go to the **Data** tab, **Outline** group, and click **Group**, the top half of the split button.
4. If you selected cells rather than whole rows, the **Group** dialog appears and asks Rows or Columns. Select **Rows** and click **OK**.
5. Repeat on a subset of those rows to make an inner level. The outline bar to the left of the row headers gains level buttons numbered 1, 2, 3.
6. Collapse and expand with the minus and plus buttons on the outline bar, or jump straight to a depth with the numbered level buttons at the top of the bar.
7. To take one group apart, select its rows and go to the **Data** tab, **Outline** group, and click **Ungroup**, top half.
8. To remove the whole outline at once, click the **Ungroup** arrow and click **Clear Outline**.
9. To let Excel build it, click the **Group** arrow and click **Auto Outline**. Excel only accepts this when the sheet already contains summary formulas that point at the detail rows; otherwise it refuses with a message that it cannot create an outline.
10. To move the summary rows above the detail instead of below, go to the **Data** tab, **Outline** group, and click the dialog box launcher. In the **Settings** dialog clear **Summary rows below detail** or **Summary columns to right of detail**, then click **Create** to apply, or **OK** to keep the setting for the next outline.
11. **Show Detail** and **Hide Detail** in the same group act on whatever group the cursor is in.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.3 -->

**Ruta de examen**

1. Ordena los datos por la columna sobre la que vas a agrupar. Los grupos hechos sobre datos sin ordenar se entrelazan y después ya no hay cómo arreglarlos.
2. Selecciona las filas completas arrastrando por sus encabezados de fila, no las celdas de adentro.
3. Ve a la pestaña **Datos**, grupo **Esquema**, y haz clic en **Agrupar**, la mitad superior del botón dividido.
4. Si seleccionaste celdas en lugar de filas completas, aparece el cuadro de diálogo **Agrupar** y pregunta si filas o columnas. Selecciona **Filas** y haz clic en **Aceptar**.
5. Repite sobre un subconjunto de esas filas para hacer un nivel interior. En la barra de esquema, a la izquierda de los encabezados de fila, aparecen botones de nivel numerados 1, 2, 3.
6. Contrae y expande con los botones de menos y de más de la barra de esquema, o salta directo a una profundidad con los botones de nivel numerados que están arriba de la barra.
7. Para deshacer un grupo, selecciona sus filas y ve a la pestaña **Datos**, grupo **Esquema**, y haz clic en **Desagrupar**, mitad superior.
8. Para quitar todo el esquema de una vez, haz clic en la flecha de **Desagrupar** y luego en **[Clear Outline]**.
9. Para que Excel lo arme, haz clic en la flecha de **Agrupar** y luego en **[Auto Outline]**. Excel solo lo acepta cuando la hoja ya tiene fórmulas de resumen que apuntan a las filas de detalle; si no, se niega con un mensaje de que no puede crear un esquema.
10. Para mover las filas de resumen arriba del detalle en lugar de abajo, ve a la pestaña **Datos**, grupo **Esquema**, y haz clic en el [dialog box launcher]. En el cuadro de diálogo **Configuración** desmarca **[Summary rows below detail]** o **[Summary columns to right of detail]**, luego haz clic en **[Create]** para aplicarlo, o en **Aceptar** para guardar el ajuste para el siguiente esquema.
11. **[Show Detail]** y **[Hide Detail]**, en el mismo grupo, actúan sobre el grupo en el que esté parado el cursor.

<!-- ES-FIN MO201-2.2.3 -->

---

### 2.2.4 Calculate data by inserting subtotals and totals

**EN · texto fuente, no editar**

**Exam route**

1. Sort the list by the column that will break the groups. Go to the **Data** tab, **Sort & Filter** group, click **Sort**, choose the column in **Sort by**, click **OK**. Subtotals on unsorted data produce one group per row.
2. Click a single cell inside the list. Do not select the range; Excel expands to the whole block on its own.
3. Go to the **Data** tab, **Outline** group, and click **Subtotal**.
4. In the **Subtotal** dialog, open the **At each change in** list and select the column you just sorted by.
5. Open the **Use function** list and select one of Sum, Count, Average, Max, Min, Product, Count Numbers, StdDev, StdDevp, Var, Varp.
6. In the **Add subtotal to** list, select the check box of every column that gets a total and clear the rest. Excel preselects the last numeric column, which is rarely the one you want.
7. Leave **Replace current subtotals** selected on the first pass. CLEAR it when you run the dialog a second time to stack a second function on top of the first, otherwise the second run deletes the first.
8. Select **Page break between groups** when each group must print on its own page.
9. Leave **Summary below data** selected, or clear it to put the totals above their groups.
10. Click **OK**. Excel inserts rows carrying `SUBTOTAL` formulas and builds a three-level outline.
11. To take them all out, click a cell in the list, reopen the dialog and click **Remove All**.

Total row on a table, the other half of the objective, is Associate 3.2.3: **Table Design** tab, **Table Style Options** group, **Total Row** check box, then the drop-down on each total cell. What matters here is the code it writes. Verified on the professor's build: a table total row writes `=SUBTOTAL(109,Columna)`. The `1xx` codes ignore rows hidden by hand as well as rows hidden by a filter; the `9` codes ignore only the filtered ones. On unfiltered data `SUBTOTAL(9,...)`, `SUBTOTAL(109,...)` and `AGGREGATE(9,3,...)` all returned the same number, so the difference is only visible once rows are hidden.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.4 -->

**Ruta de examen**

1. Ordena la lista por la columna que va a marcar los cortes de grupo. Ve a la pestaña **Datos**, grupo **Ordenar y filtrar**, haz clic en **Ordenar**, elige la columna en **[Sort by]** y haz clic en **Aceptar**. Los subtotales sobre datos sin ordenar producen un grupo por fila.
2. Haz clic en una sola celda dentro de la lista. No selecciones el rango; Excel se extiende al bloque completo por su cuenta.
3. Ve a la pestaña **Datos**, grupo **Esquema**, y haz clic en **Subtotal**.
4. En el cuadro de diálogo **Subtotal**, abre la lista **Para cada cambio en** y selecciona la columna por la que acabas de ordenar.
5. Abre la lista **Usar función** y selecciona una de estas: **Suma**, **Recuento**, **Promedio**, **Máx**, **Mín**, **[Product]**, **Contar números**, **Desvest**, **[StdDevp]**, **Var**, **[Varp]**.
6. En la lista **Agregar subtotal a**, marca la casilla de cada columna que lleva total y desmarca las demás. Excel preselecciona la última columna numérica, que casi nunca es la que quieres.
7. Deja seleccionada **Reemplazar subtotales actuales** en la primera pasada. DESMÁRCALA cuando corras el cuadro de diálogo una segunda vez para apilar una segunda función sobre la primera, porque si no la segunda corrida borra la primera.
8. Selecciona **Salto de página entre grupos** cuando cada grupo tenga que imprimirse en su propia página.
9. Deja seleccionada **Resumen debajo de los datos**, o desmárcala para poner los totales arriba de sus grupos.
10. Haz clic en **Aceptar**. Excel inserta filas con fórmulas `SUBTOTALES` y arma un esquema de tres niveles.
11. Para quitarlos todos, haz clic en una celda de la lista, vuelve a abrir el cuadro de diálogo y haz clic en **Quitar todos**.

La fila de totales de una tabla, la otra mitad del objetivo, es el 3.2.3 del Associate: pestaña **Diseño de tabla**, grupo **Opciones de estilo de tabla**, casilla **Fila de totales**, y luego la lista desplegable de cada celda de total. Lo que importa aquí es el código que escribe. Verificado en la instalación del profesor: una fila de totales de tabla escribe `=SUBTOTALES(109,[Columna])`. Los códigos `1xx` ignoran tanto las filas ocultas a mano como las ocultas por un filtro; los códigos `9` ignoran solo las filtradas. Sobre datos sin filtrar, `SUBTOTALES(9,...)`, `SUBTOTALES(109,...)` y `AGGREGATE(9,3,...)` devolvieron el mismo número, así que la diferencia solo se ve cuando hay filas ocultas.

<!-- ES-FIN MO201-2.2.4 -->

---

### 2.2.5 Remove duplicate records

**EN · texto fuente, no editar**

**Exam route**

1. Make a copy of the sheet first. Right-click the sheet tab, click **Move or Copy...**, select **Create a copy**, click **OK**. This command deletes rows and does not put them back after a save.
2. Click one cell inside the list. Excel expands to the whole block.
3. Go to the **Data** tab, **Data Tools** group, and click **Remove Duplicates**.
4. In the **Remove Duplicates** dialog, select **My data has headers** when the first row holds the column names. Watch the **Columns** list as you click it: the entries switch between `Column A, Column B` and the real header names, which is the quickest confirmation the check box is right.
5. Use **Select All** or **Unselect All**, then select only the columns that define a duplicate. Two rows count as duplicates only when every selected column matches. Selecting all columns is the strictest test, selecting one is the loosest, and the task will say which.
6. Click **OK**. A message reports how many duplicate values were found and removed and how many unique values remain. Read it before clicking OK, because it is the only record of what happened.
7. Excel deletes the rows and the rows below move up. Nothing is hidden.

Non-destructive branch, which the exam asks for when it says extract or list the unique values:

8. Go to the **Data** tab, **Sort & Filter** group, and click **Advanced**. In the **Advanced Filter** dialog select **Copy to another location**, set **List range**, leave **Criteria range** empty, set **Copy to** to a single destination cell, select **Unique records only**, click **OK**.
9. Or mark them without touching them: **Home** tab, **Styles** group, **Conditional Formatting**, **Highlight Cells Rules**, **Duplicate Values...**, pick the format in the **with** list, click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.5 -->

**Ruta de examen**

1. Haz primero una copia de la hoja. Haz clic derecho en la [sheet tab], haz clic en **[Move or Copy...]**, selecciona **Crear una copia** y haz clic en **Aceptar**. Este comando borra filas y no las regresa después de guardar.
2. Haz clic en una celda dentro de la lista. Excel se extiende al bloque completo.
3. Ve a la pestaña **Datos**, grupo **Herramientas de datos**, y haz clic en **Quitar duplicados**.
4. En el cuadro de diálogo **Quitar duplicados**, selecciona **[My data has headers]** cuando la primera fila tenga los nombres de las columnas. Observa la lista **Columnas** mientras haces clic en la casilla: las entradas cambian entre `Columna A, Columna B` y los nombres reales de los encabezados, que es la confirmación más rápida de que la casilla está bien.
5. Usa **[Select All]** o **[Unselect All]**, y después selecciona solo las columnas que definen un duplicado. Dos filas cuentan como duplicadas solo cuando coinciden todas las columnas seleccionadas. Seleccionar todas las columnas es la prueba más estricta, seleccionar una es la más laxa, y la tarea va a decir cuál.
6. Haz clic en **Aceptar**. Un mensaje informa cuántos valores duplicados se encontraron y se quitaron y cuántos valores únicos quedan. Léelo antes de hacer clic en Aceptar, porque es el único registro de lo que pasó.
7. Excel borra las filas y las de abajo suben. No se oculta nada.

Rama no destructiva, la que pide el examen cuando dice extraer o listar los valores únicos:

8. Ve a la pestaña **Datos**, grupo **Ordenar y filtrar**, y haz clic en **Avanzadas**. En el cuadro de diálogo **Filtro avanzado** selecciona **Copiar a otra ubicación**, define **Rango de la lista**, deja vacío **Rango de criterios**, define **Copiar a** con una sola celda de destino, selecciona **solo registros únicos** y haz clic en **Aceptar**.
9. O márcalos sin tocarlos: pestaña **Inicio**, grupo **Estilos**, **Formato condicional**, **Resaltar reglas de celdas**, **Duplicar valores...**, elige el formato en la lista **con** y haz clic en **Aceptar**.

<!-- ES-FIN MO201-2.2.5 -->

---

### 2.3.1 Create custom conditional formatting rules

**EN · texto fuente, no editar**

This is where the **New Formatting Rule** dialog is written out; Associate 2.4.2 reaches it through **More Rules...** and points here.

**Exam route**

1. Select the range first. The rule is stored against the range that was selected when it was made, and fixing that afterwards means editing **Applies to** by hand.
2. Go to the **Home** tab, **Styles** group, click **Conditional Formatting**, then click **New Rule...**.
3. The **New Formatting Rule** dialog opens. Pick one entry from the **Select a Rule Type** list at the top:
   - **Format all cells based on their values**
   - **Format only cells that contain**
   - **Format only top or bottom ranked values**
   - **Format only values that are above or below average**
   - **Format only unique or duplicate values**
   - **Use a formula to determine which cells to format**
4. The **Edit the Rule Description** panel below changes to match. Fill it in.
5. For **Format all cells based on their values**, open **Format Style** and pick **2-Color Scale**, **3-Color Scale**, **Data Bar** or **Icon Set**. Then set each stop: the **Type** list on every stop holds **Lowest Value**, **Number**, **Percent**, **Formula**, **Percentile**, **Highest Value**, and the **Value** box beside it takes the threshold.
6. For a **Data Bar**, select **Show Bar Only** to hide the number. Under **Bar Appearance** set **Fill** to **Gradient Fill** or **Solid Fill**, and **Border** to **Solid Border** or **No Border**. Click **Negative Value and Axis...** to say where zero sits and what colour a negative bar is.
7. For an **Icon Set**, open the **Icon Style** list, then select **Reverse Icon Order** or **Show Icon Only** if asked. Set each band's **Value** and **Type**. Set any single icon to **No Cell Icon** to leave that band unmarked.
8. For the rule types that colour cells rather than draw in them, click the **Format...** button. A cut-down Format Cells opens with four tabs only: **Number**, **Font**, **Border**, **Fill**. There is no Alignment tab and no Protection tab, because a rule cannot change either.
9. Set the font colour on the **Font** tab and then, WITHOUT closing the dialog, go to the **Fill** tab and set the background. Click **OK**. Both were applied in one operation, the same principle as Associate 2.2.6.
10. Click **OK** to close **New Formatting Rule**.

Verified on the professor's build: the top-and-bottom rule type stores a rank and a percent flag, and the above-average type stores an above-or-below flag, each as its own rule with its own priority, which is what the dialog is writing when you fill those panels in.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.3.1 -->

Aquí es donde queda escrito completo el cuadro de diálogo **Nueva regla de formato**; el 2.4.2 del Associate llega a él por **[More Rules...]** y remite aquí.

**Ruta de examen**

1. Selecciona el rango primero. La regla se guarda junto con el rango que estaba seleccionado al crearla, y corregirlo después obliga a editar **[Applies to]** a mano.
2. Ve a la pestaña **Inicio**, grupo **Estilos**, haz clic en **Formato condicional** y luego en **Nueva regla...**.
3. Se abre el cuadro de diálogo **Nueva regla de formato**. Elige una entrada de la lista **Seleccionar un tipo de regla**, arriba:
   - **Aplicar formato a todas las celdas según sus valores**
   - **Aplicar formato únicamente a las celdas que contengan**
   - **Aplicar formato únicamente a los valores con rango inferior o superior**
   - **[Format only values that are above or below average]**
   - **Aplicar formato únicamente a los valores únicos o duplicados**
   - **[Use a formula to determine which cells to format]**
4. El panel **Editar una descripción de regla** de abajo cambia según el tipo que elegiste. Llénalo.
5. Para **Aplicar formato a todas las celdas según sus valores**, abre **[Format Style]** y elige **[2-Color Scale]**, **[3-Color Scale]**, **Barra de datos** o **Conjunto de iconos**. Después ajusta cada punto de corte: la lista **Tipo** de cada punto tiene **[Lowest Value]**, **Número**, **Porcentaje**, **Fórmula**, **[Percentile]**, **[Highest Value]**, y el cuadro **Valor** de al lado recibe el umbral.
6. Para una **Barra de datos**, selecciona **[Show Bar Only]** para ocultar el número. En **[Bar Appearance]** ajusta **Relleno** a **Relleno degradado** o **[Solid Fill]**, y **Borde** a **[Solid Border]** o **Sin borde**. Haz clic en **[Negative Value and Axis...]** para decir dónde queda el cero y de qué color va una barra negativa.
7. Para un **Conjunto de iconos**, abre la lista **[Icon Style]** y luego selecciona **[Reverse Icon Order]** o **[Show Icon Only]** si te lo piden. Ajusta el **Valor** y el **Tipo** de cada banda. Pon cualquier icono suelto en **[No Cell Icon]** para dejar esa banda sin marcar.
8. Para los tipos de regla que colorean celdas en lugar de dibujar dentro de ellas, haz clic en el botón **Formato...**. Se abre un Formato de celdas recortado, con cuatro pestañas nada más: **Número**, **Fuente**, **Borde** y **Relleno**. No hay pestaña Alineación ni pestaña Protección, porque una regla no puede cambiar ninguna de las dos.
9. Pon el color de la letra en la pestaña **Fuente** y luego, SIN cerrar el cuadro de diálogo, ve a la pestaña **Relleno** y pon el fondo. Haz clic en **Aceptar**. Los dos se aplicaron en una sola operación, el mismo principio que en el 2.2.6 del Associate.
10. Haz clic en **Aceptar** para cerrar **Nueva regla de formato**.

Verificado en la instalación del profesor: el tipo de regla de superiores e inferiores guarda un número de posición y una marca de porcentaje, y el tipo por encima del promedio guarda una marca de arriba o abajo, cada uno como su propia regla con su propia prioridad, que es justo lo que el cuadro de diálogo escribe cuando llenas esos paneles.

<!-- ES-FIN MO201-2.3.1 -->

---

### 2.3.2 Create conditional formatting rules that use formulas

**EN · texto fuente, no editar**

**Exam route**

1. Select the range, starting from its top left cell. This matters more here than anywhere else: the formula is written once, for the active cell of the selection, and Excel shifts it across the rest by the same rules that shift a copied formula.
2. Go to the **Home** tab, **Styles** group, click **Conditional Formatting**, then **New Rule...**.
3. In **Select a Rule Type** click **Use a formula to determine which cells to format**.
4. Click in the **Format values where this formula is true** box.
5. Press F2 before using the arrow keys. That box starts in point mode, where an arrow key inserts a cell reference instead of moving the cursor; F2 switches it to edit mode.
6. Type a formula that returns TRUE or FALSE for the top left cell. Lock the column with a dollar sign when one column decides the whole row: `=$E2="Overdue"` over `A2:H200` colours the entire row.
7. Click **Format...**. Set the colour on the **Font** tab and then, WITHOUT closing, the background on the **Fill** tab. Click **OK**.
8. Click **OK** to close the rule dialog.

Patterns worth having ready, all written for a range whose top left cell is row 2:

- whole row driven by one column: `=$E2="Overdue"`
- banded rows: `=MOD(ROW(),2)=0`
- weekend columns in a calendar header: `=WEEKDAY(B$1,2)>5`
- over this row's own target: `=AND($C2>$B2,$B2<>"")`
- blank where a value was required: `=AND($A2<>"",$D2="")`
- repeated key: `=COUNTIF($A:$A,$A2)>1`
- due within thirty days: `=AND($F2>=TODAY(),$F2<=TODAY()+30)`

Verified on the professor's build: a rule of this type accepted `=AND($E1>3,MOD(ROW(),2)=0)` and read the formula back verbatim, with a priority of its own and Stop If True available.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.3.2 -->

**Ruta de examen**

1. Selecciona el rango empezando por su celda superior izquierda. Esto importa aquí más que en ningún otro lado: la fórmula se escribe una sola vez, para la celda activa de la selección, y Excel la desplaza al resto con las mismas reglas con que se desplaza una fórmula copiada.
2. Ve a la pestaña **Inicio**, grupo **Estilos**, haz clic en **Formato condicional** y luego en **Nueva regla...**.
3. En **Seleccionar un tipo de regla** haz clic en **[Use a formula to determine which cells to format]**.
4. Haz clic dentro del cuadro **[Format values where this formula is true]**.
5. Presiona F2 antes de usar las teclas de flecha. Ese cuadro arranca en modo de señalamiento, donde una flecha inserta una referencia de celda en lugar de mover el cursor; F2 lo pasa a modo de edición.
6. Escribe una fórmula que devuelva VERDADERO o FALSO para la celda superior izquierda. Fija la columna con un signo de pesos cuando una sola columna decide toda la fila: `=$E2="Overdue"` sobre `A2:H200` colorea la fila entera.
7. Haz clic en **Formato...**. Pon el color en la pestaña **Fuente** y luego, SIN cerrar, el fondo en la pestaña **Relleno**. Haz clic en **Aceptar**.
8. Haz clic en **Aceptar** para cerrar el cuadro de diálogo de la regla.

Patrones que conviene tener a la mano, todos escritos para un rango cuya celda superior izquierda está en la fila 2:

- fila entera gobernada por una sola columna: `=$E2="Overdue"`
- filas con bandas: `=MOD(ROW(),2)=0`
- columnas de fin de semana en el encabezado de un calendario: `=DIASEM(B$1,2)>5`
- por encima del objetivo de la propia fila: `=Y($C2>$B2,$B2<>"")`
- vacío donde se pedía un valor: `=Y($A2<>"",$D2="")`
- clave repetida: `=CONTAR.SI($A:$A,$A2)>1`
- vence dentro de treinta días: `=Y($F2>=HOY(),$F2<=HOY()+30)`

Verificado en la instalación del profesor: una regla de este tipo aceptó `=AND($E1>3,MOD(ROW(),2)=0)` y devolvió la fórmula tal cual, con una prioridad propia y con Detener si es verdad disponible.

<!-- ES-FIN MO201-2.3.2 -->

---

### 2.3.4 Manage conditional formatting rules

**EN · texto fuente, no editar**

Certiport numbers this domain 2.3.1, 2.3.2 and 2.3.4, with no 2.3.3. Nothing is missing from the list.

**Exam route**

1. Go to the **Home** tab, **Styles** group, click **Conditional Formatting**, then **Manage Rules...**.
2. The **Conditional Formatting Rules Manager** opens. Open the **Show formatting rules for** list at the top and choose **Current Selection**, **This Worksheet**, or a named sheet. Current Selection is the default, and it is why rules seem to disappear: it hides every rule whose range you are not standing in.
3. Select a rule and click **Edit Rule...**. The **Edit Formatting Rule** dialog opens, identical to **New Formatting Rule** (2.3.1). Change the rule type, the description or the **Format**. Click **OK**.
4. Reorder with the **Move Up** and **Move Down** arrow buttons. When two rules touch the same cell and set the same property, the one higher in the list wins; rules that set different properties both apply.
5. Select the **Stop If True** check box on a rule to prevent every rule below it from being evaluated for the cells that rule matched. Use it to protect a top-priority exception from a broad rule underneath.
6. Change a rule's range without recreating it: click in the **Applies to** box, then either type the range or drag over it on the sheet behind the dialog.
7. Click **Delete Rule** to remove the selected one.
8. Click **Apply** to commit without closing, so you can see the effect and keep editing. Click **OK** to commit and close.
9. To clear rules without opening the manager, use **Conditional Formatting**, **Clear Rules** (Associate 2.4.3).
10. To find where the rules are, go to **Home** tab, **Editing** group, **Find & Select**, **Conditional Formatting**, which selects every cell carrying any rule. For only the cells sharing the active cell's rule, use **Find & Select**, **Go To Special...**, **Conditional formats**, then **Same**.

Verified on the professor's build: three rules added to one range took priorities 1, 2 and 3 in the order they were created, moving the third to the front renumbered the other two, and Stop If True was set and read back. That is precisely what Move Up and the check box do from the dialog.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.3.4 -->

Certiport numera este dominio 2.3.1, 2.3.2 y 2.3.4, sin 2.3.3. No falta nada en la lista.

**Ruta de examen**

1. Ve a la pestaña **Inicio**, grupo **Estilos**, haz clic en **Formato condicional** y luego en **Administrar reglas...**.
2. Se abre el **Administrador de reglas de formato condicionales**. Abre la lista **[Show formatting rules for]** de arriba y elige **[Current Selection]**, **[This Worksheet]** o una hoja por su nombre. [Current Selection] es la opción predeterminada, y es la razón por la que las reglas parecen desaparecer: oculta toda regla cuyo rango no sea donde estás parado.
3. Selecciona una regla y haz clic en **[Edit Rule...]**. Se abre el cuadro de diálogo **Editar regla de formato**, idéntico a **Nueva regla de formato** (2.3.1). Cambia el tipo de regla, la descripción o el **Formato**. Haz clic en **Aceptar**.
4. Reordena con los botones de flecha **[Move Up]** y **[Move Down]**. Cuando dos reglas tocan la misma celda y ajustan la misma propiedad, gana la que está más arriba en la lista; las reglas que ajustan propiedades distintas se aplican las dos.
5. Marca la casilla **Detener si es verdad** en una regla para impedir que se evalúe cualquier regla debajo de ella en las celdas que esa regla marcó. Úsala para proteger una excepción de máxima prioridad de una regla amplia que esté abajo.
6. Cambia el rango de una regla sin volver a crearla: haz clic en el cuadro **[Applies to]** y después escribe el rango o arrástralo sobre la hoja que está detrás del cuadro de diálogo.
7. Haz clic en **[Delete Rule]** para quitar la que está seleccionada.
8. Haz clic en **[Apply]** para confirmar sin cerrar, y así ver el efecto y seguir editando. Haz clic en **Aceptar** para confirmar y cerrar.
9. Para borrar reglas sin abrir el administrador, usa **Formato condicional**, **Borrar reglas** (2.4.3 del Associate).
10. Para encontrar dónde están las reglas, ve a la pestaña **Inicio**, grupo **Edición**, **Buscar y seleccionar**, **Formato condicional**, que selecciona todas las celdas que llevan alguna regla. Para quedarte solo con las celdas que comparten la regla de la celda activa, usa **Buscar y seleccionar**, **Ir a Especial...**, **[Conditional formats]** y luego **[Same]**.

Verificado en la instalación del profesor: tres reglas agregadas a un mismo rango tomaron las prioridades 1, 2 y 3 en el orden en que se crearon, mover la tercera al frente renumeró las otras dos, y Detener si es verdad se activó y se volvió a leer. Eso es exactamente lo que hacen [Move Up] y la casilla desde el cuadro de diálogo.

<!-- ES-FIN MO201-2.3.4 -->

---

## MO-201 Expert · Domain 3, Create advanced formulas and macros

Every function objective in this domain goes through **Insert Function** and **Function Arguments**, which are written out at Associate 4.2.1. What is new here is nesting one function inside another from inside the dialog, and that technique is written out once, at 3.1.1, and referred to afterwards.

### 3.1.1 Perform logical operations by using nested functions including the IF(), IFS(), SWITCH(), SUMIF(), AVERAGEIF(), COUNTIF(), SUMIFS(), AVERAGEIFS(), COUNTIFS(), MAXIFS(), MINIFS(), AND(), OR(), and NOT() functions

**EN · texto fuente, no editar**

The graded route never types the function blind. It goes through the Function Library and fills the argument boxes one at a time, because that is the only route that also proves the candidate knows which argument is which.

**Exam route, part A, one function, no nesting**

1. Select the cell that will hold the formula.
2. Go to the **Formulas** tab, **Function Library** group.
3. Click the category gallery that owns the function. IF, IFS, SWITCH, AND, OR and NOT are under **Logical**. The conditional-aggregation family is not in a top-level gallery: click **More Functions**, then **Statistical** for COUNTIF, COUNTIFS, AVERAGEIF, AVERAGEIFS, MAXIFS and MINIFS, and use **Math & Trig** for SUMIF and SUMIFS.
4. Click the function name. The **Function Arguments** dialog opens, titled with the function name.
5. Click into the first argument box. Its label is the argument name, and the dialog shows the argument's description under the boxes as you move between them.
6. Type the reference, or click the collapse button at the right of the box and drag the range on the sheet, then click the button again to expand the dialog.
7. Press Tab to move to the next box. Excel evaluates each argument live and shows the value to the right of the box. Watch the **Formula result =** line at the bottom.
8. Click **OK**. The dialog writes the finished formula into the cell.

**Exam route, part B, nesting one function inside another.** This is the part the exam is actually testing, and every later objective that nests refers back to these six steps.

1. Build the outer function with part A, up to step 5.
2. Click into the argument box that has to receive the nested function. Leave it empty.
3. Look at the **Name Box**, at the left end of the formula bar. While a Function Arguments dialog is open it stops showing the cell reference and becomes a function drop-down.
4. Open it and pick the inner function from the list of recently used functions, or pick **More Functions...** to open **Insert Function** and choose from **Or select a category:** and **Select a function:**.
5. The Function Arguments dialog is replaced by the inner function's own dialog. Fill its boxes and do not click OK yet. To go back out, click the outer function's name inside the formula bar; the outer dialog returns with the nested call already in place.
6. Click **OK** once, at the outer level. One OK commits the whole nest.

**Exam route, part C, the argument boxes,** read off the live Function Arguments dialog on build 16.0.20228 so they can be quoted in class.

| Function | Boxes, in order |
|---|---|
| IF | Logical_test, Value_if_true, Value_if_false |
| IFS | Logical_test1, Value_if_true1, Logical_test2, Value_if_true2, … |
| SWITCH | Expression, Value1, Result1, Default_or_value2, Result2, … |
| AND | Logical1, Logical2, … |
| OR | Logical1, Logical2, … |
| NOT | Logical |
| SUMIF | Range, Criteria, Sum_range |
| COUNTIF | Range, Criteria |
| AVERAGEIF | Range, Criteria, Average_range |
| SUMIFS | Sum_range, Criteria_range1, Criteria1 |
| COUNTIFS | Criteria_range1, Criteria1 |
| AVERAGEIFS | Average_range, Criteria_range1, Criteria1 |
| MAXIFS | Max_range, Criteria_range1, Criteria1 |
| MINIFS | Min_range, Criteria_range1, Criteria1 |

Note the trap the singular and plural families set. SUMIF puts the range to add **last**; SUMIFS puts it **first**. Same for AVERAGEIF against AVERAGEIFS. The dialog is what makes that visible; typing hides it.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.1.1 -->

La ruta que se califica nunca teclea la función a ciegas. Pasa por el grupo [Function Library] y llena los cuadros de argumento uno por uno, porque esa es la única ruta que además demuestra que el candidato sabe cuál argumento es cuál.

**Ruta de examen, parte A, una función, sin anidar**

1. Selecciona la celda que va a contener la fórmula.
2. Ve a la pestaña **Fórmulas**, grupo **[Function Library]**.
3. Haz clic en la galería de categoría a la que pertenece la función. SI, SI.CONJUNTO, CAMBIAR, Y, O y NO están bajo **Lógicas**. La familia de agregación condicional no está en una galería de primer nivel: haz clic en **Más funciones** y después en **[Statistical]** para CONTAR.SI, CONTAR.SI.CONJUNTO, PROMEDIO.SI, PROMEDIO.SI.CONJUNTO, MAX.SI.CONJUNTO y MIN.SI.CONJUNTO, y usa **[Math & Trig]** para SUMAR.SI y SUMAR.SI.CONJUNTO.
4. Haz clic en el nombre de la función. Se abre el cuadro de diálogo **[Function Arguments]**, titulado con el nombre de la función.
5. Haz clic dentro del primer cuadro de argumento. Su etiqueta es el nombre del argumento, y el cuadro de diálogo muestra la descripción del argumento debajo de los cuadros conforme te mueves entre ellos.
6. Escribe la referencia, o haz clic en el botón de contraer que está a la derecha del cuadro y arrastra el rango sobre la hoja, y después haz clic otra vez en el botón para volver a expandir el cuadro de diálogo.
7. Presiona Tab para pasar al siguiente cuadro. Excel evalúa cada argumento en vivo y muestra el valor a la derecha del cuadro. Observa la línea **[Formula result =]** al final.
8. Haz clic en **Aceptar**. El cuadro de diálogo escribe la fórmula terminada en la celda.

**Ruta de examen, parte B, anidar una función dentro de otra.** Esta es la parte que el examen está probando de verdad, y cada objetivo posterior que anida remite a estos seis pasos.

1. Arma la función exterior con la parte A, hasta el paso 5.
2. Haz clic dentro del cuadro de argumento que tiene que recibir la función anidada. Déjalo vacío.
3. Mira el **Cuadro de nombres**, en el extremo izquierdo de la barra de fórmulas. Mientras hay un cuadro de diálogo [Function Arguments] abierto, deja de mostrar la referencia de celda y se convierte en una lista desplegable de funciones.
4. Ábrela y elige la función interior de la lista de funciones usadas recientemente, o elige **[More Functions...]** para abrir **Insertar función** y escoger desde **[Or select a category:]** y **[Select a function:]**.
5. El cuadro de diálogo [Function Arguments] queda reemplazado por el de la función interior. Llena sus cuadros y no hagas clic en Aceptar todavía. Para regresar hacia afuera, haz clic en el nombre de la función exterior dentro de la barra de fórmulas; el cuadro de diálogo exterior vuelve con la llamada anidada ya puesta.
6. Haz clic en **Aceptar** una sola vez, en el nivel exterior. Un solo Aceptar confirma todo el anidamiento.

**Ruta de examen, parte C, los cuadros de argumento,** leídos del cuadro de diálogo [Function Arguments] en vivo en la compilación 16.0.20228 para poder citarlos en clase.

| Función | Cuadros, en orden |
|---|---|
| SI | [Logical_test], [Value_if_true], [Value_if_false] |
| SI.CONJUNTO | [Logical_test1], [Value_if_true1], [Logical_test2], [Value_if_true2], … |
| CAMBIAR | [Expression], [Value1], [Result1], [Default_or_value2], [Result2], … |
| Y | [Logical1], [Logical2], … |
| O | [Logical1], [Logical2], … |
| NO | Lógicas |
| SUMAR.SI | Rango, Criterio, [Sum_range] |
| CONTAR.SI | Rango, Criterio |
| PROMEDIO.SI | Rango, Criterio, [Average_range] |
| SUMAR.SI.CONJUNTO | [Sum_range], [Criteria_range1], [Criteria1] |
| CONTAR.SI.CONJUNTO | [Criteria_range1], [Criteria1] |
| PROMEDIO.SI.CONJUNTO | [Average_range], [Criteria_range1], [Criteria1] |
| MAX.SI.CONJUNTO | [Max_range], [Criteria_range1], [Criteria1] |
| MIN.SI.CONJUNTO | [Min_range], [Criteria_range1], [Criteria1] |

Fíjate en la trampa que tienden las familias en singular y en plural. SUMAR.SI pone **al final** el rango que se suma; SUMAR.SI.CONJUNTO lo pone **al principio**. Lo mismo pasa con PROMEDIO.SI frente a PROMEDIO.SI.CONJUNTO. El cuadro de diálogo es lo que hace visible esa diferencia; teclear la esconde.

<!-- ES-FIN MO201-3.1.1 -->

---

### 3.2.1 Look up data by using the VLOOKUP(), HLOOKUP(), MATCH(), and INDEX() functions

**EN · texto fuente, no editar**

**Exam route, VLOOKUP**

1. Select the cell that will hold the lookup.
2. **Formulas** tab, **Function Library** group, **Lookup & Reference**, then **VLOOKUP**.
3. In **Lookup_value**, put the cell holding the key. Leave it relative if the formula will be filled down.
4. In **Table_array**, select the whole reference table including its first column. Press F4 to lock it to `$A$2:$D$50`. This is the step candidates lose marks on, because a relative table array walks down the sheet when the formula is filled.
5. In **Col_index_num**, type the column number counted from the first column of Table_array, not from column A of the sheet.
6. In **Range_lookup**, type FALSE for an exact match or TRUE for the banded, approximate match. Leaving it empty is not the same as FALSE: empty means TRUE.
7. Click **OK**.

HLOOKUP is the same dialog with **Row_index_num** in place of Col_index_num, and the key is searched across the top row of Table_array instead of down its first column.

**Exam route, MATCH**

1. **Formulas** tab, **Function Library** group, **Lookup & Reference**, then **MATCH**.
2. **Lookup_value**, the key.
3. **Lookup_array**, one single row or one single column. MATCH refuses a two-dimensional range.
4. **Match_type**, 0 for exact. 1 needs the array sorted ascending, -1 needs it sorted descending.
5. Click **OK**. MATCH returns a position number, not a value.

**Exam route, INDEX.** This is the one function in the objective that shows an extra dialog first.

1. **Formulas** tab, **Function Library** group, **Lookup & Reference**, then **INDEX**.
2. The **Select Arguments** dialog opens, headed INDEX, with the line "This function has multiple argument lists. Please select one of them." and an **Arguments:** list holding two entries, `array,row_num,column_num` and `reference,row_num,column_num,area_num`.
3. Pick `array,row_num,column_num` for the ordinary case. Click **OK**.
4. The Function Arguments dialog opens with **Array**, **Row_num**, **Column_num**.
5. In **Array**, select the block of values to be returned from, not the whole table with its headers.
6. Fill Row_num and Column_num. Either may be left empty when the array is a single row or a single column.
7. Click **OK**.

**Exam route, INDEX with MATCH nested**: the pairing the exam actually wants, and the one Exercise 21 forces without ever naming it.

1. Build INDEX as above and stop at step 4, with the cursor in **Row_num**.
2. Nest MATCH using the Name Box technique of 3.1.1 part B.
3. Fill MATCH's three boxes, then click the word INDEX in the formula bar to come back out.
4. If Column_num also needs a MATCH, click into it and repeat.
5. Click **OK** once, at the INDEX level.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.2.1 -->

**Ruta de examen, BUSCARV**

1. Selecciona la celda que va a contener la búsqueda.
2. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Lookup & Reference]**, y después **BUSCARV**.
3. En **[Lookup_value]**, pon la celda que tiene la clave. Déjala relativa si la fórmula se va a rellenar hacia abajo.
4. En **[Table_array]**, selecciona toda la tabla de referencia incluida su primera columna. Presiona F4 para fijarla como `$A$2:$D$50`. Este es el paso en el que los candidatos pierden puntos, porque una matriz de tabla relativa se recorre hacia abajo por la hoja cuando se rellena la fórmula.
5. En **[Col_index_num]**, escribe el número de columna contado desde la primera columna de [Table_array], no desde la columna A de la hoja.
6. En **[Range_lookup]**, escribe FALSO para una coincidencia exacta o VERDADERO para la coincidencia aproximada por rangos. Dejarlo vacío no es lo mismo que FALSO: vacío significa VERDADERO.
7. Haz clic en **Aceptar**.

BUSCARH es el mismo cuadro de diálogo con **[Row_index_num]** en lugar de [Col_index_num], y la clave se busca a lo largo de la fila superior de [Table_array] en vez de hacia abajo por su primera columna.

**Ruta de examen, COINCIDIR**

1. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Lookup & Reference]**, y después **COINCIDIR**.
2. **[Lookup_value]**, la clave.
3. **[Lookup_array]**, una sola fila o una sola columna. COINCIDIR rechaza un rango de dos dimensiones.
4. **[Match_type]**, 0 para exacta. 1 necesita la matriz ordenada de forma ascendente, -1 la necesita ordenada de forma descendente.
5. Haz clic en **Aceptar**. COINCIDIR devuelve un número de posición, no un valor.

**Ruta de examen, ÍNDICE.** Esta es la única función del objetivo que muestra un cuadro de diálogo extra antes.

1. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Lookup & Reference]**, y después **INDICE**.
2. Se abre el cuadro de diálogo **[Select Arguments]**, encabezado INDICE, con la línea ["This function has multiple argument lists. Please select one of them."] y una lista **[Arguments:]** con dos entradas, `array,row_num,column_num` y `reference,row_num,column_num,area_num`.
3. Elige `array,row_num,column_num` para el caso ordinario. Haz clic en **Aceptar**.
4. Se abre el cuadro de diálogo [Function Arguments] con **[Array]**, **[Row_num]**, **[Column_num]**.
5. En [Array], selecciona el bloque de valores del que se va a devolver el resultado, no toda la tabla con sus encabezados.
6. Llena [Row_num] y [Column_num]. Cualquiera de los dos puede quedar vacío cuando la matriz es una sola fila o una sola columna.
7. Haz clic en **Aceptar**.

**Ruta de examen, ÍNDICE con COINCIDIR anidada**: la pareja que el examen realmente quiere, y la que el Ejercicio 21 obliga a usar sin nombrarla nunca.

1. Arma ÍNDICE como arriba y detente en el paso 4, con el cursor en **[Row_num]**.
2. Anida COINCIDIR con la técnica del **Cuadro de nombres** de la parte B de 3.1.1.
3. Llena los tres cuadros de COINCIDIR y después haz clic en la palabra INDICE dentro de la barra de fórmulas para regresar hacia afuera.
4. Si [Column_num] también necesita una COINCIDIR, haz clic dentro y repite.
5. Haz clic en **Aceptar** una sola vez, en el nivel de ÍNDICE.

<!-- ES-FIN MO201-3.2.1 -->

---

### 3.3.1 Reference date and time by using the NOW() and TODAY() functions

**EN · texto fuente, no editar**

**Exam route**

1. Select the cell.
2. **Formulas** tab, **Function Library** group, **Date & Time**.
3. Click **TODAY** or **NOW**.
4. The **Function Arguments** dialog opens with no argument boxes at all, only the description and the **Formula result =** line. Neither function takes arguments.
5. Click **OK**. The cell receives `=TODAY()` or `=NOW()`.
6. Format the result, because the raw return is a serial number. Select the cell, press Ctrl+1, **Number** tab, pick **Date** or **Time** from the **Category** list, choose the type, click **OK**.
7. For an age or elapsed-days calculation, subtract in a second cell, for example `=TODAY()-B2`, then set that cell to the **General** or **Number** category, not Date, or Excel shows the difference as a date in 1900.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.3.1 -->

**Ruta de examen**

1. Selecciona la celda.
2. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Date & Time]**.
3. Haz clic en **HOY** o en **AHORA**.
4. Se abre el cuadro de diálogo **[Function Arguments]** sin ningún cuadro de argumento, solo con la descripción y la línea **[Formula result =]**. Ninguna de las dos funciones toma argumentos.
5. Haz clic en **Aceptar**. La celda recibe `=HOY()` o `=AHORA()`.
6. Da formato al resultado, porque lo que devuelve en crudo es un número de serie. Selecciona la celda, presiona Ctrl+1, pestaña **Número**, elige **Fecha** o **[Time]** en la lista **Categoría**, escoge el tipo y haz clic en **Aceptar**.
7. Para calcular una edad o los días transcurridos, resta en una segunda celda, por ejemplo `=HOY()-B2`, y después pon esa celda en la categoría **General** o **Número**, no en Fecha, o Excel muestra la diferencia como una fecha de 1900.

<!-- ES-FIN MO201-3.3.1 -->

---

### 3.3.2 Calculate dates by using the WEEKDAY() and WORKDAY() functions

**EN · texto fuente, no editar**

**Exam route, WEEKDAY**

1. Select the cell.
2. **Formulas** tab, **Function Library** group, **Date & Time**, then **WEEKDAY**.
3. In **Serial_number**, point at the cell holding the date. Do not type a date as text.
4. In **Return_type**, type the numbering scheme. The dialog's own description spells them out: 1 for Sunday=1 through Saturday=7, 2 for Monday=1 through Sunday=7, 3 for Monday=0 through Sunday=6. Leaving the box empty gives 1.
5. Click **OK**.
6. To turn the number into a day name, wrap it or format it. The graded formatting route is Ctrl+1, **Number** tab, **Custom** category, and `dddd` in the **Type** box applied to the original date cell.

**Exam route, WORKDAY**

1. **Formulas** tab, **Function Library** group, **Date & Time**, then **WORKDAY**.
2. In **Start_date**, point at the starting date cell.
3. In **Days**, type the count of working days to move forward. A negative number moves backward.
4. In **Holidays**, select the range holding the non-working dates. Press F4 to lock it, because this formula is almost always filled down. This box is optional and it is the one the exam checks, since without it Saturday and Sunday are skipped but a public holiday is not.
5. Click **OK**.
6. Format the result as a date: Ctrl+1, **Number** tab, **Date** category.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.3.2 -->

**Ruta de examen, DIASEM**

1. Selecciona la celda.
2. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Date & Time]**, y después **DIASEM**.
3. En **[Serial_number]**, apunta a la celda que tiene la fecha. No escribas una fecha como texto.
4. En **[Return_type]**, escribe el esquema de numeración. La propia descripción del cuadro de diálogo los detalla: 1 para domingo=1 hasta sábado=7, 2 para lunes=1 hasta domingo=7, 3 para lunes=0 hasta domingo=6. Dejar el cuadro vacío da 1.
5. Haz clic en **Aceptar**.
6. Para convertir el número en un nombre de día, anídalo en otra función o dale formato. La ruta de formato que se califica es Ctrl+1, pestaña **Número**, categoría **Personalizada**, y `dddd` en el cuadro **Tipo** aplicado a la celda de la fecha original.

**Ruta de examen, DIA.LAB**

1. Pestaña **Fórmulas**, grupo **[Function Library]**, **[Date & Time]**, y después **DIA.LAB**.
2. En **[Start_date]**, apunta a la celda de la fecha inicial.
3. En **[Days]**, escribe la cantidad de días laborables que hay que avanzar. Un número negativo retrocede.
4. En **[Holidays]**, selecciona el rango que tiene las fechas no laborables. Presiona F4 para fijarlo, porque esta fórmula casi siempre se rellena hacia abajo. Este cuadro es opcional y es el que revisa el examen, porque sin él se saltan el sábado y el domingo pero no un día festivo.
5. Haz clic en **Aceptar**.
6. Da formato de fecha al resultado: Ctrl+1, pestaña **Número**, categoría **Fecha**.

<!-- ES-FIN MO201-3.3.2 -->

---

### 3.4.1 Summarize data from multiple ranges by using the Consolidate feature

**EN · texto fuente, no editar**

**Exam route**

1. Click the single top-left cell of the empty area where the summary is to appear. Do not select a block: Consolidate writes as far right and as far down as it needs.
2. Go to the **Data** tab, **Data Tools** group, and click **Consolidate**. The **Consolidate** dialog opens.
3. Open the **Function:** list and pick the summary operation. The list holds exactly eleven entries: Sum, Count, Average, Max, Min, Product, Count Numbers, StdDev, StdDevp, Var, Varp.
4. Click into the **Reference:** box.
5. Go to the first source sheet and drag the first source range, headers included if you plan to use labels. Use **Browse...** instead if the source is a closed workbook.
6. Click **Add**. The range appears in the **All references:** list.
7. Repeat steps 4 to 6 for every source range. Each one must be added separately; a wrong range is taken out by selecting it in All references: and clicking **Delete**.
8. Under **Use labels in**, tick **Top row** and **Left column** if the sources carry headers and the rows are not in the same order in every sheet. This is what makes Consolidate match by name rather than by position, and it is the difference between the graded answer and a wrong one.
9. Tick **Create links to source data** if the summary has to update when the sources change. This inserts an outline with one hidden detail row per source. Leave it clear for a flat, static summary.
10. Click **OK**. Note that this dialog has **OK** and **Close**, not OK and Cancel: Close leaves without consolidating.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.4.1 -->

**Ruta de examen**

1. Haz clic en una sola celda, la superior izquierda del área vacía donde va a aparecer el resumen. No selecciones un bloque: Consolidar escribe tan a la derecha y tan abajo como lo necesite.
2. Ve a la pestaña **Datos**, grupo **Herramientas de datos**, y haz clic en **Consolidar**. Se abre el cuadro de diálogo **Consolidar**.
3. Abre la lista **Función:** y elige la operación de resumen. La lista tiene exactamente once entradas: Suma, Recuento, Promedio, Máx, Mín, [Product], Contar números, Desvest, [StdDevp], Var, [Varp].
4. Haz clic dentro del cuadro **[Reference:]**.
5. Ve a la primera hoja de origen y arrastra el primer rango de origen, con encabezados incluidos si piensas usar los rótulos. Usa **[Browse...]** en su lugar si el origen es un libro cerrado.
6. Haz clic en **[Add]**. El rango aparece en la lista **[All references:]**.
7. Repite los pasos 4 a 6 con cada rango de origen. Cada uno se tiene que agregar por separado; un rango equivocado se saca seleccionándolo en [All references:] y haciendo clic en **Eliminar**.
8. En **[Use labels in]**, marca **[Top row]** y **[Left column]** si los orígenes traen encabezados y las filas no están en el mismo orden en todas las hojas. Esto es lo que hace que Consolidar empareje por nombre y no por posición, y es la diferencia entre la respuesta que se califica y una equivocada.
9. Marca **[Create links to source data]** si el resumen tiene que actualizarse cuando cambien los orígenes. Esto inserta un esquema con una fila de detalle oculta por cada origen. Déjalo sin marcar para un resumen plano y estático.
10. Haz clic en **Aceptar**. Ten en cuenta que este cuadro de diálogo tiene **Aceptar** y **Cerrar**, no Aceptar y Cancelar: Cerrar sale sin consolidar.

<!-- ES-FIN MO201-3.4.1 -->

---

### 3.4.2 Perform what-if analysis by using Goal Seek and Scenario Manager

**EN · texto fuente, no editar**

**Exam route, Goal Seek**

1. Make sure the target cell holds a formula and that the cell you intend to change holds a value, not a formula. Goal Seek refuses to change a formula cell.
2. Select the formula cell.
3. Go to the **Data** tab, **Forecast** group, click **What-If Analysis**, then **Goal Seek...**. The dialog opens with three boxes.
4. **Set cell:** is already filled with the cell you selected. Confirm it, it must be a single cell containing a formula.
5. Click into **To value:** and type the result you want as a plain number. No equals sign, no cell reference; this box will not accept a reference.
6. Click into **By changing cell:** and click the input cell on the sheet. One cell only.
7. Click **OK**.
8. The **Goal Seek Status** dialog reports the outcome and shows **Target value:** and **Current value:** so you can see how close it landed. Click **OK** to keep the new input value on the sheet, or **Cancel** to put the sheet back as it was. The dialog also carries **Step** and **Pause**, which walk the iteration one pass at a time.

**Exam route, Scenario Manager**

1. **Data** tab, **Forecast** group, **What-If Analysis**, then **Scenario Manager...**. On a clean sheet it reads "No Scenarios defined. Choose Add to add scenarios."
2. Click **Add...**. The **Add Scenario** dialog opens.
3. In **Scenario name:**, type a name. Names are what appear in the summary report, so use words the reader will understand, not Scenario 1.
4. In **Changing cells:**, select the input cells. For cells that are not next to each other, hold Ctrl and click each one, the dialog says so itself, in the line "Ctrl+click cells to select non-adjacent changing cells." The practical ceiling is 32 changing cells.
5. **Comment:** is prefilled with your name and today's date. Overwrite it or leave it.
6. Under **Protection**, **Prevent changes** is ticked by default and **Hide** is clear. Both only bite once the sheet itself is protected. Leave them unless the item asks otherwise.
7. Click **OK**. The **Scenario Values** dialog opens with the line "Enter values for each of the changing cells." and one box per changing cell.
8. Type the value for each box.
9. Click **Add** to go straight into another scenario without leaving, or **OK** to return to Scenario Manager. Use **Add**: it is the fast path and the exam usually asks for two or three scenarios.
10. Back in Scenario Manager, select a scenario and click **Show** to push its values onto the sheet. **Edit...** reopens it, **Delete** removes it, **Merge...** pulls scenarios in from another sheet or workbook.
11. For the report, click **Summary...**. Under **Report type**, choose **Scenario summary** or **Scenario PivotTable report**. In **Result cells:**, select the formula cells whose outcome should be compared, using Ctrl for non-adjacent ones. Click **OK**. Excel inserts a new sheet named Scenario Summary.
12. Click **Close** to leave Scenario Manager.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.4.2 -->

**Ruta de examen, Buscar objetivo**

1. Asegúrate de que la celda objetivo contiene una fórmula y de que la celda que piensas cambiar contiene un valor, no una fórmula. Buscar objetivo se niega a cambiar una celda con fórmula.
2. Selecciona la celda que tiene la fórmula.
3. Ve a la pestaña **Datos**, grupo **Previsión**, haz clic en **Análisis de hipótesis** y después en **Buscar objetivo...**. El cuadro de diálogo se abre con tres cuadros.
4. **[Set cell:]** ya viene lleno con la celda que seleccionaste. Confírmala, tiene que ser una sola celda que contenga una fórmula.
5. Haz clic dentro de **[To value:]** y escribe el resultado que quieres como número simple. Sin signo de igual, sin referencia de celda; este cuadro no acepta una referencia.
6. Haz clic dentro de **[By changing cell:]** y haz clic en la celda de entrada sobre la hoja. Una sola celda.
7. Haz clic en **Aceptar**.
8. El cuadro de diálogo **Estado de la búsqueda de objetivo** informa el resultado y muestra **[Target value:]** y **[Current value:]** para que veas qué tan cerca quedó. Haz clic en **Aceptar** para conservar el nuevo valor de entrada en la hoja, o en **Cancelar** para dejar la hoja como estaba. El cuadro de diálogo también trae **Paso a paso** y **Pausa**, que recorren la iteración un paso a la vez.

**Ruta de examen, Administrador de escenarios**

1. Pestaña **Datos**, grupo **Previsión**, **Análisis de hipótesis**, y después **Administrador de escenarios...**. En una hoja limpia dice ["No Scenarios defined. Choose Add to add scenarios."].
2. Haz clic en **[Add...]**. Se abre el cuadro de diálogo **[Add Scenario]**.
3. En **[Scenario name:]**, escribe un nombre. Los nombres son lo que aparece en el informe de resumen, así que usa palabras que el lector entienda, no Escenario 1.
4. En **[Changing cells:]**, selecciona las celdas de entrada. Para celdas que no están una junto a otra, mantén presionada Ctrl y haz clic en cada una; el propio cuadro de diálogo lo dice, en la línea ["Ctrl+click cells to select non-adjacent changing cells."]. El techo práctico es de 32 celdas cambiantes.
5. **[Comment:]** viene lleno de antemano con tu nombre y la fecha de hoy. Sobrescríbelo o déjalo.
6. En **Proteger**, **[Prevent changes]** viene marcado de forma predeterminada y **Ocultar** viene sin marcar. Los dos solo surten efecto una vez que la hoja está protegida. Déjalos así salvo que el reactivo pida otra cosa.
7. Haz clic en **Aceptar**. Se abre el cuadro de diálogo **[Scenario Values]** con la línea ["Enter values for each of the changing cells."] y un cuadro por cada celda cambiante.
8. Escribe el valor de cada cuadro.
9. Haz clic en **[Add]** para entrar directo a otro escenario sin salir, o en **Aceptar** para volver al Administrador de escenarios. Usa [Add]: es el camino rápido y el examen casi siempre pide dos o tres escenarios.
10. De vuelta en el Administrador de escenarios, selecciona un escenario y haz clic en **Mostrar** para poner sus valores sobre la hoja. **[Edit...]** lo vuelve a abrir, **Eliminar** lo quita, **[Merge...]** trae escenarios desde otra hoja o desde otro libro.
11. Para el informe, haz clic en **[Summary...]**. En **[Report type]**, elige **[Scenario summary]** o **[Scenario PivotTable report]**. En **[Result cells:]**, selecciona las celdas con fórmula cuyo resultado se debe comparar, usando Ctrl para las que no están una junto a otra. Haz clic en **Aceptar**. Excel inserta una hoja nueva llamada [Scenario Summary].
12. Haz clic en **Cerrar** para salir del Administrador de escenarios.

<!-- ES-FIN MO201-3.4.2 -->

---

### 3.4.3 Forecast data by using the AND(), IF(), and NPER() functions

**EN · texto fuente, no editar**

The objective bundles a financial function with two logical ones, because the exam item is always the same shape: work out how long something takes, then decide something on the strength of the answer.

**Exam route, part A, NPER**

1. Select the cell.
2. **Formulas** tab, **Function Library** group, **Financial**, then **NPER**.
3. The **Function Arguments** dialog opens with five boxes: **Rate**, **Pmt**, **Pv**, **Fv**, **Type**.
4. **Rate**, the rate per period. Divide the annual rate by the number of periods per year in the box itself, `B2/12`, so the sheet stays readable.
5. **Pmt**, the payment made each period. Enter it negative if it is money leaving, because Excel signs cash flows.
6. **Pv**, the present value, the amount borrowed or the lump sum held today. It carries the opposite sign to Pmt.
7. **Fv**, optional, the balance to be left at the end. Empty means zero.
8. **Type**, optional, 0 or empty for payment at the end of the period, 1 for payment at the beginning.
9. Watch **Formula result =** at the bottom of the dialog. If it shows an error before you have clicked OK, the signs are wrong. This is the diagnostic the dialog gives you and the typed route does not.
10. Click **OK**.

**Exam route, part B, the decision on top of it**

1. Select the decision cell.
2. **Formulas** tab, **Function Library** group, **Logical**, then **IF**.
3. Click into **Logical_test** and nest AND using the Name Box technique of 3.1.1 part B.
4. Fill **Logical1** and **Logical2** with the two conditions, for example the NPER cell against a ceiling and the payment against a budget.
5. Click the word IF in the formula bar to return to the outer dialog.
6. Fill **Value_if_true** and **Value_if_false** with text in quotes or with references.
7. Click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.4.3 -->

El objetivo junta una función financiera con dos lógicas, porque el reactivo del examen siempre tiene la misma forma: calcular cuánto tarda algo y después decidir algo con base en esa respuesta.

**Ruta de examen, parte A, NPER**

1. Selecciona la celda.
2. Pestaña **Fórmulas**, grupo **[Function Library]**, **Financieras**, y después **NPER**.
3. Se abre el cuadro de diálogo **[Function Arguments]** con cinco cuadros: **[Rate]**, **[Pmt]**, **[Pv]**, **[Fv]**, **Tipo**.
4. **[Rate]**, la tasa por periodo. Divide la tasa anual entre el número de periodos por año dentro del mismo cuadro, `B2/12`, para que la hoja se siga leyendo bien.
5. **[Pmt]**, el pago que se hace cada periodo. Ponlo negativo si es dinero que sale, porque Excel les da signo a los flujos de efectivo.
6. **[Pv]**, el valor presente, la cantidad prestada o la suma que se tiene hoy. Lleva el signo contrario al de [Pmt].
7. **[Fv]**, opcional, el saldo que debe quedar al final. Vacío significa cero.
8. **Tipo**, opcional, 0 o vacío para el pago al final del periodo, 1 para el pago al principio.
9. Observa **[Formula result =]** al final del cuadro de diálogo. Si muestra un error antes de que hayas hecho clic en Aceptar, los signos están mal. Este es el diagnóstico que te da el cuadro de diálogo y que la ruta tecleada no da.
10. Haz clic en **Aceptar**.

**Ruta de examen, parte B, la decisión que va encima**

1. Selecciona la celda de la decisión.
2. Pestaña **Fórmulas**, grupo **[Function Library]**, **Lógicas**, y después **SI**.
3. Haz clic dentro de **[Logical_test]** y anida Y con la técnica del **Cuadro de nombres** de la parte B de 3.1.1.
4. Llena **[Logical1]** y **[Logical2]** con las dos condiciones, por ejemplo la celda de NPER contra un tope y el pago contra un presupuesto.
5. Haz clic en la palabra SI dentro de la barra de fórmulas para volver al cuadro de diálogo exterior.
6. Llena **[Value_if_true]** y **[Value_if_false]** con texto entre comillas o con referencias.
7. Haz clic en **Aceptar**.

<!-- ES-FIN MO201-3.4.3 -->

---

### 3.4.4 Calculate financial data by using the PMT() function

**EN · texto fuente, no editar**

**Exam route**

1. Lay the inputs out in labelled cells first: annual rate, term in years, amount borrowed. The exam expects the formula to reference cells, not to carry hard numbers.
2. Select the cell for the payment.
3. **Formulas** tab, **Function Library** group, **Financial**, then **PMT**.
4. The **Function Arguments** dialog opens with five boxes: **Rate**, **Nper**, **Pv**, **Fv**, **Type**.
5. **Rate**, the rate per period. Type `B2/12` for a monthly payment on an annual rate. Putting the annual rate in raw is the single most common wrong answer.
6. **Nper**, the total number of payments. Type `B3*12`, not the number of years.
7. **Pv**, the amount borrowed, as a positive number if you want the payment returned negative, or entered as `-B4` if you want the payment positive. Decide once and be consistent across the sheet.
8. **Fv**, optional, the balloon or residual left at the end. Empty means zero.
9. **Type**, optional, 0 or empty for payment at the end of the period, 1 for the beginning.
10. Read **Formula result =** at the bottom before committing.
11. Click **OK**.
12. Format the result: select it, press Ctrl+1, **Number** tab, **Currency** or **Accounting** in the **Category** list, set **Decimal places**, click **OK**.
13. For an amortisation table, lock the input cells with F4 as you build the first row, so the formula can be filled down without the references drifting.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.4.4 -->

**Ruta de examen**

1. Acomoda primero las entradas en celdas con rótulo: tasa anual, plazo en años, cantidad prestada. El examen espera que la fórmula haga referencia a celdas, no que traiga números fijos.
2. Selecciona la celda del pago.
3. Pestaña **Fórmulas**, grupo **[Function Library]**, **Financieras**, y después **PAGO**.
4. Se abre el cuadro de diálogo **[Function Arguments]** con cinco cuadros: **[Rate]**, **[Nper]**, **[Pv]**, **[Fv]**, **Tipo**.
5. **[Rate]**, la tasa por periodo. Escribe `B2/12` para un pago mensual sobre una tasa anual. Poner la tasa anual en crudo es la respuesta equivocada más común de todas.
6. **[Nper]**, el número total de pagos. Escribe `B3*12`, no el número de años.
7. **[Pv]**, la cantidad prestada, como número positivo si quieres que el pago se devuelva negativo, o escrita como `-B4` si quieres el pago positivo. Decídelo una sola vez y sé consistente en toda la hoja.
8. **[Fv]**, opcional, el saldo o valor residual que queda al final. Vacío significa cero.
9. **Tipo**, opcional, 0 o vacío para el pago al final del periodo, 1 para el principio.
10. Lee **[Formula result =]** al final antes de confirmar.
11. Haz clic en **Aceptar**.
12. Da formato al resultado: selecciónalo, presiona Ctrl+1, pestaña **Número**, **Moneda** o **Contabilidad** en la lista **Categoría**, define **Posiciones decimales** y haz clic en **Aceptar**.
13. Para una tabla de amortización, fija las celdas de entrada con F4 mientras armas la primera fila, para que la fórmula se pueda rellenar hacia abajo sin que las referencias se recorran.

<!-- ES-FIN MO201-3.4.4 -->

---

### 3.5.1 Trace precedence and dependence

**EN · texto fuente, no editar**

**Exam route, precedents, the cells this formula reads**

1. Select the cell holding the formula.
2. Go to the **Formulas** tab, **Formula Auditing** group.
3. Click **Trace Precedents**. Blue arrows appear, running from every cell the formula reads into the selected cell, with a dot at each source end.
4. Click **Trace Precedents** again to go one level further back. Each click adds a level. Keep clicking until no new arrow appears.
5. If a dashed black arrow appears pointing at a small worksheet icon, the precedent is on another sheet or in another workbook. Double-click that dashed arrow to open the **Go To** dialog, which lists the external reference; select it and click **OK** to jump there. The source workbook must be open for this to work.

**Exam route, dependents, the cells that read this cell**

1. Select the cell.
2. **Formulas** tab, **Formula Auditing** group, click **Trace Dependents**.
3. Click again for each further level.

**Exam route, clearing the arrows,** which the exam does check because it wants the sheet left clean.

1. **Formulas** tab, **Formula Auditing** group, click the arrow on the **Remove Arrows** button.
2. The menu holds three entries: **Remove Arrows**, **Remove Precedent Arrows**, **Remove Dependent Arrows**. Choose the one asked for. Clicking the button face rather than its arrow runs Remove Arrows and clears everything.

**Exam route, selecting rather than drawing,** when the item says "select the cells that feed this formula": use **Go To Special** (Associate 1.2.2) and choose **Precedents** or **Dependents**. Two extra options light up underneath, **Direct only** and **All levels**; pick the one the item asks for. Direct only is one level, All levels walks the whole chain. Click **OK** and the cells are selected, with no arrows drawn.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.5.1 -->

**Ruta de examen, precedentes, las celdas que lee esta fórmula**

1. Selecciona la celda que contiene la fórmula.
2. Ve a la pestaña **Fórmulas**, grupo **Auditoría de fórmulas**.
3. Haz clic en **Rastrear precedentes**. Aparecen flechas azules que van desde cada celda que lee la fórmula hasta la celda seleccionada, con un punto en el extremo de cada origen.
4. Haz clic otra vez en **Rastrear precedentes** para ir un nivel más atrás. Cada clic agrega un nivel. Sigue haciendo clic hasta que no aparezca ninguna flecha nueva.
5. Si aparece una flecha negra punteada que apunta a un icono pequeño de hoja de cálculo, el precedente está en otra hoja o en otro libro. Haz doble clic en esa flecha punteada para abrir el cuadro de diálogo **[Go To]**, que enlista la referencia externa; selecciónala y haz clic en **Aceptar** para saltar allá. El libro de origen tiene que estar abierto para que esto funcione.

**Ruta de examen, dependientes, las celdas que leen esta celda**

1. Selecciona la celda.
2. Pestaña **Fórmulas**, grupo **Auditoría de fórmulas**, haz clic en **Rastrear dependientes**.
3. Haz clic otra vez por cada nivel adicional.

**Ruta de examen, quitar las flechas,** que el examen sí revisa porque quiere la hoja limpia.

1. Pestaña **Fórmulas**, grupo **Auditoría de fórmulas**, haz clic en la flecha del botón **Quitar flechas**.
2. El menú tiene tres entradas: **Quitar flechas**, **[Remove Precedent Arrows]**, **[Remove Dependent Arrows]**. Elige la que se pida. Hacer clic en la cara del botón en lugar de en su flecha ejecuta Quitar flechas y borra todo.

**Ruta de examen, seleccionar en vez de dibujar,** cuando el reactivo dice "selecciona las celdas que alimentan esta fórmula": usa **Ir a Especial** (Associate 1.2.2) y elige **[Precedents]** o **[Dependents]**. Debajo se encienden dos opciones más, **[Direct only]** y **[All levels]**; escoge la que pida el reactivo. [Direct only] es un solo nivel, [All levels] recorre toda la cadena. Haz clic en **Aceptar** y las celdas quedan seleccionadas, sin dibujar ninguna flecha.

<!-- ES-FIN MO201-3.5.1 -->

---

### 3.5.2 Monitor cells and formulas by using the Watch Window

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **Formulas** tab, **Formula Auditing** group, and click **Watch Window**. A pane titled **Watch Window** opens, docked or floating.
2. Click **Add Watch...** in the pane. The **Add Watch** dialog opens with the line "Select the cells that you would like to watch the value of:" and a reference box below it.
3. Select the cell or range on the sheet. The box fills with the full reference including the sheet name, for example `=Sheet1!$A$3`. A whole range may be added at once, and each cell in it becomes its own row.
4. Click **Add**.
5. The watch appears as a row in the pane under six columns: **Book**, **Sheet**, **Name**, **Cell**, **Value**, **Formula**. The Name column stays empty unless the cell carries a defined name, which is one good reason to name cells before watching them.
6. Repeat steps 2 to 4 for every cell to be monitored. Watches on other sheets and on other open workbooks all land in the same pane, which is the point of the tool.
7. Double-click any row to jump straight to that cell, wherever it is.
8. Click a column heading to sort the list by that column.
9. To remove one, select its row and click **Delete Watch**. Ctrl+click or Shift+click selects several rows at once.
10. To close the pane, click **Watch Window** on the ribbon again, or click the X in the pane's top right corner. Closing the pane does not delete the watches: reopening it brings them back.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.5.2 -->

**Ruta de examen**

1. Ve a la pestaña **Fórmulas**, grupo **Auditoría de fórmulas**, y haz clic en **Ventana Inspección**. Se abre un panel titulado **Ventana Inspección**, acoplado o flotante.
2. Haz clic en **[Add Watch...]** dentro del panel. Se abre el cuadro de diálogo **[Add Watch]** con la línea ["Select the cells that you would like to watch the value of:"] y un cuadro de referencia debajo.
3. Selecciona la celda o el rango sobre la hoja. El cuadro se llena con la referencia completa, incluido el nombre de la hoja, por ejemplo `=Sheet1!$A$3`. Se puede agregar un rango entero de una vez, y cada celda dentro de él se vuelve su propia fila.
4. Haz clic en **[Add]**.
5. La inspección aparece como una fila en el panel bajo seis columnas: **[Book]**, **Hoja**, **Nombre**, **Celda**, **Valor**, **Fórmula**. La columna Nombre se queda vacía a menos que la celda traiga un nombre definido, que es una buena razón para nombrar las celdas antes de inspeccionarlas.
6. Repite los pasos 2 a 4 con cada celda que se vaya a monitorear. Las inspecciones de otras hojas y de otros libros abiertos caen todas en el mismo panel, que es el punto de la herramienta.
7. Haz doble clic en cualquier fila para saltar directo a esa celda, esté donde esté.
8. Haz clic en un encabezado de columna para ordenar la lista por esa columna.
9. Para quitar una, selecciona su fila y haz clic en **[Delete Watch]**. Ctrl+clic o Mayús+clic selecciona varias filas a la vez.
10. Para cerrar el panel, haz clic otra vez en **Ventana Inspección** en la cinta de opciones, o haz clic en la X de la esquina superior derecha del panel. Cerrar el panel no borra las inspecciones: al volver a abrirlo regresan.

<!-- ES-FIN MO201-3.5.2 -->

---

### 3.5.3 Validate formulas by using error checking rules

**EN · texto fuente, no editar**

**Exam route, part A, run the check**

1. Select the first cell of the area to be checked, or any cell if the whole sheet is in scope.
2. Go to the **Formulas** tab, **Formula Auditing** group. **Error Checking** is a split button.
3. Click the button face, or open its arrow and click **Error Checking...**. The **Error Checking** dialog opens on the first flagged cell.
4. Read what it shows. It names the cell, for example "Error in cell D1", prints the formula underneath, gives the error type as a heading, for example "Divide by Zero Error", and explains it in one sentence.
5. Choose one of the four action buttons down the right side:
   - **Help on this Error** opens the help topic.
   - **Show Calculation Steps** hands the cell straight to the **Evaluate Formula** dialog. This is the bridge between this objective and 3.5.4.
   - **Ignore Error** marks this one cell as reviewed and moves on.
   - **Edit in Formula Bar** puts the cursor in the formula so you can fix it, and the dialog then offers **Resume** to carry on checking.
6. Use **Previous** and **Next** at the bottom to walk the remaining flags.
7. When the sweep finishes, Excel says the error check is complete for the sheet. Click **OK**.

**Exam route, part B, change which rules are enforced.** This is the half of the objective that is actually about rules, and it lives in Excel Options, not on the ribbon.

1. Click **Options...** inside the Error Checking dialog, or go to the **File** tab, click **Options**, and select **Formulas** in the category list on the left.
2. Under **Error Checking**, the **Enable background error checking** check box switches the green triangles on and off for the whole application. **Indicate errors using this color** sets the triangle colour. **Reset Ignored Errors** un-ignores everything that was dismissed with Ignore Error, across the workbook.
3. Under **Error checking rules**, tick or clear the individual rules. On Microsoft 365 build 16.0.20228 there are twelve, and these are their exact captions:
   1. Cells containing formulas or PivotTables that result in an error
   2. Inconsistent calculated column formula in tables
   3. Cells containing years represented as 2 digits
   4. Numbers formatted as text or preceded by an apostrophe
   5. Formulas inconsistent with other formulas in the region
   6. Formulas which omit cells in a region
   7. Unlocked cells containing formulas
   8. Formulas referring to empty cells
   9. Data entered in a table is invalid
   10. Misleading number formats
   11. Cells containing data types that couldn't refresh
   12. Cells containing stale values
4. Click **OK**.
5. Note for anyone teaching from an Office 2019 machine: rules 10, 11 and 12 are not there. Office 2019 shows nine, and those first nine are the ones MO-201 can ask about.

**Exam route, part C, the inline route on a single cell**

1. Click a cell carrying a green triangle in its top left corner.
2. Click the warning button that appears to the left of the cell.
3. The menu names the error on its first line and then offers the same choices, including **Help on this error**, **Show Calculation Steps...**, **Ignore Error**, **Edit in Formula Bar** and **Error Checking Options...**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.5.3 -->

**Ruta de examen, parte A, ejecutar la comprobación**

1. Selecciona la primera celda del área que se va a comprobar, o cualquier celda si toda la hoja está dentro del alcance.
2. Ve a la pestaña **Fórmulas**, grupo **Auditoría de fórmulas**. **Comprobación de errores** es un botón dividido.
3. Haz clic en la cara del botón, o abre su flecha y haz clic en **Comprobación de errores...**. El cuadro de diálogo **Comprobación de errores** se abre en la primera celda marcada.
4. Lee lo que muestra. Nombra la celda, por ejemplo ["Error in cell D1"], imprime la fórmula debajo, da el tipo de error como encabezado, por ejemplo ["Divide by Zero Error"], y lo explica en una sola oración.
5. Elige uno de los cuatro botones de acción del lado derecho:
   - **[Help on this Error]** abre el tema de ayuda.
   - **[Show Calculation Steps]** pasa la celda directo al cuadro de diálogo **Evaluar fórmula**. Este es el puente entre este objetivo y el 3.5.4.
   - **[Ignore Error]** marca esta celda como revisada y sigue adelante.
   - **[Edit in Formula Bar]** pone el cursor en la fórmula para que la corrijas, y entonces el cuadro de diálogo ofrece **[Resume]** para continuar la comprobación.
6. Usa **Anterior** y **Siguiente** al final para recorrer las marcas que quedan.
7. Cuando termina el barrido, Excel dice que la comprobación de errores está completa para la hoja. Haz clic en **Aceptar**.

**Ruta de examen, parte B, cambiar qué reglas se aplican.** Esta es la mitad del objetivo que de verdad trata de reglas, y vive en Opciones de Excel, no en la cinta de opciones.

1. Haz clic en **[Options...]** dentro del cuadro de diálogo Comprobación de errores, o ve a la pestaña **Archivo**, haz clic en **Opciones** y selecciona **Fórmulas** en la lista de categorías de la izquierda.
2. En **Comprobación de errores**, la casilla **[Enable background error checking]** enciende y apaga los triángulos verdes para toda la aplicación. **[Indicate errors using this color]** define el color del triángulo. **[Reset Ignored Errors]** deshace todo lo que se descartó con [Ignore Error], en todo el libro.
3. En **[Error checking rules]**, marca o desmarca las reglas individuales. En la compilación 16.0.20228 de Microsoft 365 hay doce, y estos son sus rótulos exactos:
   1. [Cells containing formulas or PivotTables that result in an error]
   2. [Inconsistent calculated column formula in tables]
   3. [Cells containing years represented as 2 digits]
   4. [Numbers formatted as text or preceded by an apostrophe]
   5. [Formulas inconsistent with other formulas in the region]
   6. [Formulas which omit cells in a region]
   7. [Unlocked cells containing formulas]
   8. [Formulas referring to empty cells]
   9. [Data entered in a table is invalid]
   10. [Misleading number formats]
   11. [Cells containing data types that couldn't refresh]
   12. [Cells containing stale values]
4. Haz clic en **Aceptar**.
5. Nota para quien enseñe desde una máquina con Office 2019: las reglas 10, 11 y 12 no están. Office 2019 muestra nueve, y esas primeras nueve son las que MO-201 puede preguntar.

**Ruta de examen, parte C, la ruta en línea sobre una sola celda**

1. Haz clic en una celda que traiga un triángulo verde en su esquina superior izquierda.
2. Haz clic en el botón de advertencia que aparece a la izquierda de la celda.
3. El menú nombra el error en su primera línea y después ofrece las mismas opciones, incluidas **[Help on this error]**, **[Show Calculation Steps...]**, **[Ignore Error]**, **[Edit in Formula Bar]** y **[Error Checking Options...]**.

<!-- ES-FIN MO201-3.5.3 -->

---

### 3.5.4 Evaluate formulas

**EN · texto fuente, no editar**

**Exam route**

1. Select the single cell holding the formula. Evaluate Formula works on one cell at a time.
2. Go to the **Formulas** tab, **Formula Auditing** group, and click **Evaluate Formula**.
3. Read the layout. **Reference:** at the top shows the cell being evaluated, fully qualified, for example `Sheet1!$A$3`. **Evaluation:** below it shows the formula with one part underlined. Under the box the dialog states the rule: "To show the result of the underlined expression, click Evaluate. The most recent result appears italicized."
4. Click **Evaluate**. The underlined part is replaced by its result, shown in italic, and the underline moves to the next part to be worked out. This is Excel's own order of evaluation made visible, which is the whole reason the tool exists.
5. Keep clicking **Evaluate** until the dialog has reduced the formula to a single value. At that point the button offers to restart the evaluation.
6. When the underlined part is a reference to another cell that itself holds a formula, **Step In** becomes available. Click it to open that cell's formula in the same dialog, indented below. Work through it, then click **Step Out** to collapse back and carry the resolved value into the outer formula.
7. **Step In** stays greyed out in two cases: when the underlined reference appears for the second time in the same formula, and when it points at a cell in a different workbook. Do not spend exam time trying to make it light up.
8. Click **Close** when done. The dialog has no OK; evaluating changes nothing on the sheet.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.5.4 -->

**Ruta de examen**

1. Selecciona la única celda que contiene la fórmula. Evaluar fórmula trabaja sobre una celda a la vez.
2. Ve a la pestaña **Fórmulas**, grupo **Auditoría de fórmulas**, y haz clic en **Evaluar fórmula**.
3. Lee la disposición. **[Reference:]** arriba muestra la celda que se está evaluando, con la referencia completa, por ejemplo `Sheet1!$A$3`. **[Evaluation:]** debajo muestra la fórmula con una parte subrayada. Bajo el cuadro, el cuadro de diálogo enuncia la regla: ["To show the result of the underlined expression, click Evaluate. The most recent result appears italicized."]
4. Haz clic en **[Evaluate]**. La parte subrayada queda reemplazada por su resultado, mostrado en cursiva, y el subrayado se mueve a la siguiente parte por resolver. Así se ve el orden de evaluación del propio Excel, que es toda la razón de ser de la herramienta.
5. Sigue haciendo clic en **[Evaluate]** hasta que el cuadro de diálogo haya reducido la fórmula a un solo valor. En ese punto el botón ofrece reiniciar la evaluación.
6. Cuando la parte subrayada es una referencia a otra celda que a su vez contiene una fórmula, **[Step In]** se habilita. Haz clic para abrir la fórmula de esa celda en el mismo cuadro de diálogo, con sangría debajo. Recórrela y después haz clic en **[Step Out]** para colapsarla de vuelta y llevar el valor resuelto a la fórmula exterior.
7. **[Step In]** se queda en gris en dos casos: cuando la referencia subrayada aparece por segunda vez en la misma fórmula, y cuando apunta a una celda de otro libro. No gastes tiempo de examen tratando de encenderlo.
8. Haz clic en **Cerrar** cuando termines. El cuadro de diálogo no tiene Aceptar; evaluar no cambia nada en la hoja.

<!-- ES-FIN MO201-3.5.4 -->

---

### 3.6.1 Record simple macros

**EN · texto fuente, no editar**

**Exam route**

1. Put the Developer tab on the ribbon once, at the start of the session (Expert 1.1.3, step 1).
2. Decide where the macro starts and click that cell now. The recorder captures the cursor position from the first action, not from before it.
3. Go to the **Developer** tab, **Code** group, and click **Record Macro...**. The same command sits on the **View** tab under **Macros**, and as a small square at the far left of the status bar.
4. The **Record Macro** dialog has four boxes: **Macro name**, **Shortcut key**, **Store macro in**, **Description**.
5. Open **Store macro in** and choose **This Workbook** to keep the macro in this file, **Personal Macro Workbook** to have it in every workbook you open on this machine, or **New Workbook**.
6. Click **OK**. Recording has begun; the status bar square turns into a stop square.
7. Before touching the data, settle the reference mode: **Developer** tab, **Code** group, **Use Relative References**. With it off, the recorder writes the address you clicked, so the macro always works on the same cells. With it on, it writes the offset from where the macro started, so the macro works wherever the cursor is.
8. Do the work. Use the ribbon and the keyboard. Every selection, every scroll to a named cell and every wrong click is written down.
9. Go to the **Developer** tab, **Code** group, and click **Stop Recording**, or click the square on the status bar.
10. Go to the **File** tab, **Save As**, open **Save as type** and choose **Excel Macro-Enabled Workbook (\*.xlsm)**. Saving as `.xlsx` drops the module, and the only warning is a dialog most people click through.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.6.1 -->

**Ruta de examen**

1. Pon la pestaña Programador en la cinta de opciones una sola vez, al inicio de la sesión (Expert 1.1.3, paso 1).
2. Decide dónde empieza la macro y haz clic en esa celda ahora. La grabadora captura la posición del cursor desde la primera acción, no desde antes de ella.
3. Ve a la pestaña **Programador**, grupo **[Code]**, y haz clic en **Grabar macro...**. El mismo comando está en la pestaña **Vista** bajo **Macros**, y como un cuadrito en el extremo izquierdo de la barra de estado.
4. El cuadro de diálogo **Grabar macro** tiene cuatro cuadros: **Nombre de la macro**, **[Shortcut key]**, **[Store macro in]**, **[Description]**.
5. Abre **[Store macro in]** y elige **[This Workbook]** para dejar la macro en este archivo, **[Personal Macro Workbook]** para tenerla en todos los libros que abras en esta máquina, o **[New Workbook]**.
6. Haz clic en **Aceptar**. La grabación ya empezó; el cuadrito de la barra de estado se convierte en un cuadro de detener.
7. Antes de tocar los datos, define el modo de referencia: pestaña **Programador**, grupo **[Code]**, **[Use Relative References]**. Con la opción apagada, la grabadora escribe la dirección en la que hiciste clic, así que la macro siempre trabaja sobre las mismas celdas. Con la opción encendida, escribe el desplazamiento desde donde arrancó la macro, así que la macro trabaja donde esté el cursor.
8. Haz el trabajo. Usa la cinta de opciones y el teclado. Cada selección, cada desplazamiento hasta una celda con nombre y cada clic equivocado quedan anotados.
9. Ve a la pestaña **Programador**, grupo **[Code]**, y haz clic en **[Stop Recording]**, o haz clic en el cuadro de la barra de estado.
10. Ve a la pestaña **Archivo**, **Guardar como**, abre **[Save as type]** y elige **[Excel Macro-Enabled Workbook (\*.xlsm)]**. Guardar como `.xlsx` tira el módulo, y la única advertencia es un cuadro de diálogo que la mayoría de la gente cierra sin leer.

<!-- ES-FIN MO201-3.6.1 -->

---

### 3.6.2 Name simple macros

**EN · texto fuente, no editar**

**Exam route**

1. Type the name in the **Macro name** box of the **Record Macro** dialog, before recording, not after. There is no rename command anywhere in Excel's interface.
2. Obey the rules the box enforces: the first character must be a letter; no spaces, full stops, hyphens or other punctuation; letters, digits and the underscore only; up to 255 characters; and the name may not be a cell reference such as `A1` or `R1C1`, nor a name already used by another macro in the same workbook.
3. If the name breaks a rule, Excel refuses on OK, shows a message, and leaves the dialog open with the name still in the box.
4. Fill **Shortcut key** with a single letter. Excel prefixes it with `Ctrl+`. Hold Shift while typing the letter and the box shows `Ctrl+Shift+` instead. Prefer the Shift form: a macro assigned to `Ctrl+c` or `Ctrl+s` takes that key away from Excel for as long as the workbook is open.
5. Type a **Description**. It appears under the list in the Macro dialog and is the only documentation a recorded macro ever gets.
6. Click **OK**.
7. To rename after the fact, press Alt+F11, open the module, and edit the name on the `Sub` line: `Sub Old_Name()` becomes `Sub New_Name()`. The `End Sub` line does not change.
8. Press Alt+F8, select the macro, and click **Options...** to change the Shortcut key and the Description later. That dialog does not offer the name.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.6.2 -->

**Ruta de examen**

1. Escribe el nombre en el cuadro **Nombre de la macro** del cuadro de diálogo **Grabar macro**, antes de grabar, no después. No hay ningún comando de cambiar nombre en toda la interfaz de Excel.
2. Respeta las reglas que impone el cuadro: el primer carácter tiene que ser una letra; nada de espacios, puntos, guiones ni otra puntuación; solo letras, dígitos y guion bajo; hasta 255 caracteres; y el nombre no puede ser una referencia de celda como `A1` o `R1C1`, ni un nombre que ya use otra macro del mismo libro.
3. Si el nombre rompe una regla, Excel lo rechaza al hacer clic en Aceptar, muestra un mensaje y deja el cuadro de diálogo abierto con el nombre todavía en el cuadro.
4. Llena **[Shortcut key]** con una sola letra. Excel le antepone `Ctrl+`. Mantén presionada Mayús mientras escribes la letra y el cuadro muestra `Ctrl+Mayús+` en su lugar. Prefiere la forma con Mayús: una macro asignada a `Ctrl+c` o a `Ctrl+s` le quita esa tecla a Excel mientras el libro esté abierto.
5. Escribe una **[Description]**. Aparece debajo de la lista en el cuadro de diálogo de macros y es la única documentación que una macro grabada llega a tener.
6. Haz clic en **Aceptar**.
7. Para cambiar el nombre después de los hechos, presiona Alt+F11, abre el módulo y edita el nombre en la línea `Sub`: `Sub Nombre_Viejo()` se vuelve `Sub Nombre_Nuevo()`. La línea `End Sub` no cambia.
8. Presiona Alt+F8, selecciona la macro y haz clic en **[Options...]** para cambiar después la tecla de método abreviado y la descripción. Ese cuadro de diálogo no ofrece el nombre.

<!-- ES-FIN MO201-3.6.2 -->

---

### 3.6.3 Edit simple macros

**EN · texto fuente, no editar**

**Exam route**

1. Go to the **Developer** tab, **Code** group, and click **Macros**, or press Alt+F8.
2. Select the macro in the list and click **Edit**. The Visual Basic Editor opens with the cursor inside the `Sub`.
3. Read what the recorder wrote before changing anything. A recorded step is almost always two lines: `Range("B2").Select` and then `Selection.something`.
4. Delete the lines that undo work done a moment earlier. The recorder writes every click including the ones that corrected a mistake, and those lines are the first thing the objective expects you to remove.
5. Collapse a `Select` and its `Selection` line into one. `Range("B2").Select` followed by `Selection.Font.Bold = True` becomes `Range("B2").Font.Bold = True`. The macro stops moving the cursor and runs faster.
6. Change literals to make the macro general: an address, a colour index, a number format string, a sheet name.
7. Put an apostrophe at the start of a line to comment it out, so you can test without deleting.
8. Press F8 to step through one line at a time and watch the sheet redraw. Press F5 to run the whole `Sub`.
9. Put the cursor on a line and press F9 to set a breakpoint. The line turns dark red and F5 stops there.
10. Press Alt+Q to close the editor and return to Excel.
11. Save with Ctrl+S. The file must still be `.xlsm`.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-3.6.3 -->

**Ruta de examen**

1. Ve a la pestaña **Programador**, grupo **[Code]**, y haz clic en **Macros**, o presiona Alt+F8.
2. Selecciona la macro en la lista y haz clic en **Modificar**. Se abre el **[Visual Basic Editor]** con el cursor dentro del `Sub`.
3. Lee lo que escribió la grabadora antes de cambiar nada. Un paso grabado casi siempre son dos líneas: `Range("B2").Select` y después `Selection.something`.
4. Borra las líneas que deshacen trabajo hecho un momento antes. La grabadora escribe cada clic, incluidos los que corrigieron un error, y esas líneas son lo primero que el objetivo espera que quites.
5. Junta un `Select` y su línea `Selection` en una sola. `Range("B2").Select` seguido de `Selection.Font.Bold = True` se vuelve `Range("B2").Font.Bold = True`. La macro deja de mover el cursor y corre más rápido.
6. Cambia los literales para volver general la macro: una dirección, un índice de color, una cadena de formato de número, un nombre de hoja.
7. Pon un apóstrofo al inicio de una línea para comentarla, y así puedes probar sin borrar.
8. Presiona F8 para recorrerla línea por línea y ver cómo se redibuja la hoja. Presiona F5 para correr todo el `Sub`.
9. Pon el cursor en una línea y presiona F9 para poner un punto de interrupción. La línea se pinta de rojo oscuro y F5 se detiene ahí.
10. Presiona Alt+Q para cerrar el editor y volver a Excel.
11. Guarda con Ctrl+S. El archivo tiene que seguir siendo `.xlsm`.

<!-- ES-FIN MO201-3.6.3 -->

---

## MO-201 Expert · Domain 4, Manage advanced charts and tables

### 4.1.1 Create and modify dual axis charts

**EN · texto fuente, no editar**

**Exam route**

1. Select the range holding both series, headers included. The two series must differ in magnitude, for example Units in the tens and Revenue in the thousands.
2. Go to the **Insert** tab, **Charts** group, and click **Insert Combo Chart**. Do not use Recommended Charts.
3. At the bottom of the gallery click **Create Custom Combo Chart...**. The **Insert Chart** dialog opens on the **All Charts** tab with **Combo** already selected.
4. Under the heading "Choose the chart type and axis for your data series", find the row for the second series.
5. Open that row's **Chart Type** list and pick **Line** or **Line with Markers**.
6. In the same row, select the **Secondary Axis** check box. Both changes are made before the dialog closes, in one operation.
7. Click **OK**. The chart now carries a value axis on the left and a second one on the right.
8. Label the second axis: with the chart selected, go to the **Chart Design** contextual tab, **Chart Layouts** group, click **Add Chart Element**, point to **Axis Titles**, click **Secondary Vertical**.

To move a series that already exists onto the secondary axis without rebuilding the chart:

1. With the chart selected, go to the **Format** contextual tab, **Current Selection** group.
2. Open the **Chart Elements** list and choose the series by name. This is the graded way to select a thin series you cannot click.
3. Click **Format Selection**.
4. In the **Format Data Series** pane, **Series Options**, under **Plot Series On**, select **Secondary Axis**.

The contextual tab is captioned **Chart Design** on this build, and the ribbon resources also carry the older label **Design**. The Associate chart objectives use **Chart Design** throughout; treat **Design** as the same tab and see "Still to confirm".

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.1.1 -->

**Ruta de examen**

1. Selecciona el rango que contiene las dos series, encabezados incluidos. Las dos series deben diferir en magnitud, por ejemplo Unidades en decenas e Ingresos en miles.
2. Ve a la pestaña **Insertar**, grupo **Gráficos**, y haz clic en **[Insert Combo Chart]**. No uses Gráficos recomendados.
3. Al final de la galería haz clic en **[Create Custom Combo Chart...]**. Se abre el cuadro de diálogo **[Insert Chart]** en la pestaña **[All Charts]** con **Gráficos combinados** ya seleccionado.
4. Bajo el encabezado "[Choose the chart type and axis for your data series]", localiza la fila de la segunda serie.
5. Abre la lista **[Chart Type]** de esa fila y elige **Línea** o **[Line with Markers]**.
6. En la misma fila, marca la casilla **[Secondary Axis]**. Los dos cambios se hacen antes de que se cierre el cuadro de diálogo, en una sola operación.
7. Haz clic en **Aceptar**. El gráfico ahora lleva un eje de valores a la izquierda y otro a la derecha.
8. Ponle título al segundo eje: con el gráfico seleccionado, ve a la pestaña contextual **Diseño de gráfico**, grupo **[Chart Layouts]**, haz clic en **[Add Chart Element]**, coloca el puntero en **Títulos de eje** y haz clic en **[Secondary Vertical]**.

Para mover al eje secundario una serie que ya existe, sin rehacer el gráfico:

1. Con el gráfico seleccionado, ve a la pestaña contextual **Formato**, grupo **[Current Selection]**.
2. Abre la lista **Elementos de gráfico** y elige la serie por su nombre. Esta es la forma que puntúa para seleccionar una serie delgada en la que no puedes hacer clic.
3. Haz clic en **[Format Selection]**.
4. En el panel **[Format Data Series]**, **[Series Options]**, bajo **[Plot Series On]**, selecciona **[Secondary Axis]**.

En esta versión la pestaña contextual aparece rotulada **Chart Design**, que el glosario traduce como **Diseño de gráfico**, y los recursos de la cinta traen además la etiqueta más antigua **Design**. Los objetivos de gráficos del Associate usan **Chart Design** en todo el documento; trata **Design** como la misma pestaña y consulta "Still to confirm".

<!-- ES-FIN MO201-4.1.1 -->

---

### 4.1.2 Create and modify charts including Box & Whisker, Combo, Funnel, Histogram, Map, Sunburst, and Waterfall

**EN · texto fuente, no editar**

**Exam route**

1. Select the source data including headers. Sunburst and Treemap need one column per hierarchy level, outermost level last, with blanks where a level does not apply. Funnel needs a single series already sorted from largest to smallest.
2. Go to the **Insert** tab, **Charts** group, and open the gallery that owns the type:
   - **Insert Statistic Chart** for Histogram, Pareto, and Box and Whisker (Certiport spells it Box & Whisker; the gallery entry reads Box and Whisker, **TO CONFIRM** the ampersand).
   - **Insert Hierarchy Chart** for Treemap and Sunburst.
   - The Waterfall, Funnel, Stock, Surface and Radar gallery for Waterfall and Funnel (**TO CONFIRM** the full button caption).
   - **Insert Combo Chart** for Combo.
   - **Maps**, then **Filled Map**, for Map. Map needs an internet connection because it resolves place names through Bing, and MO-211 removed this chart type from the 365 objective list.
3. Click the thumbnail. The chart lands on the current sheet.

The dialog route reaches every one of these and is the safer answer when the task names a subtype you cannot find in a gallery: select the data, open the **Insert Chart** dialog as in Associate 5.1.1, go to the **All Charts** tab, pick the category in the left list, pick the subtype from the thumbnails at the top, click **OK**. The same dialog opens from **All Chart Types...** at the bottom of any chart gallery.

To change an existing chart into one of these types: click the chart once, **Chart Design** tab, **Type** group, **Change Chart Type...**, **All Charts** tab, pick the new category and subtype, **OK**.

Type-specific modifications the exam asks for:

- *Histogram bins:* click the horizontal axis, press Ctrl+1, and in the **Format Axis** pane, **Axis Options**, choose **By Category**, **Automatic**, **Bin width**, or **Number of bins**, plus the overflow and underflow bin check boxes (**TO CONFIRM** those two captions).
- *Waterfall totals:* click the series once to select all columns, click the single column again to select it alone, right-click it, click **Set as Total**. The column drops to the baseline.
- *Pareto:* it is a subtype of Histogram in the **Insert Statistic Chart** gallery, not a separate category, and it adds the cumulative percentage line and its secondary axis on its own.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.1.2 -->

**Ruta de examen**

1. Selecciona los datos de origen, encabezados incluidos. El gráfico de proyección solar y el de rectángulos necesitan una columna por nivel de jerarquía, el nivel más externo al final, con celdas en blanco donde un nivel no aplica. El de embudo necesita una sola serie ya ordenada de mayor a menor.
2. Ve a la pestaña **Insertar**, grupo **Gráficos**, y abre la galería a la que pertenece el tipo:
   - **[Insert Statistic Chart]** para **Gráficos de histograma**, **Diagrama de pareto** y **Gráfico de cajas y bigotes** (Certiport lo escribe Box & Whisker; la entrada de la galería dice Box and Whisker, **TO CONFIRM** el ampersand).
   - **[Insert Hierarchy Chart]** para **Gráfico de rectángulos** y **Gráfico de proyección solar**.
   - La galería de **[Waterfall, Funnel, Stock, Surface and Radar]** para **Gráficos de cascada** y **Gráficos de embudo** (**TO CONFIRM** el texto completo del botón).
   - **[Insert Combo Chart]** para **Gráficos combinados**.
   - **Mapas**, luego **[Filled Map]**, para **Gráfico de mapa**. El mapa necesita conexión a internet porque resuelve los nombres de lugar a través de Bing, y el MO-211 quitó este tipo de gráfico de la lista de objetivos de 365.
3. Haz clic en la miniatura. El gráfico aparece en la hoja actual.

La ruta por el cuadro de diálogo llega a todos estos tipos y es la respuesta más segura cuando la tarea nombra un subtipo que no encuentras en una galería: selecciona los datos, abre el cuadro de diálogo **[Insert Chart]** como en Associate 5.1.1, ve a la pestaña **[All Charts]**, elige la categoría en la lista de la izquierda, elige el subtipo en las miniaturas de arriba y haz clic en **Aceptar**. El mismo cuadro de diálogo se abre desde **[All Chart Types...]**, al final de cualquier galería de gráficos.

Para convertir en uno de estos tipos un gráfico que ya existe: haz clic una vez en el gráfico, pestaña **Diseño de gráfico**, grupo **Tipo**, **[Change Chart Type...]**, pestaña **[All Charts]**, elige la categoría y el subtipo nuevos, **Aceptar**.

Modificaciones por tipo que pide el examen:

- *Intervalos del histograma:* haz clic en el eje horizontal, presiona Ctrl+1 y, en el panel **[Format Axis]**, **[Axis Options]**, elige **[By Category]**, **[Automatic]**, **[Bin width]** o **[Number of bins]**, más las dos casillas del intervalo de desbordamiento y del intervalo de subdesbordamiento (**TO CONFIRM** esos dos textos).
- *Totales en cascada:* haz clic una vez en la serie para seleccionar todas las columnas, haz clic otra vez en esa columna para seleccionarla sola, haz clic con el botón derecho sobre ella y haz clic en **[Set as Total]**. La columna baja a la línea base.
- *Pareto:* es un subtipo de histograma dentro de la galería **[Insert Statistic Chart]**, no una categoría aparte, y agrega por su cuenta la línea de porcentaje acumulado y su eje secundario.

<!-- ES-FIN MO201-4.1.2 -->

---

### 4.2.1 Create PivotTables

**EN · texto fuente, no editar**

**Exam route**

1. Click one single cell anywhere inside the source data. Do not select the whole column or the whole sheet. Excel expands to the surrounding block on its own and gets it right when there is one header row and no blank rows.
2. Go to the **Insert** tab, **Tables** group, and click **PivotTable**. If the button opens a menu, click **From Table/Range**.
3. In the **PivotTable from table or range** dialog (Office 2019 titles it **Create PivotTable**), check that the **Table/Range** box shows the whole block including the header row, for example `Data!$A$1:$F$61`. Correct it here if it does not.
4. Under "Choose where you want the PivotTable to be placed", select **New Worksheet**, or select **Existing Worksheet** and click the cell that will hold the top left corner so its address lands in the **Location** box.
5. Click **OK**. An empty PivotTable frame appears with the **PivotTable Fields** pane on the right.
6. In the PivotTable Fields pane, **drag** each field name into the area it belongs to: **Filters**, **Columns**, **Rows**, **Values**. Drag even when the default would be right. Ticking the check box sends text fields to Rows and numeric fields to Values, and the exam task normally names an area that is not the default.
7. Name the PivotTable: **PivotTable Analyze** contextual tab, **PivotTable** group, click into the **PivotTable Name:** box, type the name, press Enter.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.1 -->

**Ruta de examen**

1. Haz clic en una sola celda, en cualquier punto dentro de los datos de origen. No selecciones la columna completa ni la hoja completa. Excel se extiende por su cuenta al bloque que la rodea y le atina cuando hay una fila de encabezado y ninguna fila en blanco.
2. Ve a la pestaña **Insertar**, grupo **Tablas**, y haz clic en **Tabla dinámica**. Si el botón abre un menú, haz clic en **Desde una tabla o rango**.
3. En el cuadro de diálogo **[PivotTable from table or range]** (Office 2019 lo titula **[Create PivotTable]**), revisa que el cuadro **[Table/Range]** muestre el bloque completo, incluida la fila de encabezado, por ejemplo `Data!$A$1:$F$61`. Corrígelo aquí si no es así.
4. Bajo "[Choose where you want the PivotTable to be placed]", selecciona **[New Worksheet]**, o selecciona **[Existing Worksheet]** y haz clic en la celda que va a quedar en la esquina superior izquierda para que su dirección aparezca en el cuadro **[Location]**.
5. Haz clic en **Aceptar**. Aparece el marco de una tabla dinámica vacía con el panel **[PivotTable Fields]** a la derecha.
6. En el panel [PivotTable Fields], **arrastra** cada nombre de campo al área que le toca: **Filtros**, **[Columns]**, **[Rows]**, **[Values]**. Arrastra incluso cuando el destino predeterminado sea el correcto. Marcar la casilla manda los campos de texto a [Rows] y los numéricos a [Values], y la tarea del examen normalmente nombra un área que no es la predeterminada.
7. Ponle nombre a la tabla dinámica: pestaña contextual **Analizar tabla dinámica**, grupo **Tabla dinámica**, haz clic dentro del cuadro **[PivotTable Name:]**, escribe el nombre y presiona Entrar.

<!-- ES-FIN MO201-4.2.1 -->

---

### 4.2.2 Modify field selections and options

**EN · texto fuente, no editar**

This is where **Field Settings** and **Value Field Settings** are written out; 4.2.6 comes back to the same dialog for number formatting.

**Exam route**

1. Click any cell inside the **Values** area of the report. The field under the pointer becomes the active field.
2. Go to the **PivotTable Analyze** tab, **Active Field** group, and click **Field Settings**. With a value field active this opens the **Value Field Settings** dialog (**TO CONFIRM** that the dialog title reads exactly that; the right-click menu entry does).
3. On the **Summarize Values By** tab, choose the function from the "Summarize value field by" list: Sum, Count, Average, Max, Min, Product, Count Numbers, StdDev, StdDevp, Var, Varp.
4. WITHOUT closing the dialog, go to the **Show Values As** tab. Open the "Show values as" list and choose the calculation, for example **% of Grand Total**, **% of Column Total**, **% of Parent Row Total**, **Difference From**, **Running Total In**. Difference From and Running Total In enable the **Base field** and **Base item** lists below; set them.
5. Still without closing, click into the **Custom Name** box and correct the caption. Changing the function rewrites this box on its own, so "Sum of Units" becomes "Average of Units"; whatever you type here overrides it.
6. Still in the same dialog, click the **Number Format** button. A cut-down Format Cells opens showing only the **Number** tab. Pick the **Category**, set **Decimal places**, click **OK**.
7. Click **OK**. Function, calculation, caption and number format were all set in one pass through one dialog.

For a row or column field rather than a value field:

1. Click a cell in that field, **PivotTable Analyze** tab, **Active Field** group, **Field Settings**.
2. The **Field Settings** dialog opens with two tabs, **Subtotals & Filters** and **Layout & Print**. Set Subtotals to **Automatic**, **None**, or **Custom** with the function list, and set the layout to compact, outline or tabular for that one field.

For which fields are offered at all:

1. **PivotTable Analyze** tab, **Show** group. Toggle **Field List**, **+/- Buttons** and **Field Headers** (**TO CONFIRM** these three captions).
2. **PivotTable Analyze** tab, **PivotTable** group, **Options** opens the **PivotTable Options** dialog, where "For empty cells show" and "For error values show" live on the **Layout & Format** tab.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.2 -->

Aquí es donde quedan escritos completos **Configuración de campo** y **Configuración de campo de valor**; el 4.2.6 regresa al mismo cuadro de diálogo para el formato de número.

**Ruta de examen**

1. Haz clic en cualquier celda del área **[Values]** del informe. El campo que queda debajo del puntero se vuelve el campo activo.
2. Ve a la pestaña **Analizar tabla dinámica**, grupo **[Active Field]**, y haz clic en **Configuración de campo**. Con un campo de valor activo, esto abre el cuadro de diálogo **Configuración de campo de valor** (**TO CONFIRM** que el título del cuadro de diálogo diga exactamente eso; la entrada del menú contextual sí lo dice).
3. En la pestaña **Resumir valores por**, elige la función en la lista "[Summarize value field by]": Suma, Recuento, Promedio, Máx, Mín, [Product], Contar números, Desvest, [StdDevp], Var, [Varp].
4. SIN cerrar el cuadro de diálogo, ve a la pestaña **Mostrar valores como**. Abre la lista "[Show values as]" y elige el cálculo, por ejemplo **[% of Grand Total]**, **[% of Column Total]**, **[% of Parent Row Total]**, **[Difference From]**, **[Running Total In]**. [Difference From] y [Running Total In] habilitan las listas **[Base field]** y **[Base item]** de abajo; defínelas.
5. Todavía sin cerrar, haz clic dentro del cuadro **[Custom Name]** y corrige el texto. Cambiar la función reescribe este cuadro por su cuenta, así que [Sum of Units] se vuelve [Average of Units]; lo que escribas aquí manda sobre eso.
6. Sin salir del mismo cuadro de diálogo, haz clic en el botón **Formato de número**. Se abre una versión recortada de **Formato de celdas**, que solo muestra la pestaña **Número**. Elige la **Categoría**, ajusta las **Posiciones decimales** y haz clic en **Aceptar**.
7. Haz clic en **Aceptar**. La función, el cálculo, el texto y el formato de número quedaron definidos en una sola pasada por un solo cuadro de diálogo.

Para un campo de fila o de columna, en lugar de un campo de valor:

1. Haz clic en una celda de ese campo, pestaña **Analizar tabla dinámica**, grupo **[Active Field]**, **Configuración de campo**.
2. Se abre el cuadro de diálogo **Configuración de campo** con dos pestañas, **[Subtotals & Filters]** y **[Layout & Print]**. Pon los subtotales en **[Automatic]**, **Ninguno** o **Personalizada** con la lista de funciones, y define el diseño compacto, de esquema o tabular solo para ese campo.

Para controlar qué campos se ofrecen:

1. Pestaña **Analizar tabla dinámica**, grupo **Mostrar**. Activa o desactiva **[Field List]**, **[+/- Buttons]** y **[Field Headers]** (**TO CONFIRM** estos tres textos).
2. Pestaña **Analizar tabla dinámica**, grupo **Tabla dinámica**, **Opciones** abre el cuadro de diálogo **[PivotTable Options]**, donde "[For empty cells show]" y "[For error values show]" están en la pestaña **[Layout & Format]**.

<!-- ES-FIN MO201-4.2.2 -->

---

### 4.2.3 Create slicers

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the PivotTable.
2. Go to the **PivotTable Analyze** tab, **Filter** group, and click **Insert Slicer**.
3. In the **Insert Slicers** dialog, select the check box of every field the task names. Tick more than one to get several slicers in a single operation.
4. Click **OK**. One slicer object per ticked field lands on the sheet, stacked.
5. Position and size: click a slicer, go to the **Slicer** contextual tab, **Size** group, and type the **Height** and **Width**. Do not drag if the task gives measurements.
6. Lay the buttons out: **Slicer** tab, **Buttons** group, set **Columns** to spread the buttons across more than one column, and set the button Height and Width.
7. Change the header text: **Slicer** tab, **Slicer** group, click into the **Slicer Caption:** box and type (**TO CONFIRM** the box caption).
8. Everything else about the object: **Slicer** tab, **Slicer** group, **Slicer Settings...**. The dialog carries the Name, the Caption, a "Display header" check box, the item sort order ascending or descending, and the two check boxes for items with no data (**TO CONFIRM** the last three captions).
9. Drive one slicer from several PivotTables: select the slicer, **Slicer** tab, **Slicer** group, **Report Connections** (Office 2019 labels this PivotTable Connections, **TO CONFIRM** the 365 caption), tick each PivotTable in the dialog, click **OK**. They must share the same PivotCache, which means both were built from the same source without Excel being told to make a second cache.
10. Filter: click a button. For several, click the **Multi Select** button in the slicer header, or hold Ctrl while clicking.

For a date field, use a timeline instead:

1. Click inside the PivotTable, **PivotTable Analyze** tab, **Filter** group, click **Timeline**.
2. In the **Insert Timelines** dialog tick the date field, click **OK**.
3. Use the level list in the top right corner of the timeline object to switch between **Years**, **Quarters**, **Months** and **Days**, then drag across the bar to pick the span.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.3 -->

**Ruta de examen**

1. Haz clic en cualquier celda dentro de la tabla dinámica.
2. Ve a la pestaña **Analizar tabla dinámica**, grupo **Filtro**, y haz clic en **[Insert Slicer]**.
3. En el cuadro de diálogo **[Insert Slicers]**, marca la casilla de cada campo que nombre la tarea. Marca más de uno para obtener varias segmentaciones de datos en una sola operación.
4. Haz clic en **Aceptar**. Aparece en la hoja un objeto de segmentación de datos por cada campo marcado, uno encima de otro.
5. Posición y tamaño: haz clic en una segmentación de datos, ve a la pestaña contextual **Segmentación de datos**, grupo **Tamaño**, y escribe el **Alto** y el **Ancho**. No arrastres si la tarea da medidas.
6. Acomoda los botones: pestaña **Segmentación de datos**, grupo **[Buttons]**, ajusta **[Columns]** para repartir los botones en más de una columna, y ajusta el **Alto** y el **Ancho** del botón.
7. Cambia el texto del encabezado: pestaña **Segmentación de datos**, grupo **Segmentación de datos**, haz clic dentro del cuadro **[Slicer Caption:]** y escribe (**TO CONFIRM** el texto del cuadro).
8. Todo lo demás del objeto: pestaña **Segmentación de datos**, grupo **Segmentación de datos**, **[Slicer Settings...]**. El cuadro de diálogo trae el nombre, el título, una casilla "[Display header]", el orden de los elementos ascendente o descendente, y las dos casillas para los elementos sin datos (**TO CONFIRM** los últimos tres textos).
9. Manejar varias tablas dinámicas desde una sola segmentación de datos: selecciona la segmentación, pestaña **Segmentación de datos**, grupo **Segmentación de datos**, **[Report Connections]** (Office 2019 lo llama PivotTable Connections, **TO CONFIRM** el texto en 365), marca cada tabla dinámica en el cuadro de diálogo y haz clic en **Aceptar**. Las tablas dinámicas tienen que compartir la misma PivotCache, lo que significa que las dos se construyeron desde el mismo origen sin que se le pidiera a Excel una segunda caché.
10. Filtrar: haz clic en un botón. Para varios, haz clic en el botón **[Multi Select]** del encabezado de la segmentación, o mantén Ctrl mientras haces clic.

Para un campo de fecha, usa en su lugar una escala de tiempo:

1. Haz clic dentro de la tabla dinámica, pestaña **Analizar tabla dinámica**, grupo **Filtro**, haz clic en **Escala de tiempo**.
2. En el cuadro de diálogo **[Insert Timelines]** marca el campo de fecha y haz clic en **Aceptar**.
3. Usa la lista de nivel de la esquina superior derecha del objeto de escala de tiempo para cambiar entre **[Years]**, **[Quarters]**, **[Months]** y **[Days]**, y luego arrastra sobre la barra para elegir el tramo.

<!-- ES-FIN MO201-4.2.3 -->

---

### 4.2.4 Group PivotTable data

**EN · texto fuente, no editar**

**Exam route, dates**

1. Click any cell holding a date item inside the Rows or Columns area. Click the item, not the field header.
2. Go to the **PivotTable Analyze** tab, **Group** group, and click **Group Field**.
3. The **Grouping** dialog opens. **Starting at** and **Ending at** are filled from the data and their check boxes are ticked. Clear a check box to type your own boundary.
4. In the **By** list click the levels the task names. The list toggles, so clicking Months, then Quarters, then Years leaves all three highlighted; Ctrl is not needed.
5. Click **OK**.
6. Read the **PivotTable Fields** pane. Excel has added one new field per level above the original, named **Quarters** and **Years**, and left the original field holding the months. Drag them into the order the task asks for.
7. For blocks of days instead of calendar levels: in the **By** list select **Days** alone and set **Number of days** to the block size, for example 7. Days with a day count cannot be combined with Months, Quarters or Years.

**Exam route, numbers**

1. Click a cell holding a numeric item in the Rows area.
2. **PivotTable Analyze** tab, **Group** group, **Group Field**.
3. In the **Grouping** dialog set **Starting at**, **Ending at** and **By**, where By is the interval width, for example 500.
4. Click **OK**. The field now shows bands written as `0-499`, `500-999`.

**Exam route, selection**

1. Click the first row item, then Ctrl+click each of the others that belong in the same group.
2. **PivotTable Analyze** tab, **Group** group, click **Group Selection**.
3. Excel creates an item called Group1 and adds a second field to the pane, named after the original with a 2 appended.
4. Click the Group1 label in the grid, type the real name, press Enter.
5. Repeat for the remaining groups.

To undo any of the three: click a grouped item, **PivotTable Analyze** tab, **Group** group, **Ungroup**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.4 -->

**Ruta de examen, fechas**

1. Haz clic en cualquier celda que contenga un elemento de fecha dentro del área [Rows] o [Columns]. Haz clic en el elemento, no en el encabezado del campo.
2. Ve a la pestaña **Analizar tabla dinámica**, grupo **Agrupar**, y haz clic en **[Group Field]**.
3. Se abre el cuadro de diálogo **[Grouping]**. **[Starting at]** y **[Ending at]** vienen llenos con los datos y con sus casillas marcadas. Desmarca una casilla para escribir tu propio límite.
4. En la lista **[By]** haz clic en los niveles que nombre la tarea. La lista funciona como interruptor, así que hacer clic en [Months], luego en [Quarters] y luego en [Years] deja los tres resaltados; no hace falta Ctrl.
5. Haz clic en **Aceptar**.
6. Lee el panel **[PivotTable Fields]**. Excel agregó un campo nuevo por cada nivel arriba del original, llamados **[Quarters]** y **[Years]**, y dejó el campo original con los meses. Arrástralos al orden que pida la tarea.
7. Para bloques de días en lugar de niveles de calendario: en la lista **[By]** selecciona solo **[Days]** y pon **[Number of days]** en el tamaño del bloque, por ejemplo 7. Los días agrupados por número de días no se pueden combinar con [Months], [Quarters] ni [Years].

**Ruta de examen, números**

1. Haz clic en una celda que contenga un elemento numérico en el área [Rows].
2. Pestaña **Analizar tabla dinámica**, grupo **Agrupar**, **[Group Field]**.
3. En el cuadro de diálogo **[Grouping]** ajusta **[Starting at]**, **[Ending at]** y **[By]**, donde [By] es el ancho del intervalo, por ejemplo 500.
4. Haz clic en **Aceptar**. El campo ahora muestra bandas escritas como `0-499`, `500-999`.

**Ruta de examen, selección**

1. Haz clic en el primer elemento de fila, luego Ctrl+clic en cada uno de los demás que van en el mismo grupo.
2. Pestaña **Analizar tabla dinámica**, grupo **Agrupar**, haz clic en **[Group Selection]**.
3. Excel crea un elemento llamado [Group1] y agrega un segundo campo al panel, con el nombre del original y un 2 al final.
4. Haz clic en la etiqueta [Group1] dentro de la cuadrícula, escribe el nombre real y presiona Entrar.
5. Repite con los grupos que falten.

Para deshacer cualquiera de las tres: haz clic en un elemento agrupado, pestaña **Analizar tabla dinámica**, grupo **Agrupar**, **Desagrupar**.

<!-- ES-FIN MO201-4.2.4 -->

---

### 4.2.5 Add calculated fields

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the PivotTable.
2. Go to the **PivotTable Analyze** tab, **Calculations** group, and click **Fields, Items, & Sets**.
3. On the menu click **Calculated Field...**.
4. The **Insert Calculated Field** dialog opens. Type the field name in the **Name** box, for example `Revenue`.
5. Click into the **Formula** box. It contains `= 0`. Delete the zero, leaving the equals sign.
6. Build the formula from the **Fields** list at the bottom of the dialog, not by typing: click the field, click **Insert Field**, type the operator, click the next field, click **Insert Field**. The box ends up reading `= Units * Price`. A calculated field knows field names only; cell references and ranges are rejected.
7. Click **Add**. The name moves into the Name list.
8. Click **OK**. The new field appears at the bottom of the PivotTable Fields pane and lands in Values as **Sum of Revenue**.

To change one: same dialog, pick the field from the **Name** drop-down, edit the Formula box, click **Modify**, click **OK**. To remove one: pick it from the Name list, click **Delete**.

To document them: **PivotTable Analyze** tab, **Calculations** group, **Fields, Items, & Sets**, **List Formulas**. Excel writes every calculated field and calculated item, with its formula and its solve order, to a new worksheet.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.5 -->

**Ruta de examen**

1. Haz clic en cualquier celda dentro de la tabla dinámica.
2. Ve a la pestaña **Analizar tabla dinámica**, grupo **[Calculations]**, y haz clic en **[Fields, Items, & Sets]**.
3. En el menú haz clic en **Campo calculado...**.
4. Se abre el cuadro de diálogo **[Insert Calculated Field]**. Escribe el nombre del campo en el cuadro **Nombre**, por ejemplo `Revenue`.
5. Haz clic dentro del cuadro **Fórmula**. Contiene `= 0`. Borra el cero y deja el signo de igual.
6. Arma la fórmula desde la lista **[Fields]**, en la parte inferior del cuadro de diálogo, en lugar de escribirla: haz clic en el campo, haz clic en **[Insert Field]**, escribe el operador, haz clic en el siguiente campo, haz clic en **[Insert Field]**. El cuadro termina diciendo `= Units * Price`. Un campo calculado solo conoce nombres de campo; rechaza referencias de celda y rangos.
7. Haz clic en **[Add]**. El nombre pasa a la lista Nombre.
8. Haz clic en **Aceptar**. El campo nuevo aparece en la parte inferior del panel [PivotTable Fields] y queda en [Values] como **[Sum of Revenue]**.

Para cambiar uno: el mismo cuadro de diálogo, elige el campo en la lista desplegable **Nombre**, edita el cuadro Fórmula, haz clic en **[Modify]** y haz clic en **Aceptar**. Para quitar uno: elígelo en la lista Nombre y haz clic en **Eliminar**.

Para documentarlos: pestaña **Analizar tabla dinámica**, grupo **[Calculations]**, **[Fields, Items, & Sets]**, **[List Formulas]**. Excel escribe cada campo calculado y cada elemento calculado, con su fórmula y su orden de resolución, en una hoja de cálculo nueva.

<!-- ES-FIN MO201-4.2.5 -->

---

### 4.2.6 Format data

**EN · texto fuente, no editar**

**Exam route**

1. Click any cell inside the PivotTable.
2. Go to the **Design** contextual tab, the one sitting next to PivotTable Analyze.
3. **PivotTable Styles** group: click the More arrow at the bottom right of the gallery to open it fully, hover to preview, click the style the task names, for example PivotStyleMedium9.
4. **PivotTable Style Options** group, same tab: tick or clear **Row Headers**, **Column Headers**, **Banded Rows**, **Banded Columns**. These four do nothing until a style is applied, so apply the style first.
5. **Layout** group, same tab, click **Report Layout** and choose **Show in Compact Form**, **Show in Outline Form**, or **Show in Tabular Form**. The same menu carries **Repeat All Item Labels** and **Do Not Repeat Item Labels**, which is what fills the blank cells down a tabular report.
6. **Layout** group, click **Subtotals**: **Do Not Show Subtotals**, **Show all Subtotals at Bottom of Group**, **Show all Subtotals at Top of Group**.
7. **Layout** group, click **Grand Totals**: **Off for Rows and Columns**, **On for Rows and Columns**, **On for Rows Only**, **On for Columns Only**.
8. **Layout** group, click **Blank Rows**, then **Insert Blank Line after Each Item**.

For the numbers themselves, which is the half of this objective candidates lose: click a cell in the Values area, go to **PivotTable Analyze** tab, **Active Field** group, **Field Settings**, click the **Number Format** button, set the **Category** and **Decimal places** in the cut-down Format Cells dialog, click **OK**, click **OK** again (4.2.2). The format now belongs to the field, not to a block of cells.

To stop a refresh from throwing the formatting away: **PivotTable Analyze** tab, **PivotTable** group, **Options**, **Layout & Format** tab, tick "Preserve cell formatting on update" and clear "Autofit column widths on update" (**TO CONFIRM** both captions), **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.2.6 -->

**Ruta de examen**

1. Haz clic en cualquier celda dentro de la tabla dinámica.
2. Ve a la pestaña contextual **Diseño**, la que está junto a Analizar tabla dinámica.
3. Grupo **[PivotTable Styles]**: haz clic en la flecha **Más** de la esquina inferior derecha de la galería para abrirla por completo, pasa el puntero para ver la vista previa y haz clic en el estilo que nombre la tarea, por ejemplo PivotStyleMedium9.
4. Grupo **[PivotTable Style Options]**, en la misma pestaña: marca o desmarca **[Row Headers]**, **[Column Headers]**, **Filas con bandas** y **Columnas con bandas**. Estas cuatro no hacen nada hasta que se aplica un estilo, así que aplica el estilo primero.
5. Grupo **[Layout]**, en la misma pestaña, haz clic en **[Report Layout]** y elige **[Show in Compact Form]**, **[Show in Outline Form]** o **[Show in Tabular Form]**. El mismo menú trae **[Repeat All Item Labels]** y **[Do Not Repeat Item Labels]**, que es lo que llena las celdas vacías a lo largo de un informe tabular.
6. Grupo **[Layout]**, haz clic en **[Subtotals]**: **[Do Not Show Subtotals]**, **[Show all Subtotals at Bottom of Group]**, **[Show all Subtotals at Top of Group]**.
7. Grupo **[Layout]**, haz clic en **[Grand Totals]**: **[Off for Rows and Columns]**, **[On for Rows and Columns]**, **[On for Rows Only]**, **[On for Columns Only]**.
8. Grupo **[Layout]**, haz clic en **[Blank Rows]** y luego en **[Insert Blank Line after Each Item]**.

Para los números en sí, que es la mitad de este objetivo donde los candidatos pierden puntos: haz clic en una celda del área [Values], ve a la pestaña **Analizar tabla dinámica**, grupo **[Active Field]**, **Configuración de campo**, haz clic en el botón **Formato de número**, define la **Categoría** y las **Posiciones decimales** en el cuadro **Formato de celdas** recortado, haz clic en **Aceptar** y haz clic otra vez en **Aceptar** (4.2.2). El formato ahora le pertenece al campo, no a un bloque de celdas.

Para que una actualización no se lleve el formato: pestaña **Analizar tabla dinámica**, grupo **Tabla dinámica**, **Opciones**, pestaña **[Layout & Format]**, marca "[Preserve cell formatting on update]" y desmarca "[Autofit column widths on update]" (**TO CONFIRM** los dos textos), **Aceptar**.

<!-- ES-FIN MO201-4.2.6 -->

---

### 4.3.1 Create PivotCharts

**EN · texto fuente, no editar**

**Exam route, from a PivotTable that already exists**

1. Click any cell inside the PivotTable.
2. Go to the **PivotTable Analyze** tab, **Tools** group, and click **PivotChart**.
3. The **Insert Chart** dialog opens. Pick the category in the left list and the subtype from the thumbnails at the top.
4. Click **OK**. The chart lands on the same sheet, wired to the PivotTable, carrying field buttons in its corners.

**Exam route, from raw data with no PivotTable yet**

1. Click one cell inside the source data.
2. **Insert** tab, **Charts** group, click the arrow under **PivotChart**.
3. Click **PivotChart & PivotTable**.
4. Confirm the range and the destination in the dialog, click **OK**. Excel builds the PivotTable and the chart together and opens the **PivotChart Fields** pane.
5. Drag the fields into **Filters**, **Legend (Series)**, **Axis (Categories)** and **Values**. On a PivotChart the pane names the areas this way, not Rows and Columns.

To move it onto its own sheet: select the chart, **Chart Design** contextual tab, **Location** group, click **Move Chart** (**TO CONFIRM** caption on a PivotChart; on an ordinary chart it is verified at Associate 5.1.2), select **New sheet**, type the sheet name, click **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.3.1 -->

**Ruta de examen, desde una tabla dinámica que ya existe**

1. Haz clic en cualquier celda dentro de la tabla dinámica.
2. Ve a la pestaña **Analizar tabla dinámica**, grupo **[Tools]**, y haz clic en **Gráfico dinámico**.
3. Se abre el cuadro de diálogo **[Insert Chart]**. Elige la categoría en la lista de la izquierda y el subtipo en las miniaturas de arriba.
4. Haz clic en **Aceptar**. El gráfico queda en la misma hoja, conectado a la tabla dinámica, con botones de campo en las esquinas.

**Ruta de examen, desde datos en bruto y sin tabla dinámica todavía**

1. Haz clic en una celda dentro de los datos de origen.
2. Pestaña **Insertar**, grupo **Gráficos**, haz clic en la flecha que está debajo de **Gráfico dinámico**.
3. Haz clic en **[PivotChart & PivotTable]**.
4. Confirma el rango y el destino en el cuadro de diálogo y haz clic en **Aceptar**. Excel construye la tabla dinámica y el gráfico juntos, y abre el panel **[PivotChart Fields]**.
5. Arrastra los campos a **Filtros**, **[Legend (Series)]**, **[Axis (Categories)]** y **[Values]**. En un gráfico dinámico el panel nombra así las áreas, no Rows y Columns.

Para moverlo a su propia hoja: selecciona el gráfico, pestaña contextual **Diseño de gráfico**, grupo **[Location]**, haz clic en **[Move Chart]** (**TO CONFIRM** el texto en un gráfico dinámico; en un gráfico normal está verificado en Associate 5.1.2), selecciona **[New sheet]**, escribe el nombre de la hoja y haz clic en **Aceptar**.

<!-- ES-FIN MO201-4.3.1 -->

---

### 4.3.2 Manipulate options in existing PivotCharts

**EN · texto fuente, no editar**

**Exam route**

1. Click the PivotChart once to select the chart object.
2. *Field buttons:* **PivotChart Analyze** tab, **Show/Hide** group, click **Field Buttons**. The menu carries the four kinds separately (**Show Report Filter Field Buttons**, **Show Legend Field Buttons**, **Show Axis Field Buttons**, **Show Value Field Buttons**) plus **Hide All** (**TO CONFIRM** the five captions). Clear only the ones the task names: turning all of them off at once with Hide All is a different answer from turning off one kind.
3. *Filter from the chart itself:* click the axis field button or the legend field button on the chart and use its filter menu. It is the PivotTable's own filter menu, so the report changes with the chart.
4. *Change the type:* **Chart Design** contextual tab, **Type** group, **Change Chart Type...**, **All Charts** tab, pick the type, **OK**. XY (Scatter), Bubble and Stock are unavailable for a PivotChart; if the task asks for one of those it is asking for an ordinary chart.
5. *Swap the axis and the legend:* **Chart Design** tab, **Data** group, click **Switch Row/Column**. On a PivotChart this swaps the Rows and Columns areas of the PivotTable underneath, so the field list moves too. That is the difference from a plain chart and it is exactly what gets checked.
6. *Add or remove a field:* use the **PivotChart Fields** pane and drag between **Filters**, **Legend (Series)**, **Axis (Categories)** and **Values**.
7. *Add elements:* **Chart Design** tab, **Chart Layouts** group, **Add Chart Element**, then Chart Title, Axis Titles, Legend or Data Labels, and pick the position from the submenu (Associate 5.2.3).
8. *Refresh and clear:* **PivotChart Analyze** tab, **Data** group, **Refresh**; **Actions** group, **Clear**, which empties the chart and the report together.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.3.2 -->

**Ruta de examen**

1. Haz clic una vez en el gráfico dinámico para seleccionar el objeto.
2. *Botones de campo:* pestaña **[PivotChart Analyze]**, grupo **[Show/Hide]**, haz clic en **[Field Buttons]**. El menú trae los cuatro tipos por separado (**[Show Report Filter Field Buttons]**, **[Show Legend Field Buttons]**, **[Show Axis Field Buttons]**, **[Show Value Field Buttons]**) más **[Hide All]** (**TO CONFIRM** los cinco textos). Desactiva solo los que nombre la tarea: apagarlos todos de un golpe con [Hide All] es una respuesta distinta de apagar un solo tipo.
3. *Filtrar desde el gráfico mismo:* haz clic en el botón de campo del eje o en el botón de campo de la leyenda que están sobre el gráfico y usa su menú de filtro. Es el menú de filtro de la propia tabla dinámica, así que el informe cambia junto con el gráfico.
4. *Cambiar el tipo:* pestaña contextual **Diseño de gráfico**, grupo **Tipo**, **[Change Chart Type...]**, pestaña **[All Charts]**, elige el tipo, **Aceptar**. El **Gráfico XY (dispersión)**, el **Gráfico de burbujas** y el **Gráfico de cotizaciones** no están disponibles para un gráfico dinámico; si la tarea pide uno de esos, está pidiendo un gráfico normal.
5. *Intercambiar el eje y la leyenda:* pestaña **Diseño de gráfico**, grupo **Datos**, haz clic en **Cambiar fila o columna**. En un gráfico dinámico esto intercambia las áreas [Rows] y [Columns] de la tabla dinámica que está debajo, así que la lista de campos también se mueve. Esa es la diferencia con un gráfico normal y es justo lo que se revisa.
6. *Agregar o quitar un campo:* usa el panel **[PivotChart Fields]** y arrastra entre **Filtros**, **[Legend (Series)]**, **[Axis (Categories)]** y **[Values]**.
7. *Agregar elementos:* pestaña **Diseño de gráfico**, grupo **[Chart Layouts]**, **[Add Chart Element]**, y luego **Título del gráfico**, **Títulos de eje**, **Leyenda** o **Etiquetas de datos**, y elige la posición en el submenú (Associate 5.2.3).
8. *Actualizar y borrar:* pestaña **[PivotChart Analyze]**, grupo **Datos**, **Actualizar**; grupo **[Actions]**, **Borrar**, que vacía el gráfico y el informe al mismo tiempo.

<!-- ES-FIN MO201-4.3.2 -->

---

### 4.3.3 Apply styles to PivotCharts

**EN · texto fuente, no editar**

**Exam route**

1. Click the PivotChart once.
2. Go to the **Chart Design** contextual tab, **Chart Styles** group. Click the More arrow at the bottom right of the gallery to open it fully, hover to preview, click the style.
3. Same group, click **Change Colors** and pick a palette from Colorful or Monochromatic (**TO CONFIRM** the button caption on a PivotChart; on an ordinary chart it is verified at Associate 5.3.2).
4. **Chart Layouts** group, same tab, click **Quick Layout** and pick a layout. Quick Layout decides which elements are present; the style decides how they look. A task that names both wants both, in that order, because changing the layout can reintroduce elements the style had hidden.
5. To style one element rather than the whole chart: **Format** contextual tab, **Current Selection** group, open the **Chart Elements** list, pick the element by name, click **Format Selection**. The Format pane opens on that element.
6. Shape formatting: **Format** tab, **Shape Styles** group, use the gallery or **Shape Fill**, **Shape Outline**, **Shape Effects**.
7. Text formatting: **Format** tab, **WordArt Styles** group, use the gallery or **Text Fill**, **Text Outline**, **Text Effects**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.3.3 -->

**Ruta de examen**

1. Haz clic una vez en el gráfico dinámico.
2. Ve a la pestaña contextual **Diseño de gráfico**, grupo **Estilos de gráfico**. Haz clic en la flecha **Más** de la esquina inferior derecha de la galería para abrirla por completo, pasa el puntero para ver la vista previa y haz clic en el estilo.
3. En el mismo grupo, haz clic en **[Change Colors]** y elige una paleta de [Colorful] o de [Monochromatic] (**TO CONFIRM** el texto del botón en un gráfico dinámico; en un gráfico normal está verificado en Associate 5.3.2).
4. Grupo **[Chart Layouts]**, en la misma pestaña, haz clic en **Diseño rápido** y elige un diseño. El diseño rápido decide qué elementos están presentes; el estilo decide cómo se ven. Una tarea que nombre los dos quiere los dos, en ese orden, porque cambiar el diseño puede regresar elementos que el estilo había ocultado.
5. Para dar formato a un solo elemento en lugar de a todo el gráfico: pestaña contextual **Formato**, grupo **[Current Selection]**, abre la lista **Elementos de gráfico**, elige el elemento por su nombre y haz clic en **[Format Selection]**. El panel de formato se abre en ese elemento.
6. Formato de forma: pestaña **Formato**, grupo **[Shape Styles]**, usa la galería o **[Shape Fill]**, **[Shape Outline]**, **[Shape Effects]**.
7. Formato de texto: pestaña **Formato**, grupo **[WordArt Styles]**, usa la galería o **[Text Fill]**, **[Text Outline]**, **[Text Effects]**.

<!-- ES-FIN MO201-4.3.3 -->

---

### 4.3.4 Drill down into PivotChart details

**EN · texto fuente, no editar**

**Exam route**

1. Give the chart something to drill through: in the **PivotChart Fields** pane, drag a second field into **Axis (Categories)** underneath the first one. The axis now has two levels, for example Region then Waiter.
2. Collapse or expand the whole level: click the chart, go to the **PivotChart Analyze** tab, **Active Field** group, check that the **Active Field:** box names the axis field, then click **Collapse Field** or **Expand Field**.
3. Collapse or expand one item only: use the small plus and minus buttons that sit on the chart's category axis. If they are missing, turn them on from **PivotChart Analyze** tab, **Show/Hide** group, **+/- Buttons** (**TO CONFIRM** caption).
4. Drill to the source rows behind a single number: switch to the PivotTable and double-click the value cell. Excel writes a new worksheet holding only the source rows that produced that cell, formatted as an Excel table.
5. Drill from the chart with Quick Explore: click a single data point, click the magnifying glass icon that appears beside it, and pick the field to drill into (**TO CONFIRM** the tool name shown on the tooltip).
6. To allow or forbid step 4 across the report: **PivotTable Analyze** tab, **PivotTable** group, **Options**, **PivotTable Options** dialog, **Data** tab, the "Enable show details" check box (**TO CONFIRM** caption), **OK**.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-4.3.4 -->

**Ruta de examen**

1. Dale al gráfico algo por donde profundizar: en el panel **[PivotChart Fields]**, arrastra un segundo campo a **[Axis (Categories)]**, debajo del primero. El eje ahora tiene dos niveles, por ejemplo Región y luego Mesero.
2. Contraer o expandir el nivel completo: haz clic en el gráfico, ve a la pestaña **[PivotChart Analyze]**, grupo **[Active Field]**, revisa que el cuadro **[Active Field:]** nombre el campo del eje y luego haz clic en **[Collapse Field]** o en **[Expand Field]**.
3. Contraer o expandir un solo elemento: usa los botones chicos de más y de menos que están sobre el eje de categorías del gráfico. Si no aparecen, actívalos desde la pestaña **[PivotChart Analyze]**, grupo **[Show/Hide]**, **[+/- Buttons]** (**TO CONFIRM** el texto).
4. Profundizar hasta las filas de origen que están detrás de un solo número: cámbiate a la tabla dinámica y haz doble clic en la celda del valor. Excel escribe una hoja de cálculo nueva que contiene solo las filas de origen que produjeron esa celda, con formato de tabla de Excel.
5. Profundizar desde el gráfico con [Quick Explore]: haz clic en un solo punto de datos, haz clic en el icono de lupa que aparece junto a él y elige el campo en el que quieres profundizar (**TO CONFIRM** el nombre de herramienta que aparece en la información en pantalla).
6. Para permitir o impedir el paso 4 en todo el informe: pestaña **Analizar tabla dinámica**, grupo **Tabla dinámica**, **Opciones**, cuadro de diálogo **[PivotTable Options]**, pestaña **Datos**, la casilla "[Enable show details]" (**TO CONFIRM** el texto), **Aceptar**.

<!-- ES-FIN MO201-4.3.4 -->

---

## Still to confirm

Nothing in this list is a guess that can be shipped. Each line is a caption, a key sequence or a Spanish term that could not be read back from the product and has to be checked against a live Excel before the material goes to the cohort. There are 82 of them: 40 English interface strings inside the routes, 40 Spanish glossary rows with no source, and 2 Spanish strings that have a source and are probably wrong anyway.

Two of them are worth more than the rest put together. Number 4 (the Document Inspector categories) and the whole of section C would close in an afternoon if somebody installed the Spanish language pack on one lab machine and opened eight dialogs. This machine has only the English resources on disk (`C:\Program Files\Microsoft Office\root\Office16\` contains `1033` and no `2058` folder) so the Spanish install-language setting never put a Spanish UI anywhere the object model could read. That single install is the highest-value thing to do before the Spanish version starts, and it doubles as the check on section D.

### Where the six drafts disagreed, and how it was settled

Six people wrote these routes and they collided in six places. None of the collisions changed a route; all six are logged below as things to verify.

1. **The number-format keyboard shortcuts.** One draft wrote them as digits (`Ctrl+Shift+1` for two decimals), another as symbols (`Ctrl+Shift+!`). They are the same keys on a US layout, because Excel binds the shifted symbol and not the digit. Written as digits with the symbol in parentheses at Associate 2.2.5, with the layout question logged as item 40.
2. **The Series dialog key sequence.** Associate 2.1.2 stated `Alt, H, F, I, S` as fact; Expert 2.1.2 flagged the same sequence TO CONFIRM. Treated as unverified in both places. Item 19.
3. **The chart contextual tab.** The Associate chart objectives call it **Chart Design**; the Expert draft noted the ribbon resources also carry **Design**. The glossary has one row, "Chart Design (contextual), Diseño de gráfico", so **Chart Design** is used throughout. Item 22.
4. **Move Chart.** Verified and unflagged at Associate 5.1.2 on an ordinary chart; flagged at Expert 4.3.1 on a PivotChart. Kept as verified for charts, unverified for PivotCharts. Item 33.
5. **Change Colors.** Same pattern: unflagged at Associate 5.3.2, flagged at Expert 4.3.3. Same treatment. Item 36.
6. **Box & Whisker.** Associate 5.1.1 lists it with an ampersand in the All Charts dialog; Expert 4.1.2 reports the gallery entry as "Box and Whisker". Both can be true, since a dialog list and a gallery tooltip are different strings. Item 23.

Two more things that are not disagreements but are worth writing down. The Expert domain 2.3 has no 2.3.3, Certiport numbers it 2.3.1, 2.3.2, 2.3.4, and nothing is missing. And the Expert macro objectives 3.6.1 to 3.6.3 arrived in the draft for domain 1; they are filed here at the end of domain 3, where their numbers put them.

### A. English interface strings inside the routes, 40

1. Associate 1.1.1, the section heading over the legacy import wizard check boxes in **File > Options > Data**.
2. Associate 1.4.1, the ribbon context-menu caption that shows the Quick Access Toolbar on builds that hide it by default.
3. Associate 1.5.2, exact punctuation of the eight **Save as type** entries.
4. Associate 1.5.4, the eleven **Document Inspector** category captions.
5. Associate 2.3.2, the KeyTip for the **Table Name:** box on the Table Design tab.
6. Associate 2.4.1, the KeyTips for the **Sparklines** group on the Insert tab.
7. Associate 3.2.3 and Expert 2.2.4, whether `Ctrl+Shift+T` toggles the Total Row on this build.
8. Associate 5.3.3, **Alt Text...** or **Edit Alt Text...** in the chart context menu.
9. Expert 1.1.2, whether the lab build shows the **Edit Links** dialog or the newer **Workbook Links** task pane.
10. Expert 1.1.3, **Disable all macros with notification** or **Disable VBA macros with notification**.
11. Expert 1.1.4, **Manage Workbook** or **Version History** on the Info pane for a local file.
12. Expert 1.2.5, **Delete thread** or **Delete comment** on the comment's `...` menu.
13. Expert 1.2.5, the caption of the **Comments and notes** list on the Page Setup Sheet tab (Office 2019 reads Comments).
14. Expert 1.2.5, whether `Ctrl+Shift+F2` inserts a note on this build.
15. Expert 1.3.1, **Set as Preferred** or **Set as Default** in the Language pane, which is the 2019 wording and MO-201 is the 2019 exam.
16. Expert 1.3.2, **Translate** or **Translate Selection** on the Review tab.
17. Expert 1.3.2, whether **Set Proofing Language...** appears on the Review tab at all, or only under File > Options > Language.
18. Expert 2.1.1, the entries on the **Flash Fill Options** button.
19. Expert 2.1.2 and Associate 2.1.2, the `Alt, H, F, I, S` key sequence for the Series dialog.
20. Expert 2.2.2, the `Alt, A, V, V` key sequence for Data Validation.
21. Expert 2.2.5, the `Alt, A, M` key sequence for Remove Duplicates.
22. Expert 4.1.1, **Chart Design** or **Design** as the contextual tab caption.
23. Expert 4.1.2, **Box & Whisker** or **Box and Whisker** in the Insert Statistic Chart gallery.
24. Expert 4.1.2, the full caption of the Waterfall, Funnel, Stock, Surface and Radar gallery button.
25. Expert 4.1.2, the overflow bin and underflow bin check box captions in the Format Axis pane.
26. Expert 4.2.2, whether the dialog title reads exactly **Value Field Settings**.
27. Expert 4.2.2, **Field List**, **+/- Buttons** and **Field Headers** in the Show group.
28. Expert 4.2.3, the **Slicer Caption:** box caption on the Slicer tab.
29. Expert 4.2.3, in Slicer Settings, the display-header check box, the sort-order options, and the two check boxes for items with no data.
30. Expert 4.2.3, **Report Connections** or **PivotTable Connections** on the 365 build.
31. Expert 4.2.4 and 4.3.4, whether `Alt+Shift+Right Arrow` and `Alt+Shift+Left Arrow` group, ungroup, expand and collapse inside a PivotTable.
32. Expert 4.2.6, "Preserve cell formatting on update" and "Autofit column widths on update" in PivotTable Options.
33. Expert 4.3.1, the **Move Chart** caption on a PivotChart.
34. Expert 4.3.1, whether `F11` on a PivotTable produces a PivotChart or a static chart.
35. Expert 4.3.2, the five entries on the **Field Buttons** menu.
36. Expert 4.3.3, the **Change Colors** caption on a PivotChart.
37. Expert 4.3.4, the **+/- Buttons** caption on the PivotChart Analyze tab.
38. Expert 4.3.4, the tool name the Quick Explore tooltip shows.
39. Expert 4.3.4, the "Enable show details" check box caption on the Data tab of PivotTable Options.
40. Associate 2.2.5, which physical keys the number-format shortcuts land on with the lab machines' keyboard layout, since Excel binds the shifted symbol and not the digit.

### B. Where the gaps cluster, and why it matters

Section C below is 40 rows long and it is not scattered. It clusters in one place: **the field labels inside dialogs**. Microsoft documents what a dialog does, not what every box in it is called, and the professor's exercises name the ribbon path and stop at the dialog door. So `Set cell`, `To value` and `By changing cell` in Goal Seek, `At each change in` and `Use function` in Subtotal, `Unique records only` in Advanced Filter, and `Report Layout` in the PivotTable are all unfilled, and those are exactly the strings an exam-route document quotes most, because a route is "in the *X* box, type *Y*".

### C. Glossary rows with no source, 40

**Ribbon tabs (4):** Help · Draw · Sparkline (contextual) · Chart Tools (contextual, 2019)

**Ribbon groups (4):** Data Tools · Forecast · Workbook Views · Show

**Format Cells (4):** Hidden (check box) · Merge cells · Orientation · Indent

**Data Validation (2):** Ignore blank · Circle Invalid Data

**Conditional formatting (2):** Greater Than / Less Than · Top 10 Items / Bottom 10 %

**Advanced Filter (1):** Unique records only

**Subtotal (2):** At each change in · Use function

**What-if analysis (5):** Set cell · To value · By changing cell · Row input cell · Column input cell

**PivotTable (5):** PivotTable Fields (pane) · Report Layout · Fields, Items & Sets · Grand Total · Drill down / Expand / Collapse

**Protection (1):** Always Open Read-Only

**Excel Options (3):** Customize Ribbon (pane) · Trust Center · Add-ins

**Commands (4):** Fill Series · Select Data Source · New Window / Arrange All · Get & Transform / From Text-CSV

**General vocabulary (3):** Sheet tab · Argument · Dialog box launcher

### D. Spanish strings that have a source and are probably still wrong, 2

1. **Advanced Filter, "Copiar a otra ubicación".** That is Microsoft's Spanish documentation page. The shipping product is widely reported to read "Copiar a otro lugar".
2. **Advanced Filter, "Filtrar la lista, de forma local".** Same page, same problem. The product is reported to read "Filtrar la lista sin moverla a otro lugar".

Both come from a page that reads as machine-translated throughout. Any other glossary row sourced to a single Microsoft page and naming a button rather than a feature deserves the same look before it ships.

---

*107 objectives documented: 59 MO-200 Associate, 48 MO-201 Expert. Counted against `associate.txt` and `expert.txt` objective by objective, no objective is missing and none appears twice.*
