# Soluciones · Análisis y Diseño de Algoritmos · COM101

Documento del profesor. Cada ejercicio trae la solución tal como se corrió, la salida exacta que produjo, la rúbrica de diez puntos y el error que más aparece al calificarlo. Todo el código de Python se ejecutó con el intérprete del curso; las soluciones de la semana 2 son de papel y se revisan contra la traza. Los ejercicios que leen por teclado se muestran con la sesión completa, con lo que el alumno escribe en la misma línea del mensaje.

Los datos son los mismos todo el semestre: el área de originación de Financiera Altamar, sus mesas MC-01 a MC-04, el crédito de nómina con tasa de política de 18.00 % y banda de 17.50 a 18.50 %, y el archivo `solicitudes.csv` de las semanas 14 a 17.

---

## Semana 01 · Encuadre y puente de Excel a Python

### 01.1 · Reconocer

**Solución**

```text
S01 1240
7990
1331.6666666666667
S04
```

`aprobadas[3]` es la semana S04, con 1510 solicitudes. En la hoja de cálculo de donde salió el dato está en la fila 5: la fila 1 son los encabezados, la fila 2 es S01, y de ahí el índice 3 de Python cae dos renglones abajo de lo que la intuición dice.

`print(aprobadas[6])` lanza `IndexError`. La lista tiene seis elementos y el último índice válido es el 5.

**Salida**

```text
S01 1240
7990
1331.6666666666667
S04
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro líneas correctas, incluido el promedio sin redondear | 4 |
| Identifica que `aprobadas[3]` es S04 | 2 |
| Ubica la fila de la hoja contando el encabezado | 2 |
| Explica el `IndexError` nombrando el último índice válido | 2 |

**Error que más se ve**

Contestar `S03 1120` en la primera línea y decir que `aprobadas[3]` es S03: es contar desde uno, y lo delata que todas las respuestas queden corridas exactamente una posición.

### 01.2 · Aplicar

**Solución**

```python
semanas = ["S01", "S02", "S03", "S04", "S05", "S06"]
aprobadas = [1240, 1385, 1120, 1510, 1295, 1440]

total = sum(aprobadas)
promedio = total / len(aprobadas)
mejor_semana = semanas[aprobadas.index(max(aprobadas))]
mejor_valor = max(aprobadas)
sobre_promedio = mejor_valor - promedio

print(f"Solicitudes del bimestre: {total:,}")
print(f"Promedio por semana:      {promedio:,.1f}")
print(f"Mejor semana:             {mejor_semana} con {mejor_valor:,}")
print(f"Arriba del promedio:      {sobre_promedio:,.1f}")
```

**Salida**

```text
Solicitudes del bimestre: 7,990
Promedio por semana:      1,331.7
Mejor semana:             S04 con 1,510
Arriba del promedio:      178.3
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro cifras son correctas | 4 |
| La mejor semana sale de `index` y `max`, no escrita a mano | 3 |
| Separador de miles y un decimal donde corresponde | 2 |
| Las etiquetas permiten leer el reporte sin ver el código | 1 |

**Error que más se ve**

Escribir `mejor_semana = "S04"` porque ya se vio en la salida anterior: el programa da el resultado correcto y deja de darlo en cuanto cambia un dato, que es justo lo que pasa en 01.3.

### 01.3 · Integrar

**Solución**

```python
semanas = ["S01", "S02", "S03", "S04", "S05", "S06"]
aprobadas = [1240, 1385, 1320, 1510, 1295, 1440]

total = sum(aprobadas)
promedio = total / len(aprobadas)
mejor_semana = semanas[aprobadas.index(max(aprobadas))]

folio = "00847"

print(f"Folio del corte:          {folio}")
print(f"Solicitudes del bimestre: {total:,}")
print(f"Promedio por semana:      {promedio:,.1f}")
print(f"Mejor semana:             {mejor_semana}")
```

Antes de la corrección: 7,990 solicitudes, 1,331.7 de promedio, S04. Después: 8,190 solicitudes, 1,365.0 de promedio, S04. La mejor semana no cambia porque S03 sigue por debajo de S04.

En la hoja de cálculo el cambio se habría propagado solo. En Python no se recalcula nada hasta que se vuelve a ejecutar el archivo, y ese es el segundo de los cuatro quiebres. La ventaja aparece al revés: el procedimiento quedó escrito, así que la corrección se puede volver a aplicar dentro de tres meses y dar exactamente lo mismo.

Capturado con formato de número, el folio se ve como 847: los ceros a la izquierda no son parte de un valor numérico y desaparecen. Es el tercero de los cuatro quiebres, el de los tipos. Un folio se guarda como texto porque es un identificador: no se suma, no se promedia, y su forma es lo único que permite volver a encontrarlo en el sistema que lo emitió.

**Salida**

```text
Folio del corte:          00847
Solicitudes del bimestre: 8,190
Promedio por semana:      1,365.0
Mejor semana:             S04
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres cifras nuevas son correctas y se comparan con las anteriores | 3 |
| Nota que la mejor semana no cambia y dice por qué | 2 |
| Nombra el quiebre del recálculo y lo explica | 2 |
| Explica que el folio capturado como número se ve 847 | 2 |
| Explica por qué un folio es texto | 1 |

**Error que más se ve**

Afirmar que la mejor semana ahora es S03 porque fue la que cambió: se razona sobre el dato que se tocó en lugar de sobre el resultado, y basta comparar 1320 con 1510 para verlo.

---

## Semana 02 · Tema 1 · Diseño de algoritmos

### 02.1 · Reconocer

**Solución**

Solicitud de 18.80 %. Se evalúa `18.80 > 18.50`, que se cumple, y el veredicto queda en «Sobreprecio fuera de política». Las otras dos ramas no se leen.

Solicitud de 17.40 %. Se evalúa `17.40 > 18.50`, que falla. Se evalúa `17.40 < 17.50`, que se cumple, y el veredicto queda en «Descuento fuera de política». El `SI NO` final no se lee.

Solicitud de 18.50 % exactos. Se evalúa `18.50 > 18.50`, que falla porque el operador pide estrictamente mayor. Se evalúa `18.50 < 17.50`, que también falla. Cae en el `SI NO` y el veredicto es «Dentro de política». La solicitud está justo en el límite y pasa.

Con la segunda versión, la solicitud de 18.80 % entra por `18.80 >= 17.50`, que se cumple, y sale como «Dentro de política». La rama del sobreprecio es inalcanzable: cualquier tasa mayor a 18.50 también es mayor o igual a 17.50, así que la primera condición se la lleva siempre.

Esa segunda versión es finita, precisa, definida, tiene entrada y tiene salida. Cumple las cinco propiedades y aun así aprueba precios que no cumplen la política. Un algoritmo correcto en su forma puede estar resolviendo el problema equivocado, y por eso el orden de las condiciones se revisa con casos, no con la vista.

**Salida**

```text
Solicitud   Condicion evaluada    Resultado    Veredicto
18.80 %     18.80 > 18.50         Se cumple    Sobreprecio fuera de politica
17.40 %     17.40 > 18.50         Falla        -
17.40 %     17.40 < 17.50         Se cumple    Descuento fuera de politica
18.50 %     18.50 > 18.50         Falla        -
18.50 %     18.50 < 17.50         Falla        Dentro de politica

Segunda version
18.80 %     18.80 >= 17.50        Se cumple    Dentro de politica
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres trazas correctas, con las condiciones que no se leen marcadas | 4 |
| El caso de 18.50 sale dentro de política y explica por qué | 2 |
| Traza la segunda versión y detecta que la rama del sobreprecio es inalcanzable | 2 |
| Argumenta que cumple las cinco propiedades y aun así está mal | 2 |

**Error que más se ve**

Decir que la solicitud de 18.50 se marca fuera porque «llegó al límite»: se confunde el límite con la zona de excepción, y se ve en que el alumno lee `>` como si fuera `>=`.

### 02.2 · Aplicar

**Solución**

```text
INICIO
    LEER expediente_completo, adeudo_vencido, score_buro

    SI expediente_completo = FALSO ENTONCES
        ESCRIBIR "Solicitud en espera: expediente incompleto"
    SI NO SI adeudo_vencido > 0 ENTONCES
        ESCRIBIR "Solicitud en espera: adeudo vencido"
    SI NO SI score_buro < 620 ENTONCES
        ESCRIBIR "Solicitud en espera: score insuficiente"
    SI NO
        ESCRIBIR "Desembolso liberado"

    FIN
```

El diagrama de flujo lleva un óvalo de inicio, un paralelogramo de lectura de los tres datos, tres rombos encadenados por la salida del NO, cuatro paralelogramos de escritura y un óvalo de fin. Cada rombo tiene sus dos salidas etiquetadas.

El orden importa: el expediente se revisa primero porque sin documentos no hay nada que consultar, y una solicitud sin comprobante de ingreso no se desembolsa aunque el score sea excelente.

**Salida**

```text
Caso 1: expediente completo, sin adeudo, score 688
  Rombo 1: expediente_completo = FALSO?   No, sigue
  Rombo 2: adeudo_vencido > 0?            No, sigue
  Rombo 3: 688 < 620?                     No, sigue
  Salida: Desembolso liberado

Caso 2: expediente completo, sin adeudo, score 601
  Rombo 1: expediente_completo = FALSO?   No, sigue
  Rombo 2: adeudo_vencido > 0?            No, sigue
  Rombo 3: 601 < 620?                     Si
  Salida: Solicitud en espera: score insuficiente
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

Un solo rombo con las tres condiciones adentro y un mensaje de «solicitud rechazada»: el algoritmo decide bien y no sirve, porque el ejecutivo no sabe qué pedirle al cliente.

### 02.3 · Integrar

**Solución**

La prueba de las dos personas: dos analistas con la misma solicitud colocada a 18.60 % pueden decidir distinto, porque «salió muy cara» depende de quién la vea. Se rompe la propiedad de ser preciso, y con ella la de ser definido, porque los mismos datos no producen el mismo resultado.

```text
INICIO
    LEER tasa

    SI tasa > 18.50 ENTONCES
        destino = "Comite de precio"
    SI NO SI tasa < 17.50 ENTONCES
        destino = "Cancelar por margen"
    SI NO
        destino = "Desembolsar"

    ESCRIBIR destino
FIN
```

Entrada: la tasa otorgada a una solicitud, en por ciento anual. Salida: el destino de esa solicitud, un texto de tres valores posibles.

Caso límite que la primera versión no cubría: una tasa de 0.00 %, que ocurre cuando el campo se quedó vacío en el sistema y llega como cero. Con el algoritmo de arriba esa solicitud sale como cancelar por margen, y no es cierto: la solicitud no se ha cotizado. Se cubre con una rama al principio que rechace tasas menores o iguales a cero y pida volver a capturar.

**Salida**

```text
Instruccion original     Dos analistas, un mismo 18.60 %, dos destinos
Propiedad rota           Preciso, y con ella la de ser definido

Traza de tres solicitudes
18.60 %   18.60 > 18.50    Se cumple    Comite de precio
17.20 %   17.20 > 18.50    Falla
17.20 %   17.20 < 17.50    Se cumple    Cancelar por margen
18.00 %   las dos fallan                Desembolsar

Caso limite agregado
 0.00 %   tasa <= 0        Se cumple    Volver a capturar
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

Reescribir la instrucción con más palabras pero sin números: «si la tasa quedó muy arriba de la política» sigue dependiendo de quién lea, y se detecta porque no aparece ni un 17.50 ni un 18.50 en toda la hoja.

---

## Semana 03 · Temas 1 y 2 · Paradigmas e introducción a la programación

### 03.1 · Reconocer

**Solución**

La traza: después de la primera línea `solicitudes` vale 1240, después de la segunda 1325 y después de la tercera 2650. El programa imprime 2650. El signo igual no compara, guarda, y cada línea pisa el valor que dejó la anterior.

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
# Montos autorizados por la mesa MC-01 el 8 de enero, en pesos.
from statistics import mean

montos = [96500, 148200, 73400, 151100, 118900]

promedio = mean(montos)
mayor = max(montos)

print("Creditos:", len(montos))
print("Monto promedio:", promedio)
print("Monto mayor:", mayor)
```

La tabla de los tres errores provocados:

| Qué se rompió | Mensaje |
|---|---|
| Paréntesis de cierre | `SyntaxError: '(' was never closed` |
| `print` con mayúscula | `NameError: name 'Print' is not defined. Did you mean: 'print'?` |
| Comilla borrada | `SyntaxError: unterminated string literal (detected at line 2)` |

**Salida**

```text
Creditos: 5
Monto promedio: 117620
Monto mayor: 151100
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
# Traduccion del pseudocodigo del veredicto de precio, semana 2.
tasa = 18.50

if tasa > 18.50:
    veredicto = "Sobreprecio fuera de politica"
elif tasa < 17.50:
    veredicto = "Descuento fuera de politica"
else:
    veredicto = "Dentro de politica"

print("Tasa otorgada:", tasa, "%")
print("Veredicto:", veredicto)
```

La corrida de 18.00 imprime `18.0` porque el cero final no es parte del valor. El número guardado es dieciocho, y cuántos decimales se ven es una decisión de presentación que se resuelve con formato, no con el dato.

Si se intercambian las dos primeras ramas, una solicitud de 18.80 % sigue saliendo como sobreprecio, porque `18.80 < 17.50` falla y la segunda rama sí se evalúa. El intercambio que sí rompe el algoritmo es el de la semana 2, donde la rama de dentro de política se pone primero.

**Salida**

```text
Tasa otorgada: 18.5 %
Veredicto: Dentro de politica

Tasa otorgada: 17.4 %
Veredicto: Descuento fuera de politica

Tasa otorgada: 18.0 %
Veredicto: Dentro de politica
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La traducción respeta el orden de las tres ramas | 3 |
| Las tres corridas se pegan completas y son correctas | 3 |
| Explica por qué imprime `18.0` | 2 |
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
1850
68
True
False
0.15000000000000002
```

La segunda línea dice cuántos paquetes de revisión se llenan por completo: 51. La tercera dice cuántas solicitudes quedan sueltas después de llenarlos: 16.

La sexta y la séptima línea comparan decimales que en papel salen exactos y dan resultados opuestos. La razón es que 0.05 no se puede representar exactamente en binario. En un caso los errores de redondeo se cancelan y la igualdad se cumple; en el otro no. Por eso la banda de precio se escribe con sus dos límites como constantes y nunca se calcula sumando y restando dentro de una condición.

**Salida**

```text
51.666666666666664
51
16
1850
68
True
False
0.15000000000000002
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho líneas correctas, con la primera sin redondear | 4 |
| Interpreta la división entera y el residuo en paquetes y solicitudes | 2 |
| Distingue la concatenación de texto de la suma de enteros | 2 |
| Explica por qué dos comparaciones parecidas dan resultados opuestos | 2 |

**Error que más se ve**

Contestar `True` en la séptima línea porque en papel 0.05 por 3 es 0.15: es el mismo razonamiento correcto que produce una condición de banda que falla una vez cada mil solicitudes.

### 04.2 · Aplicar

**Solución**

```python
financiera = "Altamar"
mesa = "MC-01"
fecha = "2026-01-08"
solicitudes = 1240
rechazadas = 37
horas_analista = 86.4
mesa_activa = True
ultima_incidencia = None

tasa_rechazo = rechazadas / solicitudes
horas_por_solicitud = horas_analista / solicitudes

print(f"{financiera} {mesa} {fecha}")
print(f"Tasa de rechazo:      {round(tasa_rechazo * 100, 2)} %")
print(f"Horas por solicitud:  {round(horas_por_solicitud, 4)} h")
print(type(solicitudes), type(horas_analista))
print(type(mesa), type(mesa_activa), type(ultima_incidencia))
```

La fecha se guarda como texto porque todavía no hay nada que hacer con ella. `ultima_incidencia` vale `None`, que es ausencia de dato, y no cero: cero minutos de caída del sistema es una medición, `None` es que nadie registró nada.

**Salida**

```text
Altamar MC-01 2026-01-08
Tasa de rechazo:      2.98 %
Horas por solicitud:  0.0697 h
<class 'int'> <class 'float'>
<class 'str'> <class 'bool'> <class 'NoneType'>
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho variables con el tipo que les corresponde | 3 |
| `ultima_incidencia` en `None` y no en cero, con la explicación | 2 |
| Las dos métricas correctas y redondeadas | 3 |
| Los nombres dicen qué guardan y ninguno es de una letra | 2 |

**Error que más se ve**

Poner `ultima_incidencia = 0`: el programa corre y el promedio de duración de incidencias sale mal en cuanto alguien lo calcule, porque un corte sin incidencias entra al promedio como una incidencia de cero minutos.

### 04.3 · Integrar

**Solución**

```python
solicitudes = 1240
rechazadas = 37
horas_analista = 86.4
por_paquete = 24

por_solicitud_mal = horas_analista / solicitudes - rechazadas
por_solicitud_bien = horas_analista / (solicitudes - rechazadas)

print(f"Sin parentesis: {round(por_solicitud_mal, 4)}")
print(f"Con parentesis: {round(por_solicitud_bien, 4)} h por solicitud aprobada")

aprobadas = solicitudes - rechazadas
paquetes_llenos = aprobadas // por_paquete
sueltas = aprobadas % por_paquete

print(f"Solicitudes aprobadas: {aprobadas}")
print(f"Paquetes llenos: {paquetes_llenos}, solicitudes sueltas: {sueltas}")

folio = "00847"

print(f"Folio: {folio}  entero: {int(folio)}  de regreso: {str(int(folio))}")
```

La primera versión reparte las horas entre todas las solicitudes y después le resta 37 al resultado, o sea le resta solicitudes a un tiempo por solicitud. Da negativo porque está restando expedientes a horas. La segunda reparte las horas del corte entre las 1203 solicitudes que sí se aprobaron, que es la pregunta que se hizo.

El folio pierde los ceros a la izquierda en cuanto se vuelve entero, y ya no los recupera al regresar a texto. Lo que se perdió no es el número, es el identificador.

**Salida**

```text
Sin parentesis: -36.9303
Con parentesis: 0.0718 h por solicitud aprobada
Solicitudes aprobadas: 1203
Paquetes llenos: 50, solicitudes sueltas: 3
Folio: 00847  entero: 847  de regreso: 847
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos expresiones escritas y sus dos resultados | 3 |
| Explica qué calcula cada una, no solo cuál está bien | 2 |
| Paquetes llenos y solicitudes sueltas correctos | 3 |
| Reporta la pérdida de los ceros del folio y qué implica | 2 |

**Error que más se ve**

Calcular los paquetes con las 1240 solicitudes recibidas en lugar de las 1203 aprobadas: el número queda cerca del correcto, y por eso nadie lo revisa hasta que faltan expedientes en el archivo físico.

---

## Semana 05 · Tema 4 · Instrucciones, entrada y salida

### 05.1 · Reconocer

**Solución**

```text
Solicitudes: 1,240
Horas: 86.40 h
Rechazo: 3.0%
Rechazo: 2.98%
MC-01         1240
Tasa cruda: 0.029838709677419355
Horas: {horas:.2f} h
```

Las líneas tercera y cuarta muestran el mismo dato con distinto número de decimales: la de un decimal redondea 2.98 a 3.0, y en un reporte de originación esa diferencia decide si la mesa aparece dentro o fuera de una meta de 3 %.

A la última línea le falta la `f` antes de la comilla. No es un error: la cadena se imprime tal cual, con las llaves y el código de formato adentro, y el programa sigue corriendo como si nada.

**Salida**

```text
Solicitudes: 1,240
Horas: 86.40 h
Rechazo: 3.0%
Rechazo: 2.98%
MC-01         1240
Tasa cruda: 0.029838709677419355
Horas: {horas:.2f} h
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
mesa = input("Mesa: ")
solicitudes = int(input("Solicitudes recibidas: "))
rechazadas = int(input("Solicitudes rechazadas: "))
horas = float(input("Horas-analista del corte: "))

tasa = rechazadas / solicitudes
por_solicitud = horas / solicitudes

print(f"Mesa:                 {mesa}")
print(f"Solicitudes:          {solicitudes:,}")
print(f"Rechazadas:           {rechazadas:,}")
print(f"Tasa de rechazo:      {tasa:.2%}")
print(f"Horas por solicitud:  {por_solicitud:.4f} h")
```

**Salida**

```text
Mesa: MC-01
Solicitudes recibidas: 1240
Solicitudes rechazadas: 37
Horas-analista del corte: 86.4
Mesa:                 MC-01
Solicitudes:          1,240
Rechazadas:           37
Tasa de rechazo:      2.98%
Horas por solicitud:  0.0697 h
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro `input` traen mensaje y se convierten donde toca | 3 |
| Las dos métricas son correctas | 3 |
| Formato de miles, porcentaje y cuatro decimales aplicados | 2 |
| La sesión se entrega completa, con lo capturado | 2 |

**Error que más se ve**

Convertir después de operar, con `int(solicitudes / rechazadas)` en lugar de convertir cada `input`: la división de dos textos revienta antes, y cuando no revienta es porque el alumno concatenó sin darse cuenta.

### 05.3 · Integrar

**Solución**

```python
SEGUNDOS_JORNADA = 28800

mesa = input("Mesa: ")
solicitudes = int(input("Solicitudes recibidas: "))
rechazadas = int(input("Solicitudes rechazadas: "))
horas = float(input("Horas-analista del corte: "))

aprobadas = solicitudes - rechazadas
tasa = rechazadas / solicitudes
segundos = SEGUNDOS_JORNADA / solicitudes
minutos_por_aprobada = horas * 60 / aprobadas

print(f"Reporte de corte {mesa}")
print(f"{'Solicitudes recibidas':<22}{solicitudes:>10,}")
print(f"{'Solicitudes aprobadas':<22}{aprobadas:>10,}")
print(f"{'Tasa de rechazo':<22}{tasa:>10.2%}")
print(f"{'Tiempo por solicitud':<22}{segundos:>10.2f} s")
print(f"{'Minutos por aprobada':<22}{minutos_por_aprobada:>10.2f} min")
```

El tiempo por solicitud se calcula con las solicitudes recibidas, porque la mesa ocupó jornada también en las que terminó rechazando. Los minutos de análisis se reparten solo entre las aprobadas, porque es un costo que hay que cargarle a lo que sí se colocó. Dos denominadores distintos en el mismo reporte, cada uno con su razón.

**Salida**

```text
Mesa: MC-03
Solicitudes recibidas: 1512
Solicitudes rechazadas: 68
Horas-analista del corte: 112.8
Reporte de corte MC-03
Solicitudes recibidas      1,512
Solicitudes aprobadas      1,444
Tasa de rechazo            4.50%
Tiempo por solicitud       19.05 s
Minutos por aprobada        4.69 min
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco cifras correctas | 4 |
| La constante de la jornada tiene nombre y está arriba | 1 |
| Las cinco líneas alineadas con los anchos pedidos | 2 |
| Cada cifra lleva su unidad | 1 |
| Justifica los dos denominadores distintos | 2 |

**Error que más se ve**

Calcular el tiempo por solicitud con las aprobadas: sale 19.94 segundos y suena razonable, pero la mesa no dejó de trabajar en las 68 solicitudes que terminó rechazando.

---

## Semana 06 · Tema 4.4 · Estructuras de selección

### 06.1 · Reconocer

**Solución**

El primer programa imprime `18.5 Dentro de politica`. La condición pide estrictamente mayor, y 18.50 no es mayor que 18.50, así que la solicitud cae en el `else`. Es el comportamiento correcto: el límite superior es parte de la banda autorizada.

El segundo programa imprime `18.8 Dentro de politica`, y eso está mal. La primera condición pregunta si la tasa es mayor o igual al límite inferior, y una solicitud de 18.80 lo cumple. Como la primera rama que se cumple es la que se ejecuta, la del sobreprecio nunca se alcanza: cualquier valor mayor a 18.50 también es mayor o igual a 17.50.

El orden correcto va de lo más exigente a lo menos: primero el sobreprecio, después el descuento, y al final el dentro de política como caso restante.

**Salida**

```text
18.5 Dentro de politica
18.8 Dentro de politica
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las dos salidas correctas | 4 |
| Explica por qué 18.50 queda dentro con el operador estricto | 2 |
| Detecta que la rama del sobreprecio es inalcanzable y dice por qué | 2 |
| Escribe el orden correcto de las tres condiciones | 2 |

**Error que más se ve**

Decir que el segundo programa lanza un error porque hay dos condiciones que se cumplen: no hay error, se ejecuta la primera y las demás ni se leen, que es exactamente lo que lo vuelve peligroso.

### 06.2 · Aplicar

**Solución**

```python
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50

solicitud = input("Folio de la solicitud: ")
tasa = float(input("Tasa otorgada en %: "))

if tasa > LIMITE_SUPERIOR:
    veredicto = "Sobreprecio fuera de politica"
elif tasa < LIMITE_INFERIOR:
    veredicto = "Descuento fuera de politica"
else:
    veredicto = "Dentro de politica"

print(f"Solicitud {solicitud}: {tasa:.2f} % -> {veredicto}")
```

**Salida**

```text
Folio de la solicitud: SOL-1003
Tasa otorgada en %: 18.60
Solicitud SOL-1003: 18.60 % -> Sobreprecio fuera de politica

Folio de la solicitud: SOL-1005
Tasa otorgada en %: 17.40
Solicitud SOL-1005: 17.40 % -> Descuento fuera de politica

Folio de la solicitud: SOL-1008
Tasa otorgada en %: 18.50
Solicitud SOL-1008: 18.50 % -> Dentro de politica

Folio de la solicitud: SOL-1013
Tasa otorgada en %: 17.50
Solicitud SOL-1013: 17.50 % -> Dentro de politica

Folio de la solicitud: SOL-1004
Tasa otorgada en %: 18.00
Solicitud SOL-1004: 18.00 % -> Dentro de politica
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres veredictos correctos en las cinco corridas | 4 |
| Los dos límites son constantes con nombre, no números sueltos | 2 |
| Las solicitudes de 18.50 y 17.50 salen dentro de política | 2 |
| El folio se lee como texto y la tasa se convierte a decimal | 2 |

**Error que más se ve**

Usar `>=` en la primera condición: las solicitudes de 18.50 se marcan como excepción, la mesa manda a comité alrededor de una de cada diez, y el programa se ve perfectamente correcto.

### 06.3 · Integrar

**Solución**

```python
NOMINAL = 18.00
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50
TOPE_AUTORIZACION = 19.50
PISO_DIRECCION = 16.50

tasa = float(input("Tasa otorgada en %: "))

if tasa <= 0 or tasa > 60:
    veredicto = "Dato invalido: revisar la captura"
elif tasa > TOPE_AUTORIZACION:
    veredicto = "Se cancela por sobreprecio"
elif tasa > LIMITE_SUPERIOR:
    veredicto = "Sobreprecio: autoriza el comite"
elif tasa >= LIMITE_INFERIOR:
    veredicto = "Dentro de politica"
elif tasa >= PISO_DIRECCION:
    veredicto = "Descuento: autoriza direccion"
else:
    veredicto = "Se cancela por margen"

print(f"{tasa:>7.2f} %  {veredicto}")
```

La validación va primero porque una tasa de -3.00 % no es un descuento agresivo, es un campo mal capturado, y clasificarla como cancelación por margen escondería la falla del sistema.

Tabla de fronteras:

| Frontera | Valor exacto | Veredicto | Por qué ese operador |
|---|---|---|---|
| Tope de autorización | 19.50 | Comité | `>` deja el 19.50 del lado que el comité todavía puede autorizar |
| Límite superior | 18.50 | Dentro de política | `>` incluye el límite en la banda, como dice la política |
| Límite inferior | 17.50 | Dentro de política | `>=` incluye el límite en la banda |
| Piso de dirección | 16.50 | Descuento autorizable | `>=` deja el 16.50 del lado que dirección puede firmar |
| Validación | 0 y 60 | Inválido | `<=` en cero porque una tasa de cero es un campo vacío |

**Salida**

```text
Tasa otorgada en %: 20.00
  20.00 %  Se cancela por sobreprecio
Tasa otorgada en %: 19.50
  19.50 %  Sobreprecio: autoriza el comite
Tasa otorgada en %: 18.60
  18.60 %  Sobreprecio: autoriza el comite
Tasa otorgada en %: 18.50
  18.50 %  Dentro de politica
Tasa otorgada en %: 18.00
  18.00 %  Dentro de politica
Tasa otorgada en %: 17.50
  17.50 %  Dentro de politica
Tasa otorgada en %: 17.20
  17.20 %  Descuento: autoriza direccion
Tasa otorgada en %: 16.50
  16.50 %  Descuento: autoriza direccion
Tasa otorgada en %: 16.20
  16.20 %  Se cancela por margen
Tasa otorgada en %: -3.00
  -3.00 %  Dato invalido: revisar la captura
Tasa otorgada en %: 75.00
  75.00 %  Dato invalido: revisar la captura
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

Poner la validación al final, después del `else`: nunca se ejecuta, porque para entonces el -3.00 ya salió clasificado como cancelación por margen y el programa no marca nada.

---

## Semana 07 · Tema 4.4 · Selección anidada y operadores lógicos

### 07.1 · Reconocer

**Solución**

```text
Mesa critica
True
False
Sin datos suficientes
True
```

Línea 1. La condición es `mesa == "MC-01" or "MC-03"`. Python evalúa la comparación, que da falso, y después evalúa la cadena `"MC-03"`, que por no estar vacía cuenta como verdadera. La condición completa siempre es verdadera, incluso con MC-04. La forma correcta es `mesa in ["MC-01", "MC-03"]`.

Línea 2. Las dos listas tienen los mismos valores en el mismo orden, así que son iguales.

Línea 3. Son dos listas distintas en memoria, así que `is` da falso. El doble igual compara contenido, `is` compara identidad.

Línea 4. Con cero solicitudes, `solicitudes > 0` es falso y Python ya no evalúa la división. Esa es la evaluación corta del `and`, y es lo que evita el `ZeroDivisionError`. Con `or` la primera condición falsa obliga a evaluar la segunda, y ahí sí revienta.

Línea 5. `ultima_incidencia is None` es la forma correcta de preguntar por la ausencia de un valor.

**Salida**

```text
Mesa critica
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

Contestar «Mesa normal» en la primera línea razonando sobre la intención del código: se lee lo que quiso decir el autor en lugar de lo que Python evalúa, y se detecta porque el alumno tampoco nota nada raro con MC-04.

### 07.2 · Aplicar

**Solución**

```python
CRITICAS = ["MC-01", "MC-03"]
TASA_MAXIMA = 0.03
MINIMO_SOLICITUDES = 500

mesa = input("Mesa: ")
solicitudes = int(input("Solicitudes del corte: "))
rechazadas = int(input("Solicitudes rechazadas: "))
en_auditoria = input("En auditoria (si/no): ") == "si"

tasa = rechazadas / solicitudes

if not en_auditoria and solicitudes >= MINIMO_SOLICITUDES and tasa <= TASA_MAXIMA:
    decision = "Corte liberado"
elif mesa in CRITICAS:
    decision = "Retener: mesa critica que no cumplio"
else:
    decision = "Retener para revision expediente por expediente"

print(f"{mesa} {solicitudes:>5} solicitudes  tasa {tasa:.2%}  -> {decision}")
```

**Salida**

```text
Mesa: MC-01
Solicitudes del corte: 1240
Solicitudes rechazadas: 37
En auditoria (si/no): no
MC-01  1240 solicitudes  tasa 2.98%  -> Corte liberado

Mesa: MC-03
Solicitudes del corte: 1512
Solicitudes rechazadas: 68
En auditoria (si/no): no
MC-03  1512 solicitudes  tasa 4.50%  -> Retener: mesa critica que no cumplio

Mesa: MC-04
Solicitudes del corte: 760
Solicitudes rechazadas: 9
En auditoria (si/no): no
MC-04   760 solicitudes  tasa 1.18%  -> Corte liberado

Mesa: MC-02
Solicitudes del corte: 420
Solicitudes rechazadas: 5
En auditoria (si/no): no
MC-02   420 solicitudes  tasa 1.19%  -> Retener para revision expediente por expediente

Mesa: MC-01
Solicitudes del corte: 1240
Solicitudes rechazadas: 37
En auditoria (si/no): si
MC-01  1240 solicitudes  tasa 2.98%  -> Retener: mesa critica que no cumplio
```

El cuarto caso es el que enseña algo: MC-02 tiene una tasa de 1.19 %, mejor que la de MC-01, y aun así se retiene. El corte de 420 solicitudes no llega al mínimo, y sin volumen la tasa no significa nada.

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cinco decisiones correctas | 4 |
| La regla de liberación usa `and` con las tres condiciones | 2 |
| La pertenencia se pregunta con `in` sobre la lista de críticas | 2 |
| Los tres umbrales son constantes con nombre | 1 |
| Comenta el caso del corte chico con buena tasa | 1 |

**Error que más se ve**

Escribir `mesa in "MC-01"` sin corchetes: la condición pasa a preguntar si el texto está contenido en el otro texto, funciona por accidente con MC-01 y falla en silencio con cualquier otra.

### 07.3 · Integrar

**Solución**

```python
LIMITE_MORA = 3.0
LIMITE_SOBREPRECIO = 0.50

mora = float(input("Mora de la cartera de la mesa en %: "))
sobreprecio = float(input("Sobreprecio promedio en puntos: "))

if mora > LIMITE_MORA:
    if sobreprecio > LIMITE_SOBREPRECIO:
        anidada = "Bloquear la mesa"
    else:
        anidada = "Seguir colocando"
else:
    if sobreprecio > LIMITE_SOBREPRECIO:
        anidada = "Seguir colocando"
    else:
        anidada = "Seguir colocando"

if mora > LIMITE_MORA and sobreprecio > LIMITE_SOBREPRECIO:
    combinada = "Bloquear la mesa"
else:
    combinada = "Seguir colocando"

print(f"{mora:>5.1f} %  {sobreprecio:>4.2f} pts  "
      f"anidada: {anidada:<18} combinada: {combinada:<18} "
      f"iguales: {anidada == combinada}")
```

Este anidado se podía colapsar porque las dos ramas internas del `else` externo hacen exactamente lo mismo. Cuando eso pasa, la segunda pregunta no aporta nada en ese camino, y las cuatro ramas se reducen a una condición unida con `and`.

Un caso de la misma área donde el anidado no se colapsa: si la mesa está en auditoría, su sobreprecio no significa nada y la acción es esperar el dictamen; si no lo está, el sobreprecio decide entre subir la meta, mantenerla y bloquear. Ahí las ramas internas hacen tres cosas distintas y la rama externa hace una cuarta, así que el anidado gana algo real.

**Salida**

```text
Mora de la cartera de la mesa en %: 4.2
Sobreprecio promedio en puntos: 0.80
  4.2 %  0.80 pts  anidada: Bloquear la mesa   combinada: Bloquear la mesa   iguales: True

Mora de la cartera de la mesa en %: 4.2
Sobreprecio promedio en puntos: 0.30
  4.2 %  0.30 pts  anidada: Seguir colocando   combinada: Seguir colocando   iguales: True

Mora de la cartera de la mesa en %: 2.4
Sobreprecio promedio en puntos: 0.80
  2.4 %  0.80 pts  anidada: Seguir colocando   combinada: Seguir colocando   iguales: True

Mora de la cartera de la mesa en %: 2.4
Sobreprecio promedio en puntos: 0.30
  2.4 %  0.30 pts  anidada: Seguir colocando   combinada: Seguir colocando   iguales: True
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

El `for` imprime seis líneas: 12, 18, 24, 30, 36 y 42. El `range` con paso 6 arranca en 12 y se detiene antes de 48, así que el 48 no aparece nunca. El último plazo que cabe es 42.

El `while` imprime `7 -2500.0`. El presupuesto arranca con 50,000 pesos y cada semana consume 7,500, así que después de seis semanas quedan 5,000. La condición pregunta si queda más de cero, y con 5,000 se cumple, así que entra a la séptima vuelta y resta 7,500 otra vez. El contador queda en 7 y el saldo en -2,500.

Semanas completas que aguanta de verdad: seis. La séptima empezó y se quedó sin fondos a la mitad, y el número negativo es la evidencia de eso.

Si se borra la línea que resta el gasto, la condición nunca cambia y el ciclo no termina. Hay que detenerlo con Control C.

**Salida**

```text
12
18
24
30
36
42
7 -2500.0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis líneas del `for` y el conteo | 3 |
| La salida del `while` con el saldo negativo | 3 |
| Distingue las 7 impresas de las 6 semanas completas reales | 2 |
| Identifica el ciclo infinito si se borra la resta | 2 |

**Error que más se ve**

Contestar que el presupuesto aguanta 7 semanas porque eso imprime el programa: el número está bien calculado y contesta otra pregunta, y el -2,500 que aparece al lado es justo la pista que nadie lee.

### 08.2 · Aplicar

**Solución**

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes = [1240, 984, 1512, 760]
rechazadas = [37, 12, 68, 9]
horas = [86.4, 61.5, 112.8, 48.2]

total_solicitudes = 0
total_rechazadas = 0
total_horas = 0.0

print(f"{'Mesa':<10}{'Solicitudes':>13}{'Rechazo':>10}{'h/solicitud':>13}")

for i in range(len(mesas)):
    tasa = rechazadas[i] / solicitudes[i]
    por_solicitud = horas[i] / solicitudes[i]

    total_solicitudes += solicitudes[i]
    total_rechazadas += rechazadas[i]
    total_horas += horas[i]

    print(f"{mesas[i]:<10}{solicitudes[i]:>13,}{tasa:>10.2%}{por_solicitud:>13.4f}")

tasa_area = total_rechazadas / total_solicitudes
horas_area = total_horas / total_solicitudes

print(f"{'ALTAMAR':<10}{total_solicitudes:>13,}{tasa_area:>10.2%}{horas_area:>13.4f}")
```

El renglón del área divide la suma de rechazadas entre la suma de solicitudes. Promediar las cuatro tasas daría 2.47 %, que le da el mismo peso a MC-04 con 760 solicitudes que a MC-03 con 1512, y no es lo que produjo el área.

**Salida**

```text
Mesa        Solicitudes   Rechazo  h/solicitud
MC-01             1,240     2.98%       0.0697
MC-02               984     1.22%       0.0625
MC-03             1,512     4.50%       0.0746
MC-04               760     1.18%       0.0634
ALTAMAR           4,496     2.80%       0.0687
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro renglones y sus tres cifras correctas | 3 |
| El renglón del área divide sumas y no promedia tasas | 3 |
| Un solo recorrido, con los tres acumuladores fuera del ciclo | 2 |
| El ciclo funciona igual si se agrega una quinta mesa | 1 |
| Salida alineada en columnas | 1 |

**Error que más se ve**

Calcular la tasa del área como el promedio de las cuatro: sale 2.47 % en vez de 2.80 %, se ve razonable, y subestima el rechazo justo donde está el volumen.

### 08.3 · Integrar

**Solución**

```python
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50

solicitudes = ["SOL-1001", "SOL-1002", "SOL-1003", "SOL-1004",
               "SOL-1005", "SOL-1006", "SOL-1007", "SOL-1008",
               "SOL-1009", "SOL-1010", "SOL-1011", "SOL-1012"]
tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

fuera = 0
suma = 0.0

for i in range(len(solicitudes)):
    tasa = tasas[i]
    suma += tasa

    if tasa > LIMITE_SUPERIOR:
        veredicto = "Sobreprecio fuera de politica"
        fuera += 1
    elif tasa < LIMITE_INFERIOR:
        veredicto = "Descuento fuera de politica"
        fuera += 1
    else:
        veredicto = "Dentro de politica"

    print(f"{solicitudes[i]:<10}{tasa:>7.2f}  {veredicto}")

promedio = suma / len(tasas)
proporcion = fuera / len(tasas)

print(f"{'Promedio':<10}{promedio:>7.4f} %")
print(f"Fuera de politica: {fuera} de {len(tasas)} ({proporcion:.1%})")
```

La solicitud SOL-1008 se colocó a 18.50 %, que es exactamente el límite superior, y el límite es parte de la banda. Con `>=` en la primera condición saldrían 4 solicitudes fuera en lugar de 3, y la proporción del corte pasaría de 25.0 % a 33.3 % sin que ninguna solicitud hubiera cambiado de precio.

**Salida**

```text
SOL-1001    18.10  Dentro de politica
SOL-1002    17.80  Dentro de politica
SOL-1003    18.60  Sobreprecio fuera de politica
SOL-1004    18.00  Dentro de politica
SOL-1005    17.40  Descuento fuera de politica
SOL-1006    18.30  Dentro de politica
SOL-1007    17.90  Dentro de politica
SOL-1008    18.50  Dentro de politica
SOL-1009    17.60  Dentro de politica
SOL-1010    18.20  Dentro de politica
SOL-1011    18.80  Sobreprecio fuera de politica
SOL-1012    17.70  Dentro de politica
Promedio  18.0750 %
Fuera de politica: 3 de 12 (25.0%)
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los doce veredictos correctos | 3 |
| Promedio a cuatro decimales y conteo de fuera de política | 3 |
| El acumulador y el contador están declarados antes del ciclo | 2 |
| Explica el caso de SOL-1008 y el efecto de cambiar a `>=` | 2 |

**Error que más se ve**

Declarar `suma = 0.0` dentro del `for`: al final vale 17.70, el promedio sale 1.4750 % y lo delata que ningún crédito de nómina se coloca a menos de dos puntos.

---

## Semana 09 · Tema 4.5 · Acumuladores, banderas y ciclos anidados

### 09.1 · Reconocer

**Solución**

El primer programa imprime `48.2`. Se esperaba 308.9, que es la suma de las cuatro cargas de trabajo. La línea `total = 0.0` está dentro del ciclo, así que en cada vuelta borra lo acumulado y al final solo queda el último valor. La única línea que hay que mover es esa, y va antes del `for`.

El segundo programa imprime `Primera fuera de control: MC-03`. La traza de las cuatro vueltas:

| i | Mesa | Solicitudes | Qué pasa |
|---|---|---|---|
| 0 | MC-01 | 1240 | Pasa el filtro. 2.98 % no rebasa 3 %, sigue |
| 1 | MC-02 | 984 | Menos de 1000 solicitudes, el `continue` la salta |
| 2 | MC-03 | 1512 | Pasa el filtro. 4.50 % sí rebasa, imprime y sale con `break` |
| 3 | MC-04 | 760 | No se evalúa, el `break` ya salió del ciclo |

El `else` del `for` no se ejecuta porque el ciclo salió por `break`. Se ejecutaría si ninguna mesa con al menos 1000 solicitudes rebasara el 3 %, por ejemplo si MC-03 hubiera cerrado el corte con 40 rechazos en lugar de 68.

**Salida**

```text
48.2
Primera fuera de control: MC-03
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
HORAS_META = 0.070

mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes = [1240, 984, 1512, 760]
rechazadas = [37, 12, 68, 9]
horas = [86.4, 61.5, 112.8, 48.2]

horas_totales = 0.0
fuera_de_meta = 0
hay_lenta = False

for i in range(len(mesas)):
    horas_totales += horas[i]

    if rechazadas[i] / solicitudes[i] > TASA_META:
        fuera_de_meta += 1

    if horas[i] / solicitudes[i] > HORAS_META:
        hay_lenta = True

print(f"Horas-analista del corte: {horas_totales:,.1f} h")
print(f"Mesas fuera de meta:      {fuera_de_meta}")
print(f"Alguna sobre 0.070 h:     {hay_lenta}")
```

La segunda pregunta cuenta casos, no magnitudes: sumar las tasas daría un número sin significado. La primera suma magnitudes: contar mesas no dice cuántas horas de análisis se pagaron. La bandera contesta si existe al menos una, y para eso no hace falta ni contar ni sumar.

**Salida**

```text
Horas-analista del corte: 308.9 h
Mesas fuera de meta:      1
Alguna sobre 0.070 h:     True
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

Escribir la bandera como `hay_lenta = horas[i] / solicitudes[i] > HORAS_META` sin el `if`: la variable se sobreescribe en cada vuelta y al final solo refleja la última mesa, que en estos datos da falso.

### 09.3 · Integrar

**Solución**

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
solicitudes_por_hora = [155, 123, 189, 95]
turnos = ["T1", "T2", "T3"]
horas = [8, 8, 6]

capacidad_total = 0
combinaciones_altas = 0

for i in range(len(mesas)):
    for j in range(len(turnos)):
        proyeccion = solicitudes_por_hora[i] * horas[j]
        capacidad_total += proyeccion

        if proyeccion > 1000:
            combinaciones_altas += 1

        print(f"{mesas[i]:<8}{turnos[j]:<5}{proyeccion:>7,}")

print(f"{'TOTAL':<13}{capacidad_total:>7,}")
print(f"Combinaciones arriba de 1000 solicitudes: {combinaciones_altas}")
```

Cuatro mesas por tres turnos son doce renglones, y ese conteo se escribe antes de correr el programa. Con 40 mesas y 3 turnos serían 120 vueltas, que sigue siendo nada. El problema aparece cuando los dos ciclos recorren listas largas: 1000 por 1000 son un millón de vueltas, y ahí un anidado deja de ser gratis.

**Salida**

```text
MC-01   T1     1,240
MC-01   T2     1,240
MC-01   T3       930
MC-02   T1       984
MC-02   T2       984
MC-02   T3       738
MC-03   T1     1,512
MC-03   T2     1,512
MC-03   T3     1,134
MC-04   T1       760
MC-04   T2       760
MC-04   T3       570
TOTAL         12,364
Combinaciones arriba de 1000 solicitudes: 5
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

Usar `i` en los dos ciclos: el interno pisa al externo, salen renglones repetidos de la última mesa y el total se descompone sin que Python marque nada.

---

## Semana 10 · Tema 5 · Funciones definidas por el usuario

### 10.1 · Reconocer

**Solución**

La primera línea imprime `None`. La función calcula la división y no la devuelve, así que entrega el valor que Python devuelve por omisión cuando no hay `return`. La segunda imprime `4.180645161290323`, que sí son los minutos de análisis por solicitud. La tercera lanza `NameError`.

Al `tasa_rechazo` le falta el `return`. El error no aparece dentro de la función porque ahí no hay nada mal escrito: aparece más adelante, en cuanto alguien intente multiplicar, comparar o formatear ese `None`.

La tercera línea falla porque `unitario` nació dentro de la función y desapareció cuando la función terminó. Fuera de ella ese nombre no existe.

Si la segunda función tuviera `print(unitario)` en lugar de `return unitario`, el número se vería en pantalla y la función devolvería `None`. El valor no se podría guardar, ni sumar, ni meter en una tabla.

**Salida**

```text
None
4.180645161290323
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
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50


def tasa_rechazo(solicitudes, rechazadas):
    """Devuelve la fraccion de solicitudes rechazadas de un corte."""
    return rechazadas / solicitudes


def dentro_de_politica(tasa):
    """Dice si una tasa otorgada cae en la banda de 17.50 a 18.50 por ciento."""
    return tasa >= LIMITE_INFERIOR and tasa <= LIMITE_SUPERIOR


print(round(tasa_rechazo(1240, 37), 4))
print(round(tasa_rechazo(1512, 68), 4))
print(round(tasa_rechazo(760, 0), 4))

print(dentro_de_politica(18.00))
print(dentro_de_politica(18.50))
print(dentro_de_politica(18.60))
```

El caso de 18.50 es el que hay que probar siempre porque es la frontera, y es donde se decide si el límite pertenece a la banda. Con `<` en lugar de `<=` esa solicitud saldría fuera de política, y la función seguiría dando resultados correctos en todos los demás valores.

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

Meter el `print` dentro de `dentro_de_politica`: la función se ve funcionando en pantalla y no sirve para contar cuántas solicitudes cumplen, que es justo lo que pide el ejercicio siguiente.

### 10.3 · Integrar

**Solución**

```python
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50


def dentro_de_politica(tasa):
    """Dice si una tasa otorgada cae en la banda de precio del producto."""
    return tasa >= LIMITE_INFERIOR and tasa <= LIMITE_SUPERIOR


def veredicto(tasa):
    """Devuelve el destino de la solicitud: dentro, sobreprecio o descuento."""
    if dentro_de_politica(tasa):
        return "Dentro de politica"
    if tasa > LIMITE_SUPERIOR:
        return "Sobreprecio"
    return "Descuento"


def solicitudes_en_politica(tasas):
    """Cuenta cuantas tasas de la lista caen dentro de la banda."""
    dentro = 0

    for tasa in tasas:
        if dentro_de_politica(tasa):
            dentro += 1

    return dentro


def tasa_promedio(tasas):
    """Devuelve el promedio de la lista de tasas otorgadas."""
    suma = 0.0

    for tasa in tasas:
        suma += tasa

    return suma / len(tasas)


solicitudes = ["SOL-1001", "SOL-1002", "SOL-1003", "SOL-1004",
               "SOL-1005", "SOL-1006", "SOL-1007", "SOL-1008",
               "SOL-1009", "SOL-1010", "SOL-1011", "SOL-1012"]
tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

for i in range(len(solicitudes)):
    print(f"{solicitudes[i]:<10}{tasas[i]:>7.2f}  {veredicto(tasas[i])}")

print(f"Revisadas:          {len(tasas)}")
print(f"Dentro de politica: {solicitudes_en_politica(tasas)}")
print(f"Tasa promedio:      {tasa_promedio(tasas):.4f} %")
```

La prueba de borrarle la comparación del límite inferior a `dentro_de_politica`: la solicitud SOL-1005, colocada a 17.40 %, pasaría a salir como dentro de política y el conteo subiría de 9 a 10. Las pruebas que lo detectan son las que usan un valor por debajo de la banda; si el alumno solo probó 18.00, 18.50 y 18.60, ninguna lo detecta y hay que agregar el caso de 17.40.

**Salida**

```text
SOL-1001    18.10  Dentro de politica
SOL-1002    17.80  Dentro de politica
SOL-1003    18.60  Sobreprecio
SOL-1004    18.00  Dentro de politica
SOL-1005    17.40  Descuento
SOL-1006    18.30  Dentro de politica
SOL-1007    17.90  Dentro de politica
SOL-1008    18.50  Dentro de politica
SOL-1009    17.60  Dentro de politica
SOL-1010    18.20  Dentro de politica
SOL-1011    18.80  Sobreprecio
SOL-1012    17.70  Dentro de politica
Revisadas:          12
Dentro de politica: 9
Tasa promedio:      18.0750 %
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro funciones con docstring y sin imprimir nada | 3 |
| `veredicto` llama a `dentro_de_politica` en vez de repetir la comparación | 2 |
| Los doce renglones y las tres cifras finales correctos | 3 |
| La prueba de borrar una línea y decir qué caso la detecta | 2 |

**Error que más se ve**

Repetir la comparación de la banda dentro de `veredicto` en lugar de llamar a la función: el programa funciona igual, y cuando dirección comercial cambie la banda habrá que acordarse de los dos lugares.

---

## Semana 11 · Tema 5 · Argumentos, funciones predefinidas y módulos

### 11.1 · Reconocer

**Solución**

```text
4.18
0.35
9.18
```

En la primera llamada no se pasa nada opcional: `factor` vale 60 y `extras` vale 0.0. Son los minutos de análisis por solicitud.

En la segunda, el 5.0 cayó en `factor`, porque los argumentos por posición llenan los huecos en orden y `factor` es el que sigue después de `solicitudes`. La función calculó 86.4 por 5 entre 1240, que no significa nada. Python no marca error porque recibió tres argumentos válidos para tres parámetros que existen.

En la tercera, el 5.0 se pasa por nombre a `extras`, se salta `factor`, y el resultado son los 4.18 anteriores más los extras.

Si `factor=60` se moviera antes de `solicitudes`, el archivo ni siquiera correría: un parámetro con valor por omisión no puede ir antes de uno sin él, y Python lo rechaza con `SyntaxError` al leerlo.

**Salida**

```text
4.180645161290323
0.34838709677419355
9.180645161290322
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los tres números correctos | 4 |
| Identifica que el 5.0 cayó en `factor` en la segunda llamada | 2 |
| Explica por qué Python no marca ningún error | 2 |
| Contesta que mover el opcional al frente es `SyntaxError` | 2 |

**Error que más se ve**

Contestar que la segunda llamada suma 5.0 al resultado: se lee el 5.0 como si fuera el extra porque es el único opcional que se ve en la tercera llamada, y el orden de los parámetros ni se revisa.

### 11.2 · Aplicar

**Solución**

```python
def fuera_de_politica(tasa, nominal=18.00, banda=0.50):
    """Dice si una tasa otorgada cae fuera de la banda nominal mas o menos banda."""
    inferior = nominal - banda
    superior = nominal + banda

    return tasa < inferior or tasa > superior


print(fuera_de_politica(18.60))
print(fuera_de_politica(18.50))
print(fuera_de_politica(18.60, 18.00, 1.00))
print(fuera_de_politica(18.60, banda=1.00))
print(fuera_de_politica(14.20, nominal=14.00))

print(18.00 - 0.50 == 17.50)
print(18.00 + 0.50 == 18.50)
```

Las dos comprobaciones del final dan verdadero, así que en este caso los límites calculados coinciden con los de la política escrita. La comprobación no sobra: con otra banda el resultado puede ser distinto, como se vio en la semana 4 con 0.05 por 3. Cuando una función calcula fronteras a partir de decimales, la frontera se prueba antes de confiar en ella.

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
| Una llamada pasa la banda por nombre saltándose el nominal | 2 |
| Las dos comprobaciones de frontera aparecen y se comentan | 2 |

**Error que más se ve**

Escribir `fuera_de_politica(18.60, 1.00)` queriendo abrir la banda: el 1.00 cae en `nominal`, la función compara contra una banda de 0.50 a 1.50 % y devuelve verdadero por la razón equivocada.

### 11.3 · Integrar

**Solución**

```python
from statistics import mean, median, pstdev

LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50

tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

con_atipica = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
               17.90, 18.50, 17.60, 18.20, 18.80, 17.70, 27.00]

print(f"Solicitudes: {len(tasas)}")
print(f"Promedio:    {mean(tasas):.4f} %")
print(f"Mediana:     {median(tasas):.4f} %")
print(f"Dispersion:  {pstdev(tasas):.4f} puntos")
print(f"Menor:       {sorted(tasas)[0]:.2f} %")
print(f"Mayor:       {max(tasas):.2f} %")

indice = (LIMITE_SUPERIOR - LIMITE_INFERIOR) / (6 * pstdev(tasas))
print(f"Indice:      {round(indice, 3)}")

print(f"Promedio con la tasa de 27.00: {mean(con_atipica):.4f} %")
print(f"Mediana con la tasa de 27.00:  {median(con_atipica):.4f} %")
```

La tercera función es `pstdev`, la desviación estándar de la población, documentada en la página del módulo `statistics` de docs.python.org. Recibe una serie de datos numéricos y devuelve la desviación estándar de esa serie tomada como población completa, no como muestra.

Un índice de capacidad de 0.41 significa que la variación real del precio es más ancha que la banda que autoriza la política. La banda mide 1.00 punto y seis dispersiones miden 2.44 puntos, así que aunque el precio promedio estuviera exactamente en 18.00 la mesa seguiría colocando fuera de banda. Al director comercial no se le pide que mueva la tasa de política: se le reporta que el proceso de cotización no está respetando el rango que él autorizó, y que hay que atacar la dispersión.

Con la tasa de 27.00 % el promedio salta de 18.0750 a 18.7615 y la mediana solo se mueve de 18.0500 a 18.1000. Cuando hay una captura sospechosa, la mediana es la que se reporta.

**Salida**

```text
Solicitudes: 12
Promedio:    18.0750 %
Mediana:     18.0500 %
Dispersion:  0.4065 puntos
Menor:       17.40 %
Mayor:       18.80 %
Indice:      0.41
Promedio con la tasa de 27.00: 18.7615 %
Mediana con la tasa de 27.00:  18.1000 %
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres funciones importadas y las siete cifras correctas | 3 |
| La tercera función sale de la documentación y se cita | 2 |
| El índice de capacidad es correcto y se interpreta | 3 |
| Compara promedio y mediana con la tasa atípica y elige una | 2 |

**Error que más se ve**

Reportar el índice de capacidad como si fuera un porcentaje de solicitudes bien cotizadas: 0.41 no es 41 %, es una razón entre el ancho de la banda y el de la dispersión, y confundirlos convierte una alerta grave en un número que suena tolerable.

---

## Semana 12 · Tema 6 · Listas y tuplas

### 12.1 · Reconocer

**Solución**

```text
18.1 17.4
[17.8, 18.6]
[17.4, 17.8, 18.0, 18.1, 18.6]
[18.1, 17.8, 18.6, 18.0, 17.4]
None
[17.4, 17.8, 18.0, 18.1, 18.6]
6 5
```

La última línea lanza `IndexError`. La lista quedó con seis elementos después del `append`, así que el último índice válido es el 5.

`tasas[1:3]` devuelve dos valores porque el primer índice entra y el segundo no. Es lo que hace que el tamaño de la rebanada sea la resta de los dos números.

`respaldo` y `copia` terminan distintos porque `respaldo = tasas` no copió nada: creó un segundo nombre para la misma lista, y el `append` la modificó. `copia = tasas.copy()` sí construyó una lista nueva, que ya no se enteró del cambio.

Con `tasas = tasas.sort()`, el método ordena la lista y devuelve `None`, y esa asignación deja el nombre `tasas` apuntando a `None`. Los datos se pierden y el error aparece después, en la siguiente línea que intente usarlos.

**Salida**

```text
18.1 17.4
[17.8, 18.6]
[17.4, 17.8, 18.0, 18.1, 18.6]
[18.1, 17.8, 18.6, 18.0, 17.4]
None
[17.4, 17.8, 18.0, 18.1, 18.6]
6 5
Traceback (most recent call last):
  File "w12_1.py", line 17, in <module>
    print(tasas[6])
          ~~~~~^^^
IndexError: list index out of range
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete líneas correctas y el `IndexError` final | 4 |
| Explica la regla de la rebanada con el segundo índice excluido | 2 |
| Explica el alias contra la copia y por qué dan 6 y 5 | 2 |
| Explica qué pasa con `tasas = tasas.sort()` | 2 |

**Error que más se ve**

Contestar `[17.8, 18.6, 18.0]` en la segunda línea: se cuentan tres posiciones porque tres menos uno son dos y el alumno suma el extremo, y basta comprobar que la longitud siempre es la resta de los dos índices.

### 12.2 · Aplicar

**Solución**

```python
tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

print("Al empezar:", tasas)

mayor = max(tasas)
menor = min(tasas)
tres_altas = sorted(tasas, reverse=True)[0:3]
posicion = tasas.index(17.40)

print(f"Mayor:             {mayor:.2f} %")
print(f"Menor:             {menor:.2f} %")
print(f"Tres mas altas:    {tres_altas}")
print(f"Posicion de 17.40: {posicion}")
print(f"Solicitud que le toca: SOL-{1001 + posicion}")
print(f"Ultimas tres:      {tasas[9:12]}")

print("Al terminar:", tasas)
```

El orden se pide con `sorted` y su argumento por nombre `reverse`, que es la semana 11 aplicada aquí. Con el método `sort` la lista original quedaría ordenada y el ejercicio pide lo contrario.

La posición 4 corresponde a la quinta solicitud, que es la SOL-1005, porque el folio arranca en SOL-1001 y el índice en 0.

**Salida**

```text
Al empezar: [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
Mayor:             18.80 %
Menor:             17.40 %
Tres mas altas:    [18.8, 18.6, 18.5]
Posicion de 17.40: 4
Solicitud que le toca: SOL-1005
Ultimas tres:      [18.2, 18.8, 17.7]
Al terminar: [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las cuatro respuestas correctas | 4 |
| La lista sale idéntica al principio y al final | 3 |
| El folio se calcula desde la posición y no se busca a mano | 2 |
| Usa `sorted` y no el método `sort` | 1 |

**Error que más se ve**

Contestar SOL-1004 para la tasa de 17.40: se suma el índice al folio inicial sin notar que la posición 4 es la quinta solicitud, y el resultado queda corrido uno.

### 12.3 · Integrar

**Solución**

```python
BANDA = (18.00, 17.50, 18.50)

tasas = [18.10, 17.80, 18.60, 18.00, 17.40, 18.30,
         17.90, 18.50, 17.60, 18.20, 18.80, 17.70]

fuera = []

for tasa in tasas:
    if tasa < BANDA[1] or tasa > BANDA[2]:
        fuera.append(tasa)

fuera_ordenada = sorted(fuera, reverse=True)

print(f"Nominal {BANDA[0]:.2f} %, banda de {BANDA[1]:.2f} a {BANDA[2]:.2f} %")
print(f"Solicitudes: {len(tasas)}")
print(f"Fuera:       {len(fuera)}")
print(f"Fuera de politica, de mayor a menor: {fuera_ordenada}")
print(f"Original intacta: {tasas}")

BANDA[2] = 19.00
```

La banda va en una tupla porque son los valores que autorizó dirección comercial y no deben cambiar mientras el programa corre. Si estuviera en una lista, cualquier línea podría modificarla por accidente y el programa seguiría corriendo con una política distinta a la que está firmada. El intento de asignación falla de inmediato y con un mensaje claro, que es exactamente lo que se quiere de una constante.

**Salida**

```text
Nominal 18.00 %, banda de 17.50 a 18.50 %
Solicitudes: 12
Fuera:       3
Fuera de politica, de mayor a menor: [18.8, 18.6, 17.4]
Original intacta: [18.1, 17.8, 18.6, 18.0, 17.4, 18.3, 17.9, 18.5, 17.6, 18.2, 18.8, 17.7]
Traceback (most recent call last):
  File "w12_3.py", line 20, in <module>
    BANDA[2] = 19.00
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

Escribir `fuera = tasas` y después quitarle a esa lista las solicitudes que sí cumplen: no hay dos listas, hay dos nombres para la misma, y el renglón que imprime la original al final lo delata.

---

## Semana 13 · Tema 6 · Conjuntos y diccionarios · Segundo parcial

### 13.1 · Reconocer

**Solución**

```text
4
Capacidad de pago arriba del 35 %
None
Motivo no catalogado
3
['M02', 'M03']
['M01']
['M01', 'M05']
```

La última línea lanza `KeyError` sobre la llave `M09`.

El diccionario termina con cuatro entradas porque `motivos["M02"] = ...` no agrega nada: la llave ya existía y se sobreescribió su valor. `motivos["M04"] = ...` sí agrega una entrada nueva. Tres más una son cuatro.

`corte_a` tiene tres elementos porque un conjunto no guarda repetidos: el `M01` que aparece dos veces cuenta una sola. Esa es la diferencia con la lista de la que salió.

**Salida**

```text
4
Capacidad de pago arriba del 35 %
None
Motivo no catalogado
3
['M02', 'M03']
['M01']
['M01', 'M05']
Traceback (most recent call last):
  File "w13_1.py", line 20, in <module>
    print(motivos["M09"])
          ~~~~~~~^^^^^^^
KeyError: 'M09'
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las ocho líneas correctas | 4 |
| El `KeyError` de la última línea, nombrado | 2 |
| Explica por qué el diccionario queda en cuatro entradas | 2 |
| Explica por qué el conjunto queda en tres elementos | 2 |

**Error que más se ve**

Contestar 5 en la primera línea: se cuentan las dos asignaciones como dos entradas nuevas, sin notar que M02 ya estaba y que una llave no se repite.

### 13.2 · Aplicar

**Solución**

```python
motivos = {"M01": "Score de buro insuficiente",
           "M02": "Capacidad de pago arriba del 35 %",
           "M03": "Documentacion incompleta",
           "M04": "Antiguedad laboral insuficiente",
           "M05": "Ingreso no comprobable",
           "M06": "Cliente ya tiene credito vigente"}

reportados = ["M01", "M03", "M01", "M05", "M01", "M02", "M03", "M09"]

print("Catalogo de motivos de rechazo")
for codigo, descripcion in motivos.items():
    print(f"  {codigo}  {descripcion}")

print(f"Motivos catalogados:  {len(motivos)}")
print(f"Rechazos reportados:  {len(reportados)}")
print(f"Motivos distintos:    {len(set(reportados))}")

for codigo in sorted(set(reportados)):
    print(f"  {codigo}  {motivos.get(codigo, 'Motivo no catalogado')}")
```

El M09 no está en el catálogo, y con corchetes el programa se habría detenido ahí. Con `get` y su valor por omisión, el reporte sale completo y además deja ver que alguien está capturando un motivo que no existe, que es información útil para el área.

**Salida**

```text
Catalogo de motivos de rechazo
  M01  Score de buro insuficiente
  M02  Capacidad de pago arriba del 35 %
  M03  Documentacion incompleta
  M04  Antiguedad laboral insuficiente
  M05  Ingreso no comprobable
  M06  Cliente ya tiene credito vigente
Motivos catalogados:  6
Rechazos reportados:  8
Motivos distintos:    5
  M01  Score de buro insuficiente
  M02  Capacidad de pago arriba del 35 %
  M03  Documentacion incompleta
  M05  Ingreso no comprobable
  M09  Motivo no catalogado
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El catálogo se recorre con `items` y sale completo | 2 |
| Las tres cifras son correctas | 3 |
| La consulta usa `get` con valor por omisión | 3 |
| El M09 aparece en el reporte sin detener el programa | 2 |

**Error que más se ve**

Contar los motivos distintos con `len(reportados)`: da 8 en lugar de 5, y confunde cuántos rechazos se reportaron con cuántos tipos de motivo hay.

### 13.3 · Integrar

**Solución**

```python
mesas = ["MC-01", "MC-02", "MC-03", "MC-04"]
horas = [86.4, 61.5, 112.8, 48.2]
solicitudes = [1240, 984, 1512, 760]

reportados_a = ["M01", "M03", "M01", "M05", "M01", "M02", "M03"]
reportados_b = ["M02", "M02", "M06", "M03", "M01"]

horas_por_mesa = {}
for i in range(len(mesas)):
    horas_por_mesa[mesas[i]] = horas[i]

conteo = {}
for codigo in reportados_a:
    conteo[codigo] = conteo.get(codigo, 0) + 1

print("Horas-analista por mesa")
for mesa, h in horas_por_mesa.items():
    print(f"  {mesa}  {h:>6.1f} h")

print(f"Total del area: {sum(horas_por_mesa.values()):.1f} h")

mesa_mas_cara = ""
mayor = 0.0
for mesa, h in horas_por_mesa.items():
    if h > mayor:
        mayor = h
        mesa_mas_cara = mesa

print(f"Mesa mas cara: {mesa_mas_cara} con {mayor:.1f} h")

print("Motivos del corte A")
for codigo in sorted(conteo):
    print(f"  {codigo}  {conteo[codigo]}")

codigos_a = set(reportados_a)
codigos_b = set(reportados_b)

print(f"En los dos cortes:       {sorted(codigos_a & codigos_b)}")
print(f"Solo en el corte A:      {sorted(codigos_a - codigos_b)}")
print(f"Nuevos en el corte B:    {sorted(codigos_b - codigos_a)}")
print(f"En uno pero no en ambos: {sorted(codigos_a ^ codigos_b)}")
```

El motivo nuevo del corte B es el M06, cliente que ya tiene crédito vigente, y ese es el que dispara una decisión de originación: si empezaron a llegar solicitudes de clientes que ya deben, la campaña está apuntando a la base equivocada y hay que revisar el filtro de la lista antes de seguir marcando.

El conteo del corte A no se podía hacer con un conjunto porque un conjunto elimina los repetidos, y lo que se quería saber era justamente cuántas veces se repitió cada motivo. El conjunto contesta cuáles hay, el diccionario contesta cuántos de cada uno.

**Salida**

```text
Horas-analista por mesa
  MC-01    86.4 h
  MC-02    61.5 h
  MC-03   112.8 h
  MC-04    48.2 h
Total del area: 308.9 h
Mesa mas cara: MC-03 con 112.8 h
Motivos del corte A
  M01  3
  M02  1
  M03  2
  M05  1
En los dos cortes:       ['M01', 'M02', 'M03']
Solo en el corte A:      ['M05']
Nuevos en el corte B:    ['M06']
En uno pero no en ambos: ['M05', 'M06']
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| El diccionario se construye con un ciclo desde las listas | 2 |
| El total sale de `values` y la mesa más cara de un recorrido | 2 |
| El contador usa `get` con valor por omisión de cero | 2 |
| Las cuatro comparaciones usan operaciones de conjuntos | 2 |
| Las dos conclusiones escritas | 2 |

**Error que más se ve**

Comparar los dos cortes con un ciclo y un `if` en lugar de operaciones de conjuntos: el resultado sale igual, ocupa quince líneas y falla en cuanto hay que contestar la cuarta pregunta, la de los que están en uno pero no en ambos.

---

## Semana 14 · Tema 7 · Archivos de texto y CSV

### 14.1 · Reconocer

**Solución**

```text
30
MC-01 18.10
<class 'str'>
18.1017.80
True
False
```

La cuarta línea no lanza error porque los dos valores son texto, y el `+` entre dos textos los pega. El resultado, `18.1017.80`, no es un número y aun así el programa sigue corriendo. Ese es el error de conversión más caro del semestre: no avisa.

La sexta línea da falso porque el tercer renglón del archivo trae la mesa escrita como `" MC-01"`, con un espacio al frente. Dos textos que se ven iguales en pantalla y difieren en un carácter son valores distintos, y por eso una agrupación por mesa reportaría nueve mesas donde hay cuatro.

Si esa misma apertura llevara `"w"`, el archivo se vaciaría en el instante de abrirlo, antes de leer nada. Los treinta renglones se perderían y después el programa fallaría al intentar leer un archivo abierto para escritura.

**Salida**

```text
30
MC-01 18.10
<class 'str'>
18.1017.80
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

Contestar `35.90` en la cuarta línea: se suman las dos tasas como si `DictReader` hubiera convertido los tipos, cuando un CSV solo guarda texto y nadie más va a convertirlo por ti.

### 14.2 · Aplicar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent


def a_decimal(texto):
    """Convierte a decimal quitando el signo de pesos y la coma de miles."""
    limpio = texto.replace("$", "").replace(",", "")
    return float(limpio.strip())


def a_entero(texto):
    """Convierte a entero. La celda vacia se reporta como ausencia con None."""
    texto = texto.strip()
    return int(texto) if texto else None


def normalizar(texto):
    """Deja una sola forma de escribir la mesa: sin espacios y en mayusculas."""
    return texto.strip().upper()


with (DATOS / "solicitudes.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

formas = set()
sin_horas = 0

for fila in filas:
    formas.add(fila["mesa"])
    if a_entero(fila["horas_resp"]) is None:
        sin_horas += 1

normalizadas = set()
for fila in filas:
    normalizadas.add(normalizar(fila["mesa"]))

print(f"Renglones leidos:              {len(filas)}")
print(f"Renglones sin horas de respuesta: {sin_horas}")
print(f"Formas de escribir la mesa:    {len(formas)}")
print(f"Mesas despues de normalizar:   {len(normalizadas)}")

comision = {}
cuenta = {}
suma_tasa = {}

for fila in filas:
    mesa = normalizar(fila["mesa"])
    comision[mesa] = comision.get(mesa, 0.0) + a_decimal(fila["comision_mxn"])
    cuenta[mesa] = cuenta.get(mesa, 0) + 1
    suma_tasa[mesa] = suma_tasa.get(mesa, 0.0) + float(fila["tasa_pct"])

print(f"{'Mesa':<10}{'Solicitudes':>13}{'Comision':>13}{'Tasa':>10}")

comision_total = 0.0
cuenta_total = 0

for mesa in sorted(comision):
    promedio = suma_tasa[mesa] / cuenta[mesa]
    comision_total += comision[mesa]
    cuenta_total += cuenta[mesa]
    print(f"{mesa:<10}{cuenta[mesa]:>13}{comision[mesa]:>13,.0f}{promedio:>10.4f}")

print(f"{'ALTAMAR':<10}{cuenta_total:>13}{comision_total:>13,.0f}")
```

`a_entero` devuelve `None` y no cero, porque unas horas de respuesta que no se capturaron no son una respuesta instantánea. La decisión de qué hacer con esa ausencia se toma en el ejercicio siguiente, no aquí.

Los diccionarios con `get` y un valor por omisión son la semana 13 aplicada: cada mesa aparece por primera vez sin que el programa tenga que saber de antemano cuántas hay.

**Salida**

```text
Renglones leidos:              30
Renglones sin horas de respuesta: 3
Formas de escribir la mesa:    9
Mesas despues de normalizar:   4
Mesa        Solicitudes     Comision      Tasa
MC-01                 9       11,325   18.0222
MC-02                 7        7,060   18.0714
MC-03                 8       12,125   18.1000
MC-04                 6        4,467   18.0833
ALTAMAR              30       34,977
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las tres funciones con docstring y responsabilidad única | 3 |
| Los cuatro renglones de diagnóstico correctos | 2 |
| La tabla por mesa y el total del área correctos | 3 |
| La ruta se arma con `pathlib` desde la ubicación del archivo | 1 |
| Lee por nombre de columna, no por posición | 1 |

**Error que más se ve**

Convertir la comisión con `float(fila["comision_mxn"])` directo: lanza `ValueError` en el primer renglón por el signo de pesos y la coma, y el alumno suele culpar al archivo en lugar de al formato.

### 14.3 · Integrar

**Solución**

```python
import csv
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50


def a_decimal(texto):
    """Convierte a decimal quitando el signo de pesos y la coma de miles."""
    limpio = texto.replace("$", "").replace(",", "")
    return float(limpio.strip())


def normalizar(texto):
    """Deja una sola forma de escribir la mesa: sin espacios y en mayusculas."""
    return texto.strip().upper()


def fuera_de_politica(tasa):
    """Dice si la tasa otorgada cae fuera de la banda de 17.50 a 18.50 por ciento."""
    return tasa < LIMITE_INFERIOR or tasa > LIMITE_SUPERIOR


with (DATOS / "solicitudes.csv").open(encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

vistos = set()
limpias = []

for fila in filas:
    huella = (fila["fecha"], fila["mesa"], fila["corte"],
              fila["tasa_pct"], fila["horas_resp"], fila["comision_mxn"])

    if huella in vistos:
        continue

    vistos.add(huella)
    limpias.append(fila)

comision = {}
cuenta = {}
fuera = {}
sin_horas = 0

for fila in limpias:
    mesa = normalizar(fila["mesa"])
    tasa = float(fila["tasa_pct"])

    comision[mesa] = comision.get(mesa, 0.0) + a_decimal(fila["comision_mxn"])
    cuenta[mesa] = cuenta.get(mesa, 0) + 1
    fuera[mesa] = fuera.get(mesa, 0)

    if fuera_de_politica(tasa):
        fuera[mesa] += 1

    if fila["horas_resp"].strip() == "":
        sin_horas += 1

print(f"Renglones en el archivo:     {len(filas)}")
print(f"Duplicados exactos quitados: {len(filas) - len(limpias)}")
print(f"Renglones que quedaron:      {len(limpias)}")
print(f"Renglones sin horas de respuesta conservados: {sin_horas}")
print(f"Solicitudes fuera de politica: {sum(fuera.values())}")
print(f"Comision del area:           {sum(comision.values()):,.0f} pesos")

salida = DATOS / "resumen_mesa.csv"

with salida.open("w", encoding="utf-8", newline="") as f:
    escritor = csv.writer(f)
    escritor.writerow(["mesa", "solicitudes", "fuera_politica", "comision_mxn"])

    for mesa in sorted(comision):
        escritor.writerow([mesa, cuenta[mesa], fuera[mesa],
                           round(comision[mesa], 1)])

print(f"Archivo escrito: {salida.name}")

with salida.open(encoding="utf-8") as f:
    print(f.read().strip())
```

La huella del renglón es una tupla con las seis columnas, y el conjunto de huellas es lo que detecta el duplicado exacto. Comparar solo por fecha y mesa habría borrado solicitudes legítimas de clientes distintos del mismo día.

Los 2,515 pesos de diferencia son la suma de los dos renglones duplicados: 1,260 del renglón de MC-01 del 9 de enero y 1,255 del de MC-01 del 12 de enero. Un duplicado infla la comisión porque el importe se suma dos veces, y casi no mueve la tasa promedio porque ahí el valor repetido entra en el numerador y en el denominador a la vez.

**Salida**

```text
Renglones en el archivo:     30
Duplicados exactos quitados: 2
Renglones que quedaron:      28
Renglones sin horas de respuesta conservados: 3
Solicitudes fuera de politica: 8
Comision del area:           32,462 pesos
Archivo escrito: resumen_mesa.csv
mesa,solicitudes,fuera_politica,comision_mxn
MC-01,7,3,8810.0
MC-02,7,1,7060.0
MC-03,8,4,12125.0
MC-04,6,0,4467.0
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los duplicados se detectan comparando el renglón completo | 2 |
| Las seis cifras de bitácora correctas | 3 |
| El archivo de salida tiene el encabezado y los cuatro renglones pedidos | 2 |
| Se escribe con `newline` vacío y sin renglones en blanco | 1 |
| Explica la diferencia exacta de 2,515 pesos | 2 |

**Error que más se ve**

Detectar duplicados solo por fecha y mesa: se borran solicitudes de clientes distintos, el conteo baja de 28 a 18 y la comisión total queda muy por debajo sin que nada lo señale.

---

## Semana 15 · Tema 8.1 · Series, DataFrame, limpieza y agrupación

### 15.1 · Reconocer

**Solución**

`shape` da `(30, 6)`. Los tipos: `fecha`, `mesa`, `corte` y `comision_mxn` salen texto, `tasa_pct` y `horas_resp` salen `float64`. Hay 3 valores faltantes en `horas_resp`, 2 renglones duplicados y 9 formas distintas de escribir la mesa.

`horas_resp` salió decimal y no entero porque tres celdas están vacías, y el marcador de ausencia solo existe en una columna decimal. No es una falla de pandas: es el precio de que la columna tenga huecos, y por eso las horas se imprimen como 44.0 en lugar de 44.

`comision_mxn` salió texto porque el signo de pesos y la coma de miles son formato, no valor. Mientras estén ahí, esa columna no puede sumarse.

En `value_counts` hay dos renglones que se ven idénticos, `MC-01` y `MC-01 `, y son entradas distintas porque uno trae un espacio al final. Ese espacio no se ve en pantalla y sí parte los grupos.

`describe` solo resume `tasa_pct` y `horas_resp`, que son las dos columnas numéricas. Las otras cuatro son texto para pandas, incluida la fecha, y por eso quedan fuera.

**Salida**

```text
(30, 6)
fecha               str
mesa                str
corte               str
tasa_pct        float64
horas_resp      float64
comision_mxn        str
dtype: object
3
2
9
mesa
MC-03     7
MC-01     6
MC-02     6
MC-04     6
 MC-01    1
mc-01     1
MC-01     1
mc-02     1
MC-03     1
Name: count, dtype: int64
count    30.000
mean     18.067
std       0.465
min      17.100
25%      17.725
50%      18.100
75%      18.400
max      18.900
Name: tasa_pct, dtype: float64
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las siete salidas correctas, con los tipos de las seis columnas | 3 |
| Explica el `float64` de `horas_resp` por los faltantes | 2 |
| Explica el texto de `comision_mxn` por el signo y la coma | 2 |
| Detecta los dos renglones que se ven iguales en `value_counts` | 2 |
| Dice qué columnas resume `describe` y por qué | 1 |

**Error que más se ve**

Decir que `horas_resp` salió decimal porque las horas traen fracciones: en el archivo todas son enteras, y quien no revisa `isna` nunca se entera de que la causa son las tres celdas vacías.

### 15.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50

solicitudes = pd.read_csv(DATOS / "solicitudes.csv")

print(f"Al cargar:              {len(solicitudes)} renglones")
print(f"Duplicados exactos:     {solicitudes.duplicated().sum()}")
print(f"Formas de la mesa:      {solicitudes['mesa'].nunique()}")
print(f"Sin horas de respuesta: {solicitudes['horas_resp'].isna().sum()}")

solicitudes = solicitudes.drop_duplicates()
print(f"Sin duplicados:         {len(solicitudes)} renglones")

solicitudes["mesa"] = solicitudes["mesa"].str.strip().str.upper()
print(f"Mesas reales:           {solicitudes['mesa'].nunique()}")

solicitudes["comision_mxn"] = (solicitudes["comision_mxn"]
                               .str.replace("$", "", regex=False)
                               .str.replace(",", "", regex=False)
                               .str.strip()
                               .astype(float))

solicitudes["fecha"] = pd.to_datetime(solicitudes["fecha"])

print(solicitudes.dtypes)

solicitudes["veredicto"] = "Dentro de politica"
solicitudes.loc[(solicitudes["tasa_pct"] < LIMITE_INFERIOR) |
                (solicitudes["tasa_pct"] > LIMITE_SUPERIOR),
                "veredicto"] = "Fuera de politica"

print(solicitudes["veredicto"].value_counts())

criticas = solicitudes[(solicitudes["mesa"] == "MC-03") &
                       (solicitudes["veredicto"] == "Fuera de politica")]
print(f"MC-03 fuera de politica: {len(criticas)}")

primeras = solicitudes[solicitudes["mesa"].isin(["MC-01", "MC-02"])]
print(f"Solicitudes de MC-01 y MC-02: {len(primeras)}")

print(f"Comision total:         {solicitudes['comision_mxn'].sum():,.0f} pesos")
print(f"Horas promedio:         {solicitudes['horas_resp'].mean():.2f} h")
print(f"Renglones si se descartan los tres sin horas: "
      f"{len(solicitudes.dropna(subset=['horas_resp']))}")
```

Descartar los tres renglones sin horas de respuesta dejaría 25 solicitudes. Conviene conservarlos porque el dato que decide si el precio cumple es la tasa, y esa sí quedó capturada en los tres casos. Tirarlos costaría tres tasas buenas para no perder tres tiempos de respuesta, y el promedio de horas se puede calcular con las 25 que sí lo traen sin necesidad de borrar nada.

**Salida**

```text
Al cargar:              30 renglones
Duplicados exactos:     2
Formas de la mesa:      9
Sin horas de respuesta: 3
Sin duplicados:         28 renglones
Mesas reales:           4
fecha           datetime64[us]
mesa                       str
corte                      str
tasa_pct               float64
horas_resp             float64
comision_mxn           float64
dtype: object
veredicto
Dentro de politica    20
Fuera de politica      8
Name: count, dtype: int64
MC-03 fuera de politica: 4
Solicitudes de MC-01 y MC-02: 14
Comision total:         32,462 pesos
Horas promedio:         44.36 h
Renglones si se descartan los tres sin horas: 25
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Las seis cifras de la bitácora correctas | 3 |
| Las cuatro reparaciones aplicadas en orden y los tipos finales correctos | 2 |
| La columna `veredicto` se escribe con `loc` en un solo paso | 2 |
| Los tres filtros dan 4, 14 y los totales correctos | 2 |
| Justifica por escrito la decisión sobre los renglones sin horas | 1 |

**Error que más se ve**

Escribir la columna con `solicitudes[solicitudes[...]]["veredicto"] = ...`: la asignación encadenada no hace nada, la columna queda completa en «Dentro de política» y el conteo sale 28 y 0 sin que se lance ningún error.

### 15.3 · Integrar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50


def cargar_limpio():
    """Carga solicitudes.csv y le aplica las cuatro reparaciones de la sesion 15.2."""
    datos = pd.read_csv(DATOS / "solicitudes.csv").drop_duplicates()

    datos["mesa"] = datos["mesa"].str.strip().str.upper()
    datos["comision_mxn"] = (datos["comision_mxn"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .str.strip()
                             .astype(float))
    datos["fecha"] = pd.to_datetime(datos["fecha"])

    datos["veredicto"] = "Dentro de politica"
    datos.loc[(datos["tasa_pct"] < LIMITE_INFERIOR) |
              (datos["tasa_pct"] > LIMITE_SUPERIOR),
              "veredicto"] = "Fuera de politica"

    return datos


solicitudes = cargar_limpio()

tablero = solicitudes.groupby("mesa").agg(
    solicitudes=("tasa_pct", "count"),
    comision=("comision_mxn", "sum"),
    horas=("horas_resp", "mean"),
    tasa=("tasa_pct", "mean"),
).round(3)

print(tablero.sort_values("comision", ascending=False))

fuera = solicitudes[solicitudes["veredicto"] == "Fuera de politica"]
print(fuera.groupby("mesa").size())

rejilla = solicitudes.pivot_table(index="mesa", columns="corte",
                                  values="comision_mxn", aggfunc="sum",
                                  fill_value=0, margins=True)
print(rejilla.round(0))

catalogo = pd.DataFrame({
    "mesa": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "plaza": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "horas_meta": [42, 40, 48, 36, 30],
})

auditoria = solicitudes.merge(catalogo, on="mesa", how="outer", indicator=True)
print(auditoria["_merge"].value_counts())

unida = tablero.reset_index().merge(catalogo, on="mesa", how="left")
unida["desvio_horas"] = (unida["horas"] / unida["horas_meta"] - 1)

print(unida[["mesa", "plaza", "solicitudes", "horas",
             "horas_meta", "desvio_horas"]].round(3))
```

La tabla de solicitudes fuera de política trae tres renglones y no cuatro porque MC-04 no aportó ninguna. `groupby` solo devuelve los grupos que existen en los datos que recibió, y una mesa sin solicitudes fuera simplemente no aparece. Si esa tabla se va a usar en una resta o en una división, hay que rellenar el cero a propósito.

La auditoría de la unión: 28 renglones cruzaron en ambos lados, 1 quedó solo del catálogo y 0 solo de las solicitudes. El del catálogo es MC-05, la plaza de Mérida, que ya está dada de alta y no colocó nada esta semana: eso está bien y se explica solo. Los cero del otro lado son la cifra importante: ninguna solicitud quedó huérfana, o sea que el archivo no trae ninguna mesa desconocida. Si ese número no fuera cero, habría que reportarlo antes de publicar cualquier total.

MC-01 corre 6.7 % arriba de su meta de tiempo de respuesta y MC-03 6.2 %, mientras MC-02 apenas 1.2 %. A la dirección de operaciones se le reporta que dos de las cuatro mesas están tardando alrededor de tres horas más de lo que dice el estándar en cada solicitud, y que en MC-03 esas tres horas se acumulan sobre el tiempo de respuesta más largo del área.

**Salida**

```text
       solicitudes  comision   horas    tasa
mesa                                        
MC-03            8   12125.0  51.000  18.100
MC-01            7    8810.0  44.833  17.986
MC-02            7    7060.0  40.500  18.071
MC-04            6    4467.0  37.800  18.083
mesa
MC-01    3
MC-02    1
MC-03    4
dtype: int64
corte   C-2601   C-2602  C-2603      All
mesa                                    
MC-01   3740.0   2485.0  2585.0   8810.0
MC-02   1990.0   2055.0  3015.0   7060.0
MC-03   4690.0   4540.0  2895.0  12125.0
MC-04   1490.0   1500.0  1477.0   4467.0
All    11910.0  10580.0  9972.0  32462.0
_merge
both          28
right_only     1
left_only      0
Name: count, dtype: int64
    mesa        plaza  solicitudes   horas  horas_meta  desvio_horas
0  MC-01    Monterrey            7  44.833          42         0.067
1  MC-02  Guadalajara            7  40.500          40         0.012
2  MC-03         Leon            8  51.000          48         0.062
3  MC-04       Puebla            6  37.800          36         0.050
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La limpieza queda encerrada en una función con docstring | 1 |
| El tablero de cuatro resúmenes sale en una sola instrucción | 2 |
| Explica por qué la tabla de fuera de política trae tres renglones | 2 |
| La rejilla con totales de fila y columna es correcta | 2 |
| La unión se audita en las dos direcciones y se interpretan los tres números | 2 |
| El tablero de desvío de tiempo de respuesta es correcto y se reporta | 1 |

**Error que más se ve**

Unir con `inner` en lugar de `left` para el tablero: con estos datos el resultado no cambia, y por eso el alumno se acostumbra a un modo que en cuanto falte una mesa en el catálogo va a borrar renglones en silencio.

---

## Semana 16 · Tema 8.2 · Visualización con matplotlib y seaborn

### 16.1 · Reconocer

**Solución**

La barra muestra la comisión promedio por solicitud, porque `barplot` promedia cuando no se le dice otra cosa. Para MC-01 la barra vale 1,258.6 pesos. Lo que dice el asunto del correo, la comisión del corte, son 8,810 pesos, siete veces más. Los dos números son correctos y contestan preguntas distintas: uno es cuánto dejó cada solicitud en promedio, el otro cuánto dejó la mesa.

Para que la barra muestre el total hay que agregar `estimator="sum"`, y con eso conviene agregar `errorbar=None`, porque el intervalo que dibuja encima de cada barra no significa nada en un reporte de ingresos.

Las cuatro gráficas:

- Comisión de las cuatro mesas: barras, porque compara categorías que no tienen orden natural. Ordenadas de mayor a menor, el ranking se lee solo.
- Reparto de las tasas dentro de cada mesa: caja y bigotes, porque la pregunta no es el centro sino la forma, y ahí es donde se ve la dispersión que el promedio esconde.
- Tasa promedio a lo largo de los tres días: línea, porque el eje horizontal es tiempo y conectar dos fechas sí afirma algo cierto.
- Horas de respuesta contra desvío de precio: dispersión, porque pregunta si dos variables numéricas se mueven juntas.

**Salida**

```text
           sum    mean  count
mesa                         
MC-03  12125.0  1515.6      8
MC-01   8810.0  1258.6      7
MC-02   7060.0  1008.6      7
MC-04   4467.0   744.5      6
          mean     std   min   max
mesa                              
MC-04  18.0833  0.3430  17.6  18.5
MC-02  18.0714  0.4348  17.5  18.7
MC-01  17.9857  0.4880  17.3  18.6
MC-03  18.1000  0.6459  17.1  18.9
mesa
MC-01    3
MC-02    1
MC-03    4
dtype: int64
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Identifica que la barra muestra el promedio y da las dos cifras de MC-01 | 3 |
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

solicitudes = cargar_limpio()

comision = (solicitudes.groupby("mesa")["comision_mxn"]
            .sum()
            .sort_values(ascending=False))

print(comision)

pico = comision.index[0]
parte = comision.iloc[0] / comision.sum()

print(f"{pico} concentra {parte:.1%} de la comision del area")

fig, ax = plt.subplots(figsize=(9, 5))

barras = ax.bar(comision.index, comision.values, color="#C7D6E8")
barras[0].set_color("#2B5F8F")

ax.set_title(f"{pico} concentra el {parte:.0%} de la comision del area de originacion")
ax.set_ylabel("Comision por apertura del corte (pesos)")
ax.set_ylim(0, 13000)
ax.yaxis.set_major_formatter(
    ticker.FuncFormatter(lambda v, _: f"{v / 1000:.0f}k"))

fig.text(0.01, 0.01,
         "Fuente: solicitudes.csv, Financiera Altamar, 8 al 12 de enero de 2026",
         fontsize=8)

fig.savefig(SALIDA / "comision_mesa.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Archivo generado:", (SALIDA / "comision_mesa.png").exists())
```

La función `cargar_limpio` es la de 15.3, guardada en un archivo `limpieza.py` al lado de los programas de esta semana, para no volver a copiar la limpieza en cada gráfica.

Texto alternativo: gráfica de barras de la comisión por apertura que dejó cada una de las cuatro mesas de Financiera Altamar entre el 8 y el 12 de enero de 2026. MC-03 encabeza con 12,125 pesos, seguida de MC-01 con 8,810, MC-02 con 7,060 y MC-04 con 4,467. MC-03 sola representa el 37 % de los 32,462 pesos del área y deja 2.7 veces lo de MC-04.

**Salida**

```text
mesa
MC-03    12125.0
MC-01     8810.0
MC-02     7060.0
MC-04     4467.0
Name: comision_mxn, dtype: float64
MC-03 concentra 37.4% de la comision del area
Archivo generado: True
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| La serie por mesa es correcta y está ordenada | 2 |
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

solicitudes = cargar_limpio()

resumen = solicitudes.groupby("mesa")["tasa_pct"].agg(
    ["mean", "median", "std", "count"]).round(4)
print(resumen.sort_values("std"))

fig, ax = plt.subplots(figsize=(9, 5))
sns.barplot(data=solicitudes, x="mesa", y="comision_mxn", estimator="sum",
            errorbar=None, hue="mesa", legend=False, ax=ax)
ax.set_title("MC-03 deja 2.7 veces la comision de MC-04 en el mismo corte")
ax.set_ylabel("Comision por apertura del corte (pesos)")
fig.savefig(SALIDA / "barras_comision.png", dpi=150, bbox_inches="tight")
plt.close(fig)

orden = (solicitudes.groupby("mesa")["tasa_pct"]
         .std().sort_values().index)

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=solicitudes, x="mesa", y="tasa_pct", order=orden,
            hue="mesa", legend=False, ax=ax)
ax.axhline(17.50, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(18.50, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("MC-01 es la mas cercana a la tasa de politica y aun asi se sale de la banda")
ax.set_ylabel("Tasa otorgada (%)")
fig.savefig(SALIDA / "caja_mesa.png", dpi=150, bbox_inches="tight")
plt.close(fig)

rejilla = solicitudes.pivot_table(index="mesa", columns="corte",
                                  values="comision_mxn", aggfunc="sum",
                                  fill_value=0) / 1000
print(rejilla.round(2))

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(rejilla, annot=True, fmt=".1f", cmap="Blues", ax=ax)
ax.set_title("El corte C-2601 de MC-03 es la celda mas rentable del tablero")
fig.savefig(SALIDA / "mapa_mesa_corte.png", dpi=150, bbox_inches="tight")
plt.close(fig)

for nombre in ["barras_comision.png", "caja_mesa.png", "mapa_mesa_corte.png"]:
    print(nombre, (SALIDA / nombre).exists())
```

La conclusión de las tres juntas: MC-03 es la mesa que más deja y la más suelta con el precio a la vez, con 12,125 pesos de comisión, la dispersión más alta con 0.6459 puntos y 4 de las 8 solicitudes fuera de banda. MC-01 tiene el promedio más cercano a la tasa de política, 17.9857 %, y aun así 3 solicitudes fuera, porque su dispersión es la segunda más alta con 0.4880. MC-04 es la que mejor apega el precio: 0.3430 de dispersión y ninguna solicitud fuera de banda, aunque también es la que menos coloca.

A la dirección de operaciones se manda la caja y bigotes. Las barras dicen cuánto deja cada mesa y el mapa dice en qué corte, pero la caja es la única que muestra que un promedio pegado a la política no significa un proceso de cotización disciplinado, que es justo lo que hay que corregir en MC-01.

**Salida**

```text
          mean  median     std  count
mesa                                 
MC-04  18.0833   18.15  0.3430      6
MC-02  18.0714   18.10  0.4348      7
MC-01  17.9857   18.10  0.4880      7
MC-03  18.1000   18.10  0.6459      8
corte  C-2601  C-2602  C-2603
mesa                         
MC-01    3.74    2.48    2.58
MC-02    1.99    2.06    3.02
MC-03    4.69    4.54    2.90
MC-04    1.49    1.50    1.48
barras_comision.png True
caja_mesa.png True
mapa_mesa_corte.png True
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
$1,240$980
17.8
```

Línea 1, agrupar antes de limpiar. Salen 9 mesas donde hay 4, porque los espacios y las minúsculas todavía parten los grupos. El resultado correcto es 4.

Línea 2, asignación encadenada. La columna nunca se creó. Desde pandas 3.0 la operación no hace nada y no lanza error, solo una advertencia que es fácil pasar por alto. Lo correcto es `solicitudes.loc[condicion, "veredicto"] = "Revisar"`.

Línea 3, confundir modificar con devolver. `sort` ordena la lista y devuelve `None`, así que la asignación borró los datos. Lo correcto es `sorted(tasas)` o llamar a `tasas.sort()` sin asignar.

Línea 4, acumulador declarado adentro. Sale 48.2, que es la última carga de trabajo. El total correcto es 308.9.

Línea 5, calcular sin convertir. Los dos valores son texto y el `+` los pega. El resultado correcto, después de convertir, es 2,220 pesos.

Línea 6, contar desde uno. `solicitudes["tasa_pct"][1]` devuelve 17.8, que es el segundo renglón del archivo. La pregunta era por el primero, que se colocó a 18.10 y está en el índice 0.

El programa no se detiene en ninguna de las seis porque las seis son operaciones válidas de Python sobre datos válidos. Ninguna es un error de sintaxis ni de tipo: son respuestas correctas a preguntas que nadie hizo.

**Salida**

```text
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series
through chained assignment.
  solicitudes[solicitudes["mesa"] == "MC-03"]["veredicto"] = "Revisar"
9
False
None
48.2
$1,240$980
17.8
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

Contestar 4 en la primera línea porque en el área hay cuatro mesas: se contesta con lo que se sabe de la operación en lugar de con lo que trae el archivo, y ese es el mismo reflejo que hace que nadie revise un total sucio.

### 17.2 · Aplicar

**Solución**

```python
import pandas as pd
from pathlib import Path

DATOS = Path(__file__).resolve().parent
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50

solicitudes = pd.read_csv(DATOS / "solicitudes.csv")

print(f"Renglones:              {len(solicitudes)}")
print(f"Duplicados:             {solicitudes.duplicated().sum()}")
print(f"Formas de la mesa:      {solicitudes['mesa'].nunique()}")
print(f"Sin horas de respuesta: {solicitudes['horas_resp'].isna().sum()}")

solicitudes = solicitudes.drop_duplicates()
solicitudes["mesa"] = solicitudes["mesa"].str.strip().str.upper()
solicitudes["comision_mxn"] = (solicitudes["comision_mxn"]
                               .str.replace("$", "", regex=False)
                               .str.replace(",", "", regex=False)
                               .str.strip()
                               .astype(float))

solicitudes["veredicto"] = "Dentro de politica"
solicitudes.loc[(solicitudes["tasa_pct"] < LIMITE_INFERIOR) |
                (solicitudes["tasa_pct"] > LIMITE_SUPERIOR),
                "veredicto"] = "Fuera de politica"

tablero = solicitudes.groupby("mesa").agg(
    solicitudes=("tasa_pct", "count"),
    comision=("comision_mxn", "sum"),
    tasa=("tasa_pct", "mean"),
    dispersion=("tasa_pct", "std"),
)
tablero["fuera"] = (solicitudes[solicitudes["veredicto"] == "Fuera de politica"]
                    .groupby("mesa").size()
                    .reindex(tablero.index, fill_value=0))
tablero["proporcion"] = tablero["fuera"] / tablero["solicitudes"]

print(tablero.round(4).sort_values("comision", ascending=False))

peor = tablero["proporcion"].idxmax()
parte_comision = tablero.loc[peor, "comision"] / tablero["comision"].sum()
parte_fuera = tablero.loc[peor, "fuera"] / tablero["fuera"].sum()

print(f"{peor} deja el {parte_comision:.1%} de la comision del area "
      f"y concentra el {parte_fuera:.0%} de las solicitudes fuera de politica.")
```

El `reindex` con relleno en cero es lo que evita que MC-04 quede vacía en la columna de solicitudes fuera. Sin él, la proporción de esa mesa saldría como dato faltante y la división del final daría un resultado sin sentido. Quien no conozca `reindex` puede llegar al mismo tablero uniendo la cuenta y rellenando con `fillna(0)`, y las dos rutas se califican igual.

**Salida**

```text
Renglones:              30
Duplicados:             2
Formas de la mesa:      9
Sin horas de respuesta: 3
       solicitudes  comision     tasa  dispersion  fuera  proporcion
mesa                                                                
MC-03            8   12125.0  18.1000      0.6459      4      0.5000
MC-01            7    8810.0  17.9857      0.4880      3      0.4286
MC-02            7    7060.0  18.0714      0.4348      1      0.1429
MC-04            6    4467.0  18.0833      0.3430      0      0.0000
MC-03 deja el 37.4% de la comision del area y concentra el 50% de las solicitudes fuera de politica.
```

**Rúbrica** (suma 10)

| Criterio | Puntos |
|---|---|
| Los cuatro renglones de inspección antes de tocar nada | 2 |
| La limpieza completa y en el orden correcto | 2 |
| El tablero con las seis columnas correctas | 3 |
| La mesa sin solicitudes fuera aparece con cero y no vacía | 1 |
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
LIMITE_INFERIOR = 17.50
LIMITE_SUPERIOR = 18.50


def marcar_veredicto(datos):
    """Agrega la columna veredicto segun la banda de 17.50 a 18.50 por ciento."""
    datos["veredicto"] = "Dentro de politica"
    datos.loc[(datos["tasa_pct"] < LIMITE_INFERIOR) |
              (datos["tasa_pct"] > LIMITE_SUPERIOR),
              "veredicto"] = "Fuera de politica"
    return datos


def cargar_limpio():
    """Carga solicitudes.csv, quita duplicados, normaliza y convierte tipos."""
    datos = pd.read_csv(DATOS / "solicitudes.csv").drop_duplicates()

    datos["mesa"] = datos["mesa"].str.strip().str.upper()
    datos["comision_mxn"] = (datos["comision_mxn"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .str.strip()
                             .astype(float))
    datos["fecha"] = pd.to_datetime(datos["fecha"])

    return marcar_veredicto(datos)


crudo = marcar_veredicto(pd.read_csv(DATOS / "solicitudes.csv"))
limpio = cargar_limpio()

fuera_crudo = (crudo["veredicto"] == "Fuera de politica").sum()
fuera_limpio = (limpio["veredicto"] == "Fuera de politica").sum()

print(f"Sin limpiar: {fuera_crudo} de {len(crudo)} fuera de politica "
      f"({fuera_crudo / len(crudo):.1%})")
print(f"Ya limpio:   {fuera_limpio} de {len(limpio)} fuera de politica "
      f"({fuera_limpio / len(limpio):.1%})")

tablero = limpio.groupby("mesa").agg(
    solicitudes=("tasa_pct", "count"),
    comision=("comision_mxn", "sum"),
    tasa=("tasa_pct", "mean"),
    dispersion=("tasa_pct", "std"),
).round(4)

print(tablero.sort_values("dispersion", ascending=False))

catalogo = pd.DataFrame({
    "mesa": ["MC-01", "MC-02", "MC-03", "MC-04", "MC-05"],
    "plaza": ["Monterrey", "Guadalajara", "Leon", "Puebla", "Merida"],
    "horas_meta": [42, 40, 48, 36, 30],
})

auditoria = limpio.merge(catalogo, on="mesa", how="outer", indicator=True)
print(auditoria["_merge"].value_counts())

sns.set_theme(style="whitegrid", palette="deep")

orden = tablero.sort_values("dispersion").index

fig, ax = plt.subplots(figsize=(9, 5))
sns.boxplot(data=limpio, x="mesa", y="tasa_pct", order=orden,
            hue="mesa", legend=False, ax=ax)
ax.axhline(LIMITE_INFERIOR, color="#B4462C", linestyle="--", linewidth=1)
ax.axhline(LIMITE_SUPERIOR, color="#B4462C", linestyle="--", linewidth=1)
ax.set_title("MC-03 es la unica mesa cuyo cuartil superior rebasa el 18.50 %")
ax.set_ylabel("Tasa otorgada (%)")
fig.text(0.01, 0.01, "Fuente: solicitudes.csv, Financiera Altamar, enero de 2026",
         fontsize=8)
fig.savefig(DATOS / "dispersion_mesa.png", dpi=150, bbox_inches="tight")
plt.close(fig)

print("Grafica generada:", (DATOS / "dispersion_mesa.png").exists())
```

El numerador no cambia porque los dos renglones duplicados son solicitudes que estaban dentro de política: 17.90 y 18.40. El denominador sí baja, de 30 a 28, y por eso la proporción sube de 26.7 % a 28.6 %. A control interno se le reporta la del archivo limpio: 8 de 28, porque un registro repetido no es una solicitud repetida y contarlo dos veces diluye el problema.

El cuartil superior de MC-03 está en 18.65 %, arriba del límite de 18.50. Eso significa que más de una cuarta parte de lo que coloca esa mesa se sale por el lado caro, y no por casos aislados sino por dónde está parada toda su distribución de precio.

A la dirección de operaciones se le pide revisar el proceso de cotización de MC-03, y se sostiene con dos cifras: dispersión de 0.6459 puntos contra 0.3430 de MC-04, y 4 de las 8 solicitudes fuera de banda de toda el área. El dato que falta en este archivo para afirmar la causa es el monto y el perfil de riesgo de cada crédito: sin saber si el sobreprecio corresponde a clientes de mayor riesgo, se puede señalar la mesa, no el motivo.

**Salida**

```text
Sin limpiar: 8 de 30 fuera de politica (26.7%)
Ya limpio:   8 de 28 fuera de politica (28.6%)
       solicitudes  comision     tasa  dispersion
mesa                                             
MC-03            8   12125.0  18.1000      0.6459
MC-01            7    8810.0  17.9857      0.4880
MC-02            7    7060.0  18.0714      0.4348
MC-04            6    4467.0  18.0833      0.3430
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
| Las dos proporciones correctas y la explicación del numerador y el denominador | 2 |
| El tablero ordenado por dispersión es correcto | 2 |
| La auditoría de la unión con sus tres conteos | 1 |
| La gráfica lleva orden, banda, título con hallazgo y fuente | 2 |
| El cierre trae las dos cifras y nombra el dato faltante | 1 |

**Error que más se ve**

Reportar la proporción del archivo sin limpiar porque «es la que trae el sistema»: 26.7 % contra 28.6 % parece una diferencia menor, y es exactamente el tipo de dilución que hace que un problema de una mesa se vea como ruido del área.
