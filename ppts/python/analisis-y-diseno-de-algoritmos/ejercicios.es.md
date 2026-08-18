# Ejercicios · Análisis y Diseño de Algoritmos · COM101

Este juego acompaña las diecisiete sesiones del curso y está pensado para el grupo de primer semestre de Ingeniería. Cada semana trae tres ejercicios: Reconocer se contesta leyendo código y prediciendo lo que imprime, Aplicar pide escribir un programa contra una especificación que ya trae sus datos y su resultado esperado, e Integrar amarra el tema de la semana con lo de las semanas anteriores. La dificultad sube dentro de la semana y también a lo largo del semestre, así que el Reconocer de la semana 12 pide más que el Integrar de la semana 4. Todos los problemas ocurren en el mismo lugar: el área de originación de Financiera Altamar, sus cuatro mesas de crédito MC-01 a MC-04, el crédito de nómina que colocan y el corte donde control interno revisa el precio de cada solicitud autorizada. Se entrega por Blackboard un archivo `.py` por ejercicio, salvo donde el enunciado pida papel, con la salida tal como la produjo tu programa.

La banda de precio del producto es la misma todo el semestre: tasa de política 18.00 % anual, límite inferior 17.50 %, límite superior 18.50 %. Los dos límites se escriben como constantes al principio del programa y no se calculan dentro de una condición.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Las seis semanas de la mesa MC-01**

La mesa MC-01 coloca crédito de nómina. Estas son las solicitudes que aprobó en las seis semanas del bimestre pasado, en dos listas emparejadas. Sin ejecutar nada, escribe las cuatro líneas que imprime este programa.

```python
semanas = ["S01", "S02", "S03", "S04", "S05", "S06"]
aprobadas = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(aprobadas)
promedio = total / len(aprobadas)
mejor = semanas[aprobadas.index(max(aprobadas))]

print(semanas[0], aprobadas[0])
print(total)
print(promedio)
print(mejor)
```

Después contesta dos cosas. A qué semana corresponde `aprobadas[3]` y en qué fila estaría ese dato en la hoja de cálculo de donde salió, si la fila 1 son los encabezados. Y qué ocurre si agregas `print(aprobadas[6])` al final del programa.

### 01.2 · Aplicar

**El resumen del bimestre, formateado**

Escribe el programa que resume esas mismas seis semanas e imprime cuatro renglones alineados: solicitudes aprobadas del bimestre con separador de miles, promedio por semana con un decimal, la mejor semana con su cifra, y cuántas solicitudes quedó esa semana por encima del promedio.

Las cifras que tiene que dar son 7,990 solicitudes en el bimestre, 1,331.7 de promedio y la semana S04 con 1,510, que está 178.3 solicitudes arriba del promedio. Ningún número se escribe a mano dentro del `print`: los cuatro salen de las dos listas.

### 01.3 · Integrar

**El dato que se recapturó**

Control interno avisa que la semana S03 se capturó mal. No fueron 1120 solicitudes sino 1320. Corrige el dato en el programa de 01.2, vuelve a correrlo y reporta las tres cifras nuevas al lado de las anteriores.

El programa imprime también el folio del corte que estaban revisando, `00847`, guardado en una variable de texto.

Contesta después tres cosas, cada una en un renglón. Qué hubiera pasado con ese cambio en una hoja de cálculo y cuál de los cuatro quiebres de la sesión explica la diferencia. Qué se ve en la celda si alguien captura ese folio con formato de número. Y con cuál de los cuatro quiebres tiene que ver eso.

---

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer

**La traza del veredicto de precio**

El crédito de nómina se coloca a una tasa de política de 18.00 % anual, y la banda autorizada va de 17.50 a 18.50 %. Este es el pseudocódigo que sigue control interno con cada solicitud autorizada que le llega.

```text
INICIO
    LEER tasa

    SI tasa > 18.50 ENTONCES
        veredicto = "Sobreprecio fuera de politica"
    SI NO SI tasa < 17.50 ENTONCES
        veredicto = "Descuento fuera de politica"
    SI NO
        veredicto = "Dentro de politica"

    ESCRIBIR veredicto
FIN
```

Escribe la traza completa para tres solicitudes: una de 18.80 %, una de 17.40 % y una de 18.50 % exactos. En cada una anota qué condiciones se evaluaron, cuáles ni se leyeron y con qué veredicto termina.

Después el ejecutivo de la mesa reordena las ramas de esta forma y afirma que el algoritmo hace lo mismo.

```text
SI tasa >= 17.50 ENTONCES
    veredicto = "Dentro de politica"
SI NO SI tasa > 18.50 ENTONCES
    veredicto = "Sobreprecio fuera de politica"
SI NO
    veredicto = "Descuento fuera de politica"
```

Traza la solicitud de 18.80 % contra esta segunda versión y di con qué veredicto sale. Explica en dos renglones por qué esta versión cumple las cinco propiedades de un algoritmo y aun así no se puede usar en el corte.

### 02.2 · Aplicar

**La liberación del desembolso, en papel**

Escribe el algoritmo de la verificación previa al desembolso de un crédito de nómina, en pseudocódigo y en diagrama de flujo. La secuencia revisa tres cosas en este orden: que el expediente esté completo, que el cliente no traiga adeudo vencido y que el score de buró llegue al menos a 620. Si las tres se cumplen, libera el desembolso. Si alguna falla, nombra cuál falló y deja la solicitud en espera.

Entrega el pseudocódigo con las palabras del curso, el diagrama con los cuatro símbolos, y la traza esperada de dos casos: expediente completo, sin adeudo vencido y score de 688; y expediente completo, sin adeudo vencido y score de 601. Sin computadora.

### 02.3 · Integrar

**Una instrucción que no es un algoritmo**

En el correo que circula en la mesa está escrito: «si la solicitud salió muy cara, mándala a comité».

Aplícale la prueba de las dos personas y explica en dos renglones cuál de las cinco propiedades se rompe y por qué. Después reescríbela como algoritmo, con la banda de 17.50 a 18.50 % y tres salidas: comité de precio si la tasa salió arriba, cancelación por margen si salió abajo y desembolso si quedó dentro.

Identifica por escrito cuáles son los datos de entrada y cuál es la salida. Agrega al final un caso límite que tu primera versión no cubría y di qué le tuviste que cambiar para cubrirlo.

---

## Semana 03 · Temas 1 y 2 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**Tres líneas que se pisan y cuatro archivos que no corren**

Primero, la traza. Escribe cuánto vale `solicitudes` después de cada línea y qué imprime el programa.

```python
solicitudes = 1240
solicitudes = solicitudes + 85
solicitudes = solicitudes * 2

print(solicitudes)
```

Después, cuatro fragmentos, cada uno guardado en su propio archivo. Para cada uno di si corre. Cuando no corra, di cuál de las cinco reglas de la sesión se rompió, qué tipo de error se lanza y en qué línea lo va a reclamar Python.

```python
# A
montos = [96500, 148200]
print(Suma(montos))

# B
montos = [96500, 148200]
print("promedio:, montos)

# C
total = 96500 + 148200
print(total

# D
total = 244700
Print(total)
```

### 03.2 · Aplicar

**El primer programa de la mesa**

La mesa MC-01 autorizó cinco créditos el 8 de enero: 96,500, 148,200, 73,400, 151,100 y 118,900 pesos. Escribe un programa con la anatomía completa de la sesión: un comentario arriba que diga de dónde salen los datos, la importación de `mean` desde `statistics`, la lista de montos y tres `print` que muestren cuántos créditos son, el monto promedio y el monto mayor, cada uno con su etiqueta.

El promedio da 117,620 pesos y el monto mayor 151,100 pesos.

Después rompe tu propio programa de tres formas, una a la vez: quita el paréntesis que cierra un `print`, cambia `print` por `Print` y borra una comilla. Entrega una tabla de tres renglones con el mensaje exacto que dio cada uno, incluida la línea que señaló.

### 03.3 · Integrar

**El pseudocódigo de la semana 2, dicho en Python**

Traduce a Python el pseudocódigo del veredicto de 02.1, con la tasa guardada en una variable arriba del programa y el resultado impreso con su etiqueta. La traducción es casi línea por línea: cambian cinco palabras y aparecen los dos puntos.

Córrelo tres veces, con 18.50, con 17.40 y con 18.00, y pega las tres salidas. Contesta además dos cosas: por qué la corrida de 18.00 imprime `18.0` y no `18.00`, y qué veredicto daría una solicitud de 18.80 % si intercambias las dos primeras ramas.

---

## Semana 04 · Tema 3 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Ocho líneas de aritmética de paquetes**

Las solicitudes se reparten en paquetes de 24 para la revisión documental. Sin ejecutar nada, escribe las ocho líneas que imprime este programa.

```python
solicitudes = 1240
por_paquete = 24

print(solicitudes / por_paquete)
print(solicitudes // por_paquete)
print(solicitudes % por_paquete)
print("18" + "50")
print(int("18") + int("50"))
print(18.00 + 0.50 == 18.50)
print(0.05 * 3 == 0.15)
print(0.05 * 3)
```

Después contesta dos cosas. Qué significan, en paquetes y en solicitudes, los resultados de la segunda y la tercera línea. Y por qué la sexta línea da un resultado y la séptima da el contrario, si las dos suman ajustes de tasa que en papel salen exactos.

### 04.2 · Aplicar

**El corte de MC-01, con cada dato en su tipo**

La mesa MC-01 cerró el corte del 8 de enero de 2026 con 1240 solicitudes recibidas, 37 rechazadas y 86.4 horas-analista invertidas. La mesa quedó activa y no registró ninguna incidencia.

Declara ocho variables con el tipo que le corresponde a cada dato, incluidas la bandera de mesa activa y la última incidencia, que no existe. Calcula la tasa de rechazo en por ciento y las horas-analista por solicitud, redondeadas a dos y a cuatro decimales. Imprime las dos métricas con su etiqueta y su unidad, y después el `type` de cinco variables para comprobar qué entendió Python.

La tasa de rechazo da 2.98 % y las horas por solicitud 0.0697. Ningún nombre de variable puede ser de una sola letra.

### 04.3 · Integrar

**Dos paréntesis que cambian la respuesta**

Con los mismos datos de MC-01, alguien quiere saber cuánto tiempo de análisis cuesta cada solicitud aprobada y escribe esto.

```python
por_solicitud = horas_analista / solicitudes - rechazadas
```

Escribe las dos versiones, la de arriba y la que sí contesta la pregunta, imprime las dos redondeadas a cuatro decimales y di en un renglón qué calcula cada una. Una da un número negativo y la otra 0.0718 horas por solicitud aprobada.

En el mismo programa resuelve dos cosas más. Cuántos paquetes llenos de 24 salen de las solicitudes aprobadas y cuántas quedan sueltas, con división entera y residuo. Y qué le pasa al folio del corte, `"00847"`, cuando lo conviertes a entero y lo regresas a texto: imprime los tres valores en una sola línea y explica en un renglón qué se perdió en el camino.

---

## Semana 05 · Tema 4 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Siete líneas de formato**

Sin ejecutar nada, escribe exactamente lo que imprime cada línea, con sus comas, sus decimales y sus espacios.

```python
solicitudes = 1240
horas = 86.4
tasa = 37 / 1240

print(f"Solicitudes: {solicitudes:,}")
print(f"Horas: {horas:,.2f} h")
print(f"Rechazo: {tasa:.1%}")
print(f"Rechazo: {tasa:.2%}")
print(f"{'MC-01':<10}{solicitudes:>8}")
print(f"Tasa cruda: {tasa}")
print("Horas: {horas:.2f} h")
```

Después explica en un renglón por qué las líneas tercera y cuarta muestran el mismo dato con dos cifras distintas, y en otro qué le falta a la última línea para hacer lo que aparenta.

### 05.2 · Aplicar

**La captura del corte**

Escribe el programa que captura un corte desde el teclado y devuelve el reporte de la mesa. Pide cuatro datos, cada uno con su mensaje: la mesa, las solicitudes recibidas, las solicitudes rechazadas y las horas-analista del corte. Convierte lo que haga falta antes de operar con ello.

El reporte son cinco renglones con etiqueta: mesa, solicitudes con separador de miles, rechazadas, tasa de rechazo con dos decimales de por ciento y horas por solicitud con cuatro decimales.

Prueba con MC-01, 1240, 37 y 86.4. Tiene que dar 2.98 % y 0.0697 h. Entrega la sesión completa, con lo que escribiste en la misma línea del mensaje.

### 05.3 · Integrar

**El reporte que se manda a dirección comercial**

Amplía el programa anterior para que además calcule el tiempo por solicitud y los minutos de análisis por solicitud aprobada. La jornada de la mesa dura ocho horas, o sea 28800 segundos, y esa constante va escrita con nombre arriba del programa. El tiempo por solicitud es la jornada entre las solicitudes recibidas. Los minutos por solicitud aprobada son las horas-analista convertidas a minutos, repartidas entre las solicitudes que no se rechazaron.

Las cinco cifras del reporte van alineadas en columna, con el nombre a la izquierda en veintidós espacios y el número a la derecha en diez, cada uno con su formato y su unidad.

Prueba con MC-03, 1512 solicitudes, 68 rechazadas y 112.8 horas-analista. Tiene que dar 1,444 solicitudes aprobadas, 4.50 % de rechazo, 19.05 segundos por solicitud y 4.69 minutos por solicitud aprobada. Entrega la sesión completa.

---

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer

**La solicitud que cae justo en el límite**

Dos programas, cada uno con una solicitud distinta. Sin ejecutar nada, di qué imprime cada uno y por qué.

```python
# Primero
tasa = 18.50

if tasa > 18.50:
    veredicto = "Sobreprecio fuera de politica"
else:
    veredicto = "Dentro de politica"

print(tasa, veredicto)
```

```python
# Segundo
tasa = 18.80

if tasa >= 17.50:
    veredicto = "Dentro de politica"
elif tasa > 18.50:
    veredicto = "Sobreprecio fuera de politica"
else:
    veredicto = "Descuento fuera de politica"

print(tasa, veredicto)
```

El segundo programa aprueba como buena una solicitud colocada a 18.80 %, treinta puntos base arriba del límite superior. Explica en dos renglones por qué la segunda rama nunca se alcanza y escribe el orden correcto de las tres condiciones.

### 06.2 · Aplicar

**El clasificador de precio del corte**

Escribe el programa que pide por teclado el folio de una solicitud y su tasa otorgada, y le da uno de tres veredictos: sobreprecio fuera de política si pasa de 18.50 %, descuento fuera de política si no llega a 17.50 %, y dentro de política en cualquier otro caso. Los dos límites van como constantes con nombre arriba del programa.

La salida es un solo renglón con el folio, la tasa a dos decimales y el veredicto.

Prueba con cinco solicitudes y entrega las cinco corridas: 18.60, 17.40, 18.50, 17.50 y 18.00. Las dos que caen exactamente en el límite tienen que salir dentro de política.

### 06.3 · Integrar

**Cinco destinos y un dato imposible**

Dirección comercial decide que tres categorías no alcanzan. Un sobreprecio se puede autorizar en comité mientras no pase de 19.50 %; arriba de ahí el producto deja de ser vendible y la solicitud se cancela. Un descuento se puede autorizar con el visto bueno de dirección mientras no baje de 16.50 %; abajo de ahí el crédito no cubre su costo de fondeo y se cancela por margen.

Escribe el clasificador de cinco categorías con esos cinco destinos, más una validación que rechace un dato imposible antes de clasificar nada: cualquier tasa menor o igual a cero, o mayor a 60 %, sale como dato inválido y manda a revisar la captura. Las cinco fronteras van como constantes con nombre.

Prueba con estas once tasas y entrega la tabla completa: 20.00, 19.50, 18.60, 18.50, 18.00, 17.50, 17.20, 16.50, 16.20, -3.00 y 75.00. Documenta al final, en una tabla de cinco renglones, qué veredicto le toca al valor exacto de cada frontera y por qué elegiste `>` o `>=` en cada una.

---

## Semana 07 · Tema 4.4 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**Cuatro condiciones que no dicen lo que parecen**

Sin ejecutar nada, escribe las cinco líneas que imprime este programa y explica cada una en un renglón.

```python
mesa = "MC-03"

if mesa == "MC-01" or "MC-03":
    print("Mesa critica")
else:
    print("Mesa normal")

tasas_a = [18.10, 17.80, 18.60]
tasas_b = [18.10, 17.80, 18.60]

print(tasas_a == tasas_b)
print(tasas_a is tasas_b)

solicitudes = 0
rechazadas = 0

if solicitudes > 0 and rechazadas / solicitudes > 0.03:
    print("Bloquear la mesa")
else:
    print("Sin datos suficientes")

ultima_incidencia = None
print(ultima_incidencia is None)
```

Contesta además dos cosas. Qué imprimiría la primera condición si la mesa fuera MC-04, y cómo se escribe correctamente. Y por qué el `and` de la tercera condición evita un `ZeroDivisionError` que con `or` sí habría reventado.

### 07.2 · Aplicar

**La política de liberación del corte**

Un corte se libera cuando se cumplen tres cosas a la vez: la mesa no está en auditoría, el corte trae al menos 500 solicitudes y la tasa de rechazo no pasa de 3 %. Si no se libera, hay dos caminos: si la mesa es de las críticas, que son MC-01 y MC-03, se retiene y se marca como mesa crítica que no cumplió; si no, se retiene para revisión expediente por expediente.

Escribe el programa que pide por teclado la mesa, las solicitudes del corte, las rechazadas y si está en auditoría, y decide. La lista de mesas críticas y los dos umbrales van como constantes arriba. La pertenencia se pregunta con `in`, no con una fila de `or`.

Prueba estos cinco casos y entrega las cinco corridas: MC-01 con 1240 y 37 sin auditoría; MC-03 con 1512 y 68 sin auditoría; MC-04 con 760 y 9 sin auditoría; MC-02 con 420 y 5 sin auditoría; y MC-01 con 1240 y 37 en auditoría.

### 07.3 · Integrar

**El anidado que en realidad era un and**

La regla de bloqueo automático de una mesa llegó del proveedor del sistema de originación escrita así, con cuatro ramas.

```python
if mora > 3.0:
    if sobreprecio > 0.50:
        accion = "Bloquear la mesa"
    else:
        accion = "Seguir colocando"
else:
    if sobreprecio > 0.50:
        accion = "Seguir colocando"
    else:
        accion = "Seguir colocando"
```

Escribe un programa que pida por teclado la mora de la cartera de la mesa en por ciento y su sobreprecio promedio en puntos de tasa, calcule la acción con esa versión anidada y con la versión colapsada en una sola condición, e imprima las dos junto con un `True` o `False` que diga si coinciden.

Corre los cuatro casos de la tabla de verdad y entrega las cuatro salidas: 4.2 con 0.80; 4.2 con 0.30; 2.4 con 0.80; y 2.4 con 0.30.

Cierra con dos renglones. El primero explica por qué este anidado sí se podía colapsar. El segundo describe un caso de la misma área donde el anidado no se puede colapsar, y dice qué tienen que tener sus ramas internas para que eso ocurra.

---

## Semana 08 · Tema 4.5 · Repetición · Primer parcial

### 08.1 · Reconocer

**Un for de seis en seis y un presupuesto que no alcanza**

Sin ejecutar nada, escribe todo lo que imprime este programa y cuántas líneas son.

```python
for plazo in range(12, 48, 6):
    print(plazo)

presupuesto = 50000.0
gasto_semana = 7500.0
semanas = 0

while presupuesto > 0:
    presupuesto -= gasto_semana
    semanas += 1

print(semanas, presupuesto)
```

Después contesta tres cosas. Por qué el `for` no imprime el 48 aunque aparezca en el `range`. Cuántas semanas completas aguanta de verdad el presupuesto de promoción y por qué el número impreso no es ese. Y qué pasaría si borras la línea que resta el gasto.

### 08.2 · Aplicar

**Las cuatro mesas, en un solo recorrido**

Estos son los datos del corte del 8 de enero, en cuatro listas emparejadas.

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes = [1240, 984, 1512, 760]
rechazadas = [37, 12, 68, 9]
horas = [86.4, 61.5, 112.8, 48.2]
```

Escribe el programa que las recorre una sola vez y produce la tabla del corte: un encabezado y un renglón por mesa con la mesa, las solicitudes con separador de miles, la tasa de rechazo con dos decimales de por ciento y las horas-analista por solicitud con cuatro decimales, todo alineado en columnas.

El último renglón es el del área completa, con 4,496 solicitudes, 2.80 % de rechazo y 0.0687 horas por solicitud. Ese renglón se calcula sumando y dividiendo los totales, no promediando las cuatro tasas.

El ciclo tiene que seguir funcionando si mañana se agrega una quinta mesa a las cuatro listas, sin tocar una sola línea de adentro.

### 08.3 · Integrar

**Repaso del primer parcial: el corte C-2601 completo**

Este ejercicio cruza lo que entra al parcial: tipos, formato, selección y repetición. Estas son las doce solicitudes del corte C-2601 con su tasa otorgada.

```python
solicitudes = ["SOL-1001", "SOL-1002", "SOL-1003", "SOL-1004",
               "SOL-1005", "SOL-1006", "SOL-1007", "SOL-1008",
               "SOL-1009", "SOL-1010", "SOL-1011", "SOL-1012"]
tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]
```

Escribe el programa que recorre las dos listas emparejadas e imprime un renglón por solicitud con su folio, su tasa a dos decimales y su veredicto, usando las tres categorías de la semana 6 y las constantes de la banda.

Al terminar el recorrido imprime dos renglones más: la tasa promedio del corte a cuatro decimales, y cuántas solicitudes quedaron fuera de política de las doce, con el porcentaje a un decimal. El promedio da 18.0750 % y salen 3 de 12.

Cierra contestando en dos renglones por qué la solicitud SOL-1008, colocada a 18.50 %, no cuenta como fuera de política, y qué habría pasado con ese conteo si el programa usara `>=` en lugar de `>` en la primera condición.

---

## Semana 09 · Tema 4.5 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Un acumulador que se borra y una búsqueda que sale antes**

Dos programas. Sin ejecutar nada, di qué imprime cada uno.

```python
# Primero
horas = [86.4, 61.5, 112.8, 48.2]

for hora in horas:
    total = 0.0
    total += hora

print(total)
```

```python
# Segundo
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes = [1240, 984, 1512, 760]
rechazadas = [37, 12, 68, 9]

for i in range(len(mesas)):
    if solicitudes[i] < 1000:
        continue

    if rechazadas[i] / solicitudes[i] > 0.03:
        print("Primera fuera de control:", mesas[i])
        break
else:
    print("Ninguna mesa rebasa el limite")
```

Del primero, di cuál era el resultado esperado, cuál sale y qué única línea hay que mover. Del segundo, escribe la traza de las cuatro vueltas diciendo qué pasa en cada una, y explica por qué el `else` del `for` no se ejecuta y en qué caso sí lo haría.

### 09.2 · Aplicar

**Tres preguntas, un solo recorrido**

Con las cuatro listas del corte de 08.2, escribe el programa que contesta tres preguntas distintas en un mismo `for`, con las tres variables declaradas antes del ciclo.

Cuántas horas-analista consumió el área completa, que es un acumulador. Cuántas mesas rebasaron la meta de 3 % de rechazo, que es un contador. Y si existe al menos una mesa que gaste más de 0.070 horas por solicitud, que es una bandera.

Las tres respuestas se imprimen con etiqueta: 308.9 horas, 1 mesa fuera de meta y la bandera en `True`. Las dos metas van como constantes con nombre.

Cierra explicando en un renglón por qué la segunda pregunta no se puede contestar con un acumulador y la primera no se puede contestar con un contador.

### 09.3 · Integrar

**La proyección de capacidad, mesa por turno**

Planeación quiere la capacidad de dictamen de cada mesa en cada uno de los tres turnos de atención del día. Estas son las velocidades del motor de decisión y las duraciones.

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes_por_hora = [155, 123, 189, 95]
turnos = ["T1", "T2", "T3"]
horas = [8, 8, 6]
```

Escribe el programa con dos ciclos anidados que imprima un renglón por combinación, con la mesa, el turno y la proyección con separador de miles, alineados. Antes de correrlo, escribe en tu cuaderno cuántos renglones deberían salir; si no coincide con lo que imprime, el anidado está mal.

Al terminar imprime dos renglones de resumen: la capacidad proyectada del área, que da 12,364 solicitudes, y cuántas combinaciones pasan de 1000 solicitudes, que son 5.

Las variables de los dos ciclos tienen que llamarse distinto y decir qué recorren. Cierra explicando en dos renglones cuántas vueltas daría este programa si la financiera tuviera 40 mesas y 3 turnos, y a partir de qué tamaño empezarías a preocuparte.

---

## Semana 10 · Tema 5 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Una función que calcula bien y no entrega nada**

Sin ejecutar nada, di qué imprime cada una de las tres líneas finales de este programa.

```python
def tasa_rechazo(solicitudes, rechazadas):
    rechazadas / solicitudes


def minutos_por_solicitud(horas, solicitudes):
    unitario = horas * 60 / solicitudes
    return unitario


print(tasa_rechazo(1240, 37))
print(minutos_por_solicitud(86.4, 1240))
print(unitario)
```

Contesta después tres cosas, cada una en un renglón. Qué le falta a la primera función, y por qué el error no aparece dentro de ella sino donde alguien use su resultado. Por qué la tercera línea falla aunque `unitario` sí se calculó. Y qué pasaría si en lugar de `return unitario` la segunda función tuviera `print(unitario)`.

### 10.2 · Aplicar

**Dos cálculos del corte, empaquetados**

Escribe dos funciones con su docstring de un renglón. La primera, `tasa_rechazo(solicitudes, rechazadas)`, devuelve la fracción de solicitudes rechazadas. La segunda, `dentro_de_politica(tasa)`, devuelve verdadero o falso según la banda de 17.50 a 18.50 %, que vive en dos constantes fuera de la función.

Ninguna de las dos puede imprimir nada. Solo reciben y devuelven.

Pruébalas con seis llamadas y pega la salida: la tasa de MC-01 con 1240 y 37, la de MC-03 con 1512 y 68, la de un corte de 760 solicitudes sin ningún rechazo, y la política de 18.00, de 18.50 y de 18.60. Las tres tasas redondeadas a cuatro decimales dan 0.0298, 0.045 y 0.0.

Cierra explicando en un renglón por qué el caso de 18.50 es el que hay que probar siempre y qué habría pasado si la función usara `<` en lugar de `<=`.

### 10.3 · Integrar

**El corte C-2601, resuelto con funciones**

Vuelve a resolver el ejercicio 08.3, ahora con cuatro funciones y sin repetir una sola condición.

`dentro_de_politica(tasa)` contesta si la solicitud está en banda. `veredicto(tasa)` devuelve dentro de política, sobreprecio o descuento, y por dentro llama a la primera en lugar de volver a comparar. `solicitudes_en_politica(tasas)` cuenta cuántas tasas de una lista caen dentro. `tasa_promedio(tasas)` devuelve el promedio.

Ninguna función imprime. El programa principal recorre las doce solicitudes del corte, imprime el renglón de cada una y cierra con tres líneas: revisadas, dentro de política y tasa promedio. Salen 12 revisadas, 9 dentro de política y 18.0750 %.

Cierra con dos renglones. Bórrale al cuerpo de `dentro_de_politica` la comparación con el límite inferior y di cuál de tus cuatro pruebas lo detecta; si ninguna lo detecta, agrega la que falta y dilo.

---

## Semana 11 · Tema 5 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**El argumento que cayó en el lugar equivocado**

Sin ejecutar nada, escribe los tres números que imprime este programa, redondeados a dos decimales, y di a qué parámetro llegó el 5.0 en cada llamada.

```python
def minutos_por_solicitud(horas, solicitudes, factor=60, extras=0.0):
    return horas * factor / solicitudes + extras


print(minutos_por_solicitud(86.4, 1240))
print(minutos_por_solicitud(86.4, 1240, 5.0))
print(minutos_por_solicitud(86.4, 1240, extras=5.0))
```

La segunda llamada devuelve un número que no se parece en nada a los otros dos. Explica en dos renglones qué pasó, por qué Python no marcó ningún error, y qué le pasaría a la definición si movieras `factor=60` antes de `solicitudes`.

### 11.2 · Aplicar

**Una función que sirve para más de un producto**

El área también coloca crédito automotriz a una tasa de política de 14.00 % con la misma banda, y a veces corre una campaña con banda abierta de 1.00 punto. Escribe `fuera_de_politica(tasa, nominal=18.00, banda=0.50)`, con su docstring, que calcule los dos límites por dentro y devuelva verdadero cuando la solicitud se sale.

Pruébala con cinco llamadas: 18.60 con los valores por omisión; 18.50 con los valores por omisión; 18.60 con nominal y banda dados por posición; 18.60 pasando solo la banda por nombre; y 14.20 pasando solo el nominal por nombre.

Agrega al final dos líneas que comprueben, antes de confiar en la función, que `18.00 - 0.50` da exactamente 17.50 y que `18.00 + 0.50` da exactamente 18.50. Explica en un renglón por qué esa comprobación no sobra, aunque en este caso las dos salgan verdaderas.

### 11.3 · Integrar

**Lo que el promedio del corte no dice**

Con las doce tasas del corte C-2601, escribe el programa que importa `mean`, `median` y una tercera función del módulo `statistics` que no vimos en clase, y que sirva para medir qué tan dispersas están las tasas otorgadas. Busca esa tercera función en docs.python.org y cita la página.

El programa imprime siete renglones: número de solicitudes, promedio, mediana y dispersión a cuatro decimales, la tasa menor y la mayor a dos, y el índice de capacidad, que es el ancho de la banda de política entre seis veces la dispersión. Da 18.0750 de promedio, 18.0500 de mediana, 0.4065 de dispersión y un índice de 0.41.

Al final, repite el promedio y la mediana sobre una lista de trece valores, la misma más una tasa de 27.00 % que alguien capturó tecleando el plazo en el campo de la tasa. Uno de los dos números se mueve mucho más que el otro.

Cierra con tres renglones: qué significa un índice de capacidad de 0.41 para la política de precio, qué le dirías al director comercial con esa cifra, y cuál de las dos medidas de centro reportarías cuando sospechas de una captura mal hecha.

---

## Semana 12 · Tema 6 · Listas y tuplas

### 12.1 · Reconocer

**Un método que ordena y borra el respaldo**

Sin ejecutar nada, escribe las siete líneas que imprime este programa y qué pasa en la última.

```python
tasas = [18.10, 17.80, 18.60, 18.00, 17.40]

print(tasas[0], tasas[-1])
print(tasas[1:3])
print(sorted(tasas))
print(tasas)

ordenadas = tasas.sort()
print(ordenadas)
print(tasas)

respaldo = tasas
copia = tasas.copy()
tasas.append(19.00)

print(len(respaldo), len(copia))
print(tasas[6])
```

Contesta además tres cosas. Por qué `tasas[1:3]` devuelve dos valores y no tres. Por qué `respaldo` y `copia` terminan con distinto número de elementos, si las dos se crearon en el mismo momento. Y qué habría pasado con los datos si en lugar de `ordenadas = tasas.sort()` alguien escribe `tasas = tasas.sort()`.

### 12.2 · Aplicar

**Cuatro preguntas sobre la columna de tasas**

Con las doce tasas del corte C-2601, escribe el programa que imprime la lista al principio, contesta cuatro preguntas y vuelve a imprimir la lista al final, que tiene que salir idéntica.

La tasa mayor y la menor. Las tres tasas más altas, ordenadas de mayor a menor. En qué posición está la tasa de 17.40 y a qué folio corresponde, sabiendo que la primera solicitud es la SOL-1001. Y las últimas tres tasas del corte, con una rebanada.

Las tres más altas son 18.80, 18.60 y 18.50. La tasa de 17.40 está en la posición 4 y le toca la solicitud SOL-1005.

### 12.3 · Integrar

**Las solicitudes fuera de banda, sin tocar el original**

Escribe el programa que recorre las doce tasas y arma una lista nueva con las que se salen de la banda, sin modificar la lista original. Después la ordena de mayor a menor y la imprime.

La banda va en una tupla de tres valores, `(18.00, 17.50, 18.50)`, que es tasa de política, límite inferior y límite superior. Todas las comparaciones leen esa tupla por posición.

El reporte son cinco renglones: la banda con sus tres cifras, cuántas solicitudes se revisaron, cuántas se salieron, la lista de las que se salieron ordenada de mayor a menor, y la lista original completa para comprobar que quedó intacta. Salen 3 de 12, y la lista de fuera de banda es 18.80, 18.60 y 17.40.

Cierra con una línea que intente cambiar el límite superior de la tupla a 19.00 y pega el error completo que lanza. Explica en un renglón por qué conviene que la banda esté en una tupla y no en una lista.

---

## Semana 13 · Tema 6 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Un catálogo que crece y un motivo que no existe**

Sin ejecutar nada, escribe las ocho líneas que imprime este programa y qué pasa en la última.

```python
motivos = {"M01": "Score de buro insuficiente",
           "M02": "Capacidad de pago rebasada",
           "M03": "Documentacion incompleta"}

motivos["M02"] = "Capacidad de pago arriba del 35 %"
motivos["M04"] = "Antiguedad laboral insuficiente"

print(len(motivos))
print(motivos["M02"])
print(motivos.get("M09"))
print(motivos.get("M09", "Motivo no catalogado"))

corte_a = {"M01", "M02", "M01", "M03"}
corte_b = {"M02", "M03", "M05"}

print(len(corte_a))
print(sorted(corte_a & corte_b))
print(sorted(corte_a - corte_b))
print(sorted(corte_a ^ corte_b))
print(motivos["M09"])
```

Contesta además dos cosas. Por qué el diccionario termina con cuatro entradas si se le asignaron dos códigos después de crearlo. Y por qué `corte_a` tiene tres elementos si la lista de la que salió trae cuatro.

### 13.2 · Aplicar

**El catálogo de motivos de rechazo**

Arma el diccionario de los seis códigos de motivo que maneja el área: M01 score de buró insuficiente, M02 capacidad de pago arriba del 35 %, M03 documentación incompleta, M04 antigüedad laboral insuficiente, M05 ingreso no comprobable y M06 cliente ya tiene crédito vigente.

El corte reportó estos ocho códigos, en este orden: M01, M03, M01, M05, M01, M02, M03 y M09.

Escribe el programa que imprime el catálogo completo recorriéndolo con `items`, después tres cifras con etiqueta (motivos catalogados, rechazos reportados y motivos distintos reportados), y al final la lista de los motivos distintos ordenada, cada uno con su descripción.

La consulta de la descripción tiene que usar `get` con un valor por omisión, porque M09 no está en el catálogo y el programa no se puede detener ahí. Salen 6 motivos catalogados, 8 rechazos reportados y 5 motivos distintos.

### 13.3 · Integrar

**Repaso del segundo parcial: el tablero del corte**

Este ejercicio cruza lo que entra al parcial: repetición, funciones y colecciones. Los datos son estos.

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
horas = [86.4, 61.5, 112.8, 48.2]
solicitudes = [1240, 984, 1512, 760]

reportados_a = ["M01", "M03", "M01", "M05", "M01", "M02", "M03"]
reportados_b = ["M02", "M02", "M06", "M03", "M01"]
```

Primero, arma con un ciclo el diccionario que va de mesa a horas-analista. No se escribe a mano. Imprímelo con `items`, saca el total con `values` y encuentra la mesa más cara recorriendo el diccionario, no a ojo. El total da 308.9 horas y la mesa más cara es MC-03 con 112.8.

Segundo, cuenta cuántas veces aparece cada motivo del corte A usando un diccionario como contador, con `get` y un valor por omisión de cero. Imprímelo ordenado por código.

Tercero, compara los motivos de los dos cortes con operaciones de conjuntos, nunca con un ciclo y un `if`: los que aparecieron en los dos, los que solo están en el corte A, los que aparecieron nuevos en el corte B y los que están en uno pero no en ambos.

Cierra con dos renglones: qué decisión de originación tomarías con el motivo que apareció nuevo en el corte B, y por qué el conteo del corte A no se podía hacer con un conjunto.

---

## Semana 14 · Tema 7 · Archivos de texto y CSV

### 14.1 · Reconocer

**Lo que devuelve un CSV, y de qué tipo**

Las cuatro semanas que quedan trabajan sobre el mismo archivo. Créalo con el nombre `solicitudes.csv`, guardado en la misma carpeta que tus programas y codificado en UTF-8. Son 30 renglones de solicitudes autorizadas de Financiera Altamar, exportados tal como salieron del sistema de originación, con tres días de operación y tres cortes.

```text
fecha,mesa,corte,tasa_pct,horas_resp,comision_mxn
2026-01-08,MC-01,C-2601,18.10,44,"$1,240"
2026-01-08,MC-02,C-2601,17.80,39,$980
2026-01-08, MC-01,C-2601,18.60,46,"$1,310"
2026-01-08,MC-03,C-2601,18.00,51,"$1,505"
2026-01-08,mc-01,C-2601,17.40,,"$1,190"
2026-01-08,MC-04,C-2601,18.30,38,$760
2026-01-09,MC-01,C-2602,17.90,45,"$1,260"
2026-01-09,MC-02,C-2602,18.50,41,"$1,020"
2026-01-09,MC-03,C-2602,18.80,52,"$1,540"
2026-01-09,MC-01 ,C-2602,18.20,43,"$1,225"
2026-01-09,MC-04,C-2602,17.60,,$745
2026-01-09,MC-03,C-2602,17.70,50,"$1,480"
2026-01-12,MC-01,C-2603,18.40,44,"$1,255"
2026-01-12,mc-02,C-2603,18.70,40,"$1,005"
2026-01-12,MC-03,C-2603,17.50,49,"$1,460"
2026-01-12,MC-04,C-2603,18.00,37,$735
2026-01-12,MC-01,C-2603,17.30,47,"$1,330"
2026-01-12,MC-02,C-2603,18.10,,$995
2026-01-08,MC-02,C-2601,18.20,40,"$1,010"
2026-01-08,MC-03,C-2601,18.90,53,"$1,575"
2026-01-09,MC-01,C-2602,17.90,45,"$1,260"
2026-01-09,MC-04,C-2602,18.30,39,$755
2026-01-12,MC-03,C-2603,18.20,48,"$1,435"
2026-01-12,MC-04,C-2603,17.80,38,$742
2026-01-08,MC-04,C-2601,18.50,37,$730
2026-01-09,MC-02,C-2602,17.50,42,"$1,035"
2026-01-12,MC-01,C-2603,18.40,44,"$1,255"
2026-01-08,MC-03 ,C-2601,17.10,54,"$1,610"
2026-01-09,MC-03,C-2602,18.60,51,"$1,520"
2026-01-12,MC-02,C-2603,17.70,41,"$1,015"
```

Sin ejecutar nada, escribe las seis líneas que imprime este programa.

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent

with (DATOS / "solicitudes.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

print(len(filas))
print(filas[0]["mesa"], filas[0]["tasa_pct"])
print(type(filas[0]["tasa_pct"]))
print(filas[0]["tasa_pct"] + filas[1]["tasa_pct"])
print(filas[4]["horas_resp"] == "")
print(filas[2]["mesa"] == "MC-01")
```

Contesta después tres cosas, cada una en un renglón. Por qué la cuarta línea no lanza ningún error a pesar de estar sumando mal. Por qué la sexta línea da falso si en el archivo ese renglón dice MC-01. Y qué le pasaría al archivo si esa misma apertura llevara `"w"` en lugar del modo por omisión.

### 14.2 · Aplicar

**El resumen por mesa, leyendo por nombre de columna**

Escribe el programa que lee `solicitudes.csv` con `DictReader` y produce el resumen del corte. Necesitas tres funciones cortas, cada una con su docstring: una que convierta la comisión a decimal quitándole el signo de pesos y la coma de miles, una que convierta las horas de respuesta a entero y devuelva la ausencia de dato como `None` cuando la celda viene vacía, y una que normalice el nombre de la mesa quitándole los espacios de los extremos y dejando una sola forma de escribirlo.

El programa imprime primero cuatro renglones de diagnóstico: renglones leídos, renglones sin horas de respuesta, formas distintas de escribir la mesa y mesas que quedan después de normalizar. Son 30 renglones, 3 sin horas de respuesta, y las 9 formas se reducen a 4 mesas.

Después imprime la tabla por mesa, ordenada por nombre, con solicitudes autorizadas, comisión total en pesos y tasa promedio a cuatro decimales, más el renglón del área completa. Con el archivo tal como viene, el área suma 34,977 pesos de comisión en 30 solicitudes.

Las rutas se arman desde la ubicación del archivo, nunca escritas a mano.

### 14.3 · Integrar

**Limpiar, decidir y escribir el archivo de salida**

Ahora el mismo archivo se procesa con criterio de control interno y el resultado se guarda.

El programa quita los renglones exactamente duplicados comparando el renglón completo y no una sola columna, normaliza la mesa, convierte la comisión, y marca cada solicitud como fuera de política cuando su tasa se sale de la banda. Los renglones que no traen horas de respuesta se conservan, porque su tasa sí quedó capturada y esa es la variable que decide si el precio cumple; el programa reporta cuántos son y deja escrita la decisión.

Imprime seis cifras de bitácora: 30 renglones en el archivo, 2 duplicados exactos quitados, 28 renglones que quedaron, 3 renglones sin horas de respuesta conservados, 8 solicitudes fuera de política y 32,462 pesos de comisión del área.

Después escribe un archivo nuevo llamado `resumen_mesa.csv`, con encabezado `mesa,solicitudes,fuera_politica,comision_mxn` y un renglón por mesa ordenada por nombre. Al escribir un CSV en Windows hay que pasar el parámetro que evita el renglón en blanco entre cada dato. Al final el programa imprime el contenido del archivo que acaba de escribir.

Esa comisión es 2,515 pesos menor que la del ejercicio anterior. Explica en dos renglones de dónde sale la diferencia exacta y por qué un duplicado infla la comisión pero casi no mueve la tasa promedio.

---

## Semana 15 · Tema 8.1 · Series, DataFrame, limpieza y agrupación

### 15.1 · Reconocer

**Lo que pandas infirió del archivo, y por qué**

Sin ejecutar nada, di qué imprime cada una de las siete instrucciones de este programa, que corre sobre el mismo `solicitudes.csv`.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

solicitudes = pd.read_csv(DATOS / "solicitudes.csv")

print(solicitudes.shape)
print(solicitudes.dtypes)
print(solicitudes["horas_resp"].isna().sum())
print(solicitudes.duplicated().sum())
print(solicitudes["mesa"].nunique())
print(solicitudes["mesa"].value_counts())
print(solicitudes["tasa_pct"].describe().round(3))
```

Contesta después cuatro cosas, cada una en un renglón. Por qué `horas_resp` salió decimal y no entero, si en el archivo todas las horas son números redondos. Por qué `comision_mxn` salió texto. Por qué en la salida de `value_counts` hay dos renglones que se ven idénticos y aun así son entradas distintas. Y qué columnas resume `describe` y cuáles no.

### 15.2 · Aplicar

**Las cuatro reparaciones, con su bitácora**

Escribe el programa que carga `solicitudes.csv` con pandas y lo deja listo para analizar, imprimiendo el conteo antes y después de cada reparación.

El orden es este: reportar el estado inicial, quitar duplicados, normalizar la mesa con métodos de texto, quitarle el signo de pesos y la coma de miles a la comisión y convertirla a decimal, y convertir la fecha a tipo fecha. Imprime los tipos de las seis columnas cuando termines.

Los números que tiene que reportar son 30 renglones al cargar, 2 duplicados, 9 formas de escribir la mesa, 3 renglones sin horas de respuesta, 28 renglones sin duplicados y 4 mesas reales.

Después agrega la columna `veredicto`, que vale «Dentro de política» en todos lados y «Fuera de política» donde la tasa se sale de la banda, escrita en un solo paso con `loc`. Salen 20 dentro y 8 fuera.

Cierra con cuatro cifras más: cuántas solicitudes de MC-03 quedaron fuera de política, que son 4; cuántas solicitudes son de MC-01 o MC-02, que son 14 y se piden con `isin`; la comisión total, que da 32,462 pesos; y las horas de respuesta promedio, que dan 44.36. Reporta también con cuántos renglones te quedarías si descartaras los tres sin horas de respuesta, y explica en dos renglones por qué en este archivo conviene conservarlos.

Las condiciones combinadas usan los símbolos y sus paréntesis, nunca las palabras.

### 15.3 · Integrar

**El tablero del área, la rejilla por corte y la unión auditada**

Encierra toda la limpieza de 15.2 en una función `cargar_limpio()` con su docstring, para no volver a escribirla en lo que queda del semestre.

Primero, agrupa por mesa y pide cuatro resúmenes en una sola instrucción: solicitudes autorizadas, comisión, horas de respuesta promedio y tasa promedio, redondeados a tres decimales y ordenados por comisión de mayor a menor. MC-03 encabeza con 12,125 pesos en 8 solicitudes.

Segundo, imprime cuántas solicitudes fuera de política aportó cada mesa. Fíjate en cuántos renglones trae esa tabla y explica en un renglón por qué no son cuatro.

Tercero, arma la rejilla de mesa contra corte con la comisión sumada, rellenando con cero lo que no tenga registro y agregando los totales de fila y de columna. La celda más rentable es el corte C-2601 en MC-03 con 4,690 pesos y el total general da 32,462.

Cuarto, construye este catálogo como DataFrame desde un diccionario de columnas y únelo con el tablero.

```python
catalogo = pd.DataFrame({
    "mesa": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "plaza": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "horas_meta": [42, 40, 48, 36, 30],
})
```

Audita la unión en las dos direcciones antes de confiar en ella. Tienen que salir 28 renglones en ambos lados, 1 solo del catálogo y 0 solo de las solicitudes. Explica en dos renglones qué significa cada uno de esos tres números para la financiera.

Cierra con el tablero de desvío de tiempo de respuesta: mesa, plaza, solicitudes, horas reales, horas meta y desvío como fracción, redondeado a tres decimales. MC-01 corre 6.7 % arriba de su meta y MC-02 apenas 1.2 %. Escribe en dos renglones qué le reportarías a la dirección de operaciones con esas cifras.

---

## Semana 16 · Tema 8.2 · Visualización con matplotlib y seaborn

### 16.1 · Reconocer

**La barra que dice promedio cuando el asunto dice total**

Alguien de la mesa armó esta gráfica con el archivo ya limpio y la mandó por correo con el asunto «comisión del corte por mesa».

```python
sns.barplot(data=solicitudes, x="mesa", y="comision_mxn", ax=ax)
```

Sin ejecutar nada, contesta qué número está mostrando cada barra, cuánto vale esa barra para MC-01 y cuánto valdría si mostrara lo que dice el asunto, y qué habría que agregarle a la llamada para que muestre el total.

Después escribe el programa corto que imprime las tres tablas que sostienen tu respuesta: la suma, el promedio y el conteo de comisión por mesa; el promedio, la dispersión, el mínimo y el máximo de la tasa por mesa, ordenado por dispersión; y cuántas solicitudes fuera de política aportó cada una.

Cierra eligiendo la gráfica correcta para cada una de estas cuatro preguntas, con un renglón de justificación cada una.

- Cómo se compara la comisión de las cuatro mesas.
- Cómo se repartieron las tasas otorgadas dentro de cada mesa.
- Cómo se movió la tasa promedio del área a lo largo de los tres días.
- Si las solicitudes que más tardan en dictaminarse son también las que más se salen de la banda de precio.

### 16.2 · Aplicar

**La comisión del área, en una gráfica que viaja sola**

Con el archivo limpio, agrupa la comisión por mesa y produce una gráfica de barras guardada como `comision_mesa.png` a 150 puntos por pulgada.

La gráfica lleva cinco cosas: el título con el hallazgo y no con el nombre de los ejes, la etiqueta del eje vertical con su unidad, el eje vertical empezando en cero, el eje vertical formateado en miles para que nadie cuente dígitos, y la fuente al pie. La barra de la mesa pico va en azul fuerte y las otras tres en azul claro.

MC-03 concentra el 37.4 % de la comisión del área con 12,125 pesos, y ese porcentaje se calcula dentro del programa, no se escribe a mano en el título.

El programa imprime la serie por mesa y una línea que compruebe que el archivo se generó. Cierra la figura al terminar.

Escribe además el texto alternativo de la gráfica, de dos o tres renglones, donde cada cifra que menciones se pueda verificar contra la serie impresa.

### 16.3 · Integrar

**Tres gráficas de seaborn y la historia que cuentan juntas**

Configura el tema de seaborn una sola vez al principio y produce tres imágenes con el archivo limpio.

La primera es una gráfica de barras de la comisión por mesa, con el estimador correcto y sin la barra de error que dibuja por omisión. Se guarda como `barras_comision.png`.

La segunda es una caja y bigotes de las tasas otorgadas por mesa, con las mesas ordenadas por dispersión de menor a mayor y dos líneas horizontales punteadas en 17.50 y 18.50 que marquen la banda. Se guarda como `caja_mesa.png`.

La tercera es un mapa de calor de la rejilla de mesa contra corte, con la comisión en miles de pesos, el valor escrito dentro de cada celda y un decimal. Se guarda como `mapa_mesa_corte.png`.

Las tres llevan título con el hallazgo. El programa imprime la tabla de promedio, mediana, dispersión y conteo de la tasa por mesa ordenada por dispersión, y la rejilla en miles.

En esa tabla, MC-01 tiene el promedio más cercano a la tasa de política de las cuatro mesas y aun así es la segunda que más solicitudes se sale de banda. Escribe en tres renglones la conclusión que sale de poner las tres gráficas juntas, con al menos tres cifras verificables, y di cuál de las tres mandarías a la dirección de operaciones si solo pudieras mandar una.

---

## Semana 17 · Repaso y examen final

### 17.1 · Reconocer

**Los seis errores caros, todos en el mismo archivo**

Este programa corre de principio a fin y produce seis resultados. Cinco están mal.

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent

solicitudes = pd.read_csv(DATOS / "solicitudes.csv")

promedios = solicitudes.groupby("mesa")["tasa_pct"].mean()
print(len(promedios))

solicitudes[solicitudes["mesa"] == "MC-03"]["veredicto"] = "Revisar"
print("veredicto" in solicitudes.columns)

tasas = [18.10, 17.80, 18.60]
tasas = tasas.sort()
print(tasas)

for hora in [86.4, 61.5, 112.8, 48.2]:
    total = 0.0
    total += hora
print(total)

print(solicitudes["comision_mxn"][0] + solicitudes["comision_mxn"][1])

print(solicitudes["tasa_pct"][1])
```

Sin ejecutar nada, escribe las seis líneas que imprime y, por cada una, nombra el error de la lista del semestre, di cuál era el resultado correcto y explica en un renglón por qué el programa no se detuvo. La última línea imprime un número que sí existe en el archivo y aun así contesta la pregunta equivocada; di cuál era la pregunta.

### 17.2 · Aplicar

**De archivo a hallazgo, en una sola corrida**

Escribe el programa que va del archivo crudo a una conclusión, en este orden y sin saltarse ningún paso: inspeccionar, limpiar, agrupar y concluir.

La inspección imprime cuatro cifras: renglones, duplicados, formas de escribir la mesa y renglones sin horas de respuesta. La limpieza quita duplicados, normaliza la mesa, convierte la comisión y marca el veredicto de cada solicitud.

El tablero por mesa trae seis columnas: solicitudes, comisión, tasa promedio, dispersión, solicitudes fuera de política y proporción de fuera de política, ordenado por comisión de mayor a menor. La columna de solicitudes fuera tiene que valer cero en la mesa que no aportó ninguna, no quedarse vacía.

La última línea es la conclusión, y se arma dentro del programa a partir del tablero, no se escribe a mano: cuál mesa tiene la proporción más alta, qué porcentaje de la comisión del área deja y qué porcentaje de las solicitudes fuera de política concentra. Salen 37.4 % de la comisión y 50 % de las solicitudes fuera.

### 17.3 · Integrar

**El cierre: limpiar cambia la respuesta, y hay que poder decir en cuánto**

Encierra la limpieza en `cargar_limpio()` y la marca del veredicto en su propia función, las dos con docstring.

Primero, reporta la proporción de solicitudes fuera de política con el archivo sin limpiar y con el archivo limpio: 8 de 30 contra 8 de 28. Explica en dos renglones por qué el numerador no cambia y el denominador sí, y cuál de las dos cifras reportarías a control interno.

Segundo, imprime el tablero por mesa con solicitudes, comisión, tasa promedio y dispersión, ordenado por dispersión de mayor a menor.

Tercero, audita la unión con el catálogo de cinco mesas de 15.3 y reporta los tres conteos del indicador.

Cuarto, produce una sola gráfica de caja y bigotes de las tasas por mesa, ordenada por dispersión, con las dos líneas de la banda, título con el hallazgo y fuente al pie, guardada como `dispersion_mesa.png`.

El hallazgo verificable es que MC-03 es la única mesa cuyo cuartil superior, 18.65 %, rebasa el límite de 18.50 %. Cierra con tres renglones: qué le pedirías a la dirección de operaciones, con qué dos cifras lo sostienes, y qué dato te falta en este archivo para poder afirmar la causa.
