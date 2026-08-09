"""notebooks/analisis-de-datos/{es,en}/w04.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w04.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 4
## Datos, tipos y operaciones primitivas

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Un código postal está hecho de dígitos y no es un número. Un folio también. Esta sesión trata de
por qué esa distinción cuesta tardes enteras cuando nadie la dice a tiempo.

Al terminar este cuaderno vas a poder:

1. Declarar variables con nombres que digan qué guardan.
2. Reconocer los cinco tipos que vas a usar todo el semestre.
3. Usar los siete operadores aritméticos y los ocho de asignación.
4. Resolver una expresión en el orden correcto, y saber cuándo hacen falta paréntesis.
5. Convertir entre tipos y explicar por qué Python no lo hace solo.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.

El caso de toda la sesión es una campaña de marketing digital: 148 230 impresiones, 5 074 clics
y 38 500 pesos de inversión.
"""),

md("""
---
# Bloque 1 · Variables y tipos

Una variable guarda un valor y se le llama de alguna forma para volver a encontrarlo. La
diferencia con una celda es doble: **el nombre lo eliges tú y dice qué guarda**, y **el valor
tiene un tipo que Python respeta al pie de la letra**.

`B7` no dice nada. `inversion_campana` sí.

## Los cinco tipos

| Tipo | Qué guarda | Ejemplo de campaña |
|---|---|---|
| `int` | Enteros, sin límite de tamaño | `impresiones = 148230` |
| `float` | Decimales, con precisión limitada | `tasa_conversion = 0.0342` |
| `str` | Texto, siempre entre comillas | `canal = "Instagram"` |
| `bool` | Verdadero o falso, nada intermedio | `campana_activa = True` |
| `NoneType` | La ausencia de un valor | `costo_por_clic = None` |
"""),

code("""
canal = "Instagram"
impresiones = 148230
clics = 5074
inversion = 38500.00
campana_activa = True
costo_por_clic = None

print(type(canal), type(impresiones))
print(type(inversion), type(campana_activa))
print(type(costo_por_clic))
"""),

md("""
`type` devuelve el tipo de un valor. Sirve para verificar qué entendió Python, no para el
programa final.

Fíjate en `inversion`: el punto decimal la vuelve `float` aunque los centavos sean cero.
`38500.00` es decimal y `38500` es entero, y la diferencia importa cuando divides.

## El nombre no tiene tipo, el valor sí

Esta es la parte que sorprende a quien viene de un lenguaje más estricto, y la que muerde a
quien viene de Excel.
"""),

code("""
dato = 148230
print(dato, type(dato))

dato = "148230"
print(dato, type(dato))

dato = None
print(dato, type(dato))
"""),

md("""
La misma variable guardó un entero, luego un texto, luego nada. Python no se quejó en ningún
momento.

Se va a quejar después, cuando alguien opere con ella esperando lo que ya no es. Ese retraso
entre el error y el síntoma es lo que hace difícil encontrarlo.
"""),

code("""
# FALLA A PROPÓSITO. El error aparece tres líneas después de la causa.
tasa_objetivo = "0.03"          # <- aquí está el problema, y no truena

print("El programa sigue corriendo...")
print("Y sigue...")

try:
    print(tasa_objetivo * 100)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
"""),

md("""
No lanzó error. `"0.03" * 100` repite el texto cien veces, porque multiplicar un texto por un
entero es una operación legítima en Python.

Corre la celda y mira la salida. Eso es lo que llega a tu reporte si nadie revisa el tipo.

## `None` no es cero

`None` es la ausencia de un dato y cero es un valor medido. Confundirlos cambia cualquier
promedio.
"""),

code("""
print("None == 0 ?", None == 0)
print("bool(None) ?", bool(None))
print("bool(0)    ?", bool(0))

# FALLA A PROPÓSITO. Sumar None no es sumar cero.
try:
    print(costo_por_clic + 10)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Un `costo_por_clic` en `None` significa "todavía no lo medimos". Un cero significa "lo medimos y
salió cero, la campaña no costó nada". Son afirmaciones distintas, y el promedio de una columna
cambia según cuál sea.

Es exactamente el mismo problema que las once celdas vacías de `sales.csv` en la semana 15,
sembrado once semanas antes.
"""),

md("""
---
# Bloque 2 · Los operadores, completos

Siete aritméticos y ocho de asignación. Van todos, no solo los que se usan a diario, porque una
tabla parcial enseña que el resto no existe.

## Los cuatro que ya usas

| Operador | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `5074 + 320` | `5394` |
| `-` | Resta | `5074 - 320` | `4754` |
| `*` | Producto | `5074 * 2` | `10148` |
| `/` | División decimal | `5074 / 4` | `1268.5` |
"""),

code("""
print(5074 + 320)
print(5074 - 320)
print(5074 * 2)
print(5074 / 4)
"""),

md("""
Nota que `/` siempre devuelve decimal, aunque la división sea exacta.
"""),

code("""
print(10 / 2, type(10 / 2))
print(10 / 5, type(10 / 5))
"""),

md("""
## Los tres que Excel no tiene así

| Operador | Qué hace | Ejemplo | Resultado |
|---|---|---|---|
| `//` | División entera | `5074 // 4` | `1268` |
| `%` | Residuo | `5074 % 4` | `2` |
| `**` | Potencia | `2 ** 10` | `1024` |
"""),

code("""
print("División entera:", 5074 // 4)
print("Residuo:        ", 5074 % 4)
print("Potencia:       ", 2 ** 10)
print()
print("Comprobación:", 1268 * 4 + 2, "== 5074")
"""),

md("""
`//` y `%` son las dos mitades de una división con resto, y juntas reconstruyen el número
original. Sirven más de lo que parece: repartir cosas en grupos, saber si un número es par, o
sacar el día de la semana.
"""),

code("""
# ¿Cuántos anuncios completos caben, y cuántas impresiones sobran?
impresiones = 148230
por_anuncio = 7

print("Anuncios completos:", impresiones // por_anuncio)
print("Impresiones sueltas:", impresiones % por_anuncio)
print()
print("¿148230 es par?", impresiones % 2 == 0)
"""),

md("""
## Guardar, y las siete abreviaturas

| Operador | Equivale a | Ejemplo |
|---|---|---|
| `=` | Guardar un valor | `clics = 5074` |
| `+=` | `x = x + y` | `clics += 320` |
| `-=` | `x = x - y` | `clics -= 12` |
| `*=` | `x = x * y` | `inversion *= 1.16` |
| `/=` | `x = x / y` | `inversion /= 30` |
| `//=` | `x = x // y` | `impresiones //= 1000` |
| `%=` | `x = x % y` | `posicion %= 7` |
| `**=` | `x = x ** y` | `base **= 2` |

Las ocho, corriendo, para que no queden como una lista que memorizar.
"""),

code("""
clics = 5074
print("Inicio:", clics)

clics += 320
print("+= 320:", clics)

clics -= 12
print("-= 12: ", clics)

clics *= 2
print("*= 2:  ", clics)

clics /= 4
print("/= 4:  ", clics, "<- ojo, se volvió float")
"""),

code("""
impresiones = 148230
impresiones //= 1000
print("//= 1000:", impresiones, type(impresiones))

posicion = 23
posicion %= 7
print("%= 7:   ", posicion)

base = 12
base **= 2
print("**= 2:  ", base)
"""),

md("""
Fíjate en el `/=`: convirtió un entero en decimal. `//=` no. Esa diferencia se cuela en reportes
donde de pronto todo se imprime con `.0` al final.
"""),

md("""
---
## La precedencia, y por qué los paréntesis cuestan cero

El orden en que Python resuelve una expresión es el de las matemáticas y el de Excel. Nada nuevo
que memorizar:

1. Paréntesis
2. Potencia
3. `*` `/` `//` `%`
4. `+` `-`

Y aquí está por qué importa.
"""),

code("""
inversion = 38500
clics = 5074

cpc_mal = inversion / clics + 100
cpc_bien = inversion / (clics + 100)

print("Sin paréntesis:", round(cpc_mal, 2))
print("Con paréntesis:", round(cpc_bien, 2))
"""),

md("""
Siete pesos con cuarenta y cuatro centavos por clic, o ciento siete. La diferencia es un par de
paréntesis.

Las dos líneas corren y las dos dan un número. Solo una contesta lo que querías preguntar.

| Expresión | Primero | Después | Resultado |
|---|---|---|---|
| `inversion / clics + 100` | `38500 / 5074` | `7.59 + 100` | `107.59` |
| `inversion / (clics + 100)` | `5074 + 100` | `38500 / 5174` | `7.44` |

La primera suma 100 al costo. La segunda suma 100 a los clics. Son dos preguntas distintas y
solo una de ellas es la que tenías en la cabeza.

Los paréntesis cuestan cero y quitan toda duda. Ponlos aunque no hagan falta.
"""),

code("""
# Los mismos números, con los paréntesis explícitos aunque sobren.
print(round((inversion / clics) + 100, 2))
print(round(inversion / (clics + 100), 2))
"""),

md("""
**Predice antes de correr.** ¿Qué imprime este programa?

- **A.** 21175.71 y 0.71
- **B.** 21175 y 5
- **C.** 21176 y 5
- **D.** Un error, porque no divide exacto
"""),

code("""
impresiones = 148230
anuncios = 7

print(impresiones // anuncios)
print(impresiones % anuncios)
"""),

md("""
La respuesta es **B**. `//` trunca hacia abajo y nunca redondea, y `%` da lo que sobró. La opción
C es la trampa: 21175.71 redondeado sería 21176, y `//` no redondea.
"""),

code("""
print("La división exacta:", impresiones / anuncios)
print("Truncada con //:   ", impresiones // anuncios)
print("Redondeada:        ", round(impresiones / anuncios))
"""),

md("""
---
# Bloque 3 · Conversión de tipos

Python convierte solo cuando no hay duda. En cuanto la hay, te lo deja a ti.

Cuando sumas un entero y un decimal, convierte el entero a decimal por su cuenta, porque no hay
otra lectura posible. Eso es **conversión implícita**.
"""),

code("""
resultado = 5074 + 0.5
print(resultado, type(resultado))

print(True + 1, "<- True vale 1 en una cuenta")
print(False + 1, "<- y False vale 0")
"""),

md("""
Cuando lo que tiene es texto, se detiene. Convertir `"5074"` a número es obvio para ti y ambiguo
para él, porque el texto podría venir con espacios, comas o un símbolo de moneda.

Ahí entra la **conversión explícita**: `int()`, `float()` y `str()`.
"""),

code("""
clics_texto = "5074"
nuevos_texto = "320"

print("Como texto: ", clics_texto + nuevos_texto)
print("Como número:", int(clics_texto) + int(nuevos_texto))
"""),

md("""
Ese `5074320` de la primera línea es el error más caro de las primeras semanas, porque no lanza
nada.

**Todo lo que entra por teclado o por archivo llega como texto.** `input` devuelve texto,
siempre. Un CSV guarda texto, siempre. Convertir es tu trabajo.

Y cada conversión falla si el contenido no corresponde, que es la buena noticia.
"""),

code("""
# FALLA A PROPÓSITO. int() sobre algo que no es un entero.
for valor in ["5074", "5074.5", " 5074 ", "5,074", "$5074"]:
    try:
        print(f"int({valor!r:12}) -> {int(valor)}")
    except ValueError as e:
        print(f"int({valor!r:12}) -> ValueError: {e}")
"""),

md("""
Cuatro resultados distintos con cinco textos que a ojo son el mismo número.

`"5074"` convierte. `" 5074 "` también, porque `int` tolera espacios alrededor. `"5074.5"` no,
porque tiene punto decimal y `int` no redondea texto. Y `"5,074"` y `"$5074"` tampoco, porque la
coma y el signo son formato.

Esa es exactamente la razón por la que la columna `unit_price` de `sales.csv` llega como texto y
hay que limpiarla antes de convertirla. Lo vas a hacer en la semana 15, y ya sabes por qué.
"""),

code("""
# El camino correcto: quitar el formato primero, convertir después.
crudo = "$ 2,082.50"
limpio = crudo.replace("$", "").replace(",", "").strip()

print(f"{crudo!r} -> {limpio!r} -> {float(limpio)}")
"""),

md("""
## Cuatro trampas de tipos que cuestan una tarde

**Tratar un código postal como número.** El 01000 de la Ciudad de México se vuelve 1000 en cuanto
lo conviertes. Un identificador es texto, aunque tenga dígitos.
"""),

code("""
cp = "01000"
print("Como texto: ", cp)
print("Convertido: ", int(cp), "<- perdió el cero y ya no es un código postal")
"""),

md("""
**Comparar texto con número.** El `"5074"` del archivo nunca va a ser igual al `5074` del
programa.
"""),

code("""
print('"5074" == 5074 ?', "5074" == 5074)
print('int("5074") == 5074 ?', int("5074") == 5074)
"""),

md("""
Fíjate en que la primera comparación **no lanza error**. Devuelve `False` tranquilamente, y un
filtro construido así descarta todos los renglones sin decir por qué.

**Confiar en la igualdad de decimales.** Esta es la que nadie cree hasta que la ve.
"""),

code("""
print(0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)
"""),

md("""
No es un error de Python. Los decimales se guardan en binario y algunos no tienen representación
exacta, igual que un tercio no se puede escribir exacto en decimal.

Para dinero hay dos salidas: comparar con una tolerancia, o trabajar en centavos enteros.
"""),

code("""
from math import isclose

print("Con tolerancia:", isclose(0.1 + 0.2, 0.3))

centavos_a = 10 + 20
print("En centavos:   ", centavos_a == 30)
"""),

md("""
**Olvidar que `None` no es cero.** Ya lo viste en el bloque 1, y vale repetirlo aquí porque es la
cuarta.

## La conversión en contexto

Toda la campaña, con cada dato en su tipo y las tres métricas calculadas.
"""),

code("""
canal = "Instagram"
impresiones = 148230
clics = 5074
inversion = 38500.00
conversiones = 173

tasa_conversion = conversiones / clics
costo_por_clic = inversion / clics
costo_por_mil = inversion / impresiones * 1000

print(f"Canal:              {canal}")
print(f"Tasa de conversión: {tasa_conversion:.2%}")
print(f"Costo por clic:     {costo_por_clic:,.2f}")
print(f"Costo por mil:      {costo_por_mil:,.2f}")
"""),

md("""
El `:.2%` de la segunda línea multiplica por cien y agrega el signo, así que no hay que hacerlo a
mano. El `:,.2f` separa miles y deja dos decimales.

Los dos son formato de salida y no tocan el valor guardado, igual que darle formato de moneda a
una celda no cambia lo que hay dentro.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Tipos

### Ejercicio 1 · Ocho variables tipadas

Toma los datos de una campaña o de un reporte que hayas visto y declara al menos ocho variables
con el tipo correcto: por lo menos un `int`, un `float`, un `str`, un `bool` y un `None`.

Imprime cada una con su `type`. Ningún nombre de una sola letra.

### Ejercicio 2 · El detector de tipos

Escribe una función `describir(valor)` que imprima el valor, su tipo y si se puede convertir a
número. Pruébala con: `42`, `"42"`, `"42.5"`, `"cuarenta"`, `True`, `None` y `"  7  "`.

### Ejercicio 3 · Identificador o cantidad

Para cada uno de estos, di en un comentario si debe guardarse como texto o como número, y por
qué: código postal, número de empleado, edad, teléfono, número de factura, cantidad de piezas,
año, RFC.

La prueba: ¿tiene sentido sumarlo o promediarlo?

## Operadores

### Ejercicio 4 · Los siete, una vez cada uno

Con `impresiones = 148230` y `anuncios = 7`, usa los siete operadores aritméticos al menos una
vez e imprime cada resultado con una etiqueta que diga qué calculaste.

### Ejercicio 5 · La precedencia

Sin correr nada, predice el resultado de estas cuatro expresiones. Después córrelas y compara.

```python
2 + 3 * 4
(2 + 3) * 4
2 ** 3 ** 2
10 - 4 - 3
```

Las dos últimas son las interesantes. Explica en un comentario por qué.

### Ejercicio 6 · El costo por adquisición

Una campaña con 38 500 de inversión, 5 074 clics y 173 conversiones. Calcula el costo por
adquisición de dos formas: dividiendo la inversión entre las conversiones, y multiplicando el
costo por clic por los clics necesarios para una conversión.

Comprueba que dan lo mismo. Si no dan lo mismo, tienes un paréntesis mal puesto.

## Conversión

### Ejercicio 7 · El limpiador de números

Escribe una función `a_numero(texto)` que reciba un texto con formato de moneda y devuelva un
`float`. Tiene que manejar `"$ 2,082.50"`, `"2082.50"`, `" 2,082.50 "` y `"$2,082"`.

Y tiene que devolver `None`, sin tronar, cuando reciba algo que no sea un número.

### Ejercicio 8 · El promedio con huecos

Tienes esta lista de costos por clic, donde `None` significa "no se midió":

```python
costos = [7.44, None, 8.10, 6.95, None, 7.80]
```

Calcula el promedio de tres formas: ignorando los `None`, tratándolos como cero, y descartando la
campaña completa si falta algún dato. Imprime los tres y di cuál reportarías.
"""),

md("""
---
## Tres ideas para llevarse

**El nombre no tiene tipo, el valor sí.** Reasignar una variable puede cambiar ese tipo sin que
nada te avise en ese momento, y el síntoma aparece líneas después.

**Un identificador es texto.** Códigos postales, folios y números de cliente. Que estén hechos de
dígitos no los vuelve números, y la prueba es si tiene sentido promediarlos.

**Los paréntesis cuestan cero.** Las dos versiones corren y dan un número. Solo una contesta la
pregunta que hiciste.

La siguiente sesión es cómo entran los datos al programa y cómo salen los resultados.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
canal = "Instagram"
impresiones = 148230
clics = 5074
conversiones = 173
inversion = 38500.00
tasa_objetivo = 0.035
campana_activa = True
fecha_cierre = None

for nombre, valor in [("canal", canal), ("impresiones", impresiones),
                      ("clics", clics), ("conversiones", conversiones),
                      ("inversion", inversion), ("tasa_objetivo", tasa_objetivo),
                      ("campana_activa", campana_activa),
                      ("fecha_cierre", fecha_cierre)]:
    print(f"{nombre:<16} {str(valor):<12} {type(valor).__name__}")
```

`fecha_cierre` en `None` es la más útil de las ocho: dice que la campaña sigue abierta, y eso es
distinto de poner una fecha inventada o dejarla en blanco.

### Ejercicio 2

```python
def describir(valor):
    print(f"{str(valor):<10} {type(valor).__name__:<8}", end=" ")
    try:
        print(f"-> float() da {float(valor)}")
    except (ValueError, TypeError) as e:
        print(f"-> no convierte: {type(e).__name__}")


for v in [42, "42", "42.5", "cuarenta", True, None, "  7  "]:
    describir(v)
```

Dos resultados sorprenden. `True` convierte a `1.0`, porque los booleanos son enteros por dentro.
Y `None` da `TypeError` en lugar de `ValueError`, porque el problema no es el contenido sino que
no hay contenido que leer.

### Ejercicio 3

```python
# Código postal    -> texto. Puede empezar con cero y sumarlo no significa nada.
# Número de empleado -> texto. Es una clave, aunque sea E0003 o 0003.
# Edad             -> número. Se promedia, se compara, se suma en un rango.
# Teléfono         -> texto. Lleva ceros, espacios, lada y a veces extensión.
# Número de factura -> texto. Identificador puro, y suele traer prefijo.
# Cantidad de piezas -> número. Es una cantidad medida.
# Año              -> número, con matices. Se resta para sacar antigüedad, pero
#                     promediar años de nacimiento casi nunca significa algo.
# RFC              -> texto. Tiene letras, así que ni discusión.
```

El año es el interesante: pasa la prueba a medias. Restarlo tiene sentido, promediarlo casi
nunca. Cuando un dato pasa la prueba a medias, conviene decidir explícitamente y anotarlo.

### Ejercicio 4

```python
impresiones = 148230
anuncios = 7

print("Suma:            ", impresiones + anuncios)
print("Resta:           ", impresiones - anuncios)
print("Producto:        ", impresiones * anuncios)
print("División:        ", impresiones / anuncios)
print("División entera: ", impresiones // anuncios)
print("Residuo:         ", impresiones % anuncios)
print("Potencia:        ", anuncios ** 2)
```

La división entera y el residuo son las que contestan una pregunta de negocio de verdad:
veintiún mil ciento setenta y cinco rondas completas de los siete anuncios, y cinco impresiones
que no alcanzaron a completar una ronda.

### Ejercicio 5

```python
print(2 + 3 * 4)        # 14, la multiplicación va primero
print((2 + 3) * 4)      # 20, el paréntesis cambia el orden
print(2 ** 3 ** 2)      # 512, no 64
print(10 - 4 - 3)       # 3, no 9

# La potencia se asocia a la derecha: 2 ** 3 ** 2 es 2 ** (3 ** 2), o sea 2 ** 9.
# Es el único operador aritmético que va de derecha a izquierda.
# La resta se asocia a la izquierda, como todos los demás: (10 - 4) - 3.
```

Si predijiste 64 en la tercera, estás en buena compañía: casi todo el mundo asume que va de
izquierda a derecha porque los otros seis operadores sí lo hacen.

### Ejercicio 6

```python
inversion = 38500.00
clics = 5074
conversiones = 173

cpa_directo = inversion / conversiones

costo_por_clic = inversion / clics
clics_por_conversion = clics / conversiones
cpa_indirecto = costo_por_clic * clics_por_conversion

print(f"Directo:   {cpa_directo:,.2f}")
print(f"Indirecto: {cpa_indirecto:,.2f}")
print("¿Iguales?", round(cpa_directo, 6) == round(cpa_indirecto, 6))
```

Dan 222.54 los dos. El redondeo a seis decimales antes de comparar no es adorno: sin él, la
comparación puede salir falsa por la misma razón que `0.1 + 0.2` no es `0.3`.

### Ejercicio 7

```python
def a_numero(texto):
    \"\"\"Convierte un texto con formato de moneda a float. Devuelve None si no puede.\"\"\"
    if not isinstance(texto, str):
        return None
    limpio = texto.replace("$", "").replace(",", "").strip()
    try:
        return float(limpio)
    except ValueError:
        return None


for t in ["$ 2,082.50", "2082.50", " 2,082.50 ", "$2,082", "sin dato", "", None]:
    print(f"{str(t)!r:<16} -> {a_numero(t)}")
```

Devolver `None` en lugar de tronar es una decisión, no una comodidad. Sirve cuando estás
limpiando una columna entera y quieres marcar lo que no se pudo convertir en vez de detener todo
en el primer renglón raro. Si lo que quieres es enterarte de inmediato, entonces conviene dejar
que lance el error.

### Ejercicio 8

```python
costos = [7.44, None, 8.10, 6.95, None, 7.80]

medidos = [c for c in costos if c is not None]

print("Ignorando los None:", round(sum(medidos) / len(medidos), 2),
      f"sobre {len(medidos)} campañas")

con_cero = [c if c is not None else 0 for c in costos]
print("Tratándolos como 0:", round(sum(con_cero) / len(con_cero), 2),
      f"sobre {len(con_cero)} campañas")

if None in costos:
    print("Descartando todo:   no se reporta, faltan", costos.count(None), "datos")

# Reportaría el primero, 7.57, diciendo que son cuatro campañas de seis. Tratar
# los None como cero afirma que dos campañas costaron cero pesos por clic, y eso
# es falso: no se midieron. Descartar todo es honesto y desperdicia cuatro datos
# buenos.
```

Ese `[c for c in costos if c is not None]` es una comprensión de lista, y se ve completa en la
semana 12. Por ahora léela como "los `c` de `costos` que no son `None`".

Nota el `is not None` en lugar de `!= None`. Los dos funcionan aquí, y `is` es la forma correcta
de preguntar por `None` porque compara identidad y no valor.
"""),

]

write(OUT / "es" / "w04.ipynb", es)
print("wrote", OUT / "es" / "w04.ipynb")


en = [

md("""
# Data Analysis · Week 4
## Data, types and primitive operations

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

A postal code is made of digits and is not a number. So is an invoice number. This session is
about why that distinction costs whole afternoons when nobody mentions it in time.

By the end of this notebook you will be able to:

1. Declare variables with names that say what they hold.
2. Recognise the five types you will use all term.
3. Use the seven arithmetic operators and the eight assignment ones.
4. Resolve an expression in the right order, and know when parentheses are needed.
5. Convert between types and explain why Python does not do it for you.

### How to use this notebook

Run the cells in order. Five fail on purpose and carry a comment saying so.

The case running through the whole session is a digital marketing campaign: 148,230 impressions,
5,074 clicks and 38,500 pesos of spend.
"""),

md("""
---
# Block 1 · Variables and types

A variable stores a value and gets called something so it can be found again. The difference
from a cell is twofold: **you choose the name and it says what it holds**, and **the value has a
type Python respects to the letter**.

`B7` says nothing. `campaign_spend` does.

## The five types

| Type | What it holds | Campaign example |
|---|---|---|
| `int` | Whole numbers, no size limit | `impressions = 148230` |
| `float` | Decimals, with limited precision | `conversion_rate = 0.0342` |
| `str` | Text, always in quotes | `channel = "Instagram"` |
| `bool` | True or false, nothing in between | `campaign_active = True` |
| `NoneType` | The absence of a value | `cost_per_click = None` |
"""),

code("""
channel = "Instagram"
impressions = 148230
clicks = 5074
spend = 38500.00
campaign_active = True
cost_per_click = None

print(type(channel), type(impressions))
print(type(spend), type(campaign_active))
print(type(cost_per_click))
"""),

md("""
`type` returns the type of a value. It is for checking what Python understood, not for the final
program.

Look at `spend`: the decimal point makes it a `float` even though the cents are zero. `38500.00`
is a decimal and `38500` is an integer, and the difference matters when you divide.

## The name has no type, the value does

This is the part that surprises anyone coming from a stricter language, and the part that bites
anyone coming from Excel.
"""),

code("""
value = 148230
print(value, type(value))

value = "148230"
print(value, type(value))

value = None
print(value, type(value))
"""),

md("""
The same variable held an integer, then text, then nothing. Python did not complain at any point.

It will complain later, when somebody operates on it expecting what it no longer is. That delay
between the cause and the symptom is what makes it hard to find.
"""),

code("""
# FAILS ON PURPOSE. The error shows up three lines after the cause.
target_rate = "0.03"          # <- here is the problem, and it does not blow up

print("The program keeps running...")
print("And keeps going...")

try:
    print(target_rate * 100)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
"""),

md("""
It raised nothing. `"0.03" * 100` repeats the text a hundred times, because multiplying text by
an integer is a legitimate operation in Python.

Run the cell and look at the output. That is what reaches your report if nobody checks the type.

## `None` is not zero

`None` is the absence of a value and zero is a measured one. Confusing them changes any average.
"""),

code("""
print("None == 0 ?", None == 0)
print("bool(None) ?", bool(None))
print("bool(0)    ?", bool(0))

# FAILS ON PURPOSE. Adding None is not adding zero.
try:
    print(cost_per_click + 10)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
A `cost_per_click` of `None` means "we have not measured it yet". A zero means "we measured it
and it came out zero, the campaign cost nothing". Those are different claims, and a column's
average changes depending on which one it is.

It is exactly the same problem as the eleven blank cells in `sales.csv` in week 15, planted
eleven weeks earlier.
"""),

md("""
---
# Block 2 · The operators, in full

Seven arithmetic and eight assignment. All of them, not only the ones used daily, because a
partial table teaches that the rest do not exist.

## The four you already use

| Operator | What it does | Example | Result |
|---|---|---|---|
| `+` | Addition | `5074 + 320` | `5394` |
| `-` | Subtraction | `5074 - 320` | `4754` |
| `*` | Product | `5074 * 2` | `10148` |
| `/` | Decimal division | `5074 / 4` | `1268.5` |
"""),

code("""
print(5074 + 320)
print(5074 - 320)
print(5074 * 2)
print(5074 / 4)
"""),

md("""
Note that `/` always returns a decimal, even when the division is exact.
"""),

code("""
print(10 / 2, type(10 / 2))
print(10 / 5, type(10 / 5))
"""),

md("""
## The three Excel does not have this way

| Operator | What it does | Example | Result |
|---|---|---|---|
| `//` | Integer division | `5074 // 4` | `1268` |
| `%` | Remainder | `5074 % 4` | `2` |
| `**` | Power | `2 ** 10` | `1024` |
"""),

code("""
print("Integer division:", 5074 // 4)
print("Remainder:       ", 5074 % 4)
print("Power:           ", 2 ** 10)
print()
print("Check:", 1268 * 4 + 2, "== 5074")
"""),

md("""
`//` and `%` are the two halves of a division with a remainder, and together they rebuild the
original number. They come up more than you would think: splitting things into groups, checking
whether a number is even, or working out the day of the week.
"""),

code("""
# How many complete ads fit, and how many impressions are left over?
impressions = 148230
per_ad = 7

print("Complete ads:      ", impressions // per_ad)
print("Leftover impressions:", impressions % per_ad)
print()
print("Is 148230 even?", impressions % 2 == 0)
"""),

md("""
## Storing, and the seven shorthands

| Operator | Equivalent to | Example |
|---|---|---|
| `=` | Store a value | `clicks = 5074` |
| `+=` | `x = x + y` | `clicks += 320` |
| `-=` | `x = x - y` | `clicks -= 12` |
| `*=` | `x = x * y` | `spend *= 1.16` |
| `/=` | `x = x / y` | `spend /= 30` |
| `//=` | `x = x // y` | `impressions //= 1000` |
| `%=` | `x = x % y` | `position %= 7` |
| `**=` | `x = x ** y` | `base **= 2` |

All eight, running, so they do not stay a list to memorise.
"""),

code("""
clicks = 5074
print("Start: ", clicks)

clicks += 320
print("+= 320:", clicks)

clicks -= 12
print("-= 12: ", clicks)

clicks *= 2
print("*= 2:  ", clicks)

clicks /= 4
print("/= 4:  ", clicks, "<- careful, it became a float")
"""),

code("""
impressions = 148230
impressions //= 1000
print("//= 1000:", impressions, type(impressions))

position = 23
position %= 7
print("%= 7:    ", position)

base = 12
base **= 2
print("**= 2:   ", base)
"""),

md("""
Look at the `/=`: it turned an integer into a decimal. `//=` did not. That difference sneaks into
reports where suddenly everything prints with a `.0` on the end.
"""),

md("""
---
## Precedence, and why parentheses cost nothing

The order Python resolves an expression in is the one from mathematics and the one from Excel.
Nothing new to memorise:

1. Parentheses
2. Power
3. `*` `/` `//` `%`
4. `+` `-`

And here is why it matters.
"""),

code("""
spend = 38500
clicks = 5074

cpc_wrong = spend / clicks + 100
cpc_right = spend / (clicks + 100)

print("Without parentheses:", round(cpc_wrong, 2))
print("With parentheses:   ", round(cpc_right, 2))
"""),

md("""
Seven pesos forty-four per click, or a hundred and seven. The difference is a pair of
parentheses.

Both lines run and both give a number. Only one answers what you meant to ask.

| Expression | First | Then | Result |
|---|---|---|---|
| `spend / clicks + 100` | `38500 / 5074` | `7.59 + 100` | `107.59` |
| `spend / (clicks + 100)` | `5074 + 100` | `38500 / 5174` | `7.44` |

The first adds 100 to the cost. The second adds 100 to the clicks. Two different questions, and
only one of them was the one in your head.

Parentheses cost nothing and remove all doubt. Put them in even when they are not needed.
"""),

code("""
# The same numbers, with the parentheses spelled out even though they are redundant.
print(round((spend / clicks) + 100, 2))
print(round(spend / (clicks + 100), 2))
"""),

md("""
**Predict before you run.** What does this program print?

- **A.** 21175.71 and 0.71
- **B.** 21175 and 5
- **C.** 21176 and 5
- **D.** An error, because it does not divide exactly
"""),

code("""
impressions = 148230
ads = 7

print(impressions // ads)
print(impressions % ads)
"""),

md("""
The answer is **B**. `//` truncates downwards and never rounds, and `%` gives what was left over.
Option C is the trap: 21175.71 rounded would be 21176, and `//` does not round.
"""),

code("""
print("The exact division:", impressions / ads)
print("Truncated with //: ", impressions // ads)
print("Rounded:           ", round(impressions / ads))
"""),

md("""
---
# Block 3 · Type conversion

Python converts only when there is no doubt. The moment there is, it leaves it to you.

When you add an integer and a decimal, it converts the integer to a decimal on its own, because
there is no other possible reading. That is **implicit conversion**.
"""),

code("""
result = 5074 + 0.5
print(result, type(result))

print(True + 1, "<- True counts as 1 in arithmetic")
print(False + 1, "<- and False counts as 0")
"""),

md("""
When what it has is text, it stops. Converting `"5074"` to a number is obvious to you and
ambiguous to it, because the text could arrive with spaces, commas or a currency symbol.

That is where **explicit conversion** comes in: `int()`, `float()` and `str()`.
"""),

code("""
clicks_text = "5074"
new_text = "320"

print("As text:  ", clicks_text + new_text)
print("As numbers:", int(clicks_text) + int(new_text))
"""),

md("""
That `5074320` on the first line is the most expensive error of the early weeks, because it
raises nothing.

**Everything that arrives from the keyboard or from a file comes as text.** `input` returns text,
always. A CSV stores text, always. Converting is your job.

And every conversion fails when the content does not match, which is the good news.
"""),

code("""
# FAILS ON PURPOSE. int() on something that is not a whole number.
for value in ["5074", "5074.5", " 5074 ", "5,074", "$5074"]:
    try:
        print(f"int({value!r:12}) -> {int(value)}")
    except ValueError as e:
        print(f"int({value!r:12}) -> ValueError: {e}")
"""),

md("""
Four different outcomes from five strings that look like the same number.

`"5074"` converts. `" 5074 "` does too, because `int` tolerates surrounding spaces. `"5074.5"`
does not, because it has a decimal point and `int` does not round text. And `"5,074"` and
`"$5074"` do not either, because the comma and the sign are formatting.

That is exactly why the `unit_price` column of `sales.csv` arrives as text and has to be cleaned
before it can be converted. You will do it in week 15, and now you know why.
"""),

code("""
# The right route: strip the formatting first, convert afterwards.
raw = "$ 2,082.50"
clean = raw.replace("$", "").replace(",", "").strip()

print(f"{raw!r} -> {clean!r} -> {float(clean)}")
"""),

md("""
## Four type traps that cost an afternoon

**Treating a postal code as a number.** Mexico City's 01000 becomes 1000 the moment you convert
it. An identifier is text, even when it is made of digits.
"""),

code("""
postal = "01000"
print("As text:  ", postal)
print("Converted:", int(postal), "<- it lost the zero and is no longer a postal code")
"""),

md("""
**Comparing text with a number.** The `"5074"` from the file will never equal the `5074` in the
program.
"""),

code("""
print('"5074" == 5074 ?', "5074" == 5074)
print('int("5074") == 5074 ?', int("5074") == 5074)
"""),

md("""
Notice that the first comparison **raises nothing**. It calmly returns `False`, and a filter
built that way discards every row without saying why.

**Trusting the equality of decimals.** This is the one nobody believes until they see it.
"""),

code("""
print(0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)
"""),

md("""
This is not a Python bug. Decimals are stored in binary and some have no exact representation,
just as a third cannot be written exactly in decimal.

For money there are two ways out: compare with a tolerance, or work in whole cents.
"""),

code("""
from math import isclose

print("With a tolerance:", isclose(0.1 + 0.2, 0.3))

cents = 10 + 20
print("In cents:        ", cents == 30)
"""),

md("""
**Forgetting that `None` is not zero.** You saw it in block 1, and it is worth repeating here
because it is the fourth.

## Conversion in context

The whole campaign, with each value in its type and the three metrics computed.
"""),

code("""
channel = "Instagram"
impressions = 148230
clicks = 5074
spend = 38500.00
conversions = 173

conversion_rate = conversions / clicks
cost_per_click = spend / clicks
cost_per_thousand = spend / impressions * 1000

print(f"Channel:          {channel}")
print(f"Conversion rate:  {conversion_rate:.2%}")
print(f"Cost per click:   {cost_per_click:,.2f}")
print(f"Cost per thousand: {cost_per_thousand:,.2f}")
"""),

md("""
The `:.2%` on the second line multiplies by a hundred and adds the sign, so it does not have to
be done by hand. The `:,.2f` separates thousands and leaves two decimals.

Both are output formatting and neither touches the stored value, just as giving a cell a currency
format does not change what is inside it.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## Types

### Exercise 1 · Eight typed variables

Take the data from a campaign or a report you have seen and declare at least eight variables with
the right type: at least one `int`, one `float`, one `str`, one `bool` and one `None`.

Print each one with its `type`. No single-letter names.

### Exercise 2 · The type detector

Write a function `describe(value)` that prints the value, its type and whether it can be
converted to a number. Test it with: `42`, `"42"`, `"42.5"`, `"forty"`, `True`, `None` and
`"  7  "`.

### Exercise 3 · Identifier or quantity

For each of these, say in a comment whether it should be stored as text or as a number, and why:
postal code, employee number, age, phone number, invoice number, quantity of pieces, year, tax ID.

The test: does it make sense to add or average it?

## Operators

### Exercise 4 · All seven, once each

With `impressions = 148230` and `ads = 7`, use all seven arithmetic operators at least once and
print each result with a label saying what you computed.

### Exercise 5 · Precedence

Without running anything, predict the result of these four expressions. Then run them and
compare.

```python
2 + 3 * 4
(2 + 3) * 4
2 ** 3 ** 2
10 - 4 - 3
```

The last two are the interesting ones. Explain why in a comment.

### Exercise 6 · Cost per acquisition

A campaign with 38,500 of spend, 5,074 clicks and 173 conversions. Work out the cost per
acquisition two ways: by dividing the spend by the conversions, and by multiplying the cost per
click by the clicks needed for one conversion.

Check that they agree. If they do not, you have a parenthesis in the wrong place.

## Conversion

### Exercise 7 · The number cleaner

Write a function `to_number(text)` that takes a string with currency formatting and returns a
`float`. It has to handle `"$ 2,082.50"`, `"2082.50"`, `" 2,082.50 "` and `"$2,082"`.

And it has to return `None`, without blowing up, when handed something that is not a number.

### Exercise 8 · The average with holes

You have this list of costs per click, where `None` means "not measured":

```python
costs = [7.44, None, 8.10, 6.95, None, 7.80]
```

Work out the average three ways: ignoring the `None`s, treating them as zero, and discarding the
whole campaign if any value is missing. Print all three and say which one you would report.
"""),

md("""
---
## Three ideas to take away

**The name has no type, the value does.** Reassigning a variable can change that type with
nothing warning you at the time, and the symptom appears lines later.

**An identifier is text.** Postal codes, invoice numbers and customer numbers. Being made of
digits does not make them numbers, and the test is whether averaging them means anything.

**Parentheses cost nothing.** Both versions run and both give a number. Only one answers the
question you asked.

Next session is how data gets into the program and how results get out.
"""),

md("""
---
# Solutions

### Exercise 1

```python
channel = "Instagram"
impressions = 148230
clicks = 5074
conversions = 173
spend = 38500.00
target_rate = 0.035
campaign_active = True
close_date = None

for name, value in [("channel", channel), ("impressions", impressions),
                    ("clicks", clicks), ("conversions", conversions),
                    ("spend", spend), ("target_rate", target_rate),
                    ("campaign_active", campaign_active),
                    ("close_date", close_date)]:
    print(f"{name:<16} {str(value):<12} {type(value).__name__}")
```

`close_date` at `None` is the most useful of the eight: it says the campaign is still open, and
that is different from putting in a made-up date or leaving it blank.

### Exercise 2

```python
def describe(value):
    print(f"{str(value):<10} {type(value).__name__:<8}", end=" ")
    try:
        print(f"-> float() gives {float(value)}")
    except (ValueError, TypeError) as e:
        print(f"-> will not convert: {type(e).__name__}")


for v in [42, "42", "42.5", "forty", True, None, "  7  "]:
    describe(v)
```

Two results surprise people. `True` converts to `1.0`, because booleans are integers underneath.
And `None` gives `TypeError` rather than `ValueError`, because the problem is not the content but
that there is no content to read.

### Exercise 3

```python
# Postal code     -> text. It can start with a zero and adding it means nothing.
# Employee number -> text. It is a key, even when it is E0003 or 0003.
# Age             -> number. It gets averaged, compared, summed across a range.
# Phone number    -> text. It carries zeros, spaces, area code and sometimes an extension.
# Invoice number  -> text. A pure identifier, and it usually carries a prefix.
# Quantity of pieces -> number. It is a measured amount.
# Year            -> number, with caveats. Subtracting gives tenure, but averaging
#                    birth years almost never means anything.
# Tax ID          -> text. It has letters, so there is nothing to discuss.
```

The year is the interesting one: it half passes the test. Subtracting it makes sense, averaging
it almost never does. When a value half passes the test, it is worth deciding explicitly and
writing the decision down.

### Exercise 4

```python
impressions = 148230
ads = 7

print("Sum:             ", impressions + ads)
print("Difference:      ", impressions - ads)
print("Product:         ", impressions * ads)
print("Division:        ", impressions / ads)
print("Integer division:", impressions // ads)
print("Remainder:       ", impressions % ads)
print("Power:           ", ads ** 2)
```

The integer division and the remainder are the ones answering a real business question:
twenty-one thousand one hundred and seventy-five complete rounds of the seven ads, and five
impressions that did not make up a round.

### Exercise 5

```python
print(2 + 3 * 4)        # 14, multiplication goes first
print((2 + 3) * 4)      # 20, the parentheses change the order
print(2 ** 3 ** 2)      # 512, not 64
print(10 - 4 - 3)       # 3, not 9

# Power associates to the right: 2 ** 3 ** 2 is 2 ** (3 ** 2), so 2 ** 9.
# It is the only arithmetic operator that runs right to left.
# Subtraction associates to the left, like all the others: (10 - 4) - 3.
```

If you predicted 64 on the third one, you are in good company: almost everyone assumes left to
right because the other six operators do work that way.

### Exercise 6

```python
spend = 38500.00
clicks = 5074
conversions = 173

cpa_direct = spend / conversions

cost_per_click = spend / clicks
clicks_per_conversion = clicks / conversions
cpa_indirect = cost_per_click * clicks_per_conversion

print(f"Direct:   {cpa_direct:,.2f}")
print(f"Indirect: {cpa_indirect:,.2f}")
print("Equal?", round(cpa_direct, 6) == round(cpa_indirect, 6))
```

Both give 222.54. Rounding to six decimals before comparing is not decoration: without it, the
comparison can come out false for the same reason `0.1 + 0.2` is not `0.3`.

### Exercise 7

```python
def to_number(text):
    \"\"\"Convert a currency-formatted string to a float. Returns None if it cannot.\"\"\"
    if not isinstance(text, str):
        return None
    clean = text.replace("$", "").replace(",", "").strip()
    try:
        return float(clean)
    except ValueError:
        return None


for t in ["$ 2,082.50", "2082.50", " 2,082.50 ", "$2,082", "no data", "", None]:
    print(f"{str(t)!r:<16} -> {to_number(t)}")
```

Returning `None` instead of blowing up is a decision, not a convenience. It helps when you are
cleaning a whole column and want to flag what could not be converted rather than stopping
everything on the first odd row. If what you want is to find out immediately, then letting it
raise is the better choice.

### Exercise 8

```python
costs = [7.44, None, 8.10, 6.95, None, 7.80]

measured = [c for c in costs if c is not None]

print("Ignoring the Nones:", round(sum(measured) / len(measured), 2),
      f"over {len(measured)} campaigns")

with_zero = [c if c is not None else 0 for c in costs]
print("Treating them as 0:", round(sum(with_zero) / len(with_zero), 2),
      f"over {len(with_zero)} campaigns")

if None in costs:
    print("Discarding it all:  not reported,", costs.count(None), "values missing")

# I would report the first, 7.57, saying it covers four campaigns out of six.
# Treating the Nones as zero claims two campaigns cost zero pesos per click, and
# that is false: they were not measured. Discarding everything is honest and
# wastes four good values.
```

That `[c for c in costs if c is not None]` is a list comprehension, and it gets covered fully in
week 12. For now read it as "the `c`s in `costs` that are not `None`".

Note the `is not None` rather than `!= None`. Both work here, and `is` is the correct way to ask
about `None` because it compares identity rather than value.
"""),

]

write(OUT / "en" / "w04.ipynb", en)
print("wrote", OUT / "en" / "w04.ipynb")
