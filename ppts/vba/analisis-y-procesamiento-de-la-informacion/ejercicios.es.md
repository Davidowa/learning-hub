# Ejercicios · Análisis y Procesamiento de la Información · TIA503

Este juego acompaña las diecisiete sesiones del curso y está pensado para el grupo de Empresariales, que llega a la materia usando Excel y sale de ella escribiéndolo. Cada semana trae tres ejercicios: Reconocer se contesta leyendo código y prediciendo qué deja en la hoja, Aplicar se contesta escribiendo una macro contra una especificación con datos y cifras dadas, e Integrar amarra la semana con las anteriores. La dificultad también sube a lo largo del semestre, así que el Reconocer de la semana 12 pide más que el Integrar de la semana 4. Cada ejercicio se entrega en Blackboard como un archivo `.xlsm` más los módulos exportados en `.bas`, salvo donde el enunciado pida otra cosa. Todos los problemas viven en las mismas cinco bases de trabajo: ventas por región, nómina, presupuesto contra real, campañas de marketing y catálogo de proveedores.

---

## Semana 01 · Encuadre y la primera macro grabada

### 01.1 · Reconocer

**Lo que deja una macro grabada**

En el libro `Proveedores.xlsm` alguien grabó esta macro mientras acomodaba la vista del catálogo. La columna D guarda el costo unitario y la E el margen.

```vba
Sub OcultarCostos()
'
' OcultarCostos Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = False
End Sub
```

Contesta tres cosas. Primero, qué columnas quedan ocultas cuando la macro termina. Segundo, para el tercer renglón de instrucción, cuál es el objeto, cuál la propiedad y cuál el valor. Tercero, cuántos renglones de instrucción se ejecutan y cuántos de ellos cambian el estado final de la hoja.

### 01.2 · Aplicar

**Quitar los renglones que se anulan**

Esto es lo que quedó grabado después de que el analista probó tres acomodos antes de decidirse.

```vba
Sub PrepararCatalogo()
'
' PrepararCatalogo Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = True
    Columns("E:E").EntireColumn.Hidden = False
    Columns("D:D").EntireColumn.Hidden = False
    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

Entrega la versión editada que cumpla tres condiciones: al terminar, la columna D queda oculta y la E visible; ningún renglón deshace lo que hizo otro; y el nombre del procedimiento no cambia. Di además cuántos renglones borraste y por qué la macro original llegaba al mismo estado final aunque le sobraran.

### 01.3 · Integrar

**La primera grabación del catálogo de proveedores**

Captura esta tabla en una hoja llamada `Proveedores`, con los encabezados en la fila 1.

| Fila | A · Clave | B · Proveedor | C · Existencias | D · Costo unitario |
|---|---|---|---|---|
| 2 | P-100 | Aceros del Bajío | 420 | 185.00 |
| 3 | P-101 | Empaques Lira | 180 | 64.50 |
| 4 | P-102 | Aceros del Bajío | 75 | 240.00 |
| 5 | P-103 | Papelera Central | 1250 | 12.80 |
| 6 | P-104 | Empaques Lira | 340 | 64.50 |

Guarda el libro como `.xlsm`. Con la grabadora encendida, oculta la columna D, oculta la columna B, vuelve a mostrar la B y ocúltala otra vez. Detén la grabación y abre el editor.

Entrega tres cosas: el código tal como lo escribió la grabadora, el mismo código sin los renglones que corresponden a clics que deshiciste, y un renglón que explique qué pasa con la macro si guardas el libro como `.xlsx`. La macro editada tiene que dejar ocultas B y D, y correrla dos veces seguidas tiene que dar el mismo resultado que correrla una.

---

## Semana 02 · Unidad 1 · El editor de VBA

### 02.1 · Reconocer

**Dónde aparece cada macro**

El libro de metas comerciales trae dos procedimientos, en dos lugares distintos del árbol del proyecto.

```vba
' En Modulo1, un módulo estándar
Sub CargarMetas()
    Range("B2").Value = 120000
    Range("B3").Value = 95000
    Range("B4").Value = 143000
End Sub
```

```vba
' En Hoja1, el módulo de la hoja
Sub AvisarMeta()
    MsgBox "Metas del trimestre cargadas"
End Sub
```

Contesta tres cosas. Cuál de los dos aparece en el cuadro de macros al presionar Alt + F8, y por qué el otro no. Qué queda en B2, B3 y B4 después de correr `CargarMetas` con F5. Y si detienes la ejecución con el resaltado amarillo ya puesto sobre `Range("B3").Value = 95000`, qué tienen en ese instante B2 y B3.

### 02.2 · Aplicar

**Tres procedimientos y una llamada**

En un módulo estándar llamado `Campanas`, escribe a mano tres procedimientos. Nada de grabadora.

`MostrarSegmento` muestra un cuadro de mensaje con el texto exacto `Segmento Premium: 3 campañas`.

`EscribirTotales` escribe 3350 en la celda B2 y 50250 en la celda B3. Son los contactos y el costo del segmento Premium.

`PrepararResumen` no escribe ni muestra nada por su cuenta: llama a los dos anteriores con `Call`, en ese orden.

Entrega el módulo exportado como `.bas` y una captura del cuadro de macros donde se vean los tres nombres.

### 02.3 · Integrar

**La macro grabada, ahora escrita a mano**

Vuelve al libro `Proveedores.xlsm` de la semana pasada. La macro que editaste sirve, pero se grabó y su nombre no dice qué columna toca.

En un módulo estándar llamado `Catalogo`, escribe tres procedimientos a mano. `OcultarCostoUnitario` oculta la columna D y muestra el mensaje `Columna de costo oculta`. `MostrarCostoUnitario` la vuelve a mostrar y muestra el mensaje `Columna de costo visible`. `RevisarCatalogo` llama al primero con `Call` y escribe en F1 el texto `Revisado`.

Después corre `RevisarCatalogo` con F8, con la hoja y el editor acomodados lado a lado, y entrega llena esta traza. El primer F8 resalta el renglón del `Sub`, y de ahí en adelante el renglón resaltado es el que está por correr, no el que acaba de correr.

| F8 | Renglón resaltado | La columna D | F1 |
|---|---|---|---|
| paso 1 | | | |
| paso 2 | | | |
| paso 3 | | | |
| paso 4 | | | |
| paso 5 | | | |
| paso 6 | | | |
| paso 7 | | | |
| paso 8 | | | |

---

## Semana 03 · Unidad 1 · Tipos, variables y celdas

### 03.1 · Reconocer

**Tres declaraciones que no dan lo que parece**

Los tres fragmentos vienen del libro de nómina. Di qué pasa con cada uno.

```vba
' (a)
Dim diasTrabajados As Integer
diasTrabajados = 14.5
Range("C2").Value = diasTrabajados
```

```vba
' (b)
Dim folioInicial, folioFinal As Integer
folioInicial = 41020
folioFinal = 41020
```

```vba
' (c) el módulo no tiene Option Explicit
Dim unidades As Long
unidades = 420
unidaes = 75
MsgBox unidades
```

Para (a), qué número queda en C2. Para (b), cuál de las dos asignaciones se detiene y con qué error, y por qué la otra no. Para (c), qué muestra el mensaje, y qué cambiaría si el módulo empezara con `Option Explicit`.

### 03.2 · Aplicar

**Una ficha de proveedor con el tipo que le toca**

En un módulo que empiece con `Option Explicit`, escribe `Sub FichaProveedor()`. Declara una variable por campo, con el tipo que le corresponde, asígnale estos valores y escríbelos en la fila 1 de una hoja vacía.

| Campo | Valor |
|---|---|
| Clave | P-101 |
| Proveedor | Empaques Lira |
| RFC | ELI980312QX4 |
| Existencias | 180 |
| Costo unitario | 64.50 |
| Activo | verdadero |

La clave va en A1 y los demás campos a su derecha, en ese orden. Usa `Range` para A1 y `Offset` para los otros cinco. En G1 escribe el valor del inventario de esa clave, que es las existencias por el costo unitario.

Ninguna variable puede quedar como `Variant` y ninguna puede llamarse con una sola letra. El RFC va como texto, aunque traiga dígitos.

### 03.3 · Integrar

**Del catálogo a la ficha, con variables**

Sobre la hoja `Proveedores` de la semana 1, escribe `Sub ValorInventario()` en un módulo con `Option Explicit`. El procedimiento tiene que hacer cinco cosas, en este orden.

Leer las existencias de C2 y el costo unitario de D2 en dos variables declaradas con su tipo. Calcular el valor del inventario de ese renglón. Escribirlo en E2. Mostrar un cuadro de mensaje con ese mismo número. Y al final, ocultar la columna D con la instrucción de la semana 1.

Corre el procedimiento desde el cuadro de macros, no desde el editor. Entrega el `.bas` y el `.xlsm` con E2 ya escrita.

---

## Semana 04 · Unidad 1 · Operaciones y nombres de rango

### 04.1 · Reconocer

**Seis cuentas del cierre de presupuesto**

Di qué queda en cada celda al correr este procedimiento.

```vba
Sub Cuentas()
    Range("D2").Value = 250000 - 180000 / 12
    Range("D3").Value = (250000 - 180000) / 12
    Range("D4").Value = 100 \ 7
    Range("D5").Value = 100 Mod 7
    Range("D6").Value = -3 ^ 2
    Range("D7").Value = 7.5 \ 2
End Sub
```

Después contesta dos preguntas. Cuál de las seis expresiones devuelve un número distinto si la escribes como fórmula en la celda en vez de en VBA, y cuál es ese número. Y qué representan D4 y D5 si el problema es empacar 100 piezas en cajas de 7.

### 04.2 · Aplicar

**La tasa mensual equivalente, legible**

Finanzas necesita convertir la inflación anual a su equivalente mensual compuesto. Escribe `Sub TasaMensualEquivalente()` que haga cinco cosas.

Crear dos nombres de rango con `ThisWorkbook.Names.Add`: `InflacionAnual` para `Sheet1!$B$1` e `InflacionMensual` para `Sheet1!$B$2`.

Escribir 0.065 en `InflacionAnual`.

Calcular la tasa mensual equivalente con la fórmula de la potencia, es decir uno más la anual elevado a un doceavo, menos uno.

Dejar el resultado en `InflacionMensual` y darle a esa celda el formato `0.00%`.

Escribir en B3 el mismo resultado ya convertido a texto con `Format` y formato `0.00%`, y en B4 el mismo resultado recortado a seis decimales con `Round`.

Entrega el `.bas` y el `.xlsm`, y agrega un comentario de un renglón que diga por qué B2 y B3 se ven iguales en pantalla y no sirven para lo mismo.

### 04.3 · Integrar

**Variación del presupuesto con nombres**

Captura esta tabla en una hoja llamada `Presupuesto`, con encabezados en la fila 1 y los totales ya escritos en la fila 6.

| Fila | A · Cuenta | B · Presupuesto | C · Real |
|---|---|---|---|
| 2 | Sueldos | 1850000.00 | 1912400.00 |
| 3 | Publicidad | 640000.00 | 588300.50 |
| 4 | Viáticos | 215000.00 | 268900.00 |
| 5 | Sistemas | 430000.00 | 430000.00 |
| 6 | Total | 3135000.00 | 3199600.50 |

Escribe `Sub CalcularVariacion()` en un módulo con `Option Explicit`. Tiene que crear cuatro nombres de rango: `PresupuestoTotal` para `$B$6`, `RealTotal` para `$C$6`, `VariacionTotal` para `$D$6` y `VariacionPct` para `$E$6`. Después lee los dos totales en variables con su tipo, calcula la variación en pesos y la variación como proporción del presupuesto, y escribe las dos en sus celdas con nombre. A la variación en pesos ponle formato `$#,##0.00` y a la proporción, formato `0.00%`.

Después de crear los nombres, ninguna instrucción de tu código puede referirse a D6 ni a E6 por coordenada.

---

## Semana 05 · Unidad 1 · Captura y mensajes

### 05.1 · Reconocer

**Lo que llega de un cuadro de captura**

La macro de nómina pide los días trabajados con un `InputBox`. Llena la tabla con lo que devuelve `IsNumeric` y con lo que hace `CDbl` para cada cosa que el usuario podría teclear.

| Lo que teclean | IsNumeric | CDbl |
|---|---|---|
| 15 | | |
| 1,000 | | |
| $780.50 | | |
| quince | | |
| nada, presionó Cancelar | | |

Después lee este fragmento y di exactamente qué pasa cuando el usuario teclea `quince`, en qué renglón se detiene y con qué número de error.

```vba
Dim t As String
t = InputBox("Días trabajados", "Nómina")

If IsNumeric(t) And CDbl(t) > 0 Then
    Range("C2").Value = CDbl(t)
End If
```

### 05.2 · Aplicar

**Captura de días que no acepta basura**

Escribe `Sub CapturarDias()`. El procedimiento pide los días trabajados de Ana Robles con un `InputBox` cuyo texto es `Días trabajados de Ana Robles` y cuyo título es `Nómina`. Mientras lo que teclean no sea un número mayor que cero, vuelve a preguntar, y antes de volver a preguntar muestra un cuadro con el texto `Eso no es un número de días válido.` y el icono de advertencia.

Cuando el dato ya sirve, pregunta con un cuadro de Sí y No, con icono de pregunta y título `Confirmar`, si se guarda ese número de días. Solo si la respuesta es Sí, escribe el valor en C2.

La validación tiene que ir en dos `If` anidados, no en uno solo con `And`. Explica en un comentario por qué.

### 05.3 · Integrar

**Recibo de nómina capturado y confirmado**

Escribe `Sub CapturarRecibo()` sobre una hoja llamada `Nomina`. Antes de nada, crea con `Names.Add` los nombres `SueldoDiario` para `$B$2`, `DiasTrabajados` para `$B$3`, `PagoBruto` para `$B$4`, `Bono` para `$B$5` y `PagoTotal` para `$B$6`.

Pide dos datos con captura validada, el sueldo diario y los días trabajados. Los dos tienen que ser números mayores que cero, y mientras no lo sean, el procedimiento insiste. Con los datos ya buenos, calcula el pago bruto, el bono, que es el ocho por ciento del bruto, y el pago total. Escribe los cinco valores en sus celdas con nombre y dale formato `$#,##0.00` a las tres celdas de importe.

Cierra con un cuadro de mensaje, con icono de información y título `Recibo`, que muestre los tres importes en tres renglones distintos usando `vbNewLine`.

Prueba con sueldo diario 780.50 y 15 días. En el reporte anota los tres importes que salieron.

---

## Semana 06 · Unidad 2 · Editar lo grabado

### 06.1 · Reconocer

**La macro grabada contra cuarenta renglones**

La hoja `Ventas` tiene encabezados en la fila 1 y datos de la fila 2 a la 41. Las columnas son A folio, B región, C vendedor y D importe. La macro se grabó el mes pasado, cuando la base traía ocho renglones.

```vba
Sub FormatearImportes()
    Range("D2:D9").Select
    Selection.NumberFormat = "$#,##0.00"
    Range("A1").Select
End Sub
```

Contesta cuatro cosas. Cuántos renglones quedan con formato de moneda al correrla hoy. Si Excel marca algún error. Qué devuelve `Cells(Rows.Count, 1).End(xlUp).Row` sobre esta hoja. Y qué dirección devuelve `Range("A1").CurrentRegion`.

### 06.2 · Aplicar

**La misma macro, para cualquier cantidad de renglones**

Reescribe `FormatearImportes` para que sirva con la base que sea. Tiene que cumplir cuatro condiciones.

No queda ningún `Select` ni ningún `Selection` en el código.

La última fila se calcula desde abajo con `End(xlUp)` sobre la columna A y se guarda en una variable `Long`.

El rango de importes se arma con `Range(Cells(...), Cells(...))` y se guarda en una variable declarada `As Range`, asignada con `Set`.

Ese rango recibe el formato `$#,##0.00`, y en F1 se escribe cuántos renglones de datos tiene la base, sin contar el encabezado.

Prueba con la base de ocho renglones de datos y anota qué quedó en F1.

### 06.3 · Integrar

**El catálogo con su columna auxiliar**

Sobre la hoja `Proveedores` de la semana 1, escribe `Sub PrepararCatalogo()` en un módulo con `Option Explicit`. Tiene que hacer cuatro cosas.

Calcular la última fila con datos y armar con `Cells` el rango de costos unitarios, de la fila 2 hasta la última, en la columna D. Darle a ese rango el formato `$#,##0.00`.

Crear el nombre de rango `TotalRenglones` para `$G$1` y escribir ahí cuántos proveedores trae la base.

Revisar si la columna E está oculta. Si lo está, mostrarla; si no, ocultarla. La columna E no se elimina nunca.

Cerrar con un cuadro de mensaje que muestre la dirección del rango de costos que armó, leída con la propiedad `Address`.

Corre la macro dos veces seguidas y anota qué le pasa a la columna E en cada corrida.

---

## Semana 07 · Unidad 2 · Búsqueda de objetivo y encadenamiento

### 07.1 · Reconocer

**Lo que devuelve una búsqueda de objetivo**

El modelo de precio de una línea de producto vive en una hoja con estos nombres de rango ya creados.

| Nombre | Celda | Contenido |
|---|---|---|
| PrecioUnitario | B2 | 120.00 |
| Unidades | B3 | 12000 |
| CostoVariable | B4 | 84.00 |
| CostosFijos | B5 | 380000.00 |
| MargenTotal | B6 | la fórmula `=(PrecioUnitario-CostoVariable)*Unidades-CostosFijos` |

Con esos datos, B6 muestra 52,000.00. Se corre esta macro.

```vba
Sub BuscarPrecio()
    Range("MargenTotal").GoalSeek _
        Goal:=250000, _
        ChangingCell:=Range("PrecioUnitario")
End Sub
```

Contesta cuatro cosas. Cuál de las dos celdas que menciona la macro no puede contener una fórmula, y por qué. A qué precio unitario llega la búsqueda. Si al terminar B6 vale exactamente 250,000.00, y qué dos propiedades de `Application` gobiernan esa respuesta. Y qué pasa si alguien escribe `ChangingCell:=Range("MargenTotal")`.

### 07.2 · Aplicar

**La maestra que acota y busca**

Escribe cuatro procedimientos en el mismo módulo, sobre el modelo de precio de 7.1.

`CargarParametros` escribe los cuatro datos de entrada en sus celdas con nombre: 120.00, 12000, 84.00 y 380000.00.

`FormatearModelo` le da formato `$#,##0.00` a las celdas de precio, costo variable, costos fijos y margen.

`BuscarPrecio` corre la búsqueda de objetivo para dejar el margen en 250,000.

`CerrarPrecio` es la maestra. Apaga el redibujado de pantalla y pone el cálculo en manual mientras se cargan y se formatean los parámetros, llama a los tres anteriores en orden con `Call`, y deja las dos propiedades como las encontró antes de terminar. Cuida que la búsqueda de objetivo corra con la hoja recalculando: es un método que tantea, y si la fórmula del margen no se vuelve a evaluar en cada intento, no tiene contra qué comparar.

La maestra no puede pasar de diez renglones de instrucción y no puede tener una sola que toque una celda. Cualquiera de los otros tres tiene que poder correrse solo desde el cuadro de macros.

### 07.3 · Integrar

**El margen como función, y el precio como respuesta**

Sobre el mismo modelo, agrega dos cosas.

Una función `MargenTotalCalculado` que reciba el precio, las unidades, el costo variable y los costos fijos, los cuatro `As Double`, y devuelva el margen. Con 120, 12000, 84 y 380000 tiene que devolver el mismo número que muestra B6.

Un procedimiento `CompararMargen` que llame a esa función con los valores actuales de las celdas con nombre, escriba el resultado en B8 y lo compare contra lo que trae B6. Si los dos números coinciden, escribe en B9 el texto `Cuadra`; si no, escribe `Revisar`.

Después de eso, corre `CerrarPrecio` y anota tres números: el precio que encontró la búsqueda, el valor que quedó en B6 y la diferencia contra 250,000. Ese tercer número es el punto del ejercicio, así que no lo redondees.

---

## Semana 08 · Unidad 3 · Decisiones y primer parcial

### 08.1 · Reconocer

**Siete comparaciones que contestan al revés**

La columna de región de la hoja `Ventas` se capturó a mano y trae Norte, norte y NORTE mezclados. La celda A1 de una hoja nueva está vacía, sin nada escrito. Di qué devuelve cada una de estas comparaciones.

```vba
MsgBox "Norte" = "norte"
MsgBox "10" < "9"
MsgBox 10 < 9
MsgBox CInt(True)
MsgBox Range("A1").Value = 0
MsgBox Range("A1").Value = ""
MsgBox Range("A1").Value > 0
```

Después contesta dos preguntas de negocio. Si agrupas las ventas por el texto de la columna región tal como está capturado, cuántas regiones distintas va a reportar Excel para el norte. Y si una venta se registró con el importe vacío, cuál de las tres últimas comparaciones no sirve para distinguirla de una venta de cero pesos.

### 08.2 · Aplicar

**Clasificar un importe de venta, de dos maneras**

El área comercial clasifica cada venta según su importe con esta tabla.

| Importe | Nivel |
|---|---|
| 150,000 o más | A |
| de 100,000 a menos de 150,000 | B |
| de 50,000 a menos de 100,000 | C |
| menos de 50,000 | D |

Escribe dos procedimientos que lean el importe de D2 y escriban el nivel en E2. `ClasificarConIf` usa `If`, `ElseIf` y `Else`. `ClasificarConCase` usa `Select Case`. Los dos tienen que dar el mismo resultado para los cuatro importes de prueba: 210500, 128400, 65900 y 41200.

Ninguna venta puede quedar sin nivel. Cierra con un comentario de dos renglones que diga por qué en este caso conviene escribir los casos con `Is` y no con `To`, y cuál de las dos formas prefieres.

### 08.3 · Integrar

**Repaso del primer parcial: del clic al nivel de la cuenta**

Este ejercicio cruza las tres unidades que entran al parcial. Sobre la hoja `Ventas` de ocho renglones de datos, entrega un módulo con una maestra llamada `RevisarCuenta` y tres procedimientos que ella llame.

La maestra apaga el redibujado y el cálculo automático, llama a los tres en orden y los vuelve a prender.

`CapturarImporte` pide un importe con `InputBox`, insiste hasta que sea un número mayor que cero y lo escribe en la celda con nombre `ImporteRevisado`, que tu código crea apuntando a `$G$2`.

`MedirBase` calcula la última fila con datos de la columna A, arma con `Cells` el rango de importes de la columna D y escribe en la celda con nombre `TotalRenglones` cuántos renglones de datos hay.

`ClasificarImporte` lee `ImporteRevisado`, le aplica la tabla de niveles de 8.2 con `Select Case` y escribe el nivel en la celda con nombre `NivelRevisado`, que tu código crea apuntando a `$G$3`, además de dar formato `$#,##0.00` a `ImporteRevisado`.

No puede haber ningún ciclo, ningún `Select` y ninguna dirección de celda escrita a mano dentro de `ClasificarImporte`. Entrega además una tabla de tres renglones que diga de qué semana viene cada procedimiento.

---

## Semana 09 · Unidad 3 · Repetición

### 09.1 · Reconocer

**Tres ciclos y lo que dejan**

Di qué produce cada uno.

```vba
' (a)
Dim i As Long
Dim mensaje As String
mensaje = "Periodos: "
For i = 10 To 1 Step -3
    mensaje = mensaje & i & " "
Next i
MsgBox mensaje
```

```vba
' (b) sobre el rango A1:B2 de la hoja de campañas
Dim celda As Range
Dim orden As String
For Each celda In Range("A1:B2")
    orden = orden & celda.Address & " "
Next celda
MsgBox orden
```

```vba
' (c) las filas 2 a 7 traen todas la marca X en la columna E
Dim fila As Long
For fila = 2 To 7
    If Cells(fila, 5).Value = "X" Then
        Rows(fila).Delete
    End If
Next fila
```

Para (a), el texto exacto del mensaje. Para (b), el orden en que entrega las cuatro celdas. Para (c), cuántas de las seis campañas marcadas quedan en la hoja al terminar, y qué cambia si el ciclo se escribe `For fila = 7 To 2 Step -1`.

### 09.2 · Aplicar

**Marcar la cartera vencida**

Captura esta base en una hoja llamada `Cartera`, con encabezados en la fila 1.

| Fila | A · Cliente | B · Factura | C · Importe | D · Días de atraso |
|---|---|---|---|---|
| 2 | Aceros del Bajío | F-2201 | 77700.00 | 12 |
| 3 | Empaques Lira | F-2202 | 11610.00 | 45 |
| 4 | Papelera Central | F-2203 | 16000.00 | 0 |
| 5 | Aceros del Bajío | F-2204 | 18000.00 | 61 |
| 6 | Empaques Lira | F-2205 | 21930.00 | 30 |
| 7 | Comercial Sáenz | F-2206 | 40120.00 | 38 |

Escribe `Sub MarcarVencidos()`. Calcula la última fila con datos, recorre la base desde la fila 2 y, en cada renglón cuyos días de atraso pasen de 30, escribe `Vencido` en la columna E y suma su importe. Al terminar, escribe en G1 cuántas facturas se marcaron y en G2 el importe vencido acumulado, con formato `$#,##0.00`.

Un renglón con exactamente 30 días de atraso no se marca. Ninguna dirección de celda del ciclo puede estar escrita a mano.

### 09.3 · Integrar

**Depurar la lista de campañas**

Captura esta base en una hoja llamada `Campanas`. Las celdas C4 y C6 se quedan vacías a propósito, sin ningún cero escrito.

| Fila | A · Campaña | B · Segmento | C · Contactos | D · Costo |
|---|---|---|---|---|
| 2 | C-01 | Premium | 1250 | 18750.00 |
| 3 | C-02 | Nuevo | 3400 | 27200.00 |
| 4 | C-03 | Premium | | 14700.00 |
| 5 | C-04 | Masivo | 7600 | 38000.00 |
| 6 | C-05 | Premium | | 16800.00 |
| 7 | C-06 | Masivo | 5300 | 26500.00 |

Escribe dos procedimientos y una maestra que los llame.

`ClasificarCampanas` recorre la base con rango variable y escribe en la columna E: `Sin dato` si la celda de contactos está vacía, `Masiva` si trae 3000 contactos o más, y `Focalizada` en cualquier otro caso. Lleva tres contadores y los escribe en G1, G2 y G3.

`DepurarSinDato` borra las filas clasificadas como `Sin dato`, recorriendo en el sentido que no se salta renglones.

La maestra apaga el redibujado, llama a los dos y lo vuelve a prender.

En el reporte anota los tres contadores y cuántos renglones de datos quedan al final.

---

## Semana 10 · Unidades 1 y 3 · Procedimientos y funciones

### 10.1 · Reconocer

**Un Sub que cambia lo que nadie le pidió**

Este módulo es del libro de nómina.

```vba
Sub AplicarBono(monto As Double)
    monto = monto * 1.08
End Sub

Function TotalRecibo(bruto As Double, bono As Double) As Double
    ' aquí iba la suma y se quedó sin escribir
End Function

Sub Probar()
    Dim bruto As Double
    bruto = 11707.5

    AplicarBono bruto
    Range("B2").Value = bruto
    Range("B3").Value = TotalRecibo(11707.5, 936.6)
End Sub
```

Di qué queda en B2 y qué queda en B3, y por qué ninguno de los dos casos marca error. Después indica el cambio de una sola palabra que dejaría B2 en 11707.5, y el renglón que falta para que B3 quede en 12644.1.

### 10.2 · Aplicar

**Una función de comisión que Excel acepte en la celda**

La comisión de una venta se calcula con esta tabla.

| Importe de la venta | Comisión |
|---|---|
| 150,000 o más | 6 % |
| de 100,000 a menos de 150,000 | 4 % |
| de 50,000 a menos de 100,000 | 2.5 % |
| menos de 50,000 | 0 % |

Escribe `Function ComisionVenta(ByVal monto As Double) As Double` en un módulo estándar. Después captura la base de ventas en una hoja llamada `Ventas`, con encabezados en la fila 1.

| Fila | A · Folio | B · Región | C · Vendedor | D · Importe |
|---|---|---|---|---|
| 2 | V-1001 | Norte | Ana Robles | 128400.00 |
| 3 | V-1002 | Sur | Beto Lira | 96750.00 |
| 4 | V-1003 | Norte | Carla Méndez | 143200.00 |
| 5 | V-1004 | Centro | Darío Sáenz | 87300.00 |
| 6 | V-1005 | Sur | Ana Robles | 210500.00 |
| 7 | V-1006 | Centro | Beto Lira | 65900.00 |
| 8 | V-1007 | Norte | Carla Méndez | 54120.00 |
| 9 | V-1008 | Bajío | Darío Sáenz | 181045.00 |

En la celda E2 escribe a mano la fórmula que llama a tu función con el importe de esa fila, y cópiala hasta E9. En E10 pon la suma de la columna. Entrega el `.xlsm` con las nueve celdas resueltas y anota el total de comisiones.

### 10.3 · Integrar

**La nómina partida en piezas**

Captura esta base en la hoja `Nomina`, con encabezados en la fila 1.

| Fila | A · Empleado | B · Número | C · Días | D · Sueldo diario | E · Bono |
|---|---|---|---|---|---|
| 2 | Ana Robles | 4102 | 15 | 780.50 | 0.08 |
| 3 | Beto Lira | 4118 | 15 | 612.00 | 0.05 |
| 4 | Carla Méndez | 4127 | 13 | 945.00 | 0.10 |
| 5 | Darío Sáenz | 4130 | 15 | 528.40 | 0.00 |

Escribe una función y tres procedimientos.

`PagoTotal` recibe los días, el sueldo diario y el porcentaje de bono, los tres `As Double` y los tres por valor, y devuelve el pago total del recibo.

`CalcularPagos` recorre la base con rango variable y escribe el pago total de cada empleado en la columna F, llamando a la función. No calcula nada por su cuenta.

`MarcarIncompletos` recorre la base y escribe `Revisar` en la columna G de todo renglón donde los días trabajados sean menos de 15.

`TotalizarNomina` suma la columna F recorriéndola y escribe el total en el renglón que sigue al último con datos, con formato `$#,##0.00`.

`ProcesarNomina` es la maestra: apaga el redibujado, llama a los tres procedimientos en orden y vuelve a prender el redibujado.

La maestra no pasa de diez renglones de instrucción y ningún procedimiento pasa de cuarenta. Cada uno tiene que correr solo desde el cuadro de macros. Anota los cuatro pagos y el total.

---

## Semana 11 · Unidades 2 y 3 · Eventos

### 11.1 · Reconocer

**El mismo manejador en dos lugares distintos**

Los dos fragmentos son el mismo manejador en dos lugares distintos. Di qué pasa en cada caso, y después contesta el inciso (c), que va al final.

```vba
' (a) pegado en Modulo1, un módulo estándar
Private Sub Worksheet_Change(ByVal Target As Range)
    MsgBox "Cambió " & Target.Address
End Sub
```

```vba
' (b) pegado en el módulo de una hoja de pruebas vacía
Private Sub Worksheet_Change(ByVal Target As Range)
    Target.Offset(0, 1).Value = "revisado"
End Sub
```

Para (a), qué ocurre al escribir en B2 de esa hoja, y si Excel avisa de algo. Para (b), qué ocurre al escribir 15 en B2, y por qué.

Para (c), llena la tabla. Es el manejador de (b) con guarda sobre B2, que en vez de escribir siempre lo mismo pregunta `IsNumeric(Target.Value)` y escribe `Número` o `No es número` en C2. Las dos columnas de en medio no son la misma pregunta: el manejador se dispara después de que Excel ya interpretó lo que se tecleó, así que `Target.Value` no siempre es el texto que el usuario capturó. Contesta las dos y di en qué renglones difieren.

| Lo que se teclea en B2 | `IsNumeric` sobre ese texto | `IsNumeric(Target.Value)` | Qué se escribe en C2 |
|---|---|---|---|
| 15 | | | |
| 12.5 | | | |
| $780.50 | | | |
| 15% | | | |
| quince | | | |

### 11.2 · Aplicar

**La celda de captura que se revisa sola**

Trabaja sobre la hoja `Nomina` de la semana 10, donde la columna C guarda los días trabajados. En el módulo de esa hoja escribe el manejador de `Worksheet_Change` que cumpla esto.

Solo reacciona cuando el cambio ocurre en C2. Cualquier otro cambio de la hoja lo ignora.

Si lo capturado es un número, escribe en H2 el texto `Días válidos` y le da a C2 el formato `0`. Si no lo es, escribe `Revisar captura` en H2 y le da a C2 relleno amarillo con `Interior.Color`.

Escribir en H2 no puede volver a disparar el manejador. Resuélvelo con la guarda de dirección y explica en un comentario por qué esa guarda basta aquí y no bastaría si el manejador escribiera también en C2.

Prueba escribiendo veinte veces seguidas en C2. Si Excel se cae, la guarda está mal puesta.

### 11.3 · Integrar

**El libro de nómina que se prepara solo**

Sobre el libro de la semana 10, agrega dos manejadores y déjalos trabajando con la función que ya tienes.

En `ThisWorkbook`, un `Workbook_Open` que active la hoja `Nomina`, seleccione C2 y muestre un cuadro con el texto `Captura los días trabajados en C2`.

En el módulo de la hoja `Nomina`, un `Worksheet_Change` que reaccione solo a C2. Si el valor capturado es un número mayor que cero, llama a la función `PagoTotal` de la semana 10 con ese número de días, el sueldo diario de D2 y el bono de E2, y escribe el resultado en F2 con formato `$#,##0.00`. Si no es un número válido, deja F2 vacía y escribe `Revisar captura` en G2.

Como el manejador escribe en dos celdas, apaga los eventos mientras escribe y vuélvelos a prender. Anota qué queda en F2 al capturar 15 días para Ana Robles.

---

## Semana 12 · Unidad 3 · Clases propias

### 12.1 · Reconocer

**Dos nombres del mismo objeto**

El proyecto trae un módulo de clase llamado `Proveedor` con un campo privado por dato, propiedades `Get` y `Let` para `Clave`, `Existencias` y `CostoUnitario`, y una función `Valor` que devuelve las existencias por el costo unitario. La propiedad `Let CostoUnitario` deja el campo en cero si le pasan un número negativo.

Di qué imprime cada bloque, o con qué error se detiene.

```vba
' (a)
Dim a As Proveedor, b As Proveedor
Set a = New Proveedor
Set b = a

a.CostoUnitario = 185
a.Existencias = 420
b.Existencias = 75

Debug.Print a.Valor
```

```vba
' (b)
Dim p As Proveedor
p.Clave = "P-100"
```

```vba
' (c)
Dim p As Proveedor
Set p = New Proveedor
p.Existencias = 420
p.CostoUnitario = -185

Debug.Print p.Valor
```

Para (a) di además cuántos objetos se crearon en total y qué habría que cambiar para que `a` y `b` fueran independientes.

### 12.2 · Aplicar

**La clase Proveedor**

Crea un módulo de clase y ponle de nombre `Proveedor`. Tiene que traer esto.

Tres campos privados: `pClave As String`, `pExistencias As Long` y `pCostoUnitario As Double`.

Propiedades `Get` y `Let` para los tres. La de existencias y la de costo unitario rechazan negativos: si les pasan uno, dejan el campo en cero. La validación vive en la clase, nunca en la macro que la usa.

Una función pública `Valor` que devuelva las existencias por el costo unitario.

Un `Class_Initialize` que deje la clave en `sin clave` y los dos números en cero.

Escribe además un `Sub ProbarProveedor()` en un módulo estándar que cree un objeto, imprima su estado recién nacido, le asigne P-100, 420 y 185.00, imprima su valor, después le asigne un costo de -50 y vuelva a imprimir su valor. Usa `Debug.Print` y entrega la ventana Inmediato en la captura.

### 12.3 · Integrar

**Un objeto por renglón del catálogo**

Sobre la hoja `Proveedores` de la semana 1, escribe `Sub ValuarCatalogo()`.

Calcula la última fila con datos. Recorre la base desde la fila 2 y, en cada vuelta, crea un objeto `Proveedor` nuevo, le asigna la clave, las existencias y el costo unitario del renglón, y escribe en la columna E el valor que devuelve el objeto. Acumula ese valor en una variable y, al terminar, escríbelo en la celda con nombre `ValorTotal`, que tu código crea apuntando a `$G$1`, con formato `$#,##0.00`.

Tres condiciones. El `New` va dentro del ciclo, no antes. Ningún cálculo de valor vive fuera de la clase. Y si un renglón trae la celda de existencias vacía, el objeto se queda en cero y el renglón se marca con `Revisar` en la columna F.

Anota el valor por renglón y el total.

---

## Semana 13 · Unidad 4 · Limpiar y ordenar

### 13.1 · Reconocer

**Lo que ensucia una base y no se ve**

Contesta los cuatro bloques.

```vba
' (a)
Debug.Print "[" & Trim("  Aceros del Bajío  ") & "]"
Debug.Print "[" & Trim("Aceros    del Bajío") & "]"
Debug.Print "[" & WorksheetFunction.Trim("Aceros    del Bajío") & "]"
```

```vba
' (b)
Dim s As String
s = "Lira" & Chr(160)

Debug.Print Len(s), Len(Trim(s))
Debug.Print Trim(s) = "Lira"
```

```vba
' (c)
Debug.Print WorksheetFunction.Proper("empaques lira")
Debug.Print WorksheetFunction.Proper("aceros del bajío")
Debug.Print WorksheetFunction.Proper("PAPELERA central")
```

```vba
' (d) la base ocupa B1:C4, con encabezados
'     B: Proveedor       C: Clave
'     Empaques Lira      P-101
'     Aceros del Bajío   P-100
'     Empaques Lira      P-104

Range("B1:C4").RemoveDuplicates Columns:=2, Header:=xlYes
```

Para (c) di cuál de los tres resultados no es el que quería el usuario. Para (d), cuántas filas quedan y qué número habría que pasar en `Columns` para quitar los proveedores repetidos.

### 13.2 · Aplicar

**Limpiar la columna de proveedor**

La columna A de la hoja `Sucia` trae los nombres tal como llegaron de otro sistema, de la fila 2 en adelante.

| Fila | Lo que trae la celda |
|---|---|
| 2 | dos espacios, `aceros del bajío`, un espacio |
| 3 | `empaques    lira`, con cuatro espacios en medio |
| 4 | `PAPELERA central` |
| 5 | `comercial sáenz` seguido de un espacio duro, `Chr(160)` |

Escribe `Sub LimpiarProveedores()`. Calcula la última fila con datos, recorre la columna A con `For Each` sobre el rango armado, y deja cada nombre limpio en tres pasos: primero cambia el espacio duro por un espacio normal, después colapsa los espacios de sobra con la versión de la hoja de `Trim`, y al final empareja las mayúsculas con `Proper`.

El orden de los tres pasos importa. Explícalo en un comentario. Anota los cuatro nombres que quedaron.

### 13.3 · Integrar

**Repaso del segundo parcial: la base lista para el reporte**

Este ejercicio cruza de la semana 8 a la 13. Captura la base sucia en una hoja llamada `Ventas`, tal cual, con la fila 4 completamente vacía.

| Fila | A · Folio | B · Región | C · Vendedor | D · Importe |
|---|---|---|---|---|
| 2 | V-1001 | Norte | Ana Robles | 128400.00 |
| 3 | V-1002 | sur | Beto Lira | 96750.00 |
| 4 | | | | |
| 5 | V-1003 | NORTE | Carla Méndez | 143200.00 |
| 6 | V-1002 | sur | Beto Lira | 96750.00 |
| 7 | V-1004 | Centro | Darío Sáenz | 87300.00 |
| 8 | V-1005 | Sur | Ana Robles | 210500.00 |

Escribe una maestra que llame a cuatro procedimientos, en este orden.

`EmparejarRegion` deja la columna B con mayúsculas parejas y sin espacios de sobra.

`BorrarVacias` elimina las filas sin ningún dato, recorriendo en el sentido correcto.

`QuitarRepetidas` quita las ventas con folio repetido y deja la primera que apareció.

`OrdenarBase` ordena la base completa por región ascendente y, dentro de cada región, por importe descendente, con el encabezado declarado.

Al terminar, la maestra escribe en F1 cuántos renglones de datos quedaron y en F2 el importe total, con formato `$#,##0.00`. Entrega la base antes y después en dos hojas, y comprueba renglón por renglón que cada importe siga con su vendedor.

---

## Semana 14 · Unidad 4 · Filtros, subtotales y tablas

### 14.1 · Reconocer

**El total que suma lo que no se ve**

Sobre la base de ventas de ocho renglones de la semana 10, se corre esto.

```vba
Range("A1:D9").AutoFilter Field:=2, Criteria1:="Norte"
```

En pantalla quedan tres renglones. Después se calcula el total de la columna D de cuatro maneras: con un `For Each` sobre `Range("D2:D9")`, con un `For Each` sobre ese mismo rango pero pidiéndole `SpecialCells(xlCellTypeVisible)`, con la fórmula `SUBTOTAL(9,D2:D9)` escrita en una celda, y con la fórmula `SUM(D2:D9)`.

Di qué devuelve cada una de las cuatro y por qué dos de ellas devuelven el mismo número equivocado.

Después contesta esto: la hoja tiene en F1 el encabezado `Departamento` y en F2 el valor `Norte`, y la base tiene en B1 el encabezado `Región`. Se corre `Range("A1:D9").AdvancedFilter xlFilterInPlace, Range("F1:F2")`. Cuántos renglones quedan visibles y qué mensaje de error aparece.

### 14.2 · Aplicar

**El total de la región filtrada**

Escribe `Sub TotalRegionVisible()` sobre la base de ventas.

Lee de la celda H1 el nombre de la región que se va a filtrar. Aplica el filtro automático sobre la columna de región con ese criterio. Recorre solo las celdas visibles de la columna de importes y acumula el total. Escribe en H2 cuántos renglones quedaron visibles y en H3 el total, con formato `$#,##0.00`.

Después, en H4, escribe la fórmula que calcula ese mismo total con `SUBTOTAL` y comprueba que los dos números coincidan. Si no coinciden, el ciclo no está respetando el filtro.

Corre la macro con `Norte`, con `Sur` y con `Bajío` en H1, y anota los tres pares de números.

### 14.3 · Integrar

**La base como tabla, con su resumen por región**

Sobre la base de ventas de ocho renglones, entrega tres procedimientos y una maestra.

`ConvertirEnTabla` convierte el bloque que rodea a A1 en un `ListObject` llamado `Ventas2026`. Si al correrla dos veces truena porque el nombre ya existe, tu código tiene que prevenirlo revisando antes si ya hay una tabla en la hoja.

`ResumirPorRegion` escribe en la hoja `Resumen`, a partir de A1, un renglón por cada una de las cuatro regiones de la base, con su nombre, su número de ventas y su importe total. Recorre la tabla por el cuerpo de datos, no por una dirección escrita a mano.

`TablaTieneDatos` es una función que devuelve `Boolean`. Si el cuerpo de la tabla no tiene ningún renglón, muestra el mensaje `La tabla no tiene datos` y devuelve falso. La maestra la consulta antes de pedir el resumen.

La maestra apaga el redibujado, llama a lo que haga falta en orden y lo vuelve a prender.

Anota el resumen completo. Después agrega dos ventas nuevas al final de la tabla, vuelve a correr la maestra y comprueba que aparezcan en el resumen sin haber tocado ningún rango del código.

---

## Semana 15 · Unidades 4 y 5 · Reportes y R1C1

### 15.1 · Reconocer

**Dos bibliotecas y una búsqueda que se cae**

Contesta los cuatro bloques. El rango con nombre `Catalogo` va de A1 a B4 en la hoja `Claves`, y trae P-100 con Aceros del Bajío, P-101 con Empaques Lira y P-103 con Papelera Central.

```vba
' (a)
Debug.Print WorksheetFunction.Left("Aceros del Bajío", 6)
Debug.Print Left("Aceros del Bajío", 6)
```

```vba
' (b)
Dim v As Variant

Debug.Print WorksheetFunction.VLookup("P-999", Range("Catalogo"), 2, False)

v = Application.VLookup("P-999", Range("Catalogo"), 2, False)
Debug.Print IsError(v)
```

```vba
' (c) A1 vale 10 y A2 vale 20
Range("C1").Formula = "=SUM(A1:A2)"
Range("D1").Value = WorksheetFunction.Sum(Range("A1:A2"))
' y ahora alguien cambia A1 a 100
```

```vba
' (d)
Range("C2").Formula = "=A2*B2"
Debug.Print Range("C2").FormulaR1C1
```

Para (b) di el número de error de cada uno y cuál de los dos permite seguir. Para (c), qué muestran C1 y D1 antes y después del cambio. Para (d), la cadena exacta que imprime.

### 15.2 · Aplicar

**La descripción de cada clave, sin detener el reporte**

La hoja `Claves` trae en A1:B4 el rango con nombre `Catalogo`, con encabezados en la fila 1 y estas tres correspondencias: P-100 con Aceros del Bajío, P-101 con Empaques Lira y P-103 con Papelera Central. La hoja `Movimientos` trae esto, con encabezados en la fila 1.

| Fila | A · Clave | B · Importe |
|---|---|---|
| 2 | P-100 | 25000.00 |
| 3 | P-101 | 12400.00 |
| 4 | P-100 | 18600.00 |
| 5 | P-103 | 9750.00 |
| 6 | P-107 | 31200.00 |
| 7 | P-101 | 7300.00 |
| 8 | P-100 | 22050.00 |
| 9 | P-103 | 14800.00 |

Escribe `Sub CompletarMovimientos()`. Recorre las ocho filas con rango variable y, por cada una, busca el nombre del proveedor en el catálogo y escríbelo en la columna C. Si la clave no está, escribe `sin catálogo` en la columna C y pinta de amarillo las tres celdas de esa fila. La macro no se puede detener en la fila 6.

Después escribe en E1 el total de importes de Aceros del Bajío usando `SumIfs` sobre la columna de nombres, y en E2 cuántos movimientos son, con `CountIf`.

La variable que recibe el resultado de la búsqueda tiene que declararse `As Variant`. Explica en un comentario por qué un `String` no sirve ahí.

### 15.3 · Integrar

**El reporte mensual del catálogo**

Sobre la hoja `Proveedores` de cinco renglones, arma el reporte completo. En la hoja `Claves` deja el rango con nombre `Catalogo`, con encabezados y dos correspondencias nada más: `Aceros Del Bajío` con `Metales` y `Empaques Lira` con `Empaque`. Papelera Central no está en el catálogo, a propósito.

Entrega una maestra y cuatro procedimientos.

`LimpiarNombres` deja la columna B sin espacios de sobra, sin espacios duros y con mayúsculas parejas.

`CalcularValor` escribe la columna E, el valor del inventario de cada renglón, con una sola instrucción en notación R1C1 sobre el rango completo. Nada de ciclos y nada de armar la cadena de la fórmula pegando el número de fila.

`ResumirPorProveedor` escribe en la hoja `Resumen` un renglón por proveedor con su valor total, calculado con `SumIfs` sobre la columna E, y el giro traído del rango `Catalogo` con una búsqueda que no detenga la macro cuando falte el proveedor.

`GraficarResumen` agrega una gráfica de columnas agrupadas sobre el resumen, con título `Valor por proveedor`. Si ya existe una gráfica en esa hoja, la borra antes de crear la nueva.

La maestra apaga el redibujado y el cálculo, llama a los cuatro y lo vuelve a prender. Anota el valor total por proveedor y el total general, y di si dejaste la columna E como fórmula viva o como valor congelado, con una línea de justificación.

---

## Semana 16 · Unidades 4 y 6 · Dinámicas, errores y protección

### 16.1 · Reconocer

**La dinámica que muestra el total de ayer**

Sobre la base de ventas de ocho renglones, con un total de 967,215.00, se crea una tabla dinámica desde macro con el caché armado sobre `A1:D9`, la región en los renglones y el importe en los datos. Después ocurre esto, en orden: se cambia el importe de la fila 2 de 128,400.00 a 200,000.00; se corre `pt.RefreshTable`; se agrega una venta nueva de 50,000.00 en la fila 10 y se vuelve a refrescar.

Di qué gran total muestra la dinámica en cada uno de los cuatro momentos, y por qué el último no se arregla refrescando.

Después contesta este bloque.

```vba
On Error Resume Next

Set wb = Workbooks.Open("C:\cierres\enero.xlsx")   ' el archivo no existe
total = 2 + 2

If Err.Number <> 0 Then
    MsgBox "Falló la suma"
End If
```

Qué muestra el mensaje, qué valor trae `Err.Number` en cada renglón, y qué dos instrucciones habría que agregar para que el diagnóstico apunte al renglón que de verdad falló.

### 16.2 · Aplicar

**El corte por región, con red**

Escribe `Sub CorteRegional()` sobre la base de ventas.

Crea la tabla dinámica desde código, con el caché armado sobre el bloque que rodea a A1, la región como campo de renglón y el importe como campo de dato, con destino en la celda A1 de la hoja `Resumen`. Si ya existe una dinámica con ese nombre, bórrala antes de crearla. Al terminar, refréscala.

Todo el procedimiento va bajo un manejador de errores de verdad, con `On Error GoTo` y una etiqueta al final que muestre el número y la descripción del error y vuelva a prender el redibujado y el cálculo. Entre el cuerpo y la etiqueta tiene que ir la instrucción que impide que el flujo normal caiga en el manejador.

Anota los cuatro renglones del corte y el gran total.

### 16.3 · Integrar

**Cerrar el libro del proyecto**

Sobre el libro de ventas, deja las tres piezas que faltan para poder entregarlo.

Convierte la base en una tabla y arma la dinámica de 16.2 tomando la tabla como origen, no un rango. Comprueba que al agregar renglones y refrescar, el corte los incluya.

Protege todas las hojas con contraseña y con `UserInterfaceOnly` en `True`, desde un `Workbook_Open` en `ThisWorkbook`. Comprueba que el usuario no pueda escribir en una celda a mano y que tus macros sí puedan.

Ponle a la maestra un manejador de errores que, además de avisar, vuelva a dejar los eventos prendidos, el cálculo en automático y el redibujado encendido, pase lo que pase.

En el reporte explica en tres renglones por qué `UserInterfaceOnly` hay que reponerla en cada apertura y qué pasaría si la macro se detuviera justo después de apagar los eventos.

---

## Semana 17 · Cierre · Examen final

### 17.1 · Reconocer

**Cinco errores con número y seis fallas mudas**

Primero, di con qué número de error se detiene cada escenario y por qué.

| Escenario | Err |
|---|---|
| Se divide el importe entre el número de facturas y esa celda está vacía | |
| Se convierte con `CDbl` lo que el usuario tecleó como `quince` | |
| Se declara un objeto `Proveedor` y se le asigna la clave sin haberle puesto `New` | |
| Se pide `WorksheetFunction.Left` sobre un texto | |
| Se busca con `WorksheetFunction.VLookup` una clave que no está en el catálogo | |

Después, de estas seis operaciones, di qué resultado equivocado produce cada una y confirma que ninguna lanza un error.

Ordenar la columna de importes sin incluir el resto de la base. Recorrer con `For Each` un rango filtrado. Escribir el encabezado del criterio de un filtro avanzado con otro nombre. Insertar subtotales sin haber ordenado antes. Leer una dinámica sin refrescarla. Revisar `Err.Number` tres renglones después de la instrucción que podía fallar.

### 17.2 · Aplicar

**Reparar una macro que corre y miente**

Esta macro corre de principio a fin, no marca ningún error, y el reporte que produce está mal en cinco cosas distintas.

```vba
Sub ReportePendiente()
    Application.Calculation = xlCalculationManual

    Dim fila As Long
    For fila = 2 To 9
        If Cells(fila, 4).Value < 50000 Then
            Rows(fila).Delete
        End If
    Next fila

    Range("D2:D9").Sort Key1:=Range("D2"), _
                        Order1:=xlAscending, Header:=xlNo

    For fila = 2 To 9
        Cells(fila, 5).Value = WorksheetFunction.VLookup( _
            Cells(fila, 1).Value, Range("Catalogo"), 2, False)
    Next fila
End Sub
```

Entrega la versión corregida y una tabla de cinco renglones que, por cada defecto, diga qué hace mal, qué resultado produce y de qué semana del curso viene la corrección. La versión corregida tiene que servir con una base de cualquier tamaño.

### 17.3 · Integrar

**El examen: una base sucia y un reporte que se defiende**

Te entregan un libro con una hoja `Ventas` que trae encabezados en la fila 1, un número desconocido de renglones de datos, regiones capturadas con mayúsculas disparejas y espacios de sobra, algunas filas completamente vacías, folios repetidos y algunos importes en blanco. También trae la hoja `Claves`, con el rango con nombre `Catalogo` que relaciona cada vendedor con su gerente, y en la que falta un vendedor.

Entrega un módulo con una maestra y los procedimientos que hagan falta, uno por tarea, que deje el libro así.

La base limpia: regiones parejas, sin filas vacías, sin folios repetidos, ordenada por región ascendente y por importe descendente dentro de cada región.

Una columna de nivel, calculada con la tabla de la semana 8, escrita por una función tuya que también se pueda usar desde una celda.

Una columna de gerente, traída del catálogo con una búsqueda que no detenga la macro y que marque como `sin catálogo` al vendedor que falta.

Una hoja `Resumen` con una tabla dinámica creada desde código, con la región en los renglones y el importe en los datos, tomando como origen una tabla para que crezca sola, más una gráfica de columnas.

Un manejador de errores en la maestra que deje el cálculo en automático, el redibujado encendido y los eventos prendidos aunque algo truene, y la protección con `UserInterfaceOnly` repuesta al abrir el libro.

Ninguna dirección de celda escrita a mano dentro de los ciclos. En el reporte escrito, explica una decisión de diseño que tomaste y qué alternativa descartaste, y señala cuál de los procedimientos falla en silencio si le quitas la línea que calcula la última fila.
