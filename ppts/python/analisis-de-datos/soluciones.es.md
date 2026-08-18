# Soluciones · Análisis de Datos · TIA502

Documento del profesor. Trae, por cada ejercicio, la solución corrida, la salida exacta que produce, la rúbrica de diez puntos y el error que más aparece al calificar. Los programas de las semanas 1 a 14 corren con Python 3.13 y la biblioteca estándar. Los de las semanas 15 a 17 necesitan pandas, y los de la 16 y la 17 además matplotlib y seaborn. Las corridas con `input` se muestran como se ven en pantalla, con el dato escrito a un lado del mensaje.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Solución**

```text
ene 128400
jun 134050
54850
6
```

`ventas[3]` es el cuarto dato de la columna, así que corresponde a la fila 5 de la hoja: la 1 es el encabezado y los datos empiezan en la 2. `print(meses[6])` lanza `IndexError`, porque la lista tiene seis elementos y el último índice válido es 5.

**Salida**

```text
ene 128400
jun 134050
54850
6
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas, en orden y con los dos valores donde van dos | 4 |
| La resta de la tercera línea da 54850 | 2 |
| La fila de la hoja está bien ubicada y se explica el corrimiento | 2 |
| `IndexError` nombrado, con el último índice válido | 2 |

**Error que más se ve**

Contestar que `ventas[3]` es la fila 3 de la hoja. Lo delata que la explicación no menciona el encabezado ni el índice cero.

### 01.2 · Aplicar

**Solución**

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [128400, 96750, 143200, 118900, 151600, 134050]

total = sum(ventas)
promedio = total / len(ventas)
mejor = meses[ventas.index(max(ventas))]
diferencia = max(ventas) - promedio

print(f"Venta del semestre: {total:,.0f}")
print(f"Promedio mensual: {promedio:,.2f}")
print(f"Mejor mes: {mejor} con {max(ventas):,.0f}")
print(f"El mejor mes rebasa el promedio por {diferencia:,.2f}")
```

**Salida**

```text
Venta del semestre: 772,900
Promedio mensual: 128,816.67
Mejor mes: may con 151,600
El mejor mes rebasa el promedio por 22,783.33
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Total y promedio correctos, calculados con `sum` y `len` | 3 |
| El mejor mes sale de `index` sobre `max`, no escrito a mano | 3 |
| La diferencia contra el promedio es correcta | 2 |
| Los cuatro formatos aplicados donde el enunciado los pide | 2 |

**Error que más se ve**

Escribir `mejor = "may"` porque ya se vio la lista. Lo delata que el programa siga diciendo may si se cambia una cifra de la lista.

### 01.3 · Integrar

**Solución**

```python
productos = ["Cuaderno profesional", "Bolígrafo negro",
             "Carpeta de argollas", "Marcador permanente"]
unidades = [1840, 5210, 960, 2375]
precios = [38.50, 9.90, 74.00, 22.50]

posicion = unidades.index(max(unidades))
lider = productos[posicion]
importe = unidades[posicion] * precios[posicion]
participacion = unidades[posicion] / sum(unidades) * 100

print(f"Producto líder: {lider}")
print(f"Piezas vendidas: {unidades[posicion]:,}")
print(f"Importe del líder: {importe:,.2f}")
print(f"Participación en piezas: {participacion:.1f} %")
print(f"Piezas totales del mes: {sum(unidades):,}")
```

**Salida**

```text
Producto líder: Bolígrafo negro
Piezas vendidas: 5,210
Importe del líder: 51,579.00
Participación en piezas: 50.2 %
Piezas totales del mes: 10,385
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La posición se calcula una vez y sirve para las tres listas | 3 |
| Importe correcto, con el precio que le toca a esa posición | 2 |
| Participación correcta, con un decimal y su símbolo | 2 |
| Los cinco renglones con etiqueta legible | 2 |
| El programa sigue siendo correcto si cambia el líder | 1 |

**Error que más se ve**

Calcular la posición tres veces, una por lista, con `unidades.index(max(unidades))` repetido. Funciona y delata que no se entendió que las tres listas comparten la misma posición.

---

## Semana 02 · Diseño de algoritmos

### 02.1 · Reconocer

**Solución**

| Cliente | Condiciones evaluadas | Cuál se cumple | descuento |
|---|---|---|---|
| Abarrotes La Paz | ¿adeudo > 0? No. ¿620,000 ≥ 500,000 y 36 ≥ 24? Sí | La segunda | 0.12 |
| Ferretería Muñoz | ¿adeudo > 0? Sí | La primera | 0 |
| Papelera Bruno | ¿adeudo > 0? No. ¿200,000 ≥ 500,000? No. ¿200,000 ≥ 200,000? Sí | La tercera | 0.06 |

Ferretería Muñoz compra más que La Paz y no cobra descuento, porque el adeudo se revisa primero y ninguna condición posterior se evalúa. Papelera Bruno cae en la tercera rama por el valor exacto de la frontera: el operador incluye el límite.

La propiedad que se rompería con «SI el cliente es importante» es la precisión. Quién es importante lo decide quien lea el algoritmo, y dos personas van a decidir distinto sobre el mismo cliente. Al romperse la precisión se cae también lo definido, porque los mismos datos dejan de producir el mismo resultado.

**Salida**

La entrega es la tabla de traza de arriba, con los tres descuentos: 0.12, 0 y 0.06, más el párrafo de la propiedad.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres descuentos correctos | 3 |
| La traza muestra qué condiciones se evaluaron y cuáles no | 3 |
| Se nombra la precisión y se explica con el caso, no en abstracto | 3 |
| Se menciona que Ferretería Muñoz nunca llega a la segunda rama | 1 |

**Error que más se ve**

Darle 0.12 a Ferretería Muñoz porque cumple los dos montos. Lo delata que la traza no incluye el renglón del adeudo.

### 02.2 · Aplicar

**Solución**

```text
INICIO
    LEER sueldo, antiguedad, evaluacion, faltas

    SI antiguedad < 6 ENTONCES
        bono = 0
    SI NO SI evaluacion >= 4.5 ENTONCES
        bono = sueldo * 0.15
    SI NO SI evaluacion >= 3.5 ENTONCES
        bono = sueldo * 0.08
    SI NO
        bono = 1200

    SI faltas > 3 ENTONCES
        bono = bono / 2

    ESCRIBIR bono
FIN
```

El descuento por faltas va fuera de la cadena de decisiones, después de que el bono ya quedó calculado. Meterlo dentro obligaría a repetirlo en las cuatro ramas.

El diagrama de flujo lleva un óvalo de inicio, un paralelogramo de lectura de los cuatro datos, tres rombos encadenados con sus salidas sí y no etiquetadas, cuatro rectángulos de asignación, un rombo más para las faltas, un rectángulo para la división y un paralelogramo de escritura antes del óvalo de fin.

Traza de Marina Cortés: antigüedad 8, así que no entra a la primera rama. Evaluación 4.6, entra a la segunda: bono = 24,500 × 0.15 = 3,675. Faltas 4, mayor que 3: bono = 3,675 / 2 = 1,837.50.

**Salida**

```text
bono = 1837.50
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro ramas del bono, en el orden correcto | 3 |
| El descuento por faltas queda fuera de la cadena, aplicado una sola vez | 2 |
| El diagrama usa cada símbolo para lo que le corresponde | 2 |
| Los rombos traen sus dos salidas etiquetadas y ambas llevan a algún lado | 2 |
| La traza de Marina Cortés llega a 1,837.50 | 1 |

**Error que más se ve**

Escribir el descuento por faltas dentro de cada rama y olvidarlo en una. Lo delata que el pseudocódigo tenga cuatro divisiones entre dos en lugar de una.

### 02.3 · Integrar

**Solución**

Una descomposición defendible parte el cierre en tres piezas:

1. **Calcular percepciones.** Recibe sueldo base, días laborados, horas extra y comisiones. Entrega el total de percepciones del periodo.
2. **Calcular deducciones.** Recibe el total de percepciones, los préstamos vigentes y el porcentaje de retención. Entrega el total de deducciones.
3. **Calcular neto y generar el recibo.** Recibe percepciones y deducciones. Entrega el neto a pagar y el desglose.

Cada pieza se puede probar sola porque su entrada y su salida están dichas. La segunda no necesita saber cómo se calcularon las percepciones, solo cuánto suman.

Pseudocódigo de la primera pieza:

```text
INICIO
    LEER sueldo_base, dias_laborados, horas_extra, comisiones

    sueldo_diario = sueldo_base / 30
    proporcional = sueldo_diario * dias_laborados

    SI horas_extra > 9 ENTONCES
        pago_extra = sueldo_diario / 8 * (9 * 2 + (horas_extra - 9) * 3)
    SI NO
        pago_extra = sueldo_diario / 8 * horas_extra * 2

    percepciones = proporcional + pago_extra + comisiones

    ESCRIBIR percepciones
FIN
```

Caso límite: un empleado que ingresó a media quincena y trae cero días laborados por incapacidad. La primera versión, la que multiplicaba el sueldo diario por 15 sin leer los días, le pagaba la quincena completa. La versión de arriba lo resuelve leyendo los días como dato de entrada, y con cero días el proporcional da cero sin ningún caso especial.

**Salida**

La entrega es la descomposición en tres piezas con sus entradas y salidas, el pseudocódigo de una de ellas, y el párrafo del caso límite con el resultado equivocado que producía.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Tres subproblemas con nombre, entrada y salida declaradas | 3 |
| Las piezas son independientes: ninguna necesita el interior de otra | 2 |
| El pseudocódigo elegido tiene al menos dos decisiones y termina | 2 |
| El caso límite rompía la versión anterior y se dice cómo | 2 |
| La prueba del intercambio se realizó y se reporta el resultado | 1 |

**Error que más se ve**

Partir el proceso en tres pasos que en realidad son uno solo escrito en tres renglones, como leer, calcular e imprimir. Lo delata que ninguna de las tres piezas se pueda probar sin las otras dos.

---

## Semana 03 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**Solución**

```python
presupuesto = 250000
presupuesto = presupuesto - 40000
presupuesto = presupuesto * 2
presupuesto = presupuesto + 15000

print(presupuesto)
```

Cada línea lee el valor que dejó la anterior y lo guarda encima: 250000, 210000, 420000, 435000.

| Línea | Error | Dónde lo reporta |
|---|---|---|
| `Print(presupuesto)` | `NameError`, porque `Print` con mayúscula no existe | En esa misma línea, al ejecutarla |
| `print("Presupuesto: , presupuesto)` | `SyntaxError`, la comilla de cierre nunca aparece | En esa línea o en la siguiente |
| `print(presupuesto` | `SyntaxError`, falta cerrar el paréntesis | Casi siempre en la línea de abajo |

**Salida**

```text
435000
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El resultado es 435000 | 3 |
| Se explica que el signo igual guarda y no compara | 2 |
| Los tres tipos de error nombrados correctamente | 3 |
| Se dice que un paréntesis sin cerrar se reclama una línea abajo | 2 |

**Error que más se ve**

Contestar 250000 porque «la primera línea es la que define la variable». Lo delata que la respuesta no incluye ninguna traza intermedia.

### 03.2 · Aplicar

**Solución**

```python
# Nómina quincenal del área de ventas.
from statistics import mean

sueldos = [23200, 42800, 82700, 24500, 31600, 28900]

promedio = mean(sueldos)
mayor = max(sueldos)

print("Empleados:", len(sueldos))
print("Sueldo promedio:", promedio)
print("Sueldo mayor:", mayor)
```

**Salida**

```text
Empleados: 6
Sueldo promedio: 38950
Sueldo mayor: 82700
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El programa corre y muestra los tres renglones | 3 |
| El promedio sale de `mean`, importado arriba del archivo | 3 |
| Comentario de encabezado presente y útil | 2 |
| Los nombres de las variables dicen qué guardan | 2 |

**Error que más se ve**

Importar `statistics` dentro del cuerpo del programa, entre los cálculos. Corre igual, y esconde de qué depende el archivo.

### 03.3 · Integrar

**Solución**

```python
# Cierre de caja de la sucursal Reforma.
from statistics import mean

dias = ["lun", "mar", "mié", "jue", "vie", "sáb"]
ingresos = [18400, 15750, 21300, 19850, 27600, 34200]

promedio = mean(ingresos)
mejor = dias[ingresos.index(max(ingresos))]

print("Días registrados:", len(ingresos))
print("Ingreso de la semana:", sum(ingresos))
print("Ingreso promedio:", promedio)
print("Mejor día:", mejor)
```

| Problema | Mensaje | Corrección |
|---|---|---|
| `Print` con mayúscula | `NameError: name 'Print' is not defined` | Escribirlo en minúsculas |
| Paréntesis sin cerrar en esa misma línea | `SyntaxError`, reportado en la línea siguiente | Cerrar el paréntesis |
| Falta la coma antes de `promedio` | `SyntaxError: invalid syntax` | Separar los argumentos con coma |
| `mejor` se calcula y nunca se imprime | No da error | Agregar el cuarto `print` |

**Salida**

```text
Días registrados: 6
Ingreso de la semana: 137100
Ingreso promedio: 22850
Mejor día: sáb
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El programa corregido corre y muestra los cuatro renglones | 3 |
| Los tres errores de sintaxis identificados con su tipo | 3 |
| El cuarto problema se reconoce como cálculo sin salida, no como error | 2 |
| La tabla dice dónde reporta Python cada error | 2 |

**Error que más se ve**

Reportar tres problemas en lugar de cuatro. El cálculo que no se imprime no lanza nada, y por eso es el que se pasa de largo.

---

## Semana 04 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Solución**

```text
179
4
32
12500
<class 'float'>
```

La cuarta línea concatena porque `precio` es texto: pega el `"0"` al final de `"1250"`. La quinta dice `float` porque la división con una sola diagonal siempre devuelve decimal, aunque los dos operandos sean enteros y la división salga exacta.

**Salida**

```text
179
4
32
12500
<class 'float'>
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas correctas | 5 |
| Se explica la concatenación con el tipo de `precio` | 3 |
| Se explica que la división simple siempre devuelve `float` | 2 |

**Error que más se ve**

Contestar 1260 en la cuarta línea. Lo delata que la explicación hable de suma y no de texto pegado.

### 04.2 · Aplicar

**Solución**

```python
unidades = 4300
por_caja = 24
precio_texto = "18.75"
flete = 3200

precio = float(precio_texto)
cajas_completas = unidades // por_caja
sueltas = unidades % por_caja
costo_mercancia = unidades * precio

costo_por_caja_mal = costo_mercancia / cajas_completas + flete
costo_por_caja_bien = (costo_mercancia + flete) / cajas_completas

print("Cajas completas:", cajas_completas)
print("Piezas sueltas:", sueltas)
print("Costo de la mercancía:", round(costo_mercancia, 2))
print("Sin paréntesis:", round(costo_por_caja_mal, 2))
print("Con paréntesis:", round(costo_por_caja_bien, 2))
print(type(precio), type(cajas_completas))
```

La versión con paréntesis es la que contesta cuánto cuesta poner una caja en el andén: reparte el flete entre las 179 cajas. La otra le suma el flete completo a cada caja, y por eso da un número casi ocho veces más grande sin marcar ningún error.

**Salida**

```text
Cajas completas: 179
Piezas sueltas: 4
Costo de la mercancía: 80625.0
Sin paréntesis: 3650.42
Con paréntesis: 468.3
<class 'float'> <class 'int'>
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Cajas completas y sueltas con `//` y `%` | 3 |
| El precio se convierte con `float` antes de multiplicar | 2 |
| Las dos versiones del costo por caja, con sus cifras | 2 |
| La explicación dice cuál contesta la pregunta del andén y por qué | 2 |
| Los dos tipos impresos al final | 1 |

**Error que más se ve**

Multiplicar `unidades * precio_texto` sin convertir. No lanza error: repite el texto 4,300 veces y llena la pantalla.

### 04.3 · Integrar

**Solución**

```python
proveedores = ["Papelera del Centro", "Insumos Aurora",
               "Distribuidora Sol", "Comercial Bravo", "Grupo Nardo"]
costos = [18420.50, 9375.00, 24680.75, 6120.25, 15302.50]
tasa_iva = 0.16
piezas = 3400
piezas_por_tarima = 48

subtotal = sum(costos)
total = subtotal
total *= (1 + tasa_iva)
costo_pieza = total / piezas
tarimas = piezas // piezas_por_tarima
sobrantes = piezas % piezas_por_tarima

print(f"Proveedores en la orden: {len(proveedores)}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Total con IVA: ${total:,.2f}")
print(f"Costo por pieza: ${costo_pieza:,.2f}")
print(f"Tarimas completas: {tarimas}, sobrantes: {sobrantes}")
print(type(subtotal), type(tarimas))
```

**Salida**

```text
Proveedores en la orden: 5
Subtotal: $73,899.00
Total con IVA: $85,722.84
Costo por pieza: $25.21
Tarimas completas: 70, sobrantes: 40
<class 'float'> <class 'int'>
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Subtotal con `sum` y total con `*=` sobre una variable | 3 |
| Costo por pieza calculado sobre el total con IVA | 2 |
| Tarimas y sobrantes con las dos divisiones | 2 |
| Formato de moneda con miles y dos decimales | 2 |
| Los dos tipos impresos y correctos | 1 |

**Error que más se ve**

Escribir `total = subtotal * 1.16` en una sola línea. Da el mismo número y se salta el operador que el enunciado pedía, que es el que después evita repetir la tasa en tres lugares.

---

## Semana 05 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Solución**

```text
248,910
2.7%
$41,250.50
Alcance: {impresiones:,}
|     248,910|
```

A la cuarta cadena le falta la `f` de apertura, así que las llaves se imprimen tal cual. Python no lo marca porque una cadena con llaves es una cadena válida: el programa hace exactamente lo que dice, solo que no es lo que su autor quería. La quinta reserva doce espacios y alinea a la derecha, de ahí los cinco espacios antes del número.

**Salida**

```text
248,910
2.7%
$41,250.50
Alcance: {impresiones:,}
|     248,910|
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas, con comas y símbolos donde van | 5 |
| El porcentaje redondeado a un decimal, no truncado | 1 |
| Se identifica la `f` faltante y se explica por qué no es error | 2 |
| El relleno de la última línea es de cinco espacios | 2 |

**Error que más se ve**

Contestar `0.0%` en la segunda línea. Lo delata que el alumno olvidó que el código de porcentaje ya multiplica por cien.

### 05.2 · Aplicar

**Solución**

```python
campana = input("Nombre de la campaña: ")
impresiones = int(input("Impresiones: "))
clics = int(input("Clics: "))
inversion = float(input("Inversión en pesos: "))

conversion = clics / impresiones
costo_por_clic = inversion / clics
costo_por_mil = inversion / impresiones * 1000

print(f"Campaña: {campana}")
print(f"Impresiones: {impresiones:,}")
print(f"Conversión: {conversion:.2%}")
print(f"Costo por clic: ${costo_por_clic:,.2f}")
print(f"Costo por mil impresiones: ${costo_por_mil:,.2f}")
```

**Salida**

```text
Nombre de la campaña: Verano Bajío
Impresiones: 248910
Clics: 6795
Inversión en pesos: 52400
Campaña: Verano Bajío
Impresiones: 248,910
Conversión: 2.73%
Costo por clic: $7.71
Costo por mil impresiones: $210.52
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro `input` con mensaje, y el nombre sin convertir | 2 |
| `int` y `float` envolviendo al `input`, no aplicados después | 3 |
| Las tres métricas correctas | 3 |
| Miles, porcentaje y moneda aplicados donde corresponde | 2 |

**Error que más se ve**

Convertir después de leer, con una línea aparte que reasigna la variable. Aquí funciona, y en cuanto haya una operación entre la lectura y la conversión el resultado sale mal sin avisar.

### 05.3 · Integrar

**Solución**

```python
semana = input("Semana: ")
ingresos = float(input("Ingresos de la semana: "))
egresos = float(input("Egresos de la semana: "))
clientes = int(input("Clientes atendidos: "))

saldo = ingresos - egresos
margen = saldo / ingresos
ticket = ingresos / clientes
diario = saldo / 7

print(f"Flujo de la semana {semana}")
print(f"{'Ingresos':<22}{ingresos:>14,.2f}")
print(f"{'Egresos':<22}{egresos:>14,.2f}")
print(f"{'Saldo':<22}{saldo:>14,.2f}")
print(f"{'Margen':<22}{margen:>14.1%}")
print(f"{'Ticket promedio':<22}{ticket:>14,.2f}")
print(f"{'Saldo por día':<22}{diario:>14,.2f}")
```

**Salida**

```text
Semana: 14
Ingresos de la semana: 186400
Egresos de la semana: 143750
Clientes atendidos: 612
Flujo de la semana 14
Ingresos                  186,400.00
Egresos                   143,750.00
Saldo                      42,650.00
Margen                         22.9%
Ticket promedio               304.58
Saldo por día               6,092.86
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro entradas con su tipo correcto | 2 |
| Saldo, margen, ticket y saldo por día correctos | 3 |
| Las columnas alineadas con los anchos que pide el enunciado | 3 |
| El margen en porcentaje y el dinero con dos decimales | 2 |

**Error que más se ve**

Convertir la semana a entero. No rompe nada aquí, y en cuanto alguien capture «14 bis» el programa se cae en la primera línea. Lo que no se opera no se convierte.

---

## Semana 06 · Estructuras de selección

### 06.1 · Reconocer

**Solución**

```text
18.0% · Alta
```

| rotacion | Rama que gana | Salida |
|---|---|---|
| 0.25 | La primera, porque el operador incluye el límite | `25.0% · Crítica` |
| 0.099 | Ninguna de las tres, cae en el `else` | `9.9% · Baja` |
| 0.30 | La primera | `30.0% · Crítica` |

Con `>` en lugar de `>=` en el segundo `elif`, un área que rote exactamente 18 % dejaría de ser Alta y bajaría a Normal, que es la clasificación que dispara acciones distintas en recursos humanos.

**Salida**

```text
18.0% · Alta
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La línea exacta, con el porcentaje formateado | 3 |
| Los tres casos de la tabla correctos | 3 |
| Se explica que el 0.25 entra por la primera rama, no por la segunda | 2 |
| El efecto de cambiar `>=` por `>` está dicho con el caso del 18 % | 2 |

**Error que más se ve**

Clasificar el 0.25 como Alta porque «también cumple la segunda condición». Cumple las dos, y la primera que se cumple es la única que corre.

### 06.2 · Aplicar

**Solución**

```python
proveedor = input("Proveedor: ")
cumplimiento = float(input("Entregas a tiempo (0 a 1): "))

if cumplimiento >= 0.95:
    categoria = "Preferente"
elif cumplimiento >= 0.85:
    categoria = "Confiable"
elif cumplimiento >= 0.70:
    categoria = "En observación"
else:
    categoria = "En revisión de contrato"

print(f"{proveedor}: {cumplimiento:.1%} · {categoria}")
```

**Salida**

```text
Proveedor: Insumos Aurora
Entregas a tiempo (0 a 1): 0.96
Insumos Aurora: 96.0% · Preferente

Proveedor: Distribuidora Sol
Entregas a tiempo (0 a 1): 0.85
Distribuidora Sol: 85.0% · Confiable

Proveedor: Comercial Bravo
Entregas a tiempo (0 a 1): 0.62
Comercial Bravo: 62.0% · En revisión de contrato
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro categorías, en orden de más exigente a menos | 4 |
| Las categorías son excluyentes: ningún proveedor cae en dos | 2 |
| Las tres corridas entregadas, incluida la de la frontera | 2 |
| El renglón de salida con nombre, porcentaje y categoría | 2 |

**Error que más se ve**

Escribir las condiciones de menor a mayor. Con ese orden, Insumos Aurora sale «En observación», porque 0.96 también es mayor o igual a 0.70 y esa rama se evalúa primero.

### 06.3 · Integrar

**Solución**

```python
centro = input("Centro de costo: ")
presupuesto = float(input("Presupuesto del mes: "))
ejercido = float(input("Gasto ejercido: "))

desviacion = (ejercido - presupuesto) / presupuesto

if desviacion > 0.10:
    estado = "Sobregiro"
elif desviacion >= 0:
    estado = "Al límite"
elif desviacion >= -0.15:
    estado = "Dentro de rango"
else:
    estado = "Subejercicio"

print(f"Centro de costo: {centro}")
print(f"Presupuesto: ${presupuesto:,.2f}")
print(f"Ejercido: ${ejercido:,.2f}")
print(f"Desviación: {desviacion:.1%}")
print(f"Estado: {estado}")
```

Un sobregiro del 8.5 % no entra en la primera categoría porque la política puso la frontera del sobregiro en más de 10 %, no en más de cero. Gastar por encima del presupuesto sin rebasar ese margen es lo que la política llama estar al límite.

**Salida**

```text
Centro de costo: Logística
Presupuesto del mes: 480000
Gasto ejercido: 521000
Centro de costo: Logística
Presupuesto: $480,000.00
Ejercido: $521,000.00
Desviación: 8.5%
Estado: Al límite
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La desviación se calcula sobre el presupuesto, no sobre el ejercido | 2 |
| Las cuatro categorías en el orden correcto | 3 |
| Los negativos se manejan bien: el `-0.15` está donde va | 2 |
| Los cinco renglones con formato de moneda y porcentaje | 2 |
| La explicación de la frontera del 10 % | 1 |

**Error que más se ve**

Dividir entre el ejercido. Da 7.9 % en lugar de 8.5 % y el estado sale igual, así que el error sobrevive a la revisión rápida.

---

## Semana 07 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**Solución**

```text
Plaza consolidada
False
True
True
True
```

En `region == "Norte" or "Occidente"`, Python evalúa dos cosas por separado: la comparación, que da `False`, y la cadena `"Occidente"`, que al no estar vacía cuenta como verdadera. El `or` se queda con la segunda y la condición siempre se cumple, sin importar la región. La versión correcta repite la variable o usa pertenencia:

```python
if region in ["Norte", "Occidente"]:
    print("Plaza consolidada")
else:
    print("Plaza en desarrollo")
```

**Salida**

```text
Plaza consolidada
False
True
True
True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas correctas | 4 |
| Se explica que la cadena no vacía se evalúa como verdadera | 3 |
| La versión corregida usa `in` o repite la comparación completa | 3 |

**Error que más se ve**

Contestar «Plaza en desarrollo» porque Bajío no es ninguna de las dos. Es el resultado que uno esperaría leyendo la condición en voz alta, y es justo por eso que el error sobrevive meses en un archivo.

### 07.2 · Aplicar

**Solución**

```python
GIROS_ELEGIBLES = ["Comercio", "Manufactura", "Servicios"]

nombre = input("Cliente: ")
ingreso = float(input("Ingreso mensual comprobable: "))
antiguedad = int(input("Antigüedad del negocio en meses: "))
giro = input("Giro: ")
buro = input("¿Historial limpio? (si/no): ")

historial_limpio = buro == "si"

if (ingreso >= 25000 and antiguedad >= 24
        and giro in GIROS_ELEGIBLES and historial_limpio):
    resultado = "Aprobado"
elif ingreso >= 60000 and historial_limpio:
    resultado = "Aprobado por ingreso"
elif not historial_limpio:
    resultado = "Rechazado por historial"
else:
    resultado = "Rechazado"

print(f"{nombre}: {resultado}")
```

**Salida**

```text
Cliente: Abarrotes La Paz
Ingreso mensual comprobable: 31500
Antigüedad del negocio en meses: 36
Giro: Comercio
¿Historial limpio? (si/no): si
Abarrotes La Paz: Aprobado

Cliente: Taller Mecánico Rueda
Ingreso mensual comprobable: 72000
Antigüedad del negocio en meses: 14
Giro: Servicios
¿Historial limpio? (si/no): si
Taller Mecánico Rueda: Aprobado por ingreso

Cliente: Constructora Zafiro
Ingreso mensual comprobable: 84000
Antigüedad del negocio en meses: 60
Giro: Construcción
¿Historial limpio? (si/no): no
Constructora Zafiro: Rechazado por historial
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La primera regla une sus cuatro condiciones con `and` | 3 |
| Los giros viven en una lista y se consultan con `in` | 2 |
| El orden de las reglas respeta el del enunciado | 2 |
| Las tres corridas entregadas y correctas | 2 |
| El resultado se guarda en una variable y se imprime una sola vez | 1 |

**Error que más se ve**

Poner la regla del ingreso alto antes que la del historial. Constructora Zafiro sale «Aprobado por ingreso» y el rechazo por buró se pierde, que es exactamente el caso que la política quería atrapar.

### 07.3 · Integrar

**Solución**

```python
CRITICOS = ["Insumos Aurora", "Grupo Nardo"]

proveedor = input("Proveedor: ")
contrato_vigente = input("¿Contrato vigente? (si/no): ") == "si"
cumplimiento = float(input("Entregas a tiempo (0 a 1): "))

if contrato_vigente:
    if cumplimiento >= 0.95:
        accion = "Ampliar volumen"
    elif cumplimiento >= 0.85:
        accion = "Mantener volumen"
    else:
        accion = "Auditar y reducir volumen"
else:
    accion = "Renovar contrato antes de evaluar"

if proveedor in CRITICOS and cumplimiento < 0.85:
    alerta = "Buscar segunda fuente"
else:
    alerta = "Sin alerta"

print(f"{proveedor}: {cumplimiento:.0%} · {accion}")
print(f"Alerta: {alerta}")
```

El anidado de la acción gana algo real: si no hay contrato, el cumplimiento no sirve para decidir nada y las tres categorías no se evalúan. La alerta es distinta: sus dos condiciones se pueden preguntar siempre, y por eso van unidas con `and` en un solo nivel. Escrita anidada quedaría así:

```python
if proveedor in CRITICOS:
    if cumplimiento < 0.85:
        alerta = "Buscar segunda fuente"
    else:
        alerta = "Sin alerta"
else:
    alerta = "Sin alerta"
```

Las dos versiones dan lo mismo en los cuatro casos posibles. La primera se lee mejor porque «Sin alerta» aparece una sola vez: en la anidada está escrito dos veces, y quien cambie una y olvide la otra deja el programa con dos comportamientos distintos.

**Salida**

```text
Proveedor: Insumos Aurora
¿Contrato vigente? (si/no): si
Entregas a tiempo (0 a 1): 0.82
Insumos Aurora: 82% · Auditar y reducir volumen
Alerta: Buscar segunda fuente

Proveedor: Distribuidora Sol
¿Contrato vigente? (si/no): no
Entregas a tiempo (0 a 1): 0.97
Distribuidora Sol: 97% · Renovar contrato antes de evaluar
Alerta: Sin alerta
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El anidado de la acción tiene la pregunta del contrato afuera | 3 |
| Las tres categorías internas, en orden y excluyentes | 2 |
| La alerta combina pertenencia y comparación con `and` | 2 |
| Las dos corridas entregadas | 1 |
| El argumento compara las dos versiones por legibilidad, no por gusto | 2 |

**Error que más se ve**

Preguntar por el cumplimiento antes que por el contrato. Distribuidora Sol sale «Ampliar volumen» con un contrato vencido, que es una recomendación que nadie puede ejecutar.

---

## Semana 08 · Repetición · Primer parcial

### 08.1 · Reconocer

**Solución**

```text
3
7
11
5 0
```

`range(3, 12, 4)` arranca en 3 y avanza de cuatro en cuatro sin llegar al 12, así que produce 3, 7 y 11.

| Vuelta | Fondo al entrar | ¿Fondo ≥ 96,000? | Fondo al salir | mes |
|---|---|---|---|---|
| 4 | 192,000 | Sí | 96,000 | 4 |
| 5 | 96,000 | Sí | 0 | 5 |
| – | 0 | No | 0 | 5 |

Con estos datos, `fondo > 0` daría el mismo resultado, porque 480,000 es múltiplo exacto de 96,000. La diferencia aparece con un fondo que no divide parejo: `fondo > 0` deja entrar una vuelta más y termina con el fondo en negativo, que es un mes que en realidad no se puede pagar.

**Salida**

```text
3
7
11
5 0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres valores del `range`, sin incluir el 11 más cuatro | 3 |
| La última línea es `5 0` | 2 |
| La traza muestra que la condición se revisa antes de cada vuelta | 3 |
| La respuesta sobre `fondo > 0` menciona el caso no exacto | 2 |

**Error que más se ve**

Contestar que el `range` produce cuatro valores porque 11 más 4 es 15 y «todavía cabe». El tope no se incluye y el 15 ya lo rebasa.

### 08.2 · Aplicar

**Solución**

```python
sucursales = ["Reforma", "Satélite", "Valle", "Chapalita", "Mitras"]
bajas = [7, 12, 4, 9, 15]
plantilla = [86, 140, 62, 108, 125]

for i in range(len(sucursales)):
    rotacion = bajas[i] / plantilla[i]
    print(f"{sucursales[i]:<12}{bajas[i]:>4}{plantilla[i]:>6}{rotacion:>9.1%}")

print(f"{'Global':<12}{sum(bajas):>4}{sum(plantilla):>6}"
      f"{sum(bajas) / sum(plantilla):>9.1%}")
```

**Salida**

```text
Reforma        7    86     8.1%
Satélite      12   140     8.6%
Valle          4    62     6.5%
Chapalita      9   108     8.3%
Mitras        15   125    12.0%
Global        47   521     9.0%
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El ciclo recorre con `range(len(...))` y sirve para cualquier largo | 3 |
| Las cinco rotaciones correctas | 2 |
| El global divide suma entre suma, no promedia las cinco | 3 |
| Los anchos de columna y el porcentaje con un decimal | 2 |

**Error que más se ve**

Calcular el global como el promedio de los cinco porcentajes. Da 8.7 % en lugar de 9.0 %, y la diferencia crece en cuanto las plantillas son de tamaños distintos.

### 08.3 · Integrar

**Solución**

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ingresos = [412000, 388500, 455200, 401800, 372900, 468300]
egresos = [398400, 401200, 430600, 418500, 395700, 402100]

print(f"{'Mes':<6}{'Ingresos':>12}{'Egresos':>12}{'Saldo':>12}  Estado")

for i in range(len(meses)):
    saldo = ingresos[i] - egresos[i]

    if saldo >= 0:
        estado = "Superávit"
    else:
        estado = "Déficit"

    print(f"{meses[i]:<6}{ingresos[i]:>12,}{egresos[i]:>12,}"
          f"{saldo:>12,}  {estado}")

print(f"{'Total':<6}{sum(ingresos):>12,}{sum(egresos):>12,}"
      f"{sum(ingresos) - sum(egresos):>12,}")

fondo = 250000
deficit = 22800
meses_cubiertos = 0

while fondo >= deficit:
    fondo -= deficit
    meses_cubiertos += 1

print(f"El fondo cubre {meses_cubiertos} meses de déficit "
      f"y quedan ${fondo:,} sin usar.")
```

**Salida**

```text
Mes       Ingresos     Egresos       Saldo  Estado
ene        412,000     398,400      13,600  Superávit
feb        388,500     401,200     -12,700  Déficit
mar        455,200     430,600      24,600  Superávit
abr        401,800     418,500     -16,700  Déficit
may        372,900     395,700     -22,800  Déficit
jun        468,300     402,100      66,200  Superávit
Total    2,498,700   2,446,500      52,200
El fondo cubre 10 meses de déficit y quedan $22,000 sin usar.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El `for` calcula el saldo mes por mes y lo clasifica | 3 |
| Los totales salen de `sum` sobre las listas completas | 2 |
| El `while` termina y reporta 10 meses con 22,000 restantes | 3 |
| La tabla queda alineada y las cifras llevan separador de miles | 2 |

**Error que más se ve**

Escribir el `while` con `fondo > 0`. Da 11 meses y deja el fondo en menos 800 pesos, que es un mes que la tesorería no puede pagar.

---

## Semana 09 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Solución**

```text
15302
3
True
Ninguna compra pasa por comité
```

La primera línea no imprime 73,877 porque `total = 0` está dentro del ciclo: se reinicia en cada vuelta y al terminar conserva solo la última requisición. La corrección es de una línea, sacar la inicialización antes del `for`:

```python
total = 0

for compra in compras:
    total += compra
```

El `else` del último ciclo corre porque ninguna compra rebasa los 30,000 y el `break` nunca se ejecutó. Ese es exactamente su propósito: decir «recorrí todo y no encontré nada».

**Salida**

```text
15302
3
True
Ninguna compra pasa por comité
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas correctas | 4 |
| Se explica el reinicio del acumulador dentro del ciclo | 2 |
| La corrección propuesta mueve la inicialización, no agrega un `if` | 2 |
| Se explica que el `else` del `for` depende del `break` | 2 |

**Error que más se ve**

Contestar 73877 en la primera línea porque «el ciclo suma las cinco». Suma las cinco y borra el resultado cuatro veces.

### 09.2 · Aplicar

**Solución**

```python
campanas = ["Instagram", "Meta", "Google", "TikTok", "Correo", "Display"]
clics = [5074, 3820, 6910, 1240, 2480, 7350]
inversion = [38500, 29800, 51200, 9600, 12400, 61300]

inversion_total = 0
con_volumen = 0
hay_cara = False
mejor_costo = inversion[0] / clics[0]
mejor_campana = campanas[0]

for i in range(len(campanas)):
    costo = inversion[i] / clics[i]
    inversion_total += inversion[i]

    if clics[i] > 3000:
        con_volumen += 1

    if costo > 8:
        hay_cara = True

    if costo < mejor_costo:
        mejor_costo = costo
        mejor_campana = campanas[i]

print(f"Inversión total: ${inversion_total:,}")
print(f"Campañas con más de 3,000 clics: {con_volumen}")
print(f"¿Hay alguna arriba de $8.00 por clic? {hay_cara}")
print(f"Mejor costo por clic: {mejor_campana} con ${mejor_costo:,.2f}")
print(f"Costo por clic global: ${inversion_total / sum(clics):,.2f}")
```

El costo global divide la suma de la inversión entre la suma de los clics, así que cada campaña pesa según lo que gastó. El promedio de los seis costos les da el mismo peso a Display, que se llevó 61,300 pesos, y a TikTok, que se llevó 9,600. En el comité se reporta el global, porque es el que contesta cuánto costó de verdad cada clic del trimestre.

**Salida**

```text
Inversión total: $202,800
Campañas con más de 3,000 clics: 4
¿Hay alguna arriba de $8.00 por clic? True
Mejor costo por clic: Correo con $5.00
Costo por clic global: $7.55
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Un solo recorrido contesta las cinco preguntas | 3 |
| El acumulador, el contador y la bandera están fuera del ciclo | 2 |
| La mejor campaña se arrastra con su nombre, no solo con su cifra | 2 |
| El global divide suma entre suma | 2 |
| La explicación habla de peso por inversión, no de redondeo | 1 |

**Error que más se ve**

Inicializar `mejor_costo = 0` y comparar con menor que. Ninguna campaña baja de cero, así que el mejor se queda en Instagram, que es solo el primero de la lista.

### 09.3 · Integrar

**Solución**

```python
sucursales = ["Norte", "Centro", "Occidente"]
trimestres = ["T1", "T2", "T3", "T4"]
ventas = [412000, 388000, 455000, 501000,
          298000, 331000, 305000, 362000,
          214000, 240000, 268000, 291000]

print(f"{'Sucursal':<10}{'T1':>10}{'T2':>10}{'T3':>10}{'T4':>10}{'Total':>12}")

general = 0
trimestres_fuertes = 0

for i in range(len(sucursales)):
    renglon = f"{sucursales[i]:<10}"
    subtotal = 0

    for j in range(len(trimestres)):
        venta = ventas[i * len(trimestres) + j]
        subtotal += venta
        renglon += f"{venta / 1000:>10,.0f}"

        if venta >= 400000:
            trimestres_fuertes += 1

    general += subtotal
    print(renglon + f"{subtotal / 1000:>12,.0f}")

print(f"{'General':<10}{'':>40}{general / 1000:>12,.0f}")
print(f"Trimestres arriba de 400 mil: {trimestres_fuertes} de "
      f"{len(sucursales) * len(trimestres)}")
```

**Salida**

```text
Sucursal          T1        T2        T3        T4       Total
Norte            412       388       455       501       1,756
Centro           298       331       305       362       1,296
Occidente        214       240       268       291       1,013
General                                                  4,065
Trimestres arriba de 400 mil: 3 de 12
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El ciclo interno da sus cuatro vueltas por cada vuelta del externo | 2 |
| El índice se calcula con `i * len(trimestres) + j` | 3 |
| El subtotal se reinicia por sucursal y el general no | 2 |
| Los tres totales de renglón y el general son correctos | 2 |
| El contador de trimestres fuertes da 3 de 12 | 1 |

**Error que más se ve**

Declarar `subtotal = 0` antes del ciclo externo. Los renglones salen acumulando la sucursal anterior: Centro reporta 3,052 y Occidente 4,065, y la última cifra coincide con el gran total, lo que hace que el error parezca correcto.

---

## Semana 10 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Solución**

```text
None
5400.0
```

Después de esas dos líneas el programa se detiene con `NameError: name 'base' is not defined`.

A `comision` le falta el `return`: calcula el producto y lo tira. Ya corregida imprimiría 9000.0. La tercera línea falla porque `base` nace dentro de `bono`, vive mientras la función corre y desaparece al terminar. Y `resultado + 100` lanzaría `TypeError`, porque no se puede sumar un entero a `None`.

**Salida**

```text
None
5400.0
Traceback (most recent call last):
  File "retorno.py", line 14, in <module>
    print(base)
          ^^^^
NameError: name 'base' is not defined
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `None` y 5400.0 en las dos primeras líneas | 3 |
| `NameError` nombrado, con la explicación del ámbito local | 3 |
| Se dice que `comision` corregida devolvería 9000.0 | 2 |
| `TypeError` identificado para la suma con `None` | 2 |

**Error que más se ve**

Contestar 9000.0 en la primera línea porque la función «hace la multiplicación». La hace, y sin `return` no la entrega.

### 10.2 · Aplicar

**Solución**

```python
def punto_equilibrio(costos_fijos, precio, costo_variable):
    """Devuelve cuántas unidades hay que vender para no perder ni ganar."""
    margen = precio - costo_variable

    return costos_fijos / margen


print(f"Cafetería: {punto_equilibrio(145000, 68.00, 23.00):,.2f} unidades")
print(f"Equipo médico: {punto_equilibrio(980000, 1250.00, 845.00):,.2f} unidades")
print(f"Taller: {punto_equilibrio(60000, 40.00, 20.00):,.2f} unidades")
```

Si el precio y el costo variable fueran iguales, el margen daría cero y la función lanzaría `ZeroDivisionError`. En el negocio significa que cada unidad vendida no deja un solo peso para pagar los costos fijos, así que no existe un volumen que alcance el equilibrio: el problema no es vender más, es el precio.

**Salida**

```text
Cafetería: 3,222.22 unidades
Equipo médico: 2,419.75 unidades
Taller: 3,000.00 unidades
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función devuelve y no imprime | 3 |
| Docstring que dice qué entrega | 2 |
| Las tres llamadas con sus tres resultados correctos | 3 |
| `ZeroDivisionError` nombrado y traducido al negocio | 2 |

**Error que más se ve**

Poner el `print` dentro de la función y llamarla tres veces sin guardar nada. Se ve idéntico en pantalla, y deja los tres números fuera del alcance de cualquier cálculo posterior.

### 10.3 · Integrar

**Solución**

```python
def rotacion(bajas, plantilla):
    """Devuelve el índice de rotación del periodo como proporción."""
    return bajas / plantilla


def clasificar(indice):
    """Devuelve la categoría de rotación que le corresponde al índice."""
    if indice >= 0.20:
        return "Crítica"
    elif indice >= 0.15:
        return "Alta"
    elif indice >= 0.10:
        return "Normal"
    else:
        return "Baja"


areas = ["Ventas", "Operaciones", "Administración", "Logística", "Sistemas"]
bajas = [9, 21, 3, 14, 2]
plantilla = [74, 112, 48, 96, 25]

print(f"{'Área':<16}{'Bajas':>7}{'Plantilla':>11}{'Rotación':>10}  Categoría")

for i in range(len(areas)):
    indice = rotacion(bajas[i], plantilla[i])
    print(f"{areas[i]:<16}{bajas[i]:>7}{plantilla[i]:>11}"
          f"{indice:>10.1%}  {clasificar(indice)}")

global_rotacion = rotacion(sum(bajas), sum(plantilla))
print(f"{'Empresa':<16}{sum(bajas):>7}{sum(plantilla):>11}"
      f"{global_rotacion:>10.1%}  {clasificar(global_rotacion)}")
```

El índice de la empresa no es el promedio de los cinco porque cada área aporta una plantilla distinta. Operaciones pesa 112 personas y Sistemas 25, así que el índice global se parece mucho más al de Operaciones que al de Sistemas.

**Salida**

```text
Área              Bajas  Plantilla  Rotación  Categoría
Ventas                9         74     12.2%  Normal
Operaciones          21        112     18.8%  Alta
Administración        3         48      6.2%  Baja
Logística            14         96     14.6%  Normal
Sistemas              2         25      8.0%  Baja
Empresa              49        355     13.8%  Normal
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos funciones devuelven, ninguna imprime | 3 |
| El renglón de empresa reusa las mismas dos funciones | 2 |
| Las cinco categorías correctas | 2 |
| La tabla alineada con el porcentaje a un decimal | 2 |
| La explicación del promedio ponderado | 1 |

**Error que más se ve**

Escribir la clasificación otra vez dentro del ciclo, con un `if` en lugar de llamar a `clasificar`. La tabla sale bien, y cuando cambien las fronteras habrá dos lugares que corregir y solo uno se va a corregir.

---

## Semana 11 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**Solución**

```text
13920.0
4212000
14270.0
23590 18400
```

En la segunda llamada, el 350 cae en el segundo parámetro, que es `iva`. La función calcula 12000 por 351 y devuelve 4,212,000 sin marcar nada, porque un IVA de 350 es un número perfectamente válido. Para que signifique el envío hay que nombrarlo: `costo_total(12000, envio=350)`.

El promedio queda arriba de la mediana porque el sueldo de 42,300 jala la suma y no mueve el valor de en medio. A un candidato se le dice la mediana: describe lo que gana la mitad del área, y no lo que gana el gerente.

**Salida**

```text
13920.0
4212000
14270.0
23590 18400
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas correctas | 4 |
| Se explica que el 350 cayó en `iva` por posición | 2 |
| La corrección nombra el argumento | 1 |
| La explicación de promedio contra mediana usa el sueldo alto | 2 |
| La elección de la mediana está justificada | 1 |

**Error que más se ve**

Contestar que la segunda línea lanza un error por pasar mal los argumentos. La llamada es válida, y ese es justo el problema.

### 11.2 · Aplicar

**Solución**

```python
def costo_nomina(sueldo_base, meses=12, bono=0.0, prestaciones=1.35):
    """Devuelve el costo anual de una plaza con prestaciones y bono."""
    return sueldo_base * meses * prestaciones * (1 + bono)


print(f"Plaza estándar: ${costo_nomina(18400):,.2f}")
print(f"Con aguinaldo extra: ${costo_nomina(18400, 13):,.2f}")
print(f"Con bono del 10 %: ${costo_nomina(18400, bono=0.10):,.2f}")
```

`costo_nomina(18400, 0.10)` entrega 2,484.00: el 0.10 cae en `meses`, así que calcula una décima parte de un mes. No hay error, solo un costo anual de dos mil pesos que nadie va a cuestionar en una hoja con veinte plazas.

**Salida**

```text
Plaza estándar: $298,080.00
Con aguinaldo extra: $322,920.00
Con bono del 10 %: $327,888.00
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres parámetros opcionales al final y con su valor por omisión | 3 |
| Las tres llamadas, una de ellas por nombre saltándose `meses` | 3 |
| Los tres resultados correctos | 2 |
| Se explica qué pasa con `costo_nomina(18400, 0.10)` | 2 |

**Error que más se ve**

Declarar la función como `costo_nomina(sueldo_base, bono=0.0, meses)`. Python la rechaza al leer el archivo con `SyntaxError`, antes de correr una sola línea.

### 11.3 · Integrar

**Solución**

```python
from statistics import mean, median


def resumir(etiqueta, valor):
    """Devuelve el renglón formateado de una métrica de nómina."""
    return f"{etiqueta:<22}${valor:>12,.2f}"


sueldos = [12800, 15600, 17950, 18400, 19250, 22400, 26500, 33900, 84000]
ordenados = sorted(sueldos)

print(f"Plazas del área: {len(sueldos)}")
print(resumir("Nómina mensual", sum(sueldos)))
print(resumir("Promedio", mean(sueldos)))
print(resumir("Mediana", median(sueldos)))
print(resumir("Sueldo más alto", max(sueldos)))
print(resumir("Sueldo más bajo", min(sueldos)))
print(resumir("Segundo más alto", ordenados[-2]))
print(f"El promedio queda {mean(sueldos) - median(sueldos):,.2f} arriba "
      f"de la mediana.")
```

Al director de área se le reporta la nómina mensual, $250,800.00, porque es la cifra que va contra el presupuesto. Al sindicato se le reporta la mediana, $19,250.00, porque describe lo que gana la plaza de en medio. Las dos son ciertas y salen de los mismos nueve datos: una mide cuánto cuesta el área y la otra cuánto gana una persona típica de esa área.

**Salida**

```text
Plazas del área: 9
Nómina mensual        $  250,800.00
Promedio              $   27,866.67
Mediana               $   19,250.00
Sueldo más alto       $   84,000.00
Sueldo más bajo       $   12,800.00
Segundo más alto      $   33,900.00
El promedio queda 8,616.67 arriba de la mediana.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `resumir` devuelve la cadena y no imprime | 2 |
| Las seis métricas correctas | 3 |
| El segundo más alto sale de `sorted`, con la lista original intacta | 2 |
| Los anchos de columna respetados | 1 |
| Las tres respuestas del cierre, con su justificación | 2 |

**Error que más se ve**

Reordenar la lista original en lugar de pedirle a `sorted` una copia. Todo lo demás sigue funcionando, así que nadie lo nota hasta que alguien necesita el orden en que se capturaron las plazas.

---

## Semana 12 · Listas y tuplas

### 12.1 · Reconocer

**Solución**

```text
None
[125, 210, 340, 470, 890]
6
6 0
[210, 340, 470]
890
```

`sort` ordena la lista en el lugar y devuelve `None`, por eso la primera línea no imprime nada útil. `respaldo = unidades` no copia: crea un segundo nombre para la misma lista, así que el `append` se ve desde los dos. Para que la original no se moviera había que escribir `respaldo = unidades.copy()`.

**Salida**

```text
None
[125, 210, 340, 470, 890]
6
6 0
[210, 340, 470]
890
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis líneas correctas | 4 |
| Se explica que `sort` devuelve `None` y modifica en el lugar | 2 |
| Se explica el alias y se propone `copy` | 2 |
| La rebanada excluye el índice 4 y el negativo apunta al penúltimo | 2 |

**Error que más se ve**

Contestar `[210, 340, 470, 890]` en la penúltima línea. El primer índice entra y el segundo no, y por eso una rebanada de 1 a 4 devuelve tres elementos.

### 12.2 · Aplicar

**Solución**

```python
inventario = [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]

print("Al inicio:", inventario)

ordenado = inventario.copy()
ordenado.sort()
ordenado.reverse()

print("Tres SKU con más piezas:", ordenado[0:3])
print("Piezas del inventario:", sum(inventario))
print("Posición del SKU de 720 piezas:", inventario.index(720))
print("Cuántas veces aparece 890:", inventario.count(890))
print("Al final:", inventario)
```

**Salida**

```text
Al inicio: [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
Tres SKU con más piezas: [890, 890, 720]
Piezas del inventario: 5428
Posición del SKU de 720 piezas: 9
Cuántas veces aparece 890: 2
Al final: [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La primera y la última línea son idénticas | 3 |
| El orden se hace sobre una copia hecha con `copy` | 2 |
| Las tres cifras más altas incluyen el 890 repetido | 2 |
| `index` y `count` usados donde toca | 2 |
| Total de piezas correcto | 1 |

**Error que más se ve**

Copiar con `ordenado = inventario`. Las dos líneas de inventario salen ordenadas y el alumno concluye que su programa funciona, porque nunca compara la primera con la última.

### 12.3 · Integrar

**Solución**

```python
skus = ["PAP-100", "PAP-215", "OFI-330", "OFI-412",
        "LIM-501", "LIM-620", "TEC-710", "TEC-844"]
unidades = [1840, 5210, 960, 2375, 3120, 880, 1450, 640]
precios = [38.50, 9.90, 74.00, 22.50, 15.75, 96.20, 58.40, 210.00]

UMBRAL = 70000
relevantes = []

for i in range(len(skus)):
    importe = unidades[i] * precios[i]

    if importe >= UMBRAL:
        relevantes.append((importe, skus[i]))

relevantes.sort()
relevantes.reverse()

print(f"SKU por arriba de ${UMBRAL:,} de venta: {len(relevantes)} de {len(skus)}")

for importe, sku in relevantes:
    print(f"{sku:<10}{importe:>12,.2f}")

print("La lista original conserva", len(skus), "claves y empieza en", skus[0])
```

La tupla guarda el importe primero porque el orden de una lista de tuplas se decide por el primer elemento. Así se ordena por dinero sin perder de vista a qué clave pertenece cada cifra.

**Salida**

```text
SKU por arriba de $70,000 de venta: 5 de 8
TEC-844     134,400.00
TEC-710      84,680.00
LIM-620      84,656.00
OFI-330      71,040.00
PAP-100      70,840.00
La lista original conserva 8 claves y empieza en PAP-100
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La lista nueva se llena con `append` dentro del ciclo | 2 |
| Los elementos son tuplas de importe y clave | 2 |
| El orden descendente conserva el emparejamiento | 2 |
| Las cinco claves correctas, con sus importes | 2 |
| El umbral vive en una sola variable y aparece en el texto | 2 |

**Error que más se ve**

Guardar dos listas paralelas de importes y claves, y ordenar solo la de importes. Los importes quedan bien ordenados y las claves siguen en el orden de captura, así que la tabla asigna cada cifra al SKU equivocado.

---

## Semana 13 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Solución**

```text
4
4
None
15
['Bravo', 'Sol']
['Nardo', 'Zafiro']
5
```

El diccionario mide 4 porque `dias_entrega["Sol"] = 4` sobrescribió una llave que ya existía, y solo `Nardo` agregó una entrada nueva. Las llaves no se repiten.

`dias_entrega["Zafiro"]` habría lanzado `KeyError` y detenido el programa ahí mismo. `get` devuelve `None`, o el valor por omisión que se le pase.

La pregunta de quién facturó en un mes y no en el otro, sin importar en cuál, la contesta la diferencia simétrica: `marzo ^ abril`, que aquí devolvería `['Aurora', 'Nardo', 'Zafiro']`.

**Salida**

```text
4
4
None
15
['Bravo', 'Sol']
['Nardo', 'Zafiro']
5
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete líneas correctas | 4 |
| Se explica la sobreescritura de la llave repetida | 2 |
| `KeyError` nombrado como lo que evita `get` | 2 |
| La diferencia simétrica identificada, con su resultado | 2 |

**Error que más se ve**

Contestar 5 en la primera línea, contando las tres iniciales más las dos asignaciones. Una de las dos era una llave que ya existía.

### 13.2 · Aplicar

**Solución**

```python
proveedores = ["Aurora", "Sol", "Bravo", "Nardo", "Zafiro", "Delta"]
dias = [3, 4, 5, 9, 6, 12]

catalogo = {}

for i in range(len(proveedores)):
    catalogo[proveedores[i]] = dias[i]

print(f"Proveedores en el catálogo: {len(catalogo)}")

for nombre, plazo in catalogo.items():
    print(f"{nombre:<10}{plazo:>4} días")

print("Plazo promedio:", sum(catalogo.values()) / len(catalogo), "días")
print("Consulta de Bravo:", catalogo.get("Bravo", 30), "días")
print("Consulta de Quintana:", catalogo.get("Quintana", 30), "días")
```

**Salida**

```text
Proveedores en el catálogo: 6
Aurora       3 días
Sol          4 días
Bravo        5 días
Nardo        9 días
Zafiro       6 días
Delta       12 días
Plazo promedio: 6.5 días
Consulta de Bravo: 5 días
Consulta de Quintana: 30 días
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El diccionario se arma con un ciclo desde las dos listas | 3 |
| El recorrido usa `items` y saca llave y valor a la vez | 2 |
| El promedio sale de `values` | 2 |
| Las dos consultas usan `get` con valor por omisión | 2 |
| La tabla queda alineada | 1 |

**Error que más se ve**

Escribir el diccionario a mano con las seis parejas. Da la misma salida y deja de servir en cuanto el catálogo llegue con cuarenta proveedores.

### 13.3 · Integrar

**Solución**

```python
def consolidar(nombres, importes):
    """Devuelve la compra acumulada por proveedor en un solo mes."""
    resumen = {}

    for i in range(len(nombres)):
        resumen[nombres[i]] = resumen.get(nombres[i], 0) + importes[i]

    return resumen


def variacion(antes, despues):
    """Devuelve el cambio porcentual entre dos importes."""
    return (despues - antes) / antes


marzo_prov = ["Aurora", "Sol", "Bravo", "Aurora", "Nardo", "Sol"]
marzo_imp = [18400, 9375, 24680, 6120, 15302, 8100]
abril_prov = ["Sol", "Bravo", "Zafiro", "Bravo", "Aurora", "Zafiro"]
abril_imp = [11250, 19800, 7400, 5600, 22150, 9900]

marzo = consolidar(marzo_prov, marzo_imp)
abril = consolidar(abril_prov, abril_imp)

print(f"Compra de marzo: ${sum(marzo.values()):,}")
print(f"Compra de abril: ${sum(abril.values()):,}")
print(f"Variación del gasto: {variacion(sum(marzo.values()), sum(abril.values())):.1%}")

nuevos = set(abril) - set(marzo)
perdidos = set(marzo) - set(abril)
constantes = set(marzo) & set(abril)

print("Proveedores nuevos:", sorted(nuevos))
print("Proveedores que dejaron de facturar:", sorted(perdidos))

print("Movimiento de los que están en los dos meses:")

for nombre in sorted(constantes):
    print(f"{nombre:<10}{marzo[nombre]:>10,}{abril[nombre]:>10,}"
          f"{variacion(marzo[nombre], abril[nombre]):>9.1%}")
```

La clave del acumulado es `resumen.get(nombres[i], 0) + importes[i]`: la primera vez que aparece un proveedor no hay llave, `get` devuelve cero y la suma arranca sin ningún caso especial.

**Salida**

```text
Compra de marzo: $81,977
Compra de abril: $76,100
Variación del gasto: -7.2%
Proveedores nuevos: ['Zafiro']
Proveedores que dejaron de facturar: ['Nardo']
Movimiento de los que están en los dos meses:
Aurora        24,520    22,150    -9.7%
Bravo         24,680    25,400     2.9%
Sol           17,475    11,250   -35.6%
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| `consolidar` acumula con `get` y devuelve el diccionario | 3 |
| Los dos totales y la variación general correctos | 2 |
| Nuevos y perdidos salen de operaciones de conjuntos | 2 |
| La tabla de los tres constantes, con sus variaciones | 2 |
| Las dos funciones con docstring y sin `print` adentro | 1 |

**Error que más se ve**

Escribir `resumen[nombres[i]] = importes[i]` sin sumar. Aurora queda en 6,120 en lugar de 24,520 porque la segunda factura pisa a la primera, y el total de marzo baja a 54,202 sin que nada lo señale.

---

## Semana 14 · Archivos de texto y CSV

### 14.1 · Reconocer

**Solución**

```text
15
E-001 $18,400.00
<class 'str'>
True
Ventas Ejecutivo
```

`len(filas)` da 15 y no 16 porque `DictReader` usa el primer renglón como encabezado: se convierte en las llaves de cada diccionario y deja de contar como dato.

Abrir el archivo en modo `"w"` lo vacía en el instante en que se abre, antes de leer una sola línea. La nómina se perdería y el `DictReader` no encontraría nada.

`int(filas[4]["dias_laborados"])` lanza `ValueError`, porque una cadena vacía no representa ningún número. Convertir el vacío en cero es una decisión que hay que escribir a mano.

**Salida**

```text
15
E-001 $18,400.00
<class 'str'>
True
Ventas Ejecutivo
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas correctas | 4 |
| Se explica el encabezado como razón del 15 | 2 |
| El efecto del modo `"w"` está dicho con la palabra borrar | 2 |
| `ValueError` nombrado, y no `TypeError` ni cero | 2 |

**Error que más se ve**

Contestar `<class 'int'>` en la tercera línea porque la columna trae números. Un archivo de texto entrega texto, siempre.

### 14.2 · Aplicar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent


def a_decimal(texto):
    """Convierte '$18,400.00' en el número 18400.0."""
    limpio = texto.replace("$", "").replace(",", "").strip()

    return float(limpio)


def a_entero(texto, ausente=0):
    """Convierte a entero y decide qué vale una celda vacía."""
    limpio = texto.strip()

    if limpio == "":
        return ausente

    return int(limpio)


with (DATOS / "nomina_marzo.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

nomina = 0
dias = 0
incompletos = 0

for fila in filas:
    nomina += a_decimal(fila["sueldo_mensual"])
    laborados = a_entero(fila["dias_laborados"])
    dias += laborados

    if laborados < 30:
        incompletos += 1

print(f"Empleados en el archivo: {len(filas)}")
print(f"Nómina mensual: ${nomina:,.2f}")
print(f"Sueldo promedio: ${nomina / len(filas):,.2f}")
print(f"Días laborados en total: {dias}")
print(f"Registros con menos de 30 días: {incompletos}")
```

El último renglón imprime 4 porque E-005, que trae la celda vacía, entró como cero días y cero es menor que treinta. La decisión de `a_entero` es la responsable: convertir el vacío en cero convierte «no sé cuántos días trabajó» en «no trabajó ninguno». Con esos datos, E-005 aparece como el caso más grave de la nómina cuando en realidad es el único del que no se sabe nada.

**Salida**

```text
Empleados en el archivo: 15
Nómina mensual: $320,550.00
Sueldo promedio: $21,370.00
Días laborados en total: 411
Registros con menos de 30 días: 4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos funciones de conversión, con docstring | 3 |
| El símbolo y la coma de miles se quitan antes de convertir | 2 |
| Los cinco renglones con las cifras correctas | 3 |
| Se identifica a E-005 como el registro contado de más | 2 |

**Error que más se ve**

Sumar `fila["sueldo_mensual"]` sin convertir. No lanza error: pega quince cadenas una tras otra y el total sale como un texto larguísimo que en un vistazo rápido parece un número enorme.

### 14.3 · Integrar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent


def a_decimal(texto):
    """Convierte '$18,400.00' en el número 18400.0."""
    return float(texto.replace("$", "").replace(",", "").strip())


with (DATOS / "nomina_marzo.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

nomina_area = {}
plazas_area = {}
sin_dias = []

for fila in filas:
    area = fila["area"]
    sueldo = a_decimal(fila["sueldo_mensual"])

    nomina_area[area] = nomina_area.get(area, 0) + sueldo
    plazas_area[area] = plazas_area.get(area, 0) + 1

    if fila["dias_laborados"].strip() == "":
        sin_dias.append(fila["clave"])

with (DATOS / "resumen_areas.csv").open("w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["area", "plazas", "nomina", "sueldo_promedio"])

    for area in sorted(nomina_area):
        escritor.writerow([area, plazas_area[area],
                           round(nomina_area[area], 2),
                           round(nomina_area[area] / plazas_area[area], 2)])

print(f"{'Área':<16}{'Plazas':>8}{'Nómina':>14}{'Promedio':>13}")

for area in sorted(nomina_area):
    print(f"{area:<16}{plazas_area[area]:>8}{nomina_area[area]:>14,.2f}"
          f"{nomina_area[area] / plazas_area[area]:>13,.2f}")

print(f"Claves sin días laborados: {sin_dias}")
print("Archivo escrito: resumen_areas.csv")
```

Las tres decisiones defendibles sobre la celda vacía de E-005 son estas. Tratarla como cero días, que es lo que hace el programa y lo que deja al empleado como el peor asistente del mes. Descartar el renglón completo, que baja la nómina reportada de Operaciones a $68,800.00 y sus plazas a 4. O dejarla marcada como dato faltante y reportar el promedio de días sobre los catorce registros que sí lo traen. Para el resumen por área ninguna de las tres cambia la nómina ni las plazas, porque el sueldo de E-005 está completo: lo que cambia es cualquier cifra que se calcule con los días.

**Salida**

```text
Área              Plazas        Nómina     Promedio
Administración         4    106,300.00    26,575.00
Operaciones            5     81,600.00    16,320.00
Ventas                 6    132,650.00    22,108.33
Claves sin días laborados: ['E-005']
Archivo escrito: resumen_areas.csv
```

El archivo `resumen_areas.csv` queda así:

```text
area,plazas,nomina,sueldo_promedio
Administración,4,106300.0,26575.0
Operaciones,5,81600.0,16320.0
Ventas,6,132650.0,22108.33
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los dos diccionarios se acumulan en un solo recorrido | 3 |
| La tabla en pantalla, ordenada y alineada | 2 |
| El archivo de salida se escribe con encabezado y `newline=""` | 3 |
| Las claves sin días se reportan | 1 |
| Las tres decisiones alternativas están dichas con su efecto | 1 |

**Error que más se ve**

Abrir el archivo de salida sin `newline=""`. En Windows el CSV sale con un renglón en blanco entre cada dato, y al abrirlo en la hoja de cálculo parece que el programa escribió el doble de filas.

---

## Semana 15 · Series, DataFrame, limpieza, agrupación y unión

### 15.1 · Reconocer

**Solución**

```text
(22, 5)
fecha                  str
region                 str
canal                  str
unidades           float64
precio_unitario        str
dtype: object
2
2
8
[' Norte ', 'Centro', 'NORTE', 'Norte', 'Occidente', 'Sureste', 'centro', 'occidente']
```

`unidades` salió `float64` porque dos celdas están vacías, y el marcador de vacío solo existe en una columna decimal. `precio_unitario` salió texto porque el signo de pesos y la coma de miles son formato, no valor, y ninguna columna con esos caracteres se puede leer como número.

Regiones de verdad hay cuatro: Norte, Centro, Occidente y Sureste. Un `groupby` corrido en este momento reportaría ocho, y partiría las cifras de Norte en cuatro montones.

El total de piezas ya se puede calcular, porque `unidades` es numérica y la suma ignora los vacíos. El total en dinero todavía no, porque el precio sigue siendo texto.

**Salida**

```text
(22, 5)
fecha                  str
region                 str
canal                  str
unidades           float64
precio_unitario        str
dtype: object
2
2
8
[' Norte ', 'Centro', 'NORTE', 'Norte', 'Occidente', 'Sureste', 'centro', 'occidente']
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Forma, tipos y los tres conteos correctos | 4 |
| La explicación de `float64` menciona las celdas vacías | 2 |
| La explicación del precio menciona el símbolo y la coma | 2 |
| Se distingue entre las 4 regiones reales y las 8 que reporta el archivo | 2 |

**Error que más se ve**

Explicar el `float64` diciendo que las unidades traen decimales. En el archivo todas son enteras: lo que obliga al decimal es el hueco, no el dato.

### 15.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

ventas = pd.read_csv(DATOS / "ventas_2026.csv")

print(f"Crudo: {len(ventas)} renglones, "
      f"{ventas['region'].nunique()} regiones, "
      f"{ventas.duplicated().sum()} duplicados, "
      f"{ventas['unidades'].isna().sum()} unidades vacías")

ventas = ventas.drop_duplicates()
print(f"Sin duplicados: {len(ventas)} renglones")

ventas["region"] = ventas["region"].str.strip().str.title()
print(f"Región normalizada: {sorted(ventas['region'].unique())}")

ventas["precio_unitario"] = (ventas["precio_unitario"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .str.strip()
                             .astype(float))
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

ventas["importe"] = ventas["unidades"] * ventas["precio_unitario"]
print(f"Importe con los huecos dentro: ${ventas['importe'].sum():,.2f}")

ventas = ventas.dropna(subset=["unidades"])
ventas["unidades"] = ventas["unidades"].astype(int)

print(f"Limpio: {len(ventas)} renglones, "
      f"{ventas['unidades'].sum():,} piezas, "
      f"${ventas['importe'].sum():,.2f} de ingreso")
print(f"Ticket promedio: ${ventas['importe'].mean():,.2f}")
print(ventas.dtypes)
```

Quitar los renglones con unidades vacías no movió el total porque el importe de esos dos renglones ya era vacío: unidades por precio, con las unidades ausentes, no produce cero, produce ausencia, y la suma la ignora. El ticket promedio tampoco se movió, por la misma razón: `mean` divide entre los 18 valores que sí existen, no entre los 20 renglones. Lo que cambió es el número de renglones de la tabla, y con eso la posibilidad de convertir `unidades` a entero. Y cambiaría cualquier cifra calculada dividiendo entre `len(ventas)` en lugar de dejar que pandas cuente.

**Salida**

```text
Crudo: 22 renglones, 8 regiones, 2 duplicados, 2 unidades vacías
Sin duplicados: 20 renglones
Región normalizada: ['Centro', 'Norte', 'Occidente', 'Sureste']
Importe con los huecos dentro: $2,301,950.00
Limpio: 18 renglones, 1,855 piezas, $2,301,950.00 de ingreso
Ticket promedio: $127,886.11
fecha              datetime64[us]
region                        str
canal                         str
unidades                    int64
precio_unitario           float64
importe                   float64
dtype: object
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los duplicados se quitan antes de agrupar o sumar cualquier cosa | 2 |
| La región se normaliza con `strip` y `title`, y quedan cuatro | 2 |
| El precio se convierte con `regex=False` y `astype` | 2 |
| La bitácora imprime un renglón por paso | 2 |
| La explicación del total que no se movió es correcta | 2 |

**Error que más se ve**

Aplicar `str.title()` sin `str.strip()` antes. `" Norte "` se convierte en `" Norte "` con la misma mayúscula y sigue contando como una región aparte, así que el conteo baja de ocho a cinco y parece resuelto.

### 15.3 · Integrar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

ventas = pd.read_csv(DATOS / "ventas_2026.csv").drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["precio_unitario"] = (ventas["precio_unitario"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .astype(float))
ventas = ventas.dropna(subset=["unidades"])
ventas["unidades"] = ventas["unidades"].astype(int)
ventas["importe"] = ventas["unidades"] * ventas["precio_unitario"]

resumen = ventas.groupby("region").agg(
    ingreso=("importe", "sum"),
    piezas=("unidades", "sum"),
    operaciones=("importe", "count"),
    ticket=("importe", "mean"),
).round(2).sort_values("ingreso", ascending=False)

print(resumen)
print()

rejilla = ventas.pivot_table(index="region", columns="canal",
                             values="importe", aggfunc="sum",
                             margins=True, margins_name="Total")
print((rejilla / 1000).round(1))
print()

catalogo = pd.DataFrame({
    "region": ["Norte", "Centro", "Occidente", "Sureste", "Golfo"],
    "gerente": ["Lucía Ramos", "Iván Peña", "Marta Ocampo",
                "Diego Salas", "Rocío Trejo"],
    "meta": [900000, 700000, 650000, 250000, 200000],
})

auditoria = resumen.reset_index().merge(catalogo, on="region",
                                        how="outer", indicator=True)
print(auditoria["_merge"].value_counts())
print(sorted(auditoria.loc[auditoria["_merge"] == "right_only", "region"]))
print()

tablero = resumen.reset_index().merge(catalogo, on="region", how="left")
tablero["avance"] = tablero["ingreso"] / tablero["meta"]
print(tablero[["region", "gerente", "ingreso", "meta", "avance"]]
      .to_string(index=False,
                 formatters={"ingreso": "{:,.2f}".format,
                             "meta": "{:,.0f}".format,
                             "avance": "{:.1%}".format}))
```

La celda vacía de la rejilla es Sureste en Online. La única venta de esa combinación era la del 18 de junio, que traía las unidades en blanco y se descartó al limpiar: la combinación existe en el catálogo comercial y no tiene ninguna operación completa en el año.

La auditoría marca a Golfo como `right_only`: está en el catálogo de plazas y no facturó nada en 2026. Eso no es un error de datos, es una plaza abierta que no vendió, y el hecho de que aparezca es justo lo que hay que reportar. Con `inner` habría desaparecido en silencio y el tablero se vería completo con cuatro regiones, sin que nadie preguntara por la quinta.

**Salida**

```text
            ingreso  piezas  operaciones    ticket
region
Norte      954450.0     765            7  136350.0
Centro     610350.0     490            5  122070.0
Occidente  568900.0     465            4  142225.0
Sureste    168250.0     135            2   84125.0

canal      Mayoreo  Menudeo  Online   Total
region
Centro       339.2    158.7   112.5   610.4
Norte        502.9     82.8   368.8   954.4
Occidente    386.8     75.9   106.2   568.9
Sureste      113.0     55.2     NaN   168.2
Total       1341.8    372.6   587.5  2302.0

_merge
both          4
right_only    1
left_only     0
Name: count, dtype: int64
['Golfo']

   region      gerente    ingreso    meta avance
    Norte  Lucía Ramos 954,450.00 900,000 106.0%
   Centro    Iván Peña 610,350.00 700,000  87.2%
Occidente Marta Ocampo 568,900.00 650,000  87.5%
  Sureste  Diego Salas 168,250.00 250,000  67.3%
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El `agg` produce las cuatro columnas con los nombres pedidos | 2 |
| La rejilla suma en lugar de promediar y trae sus totales | 2 |
| La auditoría reporta los tres conteos antes de unir | 2 |
| La unión final usa el modo izquierdo y calcula el avance | 2 |
| Se explica la celda vacía y el caso de Golfo | 2 |

**Error que más se ve**

Llamar a `pivot_table` sin `aggfunc`. Devuelve promedios, la rejilla se ve razonable y sus renglones ya no suman el ingreso del año, que es la comprobación que casi nadie hace.

---

## Semana 16 · Visualización, matplotlib y seaborn

### 16.1 · Reconocer

**Solución**

`sns.barplot` promedia por omisión, así que esa llamada dibuja el ticket promedio, no el ingreso: Norte 136,350.00, Centro 122,070.00, Occidente 142,225.00 y Sureste 84,125.00.

El ranking de esa gráfica va Occidente, Norte, Centro, Sureste. El del ingreso total va Norte, Centro, Occidente, Sureste. Las dos primeras posiciones se invierten, y quien vea la gráfica sin leer el eje va a concluir que Occidente es la región más importante del año.

Para que dibuje el total hay que pasarle `estimator="sum"`, y conviene `errorbar=None` para que no encime el intervalo de confianza sobre cada barra.

Un título que carga las dos lecturas: «Norte vende más seguido, Occidente vende más grande en cada operación».

| Línea | Qué está mal |
|---|---|
| `ax.set_ylim(500000, 1000000)` | Corta el eje: Sureste desaparece del gráfico y la diferencia entre Norte y Centro se ve del doble de lo que es |
| `ax.plot(...)` sobre regiones | Una línea afirma que hay un recorrido entre Norte y Centro, y entre categorías no existe ninguno |
| `ax.pie(...)` | Con cuatro rebanadas ya obliga a comparar ángulos, que es justo lo que la gente hace mal; en barras ordenadas la respuesta se lee sola |

**Salida**

La entrega son los cuatro promedios, los dos rankings, la corrección de la llamada y la tabla de las tres decisiones.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro promedios identificados como lo que dibuja la barra | 3 |
| Los dos rankings escritos y comparados | 2 |
| `estimator="sum"` propuesto, con `errorbar=None` | 2 |
| Las tres decisiones de gráfica explicadas | 3 |

**Error que más se ve**

Contestar que la barra dibuja el ingreso porque «es la columna que se le pasó». Se le pasa la columna, y lo que dibuja depende del estimador, que nadie escribió.

### 16.2 · Aplicar

**Solución**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

MESES = ["ene", "feb", "mar", "abr", "may", "jun",
         "jul", "ago", "sep", "oct", "nov", "dic"]

ingreso = pd.Series(
    [1284000, 962000, 1431000, 1189000, 1516000, 1340000,
     1208000, 1377000, 1465000, 1623000, 2048000, 3412000],
    index=MESES,
)

anual = ingreso.sum()
ultimo_trimestre = ingreso[["oct", "nov", "dic"]].sum() / anual
peso_diciembre = ingreso["dic"] / anual

fig, ax = plt.subplots(figsize=(10, 5))

barras = ax.bar(MESES, ingreso.values, color="#C7D6E8")

for mes in ["oct", "nov", "dic"]:
    barras[MESES.index(mes)].set_color("#2B5F8F")

ax.set_title(f"El último trimestre concentró el {ultimo_trimestre:.0%} "
             f"del ingreso del año")
ax.set_ylabel("Ingreso mensual (millones de pesos)")
ax.set_ylim(0, 3_600_000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
fig.text(0.01, 0.01, "Fuente: cierre mensual 2026, Comercializadora Aurora. "
                     "12 meses facturados.", fontsize=8, color="#555555")

fig.savefig("estacionalidad_2026.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"Ingreso del año: ${anual:,.0f}")
print(f"Peso del último trimestre: {ultimo_trimestre:.1%}")
print(f"Peso de diciembre solo: {peso_diciembre:.1%}")
print(f"Mes más bajo: {ingreso.idxmin()} con ${ingreso.min():,.0f}")
print("Gráfica guardada en estacionalidad_2026.png")
```

El título dice «38 %» porque el formato del título redondea a cero decimales lo que en la salida aparece como 37.6 %. Es la misma cifra y sale del mismo cálculo: nadie la escribió a mano, y si cambia un mes el título cambia solo.

**Salida**

```text
Ingreso del año: $18,855,000
Peso del último trimestre: 37.6%
Peso de diciembre solo: 18.1%
Mes más bajo: feb con $962,000
Gráfica guardada en estacionalidad_2026.png
```

La imagen queda con doce barras, las tres del último trimestre en azul fuerte, el eje vertical de 0.0M a 3.5M y la fuente en la esquina inferior izquierda.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres barras del último trimestre resaltadas, las nueve restantes no | 2 |
| El título trae el hallazgo y su cifra viene del cálculo | 2 |
| Eje vertical desde cero, etiquetado y con la unidad | 2 |
| El formateador deja las marcas como 1.5M | 2 |
| Fuente al pie y figura cerrada al terminar | 2 |

**Error que más se ve**

Escribir el 38 % a mano en el título. Se ve idéntico hoy y queda mintiendo el día que alguien agregue un mes o corrija una cifra.

### 16.3 · Integrar

**Solución**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATOS = Path(__file__).resolve().parent

sns.set_theme(style="whitegrid", palette="deep")

nomina = pd.read_csv(DATOS / "nomina_marzo.csv")
nomina["sueldo_mensual"] = (nomina["sueldo_mensual"]
                            .str.replace("$", "", regex=False)
                            .str.replace(",", "", regex=False)
                            .astype(float))

orden = (nomina.groupby("area")["sueldo_mensual"]
         .median()
         .sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=nomina, x="area", y="sueldo_mensual", order=orden,
            hue="area", legend=False, ax=ax)
ax.set_title("Ventas reparte sueldos más desiguales que Operaciones")
ax.set_xlabel("")
ax.set_ylabel("Sueldo mensual (pesos)")
ax.set_ylim(0, 46000)
fig.text(0.01, 0.01, "Fuente: nómina de marzo 2026, 15 plazas.",
         fontsize=8, color="#555555")
fig.savefig("sueldos_por_area.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print(nomina.groupby("area")["sueldo_mensual"]
      .agg(["count", "median", "mean", "max"]).round(2))

ventas = pd.read_csv(DATOS / "ventas_2026.csv").drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["precio_unitario"] = (ventas["precio_unitario"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .astype(float))
ventas = ventas.dropna(subset=["unidades"])
ventas["importe"] = ventas["unidades"] * ventas["precio_unitario"]

rejilla = ventas.pivot_table(index="region", columns="canal",
                             values="importe", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 4))
sns.heatmap(rejilla, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Mayoreo carga el ingreso en las cuatro regiones")
ax.set_xlabel("")
ax.set_ylabel("")
fig.text(0.01, 0.01, "Fuente: ventas 2026, 18 operaciones limpias. "
                     "Cifras en miles de pesos.", fontsize=8, color="#555555")
fig.savefig("rejilla_region_canal.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print()
print(rejilla.round(1))
print("Gráficas guardadas: sueldos_por_area.png, rejilla_region_canal.png")
```

Texto alternativo de la caja y bigotes: gráfica de caja y bigotes del sueldo mensual de quince plazas, repartidas en tres áreas y ordenadas por mediana. Administración tiene la mediana más alta, 25,350 pesos, y el reparto más apretado, entre 21,700 y 33,900. Ventas tiene una mediana de 18,225 y llega hasta 42,300, así que su caja es la más larga y la que muestra la mayor desigualdad interna del área.

Texto alternativo del mapa de calor: mapa de calor de cuatro regiones contra tres canales, con el ingreso del año en miles de pesos escrito en cada celda. La celda más intensa es Norte en Mayoreo, con 503 mil pesos. Mayoreo es la columna más cargada en las cuatro regiones y Sureste en Online aparece en blanco, porque su única venta se descartó al limpiar.

**Salida**

```text
                count   median      mean      max
area
Administración      4  25350.0  26575.00  33900.0
Operaciones         5  13900.0  16320.00  26500.0
Ventas              6  18225.0  22108.33  42300.0

canal      Mayoreo  Menudeo  Online
region
Centro       339.2    158.7   112.5
Norte        502.9     82.8   368.8
Occidente    386.8     75.9   106.2
Sureste      113.0     55.2     NaN
Gráficas guardadas: sueldos_por_area.png, rejilla_region_canal.png
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El tema de seaborn se configura una sola vez, arriba | 1 |
| Las áreas de la caja van ordenadas por mediana | 2 |
| El título de la caja dice un hallazgo verificable en la tabla | 2 |
| El mapa de calor recibe la rejilla directa, con los valores escritos | 2 |
| Los dos textos alternativos, con cada cifra comprobable | 3 |

**Error que más se ve**

Escribir el texto alternativo de memoria, con frases como «los sueldos suben en todas las áreas». Lo delata que ninguna cifra de la descripción aparezca en la tabla que el mismo programa imprimió tres líneas antes.

---

## Semana 17 · Repaso y examen final

### 17.1 · Reconocer

**Solución**

```text
8
10
175.0
None
```

| Línea | Error | Qué imprime | Qué se quería | Cómo se corrige |
|---|---|---|---|---|
| `groupby("region")` sin limpiar | Agrupar antes de limpiar | 8 regiones | 4 regiones | Normalizar con `str.strip().str.title()` y quitar duplicados antes de agrupar |
| `ventas[...]["canal"] = "Mayoreo"` | Asignación encadenada | 10 renglones en Mayoreo | 12, si la escritura hubiera funcionado | `ventas.loc[ventas["region"] == "Norte", "canal"] = "Mayoreo"` |
| `total = 0` dentro del `for` | Acumulador declarado adentro | 175.0, el último renglón | 1,855, la suma de las unidades | Sacar `total = 0` antes del ciclo |
| `orden = orden.sort()` | Confundir modificar con devolver | `None` | La lista ordenada | `orden = sorted(orden)`, o llamar a `orden.sort()` sin asignar |

El aviso que deja la segunda línea es este:

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
Such chained assignment never works to update the original DataFrame or Series,
because the intermediate object on which we are setting values always behaves as
a copy (due to Copy-on-Write).

Try using '.loc[row_indexer, col_indexer] = value' instead, to perform the
assignment in a single step.
```

Un aviso no detiene el programa: la ejecución sigue, las cuatro cifras se imprimen y el archivo termina bien. Por eso es más peligroso que un error. Un error obliga a arreglarlo antes de entregar; un aviso se pierde entre la salida y el resultado equivocado llega al comité con cara de resultado.

**Salida**

```text
8
10
175.0
None
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas de salida correctas | 3 |
| Los cuatro errores nombrados con el vocabulario del curso | 3 |
| Las cuatro correcciones son las del curso, no rodeos | 2 |
| La distinción entre aviso y error está argumentada | 2 |

**Error que más se ve**

Contestar 12 en la segunda línea, suponiendo que la asignación encadenada sí escribió. Lo delata que el alumno no notó el aviso, que estaba impreso arriba de su propia respuesta.

### 17.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

ventas = pd.read_csv(DATOS / "ventas_2026.csv")
print(f"Al cargar: {ventas.shape[0]} renglones, "
      f"{ventas['region'].nunique()} regiones, "
      f"{ventas.duplicated().sum()} duplicados, "
      f"{ventas['unidades'].isna().sum()} unidades vacías")

ventas = ventas.drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["precio_unitario"] = (ventas["precio_unitario"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .astype(float))
ventas = ventas.dropna(subset=["unidades"])
ventas["unidades"] = ventas["unidades"].astype(int)
ventas["importe"] = ventas["unidades"] * ventas["precio_unitario"]

print(f"Ya limpio: {ventas.shape[0]} renglones, "
      f"{ventas['region'].nunique()} regiones, "
      f"${ventas['importe'].sum():,.2f} de ingreso")

cruce = (ventas.groupby(["region", "canal"])
         .agg(ingreso=("importe", "sum"), operaciones=("importe", "count"))
         .sort_values("ingreso", ascending=False))

print(cruce.head(4).round(2))

lider = cruce.index[0]
ingreso_lider = cruce.iloc[0]["ingreso"]
participacion = ingreso_lider / ventas["importe"].sum()

print(f"Conviene atender primero {lider[0]} en {lider[1]}: "
      f"${ingreso_lider:,.2f}, el {participacion:.1%} del ingreso del año.")
```

**Salida**

```text
Al cargar: 22 renglones, 8 regiones, 2 duplicados, 2 unidades vacías
Ya limpio: 18 renglones, 4 regiones, $2,301,950.00 de ingreso
                    ingreso  operaciones
region    canal
Norte     Mayoreo  502900.0            3
Occidente Mayoreo  386750.0            2
Norte     Online   368750.0            3
Centro    Mayoreo  339150.0            2
Conviene atender primero Norte en Mayoreo: $502,900.00, el 21.8% del ingreso del año.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El diagnóstico se imprime antes de tocar nada | 2 |
| La limpieza cubre duplicados, región, precio y huecos | 3 |
| El cruce agrupa por las dos columnas y ordena por ingreso | 2 |
| La conclusión es una frase con dos cifras verificables | 2 |
| El porcentaje se divide entre el ingreso del año ya limpio | 1 |

**Error que más se ve**

Dividir la participación entre el ingreso de la región y no entre el del año. Da 52.7 % en lugar de 21.8 %, y la frase resultante afirma algo que la tabla no dice.

### 17.3 · Integrar

**Solución**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent


def cargar_limpio(ruta):
    """Carga el archivo de ventas y devuelve la tabla lista para analizar."""
    datos = pd.read_csv(ruta).drop_duplicates()
    datos["region"] = datos["region"].str.strip().str.title()
    datos["precio_unitario"] = (datos["precio_unitario"]
                                .str.replace("$", "", regex=False)
                                .str.replace(",", "", regex=False)
                                .astype(float))
    datos["fecha"] = pd.to_datetime(datos["fecha"])
    datos = datos.dropna(subset=["unidades"])
    datos["unidades"] = datos["unidades"].astype(int)
    datos["importe"] = datos["unidades"] * datos["precio_unitario"]

    return datos


def tablero(ventas, catalogo):
    """Devuelve el avance contra meta por región, de mayor a menor."""
    resumen = ventas.groupby("region").agg(
        ingreso=("importe", "sum"),
        operaciones=("importe", "count"),
        ticket=("importe", "mean"),
    ).reset_index()

    unida = resumen.merge(catalogo, on="region", how="left")
    unida["avance"] = unida["ingreso"] / unida["meta"]

    return unida.sort_values("avance", ascending=False)


catalogo = pd.DataFrame({
    "region": ["Norte", "Centro", "Occidente", "Sureste", "Golfo"],
    "gerente": ["Lucía Ramos", "Iván Peña", "Marta Ocampo",
                "Diego Salas", "Rocío Trejo"],
    "meta": [900000, 700000, 650000, 250000, 200000],
})

ventas = cargar_limpio(DATOS / "ventas_2026.csv")

auditoria = (ventas.groupby("region")["importe"].sum().reset_index()
             .merge(catalogo, on="region", how="outer", indicator=True))
conteo = auditoria["_merge"].value_counts()

print("Auditoría de la unión")
print(f"  Cruzan en los dos lados: {conteo.get('both', 0)}")
print(f"  Solo en el catálogo: {conteo.get('right_only', 0)} "
      f"{sorted(auditoria.loc[auditoria['_merge'] == 'right_only', 'region'])}")
print(f"  Solo en las ventas: {conteo.get('left_only', 0)}")
print()

reporte = tablero(ventas, catalogo)
print(reporte[["region", "gerente", "ingreso", "operaciones", "ticket",
               "meta", "avance"]]
      .to_string(index=False,
                 formatters={"ingreso": "{:,.2f}".format,
                             "ticket": "{:,.2f}".format,
                             "meta": "{:,.0f}".format,
                             "avance": "{:.1%}".format}))
print()

por_mes = ventas.groupby(ventas["fecha"].dt.month)["importe"].sum()
print(f"Meses con operación: {len(por_mes)}")
print(f"Mes más fuerte: {por_mes.idxmax()} con ${por_mes.max():,.2f}")
print(f"Peso del mes más fuerte: {por_mes.max() / por_mes.sum():.1%}")

fig, ax = plt.subplots(figsize=(9, 5))
orden = reporte.sort_values("ingreso", ascending=False)
barras = ax.bar(orden["region"], orden["ingreso"], color="#C7D6E8")
barras[0].set_color("#2B5F8F")
ax.set_title(f"{orden.iloc[0]['region']} aporta el "
             f"{orden.iloc[0]['ingreso'] / ventas['importe'].sum():.0%} "
             f"del ingreso del año")
ax.set_ylabel("Ingreso 2026 (millones de pesos)")
ax.set_ylim(0, 1_100_000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
fig.text(0.01, 0.01, "Fuente: ventas_2026.csv, 18 de 22 renglones "
                     "después de limpiar.", fontsize=8, color="#555555")
fig.savefig("cierre_2026.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Gráfica guardada en cierre_2026.png")
```

Reporte de cierre, el que se califica junto con el código:

La pregunta fue qué región conviene atender primero en 2027 y qué tan cerca quedó cada una de su meta. El archivo llegó con 22 renglones, dos de ellos duplicados exactos y dos con las unidades en blanco. Los duplicados se quitaron porque repetían fecha, región, canal, unidades y precio: contarlos habría inflado el ingreso de Norte y de Occidente en una operación cada uno. Los dos renglones sin unidades se descartaron, no se rellenaron con cero, porque el importe de esos renglones ya no se podía calcular y ponerles cero habría bajado el ticket promedio de sus regiones con una venta que sí existió. Quedaron 18 operaciones y cuatro regiones, después de normalizar ocho formas de capturar el mismo nombre.

El hallazgo es que Norte cerró en 106.0 % de su meta con 954,450 pesos, y es la única región arriba de cien. Occidente quedó en 87.5 % con 568,900 pesos y Centro en 87.2 % con 610,350: Occidente vende menos y avanza más, porque su meta es 50,000 pesos menor. Sureste quedó en 67.3 % con solo dos operaciones en el año. La auditoría de la unión marcó a Golfo del lado del catálogo, sin una sola venta en 2026.

La recomendación para 2027 es revisar la meta de Sureste antes que su operación: dos operaciones en doce meses no son un problema de cierre, son una plaza sin actividad comercial. Y pedir explicación de Golfo, que tiene gerente y meta asignados y no facturó nada, antes de volver a presupuestarla.

**Salida**

```text
Auditoría de la unión
  Cruzan en los dos lados: 4
  Solo en el catálogo: 1 ['Golfo']
  Solo en las ventas: 0

   region      gerente    ingreso  operaciones     ticket    meta avance
    Norte  Lucía Ramos 954,450.00            7 136,350.00 900,000 106.0%
Occidente Marta Ocampo 568,900.00            4 142,225.00 650,000  87.5%
   Centro    Iván Peña 610,350.00            5 122,070.00 700,000  87.2%
  Sureste  Diego Salas 168,250.00            2  84,125.00 250,000  67.3%

Meses con operación: 10
Mes más fuerte: 10 con $303,800.00
Peso del mes más fuerte: 13.2%
Gráfica guardada en cierre_2026.png
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos funciones con docstring, sin fórmulas repetidas fuera de ellas | 2 |
| La auditoría de la unión reporta las dos direcciones antes del tablero | 2 |
| El tablero trae las siete columnas y el orden por avance | 2 |
| La gráfica lleva título calculado, eje desde cero y fuente al pie | 2 |
| El reporte justifica cada decisión de limpieza con su efecto | 2 |

**Error que más se ve**

Unir con `how="inner"` en lugar de auditar. Golfo desaparece sin dejar rastro y el tablero se ve completo con cuatro regiones, así que nadie pregunta por la plaza que tiene gerente asignado y no vendió nada.
