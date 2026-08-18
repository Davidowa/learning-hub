# Ejercicios · Análisis de Datos · TIA502

Este cuadernillo acompaña las diecisiete semanas del curso y se resuelve con lo que ya se vio en clase, nunca con lo que viene después. Cada semana trae tres ejercicios: el primero se lee y se predice sin ejecutar nada, el segundo se escribe contra una especificación que ya trae sus datos y su resultado esperado, y el tercero amarra el tema de la semana con el de las anteriores. La dificultad sube en dos direcciones, dentro de cada semana y a lo largo del semestre, así que el ejercicio de reconocer de la semana 12 pide más que el de integrar de la semana 4. Se entrega en Blackboard un archivo `.py` por ejercicio, junto con la salida tal como la produjo tu programa, salvo donde el enunciado pida papel.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Índices de una columna de ventas**

Comercializadora Aurora tiene el primer semestre capturado en dos listas emparejadas. Sin ejecutar nada, escribe las cuatro líneas que imprime el programa.

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ventas = [128400, 96750, 143200, 118900, 151600, 134050]

print(meses[0], ventas[0])
print(meses[-1], ventas[-1])
print(ventas[4] - ventas[1])
print(len(ventas))
```

Contesta además dos cosas, un renglón cada una. Si esos datos vivieran en una hoja de cálculo con el encabezado en la fila 1, ¿a qué fila corresponde `ventas[3]`? ¿Qué ocurre si agregas `print(meses[6])` al final?

### 01.2 · Aplicar

**Resumen de un semestre**

Con las dos listas del ejercicio anterior, escribe un programa que imprima cuatro renglones:

1. La venta del semestre, con separador de miles y sin decimales.
2. El promedio mensual, con separador de miles y dos decimales.
3. El mejor mes y su cifra, en un solo renglón.
4. Cuánto rebasa el mejor mes al promedio, con dos decimales.

La venta del semestre es 772,900 y el promedio mensual es 128,816.67. Si esas dos cifras no coinciden, revisa antes de seguir. Usa `sum`, `len`, `max` e `index`, y ningún ciclo.

### 01.3 · Integrar

**El producto que carga el mes**

La papelería cerró marzo con cuatro claves, capturadas en tres listas que se corresponden por posición:

```python
productos = ["Cuaderno profesional", "Bolígrafo negro",
             "Carpeta de argollas", "Marcador permanente"]
unidades = [1840, 5210, 960, 2375]
precios = [38.50, 9.90, 74.00, 22.50]
```

Escribe un programa que encuentre el producto con más piezas vendidas y reporte cinco datos: el nombre del producto, sus piezas, el importe que dejó (piezas por precio), qué porcentaje de las piezas del mes representa, con un decimal y el símbolo escrito a un lado, y el total de piezas del mes.

El producto líder mueve 5,210 piezas y su participación es del 50.2 %. Nada de escribir el índice 1 a mano: la posición tiene que salir de los datos, para que el programa siga sirviendo si el mes que entra cambia el líder.

---

## Semana 02 · Diseño de algoritmos

Los tres ejercicios de esta semana se entregan en papel. Sin computadora y sin sintaxis de ningún lenguaje.

### 02.1 · Reconocer

**Traza de una política de descuento**

Compras corporativas autoriza el descuento de un cliente con este algoritmo:

```text
INICIO
    LEER compra_anual, meses_relacion, adeudo_vencido

    SI adeudo_vencido > 0 ENTONCES
        descuento = 0
    SI NO SI compra_anual >= 500000 Y meses_relacion >= 24 ENTONCES
        descuento = 0.12
    SI NO SI compra_anual >= 200000 ENTONCES
        descuento = 0.06
    SI NO
        descuento = 0.02

    ESCRIBIR descuento
FIN
```

Llena una tabla de traza para estos tres clientes, indicando qué condición se evalúa, cuál se cumple y qué descuento sale:

| Cliente | compra_anual | meses_relacion | adeudo_vencido |
|---|---|---|---|
| Abarrotes La Paz | 620,000 | 36 | 0 |
| Ferretería Muñoz | 780,000 | 30 | 4,500 |
| Papelera Bruno | 200,000 | 8 | 0 |

Contesta después cuál de las cinco propiedades de un algoritmo se rompería si el tercer renglón dijera «SI el cliente es importante ENTONCES descuento = 0.12», y explica en dos renglones por qué.

### 02.2 · Aplicar

**Pseudocódigo del bono trimestral**

Recursos humanos paga un bono trimestral con estas reglas, que hoy viven en un correo:

- Quien tenga menos de seis meses de antigüedad no cobra bono.
- Con seis meses o más y evaluación de 4.5 o superior, el bono es el 15 % del sueldo mensual.
- Con seis meses o más y evaluación entre 3.5 y 4.49, el bono es el 8 %.
- Con seis meses o más y evaluación menor a 3.5, el bono es de 1,200 pesos fijos.
- A quien acumule más de tres faltas en el trimestre se le descuenta la mitad de lo que le haya tocado, sin importar por qué rama entró.

Escribe el pseudocódigo completo, con `INICIO`, `LEER`, sus decisiones y `ESCRIBIR`. Dibuja después el diagrama de flujo con los cuatro símbolos, y etiqueta las dos salidas de cada rombo.

Prueba tu algoritmo con Marina Cortés: sueldo de 24,500, ocho meses de antigüedad, evaluación de 4.6 y cuatro faltas. El bono que le toca es 1,837.50.

### 02.3 · Integrar

**Descomponer el cierre de nómina**

El cierre quincenal hoy es un proceso de una sola frase: «calcular lo que se le paga a cada quien». Pártelo en tres subproblemas que se puedan resolver por separado, dales nombre y di qué recibe y qué entrega cada uno.

Elige uno de los tres y escríbelo en pseudocódigo con al menos dos decisiones. Agrega después un caso límite que tu primera versión no cubría, di qué resultado equivocado producía y cómo lo corregiste.

Lo que entregues tiene que pasar la prueba del intercambio: dáselo a un compañero junto con tus datos de entrada y comparen resultados. Si no coinciden, algo quedó ambiguo y hay que señalar dónde.

---

## Semana 03 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**El presupuesto que se pisa a sí mismo**

Marketing ajustó su presupuesto anual cuatro veces en el mismo archivo. Predice qué imprime.

```python
presupuesto = 250000
presupuesto = presupuesto - 40000
presupuesto = presupuesto * 2
presupuesto = presupuesto + 15000

print(presupuesto)
```

Arma después una tabla de tres renglones. Por cada una de estas líneas, di qué tipo de error lanza Python y en qué línea lo reporta:

```python
Print(presupuesto)
print("Presupuesto: , presupuesto)
print(presupuesto
```

### 03.2 · Aplicar

**Primer programa de nómina**

Escribe un programa completo, con su comentario de encabezado y su importación arriba, que trabaje sobre los seis sueldos del área de ventas:

```python
sueldos = [23200, 42800, 82700, 24500, 31600, 28900]
```

Tiene que imprimir tres renglones etiquetados: cuántos empleados hay, el sueldo promedio y el sueldo mayor. El promedio se calcula con `mean`, del módulo `statistics`, no dividiendo a mano. El promedio da 38950.

### 03.3 · Integrar

**Reparar el cierre de caja**

Este programa de la sucursal Reforma no corre. Tiene tres errores de sintaxis y uno que no lo es: calcula algo que nunca muestra.

```python
# Cierre de caja de la sucursal Reforma.
from statistics import mean

dias = ["lun", "mar", "mié", "jue", "vie", "sáb"]
ingresos = [18400, 15750, 21300, 19850, 27600, 34200]

promedio = mean(ingresos)
mejor = dias[ingresos.index(max(ingresos))]

Print("Días registrados:", len(ingresos)
print("Ingreso de la semana:", sum(ingresos))
print("Ingreso promedio:" promedio)
```

Entrega el programa corregido, que imprima cuatro renglones: días registrados, ingreso de la semana, ingreso promedio y mejor día. El ingreso de la semana es 137100 y el promedio es 22850.

Entrega también una tabla con los cuatro problemas: la línea, el mensaje que da Python (o «no da error» cuando no lo da) y qué lo arregla.

---

## Semana 04 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Cinco líneas de almacén**

Llegó un embarque y alguien escribió esto para revisarlo. Predice las cinco líneas de salida.

```python
unidades = 4300
por_caja = 24
precio = "1250"

print(unidades // por_caja)
print(unidades % por_caja)
print(2 ** 5)
print(precio + "0")
print(type(unidades / por_caja))
```

Explica en un renglón por qué la cuarta línea no imprime 1260, y en otro por qué la quinta dice `float` si los dos números eran enteros.

### 04.2 · Aplicar

**Costo por caja del embarque**

El embarque trae 4,300 unidades que se empacan de 24 en 24. El precio unitario llegó del sistema como el texto `"18.75"` y el flete de toda la operación costó 3,200 pesos.

Escribe un programa que declare esas cuatro variables con el tipo que les toca e imprima seis renglones: cajas completas, piezas sueltas, costo de la mercancía, el costo por caja calculado como `costo / cajas + flete`, el costo por caja calculado como `(costo + flete) / cajas`, y el tipo del precio y el de las cajas.

Salen 179 cajas completas y sobran 4 piezas. Las dos versiones del costo por caja dan 3650.42 y 468.3. Explica en dos renglones cuál de las dos contesta «cuánto me cuesta poner una caja en el andén», y por qué la otra corre igual de bien y responde otra pregunta.

### 04.3 · Integrar

**Orden de compra con IVA**

La orden de octubre junta cinco proveedores y 3,400 piezas que viajan en tarimas de 48.

```python
proveedores = ["Papelera del Centro", "Insumos Aurora",
               "Distribuidora Sol", "Comercial Bravo", "Grupo Nardo"]
costos = [18420.50, 9375.00, 24680.75, 6120.25, 15302.50]
```

Escribe un programa que imprima seis renglones: cuántos proveedores entran en la orden, el subtotal, el total con IVA del 16 %, el costo por pieza, cuántas tarimas completas salen y cuántas piezas sobran, y el tipo del subtotal y el de las tarimas.

El IVA se aplica con `*=` sobre una variable que empieza valiendo el subtotal, no escribiendo el resultado a mano. El subtotal es 73,899.00 y el total con IVA es 85,722.84. Las cifras de dinero llevan separador de miles y dos decimales.

---

## Semana 05 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Cinco formatos sobre la misma campaña**

Predice las cinco líneas que imprime este programa. Escríbelas respetando espacios, comas y símbolos.

```python
impresiones = 248910
conversion = 0.0273
inversion = 41250.5

print(f"{impresiones:,}")
print(f"{conversion:.1%}")
print(f"${inversion:,.2f}")
print("Alcance: {impresiones:,}")
print(f"|{impresiones:>12,}|")
```

La cuarta línea no imprime lo que su autor esperaba. Di qué le falta y por qué Python no lo marca como error.

### 05.2 · Aplicar

**Reporte de campaña que se pueda mandar**

Escribe un programa que pida por teclado cuatro datos de una campaña: nombre, impresiones, clics e inversión. Cada `input` lleva su mensaje, y los tres numéricos se convierten al recibirlos, no después.

El reporte que imprime son cinco renglones: nombre de la campaña, impresiones con separador de miles, conversión en porcentaje con dos decimales, costo por clic con símbolo de pesos y dos decimales, y costo por mil impresiones con el mismo formato.

Corre el programa con la campaña «Verano Bajío»: 248910 impresiones, 6795 clics y 52400 de inversión. La conversión da 2.73 % y el costo por clic da $7.71. Entrega el archivo y la captura de la corrida.

### 05.3 · Integrar

**Flujo de efectivo de la semana**

La sucursal cierra su semana y quiere el reporte en columna, alineado, para pegarlo en el correo del lunes.

Escribe un programa que pida cuatro datos por teclado: número de semana, ingresos, egresos y clientes atendidos. Con eso calcula el saldo, el margen (saldo entre ingresos), el ticket promedio (ingresos entre clientes) y el saldo por día, dividiendo entre siete.

La salida son siete renglones: un encabezado con el número de semana y seis renglones con la etiqueta alineada a la izquierda en 22 espacios y la cifra a la derecha en 14. El dinero lleva miles y dos decimales, y el margen va en porcentaje con un decimal.

Pruébalo con la semana 14: ingresos de 186400, egresos de 143750 y 612 clientes. El saldo es 42,650.00, el margen 22.9 % y el ticket promedio 304.58.

---

## Semana 06 · Estructuras de selección

### 06.1 · Reconocer

**El límite exacto de la rotación**

Recursos humanos clasifica la rotación anual de cada área con este programa.

```python
rotacion = 0.18

if rotacion >= 0.25:
    nivel = "Crítica"
elif rotacion >= 0.18:
    nivel = "Alta"
elif rotacion >= 0.10:
    nivel = "Normal"
else:
    nivel = "Baja"

print(f"{rotacion:.1%} · {nivel}")
```

Escribe la línea exacta que imprime. Después llena una tabla con lo que imprimiría si `rotacion` valiera 0.25, 0.099 y 0.30, y contesta qué área quedaría mal clasificada si el segundo `elif` usara `>` en lugar de `>=`.

### 06.2 · Aplicar

**Semáforo de proveedores**

Compras evalúa a cada proveedor por el porcentaje de entregas a tiempo del trimestre, con cuatro categorías excluyentes:

| Entregas a tiempo | Categoría |
|---|---|
| 95 % o más | Preferente |
| De 85 % a 94.9 % | Confiable |
| De 70 % a 84.9 % | En observación |
| Menos de 70 % | En revisión de contrato |

Escribe un programa que pida el nombre del proveedor y su porcentaje como proporción (0.96 para 96 %), y que imprima un solo renglón con el nombre, el porcentaje con un decimal y la categoría.

Entrega tres corridas: Insumos Aurora con 0.96, Distribuidora Sol con 0.85 y Comercial Bravo con 0.62. La segunda es la que importa, porque cae exactamente en la frontera.

### 06.3 · Integrar

**Desviación presupuestal por centro de costo**

Finanzas revisa cada centro de costo comparando lo ejercido contra lo presupuestado. La desviación es `(ejercido - presupuesto) / presupuesto`, y se clasifica así:

| Desviación | Estado |
|---|---|
| Más de 10 % | Sobregiro |
| De 0 % a 10 % | Al límite |
| De menos 15 % a menos de 0 % | Dentro de rango |
| Menos de menos 15 % | Subejercicio |

Escribe un programa que pida el nombre del centro de costo, su presupuesto y su gasto ejercido, y que imprima cinco renglones: centro de costo, presupuesto, ejercido, desviación en porcentaje con un decimal, y estado. El dinero lleva símbolo de pesos, miles y dos decimales.

Corre el programa con Logística: presupuesto de 480000 y ejercido de 521000. La desviación es 8.5 % y el estado es «Al límite». Explica en dos renglones por qué un sobregiro del 8.5 % no entra en la primera categoría.

---

## Semana 07 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**La condición que siempre se cumple**

Este programa clasifica plazas comerciales y su primera línea de salida sorprende a quien lo escribió. Predice las cinco líneas.

```python
region = "Bajío"
antiguedad = 30
ingreso = 48000

if region == "Norte" or "Occidente":
    print("Plaza consolidada")
else:
    print("Plaza en desarrollo")

print(antiguedad >= 24 and ingreso >= 50000)
print(antiguedad >= 24 or ingreso >= 50000)
print(not (region in ["Norte", "Occidente"]))
print(region in ["Norte", "Occidente", "Bajío"])
```

Explica en dos renglones qué evalúa Python en la condición del `if` y escribe la versión corregida, la que sí compara la región contra los dos valores.

### 07.2 · Aplicar

**Política de crédito con tres condiciones**

Crédito y cobranza aprueba una línea a un cliente con estas reglas, en este orden:

1. Aprobado si gana 25,000 o más al mes, tiene 24 meses o más de antigüedad, su giro está en la lista de elegibles y su historial está limpio.
2. Aprobado por ingreso si gana 60,000 o más y su historial está limpio, sin importar antigüedad ni giro.
3. Rechazado por historial si el historial no está limpio.
4. Rechazado en cualquier otro caso.

Los giros elegibles son Comercio, Manufactura y Servicios, y viven en una lista, no en una cadena de `or`.

Escribe el programa. Pide por teclado nombre, ingreso mensual, antigüedad en meses, giro e historial, y usa `and`, `or` e `in` al menos una vez cada uno. Imprime un renglón con el nombre y el resultado.

Entrega tres corridas: Abarrotes La Paz (31500, 36 meses, Comercio, historial limpio), Taller Mecánico Rueda (72000, 14 meses, Servicios, historial limpio) y Constructora Zafiro (84000, 60 meses, Construcción, historial manchado). Salen aprobado, aprobado por ingreso y rechazado por historial.

### 07.3 · Integrar

**Evaluación de proveedores con contrato**

Compras decide qué hacer con cada proveedor. La primera pregunta es si tiene contrato vigente, porque el cumplimiento de quien ya no tiene contrato no sirve para decidir nada.

Con contrato vigente: si cumple 95 % o más, se amplía volumen; si cumple de 85 % a 94.9 %, se mantiene; abajo de 85 %, se audita y se reduce volumen. Sin contrato vigente, la única acción es renovar antes de evaluar.

Aparte de eso, si el proveedor está en la lista de críticos y su cumplimiento está por debajo del 85 %, se levanta la alerta de buscar segunda fuente. Los proveedores críticos son Insumos Aurora y Grupo Nardo.

Escribe el programa con las tres entradas por teclado y dos renglones de salida: nombre con porcentaje y acción, y la alerta. Entrega dos corridas: Insumos Aurora con contrato vigente y 0.82, y Distribuidora Sol sin contrato y 0.97.

Agrega media cuartilla contestando esto: la parte de la alerta se escribió con un `if` de dos condiciones unidas con `and`. Escríbela también anidada y di cuál de las dos leerías mejor dentro de seis meses.

---

## Semana 08 · Repetición · Primer parcial

### 08.1 · Reconocer

**Cuántas vueltas dan estos dos ciclos**

Predice la salida completa. Son cuatro líneas.

```python
for trimestre in range(3, 12, 4):
    print(trimestre)

fondo = 480000
gasto = 96000
mes = 0

while fondo >= gasto:
    fondo -= gasto
    mes += 1

print(mes, fondo)
```

Escribe además la traza de las últimas dos vueltas del `while`, con las columnas vuelta, fondo al entrar, si se cumple la condición, fondo al salir y mes. Contesta qué cambiaría si la condición dijera `fondo > 0` en lugar de `fondo >= gasto`.

### 08.2 · Aplicar

**Rotación por sucursal**

Recursos humanos tiene el año cerrado en tres listas emparejadas:

```python
sucursales = ["Reforma", "Satélite", "Valle", "Chapalita", "Mitras"]
bajas = [7, 12, 4, 9, 15]
plantilla = [86, 140, 62, 108, 125]
```

Escribe un programa que recorra las cinco sucursales con un `for` y `range(len(...))`, y que imprima un renglón por sucursal con el nombre alineado a la izquierda en 12 espacios, las bajas en 4, la plantilla en 6 y la rotación en 9 con formato de porcentaje y un decimal.

Cierra con un renglón de totales etiquetado «Global», que divide la suma de bajas entre la suma de plantillas. Mitras sale con 12.0 % y el global con 9.0 %.

El programa tiene que seguir funcionando sin tocar el ciclo si mañana se agrega una sexta sucursal.

### 08.3 · Integrar

**Repaso del primer parcial: flujo de efectivo del semestre**

Este ejercicio cruza lo de las unidades 1 a 4. La operación tiene el semestre capturado así:

```python
meses = ["ene", "feb", "mar", "abr", "may", "jun"]
ingresos = [412000, 388500, 455200, 401800, 372900, 468300]
egresos = [398400, 401200, 430600, 418500, 395700, 402100]
```

El programa tiene tres partes.

La primera imprime un encabezado con las columnas Mes, Ingresos, Egresos, Saldo y Estado.

La segunda recorre los seis meses con un `for`, calcula el saldo de cada uno y lo clasifica como «Superávit» si es cero o positivo y «Déficit» si es negativo. Cada renglón lleva las cifras con separador de miles, alineadas a la derecha en 12 espacios. Cierra con un renglón de totales.

La tercera contesta con un `while` cuántos meses aguantaría un fondo de contingencia de 250,000 pesos si el déficit se repitiera a razón de 22,800 pesos al mes, e imprime cuántos meses cubre y cuánto queda sin usar. Son 10 meses y quedan 22,000 pesos.

El semestre cierra con un saldo de 52,200 pesos. Tres de los seis meses salen en déficit.

---

## Semana 09 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Un acumulador que no acumula**

Compras revisó cinco requisiciones con este programa. Predice las cuatro líneas de salida.

```python
compras = [18400, 9375, 24680, 6120, 15302]

for compra in compras:
    total = 0
    total += compra

grandes = 0
hay_urgente = False

for compra in compras:
    if compra > 15000:
        grandes += 1
    if compra > 24000:
        hay_urgente = True

print(total)
print(grandes)
print(hay_urgente)

for compra in compras:
    if compra > 30000:
        print("Requiere autorización del comité")
        break
else:
    print("Ninguna compra pasa por comité")
```

Explica en un renglón por qué la primera línea no imprime 73,877, y en otro por qué el `else` del último ciclo sí corre. Escribe además la corrección de una sola línea que arregla el primer ciclo.

### 09.2 · Aplicar

**Seis campañas en un solo recorrido**

Marketing cerró el trimestre con estas tres listas emparejadas:

```python
campanas = ["Instagram", "Meta", "Google", "TikTok", "Correo", "Display"]
clics = [5074, 3820, 6910, 1240, 2480, 7350]
inversion = [38500, 29800, 51200, 9600, 12400, 61300]
```

Escribe un programa que conteste cinco preguntas con un solo `for`, no con cinco:

1. Cuánto suma la inversión del trimestre.
2. Cuántas campañas rebasan los 3,000 clics.
3. Si existe alguna con costo por clic mayor a 8 pesos.
4. Cuál campaña tiene el mejor costo por clic, y de cuánto es.
5. El costo por clic global, que divide la inversión total entre los clics totales.

La inversión total es $202,800 y la mejor campaña es Correo con $5.00 por clic. El costo por clic global da $7.55, que no es el promedio de los seis costos. Explica en dos renglones por qué esas dos cifras son distintas y cuál reportarías en el comité.

### 09.3 · Integrar

**Tablero de sucursales por trimestre**

Las ventas del año viven en una sola lista de doce cifras, acomodada por renglón: los cuatro trimestres de Norte, luego los cuatro de Centro y luego los cuatro de Occidente.

```python
sucursales = ["Norte", "Centro", "Occidente"]
trimestres = ["T1", "T2", "T3", "T4"]
ventas = [412000, 388000, 455000, 501000,
          298000, 331000, 305000, 362000,
          214000, 240000, 268000, 291000]
```

Escribe un programa con dos ciclos, uno dentro del otro, que imprima el tablero completo en miles de pesos, sin decimales: un renglón por sucursal con sus cuatro trimestres y su total, y un renglón final con el gran total. Norte cierra en 1,756 y el gran total en 4,065.

La cifra de la sucursal `i` y el trimestre `j` está en la posición `i * len(trimestres) + j` de la lista. Ese cálculo tiene que estar escrito así, no con los índices puestos a mano.

Agrega al final un contador de cuántos trimestres del año rebasaron los 400,000 pesos. Son 3 de 12.

---

## Semana 10 · Funciones definidas por el usuario

### 10.1 · Reconocer

**La función que no devuelve nada**

Predice qué imprime este programa, línea por línea, y qué pasa al llegar a la última.

```python
def comision(venta, tasa):
    venta * tasa


def bono(venta):
    base = venta * 0.03
    return base


resultado = comision(180000, 0.05)

print(resultado)
print(bono(180000))
print(base)
```

Contesta tres cosas. Qué le falta a `comision` y qué imprimiría ya corregida. Por qué la tercera línea falla si `base` existe dentro de `bono`. Y qué error saldría, con su nombre exacto, si alguien intentara sumar `resultado + 100`.

### 10.2 · Aplicar

**Punto de equilibrio de tres negocios**

Escribe una función `punto_equilibrio(costos_fijos, precio, costo_variable)` que devuelva cuántas unidades hay que vender para no perder ni ganar. La fórmula divide los costos fijos entre el margen de contribución, que es el precio menos el costo variable.

La función lleva docstring, no imprime nada y solo devuelve el número. Llámala tres veces desde el programa principal e imprime cada resultado con etiqueta, separador de miles y dos decimales:

| Negocio | Costos fijos | Precio | Costo variable |
|---|---|---|---|
| Cafetería | 145,000 | 68.00 | 23.00 |
| Equipo médico | 980,000 | 1,250.00 | 845.00 |
| Taller | 60,000 | 40.00 | 20.00 |

La cafetería necesita 3,222.22 unidades y el taller exactamente 3,000.00. Contesta en dos renglones qué error lanzaría la función si el precio y el costo variable fueran iguales, y qué significa eso en el negocio.

### 10.3 · Integrar

**Tablero de rotación por área**

Escribe dos funciones. `rotacion(bajas, plantilla)` devuelve el índice del periodo como proporción. `clasificar(indice)` devuelve la categoría: «Crítica» con 0.20 o más, «Alta» con 0.15 o más, «Normal» con 0.10 o más y «Baja» abajo de eso. Las dos llevan docstring y ninguna imprime.

Con esas dos funciones y estos datos, imprime la tabla completa:

```python
areas = ["Ventas", "Operaciones", "Administración", "Logística", "Sistemas"]
bajas = [9, 21, 3, 14, 2]
plantilla = [74, 112, 48, 96, 25]
```

Cada renglón lleva el área alineada a la izquierda en 16 espacios, las bajas en 7, la plantilla en 11, la rotación en 10 con porcentaje y un decimal, y la categoría. Cierra con un renglón «Empresa» que use las mismas dos funciones sobre las sumas.

Operaciones sale «Alta» con 18.8 % y la empresa sale «Normal» con 13.8 %. Explica en dos renglones por qué el índice de la empresa no es el promedio de los cinco índices.

---

## Semana 11 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**Un argumento que cae en el lugar equivocado**

Predice las cuatro líneas de salida.

```python
from statistics import mean, median


def costo_total(base, iva=0.16, envio=0):
    return round(base * (1 + iva) + envio, 2)


print(costo_total(12000))
print(costo_total(12000, 350))
print(costo_total(12000, envio=350))

sueldos = [18400, 17950, 42300, 12800, 26500]

print(mean(sueldos), median(sueldos))
```

La segunda línea imprime un número absurdo y el programa no marca ningún error. Explica en dos renglones qué entendió Python del 350 y cómo se escribe la llamada para que signifique lo que su autor quería.

Contesta también por qué el promedio de esos cinco sueldos queda tan arriba de la mediana, y cuál de las dos cifras usarías para decirle a un candidato cuánto se gana en esa área.

### 11.2 · Aplicar

**Costo anual de una plaza**

Escribe una función `costo_nomina(sueldo_base, meses=12, bono=0.0, prestaciones=1.35)` que devuelva el costo anual de una plaza: el sueldo base por los meses, por el factor de prestaciones, por uno más el bono.

Llámala tres veces sobre un sueldo base de 18,400 pesos e imprime cada resultado con etiqueta, símbolo de pesos, miles y dos decimales:

1. La plaza estándar, sin tocar ningún parámetro opcional.
2. La misma plaza con trece meses, pasando el argumento por posición.
3. La misma plaza con un bono del 10 %, pasando el argumento por nombre y saltándose `meses`.

La plaza estándar cuesta $298,080.00 al año y la del bono cuesta $327,888.00. Explica en un renglón qué pasaría si escribieras `costo_nomina(18400, 0.10)` esperando el bono.

### 11.3 · Integrar

**Diagnóstico de nómina de un área**

El área tiene nueve plazas con estos sueldos mensuales:

```python
sueldos = [12800, 15600, 17950, 18400, 19250, 22400, 26500, 33900, 84000]
```

Escribe una función `resumir(etiqueta, valor)` que devuelva, sin imprimir, un renglón con la etiqueta alineada a la izquierda en 22 espacios y el valor a la derecha en 12, con símbolo de pesos, miles y dos decimales.

Usa esa función para imprimir el diagnóstico: nómina mensual, promedio, mediana, sueldo más alto, sueldo más bajo y segundo sueldo más alto. Arriba de todo va un renglón simple con cuántas plazas hay. Al final, una frase que diga cuánto queda el promedio arriba de la mediana.

El promedio y la mediana salen de `statistics`. El segundo sueldo más alto sale de una copia ordenada con `sorted`, sin tocar la lista original. La nómina mensual es $250,800.00 y el promedio queda 8,616.67 arriba de la mediana.

Cierra con tres renglones: qué cifra le reportarías al director de área, cuál al sindicato y por qué las dos son ciertas.

---

## Semana 12 · Listas y tuplas

### 12.1 · Reconocer

**Seis líneas sobre la misma lista**

Este programa toca una lista de inventario de seis formas distintas. Predice las seis líneas de salida.

```python
unidades = [340, 125, 890, 470, 210]

resultado = unidades.sort()
print(resultado)
print(unidades)

respaldo = unidades
respaldo.append(999)
print(len(unidades))

copia = unidades.copy()
copia.clear()
print(len(unidades), len(copia))

print(unidades[1:4])
print(unidades[-2])
```

Contesta tres cosas. Por qué la primera línea no imprime la lista ordenada. Por qué `unidades` mide 6 después de tocar solo `respaldo`. Y qué habría que cambiar en la línea de `respaldo` para que la lista original no se moviera.

### 12.2 · Aplicar

**Los tres SKU que más pesan**

El inventario del almacén central son doce claves con estas piezas:

```python
inventario = [340, 125, 890, 470, 210, 655, 890, 305, 148, 720, 415, 260]
```

Escribe un programa que imprima seis renglones: la lista al inicio, las tres cifras más altas, las piezas totales del inventario, la posición del SKU que tiene 720 piezas, cuántas veces aparece el valor 890, y la lista al final.

La condición que califica el ejercicio es que la primera y la última línea sean idénticas. Ordena sobre una copia, no sobre el original. El inventario suma 5,428 piezas y el SKU de 720 está en la posición 9.

### 12.3 · Integrar

**Las claves que rebasan el umbral**

El catálogo de ocho claves viene en tres listas emparejadas:

```python
skus = ["PAP-100", "PAP-215", "OFI-330", "OFI-412",
        "LIM-501", "LIM-620", "TEC-710", "TEC-844"]
unidades = [1840, 5210, 960, 2375, 3120, 880, 1450, 640]
precios = [38.50, 9.90, 74.00, 22.50, 15.75, 96.20, 58.40, 210.00]
```

Escribe un programa que calcule el importe de cada clave (unidades por precio) y arme una lista nueva, vacía al principio, con las claves cuyo importe llegue o rebase los 70,000 pesos. Cada elemento de esa lista nueva es una tupla de importe y clave, para que el orden se pueda calcular sin perder el nombre.

Ordena esa lista de mayor a menor importe e imprime, en este orden: cuántas claves quedaron de cuántas, un renglón por clave con la clave a la izquierda en 10 espacios y el importe a la derecha en 12 con miles y dos decimales, y un renglón final que compruebe que las listas originales siguen completas y en su orden.

Quedan 5 claves de 8. La primera es TEC-844 con 134,400.00 y la última que entra es PAP-100 con 70,840.00. El umbral se declara una sola vez, en una variable, y aparece también en el texto que se imprime.

---

## Semana 13 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Un catálogo y dos meses de proveedores**

Predice las siete líneas que imprime este programa.

```python
dias_entrega = {"Aurora": 3, "Sol": 7, "Bravo": 5}
dias_entrega["Sol"] = 4
dias_entrega["Nardo"] = 9

print(len(dias_entrega))
print(dias_entrega.get("Sol"))
print(dias_entrega.get("Zafiro"))
print(dias_entrega.get("Zafiro", 15))

marzo = {"Aurora", "Sol", "Bravo"}
abril = {"Sol", "Bravo", "Nardo", "Zafiro"}

print(sorted(marzo & abril))
print(sorted(abril - marzo))
print(len(marzo | abril))
```

Contesta tres cosas. Por qué el diccionario mide 4 y no 5 después de las dos asignaciones. Qué habría pasado con `dias_entrega["Zafiro"]` en lugar de `get`. Y qué operación de conjuntos contesta «qué proveedores facturaron en un mes y no en el otro», sin importar en cuál.

### 13.2 · Aplicar

**Catálogo de plazos de entrega**

Compras tiene los proveedores y sus plazos en dos listas emparejadas:

```python
proveedores = ["Aurora", "Sol", "Bravo", "Nardo", "Zafiro", "Delta"]
dias = [3, 4, 5, 9, 6, 12]
```

Escribe un programa que arme el diccionario con un ciclo, no escribiéndolo a mano, y que después imprima: cuántos proveedores tiene el catálogo, la tabla completa recorrida con `items` (nombre en 10 espacios a la izquierda, plazo en 4 a la derecha, seguido de la palabra días), el plazo promedio, la consulta de Bravo y la consulta de Quintana.

Las dos consultas usan `get` con un valor por omisión de 30 días, que es el plazo del contrato marco para quien no está en el catálogo. Bravo entrega en 5 días y Quintana en 30. El plazo promedio es 6.5 días.

### 13.3 · Integrar

**Repaso del segundo parcial: dos meses de compras**

Este ejercicio cruza lo de las unidades 4, 5 y 6. Cada mes llega como dos listas: quién facturó y cuánto, con proveedores que aparecen más de una vez.

```python
marzo_prov = ["Aurora", "Sol", "Bravo", "Aurora", "Nardo", "Sol"]
marzo_imp = [18400, 9375, 24680, 6120, 15302, 8100]
abril_prov = ["Sol", "Bravo", "Zafiro", "Bravo", "Aurora", "Zafiro"]
abril_imp = [11250, 19800, 7400, 5600, 22150, 9900]
```

Escribe dos funciones con docstring y sin `print` adentro. `consolidar(nombres, importes)` devuelve un diccionario con la compra acumulada por proveedor. `variacion(antes, despues)` devuelve el cambio porcentual entre dos importes.

Con esas dos funciones, imprime el reporte: compra total de marzo, compra total de abril, variación del gasto entre los dos meses, la lista de proveedores nuevos, la lista de los que dejaron de facturar, y una tabla de los que están en los dos meses con su importe de marzo, el de abril y su variación.

Marzo cierra en $81,977 y abril en $76,100, una caída del 7.2 %. El único proveedor nuevo es Zafiro y el único que se fue es Nardo. Las tres comparaciones de proveedores salen de operaciones de conjuntos, no de ciclos con `if`.

---

## Semana 14 · Archivos de texto y CSV

Los tres ejercicios de esta semana trabajan sobre el mismo archivo. Créalo con este contenido exacto, con el nombre `nomina_marzo.csv` y en la misma carpeta que tu programa.

```text
clave,area,puesto,sueldo_mensual,dias_laborados
E-001,Ventas,Ejecutivo,"$18,400.00",30
E-002,Ventas,Ejecutivo,"$17,950.00",28
E-003,Ventas,Gerente,"$42,300.00",30
E-004,Operaciones,Almacenista,"$12,800.00",30
E-005,Operaciones,Almacenista,"$12,800.00",
E-006,Operaciones,Supervisor,"$26,500.00",30
E-007,Administración,Analista,"$21,700.00",30
E-008,Administración,Contador,"$33,900.00",27
E-009,Ventas,Ejecutivo,"$19,250.00",30
E-010,Operaciones,Montacarguista,"$15,600.00",30
E-011,Administración,Analista,"$22,400.00",30
E-012,Ventas,Ejecutivo,"$18,050.00",30
E-013,Operaciones,Almacenista,"$13,900.00",30
E-014,Administración,Coordinador,"$28,300.00",30
E-015,Ventas,Ejecutivo,"$16,700.00",26
```

### 14.1 · Reconocer

**Lo que devuelve un archivo**

Predice las cinco líneas de salida de este programa, corriendo sobre el archivo de arriba.

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent

with (DATOS / "nomina_marzo.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

print(len(filas))
print(filas[0]["clave"], filas[0]["sueldo_mensual"])
print(type(filas[0]["dias_laborados"]))
print(filas[4]["dias_laborados"] == "")
print(filas[-1]["area"], filas[-1]["puesto"])
```

Contesta tres cosas. Por qué la primera línea imprime 15 y no 16. Qué pasaría si alguien cambiara `"utf-8"` por el modo `"w"` en la línea del `open`. Y por qué `int(filas[4]["dias_laborados"])` no lanza cero, sino un error, y cuál.

### 14.2 · Aplicar

**Totales de la nómina de marzo**

Escribe un programa que lea el archivo con `DictReader` y que defina dos funciones de conversión con docstring:

- `a_decimal(texto)` convierte `"$18,400.00"` en el número 18400.0, quitando el símbolo y la coma de miles.
- `a_entero(texto, ausente=0)` convierte a entero y decide qué vale una celda vacía. El valor por omisión de una celda vacía es cero, y esa decisión queda escrita en el docstring.

Con esas dos funciones recorre las filas e imprime cinco renglones: cuántos empleados trae el archivo, la nómina mensual, el sueldo promedio, los días laborados en total y cuántos registros tienen menos de 30 días.

La nómina mensual es $320,550.00 y los días suman 411. El último renglón imprime 4, no 3. Explica en dos renglones a quién está contando de más y por qué la decisión que tomaste en `a_entero` es la responsable.

### 14.3 · Integrar

**Resumen por área, escrito en un archivo nuevo**

Escribe un programa que lea `nomina_marzo.csv`, acumule la nómina y las plazas por área en dos diccionarios, y produzca dos salidas.

La primera es la tabla en pantalla, ordenada por nombre de área, con las columnas Área en 16 espacios a la izquierda, Plazas en 8, Nómina en 14 y Promedio en 13, las dos últimas con miles y dos decimales. Abajo va la lista de claves que traen la celda de días vacía.

La segunda es el archivo `resumen_areas.csv`, escrito desde el programa, con encabezado `area,plazas,nomina,sueldo_promedio` y un renglón por área. El archivo se abre en modo escritura, con `newline=""` y codificación explícita.

Ventas concentra 6 plazas y $132,650.00. Administración tiene el sueldo promedio más alto con $26,575.00. La única clave sin días laborados es E-005.

Cierra con tres renglones que expliquen qué decidiste con la celda vacía, qué otras dos decisiones eran defendibles y cómo cambiaría cada una las cifras que acabas de reportar.

---

## Semana 15 · Series, DataFrame, limpieza, agrupación y unión

Los tres ejercicios de esta semana trabajan sobre el mismo archivo. Créalo con este contenido exacto, con el nombre `ventas_2026.csv`.

```text
fecha,region,canal,unidades,precio_unitario
2026-01-12,Norte,Mayoreo,120,"$1,250.00"
2026-01-28,centro,Menudeo,45,"$1,380.00"
2026-02-09, Norte ,Online,80,"$1,250.00"
2026-02-23,Occidente,Mayoreo,150,"$1,190.00"
2026-03-05,NORTE,Menudeo,60,"$1,380.00"
2026-03-19,Centro,Online,,"$1,250.00"
2026-04-02,Sureste,Mayoreo,95,"$1,190.00"
2026-04-16,Norte,Online,110,"$1,250.00"
2026-05-07,Centro,Mayoreo,140,"$1,190.00"
2026-05-21,occidente,Menudeo,55,"$1,380.00"
2026-06-04,Norte,Mayoreo,130,"$1,250.00"
2026-06-18,Sureste,Online,,"$1,250.00"
2026-07-09,Centro,Menudeo,70,"$1,380.00"
2026-07-23,Occidente,Online,85,"$1,250.00"
2026-08-06,Norte,Mayoreo,160,"$1,190.00"
2026-08-20,Centro,Online,90,"$1,250.00"
2026-09-03,Sureste,Menudeo,40,"$1,380.00"
2026-09-17,Occidente,Mayoreo,175,"$1,190.00"
2026-10-01,Norte,Online,105,"$1,250.00"
2026-10-15,Centro,Mayoreo,145,"$1,190.00"
2026-08-06,Norte,Mayoreo,160,"$1,190.00"
2026-09-17,Occidente,Mayoreo,175,"$1,190.00"
```

### 15.1 · Reconocer

**Diagnóstico antes de tocar nada**

Predice la salida completa de este programa, incluidos los tipos que infiere pandas.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

ventas = pd.read_csv(DATOS / "ventas_2026.csv")

print(ventas.shape)
print(ventas.dtypes)
print(ventas["unidades"].isna().sum())
print(ventas.duplicated().sum())
print(ventas["region"].nunique())
print(sorted(ventas["region"].unique()))
```

Contesta cuatro cosas, un renglón cada una. Por qué `unidades` salió `float64` y no entero. Por qué `precio_unitario` salió texto. Cuántas regiones distintas hay de verdad en la operación, y cuántas reportaría un `groupby` corrido en este momento. Y si el total de piezas del archivo se puede calcular ya, o todavía no.

### 15.2 · Aplicar

**Las cuatro reparaciones, con su bitácora**

Escribe un programa que cargue el archivo y lo limpie en este orden, imprimiendo un renglón después de cada paso para que quede la bitácora:

1. Al cargar: cuántos renglones, cuántas regiones distintas, cuántos duplicados y cuántas unidades vacías.
2. Después de quitar duplicados: cuántos renglones quedan.
3. Después de normalizar la región con `str.strip` y `str.title`: la lista de regiones que quedaron.
4. Después de convertir el precio a número y la fecha a fecha, y de calcular la columna `importe`: el importe total.
5. Después de resolver los huecos de unidades: cuántos renglones, cuántas piezas y cuánto ingreso, más el ticket promedio y los tipos finales de todas las columnas.

El archivo empieza con 22 renglones y 8 regiones, y termina con 18 renglones y 4 regiones. El ingreso es $2,301,950.00 y el ticket promedio $127,886.11.

El punto 4 y el punto 5 reportan el mismo ingreso. Explica en dos renglones por qué quitar los renglones con unidades vacías no movió ni un peso el total, y qué sí cambió con esos dos renglones fuera.

### 15.3 · Integrar

**Tablero de avance contra meta**

Con el archivo ya limpio, produce tres salidas.

La primera es el resumen por región, con `groupby` y `agg`, con cuatro columnas que tú nombras: ingreso, piezas, operaciones y ticket promedio, ordenado por ingreso de mayor a menor.

La segunda es la rejilla de región contra canal con `pivot_table`, sumando importe, con totales de renglón y de columna, expresada en miles con un decimal. Una de las celdas sale vacía: di cuál y por qué.

La tercera es el tablero de avance. El catálogo de plazas vive en el propio programa, con esta información:

| region | gerente | meta |
|---|---|---|
| Norte | Lucía Ramos | 900,000 |
| Centro | Iván Peña | 700,000 |
| Occidente | Marta Ocampo | 650,000 |
| Sureste | Diego Salas | 250,000 |
| Golfo | Rocío Trejo | 200,000 |

Antes de unir, audita la unión en las dos direcciones con `indicator` y reporta los tres conteos. Después une con el modo seguro y agrega la columna de avance, que divide el ingreso entre la meta.

Norte cierra en 106.0 % de su meta y Sureste en 67.3 %. La auditoría marca una región de solo un lado: di cuál es, de qué lado está y por qué eso no es un error de datos. Di también qué habría pasado con esa región si hubieras unido con `inner` sin auditar.

---

## Semana 16 · Visualización, matplotlib y seaborn

### 16.1 · Reconocer

**La barra que dice otra cosa**

El resumen por región del archivo limpio de la semana pasada quedó así:

| region | ingreso (suma) | ticket (promedio) | operaciones |
|---|---|---|---|
| Norte | 954,450.00 | 136,350.00 | 7 |
| Centro | 610,350.00 | 122,070.00 | 5 |
| Occidente | 568,900.00 | 142,225.00 | 4 |
| Sureste | 168,250.00 | 84,125.00 | 2 |

Alguien va a presentar esta línea en el comité:

```python
sns.barplot(data=ventas, x="region", y="importe", ax=ax)
```

Contesta cuatro cosas. Qué cifra dibuja esa barra para cada región, con los cuatro números tomados de la tabla. En qué orden queda el ranking de esa gráfica y en qué orden quedaría la de ingreso total. Qué le falta a la llamada para que dibuje el total. Y qué frase de una línea usarías como título si quisieras que el lector se llevara las dos lecturas.

Contesta además, un renglón cada una, qué está mal en estas tres decisiones de gráfica:

```python
ax.set_ylim(500000, 1000000)
ax.plot(["Norte", "Centro", "Occidente", "Sureste"], ingresos)
ax.pie(ingresos, labels=regiones, autopct="%1.0f%%")
```

### 16.2 · Aplicar

**Estacionalidad del año en una barra**

Comercializadora Aurora cerró 2026 con este ingreso mensual:

```python
MESES = ["ene", "feb", "mar", "abr", "may", "jun",
         "jul", "ago", "sep", "oct", "nov", "dic"]

ingreso = pd.Series(
    [1284000, 962000, 1431000, 1189000, 1516000, 1340000,
     1208000, 1377000, 1465000, 1623000, 2048000, 3412000],
    index=MESES,
)
```

Produce una gráfica de barras guardada como `estacionalidad_2026.png`, a 150 puntos por pulgada, que cumpla seis condiciones:

1. Las tres barras del último trimestre van en azul fuerte y las otras nueve en azul claro.
2. El título dice el hallazgo con su cifra, y esa cifra se calcula en el código, no se escribe a mano.
3. El eje vertical está etiquetado con la unidad y empieza en cero.
4. Las marcas del eje vertical se leen como 1.5M, no como 1500000.
5. Al pie va la fuente, con el periodo y cuántos meses trae.
6. La figura se cierra al terminar.

El programa imprime además cinco renglones: ingreso del año, peso del último trimestre, peso de diciembre solo, mes más bajo con su cifra y la confirmación de que la imagen quedó guardada.

El año cierra en $18,855,000, el último trimestre pesa 37.6 % y diciembre solo pesa 18.1 %. Entrega la imagen y el archivo que la genera.

### 16.3 · Integrar

**Dos gráficas para el consejo**

Este ejercicio usa los dos archivos del curso: `nomina_marzo.csv` de la semana 14 y `ventas_2026.csv` de la semana 15. Configura el tema de seaborn una sola vez, arriba.

La primera gráfica es una caja y bigotes del sueldo mensual por área, con las áreas ordenadas por mediana de mayor a menor, base en cero, título con el hallazgo y fuente al pie. Se guarda como `sueldos_por_area.png`. Antes de dibujarla, imprime la tabla de conteo, mediana, promedio y máximo por área, que es de donde tiene que salir el título.

La segunda es un mapa de calor de región contra canal sobre el ingreso, en miles de pesos, con el valor escrito dentro de cada celda y sin decimales. Recibe directo la rejilla de `pivot_table` de la semana pasada, sin ninguna preparación extra. Se guarda como `rejilla_region_canal.png`.

Ventas tiene mediana de 18,225.00 y máximo de 42,300.00. Operaciones tiene mediana de 13,900.00 y máximo de 26,500.00.

Escribe al final el texto alternativo de cada gráfica, tres renglones cada uno: qué tipo de gráfica es, qué rango cubre y qué se ve que pasa. Cada cifra que aparezca en el texto alternativo tiene que estar en las tablas que imprimiste.

---

## Semana 17 · Repaso y examen final

### 17.1 · Reconocer

**Cuatro errores que no avisan**

Este programa corre de principio a fin y sus cuatro cifras están mal. Trabaja sobre `ventas_2026.csv` sin limpiarlo.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

ventas = pd.read_csv(DATOS / "ventas_2026.csv")

por_region = ventas.groupby("region")["unidades"].sum()

ventas[ventas["region"] == "Norte"]["canal"] = "Mayoreo"

for piezas in ventas["unidades"]:
    total = 0
    total += piezas

orden = por_region.tolist()
orden = orden.sort()

print(len(por_region))
print(ventas["canal"].value_counts()["Mayoreo"])
print(total)
print(orden)
```

Predice las cuatro líneas de salida y llena esta tabla, un renglón por error:

| Línea | Qué error de los seis del curso es | Qué imprime | Qué se quería imprimir | Cómo se corrige |
|---|---|---|---|---|

El segundo error es el único que además deja un aviso en pantalla. Cópialo tal cual y explica en un renglón por qué un aviso no es lo mismo que un error, y por qué eso lo vuelve más peligroso, no menos.

### 17.2 · Aplicar

**De archivo a hallazgo, en una sola pasada**

Escribe un programa que cargue `ventas_2026.csv`, lo inspeccione, lo limpie, cruce región con canal y cierre con una conclusión.

El orden es fijo: inspeccionar, limpiar, agrupar, concluir. La salida son cinco bloques:

1. El diagnóstico de carga en un renglón: renglones, regiones distintas, duplicados y unidades vacías.
2. El mismo renglón ya limpio: renglones, regiones distintas e ingreso.
3. Las cuatro combinaciones de región y canal con más ingreso, con su número de operaciones.
4. Una frase que diga qué combinación conviene atender primero, con dos cifras: su ingreso y qué porcentaje representa del año.

La combinación líder es Norte en Mayoreo, con $502,900.00, el 21.8 % del ingreso del año. Si tu porcentaje sale distinto, revisa contra qué total lo estás dividiendo.

### 17.3 · Integrar

**Cierre del año con auditoría, tablero y gráfica**

Este es el ejercicio de cierre y se resuelve en un solo archivo con dos funciones y su docstring.

`cargar_limpio(ruta)` recibe la ruta del archivo de ventas y devuelve la tabla lista para analizar, con la fecha convertida y con la columna `importe` ya calculada. `tablero(ventas, catalogo)` recibe la tabla limpia y el catálogo de plazas, y devuelve el avance contra meta por región, ordenado de mayor a menor avance.

El catálogo es el mismo de la semana 15, con las cinco plazas, sus gerentes y sus metas.

El programa produce cuatro salidas.

La primera es la auditoría de la unión en las dos direcciones, con los tres conteos y el nombre de la región que aparece de un solo lado.

La segunda es el tablero, con región, gerente, ingreso, operaciones, ticket promedio, meta y avance. Norte queda en 106.0 % y Occidente en 87.5 %, arriba de Centro por 0.3 puntos aunque venda menos.

La tercera son tres cifras de la operación mensual: cuántos meses tuvieron movimiento, cuál fue el más fuerte y qué porcentaje del año representa. Salen 10 meses, octubre y 13.2 %.

La cuarta es una gráfica de barras del ingreso por región guardada como `cierre_2026.png`, con la región líder resaltada, el título calculado desde los datos, el eje vertical desde cero y en millones, y la fuente al pie diciendo cuántos renglones se analizaron de cuántos.

Cierra con un reporte de media cuartilla: la pregunta que contestaste, qué decidiste con los renglones incompletos y con los duplicados, el hallazgo con sus cifras y una recomendación para el año que entra. Cada decisión de limpieza queda por escrito y cada cifra tiene que poder comprobarse contra la salida del programa.
