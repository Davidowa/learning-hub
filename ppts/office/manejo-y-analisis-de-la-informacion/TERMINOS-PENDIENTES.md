# Los términos de interfaz que faltan en español

Este archivo no es prosa, es una lista de trabajo. Sale de contar cada término que quedó
entre corchetes en `procedures.es.md` y en los diecisiete decks de `es/`, que es la marca que
dejamos donde el español no se pudo verificar.

## Qué pasó

El glosario de `procedures.es.md` trae 343 filas, 40 de ellas marcadas **NO SOURCE**. Las 303
que sirven se usaron todas. El problema es de tamaño: entre las rutas y los decks se nombran
1209 cadenas de interfaz distintas, y el glosario cubre una fracción.

Donde el término estaba en el glosario, se escribió en español. Donde no estaba, quedó en
inglés entre corchetes, que es lo que manda el propio documento: "no la inventes ni la
traduzcas de oído". Son **2977 apariciones** de **1209 términos distintos**.

Esa decisión es deliberada y es reversible. Un corchete se ve, y se arregla en un minuto con
Excel enfrente. Una traducción inventada no se ve, y el alumno se entera hasta que está
sentado frente a la máquina buscando un menú que no existe.

Un puñado de esos corchetes no son de interfaz: `Q1`, `T1`, `Source.xlsx`, `Sales.xlsx` y un
`0` son datos de ejemplo y nombres de archivo que se marcaron de más. A esos solo hay que
quitarles los corchetes.

## Por qué no se resolvió aquí

La máquina donde se hizo este trabajo no tiene el paquete de idioma español de Office.
Comprobado, no supuesto:

    HKLM\SOFTWARE\Microsoft\Office\ClickToRun\Configuration  ClientCulture = en-us
    Office16\1033\XLINTL32.DLL                                 existe
    Office16\3082\                                             solo MSO.ACL, corrector

La carpeta 3082 trae únicamente las herramientas de corrección. No hay recursos de interfaz
en español en el disco, así que no hay forma de leer una sola cadena del producto ni de tomar
las capturas de `img/es/`.

## Cómo se cierra

Dos caminos, y el segundo es el que quedó elegido.

**Con un Excel en español enfrente**, en una sesión. Se lee el nombre en el producto, se
agrega la fila al glosario con su fuente y se corre el reemplazo sobre los archivos. Si de
paso se toman las capturas a `img/es/` con los scripts de `ppts/kit/SCREENSHOTS.md`, se
cierran dos pendientes en el mismo rato.

**Contra la documentación de Microsoft en español**, que es el método con el que se construyó
el glosario original: sus fuentes M1 a M26 son páginas en español de Microsoft. Cada fila
nueva lleva su URL y una confianza declarada. Ojo con la trampa que el propio glosario ya
anota: varias páginas en español de Microsoft están traducidas por máquina, y para **nombres
de botón** eso no sirve como fuente. El caso medido está escrito ahí: la página de Filtro
avanzado escribe "Filtrar la lista, de forma local" donde el producto dice otra cosa.

Esta pasada quedó a medias. Se lanzó y se cayó completa por límite de sesión, sin escribir
nada. La lista de abajo es exactamente la entrada que necesita.

## Un ejemplo trabajado, y la trampa en vivo

Antes de que la pasada se cayera alcancé a verificar un puñado de términos a mano, y el
primero que toqué ya traía el problema. Vale la pena dejarlo escrito porque es exactamente lo
que le va a pasar a quien siga.

La página de Microsoft en español sobre formatos de número lista las categorías de la pestaña
**Número** del cuadro **Formato de celdas** así:

    General, Número, Moneda, Contabilidad, Fecha, Tiempo, Porcentaje,
    Fracción, Científico, Texto, Especial, Personalizado

Dos de esas doce están mal contra el producto. La categoría de horas se llama **Hora**, no
"Tiempo", que es traducción literal de Time. Y la última es **Personalizada** en femenino,
concordando con "categoría", no "Personalizado"; se confirma en otra página de Microsoft que
dice "en la pestaña Número, puede elegir Personalizada en la lista Categoría". El glosario
original ya traía **Personalizada**, así que el glosario le gana a esa página.

De ahí salen tres reglas para la pasada que falta:

1. Una sola página no basta para un nombre de control. Dos páginas que coincidan, o el
   glosario, que ya está verificado.
2. Cuando el glosario y una página de Microsoft se contradicen, gana el glosario. Está
   construido contra el material del profesor y contra el producto.
3. Una traducción que se lee como calco del inglés, "Tiempo" por Time, es la señal de que la
   página está traducida por máquina. Ahí no se toma el nombre de un botón.

Confirmado de paso y listo para usarse: la caja de la derecha en esa pestaña es **Tipo**.

## La lista

1209 términos, ordenados por número de apariciones. Los primeros cincuenta cierran una parte
grande del total.

| Término en inglés | Apariciones |
|---|---|
| `OK` | 154 |
| `Function Arguments` | 28 |
| `Type` | 26 |
| `Function Library` | 25 |
| `Add` | 24 |
| `Options` | 17 |
| `Text` | 17 |
| `Info` | 15 |
| `Values` | 14 |
| `Range_lookup` | 14 |
| `dialog box launcher` | 13 |
| `Name` | 12 |
| `Growth` | 12 |
| `Current Selection` | 12 |
| `Q1` | 12 |
| `All Charts` | 12 |
| `Table_array` | 12 |
| `Properties` | 11 |
| `Delete` | 11 |
| `Formula result =` | 11 |
| `Quantity` | 11 |
| `Color` | 10 |
| `Applies to` | 10 |
| `Sum` | 10 |
| `Insert Chart` | 10 |
| `Format` | 10 |
| `General` | 9 |
| `Summary` | 9 |
| `Close` | 9 |
| `Shrink to fit` | 9 |
| `Clear Formats` | 9 |
| `Average` | 9 |
| `Insert Function` | 9 |
| `Lookup & Reference` | 9 |
| `Sheet` | 8 |
| `None` | 8 |
| `Columns` | 8 |
| `Code` | 8 |
| `Data Tools` | 8 |
| `Col_index_num` | 8 |
| `Cancel` | 8 |
| `Pv` | 8 |
| `Clear` | 7 |
| `Rows` | 7 |
| `Linear` | 7 |
| `Stop value` | 7 |
| `Size` | 7 |
| `Style` | 7 |
| `Define Name` | 7 |
| `Refers to` | 7 |
| `Top row` | 7 |
| `Line` | 7 |
| `More` | 7 |
| `Count Numbers` | 7 |
| `Chart Layouts` | 7 |
| `Add Chart Element` | 7 |
| `To value` | 7 |
| `From Text/CSV` | 6 |
| `File Origin` | 6 |
| `Find & Select` | 6 |
| `Special` | 6 |
| `Orientation` | 6 |
| `Show` | 6 |
| `Hide` | 6 |
| `Title` | 6 |
| `Export` | 6 |
| `Save as type` | 6 |
| `Fill` | 6 |
| `Number Format` | 6 |
| `Left column` | 6 |
| `Tools` | 6 |
| `Count` | 6 |
| `Max` | 6 |
| `Min` | 6 |
| `More Functions` | 6 |
| `Top 10` | 6 |
| `Logical` | 6 |
| `Logical_test` | 6 |
| `Source.xlsx` | 6 |
| `Edit Links` | 6 |
| `Criteria_range1` | 6 |
| `Criteria1` | 6 |
| `Set cell` | 6 |
| `Rate` | 6 |
| `Active Field` | 6 |
| `My data has headers` | 5 |
| `Table` | 5 |
| `Page` | 5 |
| `Commands Not in the Ribbon` | 5 |
| `Move Up` | 5 |
| `Modify` | 5 |
| `Unhide` | 5 |
| `Value` | 5 |
| `Accessibility` | 5 |
| `Weekday` | 5 |
| `Trend` | 5 |
| `Time` | 5 |
| `Sample` | 5 |
| `Hidden` | 5 |
| `Font Color` | 5 |
| `Math & Trig` | 5 |
| `Statistical` | 5 |
| `Move Chart` | 5 |
| `Change Colors` | 5 |
| `Trust Center` | 5 |
| `Manage Workbook` | 5 |
| `Automatic` | 5 |
| `Language` | 5 |
| `Sum_range` | 5 |
| `Lookup_value` | 5 |
| `Row_num` | 5 |
| `By changing cell` | 5 |
| `Pmt` | 5 |
| `Secondary Axis` | 5 |
| `PivotTable Fields` | 5 |
| `Height` | 5 |
| `Width` | 5 |
| `Years` | 5 |
| `Quarters` | 5 |
| `By` | 5 |
| `Axis (Categories)` | 5 |
| `PivotChart Analyze` | 5 |
| `Data` | 5 |
| `From Text (Legacy)` | 4 |
| `Get & Transform Data` | 4 |
| `Import` | 4 |
| `Load` | 4 |
| `Find` | 4 |
| `Search` | 4 |
| `Reference` | 4 |
| `Errors` | 4 |
| `Precedents` | 4 |
| `Direct only` | 4 |
| `All levels` | 4 |
| `Header/Footer` | 4 |
| `Top` | 4 |
| `Left` | 4 |
| `Right` | 4 |
| `Print` | 4 |
| `Macros` | 4 |
| `Move Down` | 4 |
| `Custom Views` | 4 |
| `Create PDF/XPS` | 4 |
| `Excel Macro-Enabled Workbook (\*.xlsm)` | 4 |
| `Inspect Document` | 4 |
| `Skip blanks` | 4 |
| `Month` | 4 |
| `Step value` | 4 |
| `Text control` | 4 |
| `Font style` | 4 |
| `Underline` | 4 |
| `More Colors` | 4 |
| `Background Color` | 4 |
| `No Color` | 4 |
| `Fill Effects` | 4 |
| `Pattern Style` | 4 |
| `Scope` | 4 |
| `Edit` | 4 |
| `Data Range` | 4 |
| `Greater Than` | 4 |
| `Between` | 4 |
| `with` | 4 |
| `Show formatting rules for` | 4 |
| `This Worksheet` | 4 |
| `Resize Table` | 4 |
| `StdDev` | 4 |
| `Var` | 4 |
| `Sort by` | 4 |
| `AutoSum` | 4 |
| `Value_if_true` | 4 |
| `Value_if_false` | 4 |
| `Num_chars` | 4 |
| `Start_num` | 4 |
| `Ignore_empty` | 4 |
| `Recommended Charts` | 4 |
| `Location` | 4 |
| `Select Data` | 4 |
| `Enable Content` | 4 |
| `Browse` | 4 |
| `Confirm Password` | 4 |
| `Post` | 4 |
| `$-en-US` | 4 |
| `Spelling` | 4 |
| `Stop` | 4 |
| `Warning` | 4 |
| `Information` | 4 |
| `At each change in` | 4 |
| `Use function` | 4 |
| `Move or Copy` | 4 |
| `Unique records only` | 4 |
| `Apply` | 4 |
| `Fv` | 4 |
| `Show Calculation Steps` | 4 |
| `Ignore Error` | 4 |
| `Step In` | 4 |
| `Insert Combo Chart` | 4 |
| `Change Chart Type` | 4 |
| `Filters` | 4 |
| `Months` | 4 |
| `Group Field` | 4 |
| `Insert Field` | 4 |
| `Layout` | 4 |
| `Field Buttons` | 4 |
| `Fill Color` | 4 |
| `Formula result` | 4 |
| `Adjust to` | 4 |
| `Next` | 3 |
| `Comma` | 3 |
| `Import Data` | 3 |
| `Existing worksheet` | 3 |
| `Delimiter` | 3 |
| `Do not detect data types` | 3 |
| `Load To` | 3 |
| `Within` | 3 |
| `Look in` | 3 |
| `Go To` | 3 |
| `Dependents` | 3 |
| `Conditional formats` | 3 |
| `Margins` | 3 |
| `Bottom` | 3 |
| `Header` | 3 |
| `Comments and notes` | 3 |
| `Print Preview` | 3 |
| `Freeze Top Row` | 3 |
| `Horizontal` | 3 |
| `Switch Windows` | 3 |
| `Publish what` | 3 |
| `Save` | 3 |
| `Warnings` | 3 |
| `Tips` | 3 |
| `Additional Information` | 3 |
| `Copy to New Sheet` | 3 |
| `Operation` | 3 |
| `Paste Link` | 3 |
| `AutoFill` | 3 |
| `Date unit` | 3 |
| `Day` | 3 |
| `Year` | 3 |
| `Merge cells` | 3 |
| `Center` | 3 |
| `Center Across Selection` | 3 |
| `Indent` | 3 |
| `Decrease Decimal` | 3 |
| `Single Accounting` | 3 |
| `Effects` | 3 |
| `Negative numbers` | 3 |
| `Clear Contents` | 3 |
| `New Name` | 3 |
| `Create from Selection` | 3 |
| `Location Range` | 3 |

Los 959 términos restantes aparecen una o dos veces cada uno y están en los archivos, entre
corchetes. Se encuentran así:

    grep -rno "\[[^]]*\]" ppts/office/manejo-y-analisis-de-la-informacion/procedures.es.md
    grep -rno "\[[^]]*\]" ppts/office/manejo-y-analisis-de-la-informacion/es/

Cuidado al contar con grep: en los `.yaml` la sintaxis de lista de YAML también usa corchetes,
y en el markdown los enlaces igual. Un conteo ingenuo da 3,392 en vez de 2977.

## Lo que no está pendiente

Todo lo demás de esos archivos está terminado y verificado. Las 107 rutas están traducidas
paso por paso, sin fusionar ni perder pasos. Los diecisiete decks pasan los cuatro chequeos
del kit en cero. Las fórmulas llevan los nombres de función en español del glosario y la coma
como separador de argumentos, que es lo confirmado para es-MX.
