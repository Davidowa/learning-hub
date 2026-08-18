# Soluciones · Análisis y Diseño de Algoritmos · COM101

Documento del profesor. Cada ejercicio trae la solución tal como se corrió, la salida exacta que produjo, la rúbrica de diez puntos y el error que más aparece al calificarlo. Todo el código de Python se ejecutó con el intérprete del curso; las soluciones de la semana 2 son de papel y se revisan contra la traza. Los ejercicios que leen por teclado se muestran con la sesión completa, con lo que el alumno escribe en la misma línea del mensaje.

Los datos son los mismos todo el semestre: la celda de maquinado C-3, sus estaciones EST-01 a EST-04, el buje de bronce de 12.00 mm con banda de 11.95 a 12.05 mm, y el archivo `mediciones.csv` de las semanas 14 a 17.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Solución**

```text
T1 1240
7990
1331.6666666666667
T4
```

`piezas[3]` es el turno T4, con 1510 piezas. En la hoja de cálculo de donde salió el dato está en la fila 5: la fila 1 son los encabezados, la fila 2 es T1, y de ahí el índice 3 de Python cae dos renglones abajo de lo que la intuición dice.

`print(piezas[6])` lanza `IndexError`. La lista tiene seis elementos y el último índice válido es el 5.

**Salida**

```text
T1 1240
7990
1331.6666666666667
T4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas correctas, incluido el promedio sin redondear | 4 |
| Identifica que `piezas[3]` es T4 | 2 |
| Ubica la fila de la hoja contando el encabezado | 2 |
| Explica el `IndexError` nombrando el último índice válido | 2 |

**Error que más se ve**

Contestar `T3 1120` en la primera línea y decir que `piezas[3]` es T3: es contar desde uno, y lo delata que todas las respuestas queden corridas exactamente una posición.

### 01.2 · Aplicar

**Solución**

```python
turnos = ["T1", "T2", "T3", "T4", "T5", "T6"]
piezas = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(piezas)
promedio = total / len(piezas)
mejor_turno = turnos[piezas.index(max(piezas))]
mejor_valor = max(piezas)
sobre_promedio = mejor_valor - promedio

print(f"Piezas de la semana:  {total:,}")
print(f"Promedio por turno:   {promedio:,.1f}")
print(f"Mejor turno:          {mejor_turno} con {mejor_valor:,}")
print(f"Arriba del promedio:  {sobre_promedio:,.1f}")
```

**Salida**

```text
Piezas de la semana:  7,990
Promedio por turno:   1,331.7
Mejor turno:          T4 con 1,510
Arriba del promedio:  178.3
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro cifras son correctas | 4 |
| El mejor turno sale de `index` y `max`, no escrito a mano | 3 |
| Separador de miles y un decimal donde corresponde | 2 |
| Las etiquetas permiten leer el reporte sin ver el código | 1 |

**Error que más se ve**

Escribir `mejor_turno = "T4"` porque ya se vio en la salida anterior: el programa da el resultado correcto y deja de darlo en cuanto cambia un dato, que es justo lo que pasa en 01.3.

### 01.3 · Integrar

**Solución**

```python
turnos = ["T1", "T2", "T3", "T4", "T5", "T6"]
piezas = [1240, 1385, 1320, 1510, 1295, 1440]

total = sum(piezas)
promedio = total / len(piezas)
mejor_turno = turnos[piezas.index(max(piezas))]

folio = "00847"

print(f"Folio del lote:       {folio}")
print(f"Piezas de la semana:  {total:,}")
print(f"Promedio por turno:   {promedio:,.1f}")
print(f"Mejor turno:          {mejor_turno}")
```

Antes de la corrección: 7,990 piezas, 1,331.7 de promedio, T4. Después: 8,190 piezas, 1,365.0 de promedio, T4. El mejor turno no cambia porque T3 sigue por debajo de T4.

En la hoja de cálculo el cambio se habría propagado solo. En Python no se recalcula nada hasta que se vuelve a ejecutar el archivo, y ese es el segundo de los cuatro quiebres. La ventaja aparece al revés: el procedimiento quedó escrito, así que la corrección se puede volver a aplicar dentro de tres meses y dar exactamente lo mismo.

Capturado con formato de número, el folio se ve como 847: los ceros a la izquierda no son parte de un valor numérico y desaparecen. Es el tercero de los cuatro quiebres, el de los tipos. Un folio se guarda como texto porque es un identificador: no se suma, no se promedia, y su forma es lo único que permite volver a encontrarlo en el sistema que lo emitió.

**Salida**

```text
Folio del lote:       00847
Piezas de la semana:  8,190
Promedio por turno:   1,365.0
Mejor turno:          T4
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres cifras nuevas son correctas y se comparan con las anteriores | 3 |
| Nota que el mejor turno no cambia y dice por qué | 2 |
| Nombra el quiebre del recálculo y lo explica | 2 |
| Explica que el folio capturado como número se ve 847 | 2 |
| Explica por qué un folio es texto | 1 |

**Error que más se ve**

Afirmar que el mejor turno ahora es T3 porque fue el que cambió: se razona sobre el dato que se tocó en lugar de sobre el resultado, y basta comparar 1320 con 1510 para verlo.

---

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer

**Solución**

Pieza de 12.08 mm. Se evalúa `12.08 > 12.05`, que se cumple, y el veredicto queda en «Rechazo por exceso». Las otras dos ramas no se leen.

Pieza de 11.94 mm. Se evalúa `11.94 > 12.05`, que falla. Se evalúa `11.94 < 11.95`, que se cumple, y el veredicto queda en «Rechazo por defecto». El `SI NO` final no se lee.

Pieza de 12.05 mm exactos. Se evalúa `12.05 > 12.05`, que falla porque el operador pide estrictamente mayor. Se evalúa `12.05 < 11.95`, que también falla. Cae en el `SI NO` y el veredicto es «Aceptada». La pieza está justo en el límite y se libera.

Con la segunda versión, la pieza de 12.08 mm entra por `12.08 >= 11.95`, que se cumple, y sale como «Aceptada». La rama del rechazo por exceso es inalcanzable: cualquier diámetro mayor a 12.05 también es mayor o igual a 11.95, así que la primera condición se lo lleva siempre.

Esa segunda versión es finita, precisa, definida, tiene entrada y tiene salida. Cumple las cinco propiedades y aun así libera piezas que no pasan. Un algoritmo correcto en su forma puede estar resolviendo el problema equivocado, y por eso el orden de las condiciones se revisa con casos, no con la vista.

**Salida**

```text
Pieza      Condicion evaluada    Resultado    Veredicto
12.08 mm   12.08 > 12.05         Se cumple    Rechazo por exceso
11.94 mm   11.94 > 12.05         Falla        -
11.94 mm   11.94 < 11.95         Se cumple    Rechazo por defecto
12.05 mm   12.05 > 12.05         Falla        -
12.05 mm   12.05 < 11.95         Falla        Aceptada

Segunda version
12.08 mm   12.08 >= 11.95        Se cumple    Aceptada
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres trazas correctas, con las condiciones que no se leen marcadas | 4 |
| El caso de 12.05 sale aceptado y explica por qué | 2 |
| Traza la segunda versión y detecta que la rama del exceso es inalcanzable | 2 |
| Argumenta que cumple las cinco propiedades y aun así está mal | 2 |

**Error que más se ve**

Decir que la pieza de 12.05 se rechaza porque «llegó al límite»: se confunde el límite con la zona de rechazo, y se ve en que el alumno lee `>` como si fuera `>=`.

### 02.2 · Aplicar

**Solución**

```text
INICIO
    LEER guarda_cerrada, paro_liberado, temperatura_husillo

    SI guarda_cerrada = FALSO ENTONCES
        ESCRIBIR "Celda enclavada: guarda abierta"
    SI NO SI paro_liberado = FALSO ENTONCES
        ESCRIBIR "Celda enclavada: paro de emergencia oprimido"
    SI NO SI temperatura_husillo >= 68 ENTONCES
        ESCRIBIR "Celda enclavada: husillo caliente"
    SI NO
        ESCRIBIR "Celda armada"

    FIN
```

El diagrama de flujo lleva un óvalo de inicio, un paralelogramo de lectura de los tres datos, tres rombos encadenados por la salida del NO, cuatro paralelogramos de escritura y un óvalo de fin. Cada rombo tiene sus dos salidas etiquetadas.

El orden importa: la guarda se revisa primero porque es la condición que protege al operador, y una celda con la guarda abierta no se arma aunque el husillo esté frío.

**Salida**

```text
Caso 1: guarda cerrada, paro liberado, 61 C
  Rombo 1: guarda_cerrada = FALSO?   No, sigue
  Rombo 2: paro_liberado = FALSO?    No, sigue
  Rombo 3: 61 >= 68?                 No, sigue
  Salida: Celda armada

Caso 2: guarda cerrada, paro liberado, 71 C
  Rombo 1: guarda_cerrada = FALSO?   No, sigue
  Rombo 2: paro_liberado = FALSO?    No, sigue
  Rombo 3: 71 >= 68?                 Si
  Salida: Celda enclavada: husillo caliente
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El pseudocódigo revisa las tres condiciones en el orden pedido | 3 |
| Cada falla nombra cuál condición falló, no un mensaje genérico | 2 |
| El diagrama usa los cuatro símbolos por lo que significan | 2 |
| Los rombos tienen sus dos salidas etiquetadas y ambas llegan a algún lado | 1 |
| Las dos trazas son correctas | 2 |

**Error que más se ve**

Un solo rombo con las tres condiciones adentro y un mensaje de «falla en la verificación»: el algoritmo decide bien y no sirve, porque el operador no sabe qué revisar.

### 02.3 · Integrar

**Solución**

La prueba de las dos personas: dos inspectores con la misma pieza de 12.06 mm pueden decidir distinto, porque «se ve fuera de medida» depende de quién mire. Se rompe la propiedad de ser preciso, y con ella la de ser definido, porque los mismos datos no producen el mismo resultado.

```text
INICIO
    LEER diametro

    SI diametro > 12.05 ENTONCES
        destino = "Reproceso: rectificar"
    SI NO SI diametro < 11.95 ENTONCES
        destino = "Chatarra: submedida"
    SI NO
        destino = "Liberar"

    ESCRIBIR destino
FIN
```

Entrada: el diámetro medido de una pieza, en milímetros. Salida: el destino de esa pieza, un texto de tres valores posibles.

Caso límite que la primera versión no cubría: una lectura de 0.00 mm, que ocurre cuando el micrómetro no hizo contacto. Con el algoritmo de arriba esa pieza sale como chatarra por submedida, y no es cierto: la pieza no se ha medido. Se cubre con una rama al principio que rechace lecturas menores o iguales a cero y pida volver a medir.

**Salida**

```text
Instruccion original     Dos inspectores, un mismo 12.06 mm, dos destinos
Propiedad rota           Preciso, y con ella la de ser definido

Traza de tres piezas
12.06 mm   12.06 > 12.05    Se cumple    Reproceso: rectificar
11.90 mm   11.90 > 12.05    Falla
11.90 mm   11.90 < 11.95    Se cumple    Chatarra: submedida
12.00 mm   las dos fallan                Liberar

Caso limite agregado
 0.00 mm   diametro <= 0    Se cumple    Volver a medir
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Aplica la prueba de las dos personas con un valor concreto | 2 |
| Nombra la propiedad rota y la justifica | 2 |
| El algoritmo tiene las tres salidas y usa la banda correcta | 3 |
| Identifica entrada y salida por escrito | 1 |
| El caso límite rompía la versión anterior y se explica qué cambió | 2 |

**Error que más se ve**

Reescribir la instrucción con más palabras pero sin números: «si el diámetro está muy fuera del nominal» sigue dependiendo de quién lea, y se detecta porque no aparece ni un 11.95 ni un 12.05 en toda la hoja.

---

## Semana 03 · Temas 1 y 2 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**Solución**

La traza: después de la primera línea `piezas` vale 1240, después de la segunda 1325 y después de la tercera 2650. El programa imprime 2650. El signo igual no compara, guarda, y cada línea pisa el valor que dejó la anterior.

Fragmento A: no corre. `NameError`, porque `Suma` con mayúscula no existe. Rompe la regla de las mayúsculas.

Fragmento B: no corre. `SyntaxError` de cadena sin cerrar, en la línea 2. Rompe la regla de las comillas.

Fragmento C: no corre. `SyntaxError` que dice que el paréntesis nunca se cerró, y lo reclama en la línea 2 aunque el problema esté ahí mismo, al final del archivo. Rompe la regla de los paréntesis.

Fragmento D: no corre. `NameError`, porque `Print` con mayúscula no es `print`. Rompe la regla de las mayúsculas.

**Salida**

```text
2650

A  NameError: name 'Suma' is not defined. Did you mean: 'sum'?
B  SyntaxError: unterminated string literal (detected at line 2)
C  SyntaxError: '(' was never closed
D  NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La traza de las tres líneas con sus valores intermedios | 3 |
| Los cuatro fragmentos clasificados como corre o no corre | 2 |
| El tipo de error correcto en los cuatro | 3 |
| Nombra la regla rota en cada uno | 2 |

**Error que más se ve**

Contestar 250 en la traza, multiplicando antes de sumar: se lee el programa como una fórmula con precedencia, cuando son tres asignaciones que corren en orden.

### 03.2 · Aplicar

**Solución**

```python
# Lecturas del tacometro del transportador, en rpm.
from statistics import mean

lecturas = [1496, 1502, 1488, 1511, 1494]

promedio = mean(lecturas)
maxima = max(lecturas)

print("Muestras:", len(lecturas))
print("Promedio rpm:", promedio)
print("Lectura mayor:", maxima)
```

La tabla de los tres errores provocados:

| Qué se rompió | Mensaje |
|---|---|
| Paréntesis de cierre | `SyntaxError: '(' was never closed` |
| `print` con mayúscula | `NameError: name 'Print' is not defined. Did you mean: 'print'?` |
| Comilla borrada | `SyntaxError: unterminated string literal (detected at line 2)` |

**Salida**

```text
Muestras: 5
Promedio rpm: 1498.2
Lectura mayor: 1511
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El programa corre y las tres cifras son correctas | 3 |
| Trae comentario, importación y etiquetas en los `print` | 2 |
| Los tres mensajes de error se transcriben completos | 3 |
| Reporta la línea que señaló cada error | 2 |

**Error que más se ve**

Entregar los mensajes parafraseados, del estilo «marcó error de sintaxis»: se pierde justo lo que sirve, que es la última palabra del mensaje y el número de línea.

### 03.3 · Integrar

**Solución**

```python
# Traduccion del pseudocodigo del veredicto, semana 2.
diametro = 12.05

if diametro > 12.05:
    veredicto = "Rechazo por exceso"
elif diametro < 11.95:
    veredicto = "Rechazo por defecto"
else:
    veredicto = "Aceptada"

print("Diametro medido:", diametro, "mm")
print("Veredicto:", veredicto)
```

La corrida de 12.00 imprime `12.0` porque el cero final no es parte del valor. El número guardado es doce, y cuántos decimales se ven es una decisión de presentación que se resuelve con formato, no con el dato.

Si se intercambian las dos primeras ramas, una pieza de 12.08 mm sigue saliendo como rechazo por exceso, porque `12.08 < 11.95` falla y la segunda rama sí se evalúa. El intercambio que sí rompe el algoritmo es el de la semana 2, donde la rama de aceptada se pone primero.

**Salida**

```text
Diametro medido: 12.05 mm
Veredicto: Aceptada

Diametro medido: 11.94 mm
Veredicto: Rechazo por defecto

Diametro medido: 12.0 mm
Veredicto: Aceptada
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La traducción respeta el orden de las tres ramas | 3 |
| Las tres corridas se pegan completas y son correctas | 3 |
| Explica por qué imprime `12.0` | 2 |
| Contesta correctamente sobre el intercambio de ramas | 2 |

**Error que más se ve**

Escribir tres `if` sueltos en lugar de `if`, `elif` y `else`: con estas tres condiciones el resultado coincide, y el alumno no nota que ya evaluó tres comparaciones donde bastaba una.

---

## Semana 04 · Tema 3 · Datos, tipos y operaciones primitivas

### 04.1 · Reconocer

**Solución**

```text
51.666666666666664
51
16
1205
17
True
False
0.15000000000000002
```

La segunda línea dice cuántas charolas se llenan por completo: 51. La tercera dice cuántas piezas quedan sueltas después de llenarlas: 16.

La sexta y la séptima línea comparan decimales que en papel salen exactos y dan resultados opuestos. La razón es que 0.05 no se puede representar exactamente en binario. En un caso los errores de redondeo se cancelan y la igualdad se cumple; en el otro no. Por eso la banda de tolerancia se escribe con sus dos límites como constantes y nunca se calcula sumando y restando dentro de una condición.

**Salida**

```text
51.666666666666664
51
16
1205
17
True
False
0.15000000000000002
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho líneas correctas, con la primera sin redondear | 4 |
| Interpreta la división entera y el residuo en charolas y piezas | 2 |
| Distingue la concatenación de texto de la suma de enteros | 2 |
| Explica por qué dos comparaciones parecidas dan resultados opuestos | 2 |

**Error que más se ve**

Contestar `True` en la séptima línea porque en papel 0.05 por 3 es 0.15: es el mismo razonamiento correcto que produce una condición de tolerancia que falla una vez cada mil piezas.

### 04.2 · Aplicar

**Solución**

```python
celda = "C-3"
estacion = "EST-01"
fecha = "2026-01-08"
piezas = 1240
rechazos = 37
consumo_kwh = 86.4
estacion_activa = True
ultimo_paro = None

tasa_rechazo = rechazos / piezas
consumo_por_pieza = consumo_kwh / piezas

print(f"{celda} {estacion} {fecha}")
print(f"Tasa de rechazo:   {round(tasa_rechazo * 100, 2)} %")
print(f"Consumo por pieza: {round(consumo_por_pieza, 4)} kWh")
print(type(piezas), type(consumo_kwh))
print(type(estacion), type(estacion_activa), type(ultimo_paro))
```

La fecha se guarda como texto porque todavía no hay nada que hacer con ella. `ultimo_paro` vale `None`, que es ausencia de dato, y no cero: cero minutos de paro es una medición, `None` es que nadie registró nada.

**Salida**

```text
C-3 EST-01 2026-01-08
Tasa de rechazo:   2.98 %
Consumo por pieza: 0.0697 kWh
<class 'int'> <class 'float'>
<class 'str'> <class 'bool'> <class 'NoneType'>
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho variables con el tipo que les corresponde | 3 |
| `ultimo_paro` en `None` y no en cero, con la explicación | 2 |
| Las dos métricas correctas y redondeadas | 3 |
| Los nombres dicen qué guardan y ninguno es de una letra | 2 |

**Error que más se ve**

Poner `ultimo_paro = 0`: el programa corre y el promedio de duración de paros sale mal en cuanto alguien lo calcule, porque un turno sin paros entra al promedio como un paro de cero minutos.

### 04.3 · Integrar

**Solución**

```python
piezas = 1240
rechazos = 37
consumo_kwh = 86.4
por_charola = 24

por_pieza_mal = consumo_kwh / piezas - rechazos
por_pieza_bien = consumo_kwh / (piezas - rechazos)

print(f"Sin parentesis: {round(por_pieza_mal, 4)}")
print(f"Con parentesis: {round(por_pieza_bien, 4)} kWh por pieza buena")

buenas = piezas - rechazos
charolas_llenas = buenas // por_charola
sueltas = buenas % por_charola

print(f"Piezas buenas: {buenas}")
print(f"Charolas llenas: {charolas_llenas}, piezas sueltas: {sueltas}")

folio = "00847"

print(f"Folio: {folio}  entero: {int(folio)}  de regreso: {str(int(folio))}")
```

La primera versión divide el consumo entre todas las piezas y después le resta 37 al resultado, o sea le resta piezas a un consumo por pieza. Da negativo porque está restando peras a kilowatts. La segunda reparte el consumo del turno entre las 1203 piezas que sí sirvieron, que es la pregunta que se hizo.

El folio pierde los ceros a la izquierda en cuanto se vuelve entero, y ya no los recupera al regresar a texto. Lo que se perdió no es el número, es el identificador.

**Salida**

```text
Sin parentesis: -36.9303
Con parentesis: 0.0718 kWh por pieza buena
Piezas buenas: 1203
Charolas llenas: 50, piezas sueltas: 3
Folio: 00847  entero: 847  de regreso: 847
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos expresiones escritas y sus dos resultados | 3 |
| Explica qué calcula cada una, no solo cuál está bien | 2 |
| Charolas llenas y piezas sueltas correctas | 3 |
| Reporta la pérdida de los ceros del folio y qué implica | 2 |

**Error que más se ve**

Calcular las charolas con las 1240 piezas producidas en lugar de las 1203 buenas: el número queda cerca del correcto, y por eso nadie lo revisa hasta que faltan piezas en el embarque.

---

## Semana 05 · Tema 4 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Solución**

```text
Piezas: 1,240
Consumo: 86.40 kWh
Rechazo: 3.0%
Rechazo: 2.98%
EST-01        1240
Tasa cruda: 0.029838709677419355
Consumo: {consumo:.2f} kWh
```

Las líneas tercera y cuarta muestran el mismo dato con distinto número de decimales: la de un decimal redondea 2.98 a 3.0, y en un reporte de calidad esa diferencia decide si la estación aparece dentro o fuera de una meta de 3 %.

A la última línea le falta la `f` antes de la comilla. No es un error: la cadena se imprime tal cual, con las llaves y el código de formato adentro, y el programa sigue corriendo como si nada.

**Salida**

```text
Piezas: 1,240
Consumo: 86.40 kWh
Rechazo: 3.0%
Rechazo: 2.98%
EST-01        1240
Tasa cruda: 0.029838709677419355
Consumo: {consumo:.2f} kWh
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete líneas correctas, con sus comas y sus espacios | 5 |
| Explica el redondeo de 2.98 a 3.0 y por qué importa | 2 |
| Detecta la `f` faltante y dice que no lanza error | 3 |

**Error que más se ve**

Escribir `Rechazo: 0.0%` en la tercera línea: se olvida que el código de porcentaje ya multiplica por cien, y la pista es que el alumno también escriba `2.98` como si fuera el valor crudo.

### 05.2 · Aplicar

**Solución**

```python
estacion = input("Estacion: ")
piezas = int(input("Piezas producidas: "))
rechazos = int(input("Piezas rechazadas: "))
consumo = float(input("Consumo del turno en kWh: "))

tasa = rechazos / piezas
por_pieza = consumo / piezas

print(f"Estacion:          {estacion}")
print(f"Piezas:            {piezas:,}")
print(f"Rechazos:          {rechazos:,}")
print(f"Tasa de rechazo:   {tasa:.2%}")
print(f"Consumo por pieza: {por_pieza:.4f} kWh")
```

**Salida**

```text
Estacion: EST-01
Piezas producidas: 1240
Piezas rechazadas: 37
Consumo del turno en kWh: 86.4
Estacion:          EST-01
Piezas:            1,240
Rechazos:          37
Tasa de rechazo:   2.98%
Consumo por pieza: 0.0697 kWh
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro `input` traen mensaje y se convierten donde toca | 3 |
| Las dos métricas son correctas | 3 |
| Formato de miles, porcentaje y cuatro decimales aplicados | 2 |
| La sesión se entrega completa, con lo capturado | 2 |

**Error que más se ve**

Convertir después de operar, con `int(piezas / rechazos)` en lugar de convertir cada `input`: la división de dos textos revienta antes, y cuando no revienta es porque el alumno concatenó sin darse cuenta.

### 05.3 · Integrar

**Solución**

```python
SEGUNDOS_TURNO = 28800

estacion = input("Estacion: ")
piezas = int(input("Piezas producidas: "))
rechazos = int(input("Piezas rechazadas: "))
consumo = float(input("Consumo del turno en kWh: "))

buenas = piezas - rechazos
tasa = rechazos / piezas
ciclo = SEGUNDOS_TURNO / piezas
por_buena = consumo * 1000 / buenas

print(f"Reporte de turno {estacion}")
print(f"{'Piezas producidas':<22}{piezas:>10,}")
print(f"{'Piezas buenas':<22}{buenas:>10,}")
print(f"{'Tasa de rechazo':<22}{tasa:>10.2%}")
print(f"{'Tiempo de ciclo':<22}{ciclo:>10.2f} s")
print(f"{'Energia por pieza buena':<22}{por_buena:>10.1f} Wh")
```

El tiempo de ciclo se calcula con las piezas producidas, porque la máquina ocupó tiempo también en las que salieron mal. La energía por pieza buena se reparte solo entre las buenas, porque es un costo que hay que cargarle a lo que sí se vende. Dos denominadores distintos en el mismo reporte, cada uno con su razón.

**Salida**

```text
Estacion: EST-03
Piezas producidas: 1512
Piezas rechazadas: 68
Consumo del turno en kWh: 112.8
Reporte de turno EST-03
Piezas producidas          1,512
Piezas buenas              1,444
Tasa de rechazo            4.50%
Tiempo de ciclo            19.05 s
Energia por pieza buena      78.1 Wh
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco cifras correctas | 4 |
| La constante del turno tiene nombre y está arriba | 1 |
| Las cinco líneas alineadas con los anchos pedidos | 2 |
| Cada cifra lleva su unidad | 1 |
| Justifica los dos denominadores distintos | 2 |

**Error que más se ve**

Calcular el tiempo de ciclo con las piezas buenas: sale 19.94 segundos y suena razonable, pero la máquina no dejó de trabajar en las 68 piezas que salieron mal.

---

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer

**Solución**

El primer programa imprime `12.05 Aceptada`. La condición pide estrictamente mayor, y 12.05 no es mayor que 12.05, así que la pieza cae en el `else`. Es el comportamiento correcto: el límite superior es parte de la banda.

El segundo programa imprime `12.08 Aceptada`, y eso está mal. La primera condición pregunta si el diámetro es mayor o igual al límite inferior, y una pieza de 12.08 lo cumple. Como la primera rama que se cumple es la que se ejecuta, la del rechazo por exceso nunca se alcanza: cualquier valor mayor a 12.05 también es mayor o igual a 11.95.

El orden correcto va de lo más exigente a lo menos: primero el exceso, después el defecto, y al final la aceptación como caso restante.

**Salida**

```text
12.05 Aceptada
12.08 Aceptada
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos salidas correctas | 4 |
| Explica por qué 12.05 se acepta con el operador estricto | 2 |
| Detecta que la rama del exceso es inalcanzable y dice por qué | 2 |
| Escribe el orden correcto de las tres condiciones | 2 |

**Error que más se ve**

Decir que el segundo programa lanza un error porque hay dos condiciones que se cumplen: no hay error, se ejecuta la primera y las demás ni se leen, que es exactamente lo que lo vuelve peligroso.

### 06.2 · Aplicar

**Solución**

```python
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05

pieza = input("Folio de la pieza: ")
diametro = float(input("Diametro medido en mm: "))

if diametro > LIMITE_SUPERIOR:
    veredicto = "Rechazo por exceso"
elif diametro < LIMITE_INFERIOR:
    veredicto = "Rechazo por defecto"
else:
    veredicto = "Aceptada"

print(f"Pieza {pieza}: {diametro:.2f} mm -> {veredicto}")
```

**Salida**

```text
Folio de la pieza: BJ-1003
Diametro medido en mm: 12.06
Pieza BJ-1003: 12.06 mm -> Rechazo por exceso

Folio de la pieza: BJ-1005
Diametro medido en mm: 11.94
Pieza BJ-1005: 11.94 mm -> Rechazo por defecto

Folio de la pieza: BJ-1008
Diametro medido en mm: 12.05
Pieza BJ-1008: 12.05 mm -> Aceptada

Folio de la pieza: BJ-1013
Diametro medido en mm: 11.95
Pieza BJ-1013: 11.95 mm -> Aceptada

Folio de la pieza: BJ-1004
Diametro medido en mm: 12.00
Pieza BJ-1004: 12.00 mm -> Aceptada
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres veredictos correctos en las cinco corridas | 4 |
| Los dos límites son constantes con nombre, no números sueltos | 2 |
| Las piezas de 12.05 y 11.95 salen aceptadas | 2 |
| El folio se lee como texto y el diámetro se convierte a decimal | 2 |

**Error que más se ve**

Usar `>=` en la primera condición: las piezas de 12.05 se rechazan, la estación pierde alrededor de una de cada diez, y el programa se ve perfectamente correcto.

### 06.3 · Integrar

**Solución**

```python
NOMINAL = 12.00
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05
TOPE_REPROCESO = 12.15
TOPE_CONCESION = 11.85

diametro = float(input("Diametro medido en mm: "))

if diametro <= 0 or diametro > 20:
    veredicto = "Dato invalido: revisar el micrometro"
elif diametro > TOPE_REPROCESO:
    veredicto = "Chatarra por sobremedida"
elif diametro > LIMITE_SUPERIOR:
    veredicto = "Reproceso: rectificar"
elif diametro >= LIMITE_INFERIOR:
    veredicto = "Aceptada"
elif diametro >= TOPE_CONCESION:
    veredicto = "Desviacion: liberar con concesion"
else:
    veredicto = "Chatarra por submedida"

print(f"{diametro:>7.2f} mm  {veredicto}")
```

La validación va primero porque una lectura de -3.00 mm no es una pieza corta, es un micrómetro mal usado, y clasificarla como chatarra escondería la falla del instrumento.

Tabla de fronteras:

| Frontera | Valor exacto | Veredicto | Por qué ese operador |
|---|---|---|---|
| Tope de reproceso | 12.15 | Reproceso | `>` deja el 12.15 del lado recuperable, que es lo que puede la rectificadora |
| Límite superior | 12.05 | Aceptada | `>` incluye el límite en la banda, como dice el plano |
| Límite inferior | 11.95 | Aceptada | `>=` incluye el límite en la banda |
| Tope de concesión | 11.85 | Concesión | `>=` deja el 11.85 del lado que ingeniería puede liberar |
| Validación | 0 y 20 | Inválido | `<=` en cero porque una lectura de cero es falta de contacto |

**Salida**

```text
Diametro medido en mm: 12.30
  12.30 mm  Chatarra por sobremedida
Diametro medido en mm: 12.15
  12.15 mm  Reproceso: rectificar
Diametro medido en mm: 12.06
  12.06 mm  Reproceso: rectificar
Diametro medido en mm: 12.05
  12.05 mm  Aceptada
Diametro medido en mm: 12.00
  12.00 mm  Aceptada
Diametro medido en mm: 11.95
  11.95 mm  Aceptada
Diametro medido en mm: 11.90
  11.90 mm  Desviacion: liberar con concesion
Diametro medido en mm: 11.85
  11.85 mm  Desviacion: liberar con concesion
Diametro medido en mm: 11.80
  11.80 mm  Chatarra por submedida
Diametro medido en mm: -3.00
  -3.00 mm  Dato invalido: revisar el micrometro
Diametro medido en mm: 25.00
  25.00 mm  Dato invalido: revisar el micrometro
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco categorías son excluyentes y están en el orden correcto | 3 |
| La validación va antes de clasificar y atrapa los dos casos imposibles | 2 |
| Las once corridas son correctas | 2 |
| Las cinco fronteras están como constantes con nombre | 1 |
| La tabla documenta el veredicto del valor exacto de cada frontera | 2 |

**Error que más se ve**

Poner la validación al final, después del `else`: nunca se ejecuta, porque para entonces el -3.00 ya salió clasificado como chatarra por submedida y el programa no marca nada.

---

## Semana 07 · Tema 4.4 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**Solución**

```text
Estacion critica
True
False
Sin datos suficientes
True
```

Línea 1. La condición es `estacion == "EST-01" or "EST-03"`. Python evalúa la comparación, que da falso, y después evalúa la cadena `"EST-03"`, que por no estar vacía cuenta como verdadera. La condición completa siempre es verdadera, incluso con EST-04. La forma correcta es `estacion in ["EST-01", "EST-03"]`.

Línea 2. Las dos listas tienen los mismos valores en el mismo orden, así que son iguales.

Línea 3. Son dos listas distintas en memoria, así que `is` da falso. El doble igual compara contenido, `is` compara identidad.

Línea 4. Con cero piezas, `piezas > 0` es falso y Python ya no evalúa la división. Esa es la evaluación corta del `and`, y es lo que evita el `ZeroDivisionError`. Con `or` la primera condición falsa obliga a evaluar la segunda, y ahí sí revienta.

Línea 5. `ultimo_paro is None` es la forma correcta de preguntar por la ausencia de un valor.

**Salida**

```text
Estacion critica
True
False
Sin datos suficientes
True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas correctas | 4 |
| Explica por qué la primera condición siempre es verdadera y la corrige con `in` | 2 |
| Distingue `==` de `is` con el argumento de identidad | 2 |
| Explica la evaluación corta y por qué con `or` sí reventaría | 2 |

**Error que más se ve**

Contestar «Estacion normal» en la primera línea razonando sobre la intención del código: se lee lo que quiso decir el autor en lugar de lo que Python evalúa, y se detecta porque el alumno tampoco nota nada raro con EST-04.

### 07.2 · Aplicar

**Solución**

```python
CRITICAS = ["EST-01", "EST-03"]
TASA_MAXIMA = 0.03
MINIMO_PIEZAS = 500

estacion = input("Estacion: ")
piezas = int(input("Piezas del lote: "))
rechazos = int(input("Piezas rechazadas: "))
en_mantenimiento = input("En mantenimiento (si/no): ") == "si"

tasa = rechazos / piezas

if not en_mantenimiento and piezas >= MINIMO_PIEZAS and tasa <= TASA_MAXIMA:
    decision = "Lote liberado"
elif estacion in CRITICAS:
    decision = "Retener: estacion critica que no cumplio"
else:
    decision = "Retener para inspeccion al cien por ciento"

print(f"{estacion} {piezas:>5} piezas  tasa {tasa:.2%}  -> {decision}")
```

**Salida**

```text
Estacion: EST-01
Piezas del lote: 1240
Piezas rechazadas: 37
En mantenimiento (si/no): no
EST-01  1240 piezas  tasa 2.98%  -> Lote liberado

Estacion: EST-03
Piezas del lote: 1512
Piezas rechazadas: 68
En mantenimiento (si/no): no
EST-03  1512 piezas  tasa 4.50%  -> Retener: estacion critica que no cumplio

Estacion: EST-04
Piezas del lote: 760
Piezas rechazadas: 9
En mantenimiento (si/no): no
EST-04   760 piezas  tasa 1.18%  -> Lote liberado

Estacion: EST-02
Piezas del lote: 420
Piezas rechazadas: 5
En mantenimiento (si/no): no
EST-02   420 piezas  tasa 1.19%  -> Retener para inspeccion al cien por ciento

Estacion: EST-01
Piezas del lote: 1240
Piezas rechazadas: 37
En mantenimiento (si/no): si
EST-01  1240 piezas  tasa 2.98%  -> Retener: estacion critica que no cumplio
```

El cuarto caso es el que enseña algo: EST-02 tiene una tasa de 1.19 %, mejor que la de EST-01, y aun así se retiene. El lote de 420 piezas no llega al mínimo, y sin volumen la tasa no significa nada.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco decisiones correctas | 4 |
| La regla de liberación usa `and` con las tres condiciones | 2 |
| La pertenencia se pregunta con `in` sobre la lista de críticas | 2 |
| Los tres umbrales son constantes con nombre | 1 |
| Comenta el caso del lote chico con buena tasa | 1 |

**Error que más se ve**

Escribir `estacion in "EST-01"` sin corchetes: la condición pasa a preguntar si el texto está contenido en el otro texto, funciona por accidente con EST-01 y falla en silencio con cualquier otra.

### 07.3 · Integrar

**Solución**

```python
LIMITE_TEMPERATURA = 68.0
LIMITE_VIBRACION = 4.5

temperatura = float(input("Temperatura del husillo en C: "))
vibracion = float(input("Vibracion en mm/s: "))

if temperatura > LIMITE_TEMPERATURA:
    if vibracion > LIMITE_VIBRACION:
        anidada = "Detener la estacion"
    else:
        anidada = "Seguir operando"
else:
    if vibracion > LIMITE_VIBRACION:
        anidada = "Seguir operando"
    else:
        anidada = "Seguir operando"

if temperatura > LIMITE_TEMPERATURA and vibracion > LIMITE_VIBRACION:
    combinada = "Detener la estacion"
else:
    combinada = "Seguir operando"

print(f"{temperatura:>5.1f} C  {vibracion:>4.1f} mm/s  "
      f"anidada: {anidada:<20} combinada: {combinada:<20} "
      f"iguales: {anidada == combinada}")
```

Este anidado se podía colapsar porque las dos ramas internas del `else` externo hacen exactamente lo mismo. Cuando eso pasa, la segunda pregunta no aporta nada en ese camino, y las cuatro ramas se reducen a una condición unida con `and`.

Un caso de la misma celda donde el anidado no se colapsa: si la estación está en mantenimiento, su vibración no significa nada y la acción es reactivarla; si no lo está, la vibración decide entre subir el avance, mantener y detener. Ahí las ramas internas hacen tres cosas distintas y la rama externa hace una cuarta, así que el anidado gana algo real.

**Salida**

```text
Temperatura del husillo en C: 70.2
Vibracion en mm/s: 5.1
 70.2 C   5.1 mm/s  anidada: Detener la estacion  combinada: Detener la estacion  iguales: True

Temperatura del husillo en C: 70.2
Vibracion en mm/s: 3.8
 70.2 C   3.8 mm/s  anidada: Seguir operando      combinada: Seguir operando      iguales: True

Temperatura del husillo en C: 64.0
Vibracion en mm/s: 5.1
 64.0 C   5.1 mm/s  anidada: Seguir operando      combinada: Seguir operando      iguales: True

Temperatura del husillo en C: 64.0
Vibracion en mm/s: 3.8
 64.0 C   3.8 mm/s  anidada: Seguir operando      combinada: Seguir operando      iguales: True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La versión colapsada es correcta y usa una sola condición | 3 |
| Los cuatro casos coinciden y se entrega la comprobación | 3 |
| Explica que las ramas internas iguales son la señal | 2 |
| Describe un caso donde el anidado sí se justifica | 2 |

**Error que más se ve**

Colapsar con `or` en lugar de `and`: los cuatro casos dejan de coincidir en el segundo y el tercero, y el alumno que no corrió la comprobación entrega las dos versiones como equivalentes.

---

## Semana 08 · Tema 4.5 · Repetición · Primer parcial

### 08.1 · Reconocer

**Solución**

El `for` imprime cinco líneas: 38, 42, 46, 50 y 54. El `range` con paso 4 arranca en 38 y se detiene antes de 56, así que el 56 no aparece nunca. El último valor que cabe es 54.

El `while` imprime `7 -2.5`. El tanque arranca con 50.0 litros y cada turno consume 7.5, así que después de seis turnos quedan 5.0 litros. La condición pregunta si queda más de cero, y con 5.0 litros se cumple, así que entra a la séptima vuelta y resta 7.5 otra vez. El contador queda en 7 y el nivel en -2.5.

Turnos completos que aguanta de verdad: seis. El séptimo empezó y se quedó sin refrigerante a la mitad, y el número negativo es la evidencia de eso.

Si se borra la línea que resta el consumo, la condición nunca cambia y el ciclo no termina. Hay que detenerlo con Control C.

**Salida**

```text
38
42
46
50
54
7 -2.5
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco líneas del `for` y el conteo | 3 |
| La salida del `while` con el nivel negativo | 3 |
| Distingue los 7 impresos de los 6 turnos completos reales | 2 |
| Identifica el ciclo infinito si se borra la resta | 2 |

**Error que más se ve**

Contestar que el tanque aguanta 7 turnos porque eso imprime el programa: el número está bien calculado y contesta otra pregunta, y el -2.5 que aparece al lado es justo la pista que nadie lee.

### 08.2 · Aplicar

**Solución**

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas = [1240, 984, 1512, 760]
rechazos = [37, 12, 68, 9]
consumo = [86.4, 61.5, 112.8, 48.2]

total_piezas = 0
total_rechazos = 0
total_consumo = 0.0

print(f"{'Estacion':<10}{'Piezas':>8}{'Rechazo':>10}{'kWh/pieza':>12}")

for i in range(len(estaciones)):
    tasa = rechazos[i] / piezas[i]
    por_pieza = consumo[i] / piezas[i]

    total_piezas += piezas[i]
    total_rechazos += rechazos[i]
    total_consumo += consumo[i]

    print(f"{estaciones[i]:<10}{piezas[i]:>8,}{tasa:>10.2%}{por_pieza:>12.4f}")

tasa_celda = total_rechazos / total_piezas
consumo_celda = total_consumo / total_piezas

print(f"{'CELDA C-3':<10}{total_piezas:>8,}{tasa_celda:>10.2%}{consumo_celda:>12.4f}")
```

El renglón de la celda divide la suma de rechazos entre la suma de piezas. Promediar las cuatro tasas daría 2.47 %, que le da el mismo peso a EST-04 con 760 piezas que a EST-03 con 1512, y no es lo que produjo la celda.

**Salida**

```text
Estacion    Piezas   Rechazo   kWh/pieza
EST-01       1,240     2.98%      0.0697
EST-02         984     1.22%      0.0625
EST-03       1,512     4.50%      0.0746
EST-04         760     1.18%      0.0634
CELDA C-3    4,496     2.80%      0.0687
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro renglones y sus tres cifras correctas | 3 |
| El renglón de la celda divide sumas y no promedia tasas | 3 |
| Un solo recorrido, con los tres acumuladores fuera del ciclo | 2 |
| El ciclo funciona igual si se agrega una quinta estación | 1 |
| Salida alineada en columnas | 1 |

**Error que más se ve**

Calcular la tasa de la celda como el promedio de las cuatro: sale 2.47 % en vez de 2.80 %, se ve razonable, y subestima el rechazo justo donde está el volumen.

### 08.3 · Integrar

**Solución**

```python
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05

piezas = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
          "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
          "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

fuera = 0
suma = 0.0

for i in range(len(piezas)):
    diametro = diametros[i]
    suma += diametro

    if diametro > LIMITE_SUPERIOR:
        veredicto = "Rechazo por exceso"
        fuera += 1
    elif diametro < LIMITE_INFERIOR:
        veredicto = "Rechazo por defecto"
        fuera += 1
    else:
        veredicto = "Aceptada"

    print(f"{piezas[i]:<9}{diametro:>7.2f}  {veredicto}")

promedio = suma / len(diametros)
tasa = fuera / len(diametros)

print(f"{'Promedio':<9}{promedio:>7.4f} mm")
print(f"Fuera de tolerancia: {fuera} de {len(diametros)} ({tasa:.1%})")
```

La pieza BJ-1008 mide 12.05, que es exactamente el límite superior, y el límite es parte de la banda. Con `>=` en la primera condición saldrían 4 piezas fuera en lugar de 3, y la tasa del lote pasaría de 25.0 % a 33.3 % sin que ninguna pieza hubiera cambiado de medida.

**Salida**

```text
BJ-1001    12.01  Aceptada
BJ-1002    11.98  Aceptada
BJ-1003    12.06  Rechazo por exceso
BJ-1004    12.00  Aceptada
BJ-1005    11.94  Rechazo por defecto
BJ-1006    12.03  Aceptada
BJ-1007    11.99  Aceptada
BJ-1008    12.05  Aceptada
BJ-1009    11.96  Aceptada
BJ-1010    12.02  Aceptada
BJ-1011    12.08  Rechazo por exceso
BJ-1012    11.97  Aceptada
Promedio 12.0075 mm
Fuera de tolerancia: 3 de 12 (25.0%)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los doce veredictos correctos | 3 |
| Promedio a cuatro decimales y conteo de fuera de tolerancia | 3 |
| El acumulador y el contador están declarados antes del ciclo | 2 |
| Explica el caso de BJ-1008 y el efecto de cambiar a `>=` | 2 |

**Error que más se ve**

Declarar `suma = 0.0` dentro del `for`: al final vale 11.97, el promedio sale 0.9975 mm y lo delata que ningún buje de esta celda mide un milímetro.

---

## Semana 09 · Tema 4.5 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Solución**

El primer programa imprime `48.2`. Se esperaba 308.9, que es la suma de los cuatro consumos. La línea `total = 0.0` está dentro del ciclo, así que en cada vuelta borra lo acumulado y al final solo queda el último valor. La única línea que hay que mover es esa, y va antes del `for`.

El segundo programa imprime `Primera fuera de control: EST-03`. La traza de las cuatro vueltas:

| i | Estación | Piezas | Qué pasa |
|---|---|---|---|
| 0 | EST-01 | 1240 | Pasa el filtro. 2.98 % no rebasa 3 %, sigue |
| 1 | EST-02 | 984 | Menos de 1000 piezas, el `continue` la salta |
| 2 | EST-03 | 1512 | Pasa el filtro. 4.50 % sí rebasa, imprime y sale con `break` |
| 3 | EST-04 | 760 | No se evalúa, el `break` ya salió del ciclo |

El `else` del `for` no se ejecuta porque el ciclo salió por `break`. Se ejecutaría si ninguna estación con al menos 1000 piezas rebasara el 3 %, por ejemplo si EST-03 hubiera cerrado el turno con 40 rechazos en lugar de 68.

**Salida**

```text
48.2
Primera fuera de control: EST-03
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos salidas correctas | 3 |
| Identifica la línea mal colocada y dice a dónde va | 2 |
| La traza de las cuatro vueltas con el `continue` y el `break` | 3 |
| Explica cuándo sí correría el `else` del `for` | 2 |

**Error que más se ve**

Contestar 308.9 en el primer programa: se lee la intención del código y no su sangría, y es exactamente el error que produce totales equivocados que nadie revisa.

### 09.2 · Aplicar

**Solución**

```python
TASA_META = 0.03
CONSUMO_META = 0.070

estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas = [1240, 984, 1512, 760]
rechazos = [37, 12, 68, 9]
consumo = [86.4, 61.5, 112.8, 48.2]

energia_total = 0.0
fuera_de_meta = 0
hay_derrochadora = False

for i in range(len(estaciones)):
    energia_total += consumo[i]

    if rechazos[i] / piezas[i] > TASA_META:
        fuera_de_meta += 1

    if consumo[i] / piezas[i] > CONSUMO_META:
        hay_derrochadora = True

print(f"Energia del turno:        {energia_total:,.1f} kWh")
print(f"Estaciones fuera de meta: {fuera_de_meta}")
print(f"Alguna sobre 0.070 kWh:   {hay_derrochadora}")
```

La segunda pregunta cuenta casos, no magnitudes: sumar las tasas daría un número sin significado físico. La primera suma magnitudes: contar estaciones no dice cuánta energía se gastó. La bandera contesta si existe al menos una, y para eso no hace falta ni contar ni sumar.

**Salida**

```text
Energia del turno:        308.9 kWh
Estaciones fuera de meta: 1
Alguna sobre 0.070 kWh:   True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres respuestas correctas | 3 |
| Las tres variables declaradas antes del ciclo | 2 |
| Un solo recorrido para las tres preguntas | 2 |
| Las dos metas son constantes con nombre | 1 |
| Explica la diferencia entre contar y sumar | 2 |

**Error que más se ve**

Escribir la bandera como `hay_derrochadora = consumo[i] / piezas[i] > CONSUMO_META` sin el `if`: la variable se sobreescribe en cada vuelta y al final solo refleja la última estación, que en estos datos da falso.

### 09.3 · Integrar

**Solución**

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
piezas_por_hora = [155, 123, 189, 95]
turnos = ["T1", "T2", "T3"]
horas = [8, 8, 6]

produccion_total = 0
combinaciones_altas = 0

for i in range(len(estaciones)):
    for j in range(len(turnos)):
        proyeccion = piezas_por_hora[i] * horas[j]
        produccion_total += proyeccion

        if proyeccion > 1000:
            combinaciones_altas += 1

        print(f"{estaciones[i]:<8}{turnos[j]:<5}{proyeccion:>7,}")

print(f"{'TOTAL':<13}{produccion_total:>7,}")
print(f"Combinaciones arriba de 1000 piezas: {combinaciones_altas}")
```

Cuatro estaciones por tres turnos son doce renglones, y ese conteo se escribe antes de correr el programa. Con 40 estaciones y 3 turnos serían 120 vueltas, que sigue siendo nada. El problema aparece cuando los dos ciclos recorren listas largas: 1000 por 1000 son un millón de vueltas, y ahí un anidado deja de ser gratis.

**Salida**

```text
EST-01  T1     1,240
EST-01  T2     1,240
EST-01  T3       930
EST-02  T1       984
EST-02  T2       984
EST-02  T3       738
EST-03  T1     1,512
EST-03  T2     1,512
EST-03  T3     1,134
EST-04  T1       760
EST-04  T2       760
EST-04  T3       570
TOTAL         12,364
Combinaciones arriba de 1000 piezas: 5
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los doce renglones con la proyección correcta | 3 |
| El total y el conteo de combinaciones altas | 3 |
| Las dos variables de ciclo se llaman distinto y dicen qué recorren | 2 |
| Predice los doce renglones antes de correr el programa | 1 |
| Contesta el crecimiento de las vueltas con un ejemplo | 1 |

**Error que más se ve**

Usar `i` en los dos ciclos: el interno pisa al externo, salen renglones repetidos de la última estación y el total se descompone sin que Python marque nada.

---

## Semana 10 · Tema 5 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Solución**

La primera línea imprime `None`. La función calcula la división y no la devuelve, así que entrega el valor que Python devuelve por omisión cuando no hay `return`. La segunda imprime `69.6774193548387`, que sí es la energía por pieza en watt hora. La tercera lanza `NameError`.

Al `tasa_rechazo` le falta el `return`. El error no aparece dentro de la función porque ahí no hay nada mal escrito: aparece más adelante, en cuanto alguien intente multiplicar, comparar o formatear ese `None`.

La tercera línea falla porque `unitario` nació dentro de la función y desapareció cuando la función terminó. Fuera de ella ese nombre no existe.

Si la segunda función tuviera `print(unitario)` en lugar de `return unitario`, el número se vería en pantalla y la función devolvería `None`. El valor no se podría guardar, ni sumar, ni meter en una tabla.

**Salida**

```text
None
69.6774193548387
Traceback (most recent call last):
  File "w10_1.py", line 12, in <module>
    print(unitario)
          ^^^^^^^^
NameError: name 'unitario' is not defined
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres respuestas correctas, con el `NameError` nombrado | 4 |
| Explica por qué falta el `return` y dónde estalla el `None` | 2 |
| Explica el ámbito local de `unitario` | 2 |
| Distingue devolver de imprimir | 2 |

**Error que más se ve**

Contestar `0.02983` en la primera línea: se supone que una función que calcula algo lo entrega, y ese supuesto es el que produce el `None` que revienta tres líneas más abajo.

### 10.2 · Aplicar

**Solución**

```python
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05


def tasa_rechazo(piezas, rechazos):
    """Devuelve la fraccion de piezas rechazadas de un lote."""
    return rechazos / piezas


def dentro_de_tolerancia(diametro):
    """Dice si un diametro medido cae en la banda de 11.95 a 12.05 mm."""
    return diametro >= LIMITE_INFERIOR and diametro <= LIMITE_SUPERIOR


print(round(tasa_rechazo(1240, 37), 4))
print(round(tasa_rechazo(1512, 68), 4))
print(round(tasa_rechazo(760, 0), 4))

print(dentro_de_tolerancia(12.00))
print(dentro_de_tolerancia(12.05))
print(dentro_de_tolerancia(12.06))
```

El caso de 12.05 es el que hay que probar siempre porque es la frontera, y es donde se decide si el límite pertenece a la banda. Con `<` en lugar de `<=` esa pieza saldría fuera de tolerancia, y la función seguiría dando resultados correctos en todos los demás valores.

**Salida**

```text
0.0298
0.045
0.0
True
True
False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos funciones devuelven y ninguna imprime | 3 |
| Las seis llamadas dan el resultado correcto | 3 |
| Cada función trae docstring de un renglón | 2 |
| Explica por qué se prueba el valor exacto de la frontera | 2 |

**Error que más se ve**

Meter el `print` dentro de `dentro_de_tolerancia`: la función se ve funcionando en pantalla y no sirve para contar cuántas piezas pasan, que es justo lo que pide el ejercicio siguiente.

### 10.3 · Integrar

**Solución**

```python
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05


def dentro_de_tolerancia(diametro):
    """Dice si un diametro medido cae en la banda de tolerancia."""
    return diametro >= LIMITE_INFERIOR and diametro <= LIMITE_SUPERIOR


def veredicto(diametro):
    """Devuelve el destino de la pieza: aceptada, reproceso o chatarra."""
    if dentro_de_tolerancia(diametro):
        return "Aceptada"
    if diametro > LIMITE_SUPERIOR:
        return "Reproceso"
    return "Chatarra"


def piezas_aceptadas(diametros):
    """Cuenta cuantas mediciones de la lista caen dentro de tolerancia."""
    aceptadas = 0

    for diametro in diametros:
        if dentro_de_tolerancia(diametro):
            aceptadas += 1

    return aceptadas


def diametro_promedio(diametros):
    """Devuelve el promedio de la lista de mediciones."""
    suma = 0.0

    for diametro in diametros:
        suma += diametro

    return suma / len(diametros)


piezas = ["BJ-1001", "BJ-1002", "BJ-1003", "BJ-1004",
          "BJ-1005", "BJ-1006", "BJ-1007", "BJ-1008",
          "BJ-1009", "BJ-1010", "BJ-1011", "BJ-1012"]
diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

for i in range(len(piezas)):
    print(f"{piezas[i]:<9}{diametros[i]:>7.2f}  {veredicto(diametros[i])}")

print(f"Medidas:   {len(diametros)}")
print(f"Aceptadas: {piezas_aceptadas(diametros)}")
print(f"Promedio:  {diametro_promedio(diametros):.4f} mm")
```

La prueba de borrarle la comparación del límite inferior a `dentro_de_tolerancia`: la pieza BJ-1005, de 11.94 mm, pasaría a salir como aceptada y el conteo subiría de 9 a 10. Las pruebas que lo detectan son las que usan un valor por debajo de la banda; si el alumno solo probó 12.00, 12.05 y 12.06, ninguna lo detecta y hay que agregar el caso de 11.94.

**Salida**

```text
BJ-1001    12.01  Aceptada
BJ-1002    11.98  Aceptada
BJ-1003    12.06  Reproceso
BJ-1004    12.00  Aceptada
BJ-1005    11.94  Chatarra
BJ-1006    12.03  Aceptada
BJ-1007    11.99  Aceptada
BJ-1008    12.05  Aceptada
BJ-1009    11.96  Aceptada
BJ-1010    12.02  Aceptada
BJ-1011    12.08  Reproceso
BJ-1012    11.97  Aceptada
Medidas:   12
Aceptadas: 9
Promedio:  12.0075 mm
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro funciones con docstring y sin imprimir nada | 3 |
| `veredicto` llama a `dentro_de_tolerancia` en vez de repetir la comparación | 2 |
| Los doce renglones y las tres cifras finales correctos | 3 |
| La prueba de borrar una línea y decir qué caso la detecta | 2 |

**Error que más se ve**

Repetir la comparación de la banda dentro de `veredicto` en lugar de llamar a la función: el programa funciona igual, y cuando ingeniería cambie la tolerancia habrá que acordarse de los dos lugares.

---

## Semana 11 · Tema 5 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**Solución**

```text
69.68
0.35
74.68
```

En la primera llamada no se pasa nada opcional: `factor` vale 1000 y `perdidas` vale 0.0. Es la energía por pieza en watt hora.

En la segunda, el 5.0 cayó en `factor`, porque los argumentos por posición llenan los huecos en orden y `factor` es el que sigue después de `piezas`. La función calculó 86.4 por 5 entre 1240, que no significa nada. Python no marca error porque recibió tres argumentos válidos para tres parámetros que existen.

En la tercera, el 5.0 se pasa por nombre a `perdidas`, se salta `factor`, y el resultado son los 69.68 anteriores más las pérdidas.

Si `factor=1000` se moviera antes de `piezas`, el archivo ni siquiera correría: un parámetro con valor por omisión no puede ir antes de uno sin él, y Python lo rechaza con `SyntaxError` al leerlo.

**Salida**

```text
69.6774193548387
0.34838709677419355
74.6774193548387
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres números correctos | 4 |
| Identifica que el 5.0 cayó en `factor` en la segunda llamada | 2 |
| Explica por qué Python no marca ningún error | 2 |
| Contesta que mover el opcional al frente es `SyntaxError` | 2 |

**Error que más se ve**

Contestar que la segunda llamada suma 5.0 al resultado: se lee el 5.0 como si fuera la pérdida porque es el único opcional que se ve en la tercera llamada, y el orden de los parámetros ni se revisa.

### 11.2 · Aplicar

**Solución**

```python
def fuera_de_tolerancia(diametro, nominal=12.00, tolerancia=0.05):
    """Dice si una medicion cae fuera de la banda nominal mas o menos tolerancia."""
    inferior = nominal - tolerancia
    superior = nominal + tolerancia

    return diametro < inferior or diametro > superior


print(fuera_de_tolerancia(12.06))
print(fuera_de_tolerancia(12.05))
print(fuera_de_tolerancia(12.06, 12.00, 0.10))
print(fuera_de_tolerancia(12.06, tolerancia=0.10))
print(fuera_de_tolerancia(8.02, nominal=8.00))

print(12.00 - 0.05 == 11.95)
print(12.00 + 0.05 == 12.05)
```

Las dos comprobaciones del final dan verdadero, así que en este caso los límites calculados coinciden con los del plano. La comprobación no sobra: con otra tolerancia el resultado puede ser distinto, como se vio en la semana 4 con 0.05 por 3. Cuando una función calcula fronteras a partir de decimales, la frontera se prueba antes de confiar en ella.

**Salida**

```text
True
False
False
False
False
True
True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La función tiene los dos parámetros opcionales al final y su docstring | 2 |
| Las cinco llamadas dan el resultado correcto | 4 |
| Una llamada pasa la tolerancia por nombre saltándose el nominal | 2 |
| Las dos comprobaciones de frontera aparecen y se comentan | 2 |

**Error que más se ve**

Escribir `fuera_de_tolerancia(12.06, 0.10)` queriendo abrir la tolerancia: el 0.10 cae en `nominal`, la función compara contra una banda de 0.05 a 0.15 mm y devuelve verdadero por la razón equivocada.

### 11.3 · Integrar

**Solución**

```python
from statistics import mean, median, pstdev

LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05

diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

con_atipica = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
               11.99, 12.05, 11.96, 12.02, 12.08, 11.97, 12.90]

print(f"Mediciones: {len(diametros)}")
print(f"Promedio:   {mean(diametros):.4f} mm")
print(f"Mediana:    {median(diametros):.4f} mm")
print(f"Desviacion: {pstdev(diametros):.4f} mm")
print(f"Menor:      {sorted(diametros)[0]:.2f} mm")
print(f"Mayor:      {max(diametros):.2f} mm")

cp = (LIMITE_SUPERIOR - LIMITE_INFERIOR) / (6 * pstdev(diametros))
print(f"Cp:         {round(cp, 3)}")

print(f"Promedio con la lectura de 12.90: {mean(con_atipica):.4f} mm")
print(f"Mediana con la lectura de 12.90:  {median(con_atipica):.4f} mm")
```

La tercera función es `pstdev`, la desviación estándar de la población, documentada en la página del módulo `statistics` de docs.python.org. Recibe una serie de datos numéricos y devuelve la desviación estándar de esa serie tomada como población completa, no como muestra.

Un índice de capacidad de 0.41 significa que la variación del proceso es más ancha que la banda de tolerancia. La banda mide 0.10 mm y seis desviaciones miden 0.24 mm, así que aunque el proceso estuviera perfectamente centrado seguiría produciendo piezas fuera. Al jefe de producción no se le pide que ajuste el centrado: se le reporta que la máquina no da la tolerancia que pide el plano, y que hay que atacar la dispersión.

Con la lectura de 12.90 mm el promedio salta de 12.0075 a 12.0762 y la mediana solo se mueve de 12.0050 a 12.0100. Cuando hay una lectura sospechosa, la mediana es la que se reporta.

**Salida**

```text
Mediciones: 12
Promedio:   12.0075 mm
Mediana:    12.0050 mm
Desviacion: 0.0406 mm
Menor:      11.94 mm
Mayor:      12.08 mm
Cp:         0.41
Promedio con la lectura de 12.90: 12.0762 mm
Mediana con la lectura de 12.90:  12.0100 mm
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres funciones importadas y las siete cifras correctas | 3 |
| La tercera función sale de la documentación y se cita | 2 |
| El índice de capacidad es correcto y se interpreta | 3 |
| Compara promedio y mediana con la lectura atípica y elige una | 2 |

**Error que más se ve**

Reportar el índice de capacidad como si fuera un porcentaje de piezas buenas: 0.41 no es 41 %, es una razón entre el ancho de la tolerancia y el de la dispersión, y confundirlos convierte una alerta grave en un número que suena tolerable.

---

## Semana 12 · Tema 6 · Listas y tuplas

### 12.1 · Reconocer

**Solución**

```text
12.01 11.94
[11.98, 12.06]
[11.94, 11.98, 12.0, 12.01, 12.06]
[12.01, 11.98, 12.06, 12.0, 11.94]
None
[11.94, 11.98, 12.0, 12.01, 12.06]
6 5
```

La última línea lanza `IndexError`. La lista quedó con seis elementos después del `append`, así que el último índice válido es el 5.

`diametros[1:3]` devuelve dos valores porque el primer índice entra y el segundo no. Es lo que hace que el tamaño de la rebanada sea la resta de los dos números.

`respaldo` y `copia` terminan distintos porque `respaldo = diametros` no copió nada: creó un segundo nombre para la misma lista, y el `append` la modificó. `copia = diametros.copy()` sí construyó una lista nueva, que ya no se enteró del cambio.

Con `diametros = diametros.sort()`, el método ordena la lista y devuelve `None`, y esa asignación deja el nombre `diametros` apuntando a `None`. Los datos se pierden y el error aparece después, en la siguiente línea que intente usarlos.

**Salida**

```text
12.01 11.94
[11.98, 12.06]
[11.94, 11.98, 12.0, 12.01, 12.06]
[12.01, 11.98, 12.06, 12.0, 11.94]
None
[11.94, 11.98, 12.0, 12.01, 12.06]
6 5
Traceback (most recent call last):
  File "w12_1.py", line 17, in <module>
    print(diametros[6])
          ~~~~~~~~~^^^
IndexError: list index out of range
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete líneas correctas y el `IndexError` final | 4 |
| Explica la regla de la rebanada con el segundo índice excluido | 2 |
| Explica el alias contra la copia y por qué dan 6 y 5 | 2 |
| Explica qué pasa con `diametros = diametros.sort()` | 2 |

**Error que más se ve**

Contestar `[11.98, 12.06, 12.0]` en la segunda línea: se cuentan tres posiciones porque tres menos uno son dos y el alumno suma el extremo, y basta comprobar que la longitud siempre es la resta de los dos índices.

### 12.2 · Aplicar

**Solución**

```python
diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

print("Al empezar:", diametros)

mayor = max(diametros)
menor = min(diametros)
tres_altas = sorted(diametros, reverse=True)[0:3]
posicion = diametros.index(11.94)

print(f"Mayor:            {mayor:.2f} mm")
print(f"Menor:            {menor:.2f} mm")
print(f"Tres mas altas:   {tres_altas}")
print(f"Posicion de 11.94: {posicion}")
print(f"Pieza que le toca: BJ-{1001 + posicion}")
print(f"Ultimas tres:     {diametros[9:12]}")

print("Al terminar:", diametros)
```

El orden se pide con `sorted` y su argumento por nombre `reverse`, que es la semana 11 aplicada aquí. Con el método `sort` la lista original quedaría ordenada y el ejercicio pide lo contrario.

La posición 4 corresponde a la quinta pieza, que es la BJ-1005, porque el folio arranca en BJ-1001 y el índice en 0.

**Salida**

```text
Al empezar: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
Mayor:            12.08 mm
Menor:            11.94 mm
Tres mas altas:   [12.08, 12.06, 12.05]
Posicion de 11.94: 4
Pieza que le toca: BJ-1005
Ultimas tres:     [12.02, 12.08, 11.97]
Al terminar: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro respuestas correctas | 4 |
| La lista sale idéntica al principio y al final | 3 |
| El folio se calcula desde la posición y no se busca a mano | 2 |
| Usa `sorted` y no el método `sort` | 1 |

**Error que más se ve**

Contestar BJ-1004 para la lectura de 11.94: se suma el índice al folio inicial sin notar que la posición 4 es la quinta pieza, y el resultado queda corrido uno.

### 12.3 · Integrar

**Solución**

```python
BANDA = (12.00, 11.95, 12.05)

diametros = [12.01, 11.98, 12.06, 12.00, 11.94, 12.03,
             11.99, 12.05, 11.96, 12.02, 12.08, 11.97]

fuera = []

for diametro in diametros:
    if diametro < BANDA[1] or diametro > BANDA[2]:
        fuera.append(diametro)

fuera_ordenada = sorted(fuera, reverse=True)

print(f"Nominal {BANDA[0]:.2f} mm, banda de {BANDA[1]:.2f} a {BANDA[2]:.2f} mm")
print(f"Mediciones:  {len(diametros)}")
print(f"Fuera:       {len(fuera)}")
print(f"Fuera de tolerancia, de mayor a menor: {fuera_ordenada}")
print(f"Original intacta: {diametros}")

BANDA[2] = 12.10
```

La banda va en una tupla porque son los valores del plano y no deben cambiar mientras el programa corre. Si estuviera en una lista, cualquier línea podría modificarla por accidente y el programa seguiría corriendo con una tolerancia distinta a la que dice el dibujo. El intento de asignación falla de inmediato y con un mensaje claro, que es exactamente lo que se quiere de una constante.

**Salida**

```text
Nominal 12.00 mm, banda de 11.95 a 12.05 mm
Mediciones:  12
Fuera:       3
Fuera de tolerancia, de mayor a menor: [12.08, 12.06, 11.94]
Original intacta: [12.01, 11.98, 12.06, 12.0, 11.94, 12.03, 11.99, 12.05, 11.96, 12.02, 12.08, 11.97]
Traceback (most recent call last):
  File "w12_3.py", line 20, in <module>
    BANDA[2] = 12.10
    ~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La lista nueva trae exactamente las tres que se salen | 3 |
| La lista original conserva su orden y su contenido | 2 |
| El orden descendente se obtiene sin destruir nada | 2 |
| El error de la tupla se pega completo | 1 |
| Argumenta por qué la banda va en tupla | 2 |

**Error que más se ve**

Escribir `fuera = diametros` y después quitarle a esa lista las piezas que sí pasan: no hay dos listas, hay dos nombres para la misma, y el renglón que imprime la original al final lo delata.

---

## Semana 13 · Tema 6 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Solución**

```text
4
Rugosidad arriba de Ra 1.6
None
Codigo no catalogado
3
['D02', 'D03']
['D01']
['D01', 'D05']
```

La última línea lanza `KeyError` sobre la llave `D09`.

El diccionario termina con cuatro entradas porque `defectos["D02"] = ...` no agrega nada: la llave ya existía y se sobreescribió su valor. `defectos["D04"] = ...` sí agrega una entrada nueva. Tres más una son cuatro.

`turno_a` tiene tres elementos porque un conjunto no guarda repetidos: el `D01` que aparece dos veces cuenta una sola. Esa es la diferencia con la lista de la que salió.

**Salida**

```text
4
Rugosidad arriba de Ra 1.6
None
Codigo no catalogado
3
['D02', 'D03']
['D01']
['D01', 'D05']
Traceback (most recent call last):
  File "w13_1.py", line 20, in <module>
    print(defectos["D09"])
          ~~~~~~~~^^^^^^^
KeyError: 'D09'
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho líneas correctas | 4 |
| El `KeyError` de la última línea, nombrado | 2 |
| Explica por qué el diccionario queda en cuatro entradas | 2 |
| Explica por qué el conjunto queda en tres elementos | 2 |

**Error que más se ve**

Contestar 5 en la primera línea: se cuentan las dos asignaciones como dos entradas nuevas, sin notar que D02 ya estaba y que una llave no se repite.

### 13.2 · Aplicar

**Solución**

```python
defectos = {"D01": "Diametro fuera de tolerancia",
            "D02": "Rugosidad arriba de Ra 1.6",
            "D03": "Rebaba en el chaflan",
            "D04": "Golpe en la cara frontal",
            "D05": "Concentricidad fuera de norma",
            "D06": "Marca de herramienta"}

reportados = ["D01", "D03", "D01", "D05", "D01", "D02", "D03", "D09"]

print("Catalogo de defectos")
for codigo, descripcion in defectos.items():
    print(f"  {codigo}  {descripcion}")

print(f"Codigos catalogados: {len(defectos)}")
print(f"Piezas reportadas:   {len(reportados)}")
print(f"Codigos distintos:   {len(set(reportados))}")

for codigo in sorted(set(reportados)):
    print(f"  {codigo}  {defectos.get(codigo, 'Codigo no catalogado')}")
```

El D09 no está en el catálogo, y con corchetes el programa se habría detenido ahí. Con `get` y su valor por omisión, el reporte sale completo y además deja ver que alguien está capturando un código que no existe, que es información útil para el área.

**Salida**

```text
Catalogo de defectos
  D01  Diametro fuera de tolerancia
  D02  Rugosidad arriba de Ra 1.6
  D03  Rebaba en el chaflan
  D04  Golpe en la cara frontal
  D05  Concentricidad fuera de norma
  D06  Marca de herramienta
Codigos catalogados: 6
Piezas reportadas:   8
Codigos distintos:   5
  D01  Diametro fuera de tolerancia
  D02  Rugosidad arriba de Ra 1.6
  D03  Rebaba en el chaflan
  D05  Concentricidad fuera de norma
  D09  Codigo no catalogado
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El catálogo se recorre con `items` y sale completo | 2 |
| Las tres cifras son correctas | 3 |
| La consulta usa `get` con valor por omisión | 3 |
| El D09 aparece en el reporte sin detener el programa | 2 |

**Error que más se ve**

Contar los códigos distintos con `len(reportados)`: da 8 en lugar de 5, y confunde cuántas piezas se reportaron con cuántos tipos de defecto hay.

### 13.3 · Integrar

**Solución**

```python
estaciones = ["EST-01", "EST-02", "EST-03", "EST-04"]
consumo = [86.4, 61.5, 112.8, 48.2]
piezas = [1240, 984, 1512, 760]

reportados_a = ["D01", "D03", "D01", "D05", "D01", "D02", "D03"]
reportados_b = ["D02", "D02", "D06", "D03", "D01"]

consumo_por_estacion = {}
for i in range(len(estaciones)):
    consumo_por_estacion[estaciones[i]] = consumo[i]

conteo = {}
for codigo in reportados_a:
    conteo[codigo] = conteo.get(codigo, 0) + 1

print("Consumo por estacion")
for estacion, kwh in consumo_por_estacion.items():
    print(f"  {estacion}  {kwh:>6.1f} kWh")

print(f"Total de la celda: {sum(consumo_por_estacion.values()):.1f} kWh")

estacion_mas_cara = ""
mayor = 0.0
for estacion, kwh in consumo_por_estacion.items():
    if kwh > mayor:
        mayor = kwh
        estacion_mas_cara = estacion

print(f"Estacion mas cara: {estacion_mas_cara} con {mayor:.1f} kWh")

print("Defectos del turno A")
for codigo in sorted(conteo):
    print(f"  {codigo}  {conteo[codigo]}")

codigos_a = set(reportados_a)
codigos_b = set(reportados_b)

print(f"En los dos turnos:      {sorted(codigos_a & codigos_b)}")
print(f"Solo en el turno A:     {sorted(codigos_a - codigos_b)}")
print(f"Nuevos en el turno B:   {sorted(codigos_b - codigos_a)}")
print(f"En uno pero no en ambos: {sorted(codigos_a ^ codigos_b)}")
```

El código nuevo del turno B es el D06, marca de herramienta, y ese es el que dispara una acción de mantenimiento: una marca de herramienta que no aparecía en el turno anterior apunta a un inserto desgastado o mal montado, y se revisa antes de seguir produciendo.

El conteo del turno A no se podía hacer con un conjunto porque un conjunto elimina los repetidos, y lo que se quería saber era justamente cuántas veces se repitió cada código. El conjunto contesta cuáles hay, el diccionario contesta cuántos de cada uno.

**Salida**

```text
Consumo por estacion
  EST-01    86.4 kWh
  EST-02    61.5 kWh
  EST-03   112.8 kWh
  EST-04    48.2 kWh
Total de la celda: 308.9 kWh
Estacion mas cara: EST-03 con 112.8 kWh
Defectos del turno A
  D01  3
  D02  1
  D03  2
  D05  1
En los dos turnos:      ['D01', 'D02', 'D03']
Solo en el turno A:     ['D05']
Nuevos en el turno B:   ['D06']
En uno pero no en ambos: ['D05', 'D06']
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El diccionario se construye con un ciclo desde las listas | 2 |
| El total sale de `values` y la estación más cara de un recorrido | 2 |
| El contador usa `get` con valor por omisión de cero | 2 |
| Las cuatro comparaciones usan operaciones de conjuntos | 2 |
| Las dos conclusiones escritas | 2 |

**Error que más se ve**

Comparar los dos turnos con un ciclo y un `if` en lugar de operaciones de conjuntos: el resultado sale igual, ocupa quince líneas y falla en cuanto hay que contestar la cuarta pregunta, la de los que están en uno pero no en ambos.

---

## Semana 14 · Tema 7 · Archivos de texto y CSV

### 14.1 · Reconocer

**Solución**

```text
30
EST-01 12.01
<class 'str'>
12.0111.98
True
False
```

La cuarta línea no lanza error porque los dos valores son texto, y el `+` entre dos textos los pega. El resultado, `12.0111.98`, no es un número y aun así el programa sigue corriendo. Ese es el error de conversión más caro del semestre: no avisa.

La sexta línea da falso porque el tercer renglón del archivo trae la estación escrita como `" EST-01"`, con un espacio al frente. Dos textos que se ven iguales en pantalla y difieren en un carácter son valores distintos, y por eso una agrupación por estación reportaría nueve estaciones donde hay cuatro.

Si esa misma apertura llevara `"w"`, el archivo se vaciaría en el instante de abrirlo, antes de leer nada. Los treinta renglones se perderían y después el programa fallaría al intentar leer un archivo abierto para escritura.

**Salida**

```text
30
EST-01 12.01
<class 'str'>
12.0111.98
True
False
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis líneas correctas | 4 |
| Explica por qué la suma de textos no lanza error | 2 |
| Detecta el espacio al frente en el tercer renglón | 2 |
| Explica qué le pasa al archivo con el modo `"w"` | 2 |

**Error que más se ve**

Contestar `23.99` en la cuarta línea: se suman los dos diámetros como si `DictReader` hubiera convertido los tipos, cuando un CSV solo guarda texto y nadie más va a convertirlo por ti.

### 14.2 · Aplicar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent


def a_decimal(texto):
    """Convierte a decimal quitando la coma de miles y la unidad kJ."""
    limpio = texto.replace(",", "").replace("kJ", "")
    return float(limpio.strip())


def a_entero(texto):
    """Convierte a entero. La celda vacia se reporta como ausencia con None."""
    texto = texto.strip()
    return int(texto) if texto else None


def normalizar(texto):
    """Deja una sola forma de escribir la estacion: sin espacios y en mayusculas."""
    return texto.strip().upper()


with (DATOS / "mediciones.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

formas = set()
sin_ciclo = 0

for fila in filas:
    formas.add(fila["estacion"])
    if a_entero(fila["ciclo_s"]) is None:
        sin_ciclo += 1

normalizadas = set()
for fila in filas:
    normalizadas.add(normalizar(fila["estacion"]))

print(f"Renglones leidos:            {len(filas)}")
print(f"Renglones sin tiempo de ciclo: {sin_ciclo}")
print(f"Formas de escribir la estacion: {len(formas)}")
print(f"Estaciones despues de normalizar: {len(normalizadas)}")

energia = {}
medidas = {}
suma_diametro = {}

for fila in filas:
    estacion = normalizar(fila["estacion"])
    energia[estacion] = energia.get(estacion, 0.0) + a_decimal(fila["energia_kj"])
    medidas[estacion] = medidas.get(estacion, 0) + 1
    suma_diametro[estacion] = suma_diametro.get(estacion, 0.0) + float(fila["diametro_mm"])

print(f"{'Estacion':<10}{'Piezas':>8}{'Energia kJ':>13}{'Diametro':>11}")

energia_total = 0.0
medidas_total = 0

for estacion in sorted(energia):
    promedio = suma_diametro[estacion] / medidas[estacion]
    energia_total += energia[estacion]
    medidas_total += medidas[estacion]
    print(f"{estacion:<10}{medidas[estacion]:>8}{energia[estacion]:>13,.0f}{promedio:>11.4f}")

print(f"{'CELDA C-3':<10}{medidas_total:>8}{energia_total:>13,.0f}")
```

`a_entero` devuelve `None` y no cero, porque un tiempo de ciclo que no se capturó no es un ciclo de cero segundos. La decisión de qué hacer con esa ausencia se toma en el ejercicio siguiente, no aquí.

Los diccionarios con `get` y un valor por omisión son la semana 13 aplicada: cada estación aparece por primera vez sin que el programa tenga que saber de antemano cuántas hay.

**Salida**

```text
Renglones leidos:            30
Renglones sin tiempo de ciclo: 3
Formas de escribir la estacion: 9
Estaciones despues de normalizar: 4
Estacion    Piezas   Energia kJ   Diametro
EST-01           9       11,325    12.0022
EST-02           7        7,060    12.0071
EST-03           8       12,125    12.0100
EST-04           6        4,467    12.0083
CELDA C-3       30       34,977
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres funciones con docstring y responsabilidad única | 3 |
| Los cuatro renglones de diagnóstico correctos | 2 |
| La tabla por estación y el total de la celda correctos | 3 |
| La ruta se arma con `pathlib` desde la ubicación del archivo | 1 |
| Lee por nombre de columna, no por posición | 1 |

**Error que más se ve**

Convertir la energía con `float(fila["energia_kj"])` directo: lanza `ValueError` en el primer renglón por la coma y la unidad, y el alumno suele culpar al archivo en lugar de al formato.

### 14.3 · Integrar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05


def a_decimal(texto):
    """Convierte a decimal quitando la coma de miles y la unidad kJ."""
    limpio = texto.replace(",", "").replace("kJ", "")
    return float(limpio.strip())


def normalizar(texto):
    """Deja una sola forma de escribir la estacion: sin espacios y en mayusculas."""
    return texto.strip().upper()


def fuera_de_tolerancia(diametro):
    """Dice si la medicion cae fuera de la banda de 11.95 a 12.05 mm."""
    return diametro < LIMITE_INFERIOR or diametro > LIMITE_SUPERIOR


with (DATOS / "mediciones.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

vistos = set()
limpias = []

for fila in filas:
    huella = (fila["fecha"], fila["estacion"], fila["lote"],
              fila["diametro_mm"], fila["ciclo_s"], fila["energia_kj"])

    if huella in vistos:
        continue

    vistos.add(huella)
    limpias.append(fila)

energia = {}
medidas = {}
fuera = {}
sin_ciclo = 0

for fila in limpias:
    estacion = normalizar(fila["estacion"])
    diametro = float(fila["diametro_mm"])

    energia[estacion] = energia.get(estacion, 0.0) + a_decimal(fila["energia_kj"])
    medidas[estacion] = medidas.get(estacion, 0) + 1
    fuera[estacion] = fuera.get(estacion, 0)

    if fuera_de_tolerancia(diametro):
        fuera[estacion] += 1

    if fila["ciclo_s"].strip() == "":
        sin_ciclo += 1

print(f"Renglones en el archivo:     {len(filas)}")
print(f"Duplicados exactos quitados: {len(filas) - len(limpias)}")
print(f"Renglones que quedaron:      {len(limpias)}")
print(f"Renglones sin tiempo de ciclo conservados: {sin_ciclo}")
print(f"Piezas fuera de tolerancia:  {sum(fuera.values())}")
print(f"Energia de la celda:         {sum(energia.values()):,.0f} kJ")

salida = DATOS / "resumen_estacion.csv"

with salida.open("w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["estacion", "piezas", "fuera_tolerancia", "energia_kj"])

    for estacion in sorted(energia):
        escritor.writerow([estacion, medidas[estacion], fuera[estacion],
                           round(energia[estacion], 1)])

print(f"Archivo escrito: {salida.name}")

with salida.open(encoding="utf-8") as f:
    print(f.read().strip())
```

La huella del renglón es una tupla con las seis columnas, y el conjunto de huellas es lo que detecta el duplicado exacto. Comparar solo por fecha y estación habría borrado mediciones legítimas de piezas distintas del mismo turno.

Los 2,515 kJ de diferencia son la suma de los dos renglones duplicados: 1,260 del renglón de EST-01 del 9 de enero y 1,255 del de EST-01 del 12 de enero. Un duplicado infla el total porque la energía se suma dos veces, y casi no mueve el diámetro promedio porque ahí el valor repetido entra en el numerador y en el denominador a la vez.

**Salida**

```text
Renglones en el archivo:     30
Duplicados exactos quitados: 2
Renglones que quedaron:      28
Renglones sin tiempo de ciclo conservados: 3
Piezas fuera de tolerancia:  8
Energia de la celda:         32,462 kJ
Archivo escrito: resumen_estacion.csv
estacion,piezas,fuera_tolerancia,energia_kj
EST-01,7,3,8810.0
EST-02,7,1,7060.0
EST-03,8,4,12125.0
EST-04,6,0,4467.0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los duplicados se detectan comparando el renglón completo | 2 |
| Las seis cifras de bitácora correctas | 3 |
| El archivo de salida tiene el encabezado y los cuatro renglones pedidos | 2 |
| Se escribe con `newline` vacío y sin renglones en blanco | 1 |
| Explica la diferencia exacta de 2,515 kJ | 2 |

**Error que más se ve**

Detectar duplicados solo por fecha y estación: se borran mediciones de piezas distintas, el conteo baja de 28 a 18 y el total de energía queda muy por debajo sin que nada lo señale.

---

## Semana 15 · Tema 8.1 · Series, DataFrame, limpieza y agrupación

### 15.1 · Reconocer

**Solución**

`shape` da `(30, 6)`. Los tipos: `fecha`, `estacion`, `lote` y `energia_kj` salen texto, `diametro_mm` y `ciclo_s` salen `float64`. Hay 3 valores faltantes en `ciclo_s`, 2 renglones duplicados y 9 formas distintas de escribir la estación.

`ciclo_s` salió decimal y no entero porque tres celdas están vacías, y el marcador de ausencia solo existe en una columna decimal. No es una falla de pandas: es el precio de que la columna tenga huecos, y por eso los tiempos se imprimen como 44.0 en lugar de 44.

`energia_kj` salió texto porque la coma de miles y la unidad son formato, no valor. Mientras estén ahí, esa columna no puede sumarse.

En `value_counts` hay dos renglones que se ven idénticos, `EST-01` y `EST-01 `, y son entradas distintas porque uno trae un espacio al final. Ese espacio no se ve en pantalla y sí parte los grupos.

`describe` solo resume `diametro_mm` y `ciclo_s`, que son las dos columnas numéricas. Las otras cuatro son texto para pandas, incluida la fecha, y por eso quedan fuera.

**Salida**

```text
(30, 6)
fecha              str
estacion           str
lote               str
diametro_mm    float64
ciclo_s        float64
energia_kj         str
dtype: object
3
2
9
estacion
EST-03     7
EST-01     6
EST-02     6
EST-04     6
 EST-01    1
est-01     1
EST-01     1
est-02     1
EST-03     1
Name: count, dtype: int64
count    30.000
mean     12.007
std       0.046
min      11.910
25%      11.972
50%      12.010
75%      12.040
max      12.090
Name: diametro_mm, dtype: float64
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete salidas correctas, con los tipos de las seis columnas | 3 |
| Explica el `float64` de `ciclo_s` por los faltantes | 2 |
| Explica el texto de `energia_kj` por la coma y la unidad | 2 |
| Detecta los dos renglones que se ven iguales en `value_counts` | 2 |
| Dice qué columnas resume `describe` y por qué | 1 |

**Error que más se ve**

Decir que `ciclo_s` salió decimal porque los tiempos traen decimales: en el archivo todos son enteros, y quien no revisa `isna` nunca se entera de que la causa son las tres celdas vacías.

### 15.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05

mediciones = pd.read_csv(DATOS / "mediciones.csv")

print(f"Al cargar:                {len(mediciones)} renglones")
print(f"Duplicados exactos:       {mediciones.duplicated().sum()}")
print(f"Formas de la estacion:    {mediciones['estacion'].nunique()}")
print(f"Sin tiempo de ciclo:      {mediciones['ciclo_s'].isna().sum()}")

mediciones = mediciones.drop_duplicates()
print(f"Sin duplicados:           {len(mediciones)} renglones")

mediciones["estacion"] = mediciones["estacion"].str.strip().str.upper()
print(f"Estaciones reales:        {mediciones['estacion'].nunique()}")

mediciones["energia_kj"] = (mediciones["energia_kj"]
                           .str.replace(",", "", regex=False)
                           .str.replace("kJ", "", regex=False)
                           .str.strip()
                           .astype(float))

mediciones["fecha"] = pd.to_datetime(mediciones["fecha"])

print(mediciones.dtypes)

mediciones["veredicto"] = "Dentro de tolerancia"
mediciones.loc[(mediciones["diametro_mm"] < LIMITE_INFERIOR) |
               (mediciones["diametro_mm"] > LIMITE_SUPERIOR),
               "veredicto"] = "Fuera de tolerancia"

print(mediciones["veredicto"].value_counts())

criticas = mediciones[(mediciones["estacion"] == "EST-03") &
                      (mediciones["veredicto"] == "Fuera de tolerancia")]
print(f"EST-03 fuera de tolerancia: {len(criticas)}")

primeras = mediciones[mediciones["estacion"].isin(["EST-01", "EST-02"])]
print(f"Piezas de EST-01 y EST-02:  {len(primeras)}")

print(f"Energia total:            {mediciones['energia_kj'].sum():,.0f} kJ")
print(f"Ciclo promedio:           {mediciones['ciclo_s'].mean():.2f} s")
print(f"Renglones si se descartan los tres sin ciclo: "
      f"{len(mediciones.dropna(subset=['ciclo_s']))}")
```

Descartar los tres renglones sin tiempo de ciclo dejaría 25 mediciones. Conviene conservarlos porque el dato que decide si la pieza sirve es el diámetro, y ese sí se midió en los tres casos. Tirarlos costaría tres diámetros buenos para no perder tres tiempos de ciclo, y el promedio de ciclo se puede calcular con los 25 que sí lo traen sin necesidad de borrar nada.

**Salida**

```text
Al cargar:                30 renglones
Duplicados exactos:       2
Formas de la estacion:    9
Sin tiempo de ciclo:      3
Sin duplicados:           28 renglones
Estaciones reales:        4
fecha          datetime64[us]
estacion                  str
lote                      str
diametro_mm           float64
ciclo_s               float64
energia_kj            float64
dtype: object
veredicto
Dentro de tolerancia    20
Fuera de tolerancia      8
Name: count, dtype: int64
EST-03 fuera de tolerancia: 4
Piezas de EST-01 y EST-02:  14
Energia total:            32,462 kJ
Ciclo promedio:           44.36 s
Renglones si se descartan los tres sin ciclo: 25
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis cifras de la bitácora correctas | 3 |
| Las cuatro reparaciones aplicadas en orden y los tipos finales correctos | 2 |
| La columna `veredicto` se escribe con `loc` en un solo paso | 2 |
| Los tres filtros dan 4, 14 y los totales correctos | 2 |
| Justifica por escrito la decisión sobre los renglones sin ciclo | 1 |

**Error que más se ve**

Escribir la columna con `mediciones[mediciones[...]]["veredicto"] = ...`: la asignación encadenada no hace nada, la columna queda completa en «Dentro de tolerancia» y el conteo sale 28 y 0 sin que se lance ningún error.

### 15.3 · Integrar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05


def cargar_limpio():
    """Carga mediciones.csv y le aplica las cuatro reparaciones de la sesion 15.2."""
    datos = pd.read_csv(DATOS / "mediciones.csv").drop_duplicates()

    datos["estacion"] = datos["estacion"].str.strip().str.upper()
    datos["energia_kj"] = (datos["energia_kj"]
                          .str.replace(",", "", regex=False)
                          .str.replace("kJ", "", regex=False)
                          .str.strip()
                          .astype(float))
    datos["fecha"] = pd.to_datetime(datos["fecha"])

    datos["veredicto"] = "Dentro de tolerancia"
    datos.loc[(datos["diametro_mm"] < LIMITE_INFERIOR) |
              (datos["diametro_mm"] > LIMITE_SUPERIOR),
              "veredicto"] = "Fuera de tolerancia"

    return datos


mediciones = cargar_limpio()

tablero = mediciones.groupby("estacion").agg(
    piezas=("diametro_mm", "count"),
    energia=("energia_kj", "sum"),
    ciclo=("ciclo_s", "mean"),
    diametro=("diametro_mm", "mean"),
).round(3)

print(tablero.sort_values("energia", ascending=False))

fuera = mediciones[mediciones["veredicto"] == "Fuera de tolerancia"]
print(fuera.groupby("estacion").size())

rejilla = mediciones.pivot_table(index="estacion", columns="lote",
                                 values="energia_kj", aggfunc="sum",
                                 fill_value=0, margins=True)
print(rejilla.round(0))

catalogo = pd.DataFrame({
    "estacion": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "maquina": ["Torno CNC", "Fresadora CNC", "Rectificadora",
                "Banco de pruebas", "Taladro radial"],
    "ciclo_meta_s": [42, 40, 48, 36, 30],
})

auditoria = mediciones.merge(catalogo, on="estacion", how="outer", indicator=True)
print(auditoria["_merge"].value_counts())

unida = tablero.reset_index().merge(catalogo, on="estacion", how="left")
unida["desvio_ciclo"] = (unida["ciclo"] / unida["ciclo_meta_s"] - 1)

print(unida[["estacion", "maquina", "piezas", "ciclo",
             "ciclo_meta_s", "desvio_ciclo"]].round(3))
```

La tabla de piezas fuera de tolerancia trae tres renglones y no cuatro porque EST-04 no aportó ninguna. `groupby` solo devuelve los grupos que existen en los datos que recibió, y una estación sin piezas fuera simplemente no aparece. Si esa tabla se va a usar en una resta o en una división, hay que rellenar el cero a propósito.

La auditoría de la unión: 28 renglones cruzaron en ambos lados, 1 quedó solo del catálogo y 0 solo de las mediciones. El del catálogo es EST-05, el taladro radial, que existe en la planta y no produjo bujes esta semana: eso está bien y se explica solo. Los cero del otro lado son la cifra importante: ninguna medición quedó huérfana, o sea que el archivo no trae ninguna estación desconocida. Si ese número no fuera cero, habría que reportarlo antes de publicar cualquier total.

EST-01 corre 6.7 % arriba de su ciclo meta y EST-03 6.2 %, mientras EST-02 apenas 1.2 %. A mantenimiento se le reporta que dos de las cuatro estaciones están perdiendo alrededor de tres segundos por pieza contra el estándar, y que en EST-03 esos tres segundos se acumulan sobre el ciclo más largo de la celda.

**Salida**

```text
          piezas  energia   ciclo  diametro
estacion                                   
EST-03         8  12125.0  51.000    12.010
EST-01         7   8810.0  44.833    11.999
EST-02         7   7060.0  40.500    12.007
EST-04         6   4467.0  37.800    12.008
estacion
EST-01    3
EST-02    1
EST-03    4
dtype: int64
lote       L-2601   L-2602  L-2603      All
estacion                                   
EST-01     3740.0   2485.0  2585.0   8810.0
EST-02     1990.0   2055.0  3015.0   7060.0
EST-03     4690.0   4540.0  2895.0  12125.0
EST-04     1490.0   1500.0  1477.0   4467.0
All       11910.0  10580.0  9972.0  32462.0
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
  estacion           maquina  piezas   ciclo  ciclo_meta_s  desvio_ciclo
0   EST-01         Torno CNC       7  44.833            42         0.067
1   EST-02     Fresadora CNC       7  40.500            40         0.012
2   EST-03     Rectificadora       8  51.000            48         0.062
3   EST-04  Banco de pruebas       6  37.800            36         0.050
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La limpieza queda encerrada en una función con docstring | 1 |
| El tablero de cuatro resúmenes sale en una sola instrucción | 2 |
| Explica por qué la tabla de fuera de tolerancia trae tres renglones | 2 |
| La rejilla con totales de fila y columna es correcta | 2 |
| La unión se audita en las dos direcciones y se interpretan los tres números | 2 |
| El tablero de desvío de ciclo es correcto y se reporta | 1 |

**Error que más se ve**

Unir con `inner` en lugar de `left` para el tablero: con estos datos el resultado no cambia, y por eso el alumno se acostumbra a un modo que en cuanto falte una estación en el catálogo va a borrar renglones en silencio.

---

## Semana 16 · Tema 8.2 · Visualización con matplotlib y seaborn

### 16.1 · Reconocer

**Solución**

La barra muestra el promedio de energía por pieza, porque `barplot` promedia cuando no se le dice otra cosa. Para EST-01 la barra vale 1,258.6 kJ. Lo que dice el asunto del correo, la energía del turno, son 8,810 kJ, siete veces más. Los dos números son correctos y contestan preguntas distintas: uno es cuánto gastó cada pieza en promedio, el otro cuánto gastó la estación.

Para que la barra muestre el total hay que agregar `estimator="sum"`, y con eso conviene agregar `errorbar=None`, porque el intervalo que dibuja encima de cada barra no significa nada en un reporte de consumo.

Las cuatro gráficas:

- Energía de las cuatro estaciones: barras, porque compara categorías que no tienen orden natural. Ordenadas de mayor a menor, el ranking se lee solo.
- Reparto de los diámetros dentro de cada estación: caja y bigotes, porque la pregunta no es el centro sino la forma, y ahí es donde se ve la dispersión que el promedio esconde.
- Diámetro promedio a lo largo de los tres días: línea, porque el eje horizontal es tiempo y conectar dos fechas sí afirma algo cierto.
- Ciclo contra desviación de medida: dispersión, porque pregunta si dos variables numéricas se mueven juntas.

**Salida**

```text
              sum    mean  count
estacion
EST-03    12125.0  1515.6      8
EST-01     8810.0  1258.6      7
EST-02     7060.0  1008.6      7
EST-04     4467.0   744.5      6
             mean     std    min    max
estacion
EST-04    12.0083  0.0343  11.96  12.05
EST-02    12.0071  0.0435  11.95  12.07
EST-01    11.9986  0.0488  11.93  12.06
EST-03    12.0100  0.0646  11.91  12.09
estacion
EST-01    3
EST-02    1
EST-03    4
dtype: int64
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Identifica que la barra muestra el promedio y da las dos cifras de EST-01 | 3 |
| Nombra `estimator` y `errorbar` como la corrección | 2 |
| Las tres tablas se imprimen correctas | 2 |
| Las cuatro gráficas elegidas y justificadas | 3 |

**Error que más se ve**

Contestar que la barra muestra el total porque el eje llega a miles: las cuatro barras se ven plausibles en esa escala, y sin correr la tabla de suma y promedio no hay forma de notar el factor de siete.

### 16.2 · Aplicar

**Solución**

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from pathlib import Path

from limpieza import cargar_limpio

SALIDA = Path(__file__).resolve().parent

mediciones = cargar_limpio()

energia = (mediciones.groupby("estacion")["energia_kj"]
           .sum()
           .sort_values(ascending=False))

print(energia)

pico = energia.index[0]
parte = energia.iloc[0] / energia.sum()

print(f"{pico} concentra {parte:.1%} de la energia de la celda")

fig, ax = plt.subplots(figsize=(9, 5))

barras = ax.bar(energia.index, energia.values, color="#C7D6E8")
barras[0].set_color("#2B5F8F")

ax.set_title(f"{pico} concentra el {parte:.0%} de la energia de la celda C-3")
ax.set_ylabel("Energia del turno (kJ)")
ax.set_ylim(0, 13000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1000:.0f}k"))

fig.text(0.01, 0.01, "Fuente: mediciones.csv, celda C-3, 8 al 12 de enero de 2026",
         fontsize=8)

fig.savefig(SALIDA / "energia_estacion.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Archivo generado:", (SALIDA / "energia_estacion.png").exists())
```

La función `cargar_limpio` es la de 15.3, guardada en un archivo `limpieza.py` al lado de los programas de esta semana, para no volver a copiar la limpieza en cada gráfica.

Texto alternativo: gráfica de barras de la energía consumida por las cuatro estaciones de la celda C-3 entre el 8 y el 12 de enero de 2026. EST-03 encabeza con 12,125 kJ, seguida de EST-01 con 8,810, EST-02 con 7,060 y EST-04 con 4,467. EST-03 sola representa el 37 % de los 32,462 kJ de la celda y gasta 2.7 veces lo de EST-04.

**Salida**

```text
estacion
EST-03    12125.0
EST-01     8810.0
EST-02     7060.0
EST-04     4467.0
Name: energia_kj, dtype: float64
EST-03 concentra 37.4% de la energia de la celda
Archivo generado: True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La serie por estación es correcta y está ordenada | 2 |
| El título dice el hallazgo y el porcentaje se calcula en el programa | 2 |
| Eje etiquetado, base en cero y formato en miles | 2 |
| La barra pico resaltada y la fuente al pie | 2 |
| El texto alternativo trae cifras verificables contra la serie | 2 |

**Error que más se ve**

Escribir el 37 % a mano en el título: funciona hasta que llega el archivo del mes siguiente, y entonces la gráfica afirma un porcentaje que sus propias barras ya no sostienen.

### 16.3 · Integrar

**Solución**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

from limpieza import cargar_limpio

SALIDA = Path(__file__).resolve().parent

sns.set_theme(style="whitegrid", palette="deep")

mediciones = cargar_limpio()

resumen = mediciones.groupby("estacion")["diametro_mm"].agg(
    ["mean", "median", "std", "count"]).round(4)
print(resumen.sort_values("std"))

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=mediciones, x="estacion", y="energia_kj", estimator="sum",
            errorbar=None, hue="estacion", legend=False, ax=ax)
ax.set_title("EST-03 gasta 2.7 veces la energia de EST-04 en el mismo turno")
ax.set_ylabel("Energia del turno (kJ)")
fig.savefig(SALIDA / "barras_energia.png", dpi=150, bbox_inches="tight")
plt.close(fig)

orden = (mediciones.groupby("estacion")["diametro_mm"]
         .std().sort_values().index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=mediciones, x="estacion", y="diametro_mm", order=orden,
            hue="estacion", legend=False, ax=ax)
ax.axhline(11.95, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(12.05, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("EST-01 esta centrada en el nominal y aun asi se sale de la banda")
ax.set_ylabel("Diametro medido (mm)")
fig.savefig(SALIDA / "caja_estacion.png", dpi=150, bbox_inches="tight")
plt.close(fig)

rejilla = mediciones.pivot_table(index="estacion", columns="lote",
                                 values="energia_kj", aggfunc="sum",
                                 fill_value=0) / 1000
print(rejilla.round(2))

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(rejilla, annot=True, fmt=".1f", cmap="Blues", ax=ax)
ax.set_title("El lote L-2601 de EST-03 es la celda mas cara del tablero")
fig.savefig(SALIDA / "mapa_estacion_lote.png", dpi=150, bbox_inches="tight")
plt.close(fig)

for nombre in ["barras_energia.png", "caja_estacion.png", "mapa_estacion_lote.png"]:
    print(nombre, (SALIDA / nombre).exists())
```

La conclusión de las tres juntas: EST-03 es la estación cara y la imprecisa a la vez, con 12,125 kJ, la dispersión más alta con 0.0646 mm y 4 de las 8 piezas fuera de banda. EST-01 tiene el promedio más cercano al nominal, 11.9986 mm, y aun así 3 piezas fuera, porque su dispersión es la segunda más alta con 0.0488 mm. EST-04 es la que hay que copiar: 0.0343 mm de dispersión, ninguna pieza fuera y la menor energía.

A mantenimiento se manda la caja y bigotes. Las barras dicen cuánto se gasta y el mapa dice dónde, pero la caja es la única que muestra que un promedio centrado no significa un proceso capaz, que es justo lo que hay que corregir en EST-01.

**Salida**

```text
             mean  median     std  count
estacion
EST-04    12.0083  12.015  0.0343      6
EST-02    12.0071  12.010  0.0435      7
EST-01    11.9986  12.010  0.0488      7
EST-03    12.0100  12.010  0.0646      8
lote      L-2601  L-2602  L-2603
estacion
EST-01      3.74    2.48    2.58
EST-02      1.99    2.06    3.02
EST-03      4.69    4.54    2.90
EST-04      1.49    1.50    1.48
barras_energia.png True
caja_estacion.png True
mapa_estacion_lote.png True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El tema se configura una vez y las tres imágenes se generan | 2 |
| La barra usa `estimator` y quita la barra de error | 2 |
| La caja va ordenada por dispersión y trae las dos líneas de la banda | 2 |
| El mapa de calor sale de la rejilla, en miles y con valores escritos | 1 |
| Los tres títulos dicen un hallazgo verificable | 1 |
| La conclusión trae al menos tres cifras y elige una gráfica | 2 |

**Error que más se ve**

Dejar la caja y bigotes ordenada alfabéticamente: el ranking de dispersión, que es todo el contenido de esa gráfica, se queda escondido y hay que leerlo caja por caja.

---

## Semana 17 · Repaso y examen final

### 17.1 · Reconocer

**Solución**

```text
9
False
None
48.2
1,240 kJ980 kJ
11.98
```

Línea 1, agrupar antes de limpiar. Salen 9 estaciones donde hay 4, porque los espacios y las minúsculas todavía parten los grupos. El resultado correcto es 4.

Línea 2, asignación encadenada. La columna nunca se creó. Desde pandas 3.0 la operación no hace nada y no lanza error, solo una advertencia que es fácil pasar por alto. Lo correcto es `mediciones.loc[condicion, "veredicto"] = "Revisar"`.

Línea 3, confundir modificar con devolver. `sort` ordena la lista y devuelve `None`, así que la asignación borró los datos. Lo correcto es `sorted(diametros)` o llamar a `diametros.sort()` sin asignar.

Línea 4, acumulador declarado adentro. Sale 48.2, que es el último consumo. El total correcto es 308.9.

Línea 5, calcular sin convertir. Los dos valores son texto y el `+` los pega. El resultado correcto, después de convertir, es 2,220 kJ.

Línea 6, contar desde uno. `mediciones["diametro_mm"][1]` devuelve 11.98, que es el segundo renglón del archivo. La pregunta era por el primero, que mide 12.01 y está en el índice 0.

El programa no se detiene en ninguna de las seis porque las seis son operaciones válidas de Python sobre datos válidos. Ninguna es un error de sintaxis ni de tipo: son respuestas correctas a preguntas que nadie hizo.

**Salida**

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
  mediciones[mediciones["estacion"] == "EST-03"]["veredicto"] = "Revisar"
9
False
None
48.2
1,240 kJ980 kJ
11.98
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis líneas correctas | 3 |
| Los seis errores nombrados | 3 |
| El resultado correcto de cada uno | 2 |
| Explica por qué el programa no se detuvo | 1 |
| Identifica la pregunta real de la última línea | 1 |

**Error que más se ve**

Contestar 4 en la primera línea porque en la celda hay cuatro estaciones: se contesta con lo que se sabe de la planta en lugar de con lo que trae el archivo, y ese es el mismo reflejo que hace que nadie revise un total sucio.

### 17.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05

mediciones = pd.read_csv(DATOS / "mediciones.csv")

print(f"Renglones:             {len(mediciones)}")
print(f"Duplicados:            {mediciones.duplicated().sum()}")
print(f"Formas de la estacion: {mediciones['estacion'].nunique()}")
print(f"Sin tiempo de ciclo:   {mediciones['ciclo_s'].isna().sum()}")

mediciones = mediciones.drop_duplicates()
mediciones["estacion"] = mediciones["estacion"].str.strip().str.upper()
mediciones["energia_kj"] = (mediciones["energia_kj"]
                           .str.replace(",", "", regex=False)
                           .str.replace("kJ", "", regex=False)
                           .str.strip()
                           .astype(float))

mediciones["veredicto"] = "Dentro de tolerancia"
mediciones.loc[(mediciones["diametro_mm"] < LIMITE_INFERIOR) |
               (mediciones["diametro_mm"] > LIMITE_SUPERIOR),
               "veredicto"] = "Fuera de tolerancia"

tablero = mediciones.groupby("estacion").agg(
    piezas=("diametro_mm", "count"),
    energia=("energia_kj", "sum"),
    diametro=("diametro_mm", "mean"),
    dispersion=("diametro_mm", "std"),
)
tablero["fuera"] = (mediciones[mediciones["veredicto"] == "Fuera de tolerancia"]
                    .groupby("estacion").size()
                    .reindex(tablero.index, fill_value=0))
tablero["tasa"] = tablero["fuera"] / tablero["piezas"]

print(tablero.round(4).sort_values("energia", ascending=False))

peor = tablero["tasa"].idxmax()
parte_energia = tablero.loc[peor, "energia"] / tablero["energia"].sum()
parte_fuera = tablero.loc[peor, "fuera"] / tablero["fuera"].sum()

print(f"{peor} consume el {parte_energia:.1%} de la energia de la celda "
      f"y concentra el {parte_fuera:.0%} de las piezas fuera de tolerancia.")
```

El `reindex` con relleno en cero es lo que evita que EST-04 quede vacía en la columna de piezas fuera. Sin él, la tasa de esa estación saldría como dato faltante y la división del final daría un resultado sin sentido. Quien no conozca `reindex` puede llegar al mismo tablero uniendo la cuenta y rellenando con `fillna(0)`, y las dos rutas se califican igual.

**Salida**

```text
Renglones:             30
Duplicados:            2
Formas de la estacion: 9
Sin tiempo de ciclo:   3
          piezas  energia  diametro  dispersion  fuera    tasa
estacion
EST-03         8  12125.0   12.0100      0.0646      4  0.5000
EST-01         7   8810.0   11.9986      0.0488      3  0.4286
EST-02         7   7060.0   12.0071      0.0435      1  0.1429
EST-04         6   4467.0   12.0083      0.0343      0  0.0000
EST-03 consume el 37.4% de la energia de la celda y concentra el 50% de las piezas fuera de tolerancia.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro renglones de inspección antes de tocar nada | 2 |
| La limpieza completa y en el orden correcto | 2 |
| El tablero con las seis columnas correctas | 3 |
| La estación sin piezas fuera aparece con cero y no vacía | 1 |
| La conclusión se arma desde el tablero, con sus dos cifras | 2 |

**Error que más se ve**

Saltarse la inspección y limpiar de una vez: el programa entrega el mismo tablero y el alumno no puede contestar cuántos duplicados quitó, que es la primera pregunta de cualquier revisión.

### 17.3 · Integrar

**Solución**

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 11.95
LIMITE_SUPERIOR = 12.05


def marcar_veredicto(datos):
    """Agrega la columna veredicto segun la banda de 11.95 a 12.05 mm."""
    datos["veredicto"] = "Dentro de tolerancia"
    datos.loc[(datos["diametro_mm"] < LIMITE_INFERIOR) |
              (datos["diametro_mm"] > LIMITE_SUPERIOR),
              "veredicto"] = "Fuera de tolerancia"
    return datos


def cargar_limpio():
    """Carga mediciones.csv, quita duplicados, normaliza y convierte tipos."""
    datos = pd.read_csv(DATOS / "mediciones.csv").drop_duplicates()

    datos["estacion"] = datos["estacion"].str.strip().str.upper()
    datos["energia_kj"] = (datos["energia_kj"]
                          .str.replace(",", "", regex=False)
                          .str.replace("kJ", "", regex=False)
                          .str.strip()
                          .astype(float))
    datos["fecha"] = pd.to_datetime(datos["fecha"])

    return marcar_veredicto(datos)


crudo = marcar_veredicto(pd.read_csv(DATOS / "mediciones.csv"))
limpio = cargar_limpio()

fuera_crudo = (crudo["veredicto"] == "Fuera de tolerancia").sum()
fuera_limpio = (limpio["veredicto"] == "Fuera de tolerancia").sum()

print(f"Sin limpiar: {fuera_crudo} de {len(crudo)} fuera de tolerancia "
      f"({fuera_crudo / len(crudo):.1%})")
print(f"Ya limpio:   {fuera_limpio} de {len(limpio)} fuera de tolerancia "
      f"({fuera_limpio / len(limpio):.1%})")

tablero = limpio.groupby("estacion").agg(
    piezas=("diametro_mm", "count"),
    energia=("energia_kj", "sum"),
    diametro=("diametro_mm", "mean"),
    dispersion=("diametro_mm", "std"),
).round(4)

print(tablero.sort_values("dispersion", ascending=False))

catalogo = pd.DataFrame({
    "estacion": ["EST-01", "EST-02", "EST-03", "EST-04", "EST-05"],
    "maquina": ["Torno CNC", "Fresadora CNC", "Rectificadora",
                "Banco de pruebas", "Taladro radial"],
    "ciclo_meta_s": [42, 40, 48, 36, 30],
})

auditoria = limpio.merge(catalogo, on="estacion", how="outer", indicator=True)
print(auditoria["_merge"].value_counts())

sns.set_theme(style="whitegrid", palette="deep")

orden = tablero.sort_values("dispersion").index

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=limpio, x="estacion", y="diametro_mm", order=orden,
            hue="estacion", legend=False, ax=ax)
ax.axhline(LIMITE_INFERIOR, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(LIMITE_SUPERIOR, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("EST-03 es la unica estacion cuyo cuartil superior rebasa 12.05 mm")
ax.set_ylabel("Diametro medido (mm)")
fig.text(0.01, 0.01, "Fuente: mediciones.csv, celda C-3, enero de 2026", fontsize=8)
fig.savefig(DATOS / "dispersion_estacion.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Grafica generada:", (DATOS / "dispersion_estacion.png").exists())
```

El numerador no cambia porque los dos renglones duplicados son piezas que estaban dentro de tolerancia: 11.99 y 12.04. El denominador sí baja, de 30 a 28, y por eso la tasa sube de 26.7 % a 28.6 %. A calidad se le reporta la del archivo limpio: 8 de 28, porque las mediciones repetidas no son piezas repetidas y contarlas dos veces diluye el problema.

El cuartil superior de EST-03 está en 12.065 mm, arriba del límite de 12.05. Eso significa que más de una cuarta parte de lo que produce esa estación se sale por el lado alto, y no por casos aislados sino por dónde está parada toda su distribución.

A mantenimiento se le pide revisar la rectificadora de EST-03, y se sostiene con dos cifras: dispersión de 0.0646 mm contra 0.0343 de EST-04, y 4 de las 8 piezas fuera de banda de toda la celda. El dato que falta en este archivo para afirmar la causa es cuándo se cambió el inserto o se ajustó la máquina: sin el registro de mantenimiento se puede señalar la estación, no el motivo.

**Salida**

```text
Sin limpiar: 8 de 30 fuera de tolerancia (26.7%)
Ya limpio:   8 de 28 fuera de tolerancia (28.6%)
          piezas  energia  diametro  dispersion
estacion
EST-03         8  12125.0   12.0100      0.0646
EST-01         7   8810.0   11.9986      0.0488
EST-02         7   7060.0   12.0071      0.0435
EST-04         6   4467.0   12.0083      0.0343
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
Grafica generada: True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos funciones con docstring y sin código repetido | 2 |
| Las dos tasas correctas y la explicación del numerador y el denominador | 2 |
| El tablero ordenado por dispersión es correcto | 2 |
| La auditoría de la unión con sus tres conteos | 1 |
| La gráfica lleva orden, banda, título con hallazgo y fuente | 2 |
| El cierre trae las dos cifras y nombra el dato faltante | 1 |

**Error que más se ve**

Reportar la tasa del archivo sin limpiar porque «es la que trae el sistema»: 26.7 % contra 28.6 % parece una diferencia menor, y es exactamente el tipo de dilución que hace que un problema de una estación se vea como ruido de la celda.
