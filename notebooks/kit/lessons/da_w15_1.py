"""notebooks/analisis-de-datos/{es,en}/w15.1.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w15.1.*.yaml
Source code:  docs/en/courses/python-course/06 - Advanced/A05 - Pandas/
              01_series_and_dataframe.py, 02_load_and_inspect.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 15, sesión 1 de 3
## Series, DataFrame y carga de archivos

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

La hoja de cálculo que ya sabes usar existe dentro de Python y se llama DataFrame. Esta
sesión presenta los dos objetos sobre los que está construido todo pandas, y una costumbre
de dos minutos que separa un análisis correcto de uno que solo se ve correcto.

Al terminar este cuaderno vas a poder:

1. Explicar qué es una `Series` y por qué es la lista de la semana 12 con etiquetas encima.
2. Construir un `DataFrame` desde un diccionario de columnas y desde un archivo.
3. Cargar un CSV en una línea con `read_csv`, y saber qué hizo con cada columna.
4. Inspeccionar un archivo con `head`, `info`, `shape` y `describe`, siempre en ese orden.
5. Detectar valores faltantes, renglones duplicados y categorías mal capturadas antes de
   que arruinen un resultado.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden, de arriba hacia abajo. Varias dependen de una variable que
definió la anterior, así que saltarte una da un `NameError` que no tiene nada que ver con
el tema.

Antes de correr una celda marcada **Predice**, escribe tu respuesta en un papel. Fallar la
predicción y entender por qué enseña más que ver la salida correcta de primera.

Tres celdas fallan a propósito. Llevan un comentario que lo dice y atrapan el error para
que el cuaderno siga corriendo.
"""),

md("""
---
## Preparación

Dos celdas de arranque. La primera dice qué versión de pandas te tocó, la segunda deja los
datos a la mano.
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

md("""
### Qué esperar según la versión

Colab actualiza sus bibliotecas cuando quiere, así que el número de arriba puede ser 2.x o
3.x. Importa para una sola cosa en esta sesión: cómo se llama el tipo de una columna de
texto.

| | pandas 2.x | pandas 3.0 y posteriores |
|---|---|---|
| Una columna de texto reporta | `object` | `str` |
| `info()` cierra con | `dtypes: float64(1), object(5)` | `dtypes: float64(1), str(5)` |

Es el mismo dato y el mismo comportamiento, con otro nombre. `object` era el cajón donde
pandas guardaba cualquier cosa que no fuera número; desde la versión 3.0 el texto tiene su
propio tipo y ya no comparte cajón con nadie. Si tu salida dice `object` donde este
cuaderno dice `str`, no te equivocaste en nada.
"""),

bootstrap_cell("es"),

# ──────────────────────────────────────────────────────────── bloque 1

md("""
---
# Bloque 1 · Los dos objetos

Todo pandas está construido sobre dos cosas, y las dos ya las conoces con otro nombre. Una
es la columna. La otra es la hoja completa.

| En la hoja | En pandas | Lo que ya sabías |
|---|---|---|
| Una columna | `Series` | Una lista, con índice |
| La hoja completa | `DataFrame` | Varias listas emparejadas |
| El número de fila | El índice | La posición, que empieza en 0 |
| El encabezado | `columns` | Las llaves de un diccionario |

La correspondencia es exacta, y esa es la razón por la que este curso puede saltar directo
a pandas sin pasar por una biblioteca intermedia.

## Una Series es una columna

La forma más simple de hacer una es desde una lista.
"""),

code("""
unidades = pd.Series([15, 8, 22, 5, 11])
print(unidades)
"""),

md("""
Regresaron dos cosas que la lista no tenía.

A la izquierda apareció un **índice**, del 0 al 4, que pandas creó solo. Abajo apareció un
**dtype**, el tipo que comparten todos los valores de la columna. Una lista de Python puede
mezclar enteros con texto; una Series no, y de ahí sale casi toda su velocidad.
"""),

code("""
print("El índice:", list(unidades.index))
print("El dtype: ", unidades.dtype)
print("El largo: ", len(unidades))
"""),

md("""
El índice no tiene que ser un contador. Ponle etiquetas y la Series empieza a comportarse
como un rango con nombre de tu hoja de cálculo.
"""),

code("""
mensual = pd.Series(
    [42000, 51500, 38900, 60100, 55300, 47800],
    index=["ene", "feb", "mar", "abr", "may", "jun"],
)
print(mensual)
"""),

md("""
Ahora un valor se alcanza por su etiqueta y no contando posiciones. Es la diferencia entre
escribir `mensual["mar"]` y acordarte de que marzo era el tercero, o el segundo si cuentas
desde cero.
"""),

code("""
print("Marzo:", mensual["mar"])
print("Los tres primeros meses:")
print(mensual[["ene", "feb", "mar"]])
"""),

md("""
Las funciones de resumen que usas en la hoja son métodos de la Series. Son las mismas
cuentas, escritas de otra forma.
"""),

code("""
print("Total:     ", mensual.sum())
print("Promedio:  ", round(mensual.mean(), 2))
print("Mejor mes: ", mensual.idxmax(), "con", mensual.max())
print("Peor mes:  ", mensual.idxmin(), "con", mensual.min())
"""),

md("""
### El cambio grande: la operación se aplica a la columna entera

Una operación sobre una Series alcanza a todos los valores de golpe. No hay `for`, y no hay
que arrastrar la fórmula hacia abajo. Este es el cambio más grande en cómo vas a trabajar
de aquí en adelante.
"""),

code("""
con_iva = mensual * 1.16
print(con_iva.round(2))
"""),

md("""
La comparación funciona igual, y devuelve una Series de verdaderos y falsos. Esa Series de
booleanos es lo que después va a servir para filtrar renglones, así que vale la pena verla
sola antes de usarla dentro de un corchete.
"""),

code("""
buenos = mensual > 50000
print(buenos)
print()
print("Meses arriba de 50 mil:", buenos.sum())
print(mensual[buenos])
"""),

md("""
### El caso límite: dos Series con índices distintos

Aquí es donde el índice deja de ser un adorno. Cuando sumas dos Series, pandas no empareja
por posición sino por etiqueta. Si una etiqueta existe en una sola de las dos, el resultado
en esa fila es `NaN`, que es como pandas escribe "no hay dato".

**Predice antes de correr.** La primera Series tiene enero, febrero y marzo. La segunda
tiene febrero, marzo y abril. ¿Cuántas filas trae el resultado y qué hay en cada una?
"""),

code("""
primer = pd.Series([100, 200, 300], index=["ene", "feb", "mar"])
segundo = pd.Series([10, 20, 30], index=["feb", "mar", "abr"])

print(primer + segundo)
"""),

md("""
Salieron cuatro filas y no tres, porque pandas conservó la unión de las dos etiquetas.
Enero y abril quedaron en `NaN` porque a cada uno le faltó su pareja. Febrero y marzo sí se
sumaron.

Esto es correcto y es lo que quieres casi siempre, pero sorprende la primera vez. Si
esperabas tres números y te salieron cuatro con dos huecos, el índice es el culpable, no la
suma.

## Un DataFrame son varias Series que comparten el índice

Lo normal es construirlo desde un diccionario, con una llave por columna.
"""),

code("""
ventas_demo = pd.DataFrame({
    "mes": ["ene", "feb", "mar", "abr", "may", "jun"],
    "region": ["North", "North", "South", "South", "Centre", "Centre"],
    "monto": [42000, 51500, 38900, 60100, 55300, 47800],
    "unidades": [15, 18, 12, 21, 19, 16],
})
print(ventas_demo)
"""),

code("""
print("Forma (renglones, columnas):", ventas_demo.shape)
print("Nombres de columna:", list(ventas_demo.columns))
print("Índice:", list(ventas_demo.index))
"""),

md("""
Cada columna es una Series, y se saca por nombre. Que el tipo sea literalmente `Series` es
lo que hace que todo lo del bloque anterior siga sirviendo aquí.
"""),

code("""
print(ventas_demo["monto"])
print()
print("Su tipo:", type(ventas_demo["monto"]))
"""),

code("""
print(ventas_demo.dtypes)
"""),

md("""
Los `dtypes` te dicen cómo entendió pandas cada columna. `mes` y `region` traen texto,
`monto` y `unidades` traen enteros. Este ejemplo se armó a mano y por eso salió limpio; en
un archivo real es donde empiezan las sorpresas, y de eso trata el bloque 3.

### Una columna nueva a partir de las otras

Asignar a un nombre que no existe crea la columna. El lado derecho se calcula para todos
los renglones a la vez, que es exactamente lo que hace una fórmula arrastrada hasta abajo.
"""),

code("""
ventas_demo["precio_unitario"] = (ventas_demo["monto"] / ventas_demo["unidades"]).round(2)
print(ventas_demo)
"""),

md("""
Y una variante que la diapositiva no alcanzó a mostrar: la columna nueva puede salir de una
comparación, no solo de una división. Aquí marca los meses que pasaron de cincuenta mil.
"""),

code("""
ventas_demo["buen_mes"] = ventas_demo["monto"] > 50000
print(ventas_demo[["mes", "monto", "buen_mes"]])
print()
print("Cuántos buenos:", ventas_demo["buen_mes"].sum())
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · Cargar el archivo

La semana pasada abriste un CSV a mano con el módulo `csv`: abrir el archivo, leer el
encabezado, recorrer los renglones y convertir cada campo. `read_csv` hace todo eso en una
línea.

Vale la pena correr las dos versiones seguidas, porque la comparación es el argumento
entero a favor de pandas.

## La versión a mano, la de la semana 14
"""),

code("""
import csv

with open("sales.csv", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

for fila in filas:
    fila["units"] = int(fila["units"] or 0)

print(len(filas), "renglones")
print(filas[0])
"""),

md("""
Funciona, y cada renglón quedó como un diccionario. El problema no es que sea largo, es que
tú tomaste una decisión escondida: `int(fila["units"] or 0)` convirtió las celdas vacías en
cero. Eso cambia el promedio y nadie lo va a notar leyendo el código.

## La versión con pandas
"""),

code("""
ventas = pd.read_csv("sales.csv")

print(ventas.shape)
"""),

md("""
Una línea, y además `read_csv` intentó adivinar el tipo de cada columna. Lo que no puede
adivinar es qué querías que significara una celda vacía, y por eso no la rellena con cero:
la deja marcada como faltante y te deja a ti decidir. Esa decisión es la de la sesión 15.2.

### Un detalle que sirve todo el semestre

`read_csv` acepta una URL donde acepta una ruta. Con el repositorio público, cargar los
datos del curso desde cualquier máquina se ve así, sin descargar nada a mano:

```python
BASE = ("https://raw.githubusercontent.com/Davidowa/learning-hub/main/"
        "docs/en/courses/python-course/06%20-%20Advanced/data/")

ventas = pd.read_csv(BASE + "sales.csv")
```

La celda de preparación de este cuaderno intenta exactamente eso antes de reconstruir los
archivos por su cuenta.

## Los primeros renglones
"""),

code("""
print(ventas.head())
"""),

md("""
`head` muestra los primeros cinco renglones. Pásale un número para cambiar cuántos.
"""),

code("""
print(ventas.head(3))
"""),

md("""
`tail` muestra los últimos, y es la que hay que correr aunque parezca redundante. Ahí es
donde se esconde el renglón de totales que alguien pegó al final de la hoja antes de
exportarla, y que si no lo ves acaba contado como una venta más.
"""),

code("""
print(ventas.tail(3))
"""),

md("""
`shape` responde cuántos datos tienes de verdad. Devuelve una tupla, así que se puede
desempacar en dos nombres.
"""),

code("""
renglones, columnas = ventas.shape
print(f"{renglones} renglones y {columnas} columnas")
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · Mirar antes de tocar

La tentación es ir directo a la respuesta. Aguántate dos minutos. Casi todo resultado
equivocado del proyecto final se rastrea a una columna que no era del tipo que supusiste, o
a renglones que no estaban.

El orden es siempre el mismo: `head`, `info`, `shape`, `describe`.

## Los tipos que infirió
"""),

code("""
print(ventas.dtypes)
"""),

md("""
`info` es el comando más útil de esta sesión. Reporta, por columna, cuántos valores no
están vacíos y qué tipo infirió pandas. Fíjate en la columna `Non-Null Count`: una que no
llega al total de renglones tiene huecos.
"""),

code("""
ventas.info()
"""),

md("""
### Qué te están diciendo esos tipos

Tres cosas de esa salida merecen nombre propio.

**`units` entró como `float64` y no como entero.** pandas leyó bien los dígitos, pero once
celdas están vacías, y un vacío se tiene que representar de alguna forma. Ese marcador es
`NaN`, que solo existe en una columna decimal, así que la columna entera se volvió decimal.
Por eso los conteos se imprimen como `15.0` en lugar de `15`.

**`unit_price` entró como texto**, porque `"$ 2,082.50"` no es un número para Python. El
signo de pesos y la coma de miles son formato, y el formato no es parte del valor.

**`date` entró como texto**, porque un CSV no tiene tipo fecha. Mientras no se convierta,
ordenar por esa columna funciona de milagro: sale bien solo porque el formato pone el año
primero.

Ninguna de las tres es una falla de pandas. Es el CSV, que no guarda tipos, exactamente
como lo viste la semana pasada. La sesión 15.2 arregla las tres.

## El resumen numérico
"""),

code("""
print(ventas.describe())
"""),

md("""
`describe` da conteo, promedio, desviación estándar, mínimo, máximo y los cuartiles de cada
columna numérica. Por ahora solo `units` califica, y su conteo de 313 contra 324 renglones
es otra vez el dato faltante asomándose.

Esa es la razón por la que `describe` en un archivo recién cargado dice tan poco: no es que
no haya números, es que están guardados como texto. Con `include="all"` pandas también
resume las columnas de texto, con otras estadísticas.
"""),

code("""
print(ventas.describe(include="all"))
"""),

md("""
Dos renglones de esa tabla valen la revisada. `unique` cuenta cuántos valores distintos hay
en la columna, y `top` dice cuál se repite más. `region` reporta ocho valores distintos, y
en la empresa hay cuatro regiones.

## Encontrar la suciedad

Para una columna de texto, lo que sirve es contar cuántas veces aparece cada valor.
"""),

code("""
print(ventas["region"].value_counts())
"""),

md("""
Se capturaron cuatro regiones y el archivo cree que hay ocho, porque el mismo nombre se
escribió con distinta capitalización y con espacios de sobra. `" North"`, `"North "`,
`"north"` y `"NORTH"` son, para Python, cuatro textos que no tienen nada que ver entre sí.

Si agrupas por región hoy, el norte se te parte en cinco pedazos y ninguno trae el total
verdadero. Esto se arregla en la sesión 15.2, y el punto de hoy es que se detecta antes de
que pase.
"""),

code("""
print("Valores distintos en region:", ventas["region"].nunique())
print("Valores distintos en channel:", ventas["channel"].nunique())
print("Valores distintos en product:", ventas["product"].nunique())
"""),

md("""
`isna` marca cada celda faltante como verdadero, y `sum` las cuenta por columna.
"""),

code("""
print(ventas.isna().sum())
print()
print("Faltantes en toda la tabla:", ventas.isna().sum().sum())
"""),

md("""
`duplicated` marca un renglón como verdadero cuando un renglón idéntico ya apareció antes.
Los siete de aquí son el rastro de un copiar y pegar.
"""),

code("""
print("Renglones duplicados:", ventas.duplicated().sum())
print()
print(ventas[ventas.duplicated(keep=False)].sort_values("date").head(6))
"""),

md("""
Nota el `keep=False` de la última línea: con ese argumento pandas marca todas las copias,
no solo las repeticiones, así que puedes ver los pares completos y confirmar que de verdad
son idénticos.

Y ojo con la aritmética. 324 renglones con siete duplicados son 317 hechos distintos. Cuál
de los dos números va en tu reporte depende de qué estés contando, y decidirlo es tu
trabajo, no el de pandas.
"""),

# ──────────────────────────────────────────────────────── fallas a propósito

md("""
---
## Tres celdas que fallan a propósito

Un tipo equivocado no siempre truena. A veces da un número, y ese es el caso peligroso.

### La que no falla, y por eso es la peor
"""),

code("""
# FALLA A PROPÓSITO. Esta celda no lanza ningún error, y ese es justo el problema.
# unit_price es texto, así que sum() concatena en lugar de sumar.
total = ventas["unit_price"].sum()

print("Tipo del resultado:", type(total))
print("Primeros 70 caracteres:", str(total)[:70])
"""),

md("""
Pediste un total de ventas y recibiste los 324 precios pegados uno tras otro en un solo
texto. Ningún error, ninguna advertencia. Si esto va dentro de un reporte más largo, sale
publicado.

Este es el argumento entero a favor de correr `info()` antes de analizar. Dos minutos de
inspección contra un número mal en una presentación.

### La que sí falla, y avisa a tiempo
"""),

code("""
# FALLA A PROPÓSITO. Promediar texto sí lanza error, a diferencia de sumarlo.
try:
    ventas["unit_price"].mean()
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`mean` no tiene forma de inventar un promedio de textos, así que se detiene. Es el mismo
problema que la celda anterior, con mejor suerte: aquí el error aparece cuando lo
escribiste, y no tres semanas después en una junta.

### La conversión que parece obvia y no lo es
"""),

code("""
# FALLA A PROPÓSITO. units trae once NaN, y NaN no cabe en un entero.
try:
    ventas["units"].astype(int)
except Exception as e:
    print(type(e).__name__ + ":", e)
"""),

md("""
Si te molestó ver `15.0` donde esperabas `15`, este es el intento natural de arreglarlo, y
no funciona. No puedes convertir a entero mientras haya faltantes, porque `NaN` no es un
número entero representable.

El orden correcto es al revés de como se siente: primero decides qué significan los once
huecos, después conviertes. Rellenar con cero, descartar esos renglones o dejarlos como
faltantes son tres decisiones distintas con tres promedios distintos, y ninguna es la
predeterminada.

## La segunda tabla
"""),

code("""
regiones = pd.read_csv("regions.csv")
print(regiones)
"""),

md("""
Esta es la tabla de consulta del curso, el equivalente del `BUSCARV` de tu hoja: un renglón
por región, con los datos que no tienen por qué repetirse en cada venta.

Trae cinco regiones y el archivo de ventas solo cubre cuatro. La diferencia es
intencional, y la sesión 15.3 muestra qué hace una unión con la región que se quedó sin
ventas.
"""),

# ──────────────────────────────────────────────────────────── predice

md("""
---
## Predice antes de correr

Escribe tu respuesta antes de ejecutar cada celda.

### Pregunta 1

¿Por qué la columna `units` salió `float64` y no `int64`?

- **A.** Porque las unidades traen decimales en el archivo.
- **B.** Porque once celdas vacías necesitan `NaN`, que solo existe en float.
- **C.** Porque `read_csv` siempre usa float por seguridad.
- **D.** Porque la columna tiene más de trescientos renglones.
"""),

code("""
print("dtype de units:      ", ventas["units"].dtype)
print("Faltantes en units:  ", ventas["units"].isna().sum())
print("¿Algún valor con parte decimal?")
print((ventas["units"].dropna() % 1 != 0).sum(), "de", ventas["units"].notna().sum())
"""),

md("""
Cero valores con parte decimal, y once faltantes. La respuesta es **B**: los números eran
enteros desde el principio, y lo que forzó el tipo decimal fue el marcador de vacío.

### Pregunta 2

`ventas.shape` dijo 324 renglones. ¿Cuántas ventas distintas describe el archivo, y cuántas
tienen su conteo de unidades registrado?
"""),

code("""
print("Renglones:                   ", len(ventas))
print("Sin contar duplicados:       ", len(ventas.drop_duplicates()))
print("Con units registrado:        ", ventas["units"].notna().sum())
print("Distintos y con units:       ", len(ventas.drop_duplicates().dropna(subset=["units"])))
"""),

md("""
Cuatro números distintos, todos correctos, todos respuesta a preguntas diferentes. Cuál usar
depende de qué afirmes en el reporte, y por eso `shape` no es "el número de datos" sino el
primero de varios.

### Pregunta 3

¿Qué imprime la siguiente celda? Piensa en qué tipo tiene `ventas["units"]` y qué tipo
tiene `ventas[["units"]]`.
"""),

code("""
print(type(ventas["units"]))
print(type(ventas[["units"]]))
print()
print(ventas[["date", "region", "units"]].head(3))
"""),

md("""
Un corchete devuelve una `Series`, la columna sola. Dos corchetes devuelven un `DataFrame`,
porque lo que pasaste fue una lista de nombres y una lista puede traer más de uno. Es la
confusión más común de las próximas dos sesiones, y ahora ya la viste con sus dos tipos
impresos.
"""),

# ──────────────────────────────────────────────────────────── errores comunes

md("""
---
## Cuatro errores al cargar un archivo

**Analizar antes de inspeccionar.** El resultado sale, se ve razonable y está mal. `head`,
`info` y `describe` cuestan dos minutos y son la única defensa contra el error que nadie
encuentra porque nadie lo está buscando.

**Confiar en el tipo inferido.** pandas adivina bien casi siempre. Ese *casi* es donde vive
la columna de precios que resultó ser texto.

**No revisar las categorías.** `value_counts` sobre una columna de texto delata la captura
inconsistente antes de que te parta los grupos en cinco pedazos.

**Suponer que `shape` es el número de datos.** 324 renglones con siete duplicados son 317
hechos distintos, y el total cambia según cuál cuentes.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Resuélvelos en celdas nuevas debajo de cada enunciado. Las soluciones están hasta abajo del
cuaderno, así que no las alcanzas a ver de reojo mientras trabajas.

Van de menos a más. Los primeros cuatro repiten con otros datos lo que acabas de ver; los
tres siguientes te piden combinar dos ideas; el último es sobre tu propio archivo.

## Para calentar

### Ejercicio 1 · Una Series con etiquetas

Arma una `Series` con las ventas de los seis primeros meses del año, usando las etiquetas
de mes como índice. Imprime el total, el promedio redondeado a dos decimales, y el nombre
del mes más flojo. Después súbele 8 % a todos los meses de una sola operación.

### Ejercicio 2 · Un DataFrame desde cero

Construye un `DataFrame` con cinco productos de una cafetería: nombre, precio unitario y
piezas vendidas en la semana. Agrega una columna `ingreso` que multiplique precio por
piezas, imprime la tabla ordenada de mayor a menor ingreso, y di cuánto se vendió en total.

Pista: `df.sort_values("ingreso", ascending=False)`.

### Ejercicio 3 · El diagnóstico completo

Escribe una función `diagnosticar(df)` que reciba un DataFrame e imprima, en este orden:
cuántos renglones y columnas tiene, qué tipo tiene cada columna, cuántos valores faltan por
columna, y cuántos renglones duplicados hay. Pruébala con `ventas` y con `regiones`.

### Ejercicio 4 · Las columnas de texto

Recorre las columnas de `ventas` y, para cada una que haya salido de tipo texto, imprime el
nombre y cuántos valores distintos tiene. Después di, en un comentario, cuáles de esas
columnas deberían convertirse a otro tipo y cuáles están bien como texto.

## Para pensarle

### Ejercicio 5 · Cuánto cuesta el dato faltante

Los once renglones sin unidades tienen tres destinos posibles: rellenarlos con cero,
descartarlos, o dejarlos como están. Calcula el promedio de `units` bajo las tres
decisiones y ponlos en la misma salida.

Después contesta en un comentario cuál usarías si el reporte dice "promedio de unidades por
venta", y por qué las otras dos estarían mal ahí.

Pistas: `.fillna(0)`, `.dropna()`, y `.mean()` que por su cuenta ya ignora los faltantes.

### Ejercicio 6 · El tamaño del desastre

Sin limpiar nada todavía, mide cuánto daño haría analizar el archivo tal como está. Cuenta
cuántos renglones traen una versión sucia de `"North"`, o sea cualquier valor de `region`
que no sea exactamente uno de los cuatro nombres correctos.

Después imprime, lado a lado, cuántos renglones cree el archivo que son del norte y cuántos
son de verdad.

Pista: `~ventas["region"].isin([...])` invierte una pertenencia.

### Ejercicio 7 · El empleado más caro por área

Carga `employees.csv`, que trae 120 renglones y sale limpio. Imprime cuántas áreas hay,
cuántas personas tiene cada una, y el salario mensual más alto de la tabla junto con el
identificador de quien lo cobra.

No necesitas agrupar todavía, eso es la sesión 15.3. Con `value_counts`, `max` e `idxmax`
alcanza, y ese es justo el punto del ejercicio.

## Con tus datos

### Ejercicio 8 · Tu propio archivo

Carga con pandas el CSV de tu proyecto y escribe un diagnóstico de media cuartilla que
cubra cuántos renglones tiene, qué tipo infirió cada columna, cuántos valores faltan y
cuántos duplicados hay.

Todavía no limpies nada. Hoy solo se mira y se anota. Por cada columna que salió de tipo
texto, di si eso está bien o si algo hay que convertir.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**Una Series es una columna con índice.** Es la lista de la semana 12 con etiquetas, y todo
lo que aprendiste ahí sigue valiendo aquí. El índice no es adorno: es lo que empareja los
datos cuando combinas dos objetos.

**`read_csv` no adivina lo que no puede.** Infiere tipos bien casi siempre, y no tiene forma
de saber qué querías que significara una celda vacía. Esa decisión es tuya y cambia el
resultado.

**Inspeccionar antes de analizar.** `head`, `info`, `shape` y `describe`. Dos minutos que
evitan un resultado equivocado que se ve razonable, que es la peor clase de resultado
equivocado.

La siguiente sesión es seleccionar, filtrar y limpiar. Ahí se arregla todo lo que hoy
diagnosticamos.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

Compáralas con lo tuyo después de intentarlo. Si tu versión llega al mismo resultado por
otro camino, está bien: aquí no hay una sola forma correcta.

### Ejercicio 1

```python
ventas_mes = pd.Series(
    [42000, 51500, 38900, 60100, 55300, 47800],
    index=["ene", "feb", "mar", "abr", "may", "jun"],
)

print("Total:", ventas_mes.sum())
print("Promedio:", round(ventas_mes.mean(), 2))
print("Mes más flojo:", ventas_mes.idxmin(), "con", ventas_mes.min())

con_aumento = ventas_mes * 1.08
print(con_aumento.round(2))
```

El aumento se aplica a los seis meses en una sola línea. No hace falta un ciclo, y escribir
uno aquí es la señal más común de que alguien sigue pensando en listas.

### Ejercicio 2

```python
cafe = pd.DataFrame({
    "producto": ["Americano", "Capuchino", "Latte", "Concha", "Croissant"],
    "precio": [38.0, 52.0, 55.0, 24.0, 46.0],
    "piezas": [310, 185, 142, 260, 98],
})

cafe["ingreso"] = cafe["precio"] * cafe["piezas"]
print(cafe.sort_values("ingreso", ascending=False))
print("\\nIngreso total:", cafe["ingreso"].sum())
```

`sort_values` devuelve una tabla nueva y deja la original intacta. Si querías que el cambio
se quedara, hay que reasignar: `cafe = cafe.sort_values(...)`. Casi todos los métodos de
pandas se comportan así, y esa es una de las razones por las que la sesión 15.2 empieza
hablando de copias.

### Ejercicio 3

```python
def diagnosticar(df):
    renglones, columnas = df.shape
    print(f"{renglones} renglones y {columnas} columnas")

    print("\\nTipos por columna:")
    print(df.dtypes)

    print("\\nFaltantes por columna:")
    print(df.isna().sum())

    print("\\nRenglones duplicados:", df.duplicated().sum())


diagnosticar(ventas)
print("\\n" + "=" * 40 + "\\n")
diagnosticar(regiones)
```

`regiones` sale limpio: cinco renglones, sin faltantes, sin duplicados. Ese contraste es
útil, porque enseña cómo se ve un archivo sano y te da con qué comparar.

### Ejercicio 4

```python
for nombre in ventas.columns:
    if ventas[nombre].dtype == "object" or ventas[nombre].dtype == "str":
        print(f"{nombre:12} {ventas[nombre].nunique():4} valores distintos")

# date        debería convertirse a fecha, para poder ordenar y agrupar por mes
# region      debería normalizarse a cuatro valores, no convertirse de tipo
# channel     está bien como texto, tres valores y todos consistentes
# product     está bien como texto, cinco valores y todos consistentes
# unit_price  debería convertirse a número, quitando el signo y la coma
```

La comparación contra `"object"` y contra `"str"` cubre las dos versiones de pandas. Si solo
comparas contra una, el ejercicio funciona en tu máquina y falla en la de tu compañero.

### Ejercicio 5

```python
print("Rellenando con cero:", round(ventas["units"].fillna(0).mean(), 2))
print("Descartando:        ", round(ventas["units"].dropna().mean(), 2))
print("Dejándolos como están:", round(ventas["units"].mean(), 2))

print("\\nRenglones que entran en cada cuenta:")
print("Rellenando con cero:", ventas["units"].fillna(0).count())
print("Descartando:        ", ventas["units"].dropna().count())

# Para "promedio de unidades por venta" va 16.12, o sea descartar o dejarlos.
# Rellenar con cero inventa once ventas de cero unidades que nunca ocurrieron,
# y arrastra el promedio hacia abajo por una razón que no está en los datos.
```

Salen 15.57 con ceros y 16.12 en los otros dos casos. La diferencia parece chica hasta que
la multiplicas por el volumen anual.

Fíjate en algo que sorprende: descartar y dejarlos como están dan el **mismo promedio**,
porque `mean` ya ignora los faltantes por su cuenta. Lo que sí cambia entre esos dos es el
conteo, 313 contra 313 aquí, pero en cuanto sumes o dividas por `len(df)` empiezan a
separarse. Esa es la razón por la que hay que decidirlo explícitamente en lugar de confiar
en lo que haga el método.

### Ejercicio 6

```python
CORRECTAS = ["North", "South", "Centre", "West"]

sucios = ~ventas["region"].isin(CORRECTAS)
print("Renglones con una región mal capturada:", sucios.sum())
print(ventas.loc[sucios, "region"].value_counts())

print("\\nLo que el archivo cree:", (ventas["region"] == "North").sum())
print("Lo que de verdad es:  ",
      ventas["region"].str.strip().str.title().eq("North").sum())
```

Veinticuatro renglones traen una versión sucia. El norte real tiene 99 ventas y el archivo
reporta 75, así que un reporte hecho hoy le quita al norte una cuarta parte de su volumen y
se lo reparte a cuatro regiones fantasma.

`.str.strip().str.title()` es un adelanto de la sesión 15.2, y lo usamos aquí solo para
medir. Corregir el archivo es la clase que sigue.

### Ejercicio 7

```python
empleados = pd.read_csv("employees.csv")

print(empleados.shape)
print("\\nÁreas:", empleados["area"].nunique())
print(empleados["area"].value_counts())

mas_alto = empleados["monthly_salary"].idxmax()
print("\\nSalario más alto:", empleados["monthly_salary"].max())
print("Lo cobra:", empleados.loc[mas_alto, "employee_id"],
      "en", empleados.loc[mas_alto, "area"])
```

Cinco áreas, 120 personas, y el salario más alto es 82,700 de `E0003`.

Lo que hace útil este ejercicio es `idxmax`. Devuelve la **etiqueta del renglón** donde está
el máximo, no el máximo, y con esa etiqueta `.loc` te trae el renglón entero. Es el patrón
de "quién tiene el valor más alto", y lo vas a usar en cada reporte del semestre.

### Ejercicio 8

No hay solución publicada porque el archivo es distinto para cada quien. El diagnóstico se
califica sobre cuatro cosas: que estén los cuatro números pedidos, que nombres las columnas
que salieron texto, que digas de cada una si eso está bien, y que no hayas limpiado nada
todavía.
"""),

]

write(OUT / "es" / "w15.1.ipynb", es)


# ════════════════════════════════════════════════════════════════════ ENGLISH

en = [

md("""
# Data Analysis · Week 15, session 1 of 3
## Series, DataFrame and loading files

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

The spreadsheet you already know how to use exists inside Python, and it is called a
DataFrame. This session introduces the two objects the whole of pandas is built on, and a
two-minute habit that separates a correct analysis from one that merely looks correct.

By the end of this notebook you will be able to:

1. Explain what a `Series` is and why it is the week 12 list with labels on top.
2. Build a `DataFrame` from a dictionary of columns and from a file.
3. Load a CSV in one line with `read_csv`, and know what it did to each column.
4. Inspect a file with `head`, `info`, `shape` and `describe`, always in that order.
5. Spot missing values, duplicated rows and badly captured categories before they ruin a
   result.

### How to use this notebook

Run the cells in order, top to bottom. Several depend on a variable the previous one
defined, so skipping one gives you a `NameError` that has nothing to do with the topic.

Before running a cell marked **Predict**, write your answer down on paper. Getting the
prediction wrong and understanding why teaches more than seeing the right output first
time.

Three cells fail on purpose. They carry a comment saying so, and they catch the error so
the notebook keeps running.
"""),

md("""
---
## Setup

Two starting cells. The first tells you which pandas version you got, the second puts the
data within reach.
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

md("""
### What to expect from your version

Colab updates its libraries when it feels like it, so the number above may be 2.x or 3.x.
For this session it matters for exactly one thing: what the type of a text column is
called.

| | pandas 2.x | pandas 3.0 and later |
|---|---|---|
| A text column reports | `object` | `str` |
| `info()` ends with | `dtypes: float64(1), object(5)` | `dtypes: float64(1), str(5)` |

Same data, same behaviour, different name. `object` was the drawer where pandas kept
anything that was not a number; since version 3.0 text has its own type and no longer
shares a drawer with anyone. If your output says `object` where this notebook says `str`,
nothing went wrong.
"""),

bootstrap_cell("en"),

# ──────────────────────────────────────────────────────────── block 1

md("""
---
# Block 1 · The two objects

All of pandas is built on two things, and you already know both of them under another name.
One is the column. The other is the whole sheet.

| In the sheet | In pandas | What you already knew |
|---|---|---|
| One column | `Series` | A list, with an index |
| The whole sheet | `DataFrame` | Several paired lists |
| The row number | The index | The position, starting at 0 |
| The header | `columns` | The keys of a dictionary |

The mapping is exact, and that is why this course can jump straight to pandas without
stopping at an intermediate library.

## A Series is a column

The simplest way to make one is from a list.
"""),

code("""
units = pd.Series([15, 8, 22, 5, 11])
print(units)
"""),

md("""
Two things came back that the list did not have.

On the left there is an **index**, 0 to 4, which pandas created for you. At the bottom
there is a **dtype**, the type shared by every value in the column. A Python list can mix
integers with text; a Series cannot, and nearly all of its speed comes from that.
"""),

code("""
print("The index:", list(units.index))
print("The dtype:", units.dtype)
print("The length:", len(units))
"""),

md("""
The index does not have to be a counter. Give it labels and the Series starts behaving like
a named range in your spreadsheet.
"""),

code("""
monthly = pd.Series(
    [42000, 51500, 38900, 60100, 55300, 47800],
    index=["jan", "feb", "mar", "apr", "may", "jun"],
)
print(monthly)
"""),

md("""
Now a value is reached by its label rather than by counting positions. That is the
difference between writing `monthly["mar"]` and remembering that March was the third one,
or the second if you count from zero.
"""),

code("""
print("March:", monthly["mar"])
print("The first three months:")
print(monthly[["jan", "feb", "mar"]])
"""),

md("""
The summary functions you use in the sheet are methods on the Series. Same arithmetic,
written a different way.
"""),

code("""
print("Total:     ", monthly.sum())
print("Average:   ", round(monthly.mean(), 2))
print("Best month:", monthly.idxmax(), "with", monthly.max())
print("Worst month:", monthly.idxmin(), "with", monthly.min())
"""),

md("""
### The big change: the operation applies to the whole column

An operation on a Series reaches every value at once. There is no `for`, and nothing to
drag down. This is the single biggest change in how you will work from here on.
"""),

code("""
with_tax = monthly * 1.16
print(with_tax.round(2))
"""),

md("""
Comparison works the same way, and gives back a Series of trues and falses. That boolean
Series is what will later filter rows, so it is worth seeing on its own before it appears
inside a bracket.
"""),

code("""
good = monthly > 50000
print(good)
print()
print("Months above fifty thousand:", good.sum())
print(monthly[good])
"""),

md("""
### The edge case: two Series with different indexes

This is where the index stops being decoration. When you add two Series, pandas does not
pair them up by position, it pairs them by label. If a label exists in only one of the two,
the result in that row is `NaN`, which is how pandas writes "no data here".

**Predict before you run.** The first Series has January, February and March. The second
has February, March and April. How many rows does the result have, and what is in each one?
"""),

code("""
first = pd.Series([100, 200, 300], index=["jan", "feb", "mar"])
second = pd.Series([10, 20, 30], index=["feb", "mar", "apr"])

print(first + second)
"""),

md("""
Four rows came back and not three, because pandas kept the union of both sets of labels.
January and April came back as `NaN` because each was missing its partner. February and
March did add up.

This is correct, and it is what you want almost every time, but it surprises people once.
If you expected three numbers and got four with two holes in them, the index is the reason,
not the addition.

## A DataFrame is several Series sharing one index

The usual way to build one is from a dictionary, with one key per column.
"""),

code("""
demo = pd.DataFrame({
    "month": ["jan", "feb", "mar", "apr", "may", "jun"],
    "region": ["North", "North", "South", "South", "Centre", "Centre"],
    "amount": [42000, 51500, 38900, 60100, 55300, 47800],
    "units": [15, 18, 12, 21, 19, 16],
})
print(demo)
"""),

code("""
print("Shape (rows, columns):", demo.shape)
print("Column names:", list(demo.columns))
print("Index:", list(demo.index))
"""),

md("""
Each column is a Series, and you pull it out by name. The fact that its type is literally
`Series` is what makes everything from the previous block keep working here.
"""),

code("""
print(demo["amount"])
print()
print("Its type:", type(demo["amount"]))
"""),

code("""
print(demo.dtypes)
"""),

md("""
The `dtypes` tell you how pandas understood each column. `month` and `region` hold text,
`amount` and `units` hold integers. This example was built by hand and so it came out
clean. A real file is where the surprises start, and that is what block 3 is about.

### A new column built from the others

Assigning to a name that does not exist yet creates the column. The right-hand side is
computed for every row at once, which is exactly what a formula filled down does.
"""),

code("""
demo["price_per_unit"] = (demo["amount"] / demo["units"]).round(2)
print(demo)
"""),

md("""
And a variant the slide had no room for: the new column can come from a comparison, not
only from a division. Here it marks the months that cleared fifty thousand.
"""),

code("""
demo["good_month"] = demo["amount"] > 50000
print(demo[["month", "amount", "good_month"]])
print()
print("How many good ones:", demo["good_month"].sum())
"""),

# ──────────────────────────────────────────────────────────── block 2

md("""
---
# Block 2 · Loading the file

Last week you opened a CSV by hand with the `csv` module: open the file, read the header,
walk the rows and convert each field. `read_csv` does all of that in one line.

It is worth running both versions back to back, because the comparison is the whole argument
for pandas.

## The version by hand, from week 14
"""),

code("""
import csv

with open("sales.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

for row in rows:
    row["units"] = int(row["units"] or 0)

print(len(rows), "rows")
print(rows[0])
"""),

md("""
It works, and every row came back as a dictionary. The problem is not that it is long, it is
that you made a hidden decision: `int(row["units"] or 0)` turned the blank cells into zero.
That changes the average, and nobody is going to notice by reading the code.

## The version with pandas
"""),

code("""
sales = pd.read_csv("sales.csv")

print(sales.shape)
"""),

md("""
One line, and on top of that `read_csv` tried to infer the type of every column. What it
cannot infer is what you wanted a blank cell to mean, which is why it does not fill it with
zero: it marks the cell as missing and leaves the decision to you. That decision is session
15.2.

### One detail that pays off all term

`read_csv` takes a URL anywhere it takes a path. With the repository public, loading the
course data from any machine looks like this, with nothing downloaded by hand:

```python
BASE = ("https://raw.githubusercontent.com/Davidowa/learning-hub/main/"
        "docs/en/courses/python-course/06%20-%20Advanced/data/")

sales = pd.read_csv(BASE + "sales.csv")
```

The setup cell in this notebook tries exactly that before rebuilding the files on its own.

## The first rows
"""),

code("""
print(sales.head())
"""),

md("""
`head` shows the first five rows. Pass it a number to change how many.
"""),

code("""
print(sales.head(3))
"""),

md("""
`tail` shows the last ones, and it is the one to run even when it feels redundant. That is
where the totals row somebody pasted at the bottom of the sheet before exporting it hides,
and if you do not see it, it ends up counted as one more sale.
"""),

code("""
print(sales.tail(3))
"""),

md("""
`shape` answers how much data you actually have. It returns a tuple, so it can be unpacked
into two names.
"""),

code("""
rows_n, columns_n = sales.shape
print(f"{rows_n} rows and {columns_n} columns")
"""),

# ──────────────────────────────────────────────────────────── block 3

md("""
---
# Block 3 · Look before touching

The temptation is to jump straight to the answer. Hold off for two minutes. Almost every
wrong result in the final project traces back to a column that was not the type you
assumed, or to rows that were not there.

The order is always the same: `head`, `info`, `shape`, `describe`.

## The types it inferred
"""),

code("""
print(sales.dtypes)
"""),

md("""
`info` is the most useful command in this session. It reports, per column, how many values
are not empty and what type pandas inferred. Watch the `Non-Null Count` column: one that
does not reach the total number of rows has holes in it.
"""),

code("""
sales.info()
"""),

md("""
### What those types are telling you

Three things in that output deserve to be named.

**`units` came in as `float64` and not as a whole number.** pandas read the digits fine, but
eleven cells are blank, and a blank has to be represented somehow. That marker is `NaN`,
which only exists in a decimal column, so the whole column became decimal. This is why the
counts print as `15.0` instead of `15`.

**`unit_price` came in as text**, because `"$ 2,082.50"` is not a number to Python. The
currency symbol and the thousands comma are formatting, and formatting is not part of the
value.

**`date` came in as text**, because a CSV has no date type. Until it is converted, sorting
by that column works by luck: it only comes out right because the format puts the year
first.

None of the three is a pandas failure. It is the CSV, which stores no types, exactly as you
saw last week. Session 15.2 fixes all three.

## The numeric summary
"""),

code("""
print(sales.describe())
"""),

md("""
`describe` gives count, mean, standard deviation, minimum, maximum and the quartiles for
every numeric column. So far only `units` qualifies, and its count of 313 against 324 rows
is the missing data showing up again.

That is why `describe` says so little on a freshly loaded file: it is not that there are no
numbers, it is that they are stored as text. With `include="all"` pandas summarises the text
columns too, using different statistics.
"""),

code("""
print(sales.describe(include="all"))
"""),

md("""
Two rows of that table are worth a look. `unique` counts how many distinct values the column
holds, and `top` names the one that repeats most. `region` reports eight distinct values,
and the company has four regions.

## Finding the dirt

For a text column, what helps is counting how many times each value appears.
"""),

code("""
print(sales["region"].value_counts())
"""),

md("""
Four regions were captured and the file thinks there are eight, because the same name was
typed with different capitalisation and with stray spaces. `" North"`, `"North "`, `"north"`
and `"NORTH"` are, to Python, four strings with nothing to do with each other.

Group by region today and the north splits into five pieces, none of which carries the real
total. Session 15.2 fixes it, and today's point is that you catch it before it happens.
"""),

code("""
print("Distinct values in region:", sales["region"].nunique())
print("Distinct values in channel:", sales["channel"].nunique())
print("Distinct values in product:", sales["product"].nunique())
"""),

md("""
`isna` marks every missing cell as true, and `sum` counts them per column.
"""),

code("""
print(sales.isna().sum())
print()
print("Missing across the whole table:", sales.isna().sum().sum())
"""),

md("""
`duplicated` marks a row as true when an identical row appeared earlier. The seven here are
the trace of a copy and paste.
"""),

code("""
print("Duplicated rows:", sales.duplicated().sum())
print()
print(sales[sales.duplicated(keep=False)].sort_values("date").head(6))
"""),

md("""
Note the `keep=False` on that last line: with that argument pandas marks every copy, not
only the repeats, so you can see the full pairs and confirm they really are identical.

And mind the arithmetic. 324 rows with seven duplicates are 317 distinct facts. Which of the
two numbers belongs in your report depends on what you are counting, and deciding that is
your job, not pandas'.
"""),

# ──────────────────────────────────────────────────────── deliberate failures

md("""
---
## Three cells that fail on purpose

A wrong type does not always blow up. Sometimes it hands you a number, and that is the
dangerous case.

### The one that does not fail, which is why it is the worst
"""),

code("""
# FAILS ON PURPOSE. This cell raises nothing at all, and that is exactly the problem.
# unit_price is text, so sum() concatenates instead of adding.
total = sales["unit_price"].sum()

print("Type of the result:", type(total))
print("First 70 characters:", str(total)[:70])
"""),

md("""
You asked for a sales total and received all 324 prices glued one after another into a
single string. No error, no warning. If this sits inside a longer report, it gets published.

This is the entire argument for running `info()` before analysing. Two minutes of inspection
against a wrong number in a presentation.

### The one that does fail, and warns you in time
"""),

code("""
# FAILS ON PURPOSE. Averaging text does raise, unlike adding it.
try:
    sales["unit_price"].mean()
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`mean` has no way to invent an average of strings, so it stops. Same problem as the cell
before, with better luck: here the error shows up while you are writing it, not three weeks
later in a meeting.

### The conversion that looks obvious and is not
"""),

code("""
# FAILS ON PURPOSE. units carries eleven NaN, and NaN does not fit in an integer.
try:
    sales["units"].astype(int)
except Exception as e:
    print(type(e).__name__ + ":", e)
"""),

md("""
If seeing `15.0` where you expected `15` bothered you, this is the natural attempt to fix
it, and it does not work. You cannot convert to integer while there are missing values,
because `NaN` is not a representable whole number.

The right order is the opposite of how it feels: first you decide what the eleven holes
mean, then you convert. Filling with zero, dropping those rows, or leaving them missing are
three different decisions with three different averages, and none of them is the default.

## The second table
"""),

code("""
regions = pd.read_csv("regions.csv")
print(regions)
"""),

md("""
This is the course's lookup table, the equivalent of the `VLOOKUP` in your sheet: one row per
region, with the details that have no business repeating in every sales record.

It carries five regions and the sales file only covers four. The difference is deliberate,
and session 15.3 shows what a join does with the region that has no sales.
"""),

# ──────────────────────────────────────────────────────────── predict

md("""
---
## Predict before you run

Write your answer down before executing each cell.

### Question 1

Why did the `units` column come back as `float64` and not `int64`?

- **A.** Because the unit counts carry decimals in the file.
- **B.** Because eleven blank cells need `NaN`, which only exists in float.
- **C.** Because `read_csv` always uses float to be safe.
- **D.** Because the column has more than three hundred rows.
"""),

code("""
print("dtype of units:      ", sales["units"].dtype)
print("Missing in units:    ", sales["units"].isna().sum())
print("Any value with a decimal part?")
print((sales["units"].dropna() % 1 != 0).sum(), "out of", sales["units"].notna().sum())
"""),

md("""
Zero values with a decimal part, and eleven missing. The answer is **B**: the numbers were
whole from the start, and what forced the decimal type was the marker for blank.

### Question 2

`sales.shape` said 324 rows. How many distinct sales does the file describe, and how many
have their unit count on record?
"""),

code("""
print("Rows:                     ", len(sales))
print("Not counting duplicates:  ", len(sales.drop_duplicates()))
print("With units recorded:      ", sales["units"].notna().sum())
print("Distinct and with units:  ", len(sales.drop_duplicates().dropna(subset=["units"])))
"""),

md("""
Four different numbers, all correct, all answers to different questions. Which one to use
depends on what you claim in the report, and that is why `shape` is not "the number of data"
but the first of several.

### Question 3

What does the next cell print? Think about what type `sales["units"]` has and what type
`sales[["units"]]` has.
"""),

code("""
print(type(sales["units"]))
print(type(sales[["units"]]))
print()
print(sales[["date", "region", "units"]].head(3))
"""),

md("""
One bracket gives back a `Series`, the column on its own. Two brackets give back a
`DataFrame`, because what you passed was a list of names and a list can carry more than one.
It is the most common confusion of the next two sessions, and you have now seen it with both
types printed out.
"""),

# ──────────────────────────────────────────────────────────── pitfalls

md("""
---
## Four errors when loading a file

**Analysing before inspecting.** The result comes out, it looks reasonable, and it is wrong.
`head`, `info` and `describe` cost two minutes and are the only defence against the bug
nobody finds because nobody is looking for it.

**Trusting the inferred type.** pandas guesses right nearly every time. That *nearly* is
where the price column that turned out to be text lives.

**Not checking the categories.** `value_counts` on a text column exposes inconsistent capture
before it splits your groups into five pieces.

**Taking `shape` as the number of facts.** 324 rows with seven duplicates are 317 distinct
facts, and the total changes with which one you count.
"""),

# ──────────────────────────────────────────────────────────── exercises

md("""
---
# Exercises

Solve them in new cells below each brief. The solutions sit at the very bottom of the
notebook, so you cannot catch them out of the corner of your eye while you work.

They run from lighter to heavier. The first four repeat what you just saw with different
data; the next three ask you to combine two ideas; the last one is about your own file.

## Warming up

### Exercise 1 · A Series with labels

Build a `Series` with the sales for the first six months of the year, using the month labels
as the index. Print the total, the average rounded to two decimals, and the name of the
weakest month. Then add 8 % to every month in a single operation.

### Exercise 2 · A DataFrame from scratch

Build a `DataFrame` with five products from a coffee shop: name, unit price and pieces sold
during the week. Add an `income` column that multiplies price by pieces, print the table
sorted from highest to lowest income, and say how much was sold in total.

Hint: `df.sort_values("income", ascending=False)`.

### Exercise 3 · The full diagnosis

Write a function `diagnose(df)` that takes a DataFrame and prints, in this order: how many
rows and columns it has, what type each column holds, how many values are missing per
column, and how many duplicated rows there are. Test it with `sales` and with `regions`.

### Exercise 4 · The text columns

Walk the columns of `sales` and, for each one that came back as text, print the name and how
many distinct values it holds. Then say, in a comment, which of those columns should be
converted to another type and which are fine as text.

## Worth thinking about

### Exercise 5 · What the missing value costs

The eleven rows with no unit count have three possible fates: fill them with zero, drop
them, or leave them alone. Work out the average of `units` under all three decisions and
print them in the same output.

Then answer in a comment which one you would use if the report says "average units per
sale", and why the other two would be wrong there.

Hints: `.fillna(0)`, `.dropna()`, and `.mean()`, which already ignores missing values on its
own.

### Exercise 6 · The size of the mess

Without cleaning anything yet, measure how much damage analysing the file as it stands would
do. Count how many rows carry a dirty version of `"North"`, meaning any `region` value that
is not exactly one of the four correct names.

Then print, side by side, how many rows the file thinks are northern and how many really
are.

Hint: `~sales["region"].isin([...])` inverts a membership test.

### Exercise 7 · The highest paid employee

Load `employees.csv`, which has 120 rows and comes out clean. Print how many areas there
are, how many people each one holds, and the highest monthly salary in the table along with
the identifier of whoever earns it.

You do not need to group yet, that is session 15.3. `value_counts`, `max` and `idxmax` are
enough, and that is exactly the point of the exercise.

## With your own data

### Exercise 8 · Your own file

Load your project CSV with pandas and write a half-page diagnosis covering how many rows it
has, what type each column was inferred as, how many values are missing and how many
duplicates there are.

Do not clean anything yet. Today is only looking and writing down. For every column that
came back as text, say whether that is right or whether something needs converting.
"""),

# ──────────────────────────────────────────────────────────── summary

md("""
---
## Three ideas to take away

**A Series is a column with an index.** It is the week 12 list with labels, and everything
you learned there still holds here. The index is not decoration: it is what lines the data
up when you combine two objects.

**`read_csv` cannot guess what it cannot guess.** It infers types well nearly always, and it
has no way of knowing what you wanted a blank cell to mean. That decision is yours and it
changes the result.

**Inspect before analysing.** `head`, `info`, `shape` and `describe`. Two minutes that
prevent a wrong result that looks reasonable, which is the worst kind of wrong result.

Next session is selecting, filtering and cleaning. That is where everything diagnosed today
gets fixed.
"""),

# ──────────────────────────────────────────────────────────── solutions

md("""
---
# Solutions

Compare them with yours after you have tried. If your version reaches the same result by a
different route, that is fine: there is no single correct way here.

### Exercise 1

```python
monthly_sales = pd.Series(
    [42000, 51500, 38900, 60100, 55300, 47800],
    index=["jan", "feb", "mar", "apr", "may", "jun"],
)

print("Total:", monthly_sales.sum())
print("Average:", round(monthly_sales.mean(), 2))
print("Weakest month:", monthly_sales.idxmin(), "with", monthly_sales.min())

with_raise = monthly_sales * 1.08
print(with_raise.round(2))
```

The raise applies to all six months in a single line. No loop is needed, and writing one
here is the most common sign that somebody is still thinking in lists.

### Exercise 2

```python
shop = pd.DataFrame({
    "product": ["Americano", "Cappuccino", "Latte", "Sweet bread", "Croissant"],
    "price": [38.0, 52.0, 55.0, 24.0, 46.0],
    "pieces": [310, 185, 142, 260, 98],
})

shop["income"] = shop["price"] * shop["pieces"]
print(shop.sort_values("income", ascending=False))
print("\\nTotal income:", shop["income"].sum())
```

`sort_values` gives back a new table and leaves the original untouched. If you wanted the
change to stick, you have to reassign: `shop = shop.sort_values(...)`. Nearly every pandas
method behaves this way, and that is one of the reasons session 15.2 opens by talking about
copies.

### Exercise 3

```python
def diagnose(df):
    rows_n, columns_n = df.shape
    print(f"{rows_n} rows and {columns_n} columns")

    print("\\nTypes per column:")
    print(df.dtypes)

    print("\\nMissing per column:")
    print(df.isna().sum())

    print("\\nDuplicated rows:", df.duplicated().sum())


diagnose(sales)
print("\\n" + "=" * 40 + "\\n")
diagnose(regions)
```

`regions` comes out clean: five rows, nothing missing, nothing duplicated. That contrast is
useful, because it shows what a healthy file looks like and gives you something to compare
against.

### Exercise 4

```python
for name in sales.columns:
    if sales[name].dtype == "object" or sales[name].dtype == "str":
        print(f"{name:12} {sales[name].nunique():4} distinct values")

# date        should be converted to a date, so it can be sorted and grouped by month
# region      should be normalised to four values, not converted to another type
# channel     fine as text, three values and all of them consistent
# product     fine as text, five values and all of them consistent
# unit_price  should be converted to a number, dropping the sign and the comma
```

Comparing against both `"object"` and `"str"` covers the two pandas versions. Compare against
only one and the exercise works on your machine and fails on your classmate's.

### Exercise 5

```python
print("Filling with zero:", round(sales["units"].fillna(0).mean(), 2))
print("Dropping them:    ", round(sales["units"].dropna().mean(), 2))
print("Leaving them be:  ", round(sales["units"].mean(), 2))

print("\\nRows that enter each count:")
print("Filling with zero:", sales["units"].fillna(0).count())
print("Dropping them:    ", sales["units"].dropna().count())

# For "average units per sale" the answer is 16.12, so drop them or leave them.
# Filling with zero invents eleven sales of zero units that never happened, and
# drags the average down for a reason that is not in the data.
```

You get 15.57 with zeros and 16.12 in the other two cases. The gap looks small until you
multiply it by the annual volume.

Notice something surprising: dropping them and leaving them alone give the **same average**,
because `mean` already ignores missing values on its own. What does change between those two
is the count, 313 against 313 here, but the moment you sum or divide by `len(df)` they start
to diverge. That is why the decision has to be made out loud instead of trusting whatever
the method does.

### Exercise 6

```python
CORRECT = ["North", "South", "Centre", "West"]

dirty = ~sales["region"].isin(CORRECT)
print("Rows with a badly captured region:", dirty.sum())
print(sales.loc[dirty, "region"].value_counts())

print("\\nWhat the file thinks:", (sales["region"] == "North").sum())
print("What is actually true:",
      sales["region"].str.strip().str.title().eq("North").sum())
```

Twenty-four rows carry a dirty version. The real north has 99 sales and the file reports 75,
so a report written today takes a quarter of the north's volume away and hands it to four
phantom regions.

`.str.strip().str.title()` is a preview of session 15.2, and it is used here only to measure.
Fixing the file is next class.

### Exercise 7

```python
employees = pd.read_csv("employees.csv")

print(employees.shape)
print("\\nAreas:", employees["area"].nunique())
print(employees["area"].value_counts())

highest = employees["monthly_salary"].idxmax()
print("\\nHighest salary:", employees["monthly_salary"].max())
print("Earned by:", employees.loc[highest, "employee_id"],
      "in", employees.loc[highest, "area"])
```

Five areas, 120 people, and the highest salary is 82,700, earned by `E0003`.

What makes this exercise worth doing is `idxmax`. It gives back the **row label** where the
maximum sits, not the maximum itself, and with that label `.loc` brings you the whole row.
It is the "who has the highest value" pattern, and you will use it in every report this
term.

### Exercise 8

There is no published solution, because the file is different for everyone. The diagnosis is
graded on four things: that the four requested numbers are there, that you name the columns
that came back as text, that you say for each one whether that is right, and that you have
not cleaned anything yet.
"""),

]

write(OUT / "en" / "w15.1.ipynb", en)

print("wrote", OUT / "es" / "w15.1.ipynb")
print("wrote", OUT / "en" / "w15.1.ipynb")
