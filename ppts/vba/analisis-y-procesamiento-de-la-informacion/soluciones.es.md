# Soluciones · Análisis y Procesamiento de la Información · TIA503

Documento del profesor. Trae la solución corrida de cada ejercicio, la salida esperada, una rúbrica de diez puntos y el error que más aparece al calificar. La numeración es la misma que la del archivo de ejercicios. Los importes usan punto decimal y coma de millares, como los captura Excel en configuración de México. Donde el resultado depende de la máquina, del idioma de la interfaz o de una iteración, la solución lo dice en lugar de fingir una cifra exacta.

---

## Semana 01 · Encuadre y la primera macro grabada

### 01.1 · Reconocer

**Solución**

Al terminar, la columna D queda oculta y la E visible. Los dos renglones que tocan la E se anulan: el segundo la oculta y el tercero la vuelve a mostrar.

Para el tercer renglón de instrucción:

| Pieza | Qué es |
|---|---|
| Objeto | `Columns("E:E")`, y de ese objeto su `EntireColumn` |
| Propiedad | `Hidden` |
| Valor | `False` |

Se ejecutan tres renglones de instrucción. Solo uno, el primero, cambia el estado final de la hoja.

**Salida**

```text
Columna D: oculta
Columna E: visible
Renglones que corren:            3
Renglones que dejan efecto:      1
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Dice que D queda oculta y E visible | 4 |
| Separa bien objeto, propiedad y valor | 3 |
| Distingue los tres renglones que corren del único que deja efecto | 3 |

**Error que más se ve**

Contestar que las dos quedan ocultas, porque el nombre de la macro dice `OcultarCostos`. Se delata en que no menciona el tercer renglón.

### 01.2 · Aplicar

**Solución**

```vba
Sub PrepararCatalogo()
    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

Se borran cuatro renglones. La versión original terminaba en el mismo estado porque el último renglón vuelve a poner D en `True` y la E se había quedado en `False` dos renglones antes: el resultado coincidía por accidente, no por diseño.

**Salida**

```text
Columna D: oculta
Columna E: visible
Renglones borrados: 4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Queda un solo renglón de instrucción y es el correcto | 5 |
| El nombre del procedimiento no cambió y compila | 2 |
| Explica por qué el original llegaba al mismo estado | 3 |

**Error que más se ve**

Dejar dos renglones, el de D en `True` y el de E en `False`, creyendo que hay que escribir que la E se muestra. Se delata en que la macro escribe una instrucción para dejar algo como ya estaba.

### 01.3 · Integrar

**Solución**

Lo que escribe la grabadora, con sus comentarios en blanco:

```vba
Sub PrepararCatalogo()
'
' PrepararCatalogo Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = False
    Columns("B:B").EntireColumn.Hidden = True
End Sub
```

Editado, sin los renglones del clic deshecho:

```vba
Sub PrepararCatalogo()
    Columns("D:D").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = True
End Sub
```

Si el libro se guarda como `.xlsx`, Excel avisa que ese formato no admite código y, si el usuario acepta, el archivo queda sin la macro. Según cómo se den los clics, la grabadora también puede escribir renglones de `Select` y `Selection`; se quitan igual, y en la semana 6 se explica por qué sobran.

**Salida**

```text
Antes de correr:   B visible, C visible, D visible, E visible
Después de correr: B oculta,  C visible, D oculta,  E visible
Segunda corrida:   el mismo estado, sin cambios
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El libro es `.xlsm` y la macro corre desde el cuadro de macros | 2 |
| Entrega el código grabado y el editado, y se ve la diferencia | 4 |
| La versión editada deja B y D ocultas y es idempotente | 2 |
| Explica qué pasa al guardar como `.xlsx` | 2 |

**Error que más se ve**

Entregar solo la versión editada. Sin el código original no hay forma de calificar qué se quitó, y el ejercicio pedía las dos.

---

## Semana 02 · Unidad 1 · El editor de VBA

### 02.1 · Reconocer

**Solución**

En el cuadro de macros aparece solo `CargarMetas`. El cuadro lista los procedimientos de los módulos estándar; `AvisarMeta` vive en el módulo de la hoja y desde ahí no se ofrece.

Después de correr `CargarMetas` con F5 quedan los tres valores escritos.

Con el resaltado amarillo sobre `Range("B3").Value = 95000`, ese renglón todavía no corre: B2 ya vale 120000 y B3 sigue vacía. El amarillo marca lo pendiente, no lo hecho.

**Salida**

```text
Cuadro de macros:  CargarMetas

Después de F5:     B2 = 120000   B3 = 95000   B4 = 143000
Con el amarillo en B3:  B2 = 120000   B3 = (vacía)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Solo `CargarMetas` aparece, y explica por qué | 4 |
| Los tres valores de B2, B3 y B4 | 3 |
| B3 vacía cuando el amarillo está sobre su renglón | 3 |

**Error que más se ve**

Decir que B3 ya vale 95000 porque el renglón está resaltado. Es la confusión de la primera clase en el editor y se delata en que también adelanta un renglón el resto de la traza.

### 02.2 · Aplicar

**Solución**

```vba
Sub MostrarSegmento()
    MsgBox "Segmento Premium: 3 campañas"
End Sub

Sub EscribirTotales()
    Range("B2").Value = 3350
    Range("B3").Value = 50250
End Sub

Sub PrepararResumen()
    Call MostrarSegmento
    Call EscribirTotales
End Sub
```

**Salida**

```text
Cuadro de mensaje:  Segmento Premium: 3 campañas

B2 = 3350
B3 = 50250
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `MostrarSegmento` muestra el texto exacto | 3 |
| `EscribirTotales` escribe los dos números en las celdas pedidas | 3 |
| `PrepararResumen` llama a los dos con `Call` y no repite su código | 3 |
| El módulo se llama `Campanas` y se exporta como `.bas` | 1 |

**Error que más se ve**

Copiar dentro de `PrepararResumen` el contenido de los otros dos en vez de llamarlos. Se delata en que hay tres `MsgBox` idénticos en el módulo.

### 02.3 · Integrar

**Solución**

```vba
Sub OcultarCostoUnitario()
    Columns("D:D").EntireColumn.Hidden = True
    MsgBox "Columna de costo oculta"
End Sub

Sub MostrarCostoUnitario()
    Columns("D:D").EntireColumn.Hidden = False
    MsgBox "Columna de costo visible"
End Sub

Sub RevisarCatalogo()
    Call OcultarCostoUnitario
    Range("F1").Value = "Revisado"
End Sub
```

La traza, empezando con la columna D visible y F1 vacía:

| F8 | Renglón resaltado | La columna D | F1 |
|---|---|---|---|
| paso 1 | `Sub RevisarCatalogo()` | visible | vacía |
| paso 2 | `Call OcultarCostoUnitario` | visible | vacía |
| paso 3 | `Sub OcultarCostoUnitario()` | visible | vacía |
| paso 4 | `Columns("D:D")… = True` | visible | vacía |
| paso 5 | `MsgBox "Columna de costo oculta"` | oculta | vacía |
| paso 6 | `End Sub` de `OcultarCostoUnitario` | oculta | vacía |
| paso 7 | `Range("F1").Value = "Revisado"` | oculta | vacía |
| paso 8 | `End Sub` de `RevisarCatalogo` | oculta | Revisado |

**Salida**

```text
Al terminar:  columna D oculta, F1 = Revisado
Dos cuadros de mensaje en total: uno, el de OcultarCostoUnitario
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres procedimientos corren y hacen lo que su nombre dice | 3 |
| `RevisarCatalogo` usa `Call` y escribe en F1 | 2 |
| La traza respeta que el resaltado es el renglón pendiente | 3 |
| La traza muestra que F8 entra al procedimiento llamado | 2 |

**Error que más se ve**

Trazar como si `Call` fuera un solo paso y F8 no entrara al procedimiento llamado. Se delata en trazas de cuatro renglones que saltan del `Call` al `End Sub`.

---

## Semana 03 · Unidad 1 · Tipos, variables y celdas

### 03.1 · Reconocer

**Solución**

En (a), C2 queda en 14. VBA redondea al par más cercano al guardar un decimal en un `Integer`, así que 14.5 baja a 14 y 15.5 subiría a 16.

En (b), se detiene `folioFinal = 41020`, con error 6, `Overflow`. `Dim folioInicial, folioFinal As Integer` declara `As Integer` solo a la última: `folioInicial` quedó `Variant` y por eso acepta el mismo número sin quejarse.

En (c), el mensaje muestra 420. Sin `Option Explicit`, VBA crea `unidaes` al vuelo, le pone 75 y deja `unidades` en 420. Con `Option Explicit` en el primer renglón del módulo, el proyecto ya no compila y el editor señala `unidaes` como variable no definida.

**Salida**

```text
(a)  C2 = 14
(b)  folioInicial = 41020
     folioFinal    -> Run-time error '6': Overflow
(c)  Cuadro de mensaje: 420
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| (a) contesta 14 y nombra el redondeo al par | 3 |
| (b) señala `folioFinal` y el error 6, y explica el `Variant` | 4 |
| (c) contesta 420 y dice qué cambia con `Option Explicit` | 3 |

**Error que más se ve**

Contestar 15 en (a) por el redondeo de la escuela. Se delata en que el mismo alumno contesta 4 para 3.5, que sí coincide, y no nota que la regla es otra.

### 03.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub FichaProveedor()
    Dim clave As String
    Dim proveedor As String
    Dim rfc As String
    Dim existencias As Long
    Dim costoUnitario As Double
    Dim activo As Boolean
    Dim valorInventario As Double

    clave = "P-101"
    proveedor = "Empaques Lira"
    rfc = "ELI980312QX4"
    existencias = 180
    costoUnitario = 64.5
    activo = True
    valorInventario = existencias * costoUnitario

    Range("A1").Value = clave
    Range("A1").Offset(0, 1).Value = proveedor
    Range("A1").Offset(0, 2).Value = rfc
    Range("A1").Offset(0, 3).Value = existencias
    Range("A1").Offset(0, 4).Value = costoUnitario
    Range("A1").Offset(0, 5).Value = activo
    Range("A1").Offset(0, 6).Value = valorInventario
End Sub
```

**Salida**

```text
A1 = P-101
B1 = Empaques Lira
C1 = ELI980312QX4
D1 = 180
E1 = 64.5
F1 = VERDADERO
G1 = 11610
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Cada campo con el tipo correcto y ningún `Variant` | 4 |
| El RFC declarado como `String` | 2 |
| Usa `Offset` desde A1 para los seis campos siguientes | 2 |
| G1 con el valor del inventario, 11,610 | 2 |

**Error que más se ve**

Declarar el RFC como `Long` porque trae dígitos. Truena al asignarlo, y el que lo declara `Double` obtiene un número que ya no se puede comparar con el del sistema.

### 03.3 · Integrar

**Solución**

```vba
Option Explicit

Sub ValorInventario()
    Dim existencias As Long
    Dim costoUnitario As Double
    Dim valor As Double

    existencias = Range("C2").Value
    costoUnitario = Range("D2").Value
    valor = existencias * costoUnitario

    Range("E2").Value = valor
    MsgBox valor

    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

**Salida**

```text
E2 = 77700
Cuadro de mensaje: 77700
Columna D: oculta
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `Option Explicit` en el primer renglón del módulo | 1 |
| Lee C2 y D2 en variables con su tipo | 3 |
| E2 queda en 77,700 | 3 |
| Muestra el mensaje y oculta la columna D | 2 |
| Corre desde el cuadro de macros | 1 |

**Error que más se ve**

Escribir `Range("E2").Value = Range("C2").Value * Range("D2").Value` y saltarse las variables. Corre y da el número correcto, pero el ejercicio evaluaba la declaración y ahí no hay nada que calificar.

---

## Semana 04 · Unidad 1 · Operaciones y nombres de rango

### 04.1 · Reconocer

**Solución**

| Celda | Expresión | Queda en |
|---|---|---|
| D2 | `250000 - 180000 / 12` | 235000 |
| D3 | `(250000 - 180000) / 12` | 5833.33333333333 |
| D4 | `100 \ 7` | 14 |
| D5 | `100 Mod 7` | 2 |
| D6 | `-3 ^ 2` | -9 |
| D7 | `7.5 \ 2` | 4 |

La que cambia de resultado según dónde se escriba es `-3 ^ 2`. En VBA da -9, porque el signo se aplica después de la potencia; como fórmula de celda, `=-3^2` da 9.

En el problema de empaque, D4 son las cajas completas que salen y D5 son las piezas que quedan sueltas.

**Salida**

```text
D2 = 235000
D3 = 5833.33333333333
D4 = 14
D5 = 2
D6 = -9
D7 = 4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis celdas correctas, un punto cada una | 6 |
| Identifica `-3 ^ 2` y da el 9 de la celda | 2 |
| Lee D4 y D5 como cajas y piezas sueltas | 2 |

**Error que más se ve**

Contestar 3.75 en D7. La diagonal invertida redondea los dos operandos a entero antes de dividir, así que la cuenta que hace es 8 entre 2.

### 04.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub TasaMensualEquivalente()
    Dim anual As Double
    Dim mensual As Double

    ThisWorkbook.Names.Add _
        Name:="InflacionAnual", RefersTo:="=Sheet1!$B$1"
    ThisWorkbook.Names.Add _
        Name:="InflacionMensual", RefersTo:="=Sheet1!$B$2"

    Range("InflacionAnual").Value = 0.065
    anual = Range("InflacionAnual").Value

    mensual = ((1 + anual) ^ (1 / 12)) - 1

    ' B2 guarda el número completo y solo cambia cómo se ve.
    ' B3 guarda texto ya formateado y ya no se puede seguir calculando con él.
    Range("InflacionMensual").Value = mensual
    Range("InflacionMensual").NumberFormat = "0.00%"

    Range("B3").Value = Format(mensual, "0.00%")
    Range("B4").Value = Round(mensual, 6)
End Sub
```

**Salida**

```text
B1  0.065
B2  valor 0.00526169427684775, se ve 0.53%
B3  texto "0.53%"
B4  0.005262
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos nombres creados con `Names.Add` y usados después | 3 |
| La fórmula de la potencia con los paréntesis correctos | 3 |
| B2 con `NumberFormat`, B3 con `Format` y B4 con `Round` | 3 |
| El comentario distingue número formateado de texto | 1 |

**Error que más se ve**

Escribir `1 + anual ^ 1 / 12`. Corre, devuelve un número y no es la tasa: la potencia se resuelve antes que la suma y la división, así que faltan los dos pares de paréntesis.

Nota de calificación: `RefersTo` lleva el nombre real de la hoja. En un Excel en español la primera hoja se llama `Hoja1`, no `Sheet1`, y `Names.Add` con el nombre equivocado deja el nombre apuntando a una referencia rota. Si el alumno entregó con `Hoja1`, está bien.

### 04.3 · Integrar

**Solución**

```vba
Option Explicit

Sub CalcularVariacion()
    Dim presupuestado As Double
    Dim ejercido As Double
    Dim variacion As Double
    Dim proporcion As Double

    ThisWorkbook.Names.Add Name:="PresupuestoTotal", RefersTo:="=Presupuesto!$B$6"
    ThisWorkbook.Names.Add Name:="RealTotal", RefersTo:="=Presupuesto!$C$6"
    ThisWorkbook.Names.Add Name:="VariacionTotal", RefersTo:="=Presupuesto!$D$6"
    ThisWorkbook.Names.Add Name:="VariacionPct", RefersTo:="=Presupuesto!$E$6"

    presupuestado = Range("PresupuestoTotal").Value
    ejercido = Range("RealTotal").Value

    variacion = ejercido - presupuestado
    proporcion = variacion / presupuestado

    Range("VariacionTotal").Value = variacion
    Range("VariacionTotal").NumberFormat = "$#,##0.00"

    Range("VariacionPct").Value = proporcion
    Range("VariacionPct").NumberFormat = "0.00%"
End Sub
```

**Salida**

```text
D6  valor 64600.5,              se ve $64,600.50
E6  valor 0.0206062200956938,   se ve 2.06%
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro nombres creados y apuntando a las celdas correctas | 3 |
| La variación en pesos, 64,600.50 | 2 |
| La proporción sobre el presupuesto, 2.06 % | 2 |
| Los dos formatos aplicados | 2 |
| Después de crear los nombres no queda ninguna coordenada escrita | 1 |

**Error que más se ve**

Dividir la variación entre el real en vez de entre el presupuesto. Da 2.02 % y suena parecido, que es lo que lo hace difícil de ver en la revisión.

---

## Semana 05 · Unidad 1 · Captura y mensajes

### 05.1 · Reconocer

**Solución**

| Lo que teclean | IsNumeric | CDbl |
|---|---|---|
| 15 | True | 15 |
| 1,000 | True | 1000 |
| $780.50 | depende de la región, ver la nota | depende de la región, ver la nota |
| quince | False | error 13 |
| nada, presionó Cancelar | False | error 13 |

Con `quince`, la macro se detiene en el renglón del `If`, con error 13, `Type mismatch`. `And` no corta al primer falso: VBA evalúa los dos lados antes de aplicar el operador, así que `CDbl("quince")` corre aunque `IsNumeric` ya haya devuelto False.

**Salida**

```text
Run-time error '13':

Type mismatch
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco renglones de la tabla, un punto cada uno | 5 |
| Dice que se detiene en el renglón del `If` | 2 |
| Nombra el error 13 | 1 |
| Explica que `And` evalúa los dos lados | 2 |

**Error que más se ve**

Marcar `False` para `1,000`. La coma de millares sí pasa por `IsNumeric` y `CDbl` la convierte a 1000, y el alumno que la rechaza suele estar validando de más.

Nota de calificación: el renglón del símbolo de moneda depende de la configuración regional de la máquina, así que su punto se otorga con cualquiera de las dos respuestas siempre que el alumno diga en qué región la probó. `IsNumeric` acepta el símbolo de moneda de la región activa y rechaza cualquier otro. La lámina de la semana 5 dice `False` y error 13 porque se midió en un Excel con región del Reino Unido, donde el símbolo es la libra y el signo de pesos no cuenta como moneda. Medido en una máquina con región de México, que es la del aula: `IsNumeric("$780.50")` devuelve `True` y `CDbl("$780.50")` devuelve 780.5, mientras que con el símbolo de libra devuelve `False`. Lo que no se acepta es afirmar que ningún símbolo de moneda pasa nunca.

### 05.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub CapturarDias()
    Dim texto As String
    Dim dias As Double
    Dim valido As Boolean
    Dim respuesta As Long

    valido = False
    Do While Not valido
        texto = InputBox("Días trabajados de Ana Robles", "Nómina")

        ' Dos If anidados y no uno con And: en VBA los dos lados de And
        ' se evalúan siempre, así que CDbl correría sobre texto y truena.
        If IsNumeric(texto) Then
            If CDbl(texto) > 0 Then
                dias = CDbl(texto)
                valido = True
            End If
        End If

        If Not valido Then
            MsgBox "Eso no es un número de días válido.", vbExclamation
        End If
    Loop

    respuesta = MsgBox("¿Guardar " & dias & " días para Ana Robles?", _
                       vbYesNo + vbQuestion, "Confirmar")

    If respuesta = vbYes Then
        Range("C2").Value = dias
    End If
End Sub
```

**Salida**

```text
Teclea "quince"  ->  cuadro: Eso no es un número de días válido.  y vuelve a preguntar
Teclea "-3"      ->  cuadro: Eso no es un número de días válido.  y vuelve a preguntar
Teclea "15"      ->  cuadro: ¿Guardar 15 días para Ana Robles?
   Sí  ->  C2 = 15
   No  ->  C2 se queda como estaba
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El ciclo insiste hasta que el dato sirve | 3 |
| La validación va en dos `If` anidados | 2 |
| Rechaza el cero y los negativos, no solo el texto | 2 |
| La confirmación compara contra `vbYes` y solo entonces escribe | 2 |
| El comentario explica por qué no se usa `And` | 1 |

**Error que más se ve**

Comparar la respuesta contra el texto del botón, algo como `If respuesta = "Sí"`. Nunca entra al `If`, la macro no marca error y C2 se queda vacía.

### 05.3 · Integrar

**Solución**

```vba
Option Explicit

Sub CapturarRecibo()
    Dim texto As String
    Dim valido As Boolean
    Dim sueldo As Double
    Dim dias As Double
    Dim bruto As Double
    Dim bono As Double
    Dim total As Double

    ThisWorkbook.Names.Add Name:="SueldoDiario", RefersTo:="=Nomina!$B$2"
    ThisWorkbook.Names.Add Name:="DiasTrabajados", RefersTo:="=Nomina!$B$3"
    ThisWorkbook.Names.Add Name:="PagoBruto", RefersTo:="=Nomina!$B$4"
    ThisWorkbook.Names.Add Name:="Bono", RefersTo:="=Nomina!$B$5"
    ThisWorkbook.Names.Add Name:="PagoTotal", RefersTo:="=Nomina!$B$6"

    valido = False
    Do While Not valido
        texto = InputBox("Sueldo diario", "Recibo")
        If IsNumeric(texto) Then
            If CDbl(texto) > 0 Then
                sueldo = CDbl(texto)
                valido = True
            End If
        End If
        If Not valido Then
            MsgBox "El sueldo diario tiene que ser mayor que cero.", vbExclamation
        End If
    Loop

    valido = False
    Do While Not valido
        texto = InputBox("Días trabajados", "Recibo")
        If IsNumeric(texto) Then
            If CDbl(texto) > 0 Then
                dias = CDbl(texto)
                valido = True
            End If
        End If
        If Not valido Then
            MsgBox "Los días trabajados tienen que ser mayores que cero.", vbExclamation
        End If
    Loop

    bruto = sueldo * dias
    bono = bruto * 0.08
    total = bruto + bono

    Range("SueldoDiario").Value = sueldo
    Range("DiasTrabajados").Value = dias
    Range("PagoBruto").Value = bruto
    Range("Bono").Value = bono
    Range("PagoTotal").Value = total

    Range("PagoBruto").NumberFormat = "$#,##0.00"
    Range("Bono").NumberFormat = "$#,##0.00"
    Range("PagoTotal").NumberFormat = "$#,##0.00"

    MsgBox "Bruto: " & Format(bruto, "$#,##0.00") & vbNewLine & _
           "Bono: " & Format(bono, "$#,##0.00") & vbNewLine & _
           "Total: " & Format(total, "$#,##0.00"), _
           vbInformation, "Recibo"
End Sub
```

**Salida**

Con sueldo diario 780.50 y 15 días:

```text
B2 = 780.5
B3 = 15
B4 = 11707.5     se ve $11,707.50
B5 = 936.6       se ve $936.60
B6 = 12644.1     se ve $12,644.10

Cuadro de mensaje, título Recibo:
Bruto: $11,707.50
Bono: $936.60
Total: $12,644.10
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco nombres creados y usados para escribir | 2 |
| Las dos capturas validadas, cada una con su ciclo | 3 |
| Los tres importes correctos: 11,707.50, 936.60 y 12,644.10 | 3 |
| Formato de moneda en las tres celdas de importe | 1 |
| El mensaje final con los tres renglones separados por `vbNewLine` | 1 |

**Error que más se ve**

Calcular el total como `bruto * 1.08` y no escribir el bono por separado. Da el mismo total y deja B5 vacía, que es la celda que el área de nómina revisa.

Nota de calificación: `"$#,##0.00"` deja el signo de pesos sin comillas, así que Excel lo trata como marcador de moneda y usa el símbolo de la configuración regional de la máquina. En la del aula sale `$`. Si un alumno entrega el libro corrido en otra región y aparece otro símbolo, no es error suyo.

---

## Semana 06 · Unidad 2 · Editar lo grabado

### 06.1 · Reconocer

**Solución**

Quedan con formato ocho renglones, de D2 a D9. Los otros 32 no se tocan y la macro no marca ningún error: el rango que se grabó existe, nada más se quedó corto.

`Cells(Rows.Count, 1).End(xlUp).Row` devuelve 41, porque arranca desde el renglón 1,048,576 y sube hasta topar con dato. `Range("A1").CurrentRegion` devuelve `$A$1:$D$41`.

**Salida**

```text
Renglones formateados:  8 de 40
Error:                  ninguno
End(xlUp).Row:          41
CurrentRegion:          $A$1:$D$41
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Contesta 8 renglones formateados | 3 |
| Dice que no hay error | 2 |
| `End(xlUp).Row` devuelve 41 | 3 |
| `CurrentRegion` devuelve `$A$1:$D$41` | 2 |

**Error que más se ve**

Contestar 40 en `End(xlUp).Row`, olvidando que la fila 1 son los encabezados y que la propiedad devuelve el número de renglón, no la cuenta de datos.

### 06.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub FormatearImportes()
    Dim ultimaFila As Long
    Dim importes As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    Set importes = Range(Cells(2, 4), Cells(ultimaFila, 4))

    importes.NumberFormat = "$#,##0.00"
    Range("F1").Value = ultimaFila - 1
End Sub
```

**Salida**

Con la base de ocho renglones de datos:

```text
ultimaFila = 9
Rango armado: $D$2:$D$9
F1 = 8
```

Con la base de cuarenta renglones, el mismo código arma `$D$2:$D$41` y deja F1 en 40.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| No queda ningún `Select` ni `Selection` | 2 |
| La última fila se calcula con `End(xlUp)` sobre una variable `Long` | 3 |
| El rango se arma con `Range(Cells, Cells)` y se asigna con `Set` | 3 |
| F1 queda en 8, la cuenta sin encabezado | 2 |

**Error que más se ve**

Escribir `Set importes = Range(Cells(2, 4), Cells(ultimaFila, 4))` sin el `Set`. Se detiene con error 91 y el alumno cree que el problema está en `Cells`.

### 06.3 · Integrar

**Solución**

```vba
Option Explicit

Sub PrepararCatalogo()
    Dim ultimaFila As Long
    Dim costos As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    Set costos = Range(Cells(2, 4), Cells(ultimaFila, 4))
    costos.NumberFormat = "$#,##0.00"

    ThisWorkbook.Names.Add Name:="TotalRenglones", RefersTo:="=Proveedores!$G$1"
    Range("TotalRenglones").Value = ultimaFila - 1

    If Columns("E:E").EntireColumn.Hidden Then
        Columns("E:E").EntireColumn.Hidden = False
    Else
        Columns("E:E").EntireColumn.Hidden = True
    End If

    MsgBox "Rango de costos: " & costos.Address
End Sub
```

**Salida**

```text
ultimaFila = 6
G1 = 5
Cuadro de mensaje: Rango de costos: $D$2:$D$6

Primera corrida:  columna E oculta
Segunda corrida:  columna E visible
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El rango de costos se arma con `Cells` y recibe el formato | 3 |
| El nombre `TotalRenglones` se crea y queda en 5 | 2 |
| La columna E se alterna leyendo `Hidden`, y nunca se elimina | 3 |
| El mensaje muestra `$D$2:$D$6` con `Address` | 2 |

**Error que más se ve**

Usar `Delete` en vez de `Hidden` para la columna auxiliar. En la demostración se ve idéntico, y a la segunda corrida ya se llevó una columna de datos que nadie va a recuperar.

---

## Semana 07 · Unidad 2 · Búsqueda de objetivo y encadenamiento

### 07.1 · Reconocer

**Solución**

La celda que no puede traer fórmula es `PrecioUnitario`, la que va en `ChangingCell`. La búsqueda de objetivo escribe valores de prueba ahí, y no puede escribir encima de una fórmula.

La búsqueda llega a un precio unitario de 136.50. Despejado a mano: para que el margen sea 250,000 hace falta que `(precio - 84) * 12000` valga 630,000, o sea que el margen unitario sea 52.50 sobre un costo variable de 84.00.

Al terminar, B6 no queda en 250,000 exactos. La búsqueda tantea: prueba un valor, mide qué tan lejos quedó y corrige. Se detiene cuando la diferencia cabe en `Application.MaxChange`, que por omisión vale 0.001, o cuando agota `Application.MaxIterations`, que por omisión son 100 intentos.

Si `ChangingCell` apunta a `MargenTotal`, la macro se detiene con error 1004, porque esa celda contiene una fórmula.

**Salida**

```text
Antes:    PrecioUnitario 120.00     MargenTotal 52,000.00
Después:  PrecioUnitario 136.50     MargenTotal 250,000.00 con residuo

MaxChange      0.001
MaxIterations  100
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Señala `PrecioUnitario` y explica por qué no puede llevar fórmula | 3 |
| Llega a 136.50 | 3 |
| Dice que queda residuo y nombra `MaxChange` y `MaxIterations` | 2 |
| Reconoce el error 1004 del último caso | 2 |

**Error que más se ve**

Contestar que B6 queda en 250,000 exactos. Se delata en el siguiente ejercicio, cuando el alumno escribe una comparación contra cero o contra el objetivo y nunca se cumple.

### 07.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub CargarParametros()
    Range("PrecioUnitario").Value = 120
    Range("Unidades").Value = 12000
    Range("CostoVariable").Value = 84
    Range("CostosFijos").Value = 380000
End Sub

Sub FormatearModelo()
    Range("PrecioUnitario").NumberFormat = "$#,##0.00"
    Range("CostoVariable").NumberFormat = "$#,##0.00"
    Range("CostosFijos").NumberFormat = "$#,##0.00"
    Range("MargenTotal").NumberFormat = "$#,##0.00"
End Sub

Sub BuscarPrecio()
    Range("MargenTotal").GoalSeek _
        Goal:=250000, _
        ChangingCell:=Range("PrecioUnitario")
End Sub

Sub CerrarPrecio()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call CargarParametros
    Call FormatearModelo

    Application.Calculation = xlCalculationAutomatic

    Call BuscarPrecio

    Application.ScreenUpdating = True
End Sub
```

**Salida**

```text
Al terminar CerrarPrecio:
  PrecioUnitario   $136.50
  MargenTotal      $250,000.00
  Calculation      xlCalculationAutomatic (-4105)
  ScreenUpdating   True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres procedimientos corren solos desde el cuadro de macros | 3 |
| La maestra solo llama y no toca ninguna celda | 2 |
| Apaga y vuelve a prender pantalla y cálculo | 2 |
| El cálculo está en automático cuando corre la búsqueda | 3 |

**Error que más se ve**

Dejar el cálculo en manual durante la búsqueda de objetivo. La macro no marca error, pero la fórmula del margen no se vuelve a evaluar entre intento e intento, así que la búsqueda queda con el precio de arranque o con uno cualquiera.

### 07.3 · Integrar

**Solución**

```vba
Option Explicit

Function MargenTotalCalculado(precio As Double, unidades As Double, _
                              costoVar As Double, fijos As Double) As Double
    MargenTotalCalculado = (precio - costoVar) * unidades - fijos
End Function

Sub CompararMargen()
    Dim calculado As Double

    calculado = MargenTotalCalculado(Range("PrecioUnitario").Value, _
                                     Range("Unidades").Value, _
                                     Range("CostoVariable").Value, _
                                     Range("CostosFijos").Value)

    Range("B8").Value = calculado

    If calculado = Range("MargenTotal").Value Then
        Range("B9").Value = "Cuadra"
    Else
        Range("B9").Value = "Revisar"
    End If
End Sub
```

**Salida**

```text
Con el precio de arranque en 120:
  B6 = 52000     B8 = 52000     B9 = Cuadra

Después de CerrarPrecio:
  PrecioUnitario  136.5
  B6              250000 con residuo
  B6 - 250000     un número muy chico, distinto de cero
```

El residuo depende de la corrida. Este modelo es lineal, así que la búsqueda converge en pocos intentos y la diferencia suele quedar del orden de una milmillonésima o menos. Se califica que el alumno reporte el número que le salió, no que coincida con uno fijo. Reportar un cero redondo se toma como que no lo midió.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función declara el tipo de lo que devuelve y asigna su propio nombre | 3 |
| Con 120, 12000, 84 y 380000 devuelve 52,000 | 2 |
| `CompararMargen` escribe B8 y decide entre Cuadra y Revisar | 2 |
| Reporta el precio encontrado y el valor de B6 | 2 |
| Reporta la diferencia sin redondearla a cero | 1 |

**Error que más se ve**

Escribir la función sin asignarle su propio nombre. No marca error, devuelve cero, y B9 dice Revisar cuando el modelo está bien. El alumno busca el problema en la hoja.

---

## Semana 08 · Unidad 3 · Decisiones y primer parcial

### 08.1 · Reconocer

**Solución**

| Comparación | Devuelve | Por qué |
|---|---|---|
| `"Norte" = "norte"` | False | VBA compara texto respetando mayúsculas |
| `"10" < "9"` | True | Como texto, el 1 va antes que el 9 |
| `10 < 9` | False | Como números, nueve es menor |
| `CInt(True)` | -1 | Verdadero vale menos uno, no uno |
| `Range("A1").Value = 0` | True | Una celda vacía es igual a cero |
| `Range("A1").Value = ""` | True | Y también es igual a cadena vacía |
| `Range("A1").Value > 0` | False | Vacía no es mayor que cero |

Agrupando por el texto tal como está capturado, Excel reporta tres regiones distintas para el norte: Norte, norte y NORTE.

Para distinguir una venta sin importe de una venta de cero pesos, la comparación que no sirve es `= 0`, porque la celda vacía también devuelve True. Ninguna de las tres distingue el caso: hace falta `IsEmpty`, que llega la semana que entra.

**Salida**

```text
"Norte" = "norte"      False
"10" < "9"             True
10 < 9                 False
CInt(True)             -1
A1 vacía = 0           True
A1 vacía = ""          True
A1 vacía > 0           False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete comparaciones, un punto cada una | 7 |
| Contesta tres regiones para el norte | 1 |
| Señala que `= 0` no distingue la celda vacía | 2 |

**Error que más se ve**

Contestar 1 en `CInt(True)`. Lleva a escribir sumas de banderas que salen negativas, y el alumno revisa la suma en vez de la conversión.

### 08.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub ClasificarConIf()
    Dim importe As Double
    Dim nivel As String

    importe = Range("D2").Value

    If importe >= 150000 Then
        nivel = "A"
    ElseIf importe >= 100000 Then
        nivel = "B"
    ElseIf importe >= 50000 Then
        nivel = "C"
    Else
        nivel = "D"
    End If

    Range("E2").Value = nivel
End Sub

Sub ClasificarConCase()
    Dim importe As Double
    Dim nivel As String

    importe = Range("D2").Value

    ' Con Is, cada caso es un piso y todo lo de arriba ya se atrapó antes.
    ' Con To habría que escribir el techo de cada tramo, y un importe
    ' entre dos techos, como 149,999.50, se caería al Else sin nivel.
    Select Case importe
        Case Is >= 150000
            nivel = "A"
        Case Is >= 100000
            nivel = "B"
        Case Is >= 50000
            nivel = "C"
        Case Else
            nivel = "D"
    End Select

    Range("E2").Value = nivel
End Sub
```

**Salida**

```text
D2 = 210500   ->  E2 = A
D2 = 128400   ->  E2 = B
D2 =  65900   ->  E2 = C
D2 =  41200   ->  E2 = D
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La cadena de `If` va de la condición más exigente a la más floja | 3 |
| El `Select Case` da lo mismo para los cuatro importes | 3 |
| Ningún importe queda sin nivel | 2 |
| El comentario explica por qué `Is` y no `To` | 2 |

**Error que más se ve**

Escribir la cadena al revés, empezando por `>= 50000`. Corre sin error y clasifica todo como C, porque la primera condición verdadera es la que gana.

### 08.3 · Integrar

**Solución**

```vba
Option Explicit

Sub RevisarCuenta()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call CapturarImporte
    Call MedirBase
    Call ClasificarImporte

    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
End Sub

Sub CapturarImporte()
    Dim texto As String
    Dim valido As Boolean

    ThisWorkbook.Names.Add Name:="ImporteRevisado", RefersTo:="=Ventas!$G$2"

    valido = False
    Do While Not valido
        texto = InputBox("Importe a revisar", "Ventas")
        If IsNumeric(texto) Then
            If CDbl(texto) > 0 Then
                Range("ImporteRevisado").Value = CDbl(texto)
                valido = True
            End If
        End If
        If Not valido Then
            MsgBox "Eso no es un importe válido.", vbExclamation
        End If
    Loop
End Sub

Sub MedirBase()
    Dim ultimaFila As Long
    Dim importes As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    Set importes = Range(Cells(2, 4), Cells(ultimaFila, 4))
    importes.NumberFormat = "$#,##0.00"

    ThisWorkbook.Names.Add Name:="TotalRenglones", RefersTo:="=Ventas!$G$1"
    Range("TotalRenglones").Value = ultimaFila - 1
End Sub

Sub ClasificarImporte()
    Dim importe As Double
    Dim nivel As String

    ThisWorkbook.Names.Add Name:="NivelRevisado", RefersTo:="=Ventas!$G$3"

    importe = Range("ImporteRevisado").Value

    Select Case importe
        Case Is >= 150000
            nivel = "A"
        Case Is >= 100000
            nivel = "B"
        Case Is >= 50000
            nivel = "C"
        Case Else
            nivel = "D"
    End Select

    Range("NivelRevisado").Value = nivel
    Range("ImporteRevisado").NumberFormat = "$#,##0.00"
End Sub
```

De qué semana viene cada pieza:

| Procedimiento | Semana | Qué se evalúa de ahí |
|---|---|---|
| `CapturarImporte` | 5 | `InputBox`, `IsNumeric` y el ciclo que insiste |
| `MedirBase` | 6 | Rango variable con `End(xlUp)` y `Cells` |
| `ClasificarImporte` | 8 | `Select Case` sobre la tabla de niveles |
| `RevisarCuenta` | 7 | Automatización acotada y encadenamiento con `Call` |

**Salida**

Capturando 128400 sobre la base de ocho renglones:

```text
G1 = 8
G2 = 128400      se ve $128,400.00
G3 = B
Columna D con formato de moneda de D2 a D9
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La maestra acota y restaura pantalla y cálculo | 2 |
| La captura valida y no deja pasar texto ni cero | 2 |
| El rango se calcula, no se escribe, y G1 queda en 8 | 2 |
| La clasificación usa `Select Case` y G3 queda en B | 2 |
| Los tres nombres de rango creados y usados | 1 |
| La tabla asigna cada procedimiento a su semana | 1 |

**Error que más se ve**

Escribir `Range("G3").Value = nivel` dentro de `ClasificarImporte` en vez de usar el nombre. Funciona, y es exactamente la restricción que el enunciado ponía a prueba.

---

## Semana 09 · Unidad 3 · Repetición

### 09.1 · Reconocer

**Solución**

En (a) el mensaje dice `Periodos: 10 7 4 1 `, con un espacio al final. `Step -3` baja de tres en tres y se detiene en 1, porque el siguiente valor sería -2 y ya pasó del límite.

En (b) el recorrido entrega `$A$1 $B$1 $A$2 $B$2 `. `For Each` sobre un rango va a lo ancho y luego hacia abajo: termina cada renglón antes de bajar.

En (c) quedan tres de las seis campañas. Al borrar la fila 2, la 3 sube a ser la 2 y el contador ya va en 3, así que se salta una de cada dos. Con `For fila = 7 To 2 Step -1` no queda ninguna: borrar hacia atrás mueve renglones por los que el ciclo ya pasó.

**Salida**

```text
(a)  Periodos: 10 7 4 1
(b)  $A$1 $B$1 $A$2 $B$2
(c)  hacia adelante:  3 de 6
     hacia atrás:     0 de 6
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El texto de (a), incluido el orden descendente | 3 |
| El orden de (b), a lo ancho y luego hacia abajo | 3 |
| (c) contesta 3 de 6 y explica el corrimiento | 2 |
| (c) contesta 0 de 6 al recorrer al revés | 2 |

**Error que más se ve**

Contestar en (b) el orden por columnas, `$A$1 $A$2 $B$1 $B$2`. Se delata cuando el alumno usa `For Each` para leer una base y arma los renglones cruzados.

### 09.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub MarcarVencidos()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim marcadas As Long
    Dim importeVencido As Double

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        If Cells(fila, 4).Value > 30 Then
            Cells(fila, 5).Value = "Vencido"
            marcadas = marcadas + 1
            importeVencido = importeVencido + Cells(fila, 3).Value
        End If
    Next fila

    Range("G1").Value = marcadas
    Range("G2").Value = importeVencido
    Range("G2").NumberFormat = "$#,##0.00"
End Sub
```

**Salida**

```text
E3 = Vencido      (F-2202, 45 días)
E5 = Vencido      (F-2204, 61 días)
E7 = Vencido      (F-2206, 38 días)

G1 = 3
G2 = 69730        se ve $69,730.00
```

La factura F-2205, con exactamente 30 días, no se marca.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La última fila se calcula y el ciclo arranca en 2 | 3 |
| Las tres facturas marcadas son las correctas | 3 |
| G1 queda en 3 | 2 |
| G2 queda en 69,730.00 con formato de moneda | 2 |

**Error que más se ve**

Usar `>= 30` y marcar cuatro facturas. El enunciado decía que 30 exactos no se marcan, y la F-2205 mete 21,930.00 de cartera vencida que no lo está.

### 09.3 · Integrar

**Solución**

```vba
Option Explicit

Sub DepurarCampanas()
    Application.ScreenUpdating = False

    Call ClasificarCampanas
    Call DepurarSinDato

    Application.ScreenUpdating = True
End Sub

Sub ClasificarCampanas()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim masivas As Long
    Dim focalizadas As Long
    Dim sinDato As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        If IsEmpty(Cells(fila, 3).Value) Then
            Cells(fila, 5).Value = "Sin dato"
            sinDato = sinDato + 1
        ElseIf Cells(fila, 3).Value >= 3000 Then
            Cells(fila, 5).Value = "Masiva"
            masivas = masivas + 1
        Else
            Cells(fila, 5).Value = "Focalizada"
            focalizadas = focalizadas + 1
        End If
    Next fila

    Range("G1").Value = masivas
    Range("G2").Value = focalizadas
    Range("G3").Value = sinDato
End Sub

Sub DepurarSinDato()
    Dim ultimaFila As Long
    Dim fila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = ultimaFila To 2 Step -1
        If Cells(fila, 5).Value = "Sin dato" Then
            Rows(fila).Delete
        End If
    Next fila
End Sub
```

**Salida**

```text
Después de ClasificarCampanas:
  E2 Focalizada   E3 Masiva   E4 Sin dato
  E5 Masiva       E6 Sin dato E7 Masiva

  G1 = 3    masivas
  G2 = 1    focalizadas
  G3 = 2    sin dato

Después de DepurarSinDato:
  Quedan 4 renglones de datos: C-01, C-02, C-04 y C-06
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `IsEmpty` distingue la celda vacía, y va antes que la comparación | 3 |
| Las seis clasificaciones correctas | 2 |
| Los tres contadores en 3, 1 y 2 | 2 |
| El borrado recorre de abajo hacia arriba | 2 |
| Quedan cuatro renglones de datos | 1 |

**Error que más se ve**

Preguntar `If Cells(fila, 3).Value = 0` en vez de `IsEmpty`. Las dos campañas sin dato se clasifican como focalizadas, los contadores salen 3, 3 y 0, y no se borra nada.

---

## Semana 10 · Unidades 1 y 3 · Procedimientos y funciones

### 10.1 · Reconocer

**Solución**

B2 queda en 12644.1. El parámetro de `AplicarBono` se declaró `monto As Double`, sin escribir `ByVal`, y en VBA lo que no se declara va por referencia: el procedimiento le multiplicó por 1.08 a la variable de quien lo llamó.

B3 queda en 0. `TotalRecibo` nunca le asigna nada a su propio nombre, así que devuelve el valor por omisión de un `Double`. No marca error, y el cálculo sigue con ese cero.

La palabra que arregla lo primero es `ByVal`, en `Sub AplicarBono(ByVal monto As Double)`. El renglón que falta para lo segundo es `TotalRecibo = bruto + bono`.

**Salida**

```text
B2 = 12644.1
B3 = 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| B2 en 12,644.10 y nombra el paso por referencia | 3 |
| B3 en cero y explica que la función no asigna su nombre | 3 |
| Propone `ByVal` como la palabra que falta | 2 |
| Escribe el renglón de asignación que falta | 2 |

**Error que más se ve**

Contestar que B3 marca error. Es lo que uno esperaría, y es justo lo que no pasa: el silencio es lo caro del caso.

### 10.2 · Aplicar

**Solución**

```vba
Option Explicit

Function ComisionVenta(ByVal monto As Double) As Double
    If monto >= 150000 Then
        ComisionVenta = monto * 0.06
    ElseIf monto >= 100000 Then
        ComisionVenta = monto * 0.04
    ElseIf monto >= 50000 Then
        ComisionVenta = monto * 0.025
    Else
        ComisionVenta = 0
    End If
End Function
```

En la hoja, E2 lleva `=ComisionVenta(D2)` y se copia hasta E9. En E10 va `=SUM(E2:E9)`.

**Salida**

```text
V-1001   128,400.00   4.0 %    5,136.00
V-1002    96,750.00   2.5 %    2,418.75
V-1003   143,200.00   4.0 %    5,728.00
V-1004    87,300.00   2.5 %    2,182.50
V-1005   210,500.00   6.0 %   12,630.00
V-1006    65,900.00   2.5 %    1,647.50
V-1007    54,120.00   2.5 %    1,353.00
V-1008   181,045.00   6.0 %   10,862.70

Total de comisiones            41,958.45
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función declara `As Double` de salida y asigna su nombre en las cuatro ramas | 3 |
| El parámetro va `ByVal` | 1 |
| Las ocho comisiones correctas | 4 |
| El total en 41,958.45 | 1 |
| La función se usa desde la celda, no desde una macro | 1 |

**Error que más se ve**

Escribir la función como `Sub`. No aparece error hasta que se teclea en la celda, y ahí Excel devuelve `#¿NOMBRE?`, que el alumno lee como que se escribió mal el nombre.

### 10.3 · Integrar

**Solución**

```vba
Option Explicit

Function PagoTotal(ByVal dias As Double, ByVal sueldo As Double, _
                   ByVal bonoPct As Double) As Double
    Dim bruto As Double

    bruto = dias * sueldo
    PagoTotal = bruto + bruto * bonoPct
End Function

Sub CalcularPagos()
    Dim ultimaFila As Long
    Dim fila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        Cells(fila, 6).Value = PagoTotal(Cells(fila, 3).Value, _
                                         Cells(fila, 4).Value, _
                                         Cells(fila, 5).Value)
        Cells(fila, 6).NumberFormat = "$#,##0.00"
    Next fila
End Sub

Sub MarcarIncompletos()
    Dim ultimaFila As Long
    Dim fila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        If Cells(fila, 3).Value < 15 Then
            Cells(fila, 7).Value = "Revisar"
        End If
    Next fila
End Sub

Sub TotalizarNomina()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim total As Double

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        total = total + Cells(fila, 6).Value
    Next fila

    Cells(ultimaFila + 1, 6).Value = total
    Cells(ultimaFila + 1, 6).NumberFormat = "$#,##0.00"
End Sub

Sub ProcesarNomina()
    Application.ScreenUpdating = False

    Call CalcularPagos
    Call MarcarIncompletos
    Call TotalizarNomina

    Application.ScreenUpdating = True
End Sub
```

**Salida**

```text
F2 = 12644.1     $12,644.10    Ana Robles
F3 =  9639       $9,639.00     Beto Lira
F4 = 13513.5     $13,513.50    Carla Méndez
F5 =  7926       $7,926.00     Darío Sáenz
F6 = 43722.6     $43,722.60    total

G4 = Revisar     (Carla Méndez, 13 días)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función recibe los tres parámetros `ByVal` y devuelve `Double` | 2 |
| `CalcularPagos` no calcula nada por su cuenta, solo llama a la función | 2 |
| Los cuatro pagos correctos | 2 |
| El total en 43,722.60, en el renglón que sigue al último dato | 2 |
| Solo Carla Méndez queda marcada como Revisar | 1 |
| Cada procedimiento corre solo desde el cuadro de macros | 1 |

**Error que más se ve**

Meter el cálculo del bono dentro de `CalcularPagos` y dejar la función sin usar. La entrega corre y da los mismos números, y no hay nada que se pueda probar por separado, que era el punto de la sesión.

---

## Semana 11 · Unidades 2 y 3 · Eventos

### 11.1 · Reconocer

**Solución**

En (a) no pasa nada. El código compila, el nombre es el correcto, y Excel busca los manejadores de hoja solo en el módulo de esa hoja. En un módulo estándar queda como un procedimiento que nadie llama. No hay mensaje, no hay error y no hay aviso de que quedó huérfano. Además es `Private`, así que tampoco aparece en el cuadro de macros.

En (b), escribir 15 en B2 dispara el manejador, que escribe en C2. Escribir en C2 también es un cambio, así que Excel vuelve a llamar al manejador, que escribe en D2, y así. Nada lo detiene: Excel deja de responder y el proceso termina solo.

En (c), con la guarda puesta sobre B2 y `IsNumeric` decidiendo qué escribir:

| Lo que se teclea en B2 | `IsNumeric` sobre ese texto | `IsNumeric(Target.Value)` | Qué se escribe en C2 |
|---|---|---|---|
| 15 | True | True | Número |
| 12.5 | True | True | Número |
| $780.50 | True en región de México | True | Número |
| 15% | False | True | Número |
| quince | False | False | No es número |

Los dos renglones donde las columnas difieren son `15%` y, según la región, `$780.50`. La razón es la misma en los dos: cuando el manejador se dispara, Excel ya interpretó lo capturado y lo guardó como número. `15%` queda en la celda como 0.15 con formato de porcentaje, y `$780.50` como 780.5 con formato de moneda. `Target.Value` entrega esos números, no el texto, así que `IsNumeric` dice True aunque la cadena original no fuera numérica. Solo `quince` se queda como texto y es el único que llega a `No es número`.

**Salida**

```text
(a)  no ocurre nada, y Excel no avisa
(b)  Excel deja de responder y el proceso termina
(c)  cuatro veces Número y una sola vez No es número
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| (a) dice que no pasa nada y explica dónde busca Excel el manejador | 3 |
| (b) describe la cadena de escrituras que se redisparan | 2 |
| La columna de `IsNumeric(Target.Value)` y la columna de C2 | 3 |
| Señala que `15%` es el renglón donde las dos columnas difieren | 2 |

**Error que más se ve**

Contestar `No es número` para `15%`, copiando la tabla de la lámina de la semana 11 sin notar que ahí se mide `IsNumeric` sobre una cadena y aquí sobre `Target.Value`. Se delata en que el alumno entrega la columna del texto llenada dos veces.

Nota de calificación: la lámina de la semana 11 lista `$5`, `5%` y `2026-01-01` como `False`, y eso es cierto de `IsNumeric` aplicado a esas cadenas, no de la celda ya capturada. Medido con Excel 16.0 en región de México, escribir esos tres valores en una celda deja `Target.Value` en 5, 0.15 y 46023, los tres numéricos. El renglón de `$780.50` además depende de la región en la columna del texto: `IsNumeric` acepta el símbolo de moneda de la región activa, así que en México devuelve `True` y en el Reino Unido, donde el símbolo es la libra, devuelve `False`. Se acepta la respuesta de la lámina si el alumno explica sobre qué se está preguntando.

### 11.2 · Aplicar

**Solución**

En el módulo de la hoja `Nomina`:

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    ' La guarda basta porque el manejador escribe en H2 y nunca en C2.
    ' Si también escribiera en C2, esa escritura entraría por la guarda
    ' y se volvería a llamar a sí mismo: ahí haría falta EnableEvents.
    If Target.Address <> "$C$2" Then Exit Sub

    If IsNumeric(Target.Value) Then
        Range("H2").Value = "Días válidos"
        Target.NumberFormat = "0"
    Else
        Range("H2").Value = "Revisar captura"
        Target.Interior.Color = RGB(255, 235, 156)
    End If
End Sub
```

**Salida**

```text
Se teclea 15 en C2       ->  H2 = Días válidos,     C2 con formato 0
Se teclea quince en C2   ->  H2 = Revisar captura,  C2 en amarillo
Se teclea algo en D2     ->  no pasa nada
Veinte capturas seguidas ->  Excel sigue respondiendo
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El manejador está en el módulo de la hoja, no en uno estándar | 2 |
| La guarda deja pasar solo el cambio de C2 | 3 |
| Los dos textos de H2 según `IsNumeric` | 2 |
| El formato y el relleno amarillo aplicados a C2 | 2 |
| El comentario explica el límite de la guarda | 1 |

**Error que más se ve**

Poner el manejador en un módulo estándar. Compila, aparece en el árbol, y no se dispara nunca. Se delata en que el alumno reporta que su código no hace nada y no tiene ningún error que enseñar.

### 11.3 · Integrar

**Solución**

En `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    ThisWorkbook.Worksheets("Nomina").Activate
    ThisWorkbook.Worksheets("Nomina").Range("C2").Select
    MsgBox "Captura los días trabajados en C2"
End Sub
```

En el módulo de la hoja `Nomina`:

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    If Target.Address <> "$C$2" Then Exit Sub

    Application.EnableEvents = False

    If IsNumeric(Target.Value) Then
        If CDbl(Target.Value) > 0 Then
            Range("F2").Value = PagoTotal(CDbl(Target.Value), _
                                          Range("D2").Value, _
                                          Range("E2").Value)
            Range("F2").NumberFormat = "$#,##0.00"
            Range("G2").ClearContents
        Else
            Range("F2").ClearContents
            Range("G2").Value = "Revisar captura"
        End If
    Else
        Range("F2").ClearContents
        Range("G2").Value = "Revisar captura"
    End If

    Application.EnableEvents = True
End Sub
```

**Salida**

```text
Al abrir el libro:
  hoja Nomina activa, C2 seleccionada
  cuadro: Captura los días trabajados en C2

Se captura 15 en C2:
  F2 = 12644.1    se ve $12,644.10
  G2 vacía

Se captura quince en C2:
  F2 vacía
  G2 = Revisar captura
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `Workbook_Open` vive en `ThisWorkbook` y deja C2 seleccionada | 2 |
| El manejador de hoja reacciona solo a C2 | 2 |
| Reutiliza la función `PagoTotal` de la semana 10 en vez de recalcular | 2 |
| F2 queda en 12,644.10 al capturar 15 | 2 |
| Apaga y vuelve a prender los eventos alrededor de las escrituras | 2 |

**Error que más se ve**

Apagar los eventos y no volverlos a prender por salir del procedimiento en la rama del error. Excel se queda sin eventos hasta que se cierra, y el alumno reporta que el manejador dejó de funcionar sin razón.

---

## Semana 12 · Unidad 3 · Clases propias

### 12.1 · Reconocer

**Solución**

En (a) se imprime 13875. Solo hubo un `New`, así que solo existe un objeto: `Set b = a` no copia nada, deja dos nombres apuntando al mismo lugar. La última asignación de existencias es la de `b`, que puso 75, y el costo se quedó en 185. Para que fueran independientes hace falta un segundo `New`, es decir `Set b = New Proveedor`.

En (b) se detiene con error 91, `Object variable or With block variable not set`. `Dim` reserva el nombre y no crea nada; sin `Set p = New Proveedor`, la primera línea que use el objeto truena.

En (c) se imprime 0. La validación vive en `Property Let CostoUnitario`, así que el -185 nunca entra: el campo se queda en cero y el valor del inventario también.

**Salida**

```text
(a)  13875        objetos creados: 1
(b)  Error 91     Object variable or With block variable not set
(c)  0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| (a) contesta 13875 y explica que hay un solo objeto | 4 |
| (a) propone el segundo `New` para separarlos | 1 |
| (b) nombra el error 91 y la diferencia entre `Dim` y `Set` | 3 |
| (c) contesta cero y ubica la validación en `Let` | 2 |

**Error que más se ve**

Contestar 77700 en (a), leyendo las asignaciones como si `a` y `b` fueran cajas distintas. Es el mismo razonamiento que sirve para números y que deja de servir para objetos.

### 12.2 · Aplicar

**Solución**

Módulo de clase, nombrado `Proveedor` desde la ventana Propiedades:

```vba
Option Explicit

Private pClave As String
Private pExistencias As Long
Private pCostoUnitario As Double

Private Sub Class_Initialize()
    pClave = "sin clave"
    pExistencias = 0
    pCostoUnitario = 0
End Sub

Public Property Get Clave() As String
    Clave = pClave
End Property

Public Property Let Clave(valor As String)
    pClave = valor
End Property

Public Property Get Existencias() As Long
    Existencias = pExistencias
End Property

Public Property Let Existencias(valor As Long)
    If valor < 0 Then
        pExistencias = 0
    Else
        pExistencias = valor
    End If
End Property

Public Property Get CostoUnitario() As Double
    CostoUnitario = pCostoUnitario
End Property

Public Property Let CostoUnitario(valor As Double)
    If valor < 0 Then
        pCostoUnitario = 0
    Else
        pCostoUnitario = valor
    End If
End Property

Public Function Valor() As Double
    Valor = pExistencias * pCostoUnitario
End Function
```

Módulo estándar:

```vba
Option Explicit

Sub ProbarProveedor()
    Dim p As Proveedor
    Set p = New Proveedor

    Debug.Print p.Clave & " | " & p.Existencias & " | " & _
                p.CostoUnitario & " | " & p.Valor

    p.Clave = "P-100"
    p.Existencias = 420
    p.CostoUnitario = 185
    Debug.Print p.Clave & " | " & p.Existencias & " | " & _
                p.CostoUnitario & " | " & p.Valor

    p.CostoUnitario = -50
    Debug.Print p.Clave & " | " & p.Existencias & " | " & _
                p.CostoUnitario & " | " & p.Valor
End Sub
```

**Salida**

Ventana Inmediato:

```text
sin clave | 0 | 0 | 0
P-100 | 420 | 185 | 77700
P-100 | 420 | 0 | 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El módulo de clase se llama `Proveedor`, no Clase1 | 1 |
| Tres campos privados y sus tres pares de `Get` y `Let` | 3 |
| La validación de negativos vive dentro de `Let` | 2 |
| `Valor` devuelve existencias por costo unitario | 2 |
| `Class_Initialize` deja el objeto usable sin asignarle nada | 2 |

**Error que más se ve**

Llamar al campo privado igual que la propiedad. La propiedad se llama a sí misma, entra en recursión y el programa se queda sin pila. Se delata en que el error aparece con la primera lectura y no con la escritura.

### 12.3 · Integrar

**Solución**

```vba
Option Explicit

Sub ValuarCatalogo()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim total As Double
    Dim prov As Proveedor

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    ThisWorkbook.Names.Add Name:="ValorTotal", RefersTo:="=Proveedores!$G$1"

    For fila = 2 To ultimaFila
        Set prov = New Proveedor

        prov.Clave = Cells(fila, 1).Value

        If IsEmpty(Cells(fila, 3).Value) Then
            Cells(fila, 6).Value = "Revisar"
        Else
            prov.Existencias = Cells(fila, 3).Value
        End If

        prov.CostoUnitario = Cells(fila, 4).Value

        Cells(fila, 5).Value = prov.Valor
        Cells(fila, 5).NumberFormat = "$#,##0.00"
        total = total + prov.Valor
    Next fila

    Range("ValorTotal").Value = total
    Range("ValorTotal").NumberFormat = "$#,##0.00"
End Sub
```

**Salida**

```text
E2 =  77700     $77,700.00     P-100
E3 =  11610     $11,610.00     P-101
E4 =  18000     $18,000.00     P-102
E5 =  16000     $16,000.00     P-103
E6 =  21930     $21,930.00     P-104

G1 = 145240     $145,240.00
```

Si se vacía C4, ese renglón queda en cero, F4 dice Revisar y el total baja a 127,240.00.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El `New` va dentro del ciclo, uno por renglón | 3 |
| El valor de cada renglón sale del objeto, no de una cuenta en la macro | 3 |
| El total en 145,240.00, en la celda con nombre | 2 |
| Un renglón con existencias vacías queda en cero y marcado | 2 |

**Error que más se ve**

Poner el `Set prov = New Proveedor` antes del ciclo. Corre y da el total correcto, porque el objeto se reusa y siempre se le sobreescriben los tres datos, pero deja de haber un objeto por renglón y a la primera propiedad que no se reasigne se arrastra el valor del anterior.

---

## Semana 13 · Unidad 4 · Limpiar y ordenar

### 13.1 · Reconocer

**Solución**

En (a) el `Trim` de VBA quita los espacios de las orillas y no toca los de en medio. El de la hoja, llamado con `WorksheetFunction`, además colapsa los de en medio a uno solo.

En (b), `Len(s)` y `Len(Trim(s))` valen los dos 5, y la comparación devuelve `False`. `Chr(160)` es un espacio duro y `Trim` no lo reconoce como espacio, así que sobrevive y hace que dos celdas que se ven idénticas no sean iguales.

En (c), el que no es el que quería el usuario es `Aceros Del Bajío`: `Proper` pone mayúscula en cada palabra, incluidos los artículos y las preposiciones.

En (d) quedan las cuatro filas, el encabezado y los tres datos. `Columns:=2` cuenta dentro del rango, así que apunta a la columna C, la de claves, y las tres son distintas. Para quitar los proveedores repetidos hay que pasar `Columns:=1`.

**Salida**

```text
(a)  [Aceros del Bajío]
     [Aceros    del Bajío]
     [Aceros del Bajío]

(b)  5    5
     False

(c)  Empaques Lira
     Aceros Del Bajío
     Papelera Central

(d)  4 filas, sin cambios
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| (a) distingue el `Trim` de VBA del de la hoja | 3 |
| (b) contesta 5 y 5, y False, y nombra el espacio duro | 3 |
| (c) señala `Aceros Del Bajío` | 2 |
| (d) contesta cuatro filas y propone `Columns:=1` | 2 |

**Error que más se ve**

Contestar 5 y 4 en (b), suponiendo que `Trim` quita el espacio duro porque en pantalla se ve igual que un espacio. Es exactamente la suposición que deja la base sucia.

### 13.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub LimpiarProveedores()
    Dim ultimaFila As Long
    Dim celda As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For Each celda In Range(Cells(2, 1), Cells(ultimaFila, 1))
        ' El orden importa: si Trim va primero, el espacio duro sigue
        ' ahí y ni él ni Proper lo tocan. Primero se traduce a espacio
        ' normal, después se colapsa y al final se emparejan mayúsculas.
        celda.Value = Replace(celda.Value, Chr(160), " ")
        celda.Value = WorksheetFunction.Trim(celda.Value)
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub
```

**Salida**

```text
A2 = Aceros Del Bajío
A3 = Empaques Lira
A4 = Papelera Central
A5 = Comercial Sáenz
```

`Proper` deja `Del` con mayúscula. Es el resultado correcto de la función y no del negocio: si el catálogo lo exige en minúscula, hay que corregirlo después con `Replace`.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La última fila se calcula y el rango se arma con `Cells` | 2 |
| El espacio duro se reemplaza antes de recortar | 3 |
| Usa el `Trim` de la hoja, no el de VBA | 2 |
| `Proper` empareja las mayúsculas de los cuatro | 2 |
| El comentario explica el orden | 1 |

**Error que más se ve**

Usar el `Trim` de VBA. El renglón 3 se queda con sus cuatro espacios de en medio, la base se ve limpia y la tabla dinámica sigue reportando dos proveedores donde hay uno.

### 13.3 · Integrar

**Solución**

```vba
Option Explicit

Sub PrepararVentas()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim total As Double

    Application.ScreenUpdating = False

    Call EmparejarRegion
    Call BorrarVacias
    Call QuitarRepetidas
    Call OrdenarBase

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    For fila = 2 To ultimaFila
        total = total + Cells(fila, 4).Value
    Next fila

    Range("F1").Value = ultimaFila - 1
    Range("F2").Value = total
    Range("F2").NumberFormat = "$#,##0.00"

    Application.ScreenUpdating = True
End Sub

Sub EmparejarRegion()
    Dim ultimaFila As Long
    Dim celda As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For Each celda In Range(Cells(2, 2), Cells(ultimaFila, 2))
        If Not IsEmpty(celda.Value) Then
            celda.Value = WorksheetFunction.Proper( _
                WorksheetFunction.Trim(celda.Value))
        End If
    Next celda
End Sub

Sub BorrarVacias()
    Dim ultimaFila As Long
    Dim fila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = ultimaFila To 2 Step -1
        If WorksheetFunction.CountA(Rows(fila)) = 0 Then
            Rows(fila).Delete
        End If
    Next fila
End Sub

Sub QuitarRepetidas()
    Dim ultimaFila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(ultimaFila, 4)).RemoveDuplicates _
        Columns:=1, Header:=xlYes
End Sub

Sub OrdenarBase()
    Dim ultimaFila As Long

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(ultimaFila, 4)).Sort _
        Key1:=Range("B1"), Order1:=xlAscending, _
        Key2:=Range("D1"), Order2:=xlDescending, _
        Header:=xlYes
End Sub
```

**Salida**

```text
Base al terminar:

  A         B        C               D
2 V-1004    Centro   Darío Sáenz      87300.00
3 V-1003    Norte    Carla Méndez    143200.00
4 V-1001    Norte    Ana Robles      128400.00
5 V-1005    Sur      Ana Robles      210500.00
6 V-1002    Sur      Beto Lira        96750.00

F1 = 5
F2 = 666150      se ve $666,150.00
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las regiones quedan parejas: sur y NORTE se vuelven Sur y Norte | 2 |
| La fila vacía se borra recorriendo de abajo hacia arriba | 2 |
| El folio repetido se quita y sobrevive el primero | 2 |
| El orden por dos criterios sobre la base completa, con encabezado declarado | 2 |
| F1 en 5 y F2 en 666,150.00 | 1 |
| Cada renglón conserva su vendedor y su importe después de ordenar | 1 |

**Error que más se ve**

Ordenar pasando solo la columna del importe como rango. Los importes quedan ordenados, los nombres no se mueven, no aparece ningún error y todos los renglones dicen algo falso.

---

## Semana 14 · Unidad 4 · Filtros, subtotales y tablas

### 14.1 · Reconocer

**Solución**

| Cómo se suma | Devuelve |
|---|---|
| `For Each` sobre `D2:D9` | 967,215.00 |
| `For Each` sobre `D2:D9` con `SpecialCells(xlCellTypeVisible)` | 325,720.00 |
| `SUBTOTAL(9,D2:D9)` | 325,720.00 |
| `SUM(D2:D9)` | 967,215.00 |

Las dos que devuelven 967,215 son el ciclo plano y `SUM`. Filtrar es una decisión de la vista: las filas ocultas siguen en su lugar con su contenido intacto, y ni el ciclo ni `SUM` preguntan si están visibles.

Con el criterio encabezado como `Departamento` y la base encabezada como `Región`, el filtro avanzado no encuentra la columna, no empareja nada y esconde las ocho. Quedan cero renglones visibles y no aparece ningún mensaje de error.

**Salida**

```text
ciclo For Each .......  967,215.00
solo visibles ........  325,720.00
SUBTOTAL(9) ..........  325,720.00
SUM ..................  967,215.00

filtro avanzado con encabezado distinto:  0 de 8 visibles, sin error
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro totales, dos puntos cada uno | 8 |
| Contesta cero renglones visibles y ningún error en el filtro avanzado | 2 |

**Error que más se ve**

Suponer que `SUM` respeta el filtro porque en pantalla se ve el rango filtrado. La que lo respeta es `SUBTOTAL`, y por eso Excel la usa cuando el usuario aprieta Autosuma sobre una lista filtrada.

### 14.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub TotalRegionVisible()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim celda As Range
    Dim total As Double
    Dim visibles As Long

    Set ws = ThisWorkbook.Worksheets("Ventas")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    ws.Range(ws.Cells(1, 1), ws.Cells(ultimaFila, 4)).AutoFilter _
        Field:=2, Criteria1:=ws.Range("H1").Value

    For Each celda In ws.Range(ws.Cells(2, 4), ws.Cells(ultimaFila, 4)) _
            .SpecialCells(xlCellTypeVisible)
        total = total + celda.Value
        visibles = visibles + 1
    Next celda

    ws.Range("H2").Value = visibles
    ws.Range("H3").Value = total
    ws.Range("H3").NumberFormat = "$#,##0.00"
    ws.Range("H4").Formula = "=SUBTOTAL(9,D2:D" & ultimaFila & ")"
End Sub
```

**Salida**

```text
H1 = Norte    ->  H2 = 3   H3 = $325,720.00   H4 = 325720
H1 = Sur      ->  H2 = 2   H3 = $307,250.00   H4 = 307250
H1 = Bajío    ->  H2 = 1   H3 = $181,045.00   H4 = 181045
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El criterio se lee de H1 y no está escrito en el código | 2 |
| El filtro se aplica sobre la columna de región con rango variable | 2 |
| El total sale de `SpecialCells(xlCellTypeVisible)` | 3 |
| Los tres pares de números coinciden con `SUBTOTAL` | 3 |

**Error que más se ve**

Recorrer `D2:D9` sin pedir las celdas visibles y reportar 967,215 para las tres regiones. El número se ve razonable, y se delata en que no cambia al cambiar el criterio.

Nota de calificación: si el filtro deja cero renglones visibles, `SpecialCells` se detiene con error 1004 en vez de devolver un rango vacío. Atenderlo se ve en la semana 16; esta semana basta con que el alumno lo señale.

### 14.3 · Integrar

**Solución**

```vba
Option Explicit

Sub PrepararResumen()
    Application.ScreenUpdating = False

    Call ConvertirEnTabla
    If TablaTieneDatos Then Call ResumirPorRegion

    Application.ScreenUpdating = True
End Sub

Sub ConvertirEnTabla()
    Dim ws As Worksheet
    Dim tbl As ListObject

    Set ws = ThisWorkbook.Worksheets("Ventas")
    If ws.ListObjects.Count > 0 Then Exit Sub

    Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1").CurrentRegion, , xlYes)
    tbl.Name = "Ventas2026"
End Sub

Function TablaTieneDatos() As Boolean
    Dim tbl As ListObject

    Set tbl = ThisWorkbook.Worksheets("Ventas").ListObjects("Ventas2026")

    If tbl.DataBodyRange Is Nothing Then
        MsgBox "La tabla no tiene datos"
        TablaTieneDatos = False
    Else
        TablaTieneDatos = True
    End If
End Function

Sub ResumirPorRegion()
    Dim tbl As ListObject
    Dim wr As Worksheet
    Dim fila As Range
    Dim renglon As Long
    Dim cuenta As Long
    Dim suma As Double

    Set tbl = ThisWorkbook.Worksheets("Ventas").ListObjects("Ventas2026")
    Set wr = ThisWorkbook.Worksheets("Resumen")

    wr.Range("A1").Value = "Región"
    wr.Range("B1").Value = "Ventas"
    wr.Range("C1").Value = "Importe"
    wr.Range("A2").Value = "Bajío"
    wr.Range("A3").Value = "Centro"
    wr.Range("A4").Value = "Norte"
    wr.Range("A5").Value = "Sur"

    For renglon = 2 To 5
        cuenta = 0
        suma = 0

        For Each fila In tbl.DataBodyRange.Rows
            If fila.Cells(1, 2).Value = wr.Cells(renglon, 1).Value Then
                cuenta = cuenta + 1
                suma = suma + fila.Cells(1, 4).Value
            End If
        Next fila

        wr.Cells(renglon, 2).Value = cuenta
        wr.Cells(renglon, 3).Value = suma
        wr.Cells(renglon, 3).NumberFormat = "$#,##0.00"
    Next renglon
End Sub
```

**Salida**

```text
Hoja Resumen:

  Región    Ventas   Importe
  Bajío        1     $181,045.00
  Centro       2     $153,200.00
  Norte        3     $325,720.00
  Sur          2     $307,250.00
```

Al agregar dos ventas al final de la tabla, la tabla crece sola, `DataBodyRange` entrega ocho más dos renglones y el resumen las incluye sin haber tocado ninguna dirección del código.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La tabla se crea con el nombre pedido y correr dos veces no truena | 2 |
| `TablaTieneDatos` revisa `DataBodyRange Is Nothing` y devuelve `Boolean` | 3 |
| El resumen recorre el cuerpo de la tabla, no una dirección escrita | 2 |
| Los cuatro renglones del resumen correctos | 2 |
| Al agregar renglones el resumen los incluye sin tocar el código | 1 |

**Error que más se ve**

Revisar la tabla vacía con `If tbl.DataBodyRange.Rows.Count = 0`. La revisión misma se detiene con error 91, porque para preguntarle los renglones a `Nothing` primero hay que tener algo.

---

## Semana 15 · Unidades 4 y 5 · Reportes y R1C1

### 15.1 · Reconocer

**Solución**

En (a), el primer renglón se detiene con error 438, `Object doesn't support this property or method`: `Left` es de VBA y no aparece en `WorksheetFunction`. El segundo devuelve `Aceros`.

En (b), `WorksheetFunction.VLookup` se detiene con error 1004 cuando la clave no está. `Application.VLookup` no se detiene: devuelve el valor de error `#N/A` como valor, y por eso `IsError(v)` imprime `True`. El que permite seguir es el de `Application`.

En (c), al escribirlas las dos celdas muestran 30. Después de cambiar A1 a 100, C1 pasa a 120 porque la fórmula sigue viva en la celda, y D1 se queda en 30 porque ahí solo quedó el número que dio el cálculo en el momento de correr la macro.

En (d) imprime `=RC[-2]*RC[-1]`.

**Salida**

```text
(a)  Error 438  /  Aceros
(b)  Error 1004 /  True
(c)  al escribir:      C1 = 30    D1 = 30
     tras A1 = 100:    C1 = 120   D1 = 30
(d)  =RC[-2]*RC[-1]
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| (a) nombra el 438 y devuelve `Aceros` | 2 |
| (b) nombra el 1004 y dice que `Application` devuelve el error como valor | 3 |
| (c) los cuatro valores, antes y después | 3 |
| (d) la cadena exacta en R1C1 | 2 |

**Error que más se ve**

Escribir que `Application.VLookup` devuelve una cadena vacía. Devuelve un valor de error, y por eso hay que recibirlo en un `Variant` y preguntarle con `IsError`.

### 15.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub CompletarMovimientos()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim fila As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Movimientos")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultimaFila
        ' v tiene que ser Variant: un String no puede recibir un valor
        ' de error, y la asignación truena antes de poder revisarlo.
        v = Application.VLookup(ws.Cells(fila, 1).Value, _
                                Range("Catalogo"), 2, False)

        If IsError(v) Then
            ws.Cells(fila, 3).Value = "sin catálogo"
            ws.Range(ws.Cells(fila, 1), ws.Cells(fila, 3)) _
                .Interior.Color = RGB(255, 235, 156)
        Else
            ws.Cells(fila, 3).Value = v
        End If
    Next fila

    ws.Range("E1").Value = WorksheetFunction.SumIfs( _
        ws.Range(ws.Cells(2, 2), ws.Cells(ultimaFila, 2)), _
        ws.Range(ws.Cells(2, 3), ws.Cells(ultimaFila, 3)), _
        "Aceros del Bajío")
    ws.Range("E1").NumberFormat = "$#,##0.00"

    ws.Range("E2").Value = WorksheetFunction.CountIf( _
        ws.Range(ws.Cells(2, 3), ws.Cells(ultimaFila, 3)), _
        "Aceros del Bajío")
End Sub
```

**Salida**

```text
C2 = Aceros del Bajío
C3 = Empaques Lira
C4 = Aceros del Bajío
C5 = Papelera Central
C6 = sin catálogo          fila 6 en amarillo
C7 = Empaques Lira
C8 = Aceros del Bajío
C9 = Papelera Central

E1 = 65650      se ve $65,650.00
E2 = 3
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Usa `Application.VLookup` y no `WorksheetFunction.VLookup` | 3 |
| La variable que recibe la búsqueda es `Variant` y se revisa con `IsError` | 2 |
| La fila 6 queda marcada y la macro llega hasta la 9 | 2 |
| E1 en 65,650.00 y E2 en 3 | 2 |
| El comentario explica por qué no sirve un `String` | 1 |

**Error que más se ve**

Declarar la variable `As String`. La asignación del valor de error truena con el 13 antes de que `IsError` alcance a revisarla, así que la red se cae en el mismo renglón que debía protegerse.

### 15.3 · Integrar

**Solución**

```vba
Option Explicit

Sub ReporteCatalogo()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call LimpiarNombres
    Call CalcularValor

    ' Las fórmulas de la columna E tienen que estar evaluadas antes de
    ' que SumIfs las lea, así que aquí se devuelve el cálculo automático.
    Application.Calculation = xlCalculationAutomatic

    Call ResumirPorProveedor
    Call GraficarResumen

    Application.ScreenUpdating = True
End Sub

Sub LimpiarNombres()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim celda As Range

    Set ws = ThisWorkbook.Worksheets("Proveedores")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For Each celda In ws.Range(ws.Cells(2, 2), ws.Cells(ultimaFila, 2))
        celda.Value = Replace(celda.Value, Chr(160), " ")
        celda.Value = WorksheetFunction.Trim(celda.Value)
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub

Sub CalcularValor()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim valores As Range

    Set ws = ThisWorkbook.Worksheets("Proveedores")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    Set valores = ws.Range(ws.Cells(2, 5), ws.Cells(ultimaFila, 5))

    valores.FormulaR1C1 = "=RC[-2]*RC[-1]"
    valores.NumberFormat = "$#,##0.00"
End Sub

Sub ResumirPorProveedor()
    Dim ws As Worksheet
    Dim wr As Worksheet
    Dim ultimaFila As Long
    Dim renglon As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Proveedores")
    Set wr = ThisWorkbook.Worksheets("Resumen")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    wr.Range("A1").Value = "Proveedor"
    wr.Range("B1").Value = "Valor"
    wr.Range("C1").Value = "Giro"
    wr.Range("A2").Value = "Aceros Del Bajío"
    wr.Range("A3").Value = "Empaques Lira"
    wr.Range("A4").Value = "Papelera Central"

    For renglon = 2 To 4
        wr.Cells(renglon, 2).Value = WorksheetFunction.SumIfs( _
            ws.Range(ws.Cells(2, 5), ws.Cells(ultimaFila, 5)), _
            ws.Range(ws.Cells(2, 2), ws.Cells(ultimaFila, 2)), _
            wr.Cells(renglon, 1).Value)
        wr.Cells(renglon, 2).NumberFormat = "$#,##0.00"

        v = Application.VLookup(wr.Cells(renglon, 1).Value, _
                                Range("Catalogo"), 2, False)
        If IsError(v) Then
            wr.Cells(renglon, 3).Value = "sin catálogo"
        Else
            wr.Cells(renglon, 3).Value = v
        End If
    Next renglon
End Sub

Sub GraficarResumen()
    Dim wr As Worksheet
    Dim ch As ChartObject

    Set wr = ThisWorkbook.Worksheets("Resumen")

    Do While wr.ChartObjects.Count > 0
        wr.ChartObjects(1).Delete
    Loop

    Set ch = wr.ChartObjects.Add(250, 20, 320, 200)
    ch.Chart.SetSourceData wr.Range("A1:B4")
    ch.Chart.ChartType = xlColumnClustered
    ch.Chart.HasTitle = True
    ch.Chart.ChartTitle.Text = "Valor por proveedor"
End Sub
```

**Salida**

```text
Columna E de Proveedores, escrita con una sola instrucción:
  E2  =C2*D2  ->   77,700.00
  E3  =C3*D3  ->   11,610.00
  E4  =C4*D4  ->   18,000.00
  E5  =C5*D5  ->   16,000.00
  E6  =C6*D6  ->   21,930.00

Hoja Resumen:
  Aceros Del Bajío    $95,700.00    Metales
  Empaques Lira       $33,540.00    Empaque
  Papelera Central    $16,000.00    sin catálogo

  Total general      $145,240.00
  Una gráfica de columnas, título Valor por proveedor
```

La columna E queda como fórmula viva porque el reporte se vuelve a abrir cada mes con existencias nuevas. Si el entregable fuera el corte cerrado de un mes, ahí sí conviene congelar el valor.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La limpieza deja la columna B pareja antes de agrupar | 2 |
| La columna E se escribe con una sola instrucción en R1C1 | 3 |
| El resumen usa `SumIfs` y da los tres totales correctos | 2 |
| La búsqueda del giro no detiene la macro y marca Papelera Central | 2 |
| La gráfica se crea y no se encima al correr dos veces | 1 |

**Error que más se ve**

Armar la fórmula de la columna E pegando el número de fila, con algo como `"=C" & fila & "*D" & fila` dentro de un ciclo. Funciona y es el camino que R1C1 estaba ahí para evitar, así que no acredita el criterio.

Nota de calificación: si el alumno deja el cálculo en manual durante todo el procedimiento, `SumIfs` lee ceros y los tres totales salen en cero, sin ningún error. Vale la pena preguntarlo en la revisión aunque el resultado esté bien.

---

## Semana 16 · Unidades 4 y 6 · Dinámicas, errores y protección

### 16.1 · Reconocer

**Solución**

| Momento | Gran total |
|---|---|
| Recién creada | 967,215.00 |
| Después de cambiar el importe de la fila 2 a 200,000 | 967,215.00 |
| Después de `pt.RefreshTable` | 1,038,815.00 |
| Después de agregar la fila 10 y refrescar otra vez | 1,038,815.00 |

Son dos fallas distintas. La primera es del caché: la dinámica lee una copia de los datos, no la hoja, y refrescar la vuelve a llenar. La segunda no la arregla refrescar, porque el caché se creó sobre `A1:D9` y la fila 10 queda fuera de ese rango. Para que entren los renglones nuevos, el origen tiene que ser una tabla.

En el bloque de `Err`, el mensaje sale: dice `Falló la suma` aunque la suma haya salido perfecta. `Err.Number` vale 0 antes del `Open`, 1004 en cuanto el archivo no existe, y sigue en 1004 después de `total = 2 + 2`, porque `Resume Next` no maneja el error, nada más sigue de largo y no limpia nada.

Las dos instrucciones que faltan son revisar `Err.Number` en el renglón inmediato al `Open` y limpiar con `Err.Clear` antes de seguir. Apagar el tramo con `On Error GoTo 0` en cuanto pasó lo peligroso es la tercera, y es la que evita que el resto del procedimiento quede tapado.

**Salida**

```text
recién creada ...... 967,215.00
cambié el importe .. 967,215.00
tras RefreshTable .. 1,038,815.00
fila nueva ......... 1,038,815.00

Err antes del Open ......... 0
Err después del Open ....... 1004
Err después de 2 + 2 ....... 1004
Cuadro de mensaje: Falló la suma
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro grandes totales | 4 |
| Distingue la falla del caché de la del rango fijo | 2 |
| Dice que sale el mensaje y que `Err` sigue en 1004 | 2 |
| Propone revisar de inmediato y limpiar con `Err.Clear` | 2 |

**Error que más se ve**

Contestar que después de refrescar la segunda vez el total sí incluye la venta nueva. Es lo que uno esperaría de la palabra refrescar, y es la razón por la que el rango fijo se cobra tres semanas seguidas.

### 16.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub CorteRegional()
    Dim ws As Worksheet
    Dim wd As Worksheet
    Dim pc As PivotCache
    Dim pt As PivotTable

    On Error GoTo Falla

    Application.ScreenUpdating = False

    Set ws = ThisWorkbook.Worksheets("Ventas")
    Set wd = ThisWorkbook.Worksheets("Resumen")

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create( _
        xlDatabase, ws.Range("A1").CurrentRegion)
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte")

    pt.PivotFields("Región").Orientation = xlRowField
    pt.PivotFields("Importe").Orientation = xlDataField
    pt.RefreshTable

    Application.ScreenUpdating = True
    Exit Sub

Falla:
    MsgBox "Se detuvo con el error " & Err.Number & ": " & Err.Description
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
End Sub
```

**Salida**

```text
Hoja Resumen:

  Bajío        181,045.00
  Centro       153,200.00
  Norte        325,720.00
  Sur          307,250.00
  Total general 967,215.00
```

El renglón de encabezado del campo de dato lo escribe Excel con el idioma de su interfaz: en una instalación en español dice `Suma de Importe` y en una en inglés, `Sum of Importe`. No se califica esa cadena.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El caché se arma con `CurrentRegion` y no con un rango escrito | 2 |
| Los dos campos con la orientación correcta | 2 |
| Correr dos veces no truena porque la dinámica anterior se borra | 2 |
| `On Error GoTo` con etiqueta, y `Exit Sub` antes de ella | 3 |
| El manejador reporta número y descripción, y restaura lo que apagó | 1 |

**Error que más se ve**

Olvidar el `Exit Sub` antes de la etiqueta. El flujo normal se mete al manejador y sale un cuadro que reporta el error 0 con descripción vacía, en una corrida que salió perfecta.

### 16.3 · Integrar

**Solución**

En `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    Dim ws As Worksheet

    For Each ws In ThisWorkbook.Worksheets
        ws.Protect Password:="tia503", UserInterfaceOnly:=True
    Next ws
End Sub
```

En un módulo estándar:

```vba
Option Explicit

Sub CerrarProyecto()
    Dim ws As Worksheet
    Dim wd As Worksheet
    Dim tbl As ListObject
    Dim pc As PivotCache
    Dim pt As PivotTable

    On Error GoTo Falla

    Application.ScreenUpdating = False
    Application.EnableEvents = False

    Set ws = ThisWorkbook.Worksheets("Ventas")
    Set wd = ThisWorkbook.Worksheets("Resumen")

    If ws.ListObjects.Count = 0 Then
        Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1").CurrentRegion, , xlYes)
        tbl.Name = "Ventas2026"
    End If

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, "Ventas2026")
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte")

    pt.PivotFields("Región").Orientation = xlRowField
    pt.PivotFields("Importe").Orientation = xlDataField
    pt.RefreshTable

    Application.EnableEvents = True
    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
    Exit Sub

Falla:
    MsgBox "Se detuvo con el error " & Err.Number & ": " & Err.Description
    Application.EnableEvents = True
    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
End Sub
```

`UserInterfaceOnly` hay que reponerla cada vez que el libro abre porque es una bandera de la sesión, no del archivo: al guardar se conserva la protección, pero no el permiso para que el código escriba. Comprobado, al reabrir el libro protegido de esa forma la primera escritura de la macro devuelve el error 1004.

Si la macro se detuviera justo después de apagar los eventos, Excel se quedaría sin eventos hasta que alguien lo cierre. Los manejadores de hoja y de libro dejarían de dispararse y no habría ningún aviso. Por eso el manejador de errores los vuelve a prender antes de terminar.

**Salida**

```text
Al abrir el libro:  todas las hojas protegidas con UserInterfaceOnly

Usuario escribe a mano en una celda  ->  Excel no lo deja
La macro escribe en la misma celda   ->  escribe sin problema

Corte sobre la tabla Ventas2026:
  Bajío  181,045.00   Centro 153,200.00
  Norte  325,720.00   Sur    307,250.00
  Total  967,215.00

Se agregan dos ventas al final de la tabla y se vuelve a correr:
  el corte las incluye, sin tocar ningún rango del código
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La dinámica se arma sobre la tabla y crece con ella | 3 |
| La protección se repone en `Workbook_Open` con `UserInterfaceOnly` | 3 |
| El manejador restaura eventos, cálculo y pantalla pase lo que pase | 2 |
| Explica por qué la bandera no sobrevive al guardado | 1 |
| Explica qué pasaría si muriera con los eventos apagados | 1 |

**Error que más se ve**

Proteger sin `UserInterfaceOnly` y quitar la protección al principio de cada macro para volverla a poner al final. Funciona hasta la primera macro que truena a media ejecución y deja el libro abierto de par en par.

---

## Semana 17 · Cierre · Examen final

### 17.1 · Reconocer

**Solución**

| Escenario | Err | Por qué |
|---|---|---|
| Dividir entre una celda vacía | 11 | La celda vacía se lee como cero y VBA no divide entre cero |
| `CDbl` sobre `quince` | 13 | Type mismatch: no hay número que convertir |
| Objeto declarado sin `New` | 91 | `Dim` reserva el nombre, no crea el objeto |
| `WorksheetFunction.Left` | 438 | `Left` es de VBA y no vive en `WorksheetFunction` |
| `WorksheetFunction.VLookup` sin dato | 1004 | Lanza el error en vez de devolver `#N/A` |

Las seis que no avisan:

| Operación | Qué produce |
|---|---|
| Ordenar solo la columna de importes | Los importes se ordenan y los nombres se quedan quietos: cada renglón dice algo falso |
| Recorrer con `For Each` un rango filtrado | Suma también las filas ocultas y el total sale del rango completo |
| Encabezado del criterio mal escrito en el filtro avanzado | Esconde todas las filas y el reporte sale vacío |
| Subtotales sin ordenar antes | Un corte cada vez que el valor cambia, así que ningún corte cierra un grupo |
| Leer una dinámica sin refrescar | El total de la corrida anterior, con los datos de ayer |
| Revisar `Err.Number` tres renglones después | Culpa a una instrucción que salió bien |

Ninguna de las seis lanza error. Es lo que las hace caras: el archivo se ve normal y el número llega al reporte.

**Salida**

```text
Err  11, 13, 91, 438, 1004
Fallas mudas: seis, ninguna lanza nada
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cinco números de error, un punto cada uno | 5 |
| Las seis fallas mudas con el resultado equivocado que produce cada una | 3 |
| Dice que ninguna de las seis lanza error | 2 |

**Error que más se ve**

Asignar el 1004 a la celda vacía dividida. El 1004 es de Excel diciendo que no puede hacer algo con un objeto; el de dividir entre cero es de VBA y es el 11.

### 17.2 · Aplicar

**Solución**

```vba
Option Explicit

Sub ReporteCorregido()
    Dim ultimaFila As Long
    Dim fila As Long
    Dim v As Variant

    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = ultimaFila To 2 Step -1
        If Cells(fila, 4).Value < 50000 Then
            Rows(fila).Delete
        End If
    Next fila

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(ultimaFila, 4)).Sort _
        Key1:=Range("D1"), Order1:=xlAscending, Header:=xlYes

    Application.Calculation = xlCalculationAutomatic

    For fila = 2 To ultimaFila
        v = Application.VLookup(Cells(fila, 1).Value, Range("Catalogo"), 2, False)
        If IsError(v) Then
            Cells(fila, 5).Value = "sin catálogo"
        Else
            Cells(fila, 5).Value = v
        End If
    Next fila

    Application.ScreenUpdating = True
End Sub
```

| Defecto | Qué hace mal | Qué produce | Semana |
|---|---|---|---|
| El cálculo se queda en manual | Nunca vuelve a automático | Excel deja de actualizar fórmulas y el usuario cree que sus datos están mal | 7 |
| El ciclo de borrado va hacia adelante | Al borrar una fila, la de abajo sube al lugar por el que ya pasó | Se salta la mitad de las filas que debía borrar | 9 |
| Los dos ciclos van de 2 a 9 | El límite está escrito, no calculado | Con una base más grande deja renglones sin procesar, y con una más chica escribe fuera de los datos | 6 |
| El `Sort` recibe solo `D2:D9` | Ordena una columna sola | Los importes se ordenan y los nombres se quedan: cada renglón dice algo falso | 13 |
| `WorksheetFunction.VLookup` | Lanza el error en vez de devolverlo | Se detiene en la primera clave que falte y deja el reporte partido | 15 |

**Salida**

```text
Antes:  la macro corre, no marca error, y el reporte sale mal en cinco cosas
Después: corre con base de cualquier tamaño, cada renglón conserva sus datos,
         y las claves que faltan quedan marcadas como sin catálogo
```

Vale la pena señalarlo en la revisión aunque no cuente entre los cinco: una celda de importe vacía se compara como cero, así que la condición `< 50000` la borra. Si el negocio no quiere eso, la condición necesita un `IsEmpty` adelante.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El cálculo vuelve a automático antes de terminar | 2 |
| El borrado recorre de abajo hacia arriba | 2 |
| La última fila se calcula, y se vuelve a calcular después de borrar | 2 |
| El `Sort` abarca las cuatro columnas y declara el encabezado | 2 |
| La búsqueda usa `Application` e `IsError` | 1 |
| La tabla nombra los cinco defectos con su semana | 1 |

**Error que más se ve**

Corregir el rango del `Sort` y dejar `Header:=xlNo`. El encabezado entra al montón y termina en medio de la base, ordenado como si fuera una venta más.

### 17.3 · Integrar

**Solución**

En `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    Dim ws As Worksheet

    For Each ws In ThisWorkbook.Worksheets
        ws.Protect Password:="tia503", UserInterfaceOnly:=True
    Next ws
End Sub
```

En un módulo estándar:

```vba
Option Explicit

Function NivelVenta(ByVal monto As Double) As String
    Select Case monto
        Case Is >= 150000
            NivelVenta = "A"
        Case Is >= 100000
            NivelVenta = "B"
        Case Is >= 50000
            NivelVenta = "C"
        Case Else
            NivelVenta = "D"
    End Select
End Function

Sub ProcesarVentas()
    On Error GoTo Falla

    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Application.Calculation = xlCalculationManual

    Call EmparejarRegion
    Call BorrarVacias
    Call QuitarRepetidas
    Call OrdenarBase

    Application.Calculation = xlCalculationAutomatic

    Call ClasificarVentas
    Call TraerGerente
    Call ConvertirEnTabla
    Call ArmarResumen
    Call GraficarResumen

    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Exit Sub

Falla:
    MsgBox "Se detuvo con el error " & Err.Number & ": " & Err.Description
    Application.Calculation = xlCalculationAutomatic
    Application.EnableEvents = True
    Application.ScreenUpdating = True
End Sub

Sub ClasificarVentas()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim fila As Long

    Set ws = ThisWorkbook.Worksheets("Ventas")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    ws.Cells(1, 5).Value = "Nivel"

    For fila = 2 To ultimaFila
        If IsEmpty(ws.Cells(fila, 4).Value) Then
            ws.Cells(fila, 5).Value = "sin importe"
        Else
            ws.Cells(fila, 5).Value = NivelVenta(ws.Cells(fila, 4).Value)
        End If
    Next fila
End Sub

Sub TraerGerente()
    Dim ws As Worksheet
    Dim ultimaFila As Long
    Dim fila As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Ventas")
    ultimaFila = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    ws.Cells(1, 6).Value = "Gerente"

    For fila = 2 To ultimaFila
        v = Application.VLookup(ws.Cells(fila, 3).Value, _
                                Range("Catalogo"), 2, False)
        If IsError(v) Then
            ws.Cells(fila, 6).Value = "sin catálogo"
        Else
            ws.Cells(fila, 6).Value = v
        End If
    Next fila
End Sub

Sub ArmarResumen()
    Dim wd As Worksheet
    Dim pc As PivotCache
    Dim pt As PivotTable

    Set wd = ThisWorkbook.Worksheets("Resumen")

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, "Ventas2026")
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte")

    pt.PivotFields("Región").Orientation = xlRowField
    pt.PivotFields("Importe").Orientation = xlDataField
    pt.RefreshTable
End Sub
```

`EmparejarRegion`, `BorrarVacias`, `QuitarRepetidas` y `OrdenarBase` son los de 13.3 sin cambios. `ConvertirEnTabla` es el de 14.3 y `GraficarResumen` el de 15.3, apuntando a la hoja `Resumen`.

El procedimiento que falla en silencio si se le quita el renglón de la última fila es cualquiera de los que recorren, pero el más caro es `ClasificarVentas`: sin ese renglón hay que escribir un límite, y con una base más larga que la de prueba deja renglones sin nivel, sin marcar nada y sin detenerse.

**Salida**

```text
Base al terminar:
  regiones parejas, sin filas vacías, sin folios repetidos
  ordenada por región ascendente y por importe descendente
  columna Nivel escrita por NivelVenta, también usable desde una celda
  columna Gerente con el vendedor que falta marcado como sin catálogo

Hoja Resumen:
  dinámica sobre la tabla Ventas2026, región en renglones e importe en datos
  gráfica de columnas del mismo corte

Al abrir el libro:
  todas las hojas protegidas, y las macros siguen escribiendo
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La base queda limpia, sin vacías, sin repetidos y bien ordenada | 2 |
| El nivel sale de una función propia que también corre en una celda | 2 |
| La búsqueda del gerente no detiene la macro y marca al que falta | 1 |
| La dinámica y la gráfica se arman sobre la tabla y crecen con ella | 2 |
| El manejador restaura cálculo, eventos y pantalla pase lo que pase | 1 |
| La protección con `UserInterfaceOnly` se repone al abrir | 1 |
| Ningún ciclo trae una dirección escrita a mano | 1 |

**Error que más se ve**

Entregar el libro sin volver a correrlo desde cero sobre datos nuevos. La macro que se fue probando por pedazos deja la base a medio limpiar, y el corte sale de un caché que ya no corresponde. Un libro que no corre tiene techo de 30 %.

