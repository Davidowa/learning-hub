"""notebooks/analisis-de-datos/es/w16.2.ipynb

Source deck: ppts/python/analisis-de-datos/es/w16.2.es.yaml
Source code:  06 - Advanced/A06 - Data Visualization/04_seaborn.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

LIMPIEZA = """
# La limpieza de la sesión 15.2, para que este cuaderno se abra solo.
ventas = pd.read_csv("sales.csv").drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["unit_price"] = (ventas["unit_price"]
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.strip().astype(float))
ventas["date"] = pd.to_datetime(ventas["date"])
ventas = ventas.dropna(subset=["units"])
ventas["units"] = ventas["units"].astype(int)
ventas["amount"] = ventas["units"] * ventas["unit_price"]

empleados = pd.read_csv("employees.csv")

print(f"{len(ventas)} ventas limpias, {len(empleados)} empleados")
"""

es = [

md("""
# Análisis de Datos · Semana 16, sesión 2 de 2
## seaborn y cierre del proyecto

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Última sesión de contenido. Las gráficas estadísticas en una línea, lo que un promedio esconde, y
la entrega del proyecto.

Al terminar este cuaderno vas a poder:

1. Graficar desde un `DataFrame`, pasando nombres de columna sin preparar los datos antes.
2. Elegir el estimador correcto, porque seaborn promedia por omisión.
3. Meter una tercera variable con `hue`.
4. Leer una caja y bigotes: mediana, mitad central, rango y atípicos.
5. Presentar un hallazgo con la conclusión primero.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Tres dibujan a propósito una gráfica que engaña, para que compares.
"""),

md("""
---
## Preparación
"""),

code("""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("pandas", pd.__version__, "· seaborn", sns.__version__)
"""),

bootstrap_cell("es"),

code(LIMPIEZA),

md("""
---
# Bloque 1 · seaborn

Vive encima de matplotlib y recibe el `DataFrame` directo. Le dices qué columnas usar y él
resuelve el resto.

Con matplotlib hay que agrupar primero:

```python
por_region = ventas.groupby("region")["amount"].sum()
ax.bar(por_region.index, por_region.values)
```

Con seaborn se nombran las columnas:
"""),

code("""
sns.set_theme(style="whitegrid", palette="deep")

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=ventas, x="region", y="amount", estimator="sum",
            errorbar=None, hue="region", legend=False, ax=ax)
ax.set_title("Ingreso total por región", loc="left", fontweight="bold")
ax.set_ylabel("Ingreso")
plt.show()
"""),

md("""
**`set_theme`** fija cuadrícula, tipografía y paleta para todas las gráficas que vengan después.
Se configura una vez y por eso se ven consistentes.

**`estimator="sum"`** dice qué resumen quieres. Y aquí viene el error número uno con seaborn.

**Predice antes de correr.** ¿Qué dibuja esta línea si no pasas `estimator`?

- **A.** El total por región.
- **B.** El promedio por región, que es lo que hace por omisión.
- **C.** El conteo de renglones por región.
- **D.** Un error, porque falta el estimador.
"""),

code("""
# DIBUJA MAL A PROPÓSITO, del lado izquierdo. Los dos paneles traen los mismos datos.
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.barplot(data=ventas, x="region", y="amount",
            errorbar=None, hue="region", legend=False, ax=axes[0])
axes[0].set_title("Sin estimator: promedia", loc="left", fontweight="bold")

sns.barplot(data=ventas, x="region", y="amount", estimator="sum",
            errorbar=None, hue="region", legend=False, ax=axes[1])
axes[1].set_title("Con estimator='sum': totaliza", loc="left", fontweight="bold")

for a in axes:
    a.set_ylabel("Ingreso")
fig.tight_layout()
plt.show()
"""),

md("""
La respuesta es **B**. Por omisión promedia, y las dos gráficas ordenan las regiones distinto.

Una barra que dice promedio cuando el lector esperaba total es un número correcto que engaña. Es
exactamente la misma trampa que `pivot_table` sin `aggfunc` en la semana 15.3.

**`errorbar=None`** también importa: sin él, seaborn dibuja un intervalo de confianza encima de
cada barra, que casi nunca es lo que querías y que nadie te va a preguntar si entendiste.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=ventas, x="region", y="amount", estimator="sum",
            hue="region", legend=False, ax=ax)
ax.set_title("Sin errorbar=None: aparecen las rayitas", loc="left", fontweight="bold")
plt.show()
"""),

md("""
## El hallazgo

Las dos gráficas de arriba ordenan distinto, y eso no es un defecto. Es el hallazgo.
"""),

code("""
resumen = (ventas.groupby("region")["amount"]
           .agg(["sum", "mean", "count"]) / [1000, 1000, 1])

print(resumen.round(0).sort_values("sum", ascending=False))
"""),

md("""
**Norte vende más que Centro en el año. Centro vende más grande en cada operación.**

Las dos afirmaciones son ciertas y salen de la misma tabla. La gráfica que escojas decide cuál de
las dos ve tu lector, y elegir sin darte cuenta es cómo un reporte honesto termina diciendo algo
que no querías decir.

| Pregunta | La contesta |
|---|---|
| ¿Cuánto entró? | El total |
| ¿De qué tamaño es cada venta? | El promedio |
| ¿Qué tan seguido vendemos? | El conteo |

Las tres juntas cuentan la historia: **Norte vende seguido, Centro vende caro.** Esa frase no se ve
en ninguna de las dos gráficas por separado.

## Una tercera variable con `hue`
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.barplot(data=ventas, x="region", y="amount", hue="channel",
            estimator="sum", errorbar=None, ax=ax)
ax.set_title("Mayoreo domina en las cuatro regiones", loc="left", fontweight="bold")
ax.set_ylabel("Ingreso")
plt.show()
"""),

md("""
`hue` separa por color y arma la leyenda solo. Doce barras que con matplotlib habrían costado un
ciclo y una lista de colores.

Y el título dice el hallazgo, no los ejes, que es la regla de la sesión pasada.
"""),

md("""
---
# Bloque 2 · Lo que un promedio esconde

Dos áreas con el mismo sueldo promedio pueden no parecerse en nada. La caja lo enseña de un
vistazo.
"""),

code("""
print(empleados.groupby("area")["monthly_salary"]
      .agg(["mean", "median", "std", "count"]).round(0))
"""),

code("""
orden = (empleados.groupby("area")["monthly_salary"]
         .median().sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(10, 4.5))
sns.boxplot(data=empleados, x="area", y="monthly_salary", order=orden,
            hue="area", legend=False, ax=ax)
ax.set_title("El sueldo típico y qué tan disparejo es cada área",
             loc="left", fontweight="bold")
ax.set_ylabel("Sueldo mensual")
plt.show()
"""),

md("""
**La caja** contiene la mitad central de los valores, del primer al tercer cuartil. La línea de
adentro es la **mediana**, no el promedio.

**Los bigotes** llegan hasta el rango típico. Los puntos sueltos más allá son los valores atípicos.

**`order`** ordena por mediana, y hace que el ranking se lea solo. Es la misma regla que ordenar
las barras.

Compara la caja con el promedio dibujado encima:
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.boxplot(data=empleados, x="area", y="monthly_salary", order=orden,
            hue="area", legend=False, ax=ax)
sns.pointplot(data=empleados, x="area", y="monthly_salary", order=orden,
              errorbar=None, color="#B4530A", linestyle="none",
              markers="D", ax=ax)
ax.set_title("El rombo es el promedio, la línea es la mediana",
             loc="left", fontweight="bold")
ax.set_ylabel("Sueldo mensual")
plt.show()
"""),

md("""
En cada área el rombo queda por arriba de la línea. Eso es la cola de sueldos altos jalando el
promedio, y es lo mismo que viste con los cinco sueldos de la semana 3.

## El histograma, ahora en una línea
"""),

code("""
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(data=empleados, x="monthly_salary", bins=15, ax=axes[0])
axes[0].set_title("Todos juntos", loc="left", fontweight="bold")

sns.histplot(data=empleados, x="monthly_salary", hue="area",
             element="step", bins=15, ax=axes[1])
axes[1].set_title("Separado por área", loc="left", fontweight="bold")

fig.tight_layout()
plt.show()
"""),

md("""
## El mapa de calor

Recibe la rejilla que produjo `pivot_table` en la sesión 15.3, sin preparación extra.
"""),

code("""
rejilla = ventas.pivot_table(index="region", columns="channel",
                             values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 4))
sns.heatmap(rejilla, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Ingreso por región y canal, en miles", loc="left", fontweight="bold")
plt.show()
"""),

md("""
**`annot`** escribe el valor dentro de cada celda. Sin él, el color obliga a estimar contra la
barra lateral.

**`fmt`** controla cómo se redondea lo que se escribe. Con miles y cero decimales cabe cómodo.

El color hace el ranking por ti: se ve dónde está lo alto sin comparar cifras una por una.

## La dispersión, con la recta
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.regplot(data=empleados, x="tenure_months", y="monthly_salary",
            scatter_kws={"alpha": 0.5}, line_kws={"color": "#B4530A"}, ax=ax)

r = empleados["tenure_months"].corr(empleados["monthly_salary"])
ax.set_title(f"La antigüedad explica poco del sueldo, correlación {r:.2f}",
             loc="left", fontweight="bold")
ax.set_xlabel("Antigüedad en meses")
ax.set_ylabel("Sueldo mensual")
plt.show()
"""),

md("""
`regplot` dibuja la nube y le ajusta una recta. La recta sube, y la nube está tan dispersa que la
correlación es de 0.28.

Y ahí hay una trampa que vale nombrar: **una recta siempre se puede dibujar.** Que exista no
significa que explique nada. El número al lado es lo que dice cuánto vale, y sin él la recta
sugiere más de lo que hay.
"""),

md("""
---
# Bloque 3 · El proyecto integrador

Se entrega y se presenta hoy. Vale el veinte por ciento, y la evaluación es individual aunque el
trabajo sea en equipo.

| Aspecto | Detalle |
|---|---|
| Qué | Cuaderno o código, el conjunto de datos usado, y un reporte en PDF |
| Dónde | Blackboard. Por correo no se califica |
| Peso | 20 % de la calificación final |
| Código y análisis | 70 %: corre y contesta, limpieza correcta, gráficas honestas |
| Reporte | 30 %: narrativa, justificación de decisiones y evidencia integrada |

## La conclusión primero, la evidencia detrás

Empieza diciendo qué encontraste. Después enseñas cómo lo obtuviste, y al final qué harías con
eso.

Quien te escucha decide en los primeros treinta segundos si va a poner atención al resto.

| Orden equivocado | Orden que funciona |
|---|---|
| "Limpiamos el archivo, quitamos duplicados..." | "El norte vende seguido y el centro vende caro" |
| "...después agrupamos por región..." | "Se ve en estas dos barras" |
| "...y el resultado fue este" | "Sugiero mover presupuesto de volumen a ticket" |

## Una revisión antes de entregar

Corre esta celda sobre tu propio análisis. Las cuatro preguntas son las que más puntos cuestan.
"""),

code("""
REVISION = [
    "¿El cuaderno corre de cero, con el kernel reiniciado y sin errores?",
    "¿Todas las rutas son relativas, y los datos van junto al código?",
    "¿Cada gráfica tiene título con el hallazgo, etiquetas de eje y fuente?",
    "¿El reporte dice qué hiciste con los huecos y los duplicados?",
    "¿El eje vertical de cada barra empieza en cero?",
    "¿Cada integrante puede explicar cualquier parte, no solo la suya?",
]

for i, pregunta in enumerate(REVISION, 1):
    print(f"{i}. {pregunta}")
"""),

md("""
**El cuaderno que no corre de cero** es el que más cuesta: si truena, la calificación máxima es
30 %. Reinícialo y córrelo completo antes de entregar.

**Las rutas absolutas** funcionan en tu máquina y en ninguna otra. Es el error de la semana 14.

**Las gráficas sin título ni fuente** son lo primero que se revisa, y lo que menos cuesta arreglar
de todo el proyecto.

**Limpiar sin dejar constancia** vuelve el análisis indefendible. Si el reporte no dice qué hiciste
con los huecos, nadie puede juzgar si estuvo bien.

## La presentación

Tres minutos por equipo. La pregunta, el hallazgo, cómo llegaste a él y qué recomendarías.

**Máximo dos gráficas en pantalla.** Si necesitas cinco, todavía no sabes cuál es el hallazgo.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

### Ejercicio 1 · El estimador

Dibuja la misma barra tres veces, con `sum`, `mean` y `count`, en una fila de tres paneles. Ponle
a cada una el título que corresponde a la pregunta que contesta.

Después di en un comentario cuál usarías para decidir dónde poner más presupuesto, y por qué.

### Ejercicio 2 · La tercera variable

Con `hue`, dibuja el ingreso por canal separado por región. Es la misma información que la del
cuaderno con los ejes intercambiados.

Di en un comentario cuál de las dos versiones se lee mejor y por qué.

### Ejercicio 3 · La caja de tus datos

Haz un `boxplot` de `amount` por canal, ordenado por mediana. Después contesta: ¿qué canal tiene
la venta típica más grande, y cuál tiene más dispersión?

### Ejercicio 4 · Promedio contra mediana

Para cada canal, calcula el promedio y la mediana de `amount` y la diferencia entre los dos.
Ordena por esa diferencia.

El canal con la diferencia más grande es el que tiene la cola más larga. Dibújalo con un
histograma y compruébalo.

### Ejercicio 5 · El mapa de calor por mes

Arma un mapa de calor con el mes en las filas y la región en las columnas. Usa `fmt=".0f"` y
divide entre mil.

Di en un comentario qué celda es la más alta y si eso te sorprende.

### Ejercicio 6 · La recta que no dice nada

Dibuja un `regplot` de `units` contra `unit_price` en `ventas`, con la correlación en el título.

Después explica en un comentario por qué esa recta no debería usarse para predecir nada.

### Ejercicio 7 · Tu proyecto, revisado

Corre la lista de revisión sobre tu propio análisis y contesta las seis por escrito. Por cada
"no", arregla y vuelve a contestar.

### Ejercicio 8 · Las dos gráficas

Elige las dos únicas gráficas que van a tu presentación. Escribe para cada una: el hallazgo que
comunica, por qué esa forma y no otra, y el texto alternativo.

Si no puedes elegir dos, todavía no sabes cuál es el hallazgo.
"""),

md("""
---
## Tres ideas para llevarse

**seaborn promedia por omisión.** Si querías el total y no dijiste `estimator`, la barra muestra un
número correcto que engaña.

**El promedio esconde la forma.** Dos áreas con el mismo sueldo promedio pueden repartirse de
maneras que no se parecen en nada, y la caja lo enseña en un vistazo.

**La conclusión va primero.** Quien te escucha decide en los primeros treinta segundos si va a
poner atención al resto.

La siguiente sesión es repaso y examen final.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
titulos = [("sum", "¿Cuánto entró?"), ("mean", "¿De qué tamaño es cada venta?"),
           ("count", "¿Qué tan seguido vendemos?")]

for ax, (est, titulo) in zip(axes, titulos):
    sns.barplot(data=ventas, x="region", y="amount", estimator=est,
                errorbar=None, hue="region", legend=False, ax=ax)
    ax.set_title(titulo, loc="left", fontweight="bold")
    ax.set_ylabel("")

fig.tight_layout()
plt.show()

# Para decidir presupuesto usaría las tres, no una. El total dice dónde está el
# dinero hoy, el promedio dice dónde cada peso invertido rinde más por operación,
# y el conteo dice dónde hay volumen que sostener. Norte tiene el total más alto
# y Centro el mejor promedio: mover presupuesto de uno a otro cambia qué tipo de
# negocio estás comprando.
```

Que las tres barras ordenen distinto es el punto. Una sola gráfica habría escondido dos de las
tres respuestas.

### Ejercicio 2

```python
fig, ax = plt.subplots(figsize=(10, 4.5))
sns.barplot(data=ventas, x="channel", y="amount", hue="region",
            estimator="sum", errorbar=None, ax=ax)
ax.set_title("Mayoreo concentra el ingreso en todas las regiones",
             loc="left", fontweight="bold")
plt.show()

# Se lee mejor esta, con el canal en el eje. La diferencia entre canales es mucho
# más grande que la diferencia entre regiones, así que ponerla en el eje deja que
# el ojo compare lo que más importa. Con la región en el eje, las tres barras de
# cada grupo quedan parecidas y hay que buscar el patrón.
```

La regla que sale de ahí: la variable con más contraste va en el eje, y la otra en el color.

### Ejercicio 3

```python
orden_canal = (ventas.groupby("channel")["amount"]
               .median().sort_values(ascending=False).index)

fig, ax = plt.subplots(figsize=(8, 4.5))
sns.boxplot(data=ventas, x="channel", y="amount", order=orden_canal,
            hue="channel", legend=False, ax=ax)
ax.set_title("Mayoreo tiene la venta típica más grande y la más dispareja",
             loc="left", fontweight="bold")
plt.show()

print(ventas.groupby("channel")["amount"].agg(["median", "std"]).round(0))
```

Mayoreo gana en las dos: la venta típica más grande y la mayor dispersión. Tiene sentido, porque
una venta de mayoreo puede ser de tres unidades o de sesenta.

### Ejercicio 4

```python
comparacion = ventas.groupby("channel")["amount"].agg(["mean", "median"])
comparacion["diferencia"] = comparacion["mean"] - comparacion["median"]
print(comparacion.round(0).sort_values("diferencia", ascending=False))

peor = comparacion["diferencia"].idxmax()

fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=ventas[ventas["channel"] == peor], x="amount", bins=25, ax=ax)
ax.axvline(ventas[ventas["channel"] == peor]["amount"].mean(),
           color="#B4530A", linestyle="--")
ax.axvline(ventas[ventas["channel"] == peor]["amount"].median(),
           color="#0B1B3A", linestyle=":")
ax.set_title(f"{peor}: la cola larga jala el promedio", loc="left", fontweight="bold")
plt.show()
```

La cola a la derecha es de las ventas de máquina de espresso. Son pocas y muy grandes, y son las
que separan el promedio de la mediana.

### Ejercicio 5

```python
por_mes = ventas.pivot_table(index=ventas["date"].dt.month, columns="region",
                             values="amount", aggfunc="sum") / 1000

fig, ax = plt.subplots(figsize=(7, 6))
sns.heatmap(por_mes, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_title("Ingreso por mes y región, en miles", loc="left", fontweight="bold")
ax.set_ylabel("Mes")
plt.show()

print("La celda más alta:", por_mes.stack().idxmax(), round(por_mes.stack().max()))

# La celda más alta es diciembre en el norte, y no me sorprende después de la
# sesión 15.3: diciembre concentró el 20 % del año y el norte es la región de
# mayor volumen. Lo que sí sorprende es cuánto destaca sobre todo lo demás.
```

`stack()` aplana la rejilla en una Series con índice de dos niveles, y así `idxmax` devuelve la
celda como un par de etiquetas.

### Ejercicio 6

```python
r = ventas["units"].corr(ventas["unit_price"])

fig, ax = plt.subplots(figsize=(8, 4.5))
sns.regplot(data=ventas, x="units", y="unit_price",
            scatter_kws={"alpha": 0.4}, line_kws={"color": "#B4530A"}, ax=ax)
ax.set_title(f"Correlación de {r:.2f}: la recta no explica nada",
             loc="left", fontweight="bold")
plt.show()

# La nube se ve en bandas horizontales, una por producto, porque unit_price solo
# toma quince valores distintos. Una recta ajustada sobre bandas no describe una
# relación, describe un promedio de cosas que no se parecen. Además la correlación
# es cercana a cero, así que la recta es prácticamente horizontal y aun así se
# dibuja, que es justo el problema: regplot siempre te da una recta.
```

Ese es el reflejo que vale la pena llevarse: la recta aparece siempre, y decidir si significa algo
es tuyo.

### Ejercicio 7

No hay solución publicada porque es sobre tu propio proyecto. Se califica sobre que las seis estén
contestadas por escrito y que los "no" estén corregidos, no ocultados.

### Ejercicio 8

No hay solución publicada. Se califica sobre tres cosas: que sean exactamente dos gráficas, que
cada una tenga escrito el hallazgo que comunica y por qué esa forma, y que el texto alternativo de
las dos se pueda verificar contra los datos.
"""),

]

write(OUT / "es" / "w16.2.ipynb", es)
print("wrote", OUT / "es" / "w16.2.ipynb")
