# Los términos de interfaz que faltan en español

Este archivo no es prosa, es una lista de trabajo. Sale de contar cada término que quedó
entre corchetes en `procedures.es.md` y en los diecisiete decks de `es/`, que es la marca
que dejamos donde el español no se pudo verificar.

## Qué pasó

El glosario de `procedures.es.md` trae 343 filas, 40 de ellas marcadas **NO SOURCE**. Las
303 que sirven se usaron todas. El problema es de tamaño: las rutas y los decks nombran
1426 cadenas de interfaz distintas, y el glosario cubre una fracción.

Donde el término estaba en el glosario, se escribió en español. Donde no estaba, quedó en
inglés entre corchetes, que es lo que manda el propio documento: "no la inventes ni la
traduzcas de oído". Son **3392 apariciones** de **1426 términos distintos**.

Esa decisión es deliberada y es reversible. Un corchete se ve y se arregla en un minuto
con Excel enfrente. Una traducción inventada no se ve, y el alumno se entera hasta que
está sentado frente a la máquina buscando un menú que no existe.

## Por qué no se resolvió aquí

La máquina donde se hizo este trabajo no tiene el paquete de idioma español de Office.
Comprobado, no supuesto:

    HKLM\SOFTWARE\Microsoft\Office\ClickToRun\Configuration  ClientCulture = en-us
    Office16\1033\XLINTL32.DLL                                 existe
    Office16\3082\                                             solo MSO.ACL, corrector

La carpeta 3082 trae únicamente las herramientas de corrección. No hay recursos de interfaz
en español en el disco, así que no hay forma de leer una sola cadena del producto ni de
tomar las capturas de `img/es/`.

## Cómo se cierra

Con un Excel en español enfrente, en una sesión. La lista de abajo va ordenada por número
de apariciones, así que los primeros cincuenta términos cierran una parte grande del total.
Por cada uno: se lee el nombre en el producto, se agrega la fila al glosario de
`procedures.es.md` con su fuente, y se corre el reemplazo sobre los archivos.

Si de paso se toman las capturas a `img/es/` con los scripts de `ppts/kit/SCREENSHOTS.md`,
se cierran dos pendientes en el mismo rato.

## La lista

1426 términos. La columna de la derecha dice en cuántos lugares aparece cada uno.

| Término en inglés | Apariciones |
|---|---|
| `OK` | 154 |
| `Function Arguments` | 28 |
| `Type` | 26 |
| `Function Library` | 25 |
| `Add` | 24 |
| `Text` | 18 |
| `Options` | 17 |
| `Profesor, David Escobar-Castillejos` | 17 |
| `Clave, TIA501 · Empresariales` | 17 |
| `Correo, descobarc@up.edu.mx` | 17 |
| `Mensajería, Google Chat institucional` | 17 |
| `Repositorio, github.com/davidowa/learning-hub` | 17 |
| `Info` | 15 |
| `Values` | 14 |
| `Table_array` | 14 |
| `Range_lookup` | 14 |
| `dialog box launcher` | 13 |
| `Name` | 12 |
| `Growth` | 12 |
| `Shrink to fit` | 12 |
| `Current Selection` | 12 |
| `Q1` | 12 |
| `All Charts` | 12 |
| `Properties` | 11 |
| `Delete` | 11 |
| `Formula result =` | 11 |
| `Criteria1` | 11 |
| `Quantity` | 11 |
| `Color` | 10 |
| `Clear Formats` | 10 |
| `Applies to` | 10 |
| `Sum` | 10 |
| `Insert Chart` | 10 |
| `Format` | 10 |
| `Criteria_range1` | 10 |
| `General` | 9 |
| `Summary` | 9 |
| `Close` | 9 |
| `Columns` | 9 |
| `Average` | 9 |
| `Insert Function` | 9 |
| `Lookup & Reference` | 9 |
| `Sheet` | 8 |
| `None` | 8 |
| `Rows` | 8 |
| `Code` | 8 |
| `Data Tools` | 8 |
| `Col_index_num` | 8 |
| `Cancel` | 8 |
| `Pv` | 8 |
| `Special` | 7 |
| `Clear` | 7 |
| `Orientation` | 7 |
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
| `Top 10` | 7 |
| `Chart Layouts` | 7 |
| `Add Chart Element` | 7 |
| `To value` | 7 |
| `From Text/CSV` | 6 |
| `File Origin` | 6 |
| `Find & Select` | 6 |
| `Top` | 6 |
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
| `Logical` | 6 |
| `Logical_test` | 6 |
| `Source.xlsx` | 6 |
| `Edit Links` | 6 |
| `Automatic` | 6 |
| `Sum_range` | 6 |
| `Set cell` | 6 |
| `Rate` | 6 |
| `Active Field` | 6 |
| `ISNUMBER` | 6 |
| `My data has headers` | 5 |
| `Table` | 5 |
| `Errors` | 5 |
| `Page` | 5 |
| `Left` | 5 |
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
| `Data Range` | 5 |
| `Between` | 5 |
| `Cell Values` | 5 |
| `Font Color` | 5 |
| `Math & Trig` | 5 |
| `Statistical` | 5 |
| `Move Chart` | 5 |
| `Change Colors` | 5 |
| `Trust Center` | 5 |
| `Manage Workbook` | 5 |
| `Language` | 5 |
| `Logical2` | 5 |
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
| `Criteria` | 5 |
| `Data` | 5 |
| `From Text (Legacy)` | 4 |
| `Get & Transform Data` | 4 |
| `Import` | 4 |
| `Load` | 4 |
| `Find` | 4 |
| `Search` | 4 |
| `Reference` | 4 |
| `Precedents` | 4 |
| `Direct only` | 4 |
| `All levels` | 4 |
| `Header/Footer` | 4 |
| `Bottom` | 4 |
| `Right` | 4 |
| `Print` | 4 |
| `Macros` | 4 |
| `Move Down` | 4 |
| `Custom Views` | 4 |
| `Horizontal` | 4 |
| `Vertical` | 4 |
| `Create PDF/XPS` | 4 |
| `Excel Macro-Enabled Workbook (\*.xlsm)` | 4 |
| `Inspect Document` | 4 |
| `Skip blanks` | 4 |
| `Month` | 4 |
| `Step value` | 4 |
| `Merge cells` | 4 |
| `Text control` | 4 |
| `Center Across Selection` | 4 |
| `Indent` | 4 |
| `Font style` | 4 |
| `Underline` | 4 |
| `More Colors` | 4 |
| `Background Color` | 4 |
| `No Color` | 4 |
| `Fill Effects` | 4 |
| `Pattern Style` | 4 |
| `Scope` | 4 |
| `Edit` | 4 |
| `Location Range` | 4 |
| `Greater Than` | 4 |
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
| `Red` | 4 |
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
| `Peso, Parte del 30 % del primer parcial` | 4 |
| `Formula result` | 4 |
| `Formato, Blackboard · un archivo .xlsx` | 4 |
| `Formato, Blackboard · dos archivos .xlsx` | 4 |
| `Adjust to` | 4 |
| `Fit to` | 4 |
| `Next` | 3 |
| `Comma` | 3 |
| `Import Data` | 3 |
| `Existing worksheet` | 3 |
| `Delimiter` | 3 |
| `Do not detect data types` | 3 |
| `Load To` | 3 |
| `Within` | 3 |
| `Look in` | 3 |
| `Notes` | 3 |
| `Go To` | 3 |
| `Dependents` | 3 |
| `Conditional formats` | 3 |
| `Subject` | 3 |
| `Clear Hyperlinks` | 3 |
| `Margins` | 3 |
| `Scaling` | 3 |
| `Paper size` | 3 |
| `Header` | 3 |
| `Comments and notes` | 3 |
| `Print Preview` | 3 |
| `Row Height` | 3 |
| `Different first page` | 3 |

Los 1176 términos restantes aparecen una o dos veces cada uno y están en los archivos, entre
corchetes. Se encuentran así:

    grep -rno '\[[^]]*\]' ppts/office/manejo-y-analisis-de-la-informacion/procedures.es.md
    grep -rno '\[[^]]*\]' ppts/office/manejo-y-analisis-de-la-informacion/es/

## Lo que no está pendiente

Todo lo demás de esos archivos sí está terminado y verificado. Las 107 rutas están
traducidas paso por paso, sin fusionar ni perder pasos. Los diecisiete decks pasan los
cuatro chequeos del kit en cero. Las fórmulas están en español, con los nombres de función
del glosario y con la coma como separador de argumentos, que es lo que corresponde a es-MX.
