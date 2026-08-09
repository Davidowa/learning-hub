"""notebooks/analisis-de-datos/{es,en}/w15.3.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w15.3.*.yaml
Source code:  A05 - Pandas/05_group_and_aggregate.py, 06_merge_and_export.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

# The cleaning from 15.2, compressed into one cell so this notebook stands alone.
LIMPIEZA_ES = """
# La limpieza de la sesión 15.2, en una celda. No es material nuevo: es para que
# este cuaderno se pueda abrir solo, sin depender de que corriste el anterior.
ventas = pd.read_csv("sales.csv").drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["unit_price"] = (ventas["unit_price"]
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.strip()
                        .astype(float))
ventas["date"] = pd.to_datetime(ventas["date"])
ventas = ventas.dropna(subset=["units"])
ventas["units"] = ventas["units"].astype(int)
ventas["amount"] = ventas["units"] * ventas["unit_price"]

ventas.to_csv("sales_clean.csv", index=False)
print(f"{len(ventas)} renglones limpios, total {ventas['amount'].sum():,.2f}")
"""

LIMPIEZA_EN = """
# The cleaning from session 15.2, in one cell. Nothing new here: it is so this
# notebook opens on its own, without depending on you having run the last one.
sales = pd.read_csv("sales.csv").drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip()
                       .astype(float))
sales["date"] = pd.to_datetime(sales["date"])
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

sales.to_csv("sales_clean.csv", index=False)
print(f"{len(sales)} clean rows, total {sales['amount'].sum():,.2f}")
"""

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 15, sesión 3 de 3
## Agrupar, resumir y unir

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Las ochenta líneas que escribiste a mano en la semana 14 caben hoy en ocho, y los números
coinciden hasta el centavo. Vas a ver la tabla dinámica y el `BUSCARV` escritos, y además
una revisión que ninguna hoja de cálculo te deja hacer.

Al terminar este cuaderno vas a poder:

1. Agrupar y resumir en una línea, con `groupby` seguido de la columna y la función.
2. Pedir varios resúmenes a la vez con `agg`, y con nombres de columna que tú eliges.
3. Armar una rejilla con `pivot_table`, incluidos los totales de fila y de columna.
4. Unir dos tablas con `merge`, y explicar por qué el modo izquierdo es el seguro.
5. Auditar una unión con `indicator`, revisando las dos direcciones antes de confiar.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Este cuaderno no depende de que hayas corrido el de la sesión
15.2: la segunda celda repite la limpieza para que puedas abrir este solo.

Tres celdas fallan a propósito y llevan un comentario que lo dice.
"""),

md("""
---
## Preparación
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

bootstrap_cell("es"),

md("""
### La limpieza, otra vez y sin explicación

Agrupar sobre datos sucios es el primer error de esta sesión, así que el archivo se limpia
antes de tocarlo. Si algo de esta celda no se entiende, está explicado paso por paso en la
sesión 15.2.
"""),

code(LIMPIEZA_ES),

# ──────────────────────────────────────────────────────────── bloque 1

md("""
---
# Bloque 1 · Agrupar

`groupby` hace exactamente lo que hace arrastrar un campo a una tabla dinámica: parte los
renglones en montones que comparten un valor, aplica un resumen a cada montón, y vuelve a
juntar los resultados como tabla.

Partir, resumir, juntar. Eso es todo.

## Ochenta líneas, u ocho

Primero la versión de la semana 14, con un diccionario y un ciclo. Corre de verdad, sobre el
archivo limpio que acabas de escribir.
"""),

code("""
import csv
from collections import defaultdict

por_region_manual = defaultdict(float)

with open("sales_clean.csv", encoding="utf-8") as f:
    for registro in csv.DictReader(f):
        por_region_manual[registro["region"]] += float(registro["amount"])

for region in sorted(por_region_manual, key=por_region_manual.get, reverse=True):
    print(f"{region:8} {por_region_manual[region]:>12,.2f}")
"""),

md("""
Ahora lo mismo con pandas.
"""),

code("""
por_region = ventas.groupby("region")["amount"].sum()

print(por_region.sort_values(ascending=False).round(2))
"""),

md("""
Los mismos cuatro totales, hasta el centavo. La diferencia es que uno se lee de un vistazo y
el otro hay que revisarlo renglón por renglón para creerle.

Vale la pena comprobarlo en lugar de tomármelo de palabra.
"""),

code("""
iguales = all(
    round(por_region_manual[region], 2) == round(por_region[region], 2)
    for region in por_region.index
)
print("¿Coinciden los cuatro totales?", iguales)
"""),

md("""
El resultado de `groupby` es una `Series` cuyo índice es aquello por lo que agrupaste, así
que todo lo de la sesión 15.1 sigue sirviendo aquí.
"""),

code("""
print("Mejor región:", por_region.idxmax())
print("Su parte del año:", f"{por_region.max() / ventas['amount'].sum():.1%}")
print()
print("Las cuatro, en miles:")
print((por_region.sort_values(ascending=False) / 1000).round(0))
"""),

md("""
## Varios resúmenes a la vez

`agg` recibe una lista de funciones y devuelve una columna por cada una. Contesta cuánto,
cuántas veces y de qué tamaño en una sola pasada.
"""),

code("""
resumen = ventas.groupby("region")["amount"].agg(["sum", "count", "mean"]).round(2)

print(resumen.sort_values("sum", ascending=False))
"""),

md("""
Resúmenes distintos para columnas distintas, con los nombres que tú elijas. El patrón es
`nombre_nuevo=("columna de origen", "función")`, y es como se arma una tabla de reporte en
una sola instrucción.
"""),

code("""
detalle = ventas.groupby("region").agg(
    ingreso=("amount", "sum"),
    unidades=("units", "sum"),
    ventas_hechas=("amount", "count"),
    promedio=("amount", "mean"),
).round(2)

print(detalle.sort_values("ingreso", ascending=False))
"""),

md("""
### Aquí está la historia

Fíjate bien en esa tabla antes de seguir. **North vende más que nadie, y Centre tiene la
venta promedio más alta.** North hizo 92 ventas de 47 mil en promedio; Centre hizo 70 de 56
mil.

Son dos negocios distintos con el mismo ingreso aparente, y esa diferencia no se ve en un
total. `sum` contesta magnitud y `count` contesta frecuencia, que son las dos preguntas de
la semana 9, y hace falta hacer las dos para entender qué pasó.
"""),

code("""
print("Ventas hechas por región:")
print(detalle["ventas_hechas"].sort_values(ascending=False))
print()
print("Tamaño promedio de la venta:")
print(detalle["promedio"].sort_values(ascending=False).round(0))
"""),

md("""
## Dos campos de agrupación

Pásale una lista y los montones se vuelven cada combinación de los dos campos.
"""),

code("""
por_region_canal = ventas.groupby(["region", "channel"])["amount"].sum().round(2)

print(por_region_canal)
"""),

md("""
Doce renglones, uno por combinación. Se lee como una lista larga, y ese es justamente el
problema que resuelve el bloque siguiente.
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · La rejilla

`pivot_table` acomoda esos mismos números como cuadrícula, que es la forma en que los ves en
pantalla cuando abres una tabla dinámica.

Cuatro argumentos, y cada uno corresponde a algo que arrastrarías con el ratón:

| Argumento | Qué es | En la tabla dinámica |
|---|---|---|
| `index` | Lo que baja por el lado | El campo que arrastras a las filas |
| `columns` | Lo que cruza arriba | El campo que arrastras a las columnas |
| `values` | Lo que llena las celdas | El campo de valores |
| `aggfunc` | Cómo se resumen | Configuración del campo de valor |
"""),

code("""
rejilla = ventas.pivot_table(
    index="region",      # lo que baja por el lado
    columns="channel",   # lo que cruza arriba
    values="amount",     # lo que llena las celdas
    aggfunc="sum",       # cómo se resumen
)

print((rejilla / 1000).round(0))
"""),

md("""
Los mismos doce números del bloque anterior, ahora legibles de un vistazo. En miles, para que
quepan.

## La trampa del `aggfunc`

**Predice antes de correr.** ¿Qué devuelve `pivot_table` si no dices `aggfunc`?

- **A.** La suma por región y canal.
- **B.** El promedio, que es lo que hace por omisión.
- **C.** El conteo de renglones.
- **D.** Un error, porque `aggfunc` es obligatorio.
"""),

code("""
# FALLA A PROPÓSITO. No lanza error: da otro número, que es peor.
sin_aggfunc = ventas.pivot_table(
    index="region",
    columns="channel",
    values="amount",
)

print("Sin aggfunc, celda Centre/Online:", round(sin_aggfunc.loc["Centre", "Online"], 2))
print("Con sum,      celda Centre/Online:", round(rejilla.loc["Centre", "Online"], 2))
print()
print("¿Cuántas veces más grande es la suma?",
      round(rejilla.loc["Centre", "Online"] / sin_aggfunc.loc["Centre", "Online"], 1))
"""),

md("""
La respuesta es **B**. Por omisión `pivot_table` promedia, no suma.

Y ahí está el peligro: no lanza error, devuelve una rejilla con la misma forma y los mismos
encabezados, con números treinta veces más chicos. Si esperabas totales y no dijiste
`aggfunc`, tu reporte sale mal y se ve perfectamente bien.

El número por el que difieren no es casualidad: es cuántas ventas cayeron en esa celda.

## Los totales
"""),

code("""
con_totales = ventas.pivot_table(
    index="region", columns="channel", values="amount",
    aggfunc="sum", margins=True, margins_name="Total",
)

print((con_totales / 1000).round(0))
"""),

md("""
`margins=True` agrega los totales de fila y de columna, igual que el total general de una
tabla dinámica. El número de hasta abajo a la derecha tiene que coincidir con el total de la
tabla, y comprobarlo es la forma más rápida de saber si se perdió algo por el camino.
"""),

code("""
esquina = con_totales.loc["Total", "Total"]
tabla = ventas["amount"].sum()

print(f"Esquina de la rejilla: {esquina:,.2f}")
print(f"Total de la tabla:     {tabla:,.2f}")
print("¿Coinciden?", round(esquina, 2) == round(tabla, 2))
"""),

md("""
## Agrupar por tiempo

Una columna de fecha se puede agrupar por cualquier parte de sí misma. `.dt` entra en la
fecha igual que `.str` entra en el texto.
"""),

code("""
ventas["month"] = ventas["date"].dt.month
mensual = ventas.groupby("month")["amount"].sum().round(2)

print((mensual / 1000).round(0))
print()
print("Mejor mes:", mensual.idxmax(), "| peor mes:", mensual.idxmin())
"""),

md("""
Diciembre manda con más del doble de casi cualquier otro mes, y julio es el más flojo. Ese
patrón solo aparece cuando agrupas: en la tabla renglón por renglón no se ve.

Ahora, cuidado con la lectura fácil. El archivo trae dentro una curva estacional que sube en
noviembre y diciembre, y aun así noviembre salió abajo. La razón es que unas pocas ventas de
máquina de espresso, que es el producto caro, pesan más que la estacionalidad de todo el
resto. Un total esconde su composición, y es exactamente por eso que `agg` con `count` al
lado de `sum` vale la pena.
"""),

code("""
print("Ingreso y número de ventas por mes:")
print(ventas.groupby("month").agg(
    ingreso=("amount", "sum"),
    ventas=("amount", "count"),
    ticket=("amount", "mean"),
).round(0).sort_values("ingreso", ascending=False).head())
"""),

md("""
Diciembre tuvo un ticket promedio muy por encima del resto, no muchas más ventas. El mes no
fue mejor porque se vendiera más seguido, sino porque se vendió más caro.

Trimestre, año y día de la semana funcionan igual.
"""),

code("""
por_trimestre = ventas.groupby(ventas["date"].dt.quarter)["amount"].sum().round(2)
print("Por trimestre, en miles:")
print((por_trimestre / 1000).round(0))

print()
print("Por día de la semana, en miles:")
print((ventas.groupby(ventas["date"].dt.day_name())["amount"].sum() / 1000).round(0))
"""),

md("""
El día de la semana sale con un solo valor porque el archivo se generó con una venta por
semana, todos los lunes. Es un buen recordatorio de que una agrupación no inventa variedad
donde no la hay, y de que conviene mirar el resultado antes de sacar conclusiones.

## Lo más vendido de cada grupo

Una pregunta que sale en todo reporte: qué producto vende más en cada región. Se agrupa por
los dos, se totaliza, y se toma el mayor de cada región.
"""),

code("""
producto_region = ventas.groupby(["region", "product"])["amount"].sum()
mejor_por_region = producto_region.loc[producto_region.groupby("region").idxmax()]

print(mejor_por_region.round(2))
"""),

md("""
La línea del medio se lee de adentro hacia afuera: `groupby("region").idxmax()` devuelve, por
cada región, la etiqueta completa del renglón más grande, y `loc` va por esos renglones. Es
el mismo `idxmax` de la sesión 15.1, aplicado a un índice de dos niveles.
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · Unir dos tablas

`merge` es el `BUSCARV`, con dos diferencias que importan. Trae todas las columnas de golpe
en lugar de una por fórmula, y te dice qué no encontró en vez de dejar `#N/A` regados por la
hoja.

| Modo | Qué conserva | Cuándo |
|---|---|---|
| `left` | Todos los renglones de la izquierda | El seguro, y el que imita a `BUSCARV` |
| `inner` | Solo los que coinciden | Cuando lo que no cruza no interesa |
| `right` | Todos los de la derecha | Raro, es un `left` al revés |
| `outer` | Todos los de ambos lados | Para auditar qué no coincidió |
"""),

code("""
regiones = pd.read_csv("regions.csv")

print(regiones)
print()
print("Ventas:", ventas.shape, "| Regiones:", regiones.shape)
"""),

md("""
`on` nombra la columna que las dos tablas comparten. Cada renglón de `regiones` que coincida
se pega al renglón de ventas, trayendo todas sus columnas con él.
"""),

code("""
unida = ventas.merge(regiones, on="region", how="left")

print("Después de la unión:", unida.shape)
print(unida[["date", "region", "amount", "manager", "monthly_target"]].head(3))
"""),

md("""
`how="left"` conserva todos los renglones de ventas, encuentre o no pareja el catálogo. Ese
es el comportamiento del `BUSCARV` y es el valor seguro: nunca pierdes una venta en silencio
porque su región faltaba en el catálogo.

Fíjate en la forma: 306 renglones antes, 306 después. Si ese número hubiera cambiado, algo
pasó que hay que entender antes de seguir.

## La auditoría, que es lo que ninguna hoja te deja hacer
"""),

code("""
auditoria = ventas.merge(regiones, on="region", how="outer", indicator=True)

print(auditoria["_merge"].value_counts())
"""),

md("""
`how="outer"` conserva todo de ambos lados, y la columna `_merge` dice de dónde vino cada
renglón. Las dos direcciones se revisan por separado y significan cosas distintas.

**`right_only` en uno** significa que el catálogo tiene una región sin ninguna venta. Casi
siempre está bien: una plaza nueva, o una que cerró.

**`left_only` en cero** significa que ninguna venta quedó huérfana. Eso sí importa: una venta
con una región que el catálogo no conoce es un problema de datos que hay que reportar, no
tapar.
"""),

code("""
huerfanas = auditoria[auditoria["_merge"] == "right_only"]["region"].unique()
print("Regiones del catálogo sin ninguna venta:", list(huerfanas))

sin_catalogo = auditoria[auditoria["_merge"] == "left_only"]["region"].unique()
print("Ventas con una región que el catálogo no conoce:", list(sin_catalogo) or "ninguna")
"""),

md("""
Con una fórmula tendrías que contar los `#N/A` a mano, y solo en una dirección. Aquí el
conteo viene incluido y cubre las dos.

## Usar lo que trajo la unión

Ahora que cada renglón conoce su meta, la comparación es una columna normal.
"""),

code("""
mensual_region = (
    unida.assign(month=unida["date"].dt.month)
    .groupby(["region", "manager", "monthly_target", "month"])["amount"]
    .sum()
    .reset_index()
)

mensual_region["cumplio"] = mensual_region["amount"] >= mensual_region["monthly_target"]
mensual_region["avance"] = (mensual_region["amount"] / mensual_region["monthly_target"]).round(3)

print(mensual_region.head())
"""),

md("""
`reset_index` convierte el índice de la agrupación de vuelta en columnas normales. Sin él,
`region`, `manager`, `monthly_target` y `month` seguirían siendo índice y no se podrían usar
en una comparación.

Y con eso ya se puede armar el tablero.
"""),

code("""
tablero = (
    mensual_region.groupby(["region", "manager"])
    .agg(meses=("cumplio", "count"),
         meses_en_meta=("cumplio", "sum"),
         avance_promedio=("avance", "mean"))
    .round(3)
    .sort_values("avance_promedio", ascending=False)
)

print(tablero)
"""),

md("""
Ninguna región llegó a su meta más de tres meses de doce, y la mejor promedia 76 % de avance.
Eso no lo dice ninguna de las dos tablas por separado: `ventas` no conoce las metas y
`regiones` no conoce las ventas. Sale de haberlas unido.

## Cuando la llave se llama distinto en cada tabla

Se nombran los dos lados. Aquí las dos se llaman `region`, así que el ejemplo renombra una de
paso para que se vea la forma.
"""),

code("""
codigos = regiones.rename(columns={"region": "region_code"})
ejemplo = ventas.merge(codigos, left_on="region", right_on="region_code", how="left")

print("Unida con llaves de distinto nombre:", ejemplo.shape)
print(ejemplo[["region", "region_code", "manager"]].head(3))
"""),

md("""
Nota que quedaron las dos columnas de llave, `region` y `region_code`, con el mismo
contenido. Es lo normal, y si estorban se quitan con `drop`.

## Exportar

El análisis termina donde empezó, como un archivo que alguien más puede abrir.
"""),

code("""
tablero.to_csv("tablero.csv")

print("Escrito tablero.csv")
print(open("tablero.csv", encoding="utf-8").read())
"""),

md("""
Para Excel, que es donde esto suele tener que acabar, se usa un `ExcelWriter` cuando son
varias hojas. Necesita el paquete `openpyxl`, que Colab ya trae instalado.
"""),

code("""
# Si openpyxl faltara, pandas lanza ImportError nombrándolo. Colab ya lo trae.
try:
    with pd.ExcelWriter("reporte.xlsx") as writer:
        tablero.to_excel(writer, sheet_name="Tablero")
        mensual_region.to_excel(writer, sheet_name="Mensual", index=False)
        regiones.to_excel(writer, sheet_name="Regiones", index=False)
    print("Escrito reporte.xlsx con tres hojas")
except ImportError as e:
    print("No se escribió el .xlsx:", e)
"""),

md("""
Los archivos quedan en la sesión de Colab. Para bajarlos a tu máquina, el panel de archivos
de la izquierda tiene la opción de descarga en el menú de cada uno.
"""),

# ──────────────────────────────────────────────────────────── errores comunes

md("""
---
## Cuatro errores al agrupar y unir

**Agrupar sin haber limpiado.** Ocho regiones donde hay cuatro. Los totales se parten y cada
mitad se ve perfectamente razonable. Por eso la limpieza va antes en este cuaderno.

**Suponer que `pivot_table` suma.** Por omisión promedia. Ya viste el número que sale, y ya
viste que no avisa.

**Unir con `inner` sin darte cuenta.** Los renglones que no cruzan desaparecen en silencio, y
tu total baja sin que nada lo explique.

**Confiar en la unión sin auditarla.** `indicator=True` cuesta una palabra y te dice
exactamente cuántos renglones quedaron sueltos, en las dos direcciones.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Las soluciones están hasta abajo.

## Agrupar

### Ejercicio 1 · Tres agrupaciones sencillas

Sobre `ventas`, calcula e imprime:

1. El ingreso total por canal, ordenado de mayor a menor.
2. Cuántas unidades se vendieron de cada producto.
3. El precio unitario promedio por producto, redondeado a dos decimales.

### Ejercicio 2 · El reporte de una instrucción

Arma con `agg` una tabla por producto que traiga, con estos nombres exactos: `ingreso`,
`unidades`, `ventas`, `ticket_promedio` y `precio_promedio`. Ordénala por ingreso.

Después contesta en un comentario cuál producto conviene empujar si lo que quieres es subir
el ingreso, y cuál si lo que quieres es subir el número de ventas.

### Ejercicio 3 · La rejilla que cruza tiempo

Arma una rejilla con el mes en las filas, la región en las columnas y el ingreso en las
celdas, con totales. Divídela entre mil y redondéala para que se pueda leer.

Comprueba que la esquina coincide con el total de la tabla.

## Unir

### Ejercicio 4 · La unión auditada, al revés

Haz la unión de `regiones` contra `ventas`, o sea con `regiones` del lado izquierdo, en modo
`left`. Compara cuántos renglones salen contra la unión que hicimos en clase y explica en un
comentario por qué el número es distinto.

### Ejercicio 5 · La región inventada

Agrega a mano un renglón a una copia de `ventas` con la región `"East Coast"`, que no está en
el catálogo. Corre la auditoría y comprueba que ahora `left_only` ya no es cero.

Después di, en un comentario, qué harías con ese renglón si apareciera en tu proyecto.

### Ejercicio 6 · El mes en que cada región cumplió

Con `mensual_region`, encuentra para cada región el mes de mayor avance y el de menor.
Imprime región, mes y avance de los dos.

Pista: `idxmax` dentro de un `groupby`, como el ejercicio de lo más vendido.

## Con tus datos

### Ejercicio 7 · Contesta tu pregunta de negocio

Con tu archivo limpio, contesta la pregunta que planteaste en la semana 1 usando una
agrupación. Produce además una rejilla que cruce dos categorías, y únela con una tabla de
catálogo si tu caso lo pide.

Si hay unión, tiene que venir auditada con `indicator` y comentada.

La prueba: suma la rejilla completa y compárala con el total de la tabla. Si no coinciden,
algo se perdió.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**`groupby` es la tabla dinámica.** Partir, resumir y volver a juntar. Las ochenta líneas de
la semana 14, en ocho, y con los mismos totales al centavo.

**`pivot_table` promedia por omisión.** Si querías totales tienes que decirlo, y ese olvido
produce un número treinta veces más chico que se ve perfectamente razonable.

**Una unión se audita.** `indicator` cuesta una palabra y contesta, en las dos direcciones,
qué renglones no encontraron pareja.

La siguiente sesión son gráficas. Cómo se ve un número para que alguien lo entienda sin que
se lo expliques.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

### Ejercicio 1

```python
print("Ingreso por canal:")
print((ventas.groupby("channel")["amount"].sum().sort_values(ascending=False) / 1000).round(0))

print("\\nUnidades por producto:")
print(ventas.groupby("product")["units"].sum().sort_values(ascending=False))

print("\\nPrecio unitario promedio por producto:")
print(ventas.groupby("product")["unit_price"].mean().round(2).sort_values(ascending=False))
```

Wholesale se lleva más de la mitad del ingreso, y no porque venda más veces sino porque cada
venta es más grande. Otra vez la misma lección: magnitud y frecuencia son dos preguntas.

### Ejercicio 2

```python
por_producto = ventas.groupby("product").agg(
    ingreso=("amount", "sum"),
    unidades=("units", "sum"),
    ventas=("amount", "count"),
    ticket_promedio=("amount", "mean"),
    precio_promedio=("unit_price", "mean"),
).round(2)

print(por_producto.sort_values("ingreso", ascending=False))

# Para subir el ingreso conviene empujar Espresso machine: es el ticket más alto
# con diferencia, así que cada venta extra pesa mucho. Para subir el número de
# ventas conviene Travel mug o Bean subscription, que son los baratos y por eso
# los que más se mueven. Son dos estrategias distintas y la tabla las separa.
```

Esta tabla es el reporte completo en una instrucción. Que los nombres de columna los elijas
tú es lo que la vuelve entregable en lugar de un paso intermedio.

### Ejercicio 3

```python
por_mes = ventas.pivot_table(
    index=ventas["date"].dt.month,
    columns="region",
    values="amount",
    aggfunc="sum",
    margins=True,
    margins_name="Total",
)

print((por_mes / 1000).round(0))

esquina = por_mes.loc["Total", "Total"]
print("\\n¿La esquina coincide?", round(esquina, 2) == round(ventas["amount"].sum(), 2))
```

Se le puede pasar a `index` una Series calculada al vuelo, no solo el nombre de una columna.
Es lo que evita crear una columna `month` que después estorba.

### Ejercicio 4

```python
al_reves = regiones.merge(ventas, on="region", how="left")

print("Ventas merge regiones:", len(ventas.merge(regiones, on="region", how="left")))
print("Regiones merge ventas:", len(al_reves))
print(al_reves[al_reves["amount"].isna()][["region", "manager"]])

# Sale un renglón más, 307 contra 306. Con regiones a la izquierda, how="left"
# conserva las cinco regiones del catálogo, incluida East, que no tiene ninguna
# venta. Ese renglón aparece con todas las columnas de ventas en NaN. No es un
# error: es el catálogo diciendo que East existe y no vendió nada.
```

Cuál tabla va a la izquierda es una decisión, no un detalle. La de la izquierda es la que
tiene garantizado sobrevivir completa.

### Ejercicio 5

```python
inventada = ventas.copy()
renglon = ventas.iloc[0].copy()
renglon["region"] = "East Coast"
inventada = pd.concat([inventada, renglon.to_frame().T], ignore_index=True)

revision = inventada.merge(regiones, on="region", how="outer", indicator=True)
print(revision["_merge"].value_counts())
print("\\nVentas sin región en el catálogo:")
print(revision[revision["_merge"] == "left_only"][["region", "amount"]])

# Ese renglón no se borra y no se inventa una región para él. Se reporta a quien
# capturó los datos, porque "East Coast" puede ser East mal escrito, una plaza
# nueva que nadie dio de alta, o una venta de otra empresa. Las tres se arreglan
# distinto y ninguna se arregla adivinando.
```

Este ejercicio es el que justifica auditar siempre. Un renglón en 307 no cambia el total lo
suficiente para que alguien lo note, y aun así es un dato mal.

### Ejercicio 6

```python
mejor = mensual_region.loc[mensual_region.groupby("region")["avance"].idxmax()]
peor = mensual_region.loc[mensual_region.groupby("region")["avance"].idxmin()]

print("Mejor mes de cada región:")
print(mejor[["region", "manager", "month", "avance"]].to_string(index=False))
print("\\nPeor mes de cada región:")
print(peor[["region", "manager", "month", "avance"]].to_string(index=False))
```

`idxmax` sobre un `groupby` devuelve una etiqueta por grupo, y `loc` las convierte en
renglones completos. Es el mismo patrón de "lo más vendido de cada grupo", y ya que lo
reconoces vas a usarlo en casi todo reporte.

### Ejercicio 7

No hay solución publicada porque el archivo es distinto para cada quien. Se califica sobre
tres cosas: que la agrupación conteste la pregunta que planteaste y no otra, que la
auditoría venga comentada si hubo unión, y que la suma de la rejilla coincida con el total de
la tabla.
"""),

]

write(OUT / "es" / "w15.3.ipynb", es)
print("wrote", OUT / "es" / "w15.3.ipynb")


# ════════════════════════════════════════════════════════════════════ ENGLISH

en = [

md("""
# Data Analysis · Week 15, session 3 of 3
## Grouping, summarising and joining

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

The eighty lines you wrote by hand in week 14 fit into eight today, and the numbers match to
the cent. You will see the PivotTable and the `VLOOKUP` written out, plus a check no
spreadsheet lets you run.

By the end of this notebook you will be able to:

1. Group and summarise in one line, with `groupby` followed by the column and the function.
2. Ask for several summaries at once with `agg`, using column names you choose.
3. Build a grid with `pivot_table`, including the row and column totals.
4. Join two tables with `merge`, and explain why the left mode is the safe one.
5. Audit a join with `indicator`, checking both directions before trusting it.

### How to use this notebook

Run the cells in order. This notebook does not depend on you having run session 15.2: the
second cell repeats the cleaning so you can open this one on its own.

Three cells fail on purpose and carry a comment saying so.
"""),

md("""
---
## Setup
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

bootstrap_cell("en"),

md("""
### The cleaning, again and without explanation

Grouping over dirty data is the first error of this session, so the file gets cleaned before
anything touches it. If something in this cell is unclear, session 15.2 explains it step by
step.
"""),

code(LIMPIEZA_EN),

md("""
---
# Block 1 · Grouping

`groupby` does exactly what dragging a field into a PivotTable does: it splits the rows into
buckets that share a value, applies a summary to each bucket, and puts the results back
together as a table.

Split, summarise, put back together. That is all of it.

## Eighty lines, or eight

First the week 14 version, with a dictionary and a loop. It really runs, over the clean file
you just wrote.
"""),

code("""
import csv
from collections import defaultdict

by_region_manual = defaultdict(float)

with open("sales_clean.csv", encoding="utf-8") as f:
    for record in csv.DictReader(f):
        by_region_manual[record["region"]] += float(record["amount"])

for region in sorted(by_region_manual, key=by_region_manual.get, reverse=True):
    print(f"{region:8} {by_region_manual[region]:>12,.2f}")
"""),

md("""
Now the same thing with pandas.
"""),

code("""
by_region = sales.groupby("region")["amount"].sum()

print(by_region.sort_values(ascending=False).round(2))
"""),

md("""
The same four totals, to the cent. The difference is that one reads at a glance and the other
has to be checked line by line before you believe it.

Worth confirming rather than taking my word for it.
"""),

code("""
same = all(
    round(by_region_manual[region], 2) == round(by_region[region], 2)
    for region in by_region.index
)
print("Do the four totals match?", same)
"""),

md("""
The result of `groupby` is a `Series` whose index is the thing you grouped by, so everything
from session 15.1 still applies here.
"""),

code("""
print("Best region:", by_region.idxmax())
print("Its share of the year:", f"{by_region.max() / sales['amount'].sum():.1%}")
print()
print("All four, in thousands:")
print((by_region.sort_values(ascending=False) / 1000).round(0))
"""),

md("""
## Several summaries at once

`agg` takes a list of functions and gives back a column for each. It answers how much, how
many times and how big in a single pass.
"""),

code("""
summary = sales.groupby("region")["amount"].agg(["sum", "count", "mean"]).round(2)

print(summary.sort_values("sum", ascending=False))
"""),

md("""
Different summaries for different columns, with names you choose. The pattern is
`new_name=("source column", "function")`, and it is how a report table gets built in a single
statement.
"""),

code("""
detailed = sales.groupby("region").agg(
    revenue=("amount", "sum"),
    units_sold=("units", "sum"),
    sales_made=("amount", "count"),
    average_sale=("amount", "mean"),
).round(2)

print(detailed.sort_values("revenue", ascending=False))
"""),

md("""
### Here is the story

Look at that table carefully before moving on. **North sells more than anyone, and Centre has
the highest average sale.** North made 92 sales averaging 47 thousand; Centre made 70
averaging 56 thousand.

They are two different businesses with the same apparent revenue, and that difference does
not show up in a total. `sum` answers magnitude and `count` answers frequency, which are the
two questions from week 9, and you need both to understand what happened.
"""),

code("""
print("Sales made per region:")
print(detailed["sales_made"].sort_values(ascending=False))
print()
print("Average size of a sale:")
print(detailed["average_sale"].sort_values(ascending=False).round(0))
"""),

md("""
## Two grouping fields

Pass a list and the buckets become every combination of the two fields.
"""),

code("""
by_region_channel = sales.groupby(["region", "channel"])["amount"].sum().round(2)

print(by_region_channel)
"""),

md("""
Twelve rows, one per combination. It reads as a long list, and that is exactly the problem the
next block solves.
"""),

md("""
---
# Block 2 · The grid

`pivot_table` lays those same numbers out as a grid, which is the shape you see on screen
when you open a PivotTable.

Four arguments, and each one matches something you would drag with the mouse:

| Argument | What it is | In the PivotTable |
|---|---|---|
| `index` | What goes down the side | The field you drag into rows |
| `columns` | What goes across the top | The field you drag into columns |
| `values` | What fills the cells | The values field |
| `aggfunc` | How they are summarised | Value field settings |
"""),

code("""
grid = sales.pivot_table(
    index="region",      # what goes down the side
    columns="channel",   # what goes across the top
    values="amount",     # what fills the cells
    aggfunc="sum",       # how they are summarised
)

print((grid / 1000).round(0))
"""),

md("""
The same twelve numbers from the previous block, now readable at a glance. In thousands, so
they fit.

## The `aggfunc` trap

**Predict before you run.** What does `pivot_table` give back if you do not say `aggfunc`?

- **A.** The sum by region and channel.
- **B.** The mean, which is what it does by default.
- **C.** The row count.
- **D.** An error, because `aggfunc` is required.
"""),

code("""
# FAILS ON PURPOSE. It raises nothing: it gives a different number, which is worse.
no_aggfunc = sales.pivot_table(
    index="region",
    columns="channel",
    values="amount",
)

print("Without aggfunc, Centre/Online cell:", round(no_aggfunc.loc["Centre", "Online"], 2))
print("With sum,        Centre/Online cell:", round(grid.loc["Centre", "Online"], 2))
print()
print("How many times bigger is the sum?",
      round(grid.loc["Centre", "Online"] / no_aggfunc.loc["Centre", "Online"], 1))
"""),

md("""
The answer is **B**. By default `pivot_table` averages, it does not add.

And there is the danger: it raises nothing, it gives back a grid with the same shape and the
same headers, holding numbers thirty times smaller. If you expected totals and did not say
`aggfunc`, your report is wrong and looks perfectly fine.

The factor they differ by is not a coincidence: it is how many sales fell into that cell.

## The totals
"""),

code("""
with_totals = sales.pivot_table(
    index="region", columns="channel", values="amount",
    aggfunc="sum", margins=True, margins_name="Total",
)

print((with_totals / 1000).round(0))
"""),

md("""
`margins=True` adds the row and column totals, the way a PivotTable's grand total does. The
number in the bottom right corner has to match the table's total, and checking it is the
fastest way to know whether something got lost along the way.
"""),

code("""
corner = with_totals.loc["Total", "Total"]
table = sales["amount"].sum()

print(f"Corner of the grid: {corner:,.2f}")
print(f"Total of the table: {table:,.2f}")
print("Match?", round(corner, 2) == round(table, 2))
"""),

md("""
## Grouping over time

A date column can be grouped by any part of itself. `.dt` reaches into the date the same way
`.str` reaches into text.
"""),

code("""
sales["month"] = sales["date"].dt.month
monthly = sales.groupby("month")["amount"].sum().round(2)

print((monthly / 1000).round(0))
print()
print("Best month:", monthly.idxmax(), "| worst month:", monthly.idxmin())
"""),

md("""
December runs away with it, at more than double almost any other month, and July is the
weakest. That pattern only appears once you group: row by row in the table it is invisible.

Now, careful with the easy reading. The file carries a seasonal curve that rises in November
and December, and November still came out low. The reason is that a handful of espresso
machine sales, the expensive product, outweigh the seasonality of everything else. A total
hides its composition, and that is exactly why `agg` with `count` next to `sum` earns its
place.
"""),

code("""
print("Revenue and number of sales per month:")
print(sales.groupby("month").agg(
    revenue=("amount", "sum"),
    sales_made=("amount", "count"),
    ticket=("amount", "mean"),
).round(0).sort_values("revenue", ascending=False).head())
"""),

md("""
December had an average ticket well above the rest, not many more sales. The month was not
better because things sold more often, it was better because they sold dearer.

Quarter, year and day of week work the same way.
"""),

code("""
by_quarter = sales.groupby(sales["date"].dt.quarter)["amount"].sum().round(2)
print("By quarter, in thousands:")
print((by_quarter / 1000).round(0))

print()
print("By day of week, in thousands:")
print((sales.groupby(sales["date"].dt.day_name())["amount"].sum() / 1000).round(0))
"""),

md("""
Day of week comes back with a single value because the file was generated with one sale per
week, every Monday. It is a good reminder that a grouping does not invent variety where there
is none, and that it pays to look at the result before drawing a conclusion.

## The top of each group

A question that turns up in every report: which product sells most in each region. Group by
both, total, then take the largest of each region.
"""),

code("""
product_region = sales.groupby(["region", "product"])["amount"].sum()
best_per_region = product_region.loc[product_region.groupby("region").idxmax()]

print(best_per_region.round(2))
"""),

md("""
The middle line reads from the inside out: `groupby("region").idxmax()` gives back, for each
region, the full label of its largest row, and `loc` goes and fetches those rows. It is the
same `idxmax` from session 15.1, applied to a two-level index.
"""),

md("""
---
# Block 3 · Joining two tables

`merge` is `VLOOKUP`, with two differences that matter. It brings every column across at once
instead of one per formula, and it tells you what did not match instead of leaving `#N/A`
scattered through the sheet.

| Mode | What it keeps | When |
|---|---|---|
| `left` | Every row on the left | The safe one, and the `VLOOKUP` lookalike |
| `inner` | Only the ones that match | When what does not cross does not matter |
| `right` | Every row on the right | Rare, it is a `left` backwards |
| `outer` | Everything from both sides | For auditing what did not match |
"""),

code("""
regions = pd.read_csv("regions.csv")

print(regions)
print()
print("Sales:", sales.shape, "| Regions:", regions.shape)
"""),

md("""
`on` names the column both tables share. Every matching row of `regions` is attached to the
sales row, bringing all of its columns with it.
"""),

code("""
joined = sales.merge(regions, on="region", how="left")

print("After the join:", joined.shape)
print(joined[["date", "region", "amount", "manager", "monthly_target"]].head(3))
"""),

md("""
`how="left"` keeps every sales row, whether or not the lookup found a match. That is the
`VLOOKUP` behaviour and it is the safe default: you never silently lose a sale because its
region was missing from the catalogue.

Watch the shape: 306 rows before, 306 after. Had that number changed, something happened that
needs understanding before you go on.

## The audit, which is what no spreadsheet lets you do
"""),

code("""
audit = sales.merge(regions, on="region", how="outer", indicator=True)

print(audit["_merge"].value_counts())
"""),

md("""
`how="outer"` keeps everything from both sides, and the `_merge` column says where each row
came from. The two directions get checked separately and they mean different things.

**`right_only` at one** means the catalogue holds a region with no sales at all. That is
usually fine: a new location, or one that closed.

**`left_only` at zero** means no sale was left orphaned. That one matters: a sale whose region
the catalogue does not know is a data problem to report, not to paper over.
"""),

code("""
orphans = audit[audit["_merge"] == "right_only"]["region"].unique()
print("Catalogue regions with no sales:", list(orphans))

uncatalogued = audit[audit["_merge"] == "left_only"]["region"].unique()
print("Sales whose region the catalogue does not know:", list(uncatalogued) or "none")
"""),

md("""
With a formula you would have to count the `#N/A` by hand, and only in one direction. Here the
count comes included and it covers both.

## Using what the join brought

Now that every row knows its target, the comparison is an ordinary column.
"""),

code("""
monthly_region = (
    joined.assign(month=joined["date"].dt.month)
    .groupby(["region", "manager", "monthly_target", "month"])["amount"]
    .sum()
    .reset_index()
)

monthly_region["hit_target"] = monthly_region["amount"] >= monthly_region["monthly_target"]
monthly_region["attainment"] = (monthly_region["amount"] / monthly_region["monthly_target"]).round(3)

print(monthly_region.head())
"""),

md("""
`reset_index` turns the grouping index back into ordinary columns. Without it, `region`,
`manager`, `monthly_target` and `month` would still be index and could not be used in a
comparison.

And with that the scoreboard can be built.
"""),

code("""
scoreboard = (
    monthly_region.groupby(["region", "manager"])
    .agg(months=("hit_target", "count"),
         months_on_target=("hit_target", "sum"),
         mean_attainment=("attainment", "mean"))
    .round(3)
    .sort_values("mean_attainment", ascending=False)
)

print(scoreboard)
"""),

md("""
No region hit its target more than three months out of twelve, and the best one averages 76 %
attainment. Neither table says that on its own: `sales` does not know the targets and
`regions` does not know the sales. It comes from having joined them.

## When the key is named differently in each table

Name both sides. Here both are called `region`, so the example renames one on the way in to
show the shape.
"""),

code("""
codes = regions.rename(columns={"region": "region_code"})
example = sales.merge(codes, left_on="region", right_on="region_code", how="left")

print("Joined on differently named keys:", example.shape)
print(example[["region", "region_code", "manager"]].head(3))
"""),

md("""
Note that both key columns survived, `region` and `region_code`, holding the same content.
That is normal, and if they get in the way they come off with `drop`.

## Exporting

The analysis ends where it started, as a file somebody else can open.
"""),

code("""
scoreboard.to_csv("scoreboard.csv")

print("Wrote scoreboard.csv")
print(open("scoreboard.csv", encoding="utf-8").read())
"""),

md("""
For Excel, which is where this usually has to end up, an `ExcelWriter` handles several sheets
at once. It needs the `openpyxl` package, which Colab already has installed.
"""),

code("""
# If openpyxl were missing, pandas raises ImportError naming it. Colab ships with it.
try:
    with pd.ExcelWriter("report.xlsx") as writer:
        scoreboard.to_excel(writer, sheet_name="Scoreboard")
        monthly_region.to_excel(writer, sheet_name="Monthly", index=False)
        regions.to_excel(writer, sheet_name="Regions", index=False)
    print("Wrote report.xlsx with three sheets")
except ImportError as e:
    print("The .xlsx was not written:", e)
"""),

md("""
The files sit in the Colab session. To pull them down to your machine, the file panel on the
left has a download option in each file's menu.
"""),

md("""
---
## Four errors when grouping and joining

**Grouping without having cleaned.** Eight regions where there are four. The totals split and
each half looks perfectly reasonable. That is why the cleaning comes first in this notebook.

**Assuming `pivot_table` sums.** By default it averages. You have seen the number it gives,
and you have seen that it does not warn you.

**Joining with `inner` without noticing.** The rows that do not cross disappear silently, and
your total drops with nothing to explain it.

**Trusting a join without auditing it.** `indicator=True` costs one word and tells you exactly
how many rows were left loose, in both directions.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom.

## Grouping

### Exercise 1 · Three simple groupings

On `sales`, work out and print:

1. Total revenue per channel, sorted highest to lowest.
2. How many units were sold of each product.
3. The average unit price per product, rounded to two decimals.

### Exercise 2 · The one-statement report

Use `agg` to build a per-product table carrying, with these exact names: `revenue`, `units`,
`sales`, `average_ticket` and `average_price`. Sort it by revenue.

Then answer in a comment which product to push if what you want is more revenue, and which
one if what you want is more sales.

### Exercise 3 · The grid that crosses time

Build a grid with the month down the rows, the region across the columns and revenue in the
cells, with totals. Divide it by a thousand and round it so it can be read.

Check that the corner matches the table's total.

## Joining

### Exercise 4 · The audited join, backwards

Join `regions` against `sales`, meaning with `regions` on the left, in `left` mode. Compare
how many rows come back against the join we did in class and explain in a comment why the
number is different.

### Exercise 5 · The invented region

Add a row by hand to a copy of `sales` with the region `"East Coast"`, which is not in the
catalogue. Run the audit and confirm that `left_only` is no longer zero.

Then say, in a comment, what you would do with that row if it turned up in your project.

### Exercise 6 · The month each region delivered

With `monthly_region`, find each region's best and worst month by attainment. Print region,
month and attainment for both.

Hint: `idxmax` inside a `groupby`, like the best-selling-product exercise.

## With your own data

### Exercise 7 · Answer your business question

With your clean file, answer the question you posed in week 1 using a grouping. Produce a
grid crossing two categories as well, and join it with a catalogue table if your case calls
for one.

If there is a join, it has to come audited with `indicator` and commented.

The test: sum the whole grid and compare it against the table's total. If they do not match,
something got lost.
"""),

md("""
---
## Three ideas to take away

**`groupby` is the PivotTable.** Split, summarise, put back together. The eighty lines of week
14, in eight, with the same totals to the cent.

**`pivot_table` averages by default.** If you wanted totals you have to say so, and forgetting
produces a number thirty times smaller that looks perfectly reasonable.

**A join gets audited.** `indicator` costs one word and answers, in both directions, which
rows found no partner.

Next session is charts. What a number has to look like for somebody to understand it without
you explaining it.
"""),

md("""
---
# Solutions

### Exercise 1

```python
print("Revenue per channel:")
print((sales.groupby("channel")["amount"].sum().sort_values(ascending=False) / 1000).round(0))

print("\\nUnits per product:")
print(sales.groupby("product")["units"].sum().sort_values(ascending=False))

print("\\nAverage unit price per product:")
print(sales.groupby("product")["unit_price"].mean().round(2).sort_values(ascending=False))
```

Wholesale takes more than half the revenue, and not because it sells more often but because
each sale is bigger. The same lesson again: magnitude and frequency are two questions.

### Exercise 2

```python
by_product = sales.groupby("product").agg(
    revenue=("amount", "sum"),
    units=("units", "sum"),
    sales=("amount", "count"),
    average_ticket=("amount", "mean"),
    average_price=("unit_price", "mean"),
).round(2)

print(by_product.sort_values("revenue", ascending=False))

# To lift revenue, push the Espresso machine: it has the highest ticket by a wide
# margin, so every extra sale counts for a lot. To lift the number of sales, push
# the Travel mug or the Bean subscription, the cheap ones, which is why they move
# most. Two different strategies, and the table separates them.
```

This table is the whole report in one statement. That you choose the column names is what
makes it a deliverable rather than an intermediate step.

### Exercise 3

```python
by_month = sales.pivot_table(
    index=sales["date"].dt.month,
    columns="region",
    values="amount",
    aggfunc="sum",
    margins=True,
    margins_name="Total",
)

print((by_month / 1000).round(0))

corner = by_month.loc["Total", "Total"]
print("\\nDoes the corner match?", round(corner, 2) == round(sales["amount"].sum(), 2))
```

`index` accepts a Series computed on the spot, not only a column name. That is what saves you
from creating a `month` column that gets in the way afterwards.

### Exercise 4

```python
backwards = regions.merge(sales, on="region", how="left")

print("Sales merge regions:", len(sales.merge(regions, on="region", how="left")))
print("Regions merge sales:", len(backwards))
print(backwards[backwards["amount"].isna()][["region", "manager"]])

# One extra row comes back, 307 against 306. With regions on the left, how="left"
# keeps all five catalogue regions, East included, which has no sales at all. That
# row shows up with every sales column as NaN. It is not an error: it is the
# catalogue saying East exists and sold nothing.
```

Which table goes on the left is a decision, not a detail. The one on the left is the one
guaranteed to survive intact.

### Exercise 5

```python
invented = sales.copy()
row = sales.iloc[0].copy()
row["region"] = "East Coast"
invented = pd.concat([invented, row.to_frame().T], ignore_index=True)

check = invented.merge(regions, on="region", how="outer", indicator=True)
print(check["_merge"].value_counts())
print("\\nSales with no region in the catalogue:")
print(check[check["_merge"] == "left_only"][["region", "amount"]])

# That row does not get deleted and does not get a region invented for it. It goes
# back to whoever captured the data, because "East Coast" could be East misspelled,
# a new location nobody registered, or a sale from another company. Those three get
# fixed differently and none of them gets fixed by guessing.
```

This exercise is what justifies always auditing. One row in 307 does not move the total enough
for anyone to notice, and it is still wrong data.

### Exercise 6

```python
best = monthly_region.loc[monthly_region.groupby("region")["attainment"].idxmax()]
worst = monthly_region.loc[monthly_region.groupby("region")["attainment"].idxmin()]

print("Best month per region:")
print(best[["region", "manager", "month", "attainment"]].to_string(index=False))
print("\\nWorst month per region:")
print(worst[["region", "manager", "month", "attainment"]].to_string(index=False))
```

`idxmax` over a `groupby` gives back one label per group, and `loc` turns them into whole
rows. It is the same pattern as the best-selling product, and once you recognise it you will
use it in nearly every report.

### Exercise 7

There is no published solution, because the file is different for everyone. It is graded on
three things: that the grouping answers the question you posed rather than another one, that
the audit is commented if there was a join, and that the grid's sum matches the table's total.
"""),

]

write(OUT / "en" / "w15.3.ipynb", en)
print("wrote", OUT / "en" / "w15.3.ipynb")
