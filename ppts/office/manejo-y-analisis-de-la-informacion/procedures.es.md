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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

Total row on a table, the other half of the objective, is Associate 3.2.3: **Table Design** tab, **Table Style Options** group, **Total Row** check box, then the drop-down on each total cell. What matters here is the code it writes. Verified on the professor's build: a table total row writes `=SUBTOTAL(109,[Column])`. The `1xx` codes ignore rows hidden by hand as well as rows hidden by a filter; the `9` codes ignore only the filtered ones. On unfiltered data `SUBTOTAL(9,...)`, `SUBTOTAL(109,...)` and `AGGREGATE(9,3,...)` all returned the same number, so the difference is only visible once rows are hidden.

**ES · ruta de examen, traducir aquí**

<!-- ES-INICIO MO201-2.2.4 -->

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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

_Pendiente._

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
