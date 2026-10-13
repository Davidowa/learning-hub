# Pruebas de VBA en Excel para Mac

Las pruebas se ejecutaron el 13 de octubre de 2026 en Microsoft Excel para Mac 16.112.3. Los resultados provienen de macros ejecutadas en Excel y guardadas en los libros de evidencia. El lector Python extrae las celdas del archivo guardado; no calcula ni simula VBA.

Se registraron 134 comprobaciones del curso: 133 pasaron y una detectó una diferencia de plataforma. La prueba original esperaba que `Chr(160)` representara el espacio duro; en este Mac, `AscW(Chr(160))` devolvió 8224. `WorksheetFunction.Unichar(160)` devolvió 160. La limpieza original dejó el espacio duro en los nombres y la corrección lo eliminó. El generador de las ediciones Mac incorpora esa corrección en español e inglés.

| Evidencia | Resultado | Contenido |
|---|---|---|
| `vba-core-104.xlsm`, hoja `VBAResultsV2` | 103 aprobadas y una diferencia de plataforma | Tipos, operadores, rangos, amortización, GoalSeek, ciclos, argumentos, UDF, clases, limpieza, filtros, tablas, gráficas, tablas dinámicas, errores y protección |
| `vba-events.xlsm`, hoja `VBAExtension` | 17 aprobadas; un error inicial del banco de pruebas | Limpieza, eventos, prevención de recursión, selección, InputBox y MsgBox |
| `vba-protection.xlsm`, hoja `VBAProtection` | Cinco aprobadas | Protección después de guardar y reabrir; pérdida y restauración de UserInterfaceOnly |
| `vba-mac-regression.xlsm`, hoja `MacRegressionResults` | Ocho aprobadas | Procedimientos finales de limpieza ES y EN; validación Mac con texto, cero, número negativo y número positivo |

El error inicial del banco de pruebas fue un SaveAs sobre una ruta construida desde un libro que todavía no se había guardado. Ese registro se conserva y se excluye del total de comprobaciones del curso. La prueba se repitió desde un libro guardado y pasó las cinco comprobaciones de protección.

Los nombres de procedimientos y hojas del banco principal se aislaron para evitar colisiones entre ejemplos. Los mensajes automáticos se registraron como texto y se normalizaron los acentos para importar el módulo. Los cuadros interactivos se probaron con entradas reales: 500000, 0.12 y la secuencia abc, aviso, 1000. Los eventos usan contadores de observación. La demostración de recursión se limita a cinco escrituras; no se ejecutó el ejemplo de recursión sin límite.

La prueba principal usa los procedimientos en español y libros de ensayo. No constituye una ejecución separada de todos los procedimientos en inglés ni de los proyectos finales de alumnos. La limpieza corregida sí se ejecutó con el código final de ambos idiomas. Los formularios de Windows y los errores intencionales de compilación quedan fuera de esta ejecución.

## Repetir las pruebas

Trabaja en copias de estos libros y guarda cada copia antes de ejecutar macros que usan `ThisWorkbook.Path`. Habilita las macros únicamente para los libros de ensayo conocidos. La hoja de resultados de cada libro conserva valores reales y esperados.

Para reconstruir el banco principal en un libro nuevo, crea primero una clase llamada `Empleado` desde Insert, Class Module y pega `Empleado-source.txt`. Importa después `RuntimeSuiteV2.bas` y ejecuta `RunAutoTestsV2`. La comprobación del Chr original conserva deliberadamente la diferencia que motivó la corrección.

Para reconstruir los eventos en otro libro nuevo, importa `RuntimeEvents.bas` y pega `SheetEventsIsolated.txt` en el módulo de la hoja cuyo nombre es Sheet1. Guarda el libro antes de ejecutar `RunExtensionTests`. Ejecuta por separado `RunHelloWorld`, `RunInputBoxes` y `RunNumericInputLoop` con las entradas indicadas arriba. Los contadores residen en el módulo estándar para observar el evento.

La prueba de protección usa `RuntimeProtection.bas` en otro libro nuevo y guardado. Ejecuta `RunProtectionRoundtrip`; Excel puede pedir acceso al directorio local de evidencia para reabrir `protection-roundtrip.xlsx`. La regresión usa `MacRegression.bas` y `RunMacRegression` en otro libro nuevo. Este módulo contiene las dos rutinas finales de limpieza tomadas de los YAML Mac.

Importa todo el código antes de la primera ejecución. Durante el trabajo, añadir módulos o miembros de hoja a proyectos ya ejecutados produjo avisos de biblioteca de objetos inválida del editor. Las pruebas restantes se ejecutaron en proyectos nuevos. Los archivos de esos intentos están en `diagnosticos/` y no son ejemplos para distribuir.

El script `read_results.py` extrae los resultados sin modificar el libro:

```bash
.venv/bin/python ppts/audit/evidencia-vba-runtime-2026-10-13/read_results.py \
  ppts/audit/evidencia-vba-runtime-2026-10-13/vba-mac-regression.xlsm \
  --sheet MacRegressionResults --out /tmp/vba-regression.json
```

La documentación de Microsoft explica el juego de caracteres de [Chr](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/chr-function) y la conversión de un valor Unicode mediante [Unichar](https://learn.microsoft.com/en-us/office/vba/api/excel.worksheetfunction.unichar). La diferencia numérica indicada arriba es una medición de este Excel para Mac.
