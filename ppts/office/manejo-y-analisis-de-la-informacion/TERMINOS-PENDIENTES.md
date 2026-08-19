# Los terminos de interfaz que faltan en espanol

Lista de trabajo, no prosa. Sale de contar cada termino que quedo entre corchetes en
`procedures.es.md` y en los diecisiete decks de `es/`, que es la marca que dejamos donde el
espanol no se pudo verificar.

Van **%d apariciones** de **%d terminos distintos**. Eran 2,977 de 1,209.

## Lo que cerro la diferencia

Los .docx de instrucciones del profesor traian 92 capturas de pantalla de **Excel corriendo
en espanol**. Se leyeron una por una antes de retirar la carpeta `Excel/` y salieron 569
cadenas de interfaz verificadas contra el producto, que es mejor fuente que la documentacion
de Microsoft. Estan en el glosario de `procedures.es.md`, en la seccion con clave de fuente
`IMG`, y ya se sustituyeron en los archivos: 1,016 corchetes menos.

Las imagenes no se guardaron. Fueron tomadas en la maquina de otra persona y traen su nombre
en la barra de titulo y su escritorio en el cuadro.

## Tres cosas que salieron mal en esa sustitucion, y como se arreglaron

Valen mas que la lista, porque le van a volver a pasar a quien siga.

**El mismo ingles, dos controles distintos.** `Comma` es `Millares` cuando es el estilo de
celda, y es la coma cuando es el delimitador de un archivo de texto. La sustitucion automatica
puso `Millares` en la lista de delimitadores de tres lugares. Se revirtieron a corchete: la
palabra para el delimitador no aparece en ninguna captura, asi que sigue sin verificarse.

**Excel corta sus propias listas.** `Automatic` se leyo como `Automat.` en las dos capturas
donde sale, porque el cuadro de lista lo trunca. Un truncamiento no es una traduccion, asi que
esas filas volvieron a corchete.

**El boton no dice la palabra.** `Bold` en la minibarra es la letra `N`, no `Negrita`. Para
prosa se usa `Negrita`, que si aparece en la lista de estilos de fuente del cuadro Formato de
celdas. Lo mismo con `Italic`, `K` contra `Cursiva`.

## Como se cierra lo que queda

Con un Excel en espanol enfrente, o contra la documentacion de Microsoft en espanol, con URL
y confianza declarada por fila. Cuidado con la trampa que el glosario ya anota: la pagina de
formatos de numero de Microsoft escribe `Tiempo` y `Personalizado` donde el producto dice
**Hora** y **Personalizada**. Dos paginas que coincidan es el minimo para el nombre de un
control, y el glosario le gana a una pagina suelta.

Esta maquina no puede cerrarlo sola. Tiene el corrector en espanol y no el paquete de idioma
de la interfaz:

    HKLM\SOFTWARE\Microsoft\Office\ClickToRun\Configuration  ClientCulture = en-us
    Office16\1033\XLINTL32.DLL                                 existe
    Office16\3082\                                             solo MSO.ACL, corrector

## La lista

969 terminos, por numero de apariciones.

| Termino en ingles | Apariciones |
|---|---|
| `Function Arguments` | 28 |
| `Function Library` | 25 |
| `Add` | 24 |
| `Values` | 14 |
| `Range_lookup` | 14 |
| `dialog box launcher` | 13 |
| `Growth` | 12 |
| `Current Selection` | 12 |
| `All Charts` | 12 |
| `Table_array` | 12 |
| `Formula result =` | 11 |
| `Quantity` | 11 |
| `Applies to` | 10 |
| `OK` | 10 |
| `Insert Chart` | 10 |
| `Summary` | 9 |
| `Lookup & Reference` | 9 |
| `Columns` | 8 |
| `Code` | 8 |
| `Col_index_num` | 8 |
| `Pv` | 8 |
| `Rows` | 7 |
| `Linear` | 7 |
| `Stop value` | 7 |
| `Top row` | 7 |
| `Text` | 7 |
| `Chart Layouts` | 7 |
| `Add Chart Element` | 7 |
| `File Origin` | 6 |
| `Special` | 6 |
| `Save as type` | 6 |
| `Left column` | 6 |
| `Tools` | 6 |
| `Top 10` | 6 |
| `Logical_test` | 6 |
| `Criteria_range1` | 6 |
| `Criteria1` | 6 |
| `Rate` | 6 |
| `Active Field` | 6 |
| `My data has headers` | 5 |
| `Commands Not in the Ribbon` | 5 |
| `Move Up` | 5 |
| `Modify` | 5 |
| `Weekday` | 5 |
| `Trend` | 5 |
| `Time` | 5 |
| `Sample` | 5 |
| `Font Color` | 5 |
| `Math & Trig` | 5 |
| `Statistical` | 5 |
| `Move Chart` | 5 |
| `Change Colors` | 5 |
| `Trust Center` | 5 |
| `Manage Workbook` | 5 |
| `Automatic` | 5 |
| `Sum_range` | 5 |
| `Lookup_value` | 5 |
| `Row_num` | 5 |
| `Pmt` | 5 |
| `Secondary Axis` | 5 |
| `PivotTable Fields` | 5 |
| `Years` | 5 |
| `Quarters` | 5 |
| `By` | 5 |
| `Axis (Categories)` | 5 |
| `PivotChart Analyze` | 5 |
| `From Text (Legacy)` | 4 |
| `Import` | 4 |
| `Load` | 4 |
| `Find` | 4 |
| `Precedents` | 4 |
| `Direct only` | 4 |
| `All levels` | 4 |
| `Top` | 4 |
| `Left` | 4 |
| `Right` | 4 |
| `Move Down` | 4 |
| `Create PDF/XPS` | 4 |
| `Options` | 4 |
| `Excel Macro-Enabled Workbook (\*.xlsm)` | 4 |
| `Inspect Document` | 4 |
| `Skip blanks` | 4 |
| `Month` | 4 |
| `Step value` | 4 |
| `Background Color` | 4 |
| `Fill Effects` | 4 |
| `Pattern Style` | 4 |
| `Show formatting rules for` | 4 |
| `This Worksheet` | 4 |
| `Resize Table` | 4 |
| `Sort by` | 4 |
| `Value_if_true` | 4 |
| `Value_if_false` | 4 |
| `Num_chars` | 4 |
| `Start_num` | 4 |
| `Ignore_empty` | 4 |
| `Location` | 4 |
| `Select Data` | 4 |
| `Enable Content` | 4 |
| `Browse` | 4 |
| `Confirm Password` | 4 |
| `Post` | 4 |
| `Stop` | 4 |
| `Warning` | 4 |
| `Information` | 4 |
| `Apply` | 4 |
| `Fv` | 4 |
| `Show Calculation Steps` | 4 |
| `Ignore Error` | 4 |
| `Step In` | 4 |
| `Insert Combo Chart` | 4 |
| `Change Chart Type` | 4 |
| `Months` | 4 |
| `Group Field` | 4 |
| `Insert Field` | 4 |
| `Layout` | 4 |
| `Field Buttons` | 4 |
| `Fill Color` | 4 |
| `Formula result` | 4 |
| `Comma` | 3 |
| `Import Data` | 3 |
| `Existing worksheet` | 3 |
| `Delimiter` | 3 |
| `Do not detect data types` | 3 |
| `Load To` | 3 |
| `Within` | 3 |
| `Go To` | 3 |
| `Reference` | 3 |
| `Dependents` | 3 |
| `Conditional formats` | 3 |
| `Bottom` | 3 |
| `Header` | 3 |
| `Comments and notes` | 3 |
| `Name` | 3 |
| `Publish what` | 3 |
| `Warnings` | 3 |
| `Tips` | 3 |
| `Copy to New Sheet` | 3 |
| `Operation` | 3 |
| `Paste Link` | 3 |
| `AutoFill` | 3 |
| `Date unit` | 3 |
| `Day` | 3 |
| `Year` | 3 |
| `Center Across Selection` | 3 |
| `Decrease Decimal` | 3 |
| `Single Accounting` | 3 |
| `Negative numbers` | 3 |
| `New Name` | 3 |
| `Delete Rule` | 3 |
| `Sort On` | 3 |
| `Order` | 3 |
| `Insert Function` | 3 |
| `New sheet` | 3 |
| `Select Data Source` | 3 |
| `Edit Series` | 3 |
| `Colorful` | 3 |
| `Monochromatic` | 3 |
| `Store macro in` | 3 |
| `Break Link` | 3 |
| `Macro Security` | 3 |
| `Macro Settings` | 3 |
| `Unblock` | 3 |
| `Restore` | 3 |
| `Recover Unsaved Workbooks` | 3 |
| `Always Open Read-Only` | 3 |
| `Protect Workbook Structure` | 3 |
| `Password to modify` | 3 |
| `Structure` | 3 |
| `Automatic Except for Data Tables` | 3 |
| `Set as Preferred` | 3 |
| `List` | 3 |
| `Circle Invalid Data` | 3 |
| `Clear Outline` | 3 |
| `Product` | 3 |
| `StdDevp` | 3 |
| `Varp` | 3 |
| `Logical1` | 3 |
| `Logical2` | 3 |
| `Array` | 3 |
| `Column_num` | 3 |
| `Date & Time` | 3 |
| `Days` | 3 |
| `Result cells` | 3 |
| `Nper` | 3 |
| `Add Watch` | 3 |
| `Edit in Formula Bar` | 3 |
| `Evaluate` | 3 |
| `Format Selection` | 3 |
| `Format Data Series` | 3 |
| `Series Options` | 3 |
| `Insert Statistic Chart` | 3 |
| `PivotTable Options` | 3 |
| `Report Connections` | 3 |
| `Starting at` | 3 |
| `Ending at` | 3 |
| `Fields, Items, & Sets` | 3 |
| `PivotChart Fields` | 3 |
| `Legend (Series)` | 3 |
| `Show/Hide` | 3 |
| `ISNUMBER` | 3 |
| `Sales.xlsx` | 3 |
| `Legacy Wizards` | 2 |
| `Original data type` | 2 |
| `Start import at row` | 2 |
| `File origin` | 2 |
| `Tab` | 2 |
| `Semicolon` | 2 |
| `Space` | 2 |
| `Text qualifier` | 2 |
| `Data preview` | 2 |
| `Column data format` | 2 |
| `Finish` | 2 |
| `Where do you want to put the data?` | 2 |
| `New worksheet` | 2 |
| `Data Type Detection` | 2 |
| `Find and Replace` | 2 |
| `Notes` | 2 |
| `Find All` | 2 |
| `Data validation` | 2 |
| `Subject` | 2 |
| `Footer` | 2 |
| `Custom Header` | 2 |
| `Left section` | 2 |
| `Center section` | 2 |
| `Right section` | 2 |
| `Insert Date` | 2 |
| `Custom Footer` | 2 |
| `Different odd and even pages` | 2 |
| `Different first page` | 2 |
| `Scale with Document` | 2 |
| `Align with page margins` | 2 |
| `For all documents (default)` | 2 |
| `Choose commands from` | 2 |
| `Popular Commands` | 2 |
| `All Commands` | 2 |
| `Custom Views` | 2 |
| `Print settings` | 2 |
| `Tiled` | 2 |
| `Cascade` | 2 |
| `Windows of active workbook` | 2 |
| `Show All Properties` | 2 |
| `Advanced Properties` | 2 |
| `Document Properties` | 2 |
| `Author` | 2 |
| `Manager` | 2 |
| `Company` | 2 |
| `Add to Print Area` | 2 |
| `Publish as PDF or XPS` | 2 |
| `Selection` | 2 |

Los 719 restantes aparecen una o dos veces y estan en los archivos, entre corchetes.

Al contar con grep, tres cosas inflan el numero: la sintaxis de lista de YAML usa corchetes,
los enlaces de markdown tambien, y una referencia estructurada de tabla dentro de una formula
se escribe `=SUMA(Sales[Q1])`. Un conteo ingenuo da 3,392 donde el real es 1986.
