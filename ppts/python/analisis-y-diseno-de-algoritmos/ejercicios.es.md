# Ejercicios · Análisis y Diseño de Algoritmos · COM101

Este juego acompaña las diecisiete sesiones del curso y está pensado para el grupo de primer semestre de Ingeniería. Cada semana trae tres ejercicios: Reconocer se contesta leyendo código y prediciendo lo que imprime, Aplicar pide escribir un programa contra una especificación que ya trae sus datos y su resultado esperado, e Integrar amarra el tema de la semana con lo de las semanas anteriores. La dificultad sube dentro de la semana y también a lo largo del semestre, así que el Reconocer de la semana 12 pide más que el Integrar de la semana 4. Todos los problemas ocurren en el mismo lugar: la celda de maquinado C-3, sus cuatro estaciones, los bujes de bronce de 12.00 mm que produce y el banco de metrología donde se miden. Se entrega por Blackboard un archivo `.py` por ejercicio, salvo donde el enunciado pida papel, con la salida tal como la produjo tu programa.

La banda de tolerancia del buje es la misma todo el semestre: nominal 12.00 mm, límite inferior 11.95 mm, límite superior 12.05 mm. Los dos límites se escriben como constantes al principio del programa y no se calculan dentro de una condición.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Los seis turnos de la celda C-3**

La celda de maquinado C-3 produce bujes de bronce. Estas son las piezas buenas de los seis turnos de la semana pasada, en dos listas emparejadas. Sin ejecutar nada, escribe las cuatro líneas que imprime este programa.

```python
turnos = ["T1", "T2", "T3", "T4", "T5", "T6"]
piezas = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(piezas)
promedio = total / len(piezas)
mejor = turnos[piezas.index(max(piezas))]

print(turnos[0], piezas[0])
print(total)
print(promedio)
print(mejor)
```

Después contesta dos cosas. A qué turno corresponde `piezas[3]` y en qué fila estaría ese dato en la hoja de cálculo de donde salió, si la fila 1 son los encabezados. Y qué ocurre si agregas `print(piezas[6])` al final del programa.

### 01.2 · Aplicar

**El resumen de la semana, formateado**

Escribe el programa que resume esos mismos seis turnos e imprime cuatro renglones alineados: piezas de la semana con separador de miles, promedio por turno con un decimal, el mejor turno con su cifra, y cuántas piezas quedó ese turno por encima del promedio.

Las cifras que tiene que dar son 7,990 piezas en la semana, 1,331.7 de promedio y el turno T4 con 1,510, que está 178.3 piezas arriba del promedio. Ningún número se escribe a mano dentro del `print`: los cuatro salen de las dos listas.

### 01.3 · Integrar

**El dato que se recapturó**

Metrología avisa que el turno T3 se capturó mal. No fueron 1120 piezas sino 1320. Corrige el dato en el programa de 01.2, vuelve a correrlo y reporta las tres cifras nuevas al lado de las anteriores.

El programa imprime también el folio del lote que estaban midiendo, `00847`, guardado en una variable de texto.

Contesta después tres cosas, cada una en un renglón. Qué hubiera pasado con ese cambio en una hoja de cálculo y cuál de los cuatro quiebres de la sesión explica la diferencia. Qué se ve en la celda si alguien captura ese folio con formato de número. Y con cuál de los cuatro quiebres tiene que ver eso.

---

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer

**La traza del veredicto de un buje**

El buje nominal mide 12.00 mm y la banda de tolerancia va de 11.95 a 12.05 mm. Este es el pseudocódigo que sigue el banco de metrología con cada pieza que le llega.

```text
INICIO
    LEER diametro

    SI diametro > 12.05 ENTONCES
        veredicto = "Rechazo por exceso"
    SI NO SI diametro < 11.95 ENTONCES
        veredicto = "Rechazo por defecto"
    SI NO
        veredicto = "Aceptada"

    ESCRIBIR veredicto
FIN
```

Escribe la traza completa para tres piezas: una de 12.08 mm, una de 11.94 mm y una de 12.05 mm exactos. En cada una anota qué condiciones se evaluaron, cuáles ni se leyeron y con qué veredicto termina.

Después el operador reordena las ramas de esta forma y afirma que el algoritmo hace lo mismo.

```text
SI diametro >= 11.95 ENTONCES
    veredicto = "Aceptada"
SI NO SI diametro > 12.05 ENTONCES
    veredicto = "Rechazo por exceso"
SI NO
    veredicto = "Rechazo por defecto"
```

Traza la pieza de 12.08 mm contra esta segunda versión y di con qué veredicto sale. Explica en dos renglones por qué esta versión cumple las cinco propiedades de un algoritmo y aun así no se puede usar en el banco.

### 02.2 · Aplicar

**El arranque de la celda, en papel**

Escribe el algoritmo de la verificación previa al arranque de la celda C-3, en pseudocódigo y en diagrama de flujo. La secuencia revisa tres cosas en este orden: que la guarda esté cerrada, que el paro de emergencia esté liberado y que la temperatura del husillo esté por debajo de 68 °C. Si las tres se cumplen, arma la celda. Si alguna falla, nombra cuál falló y deja la celda enclavada.

Entrega el pseudocódigo con las palabras del curso, el diagrama con los cuatro símbolos, y la traza esperada de dos casos: guarda cerrada, paro liberado y 61 °C; y guarda cerrada, paro liberado y 71 °C. Sin computadora.

### 02.3 · Integrar

**Una instrucción que no es un algoritmo**

En el pizarrón del área de inspección está escrito: «si la pieza se ve fuera de medida, mándala a reproceso».

Aplícale la prueba de las dos personas y explica en dos renglones cuál de las cinco propiedades se rompe y por qué. Después reescríbela como algoritmo, con la banda de 11.95 a 12.05 mm y tres salidas: reproceso si la pieza salió sobrada, chatarra si salió corta y liberar si está dentro.

Identifica por escrito cuáles son los datos de entrada y cuál es la salida. Agrega al final un caso límite que tu primera versión no cubría y di qué le tuviste que cambiar para cubrirlo.

---

## Semana 03 · Temas 1 y 2 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**Tres líneas que se pisan y cuatro archivos que no corren**

Primero, la traza. Escribe cuánto vale `piezas` después de cada línea y qué imprime el programa.

```python
piezas = 1240
piezas = piezas + 85
piezas = piezas * 2

print(piezas)
```

Después, cuatro fragmentos, cada uno guardado en su propio archivo. Para cada uno di si corre. Cuando no corra, di cuál de las cinco reglas de la sesión se rompió, qué tipo de error se lanza y en qué línea lo va a reclamar Python.

```python
# A
lecturas = [1496, 1502]
print(Suma(lecturas))

# B
lecturas = [1496, 1502]
print("promedio:, lecturas)

# C
total = 1496 + 1502
print(total

# D
total = 2998
Print(total)
```

### 03.2 · Aplicar

**El primer programa del tacómetro**

El tacómetro del transportador de la celda registró cinco lecturas en el turno: 1496, 1502, 1488, 1511 y 1494 rpm. Escribe un programa con la anatomía completa de la sesión: un comentario arriba que diga de dónde salen los datos, la importación de `mean` desde `statistics`, la lista de lecturas y tres `print` que muestren el número de muestras, el promedio y la lectura mayor, cada uno con su etiqueta.

El promedio da 1498.2 rpm y la lectura mayor 1511 rpm.

Después rompe tu propio programa de tres formas, una a la vez: quita el paréntesis que cierra un `print`, cambia `print` por `Print` y borra una comilla. Entrega una tabla de tres renglones con el mensaje exacto que dio cada uno, incluida la línea que señaló.

### 03.3 · Integrar

**El pseudocódigo de la semana 2, dicho en Python**

Traduce a Python el pseudocódigo del veredicto de 02.1, con el diámetro guardado en una variable arriba del programa y el resultado impreso con su etiqueta. La traducción es casi línea por línea: cambian cinco palabras y aparecen los dos puntos.

Córrelo tres veces, con 12.05, con 11.94 y con 12.00, y pega las tres salidas. Contesta además dos cosas: por qué la corrida de 12.00 imprime `12.0` y no `12.00`, y qué veredicto daría una pieza de 12.08 mm si intercambias las dos primeras ramas.

---

## Semana 04 · Tema 3 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Ocho líneas de aritmética de charolas**

Las piezas terminadas se acomodan en charolas de 24. Sin ejecutar nada, escribe las ocho líneas que imprime este programa.

```python
piezas = 1240
por_charola = 24

print(piezas / por_charola)
print(piezas // por_charola)
print(piezas % por_charola)
print("12" + "05")
print(int("12") + int("05"))
print(12.00 + 0.05 == 12.05)
print(0.05 * 3 == 0.15)
print(0.05 * 3)
```

Después contesta dos cosas. Qué significan, en charolas y en piezas, los resultados de la segunda y la tercera línea. Y por qué la sexta línea da un resultado y la séptima da el contrario, si las dos comparan decimales que en papel salen exactos.

### 04.2 · Aplicar

**El turno de EST-01, con cada dato en su tipo**

La estación EST-01 cerró el turno del 8 de enero de 2026 con 1240 piezas producidas, 37 rechazadas y 86.4 kWh de consumo. La estación quedó activa y no registró ningún paro.

Declara ocho variables con el tipo que le corresponde a cada dato, incluidas la bandera de estación activa y el último paro, que no existe. Calcula la tasa de rechazo en por ciento y el consumo por pieza en kWh, redondeados a dos y a cuatro decimales. Imprime las dos métricas con su etiqueta y su unidad, y después el `type` de cinco variables para comprobar qué entendió Python.

La tasa de rechazo da 2.98 % y el consumo por pieza 0.0697 kWh. Ningún nombre de variable puede ser de una sola letra.

### 04.3 · Integrar

**Dos paréntesis que cambian la respuesta**

Con los mismos datos de EST-01, alguien quiere saber cuánta energía cuesta cada pieza buena y escribe esto.

```python
por_pieza = consumo_kwh / piezas - rechazos
```

Escribe las dos versiones, la de arriba y la que sí contesta la pregunta, imprime las dos redondeadas a cuatro decimales y di en un renglón qué calcula cada una. Una da un número negativo y la otra 0.0718 kWh.

En el mismo programa resuelve dos cosas más. Cuántas charolas llenas de 24 salen de las piezas buenas y cuántas piezas quedan sueltas, con división entera y residuo. Y qué le pasa al folio del lote, `"00847"`, cuando lo conviertes a entero y lo regresas a texto: imprime los tres valores en una sola línea y explica en un renglón qué se perdió en el camino.

---

## Semana 05 · Tema 4 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Siete líneas de formato**

Sin ejecutar nada, escribe exactamente lo que imprime cada línea, con sus comas, sus decimales y sus espacios.

```python
piezas = 1240
consumo = 86.4
tasa = 37 / 1240

print(f"Piezas: {piezas:,}")
print(f"Consumo: {consumo:,.2f} kWh")
print(f"Rechazo: {tasa:.1%}")
print(f"Rechazo: {tasa:.2%}")
print(f"{'EST-01':<10}{piezas:>8}")
print(f"Tasa cruda: {tasa}")
print("Consumo: {consumo:.2f} kWh")
```

Después explica en un renglón por qué las líneas tercera y cuarta muestran el mismo dato con dos cifras distintas, y en otro qué le falta a la última línea para hacer lo que aparenta.

### 05.2 · Aplicar

**La captura del turno**

Escribe el programa que captura un turno desde el teclado y devuelve el reporte de la estación. Pide cuatro datos, cada uno con su mensaje: la estación, las piezas producidas, las piezas rechazadas y el consumo del turno en kWh. Convierte lo que haga falta antes de operar con ello.

El reporte son cinco renglones con etiqueta: estación, piezas con separador de miles, rechazos, tasa de rechazo con dos decimales de por ciento y consumo por pieza con cuatro decimales.

Prueba con EST-01, 1240, 37 y 86.4. Tiene que dar 2.98 % y 0.0697 kWh. Entrega la sesión completa, con lo que escribiste en la misma línea del mensaje.

### 05.3 · Integrar

**El reporte que se manda a producción**

Amplía el programa anterior para que además calcule el tiempo de ciclo y la energía por pieza buena. El turno dura ocho horas, o sea 28800 segundos, y esa constante va escrita con nombre arriba del programa. El tiempo de ciclo es el turno entre las piezas producidas. La energía por pieza buena son los kWh convertidos a watt hora, repartidos entre las piezas que no se rechazaron.

Las cinco cifras del reporte van alineadas en columna, con el nombre a la izquierda en veintidós espacios y el número a la derecha en diez, cada uno con su formato y su unidad.

Prueba con EST-03, 1512 piezas, 68 rechazos y 112.8 kWh. Tiene que dar 1,444 piezas buenas, 4.50 % de rechazo, 19.05 segundos de ciclo y 78.1 Wh por pieza buena. Entrega la sesión completa.

---

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer

**La pieza que cae justo en el límite**

Dos programas, cada uno con una pieza distinta. Sin ejecutar nada, di qué imprime cada uno y por qué.

```python
# Primero
diametro = 12.05

if diametro > 12.05:
    veredicto = "Rechazo por exceso"
else:
    veredicto = "Aceptada"

print(diametro, veredicto)
```

```python
# Segundo
diametro = 12.08

if diametro >= 11.95:
    veredicto = "Aceptada"
elif diametro > 12.05:
    veredicto = "Rechazo por exceso"
else:
    veredicto = "Rechazo por defecto"

print(diametro, veredicto)
```

El segundo programa acepta una pieza que mide 12.08 mm, tres centésimas arriba del límite superior. Explica en dos renglones por qué la segunda rama nunca se alcanza y escribe el orden correcto de las tres condiciones.

### 06.2 · Aplicar

**El clasificador del banco de metrología**

Escribe el programa que pide por teclado el folio de una pieza y su diámetro medido, y le da uno de tres veredictos: rechazo por exceso si pasa de 12.05 mm, rechazo por defecto si no llega a 11.95 mm, y aceptada en cualquier otro caso. Los dos límites van como constantes con nombre arriba del programa.

La salida es un solo renglón con el folio, el diámetro a dos decimales y el veredicto.

Prueba con cinco piezas y entrega las cinco corridas: 12.06, 11.94, 12.05, 11.95 y 12.00. Las dos que caen exactamente en el límite tienen que salir aceptadas.

### 06.3 · Integrar

**Cinco destinos y un dato imposible**

Producción decide que tres categorías no alcanzan. Una pieza sobrada se puede rectificar mientras no pase de 12.15 mm; arriba de ahí ya no hay material que quitar. Una pieza corta se puede liberar con concesión mientras no baje de 11.85 mm; abajo de ahí es chatarra.

Escribe el clasificador de cinco categorías con esos cinco destinos, más una validación que rechace un dato imposible antes de clasificar nada: cualquier lectura menor o igual a cero, o mayor a 20 mm, sale como dato inválido y manda a revisar el micrómetro. Las cinco fronteras van como constantes con nombre.

Prueba con estas once lecturas y entrega la tabla completa: 12.30, 12.15, 12.06, 12.05, 12.00, 11.95, 11.90, 11.85, 11.80, -3.00 y 25.00. Documenta al final, en una tabla de cinco renglones, qué veredicto le toca al valor exacto de cada frontera y por qué elegiste `>` o `>=` en cada una.

---

## Semana 07 · Tema 4.4 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**Cuatro condiciones que no dicen lo que parecen**

Sin ejecutar nada, escribe las cinco líneas que imprime este programa y explica cada una en un renglón.

```python
estacion = "EST-03"

if estacion == "EST-01" or "EST-03":
    print("Estacion critica")
else:
    print("Estacion normal")

lectura_a = [12.01, 11.98, 12.06]
lectura_b = [12.01, 11.98, 12.06]

print(lectura_a == lectura_b)
print(lectura_a is lectura_b)

piezas = 0
rechazos = 0

if piezas > 0 and rechazos / piezas > 0.03:
    print("Detener la estacion")
else:
    print("Sin datos suficientes")

ultimo_paro = None
print(ultimo_paro is None)
```

Contesta además dos cosas. Qué imprimiría la primera condición si la estación fuera EST-04, y cómo se escribe correctamente. Y por qué el `and` de la tercera condición evita un `ZeroDivisionError` que con `or` sí habría reventado.

### 07.2 · Aplicar

**La política de liberación de lote**

Un lote se libera cuando se cumplen tres cosas a la vez: la estación no está en mantenimiento, el lote trae al menos 500 piezas y la tasa de rechazo no pasa de 3 %. Si no se libera, hay dos caminos: si la estación es de las críticas, que son EST-01 y EST-03, se retiene y se marca como estación crítica que no cumplió; si no, se retiene para inspección al cien por ciento.

Escribe el programa que pide por teclado la estación, las piezas del lote, las rechazadas y si está en mantenimiento, y decide. La lista de estaciones críticas y los dos umbrales van como constantes arriba. La pertenencia se pregunta con `in`, no con una fila de `or`.

Prueba estos cinco casos y entrega las cinco corridas: EST-01 con 1240 y 37 sin mantenimiento; EST-03 con 1512 y 68 sin mantenimiento; EST-04 con 760 y 9 sin mantenimiento; EST-02 con 420 y 5 sin mantenimiento; y EST-01 con 1240 y 37 en mantenimiento.

### 07.3 · Integrar

**El anidado que en realidad era un and**

El paro automático del husillo llegó del proveedor escrito así, con cuatro ramas.

```python
if temperatura > 68.0:
    if vibracion > 4.5:
        accion = "Detener la estacion"
    else:
        accion = "Seguir operando"
else:
    if vibracion > 4.5:
        accion = "Seguir operando"
    else:
        accion = "Seguir operando"
```

Escribe un programa que pida la temperatura del husillo y la vibración por teclado, calcule la acción con esa versión anidada y con la versión colapsada en una sola condición, e imprima las dos junto con un `True` o `False` que diga si coinciden.

Corre los cuatro casos de la tabla de verdad y entrega las cuatro salidas: 70.2 con 5.1; 70.2 con 3.8; 64.0 con 5.1; y 64.0 con 3.8.

Cierra con dos renglones. El primero explica por qué este anidado sí se podía colapsar. El segundo describe un caso de la misma celda donde el anidado no se puede colapsar, y dice qué tienen que tener sus ramas internas para que eso ocurra.

---

## Semana 08 · Tema 4.5 · Repetición · Primer parcial

### 08.1 · Reconocer

**Un for de tres en tres y un tanque que no alcanza**

Sin ejecutar nada, escribe todo lo que imprime este programa y cuántas líneas son.

```python
for velocidad in range(38, 56, 4):
    print(velocidad)

refrigerante = 50.0
consumo_turno = 7.5
turnos = 0

while refrigerante > 0:
    refrigerante -= consumo_turno
    turnos += 1

print(turnos, refrigerante)
```

Después contesta tres cosas. Por qué el `for` no imprime el 56 aunque aparezca en el `range`. Cuántos turnos completos aguanta de verdad el tanque de refrigerante y por qué el número impreso no es ese. Y qué pasaría si borras la línea que resta el consumo.

### 08.2 · Aplicar

**Las cuatro estaciones, en un solo recorrido**

Estos son los datos del turno del 8 de enero, en cuatro listas emparejadas.

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas = [1240, 984, 1512, 760]
rechazos = [37, 12, 68, 9]
consumo = [86.4, 61.5, 112.8, 48.2]
```

Escribe el programa que las recorre una sola vez y produce la tabla del turno: un encabezado y un renglón por estación con la estación, las piezas con separador de miles, la tasa de rechazo con dos decimales de por ciento y los kWh por pieza con cuatro decimales, todo alineado en columnas.

El último renglón es el de la celda completa, con 4,496 piezas, 2.80 % de rechazo y 0.0687 kWh por pieza. Ese renglón se calcula sumando y dividiendo los totales, no promediando las cuatro tasas.

El ciclo tiene que seguir funcionando si mañana se agrega una quinta estación a las cuatro listas, sin tocar una sola línea de adentro.

### 08.3 · Integrar

**Repaso del primer parcial: el lote L-2601 completo**

Este ejercicio cruza lo que entra al parcial: tipos, formato, selección y repetición. Estas son las doce piezas del lote L-2601 con su diámetro medido.

```python
piezas = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
          "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
          "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
```

Escribe el programa que recorre las dos listas emparejadas e imprime un renglón por pieza con su folio, su diámetro a dos decimales y su veredicto, usando las tres categorías de la semana 6 y las constantes de la banda.

Al terminar el recorrido imprime dos renglones más: el diámetro promedio del lote a cuatro decimales, y cuántas piezas quedaron fuera de tolerancia de las doce, con el porcentaje a un decimal. El promedio da 12.0075 mm y salen 3 de 12.

Cierra contestando en dos renglones por qué la pieza BJ-1008, que mide 12.05, no cuenta como fuera de tolerancia, y qué habría pasado con ese conteo si el programa usara `>=` en lugar de `>` en la primera condición.

---

## Semana 09 · Tema 4.5 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Un acumulador que se borra y una búsqueda que sale antes**

Dos programas. Sin ejecutar nada, di qué imprime cada uno.

```python
# Primero
consumos = [86.4, 61.5, 112.8, 48.2]

for consumo in consumos:
    total = 0.0
    total += consumo

print(total)
```

```python
# Segundo
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas = [1240, 984, 1512, 760]
rechazos = [37, 12, 68, 9]

for i in range(len(estaciones)):
    if piezas[i] < 1000:
        continue

    if rechazos[i] / piezas[i] > 0.03:
        print("Primera fuera de control:", estaciones[i])
        break
else:
    print("Ninguna estacion rebasa el limite")
```

Del primero, di cuál era el resultado esperado, cuál sale y qué única línea hay que mover. Del segundo, escribe la traza de las cuatro vueltas diciendo qué pasa en cada una, y explica por qué el `else` del `for` no se ejecuta y en qué caso sí lo haría.

### 09.2 · Aplicar

**Tres preguntas, un solo recorrido**

Con las cuatro listas del turno de 08.2, escribe el programa que contesta tres preguntas distintas en un mismo `for`, con las tres variables declaradas antes del ciclo.

Cuánta energía consumió la celda completa, que es un acumulador. Cuántas estaciones rebasaron la meta de 3 % de rechazo, que es un contador. Y si existe al menos una estación que gaste más de 0.070 kWh por pieza, que es una bandera.

Las tres respuestas se imprimen con etiqueta: 308.9 kWh, 1 estación fuera de meta y la bandera en `True`. Las dos metas van como constantes con nombre.

Cierra explicando en un renglón por qué la segunda pregunta no se puede contestar con un acumulador y la primera no se puede contestar con un contador.

### 09.3 · Integrar

**La proyección de producción, estación por turno**

Ingeniería industrial quiere la proyección de piezas de cada estación en cada uno de los tres turnos del día. Estas son las velocidades y las duraciones.

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas_por_hora = [155, 123, 189, 95]
turnos = ["T1", "T2", "T3"]
horas = [8, 8, 6]
```

Escribe el programa con dos ciclos anidados que imprima un renglón por combinación, con la estación, el turno y la proyección con separador de miles, alineados. Antes de correrlo, escribe en tu cuaderno cuántos renglones deberían salir; si no coincide con lo que imprime, el anidado está mal.

Al terminar imprime dos renglones de resumen: la producción proyectada de la celda, que da 12,364 piezas, y cuántas combinaciones pasan de 1000 piezas, que son 5.

Las variables de los dos ciclos tienen que llamarse distinto y decir qué recorren. Cierra explicando en dos renglones cuántas vueltas daría este programa si la planta tuviera 40 estaciones y 3 turnos, y a partir de qué tamaño empezarías a preocuparte.

---

## Semana 10 · Tema 5 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Una función que calcula bien y no entrega nada**

Sin ejecutar nada, di qué imprime cada una de las tres líneas finales de este programa.

```python
def tasa_rechazo(piezas, rechazos):
    rechazos / piezas


def energia_por_pieza(consumo_kwh, piezas):
    unitario = consumo_kwh * 1000 / piezas
    return unitario


print(tasa_rechazo(1240, 37))
print(energia_por_pieza(86.4, 1240))
print(unitario)
```

Contesta después tres cosas, cada una en un renglón. Qué le falta a la primera función, y por qué el error no aparece dentro de ella sino donde alguien use su resultado. Por qué la tercera línea falla aunque `unitario` sí se calculó. Y qué pasaría si en lugar de `return unitario` la segunda función tuviera `print(unitario)`.

### 10.2 · Aplicar

**Dos cálculos del turno, empaquetados**

Escribe dos funciones con su docstring de un renglón. La primera, `tasa_rechazo(piezas, rechazos)`, devuelve la fracción de piezas rechazadas. La segunda, `dentro_de_tolerancia(diametro)`, devuelve verdadero o falso según la banda de 11.95 a 12.05 mm, que vive en dos constantes fuera de la función.

Ninguna de las dos puede imprimir nada. Solo reciben y devuelven.

Pruébalas con seis llamadas y pega la salida: la tasa de EST-01 con 1240 y 37, la de EST-03 con 1512 y 68, la de un lote de 760 piezas sin ningún rechazo, y la tolerancia de 12.00, de 12.05 y de 12.06. Las tres tasas redondeadas a cuatro decimales dan 0.0298, 0.045 y 0.0.

Cierra explicando en un renglón por qué el caso de 12.05 es el que hay que probar siempre y qué habría pasado si la función usara `<` en lugar de `<=`.

### 10.3 · Integrar

**El lote L-2601, resuelto con funciones**

Vuelve a resolver el ejercicio 08.3, ahora con cuatro funciones y sin repetir una sola condición.

`dentro_de_tolerancia(diametro)` contesta si la pieza está en banda. `veredicto(diametro)` devuelve aceptada, reproceso o chatarra, y por dentro llama a la primera en lugar de volver a comparar. `piezas_aceptadas(diametros)` cuenta cuántas mediciones de una lista caen dentro. `diametro_promedio(diametros)` devuelve el promedio.

Ninguna función imprime. El programa principal recorre las doce piezas del lote, imprime el renglón de cada una y cierra con tres líneas: medidas, aceptadas y promedio. Salen 12 medidas, 9 aceptadas y 12.0075 mm.

Cierra con dos renglones. Bórrale al cuerpo de `dentro_de_tolerancia` la comparación con el límite inferior y di cuál de tus cuatro pruebas lo detecta; si ninguna lo detecta, agrega la que falta y dilo.

---

## Semana 11 · Tema 5 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**El argumento que cayó en el lugar equivocado**

Sin ejecutar nada, escribe los tres números que imprime este programa, redondeados a dos decimales, y di a qué parámetro llegó el 5.0 en cada llamada.

```python
def energia_por_pieza(consumo_kwh, piezas, factor=1000, perdidas=0.0):
    return consumo_kwh * factor / piezas + perdidas


print(energia_por_pieza(86.4, 1240))
print(energia_por_pieza(86.4, 1240, 5.0))
print(energia_por_pieza(86.4, 1240, perdidas=5.0))
```

La segunda llamada devuelve un número que no se parece en nada a los otros dos. Explica en dos renglones qué pasó, por qué Python no marcó ningún error, y qué le pasaría a la definición si movieras `factor=1000` antes de `piezas`.

### 11.2 · Aplicar

**Una función que sirve para más de un buje**

La celda también maquina bujes de 8.00 mm con la misma tolerancia, y a veces produce una corrida especial con tolerancia abierta de 0.10 mm. Escribe `fuera_de_tolerancia(diametro, nominal=12.00, tolerancia=0.05)`, con su docstring, que calcule los dos límites por dentro y devuelva verdadero cuando la pieza se sale.

Pruébala con cinco llamadas: 12.06 con los valores por omisión; 12.05 con los valores por omisión; 12.06 con nominal y tolerancia dados por posición; 12.06 pasando solo la tolerancia por nombre; y 8.02 pasando solo el nominal por nombre.

Agrega al final dos líneas que comprueben, antes de confiar en la función, que `12.00 - 0.05` da exactamente 11.95 y que `12.00 + 0.05` da exactamente 12.05. Explica en un renglón por qué esa comprobación no sobra, aunque en este caso las dos salgan verdaderas.

### 11.3 · Integrar

**Lo que el promedio del lote no dice**

Con las doce mediciones del lote L-2601, escribe el programa que importa `mean`, `median` y una tercera función del módulo `statistics` que no vimos en clase, y que sirva para medir qué tan dispersas están las lecturas. Busca esa tercera función en docs.python.org y cita la página.

El programa imprime siete renglones: número de mediciones, promedio, mediana y dispersión a cuatro decimales, la menor y la mayor a dos, y el índice de capacidad, que es el ancho de la banda de tolerancia entre seis veces la dispersión. Da 12.0075 de promedio, 12.0050 de mediana, 0.0406 de dispersión y un índice de 0.41.

Al final, repite el promedio y la mediana sobre una lista de trece valores, la misma más una lectura de 12.90 mm que alguien capturó con el micrómetro mal ajustado. Uno de los dos números se mueve mucho más que el otro.

Cierra con tres renglones: qué significa un índice de capacidad de 0.41 para el proceso, qué le dirías al jefe de producción con esa cifra, y cuál de las dos medidas de centro reportarías cuando sospechas de una lectura mal tomada.

---

## Semana 12 · Tema 6 · Listas y tuplas

### 12.1 · Reconocer

**Un método que ordena y borra el respaldo**

Sin ejecutar nada, escribe las ocho líneas que imprime este programa y qué pasa en la última.

```python
diametros = [12.01, 11.98, 12.06, 12.00, 11.94]

print(diametros[0], diametros[-1])
print(diametros[1:3])
print(sorted(diametros))
print(diametros)

ordenados = diametros.sort()
print(ordenados)
print(diametros)

respaldo = diametros
copia = diametros.copy()
diametros.append(12.10)

print(len(respaldo), len(copia))
print(diametros[6])
```

Contesta además tres cosas. Por qué `diametros[1:3]` devuelve dos valores y no tres. Por qué `respaldo` y `copia` terminan con distinto número de elementos, si las dos se crearon en el mismo momento. Y qué habría pasado con los datos si en lugar de `ordenados = diametros.sort()` alguien escribe `diametros = diametros.sort()`.

### 12.2 · Aplicar

**Cuatro preguntas sobre la columna de diámetros**

Con las doce mediciones del lote L-2601, escribe el programa que imprime la lista al principio, contesta cuatro preguntas y vuelve a imprimir la lista al final, que tiene que salir idéntica.

La medición mayor y la menor. Las tres mediciones más altas, ordenadas de mayor a menor. En qué posición está la lectura de 11.94 y a qué folio corresponde, sabiendo que la primera pieza es la BJ-1001. Y las últimas tres mediciones del lote, con una rebanada.

Las tres más altas son 12.08, 12.06 y 12.05. La lectura de 11.94 está en la posición 4 y le toca la pieza BJ-1005.

### 12.3 · Integrar

**Las piezas fuera de banda, sin tocar el original**

Escribe el programa que recorre las doce mediciones y arma una lista nueva con las que se salen de la banda, sin modificar la lista original. Después la ordena de mayor a menor y la imprime.

La banda va en una tupla de tres valores, `(12.00, 11.95, 12.05)`, que es nominal, límite inferior y límite superior. Todas las comparaciones leen esa tupla por posición.

El reporte son cinco renglones: la banda con sus tres cifras, cuántas mediciones se revisaron, cuántas se salieron, la lista de las que se salieron ordenada de mayor a menor, y la lista original completa para comprobar que quedó intacta. Salen 3 de 12, y la lista de fuera de banda es 12.08, 12.06 y 11.94.

Cierra con una línea que intente cambiar el límite superior de la tupla a 12.10 y pega el error completo que lanza. Explica en un renglón por qué conviene que la banda esté en una tupla y no en una lista.

---

## Semana 13 · Tema 6 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Un catálogo que crece y un código que no existe**

Sin ejecutar nada, escribe las nueve líneas que imprime este programa y qué pasa en la última.

```python
defectos = {"D01": "Diametro fuera de tolerancia",
            "D02": "Rugosidad excesiva",
            "D03": "Rebaba en el chaflan"}

defectos["D02"] = "Rugosidad arriba de Ra 1.6"
defectos["D04"] = "Golpe en la cara frontal"

print(len(defectos))
print(defectos["D02"])
print(defectos.get("D09"))
print(defectos.get("D09", "Codigo no catalogado"))

turno_a = {"D01", "D02", "D01", "D03"}
turno_b = {"D02", "D03", "D05"}

print(len(turno_a))
print(sorted(turno_a & turno_b))
print(sorted(turno_a - turno_b))
print(sorted(turno_a ^ turno_b))
print(defectos["D09"])
```

Contesta además dos cosas. Por qué el diccionario termina con cuatro entradas si se le asignaron dos códigos después de crearlo. Y por qué `turno_a` tiene tres elementos si la lista de la que salió trae cuatro.

### 13.2 · Aplicar

**El catálogo de defectos de la celda**

Arma el diccionario de los seis códigos de defecto que maneja la celda: D01 diámetro fuera de tolerancia, D02 rugosidad arriba de Ra 1.6, D03 rebaba en el chaflán, D04 golpe en la cara frontal, D05 concentricidad fuera de norma y D06 marca de herramienta.

El turno reportó estos ocho códigos, en este orden: D01, D03, D01, D05, D01, D02, D03 y D09.

Escribe el programa que imprime el catálogo completo recorriéndolo con `items`, después tres cifras con etiqueta (códigos catalogados, piezas reportadas y códigos distintos reportados), y al final la lista de los códigos distintos ordenada, cada uno con su descripción.

La consulta de la descripción tiene que usar `get` con un valor por omisión, porque D09 no está en el catálogo y el programa no se puede detener ahí. Salen 6 códigos catalogados, 8 piezas reportadas y 5 códigos distintos.

### 13.3 · Integrar

**Repaso del segundo parcial: el tablero del turno**

Este ejercicio cruza lo que entra al parcial: repetición, funciones y colecciones. Los datos son estos.

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
consumo = [86.4, 61.5, 112.8, 48.2]
piezas = [1240, 984, 1512, 760]

reportados_a = ["D01", "D03", "D01", "D05", "D01", "D02", "D03"]
reportados_b = ["D02", "D02", "D06", "D03", "D01"]
```

Primero, arma con un ciclo el diccionario que va de estación a consumo. No se escribe a mano. Imprímelo con `items`, saca el total con `values` y encuentra la estación más cara recorriendo el diccionario, no a ojo. El total da 308.9 kWh y la estación más cara es EST-03 con 112.8.

Segundo, cuenta cuántas veces aparece cada código del turno A usando un diccionario como contador, con `get` y un valor por omisión de cero. Imprímelo ordenado por código.

Tercero, compara los códigos de los dos turnos con operaciones de conjuntos, nunca con un ciclo y un `if`: los que aparecieron en los dos, los que solo están en el turno A, los que aparecieron nuevos en el turno B y los que están en uno pero no en ambos.

Cierra con dos renglones: qué decisión de mantenimiento tomarías con el código que apareció nuevo en el turno B, y por qué el conteo del turno A no se podía hacer con un conjunto.

---

## Semana 14 · Tema 7 · Archivos de texto y CSV

### 14.1 · Reconocer

**Lo que devuelve un CSV, y de qué tipo**

Las cuatro semanas que quedan trabajan sobre el mismo archivo. Créalo con el nombre `mediciones.csv`, guardado en la misma carpeta que tus programas y codificado en UTF-8. Son 30 renglones del banco de metrología de la celda C-3, exportados tal como salieron del sistema, con tres días de mediciones y tres lotes.

```text
fecha,estacion,lote,diametro_mm,ciclo_s,energia_kj
2026-01-08,EST-01,L-2601,12.01,44,"1,240 kJ"
2026-01-08,EST-02,L-2601,11.98,39,980 kJ
2026-01-08, EST-01,L-2601,12.06,46,"1,310 kJ"
2026-01-08,EST-03,L-2601,12.00,51,"1,505 kJ"
2026-01-08,est-01,L-2601,11.94,,"1,190 kJ"
2026-01-08,EST-04,L-2601,12.03,38,760 kJ
2026-01-09,EST-01,L-2602,11.99,45,"1,260 kJ"
2026-01-09,EST-02,L-2602,12.05,41,"1,020 kJ"
2026-01-09,EST-03,L-2602,12.08,52,"1,540 kJ"
2026-01-09,EST-01 ,L-2602,12.02,43,"1,225 kJ"
2026-01-09,EST-04,L-2602,11.96,,745 kJ
2026-01-09,EST-03,L-2602,11.97,50,"1,480 kJ"
2026-01-12,EST-01,L-2603,12.04,44,"1,255 kJ"
2026-01-12,est-02,L-2603,12.07,40,"1,005 kJ"
2026-01-12,EST-03,L-2603,11.95,49,"1,460 kJ"
2026-01-12,EST-04,L-2603,12.00,37,735 kJ
2026-01-12,EST-01,L-2603,11.93,47,"1,330 kJ"
2026-01-12,EST-02,L-2603,12.01,,995 kJ
2026-01-08,EST-02,L-2601,12.02,40,"1,010 kJ"
2026-01-08,EST-03,L-2601,12.09,53,"1,575 kJ"
2026-01-09,EST-01,L-2602,11.99,45,"1,260 kJ"
2026-01-09,EST-04,L-2602,12.03,39,755 kJ
2026-01-12,EST-03,L-2603,12.02,48,"1,435 kJ"
2026-01-12,EST-04,L-2603,11.98,38,742 kJ
2026-01-08,EST-04,L-2601,12.05,37,730 kJ
2026-01-09,EST-02,L-2602,11.95,42,"1,035 kJ"
2026-01-12,EST-01,L-2603,12.04,44,"1,255 kJ"
2026-01-08,EST-03 ,L-2601,11.91,54,"1,610 kJ"
2026-01-09,EST-03,L-2602,12.06,51,"1,520 kJ"
2026-01-12,EST-02,L-2603,11.97,41,"1,015 kJ"
```

Sin ejecutar nada, escribe las seis líneas que imprime este programa.

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent

with (DATOS / "mediciones.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

print(len(filas))
print(filas[0]["estacion"], filas[0]["diametro_mm"])
print(type(filas[0]["diametro_mm"]))
print(filas[0]["diametro_mm"] + filas[1]["diametro_mm"])
print(filas[4]["ciclo_s"] == "")
print(filas[2]["estacion"] == "EST-01")
```

Contesta después tres cosas, cada una en un renglón. Por qué la cuarta línea no lanza ningún error a pesar de estar sumando mal. Por qué la sexta línea da falso si en el archivo ese renglón dice EST-01. Y qué le pasaría al archivo si esa misma apertura llevara `"w"` en lugar del modo por omisión.

### 14.2 · Aplicar

**El resumen por estación, leyendo por nombre de columna**

Escribe el programa que lee `mediciones.csv` con `DictReader` y produce el resumen del banco. Necesitas tres funciones cortas, cada una con su docstring: una que convierta la energía a decimal quitándole la coma de miles y la unidad, una que convierta el tiempo de ciclo a entero y devuelva la ausencia de dato como `None` cuando la celda viene vacía, y una que normalice el nombre de la estación quitándole los espacios de los extremos y dejando una sola forma de escribirlo.

El programa imprime primero cuatro renglones de diagnóstico: renglones leídos, renglones sin tiempo de ciclo, formas distintas de escribir la estación y estaciones que quedan después de normalizar. Son 30 renglones, 3 sin tiempo de ciclo, y las 9 formas se reducen a 4 estaciones.

Después imprime la tabla por estación, ordenada por nombre, con piezas medidas, energía total en kJ y diámetro promedio a cuatro decimales, más el renglón de la celda completa. Con el archivo tal como viene, la celda suma 34,977 kJ en 30 mediciones.

Las rutas se arman desde la ubicación del archivo, nunca escritas a mano.

### 14.3 · Integrar

**Limpiar, decidir y escribir el archivo de salida**

Ahora el mismo archivo se procesa con criterio de ingeniería y el resultado se guarda.

El programa quita los renglones exactamente duplicados comparando el renglón completo y no una sola columna, normaliza la estación, convierte la energía, y marca cada pieza como fuera de tolerancia cuando su diámetro se sale de la banda. Los renglones que no traen tiempo de ciclo se conservan, porque su diámetro sí se midió y esa es la variable que decide si la pieza sirve; el programa reporta cuántos son y deja escrita la decisión.

Imprime seis cifras de bitácora: 30 renglones en el archivo, 2 duplicados exactos quitados, 28 renglones que quedaron, 3 renglones sin tiempo de ciclo conservados, 8 piezas fuera de tolerancia y 32,462 kJ de energía de la celda.

Después escribe un archivo nuevo llamado `resumen_estacion.csv`, con encabezado `estacion,piezas,fuera_tolerancia,energia_kj` y un renglón por estación ordenada por nombre. Al escribir un CSV en Windows hay que pasar el parámetro que evita el renglón en blanco entre cada dato. Al final el programa imprime el contenido del archivo que acaba de escribir.

Esa energía es 2,515 kJ menor que la del ejercicio anterior. Explica en dos renglones de dónde sale la diferencia exacta y por qué un duplicado infla el total pero casi no mueve el diámetro promedio.

---

## Semana 15 · Tema 8.1 · Series, DataFrame, limpieza y agrupación

### 15.1 · Reconocer

**Lo que pandas infirió del archivo, y por qué**

Sin ejecutar nada, di qué imprime cada una de las siete instrucciones de este programa, que corre sobre el mismo `mediciones.csv`.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

mediciones = pd.read_csv(DATOS / "mediciones.csv")

print(mediciones.shape)
print(mediciones.dtypes)
print(mediciones["ciclo_s"].isna().sum())
print(mediciones.duplicated().sum())
print(mediciones["estacion"].nunique())
print(mediciones["estacion"].value_counts())
print(mediciones["diametro_mm"].describe().round(3))
```

Contesta después cuatro cosas, cada una en un renglón. Por qué `ciclo_s` salió decimal y no entero, si en el archivo todos los tiempos son números redondos de segundos. Por qué `energia_kj` salió texto. Por qué en la salida de `value_counts` hay dos renglones que se ven idénticos y aun así son entradas distintas. Y qué columnas resume `describe` y cuáles no.

### 15.2 · Aplicar

**Las cuatro reparaciones, con su bitácora**

Escribe el programa que carga `mediciones.csv` con pandas y lo deja listo para analizar, imprimiendo el conteo antes y después de cada reparación.

El orden es este: reportar el estado inicial, quitar duplicados, normalizar la estación con métodos de texto, quitarle la coma de miles y la unidad a la energía y convertirla a decimal, y convertir la fecha a tipo fecha. Imprime los tipos de las seis columnas cuando termines.

Los números que tiene que reportar son 30 renglones al cargar, 2 duplicados, 9 formas de escribir la estación, 3 renglones sin tiempo de ciclo, 28 renglones sin duplicados y 4 estaciones reales.

Después agrega la columna `veredicto`, que vale «Dentro de tolerancia» en todos lados y «Fuera de tolerancia» donde el diámetro se sale de la banda, escrita en un solo paso con `loc`. Salen 20 dentro y 8 fuera.

Cierra con cuatro cifras más: cuántas piezas de EST-03 quedaron fuera de tolerancia, que son 4; cuántas mediciones son de EST-01 o EST-02, que son 14 y se piden con `isin`; la energía total, que da 32,462 kJ; y el ciclo promedio, que da 44.36 segundos. Reporta también con cuántos renglones te quedarías si descartaras los tres sin tiempo de ciclo, y explica en dos renglones por qué en este archivo conviene conservarlos.

Las condiciones combinadas usan los símbolos y sus paréntesis, nunca las palabras.

### 15.3 · Integrar

**El tablero de la celda, la rejilla por lote y la unión auditada**

Encierra toda la limpieza de 15.2 en una función `cargar_limpio()` con su docstring, para no volver a escribirla en lo que queda del semestre.

Primero, agrupa por estación y pide cuatro resúmenes en una sola instrucción: piezas medidas, energía, ciclo promedio y diámetro promedio, redondeados a tres decimales y ordenados por energía de mayor a menor. EST-03 encabeza con 12,125 kJ en 8 piezas.

Segundo, imprime cuántas piezas fuera de tolerancia aportó cada estación. Fíjate en cuántos renglones trae esa tabla y explica en un renglón por qué no son cuatro.

Tercero, arma la rejilla de estación contra lote con la energía sumada, rellenando con cero lo que no tenga registro y agregando los totales de fila y de columna. La celda más cara es el lote L-2601 en EST-03 con 4,690 kJ y el total general da 32,462.

Cuarto, construye este catálogo como DataFrame desde un diccionario de columnas y únelo con el tablero.

```python
catalogo = pd.DataFrame({
    "estacion": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "maquina": ["Torno CNC", "Fresadora CNC", "Rectificadora",
                "Banco de pruebas", "Taladro radial"],
    "ciclo_meta_s": [42, 40, 48, 36, 30],
})
```

Audita la unión en las dos direcciones antes de confiar en ella. Tienen que salir 28 renglones en ambos lados, 1 solo del catálogo y 0 solo de las mediciones. Explica en dos renglones qué significa cada uno de esos tres números para la planta.

Cierra con el tablero de desvío de ciclo: estación, máquina, piezas, ciclo real, ciclo meta y desvío como fracción, redondeado a tres decimales. EST-01 corre 6.7 % arriba de su meta y EST-02 apenas 1.2 %. Escribe en dos renglones qué le reportarías a mantenimiento con esas cifras.

---

## Semana 16 · Tema 8.2 · Visualización con matplotlib y seaborn

### 16.1 · Reconocer

**La barra que dice promedio cuando el asunto dice total**

Alguien de producción armó esta gráfica con el archivo ya limpio y la mandó por correo con el asunto «energía del turno por estación».

```python
sns.barplot(data=mediciones, x="estacion", y="energia_kj", ax=ax)
```

Sin ejecutar nada, contesta qué número está mostrando cada barra, cuánto vale esa barra para EST-01 y cuánto valdría si mostrara lo que dice el asunto, y qué habría que agregarle a la llamada para que muestre el total.

Después escribe el programa corto que imprime las tres tablas que sostienen tu respuesta: la suma, el promedio y el conteo de energía por estación; el promedio, la desviación, el mínimo y el máximo del diámetro por estación, ordenado por desviación; y cuántas piezas fuera de tolerancia aportó cada una.

Cierra eligiendo la gráfica correcta para cada una de estas cuatro preguntas, con un renglón de justificación cada una.

- Cómo se compara la energía de las cuatro estaciones.
- Cómo se repartieron los diámetros medidos dentro de cada estación.
- Cómo se movió el diámetro promedio de la celda a lo largo de los tres días.
- Si las piezas de ciclo más largo son también las que más se salen de medida.

### 16.2 · Aplicar

**La energía de la celda, en una gráfica que viaja sola**

Con el archivo limpio, agrupa la energía por estación y produce una gráfica de barras guardada como `energia_estacion.png` a 150 puntos por pulgada.

La gráfica lleva cinco cosas: el título con el hallazgo y no con el nombre de los ejes, la etiqueta del eje vertical con su unidad, el eje vertical empezando en cero, el eje vertical formateado en miles para que nadie cuente dígitos, y la fuente al pie. La barra de la estación pico va en azul fuerte y las otras tres en azul claro.

EST-03 concentra el 37.4 % de la energía de la celda con 12,125 kJ, y ese porcentaje se calcula dentro del programa, no se escribe a mano en el título.

El programa imprime la serie por estación y una línea que compruebe que el archivo se generó. Cierra la figura al terminar.

Escribe además el texto alternativo de la gráfica, de dos o tres renglones, donde cada cifra que menciones se pueda verificar contra la serie impresa.

### 16.3 · Integrar

**Tres gráficas de seaborn y la historia que cuentan juntas**

Configura el tema de seaborn una sola vez al principio y produce tres imágenes con el archivo limpio.

La primera es una gráfica de barras de la energía por estación, con el estimador correcto y sin la barra de error que dibuja por omisión. Se guarda como `barras_energia.png`.

La segunda es una caja y bigotes de los diámetros medidos por estación, con las estaciones ordenadas por dispersión de menor a mayor y dos líneas horizontales punteadas en 11.95 y 12.05 que marquen la banda. Se guarda como `caja_estacion.png`.

La tercera es un mapa de calor de la rejilla de estación contra lote, con la energía en miles de kJ, el valor escrito dentro de cada celda y un decimal. Se guarda como `mapa_estacion_lote.png`.

Las tres llevan título con el hallazgo. El programa imprime la tabla de promedio, mediana, desviación y conteo del diámetro por estación ordenada por desviación, y la rejilla en miles.

En esa tabla, EST-01 tiene el promedio más cercano al nominal de las cuatro estaciones y aun así es la segunda que más piezas se sale de banda. Escribe en tres renglones la conclusión que sale de poner las tres gráficas juntas, con al menos tres cifras verificables, y di cuál de las tres mandarías a mantenimiento si solo pudieras mandar una.

---

## Semana 17 · Repaso y examen final

### 17.1 · Reconocer

**Los seis errores caros, todos en el mismo archivo**

Este programa corre de principio a fin y produce seis resultados. Cinco están mal.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

mediciones = pd.read_csv(DATOS / "mediciones.csv")

promedios = mediciones.groupby("estacion")["diametro_mm"].mean()
print(len(promedios))

mediciones[mediciones["estacion"] == "EST-03"]["veredicto"] = "Revisar"
print("veredicto" in mediciones.columns)

diametros = [12.01, 11.98, 12.06]
diametros = diametros.sort()
print(diametros)

for consumo in [86.4, 61.5, 112.8, 48.2]:
    total = 0.0
    total += consumo
print(total)

print(mediciones["energia_kj"][0] + mediciones["energia_kj"][1])

print(mediciones["diametro_mm"][1])
```

Sin ejecutar nada, escribe las seis líneas que imprime y, por cada una, nombra el error de la lista del semestre, di cuál era el resultado correcto y explica en un renglón por qué el programa no se detuvo. La última línea imprime un número que sí existe en el archivo y aun así contesta la pregunta equivocada; di cuál era la pregunta.

### 17.2 · Aplicar

**De archivo a hallazgo, en una sola corrida**

Escribe el programa que va del archivo crudo a una conclusión, en este orden y sin saltarse ningún paso: inspeccionar, limpiar, agrupar y concluir.

La inspección imprime cuatro cifras: renglones, duplicados, formas de escribir la estación y renglones sin tiempo de ciclo. La limpieza quita duplicados, normaliza la estación, convierte la energía y marca el veredicto de cada pieza.

El tablero por estación trae seis columnas: piezas, energía, diámetro promedio, dispersión, piezas fuera de tolerancia y tasa de fuera de tolerancia, ordenado por energía de mayor a menor. La columna de piezas fuera tiene que valer cero en la estación que no aportó ninguna, no quedarse vacía.

La última línea es la conclusión, y se arma dentro del programa a partir del tablero, no se escribe a mano: cuál estación tiene la tasa más alta, qué porcentaje de la energía de la celda consume y qué porcentaje de las piezas fuera de tolerancia concentra. Salen 37.4 % de la energía y 50 % de las piezas fuera.

### 17.3 · Integrar

**El cierre: limpiar cambia la respuesta, y hay que poder decir en cuánto**

Encierra la limpieza en `cargar_limpio()` y la marca del veredicto en su propia función, las dos con docstring.

Primero, reporta la tasa de piezas fuera de tolerancia con el archivo sin limpiar y con el archivo limpio: 8 de 30 contra 8 de 28. Explica en dos renglones por qué el numerador no cambia y el denominador sí, y cuál de las dos cifras reportarías a calidad.

Segundo, imprime el tablero por estación con piezas, energía, diámetro promedio y dispersión, ordenado por dispersión de mayor a menor.

Tercero, audita la unión con el catálogo de cinco estaciones de 15.3 y reporta los tres conteos del indicador.

Cuarto, produce una sola gráfica de caja y bigotes de los diámetros por estación, ordenada por dispersión, con las dos líneas de la banda, título con el hallazgo y fuente al pie, guardada como `dispersion_estacion.png`.

El hallazgo verificable es que EST-03 es la única estación cuyo cuartil superior, 12.065 mm, rebasa el límite de 12.05 mm. Cierra con tres renglones: qué le pedirías a mantenimiento, con qué dos cifras lo sostienes, y qué dato te falta en este archivo para poder afirmar la causa.
