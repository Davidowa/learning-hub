"""notebooks/analisis-de-datos/{es,en}/w16.1.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w16.1.*.yaml
Source code:  A06 - Data Visualization/01_matplotlib_basics.py,
              02_chart_types.py, 03_labels_and_accessibility.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

LIMPIEZA_ES = """
# La limpieza de la sesión 15.2, en una celda, para que este cuaderno se abra solo.
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
mensual = ventas.groupby(ventas["date"].dt.month)["amount"].sum()

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

print(f"{len(ventas)} renglones limpios, {len(empleados)} empleados")
"""

LIMPIEZA_EN = """
# The cleaning from session 15.2, in one cell, so this notebook opens on its own.
sales = pd.read_csv("sales.csv").drop_duplicates()
sales["region"] = sales["region"].str.strip().str.title()
sales["unit_price"] = (sales["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip().astype(float))
sales["date"] = pd.to_datetime(sales["date"])
sales = sales.dropna(subset=["units"])
sales["units"] = sales["units"].astype(int)
sales["amount"] = sales["units"] * sales["unit_price"]

employees = pd.read_csv("employees.csv")
monthly = sales.groupby(sales["date"].dt.month)["amount"].sum()

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print(f"{len(sales)} clean rows, {len(employees)} employees")
"""

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 16, sesión 1 de 2
## Visualización y matplotlib

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Una gráfica es un argumento. Todo lo de esta sesión existe para que ese argumento lo entienda
alguien que no estuvo en el cuarto cuando lo hiciste.

Al terminar este cuaderno vas a poder:

1. Elegir la gráfica por la pregunta: barra, línea, dispersión o histograma.
2. Construir una gráfica con `matplotlib`, con figura y ejes, y guardarla como imagen.
3. Titular con el hallazgo y no con los nombres de los ejes.
4. Formatear los ejes para que nadie tenga que contar dígitos.
5. Elegir color accesible, y no dejar que el color sea la única señal.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Las gráficas aparecen debajo de la celda que las dibuja, así que
vas a ver el efecto de cada cambio inmediatamente.

Dos celdas dibujan a propósito una gráfica mala, para que compares. Llevan un comentario que
lo dice.
"""),

md("""
---
## Preparación
"""),

code("""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

print("pandas", pd.__version__)
print("matplotlib", plt.matplotlib.__version__)
"""),

bootstrap_cell("es"),

code(LIMPIEZA_ES),

# ──────────────────────────────────────────────────────────── bloque 1

md("""
---
# Bloque 1 · Cuál gráfica

No es una decisión de estilo. Cada forma contesta una pregunta, y usar la equivocada hace que
un número cierto diga algo falso.

| Gráfica | La pregunta que contesta | Ejemplo del curso |
|---|---|---|
| Barra | ¿Cómo se comparan estas categorías? | Ingreso por producto |
| Línea | ¿Cómo cambió esto con el tiempo? | Ingreso por mes |
| Dispersión | ¿Estas dos cifras se mueven juntas? | Sueldo contra antigüedad |
| Histograma | ¿Cómo se reparten los valores? | Distribución de sueldos |

Las cuatro, dibujadas con los datos del curso, una por una.

## Barra: comparar categorías

Ordenada, porque una gráfica de barras sin ordenar obliga al lector a hacer el ranking a ojo.
Horizontal, porque los nombres de las categorías son palabras y las palabras se leen a lo
ancho.
"""),

code("""
por_producto = ventas.groupby("product")["amount"].sum().sort_values() / 1000

fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(por_producto.index, por_producto.values, color="#2B5F8F")
ax.set_title("¿Qué producto trae más ingreso?", loc="left", fontweight="bold")
ax.set_xlabel("Miles de pesos")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()
"""),

md("""
La máquina de espresso trae más de la mitad del ingreso, y el orden de las barras ya contestó
la pregunta sin que nadie tenga que comparar longitudes.

## Línea: el cambio a lo largo de un eje ordenado

Una línea le dice al lector que los puntos están conectados en un orden que significa algo.
Eso es cierto entre enero y febrero.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(MESES, mensual.values / 1000, marker="o", linewidth=2, color="#2B5F8F")
ax.set_title("¿Cómo se movió el ingreso durante el año?", loc="left", fontweight="bold")
ax.set_ylabel("Miles de pesos")
ax.set_ylim(bottom=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()
"""),

md("""
### La regla que sigue de eso

Conectar dos puntos con una línea afirma que hay un recorrido entre ellos. Entre enero y
febrero es cierto. Entre Norte y Sur es falso, y el lector se lo va a creer porque la forma se
lo está diciendo.
"""),

code("""
# DIBUJA MAL A PROPÓSITO. Una línea sobre categorías inventa una trayectoria.
por_region = ventas.groupby("region")["amount"].sum() / 1000

fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))

axes[0].plot(por_region.index, por_region.values, marker="o", color="#B4530A", linewidth=2)
axes[0].set_title("Mal: ¿Norte lleva a Centre?", loc="left", fontweight="bold")

axes[1].bar(por_region.index, por_region.values, color="#2B5F8F")
axes[1].set_title("Bien: cuatro cosas comparables", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Miles de pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()
"""),

md("""
Las dos gráficas traen exactamente los mismos cuatro números. La de la izquierda sugiere que
las regiones están en una secuencia y que hay una caída de Centre a South, cuando el orden es
alfabético y no significa nada.

## Dispersión: la relación entre dos cifras

Un punto por renglón, colocado por dos de sus valores. Es la gráfica que contesta si más de
esto viene con más de aquello.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.scatter(empleados["tenure_months"], empleados["monthly_salary"],
           alpha=0.55, color="#2B5F8F", edgecolor="none")
ax.set_title("¿El sueldo sube con la antigüedad?", loc="left", fontweight="bold")
ax.set_xlabel("Antigüedad en meses")
ax.set_ylabel("Sueldo mensual")

r = empleados["tenure_months"].corr(empleados["monthly_salary"])
ax.annotate(f"correlación = {r:.2f}", xy=(0.04, 0.92), xycoords="axes fraction",
            fontsize=10, color="#5B6B84")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

print("Correlación:", round(r, 3))
"""),

md("""
La correlación le pone número a lo que el ojo está haciendo. Va de menos uno a uno.

Aquí sale 0.28, que es una relación débil: la nube sube un poco a la derecha y aun así hay
gente con dos años ganando más que gente con diez. Un número cerca de cero significa que la
nube no tiene dirección, y un número fuerte **sigue sin significar** que uno causó al otro.

## Histograma: cómo se reparte una columna

Un histograma rebana una columna en rangos y cuenta cuántos renglones caen en cada uno.
Contesta cómo se ve lo típico y qué tan ancho es el reparto.

Una gráfica de barras compara cosas con nombre; un histograma compara rangos de una sola
cosa. Es la diferencia que más se confunde de las cuatro.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.hist(empleados["monthly_salary"], bins=15, color="#2B5F8F", edgecolor="white")
ax.set_title("¿Cómo se reparten los sueldos?", loc="left", fontweight="bold")
ax.set_xlabel("Sueldo mensual")
ax.set_ylabel("Empleados")

promedio = empleados["monthly_salary"].mean()
ax.axvline(promedio, color="#B4530A", linestyle="--", linewidth=2)
ax.annotate(f"promedio {promedio:,.0f}", xy=(promedio, 0), xytext=(6, 6),
            textcoords="offset points", color="#B4530A", fontsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

print("Promedio:", round(promedio))
print("Mediana: ", empleados["monthly_salary"].median())
"""),

md("""
El promedio dibujado encima muestra cuánto esconde. La mayoría de la gente gana por debajo de
él, y unos cuantos sueldos altos lo jalan hacia la derecha. Reportar solo el promedio de esta
columna daría una idea equivocada de lo que gana una persona típica.

## La que casi nunca sirve

Un pastel pide comparar ángulos, que es algo que la gente hace mal. Pasando de tres rebanadas
deja de leerse. Dibuja las dos con los mismos números y la diferencia se ve sola.
"""),

code("""
# DIBUJA MAL A PROPÓSITO, del lado izquierdo. Los dos paneles traen los mismos datos.
partes = ventas.groupby("product")["amount"].sum().sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

axes[0].pie(partes.values, labels=partes.index, autopct="%1.0f%%",
            startangle=90, colors=plt.cm.Blues(range(60, 260, 40)))
axes[0].set_title("En pastel: ¿cuáles dos se parecen más?", loc="left", fontweight="bold")

axes[1].barh(partes.sort_values().index, partes.sort_values().values / 1000, color="#2B5F8F")
axes[1].set_title("En barras: ahora sí se nota", loc="left", fontweight="bold")
axes[1].set_xlabel("Miles de pesos")
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)

fig.tight_layout()
plt.show()
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · Cómo se construye

Dos objetos, y toda gráfica de matplotlib empieza con la misma línea.

Una **figura** es la hoja de papel. Unos **ejes** son un par de ejes dibujados sobre ella.
`subplots()` te entrega las dos cosas de golpe, y así empieza prácticamente toda gráfica que
vas a escribir.

Se dibuja en los ejes, y se guarda la figura.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(MESES, mensual.values / 1000)

fig.savefig("primera.png", dpi=150, bbox_inches="tight")
plt.show()
plt.close(fig)

print("Escrito primera.png")
"""),

md("""
`dpi` controla qué tan nítido sale el archivo: 150 alcanza para proyectar, 300 para imprimir.
`bbox_inches="tight"` recorta el margen blanco de sobra.

`plt.close(fig)` cierra la figura al terminar. Un ciclo que dibuja cincuenta y no las cierra
las deja las cincuenta en memoria, y matplotlib acaba avisándotelo.

## Lo que le falta a esa gráfica

La de arriba es técnicamente correcta y no dice nada. No tiene título, los números del eje no
están etiquetados, y el lector tiene que adivinar qué significa el 1 al 12.

| Elemento | Qué aporta | Método |
|---|---|---|
| Título | El hallazgo, en una frase | `set_title` |
| Etiqueta de eje | Qué se mide, y en qué unidad | `set_ylabel` |
| Base en cero | Que la diferencia no se exagere | `set_ylim` |
| Fuente | De dónde salieron los números | `fig.text` |

Los mismos datos, contados bien.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4.5))

ax.plot(MESES, mensual.values / 1000, marker="o", linewidth=2, color="#2B5F8F")

ax.set_title("Ingreso por mes, 2025", fontsize=14, fontweight="bold", loc="left")
ax.set_ylabel("Miles de pesos")
ax.set_ylim(bottom=0)          # una barra o una línea empiezan en cero, o mienten

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.show()
plt.close(fig)
"""),

md("""
Todo lo que se quitó del marco era tinta que no estaba diciendo nada.

## El eje cortado, que es como se miente con números ciertos

`set_ylim(bottom=0)` no es decoración. Cortar el eje exagera la diferencia, y hacerlo a
propósito es la forma más común de mentir con una gráfica que solo contiene números
correctos.
"""),

code("""
# DIBUJA MAL A PROPÓSITO, del lado izquierdo. Los mismos cuatro números en los dos.
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].bar(por_region.index, por_region.values, color="#B4530A")
axes[0].set_ylim(1400, 4500)                      # el eje cortado
axes[0].set_title("Mal: South parece no existir", loc="left", fontweight="bold")

axes[1].bar(por_region.index, por_region.values, color="#2B5F8F")
axes[1].set_ylim(bottom=0)
axes[1].set_title("Bien: South vende un tercio de North", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Miles de pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()

print("North contra South:", round(por_region["North"] / por_region["South"], 2), "veces")
"""),

md("""
North vende 2.8 veces lo de South. En la gráfica de la izquierda parece veinte veces. Los
cuatro números son los mismos y ninguno está mal.

## Varias gráficas a la vez

`subplots` acepta una cuadrícula. Los ejes regresan como un arreglo que se indexa.
"""),

code("""
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

por_region_ord = ventas.groupby("region")["amount"].sum().sort_values() / 1000
por_canal = ventas.groupby("channel")["amount"].sum().sort_values() / 1000

axes[0].barh(por_region_ord.index, por_region_ord.values, color="#3776AB")
axes[0].set_title("Por región", loc="left", fontweight="bold")

axes[1].barh(por_canal.index, por_canal.values, color="#3776AB")
axes[1].set_title("Por canal", loc="left", fontweight="bold")

for ax in axes:
    ax.set_xlabel("Miles de pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.tight_layout()          # evita que las etiquetas de una encimen a la otra
plt.show()
plt.close(fig)
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · Que se entienda sin ti

La gráfica va a viajar sola en un correo. Todo lo que tengas que explicar en voz alta le falta
escrito.

## El título dice el hallazgo

"Ingreso por mes" describe los ejes, que el lector ya está viendo. "Diciembre concentró el
20 % del ingreso del año" es lo que de verdad encontraste.

Una gráfica titulada con su conclusión se lee una vez. Una titulada con sus ejes se queda
mirando hasta que alguien la explica.
"""),

code("""
pico = mensual.idxmax()
parte = mensual.max() / mensual.sum()

print(f"El mes pico es el {pico} y se llevó {parte:.1%} del año")
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 5))

barras = ax.bar(MESES, mensual.values, color="#C7D6E8", edgecolor="none")

# Una sola barra carga el argumento, así que una sola lleva el color fuerte.
barras[pico - 1].set_color("#2B5F8F")

ax.set_title(f"Diciembre concentró el {parte:.0%} del ingreso del año",
             fontsize=15, fontweight="bold", loc="left", pad=18)

# El subtítulo es donde va la descripción, ahora que el título dice lo que importa.
ax.text(0, 1.02, "Ingreso por mes, 2025", transform=ax.transAxes,
        fontsize=10.5, color="#5B6B84")

# 2567118.5 obliga a contar dígitos. 2.6M se lee sin pensarlo.
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
ax.set_ylabel("Ingreso")
ax.set_ylim(bottom=0)

ax.annotate(f"{mensual.max() / 1_000_000:.2f}M",
            xy=(pico - 1, mensual.max()), xytext=(0, 8), textcoords="offset points",
            ha="center", fontweight="bold", color="#2B5F8F")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(axis="y", alpha=0.3)
ax.tick_params(axis="y", length=0)

# Una gráfica sin fuente es una opinión.
fig.text(0.125, -0.02, "Fuente: sales_clean.csv, 306 registros, 2025",
         fontsize=9, color="#5B6B84")

plt.show()
plt.close(fig)
"""),

md("""
Cuatro cosas cambiaron respecto a la versión anterior, y ninguna tocó los datos.

El **título** dice el hallazgo y el subtítulo se quedó con la descripción. Una **sola barra**
lleva el color intenso: si todo resalta, nada resalta, y las otras once siguen ahí y siguen
siendo comparables, solo dejaron de competir por la atención. El **formateador** cambia las
etiquetas del eje sin tocar los valores de abajo. Y la **fuente** al pie convierte una opinión
en evidencia.

## Color que sobrevive al gris

Alrededor de uno de cada doce hombres tiene alguna forma de daltonismo, y toda gráfica acaba
tarde o temprano impresa en blanco y negro. Dos defensas:

1. **Usa una paleta pensada para eso.** Azul contra naranja se separa para casi todo el
   mundo; rojo contra verde no.
2. **No dejes que el color sea la única señal.** El estilo de línea, la forma del marcador y
   una etiqueta directa sobreviven todos a volverse grises.
"""),

code("""
por_canal_mes = ventas.pivot_table(index=ventas["date"].dt.month,
                                   columns="channel", values="amount", aggfunc="sum")

SEGURO = {"Retail": "#2B5F8F", "Online": "#B4530A", "Wholesale": "#5B6B84"}
ESTILO = {"Retail": "-", "Online": "--", "Wholesale": ":"}
MARCA = {"Retail": "o", "Online": "s", "Wholesale": "^"}

fig, ax = plt.subplots(figsize=(10, 5))

for canal in por_canal_mes.columns:
    ax.plot(MESES, por_canal_mes[canal] / 1000, label=canal, color=SEGURO[canal],
            linestyle=ESTILO[canal], marker=MARCA[canal], linewidth=2)

    # Una etiqueta al final de la línea le gana a una leyenda: el ojo nunca tiene
    # que salirse de los datos para averiguar cuál línea es cuál.
    ax.annotate(canal, xy=(11, por_canal_mes[canal].iloc[-1] / 1000),
                xytext=(8, 0), textcoords="offset points",
                color=SEGURO[canal], fontweight="bold", va="center")

ax.set_title("Mayoreo es lo que produce el pico de diciembre",
             fontsize=15, fontweight="bold", loc="left", pad=18)
ax.text(0, 1.02, "Ingreso por canal y mes, en miles de pesos",
        transform=ax.transAxes, fontsize=10.5, color="#5B6B84")
ax.set_ylim(bottom=0)
ax.set_xlim(-0.4, 12.6)          # espacio a la derecha para las etiquetas
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.show()
plt.close(fig)
"""),

md("""
Esa gráfica se sigue leyendo impresa en gris, porque cada línea trae tres señales además del
color: su estilo de trazo, su marcador y su nombre escrito al final.

## El texto alternativo

Una gráfica en un reporte o en una página necesita una descripción escrita para quien use
lector de pantalla. Se escribe como la frase que dirías en voz alta si la imagen no cargara:
qué muestra, y qué te muestra a ti.

Y se escribe mirando la tabla, no de memoria. Describir una tendencia que los datos no tienen
es la forma más fácil de que una gráfica accesible diga algo falso.
"""),

code("""
print((por_canal_mes / 1000).round(0).to_string())
"""),

code("""
texto_alt = (
    "Gráfica de líneas del ingreso de 2025 por mes para tres canales de venta, en miles "
    "de pesos. Retail se mantiene entre 120 y 320 todo el año. Online oscila entre 36 y "
    "656 sin tendencia clara. Mayoreo es el canal más grande en diez de los doce meses y "
    "salta de 322 en noviembre a 1,611 en diciembre, que es lo que produce el pico de fin "
    "de año."
)
print(texto_alt)
"""),

md("""
Cada cifra de ese párrafo se puede verificar contra la tabla de arriba, y por eso se puede
escribir sin miedo. Compruébalo tú.
"""),

code("""
tabla = (por_canal_mes / 1000).round(0)

print("Retail va de", tabla["Retail"].min(), "a", tabla["Retail"].max())
print("Online va de", tabla["Online"].min(), "a", tabla["Online"].max())
print("Meses en que Mayoreo es el más grande:",
      (tabla.idxmax(axis=1) == "Wholesale").sum(), "de 12")
print("Mayoreo en noviembre:", tabla["Wholesale"].iloc[10],
      "| en diciembre:", tabla["Wholesale"].iloc[11])
"""),

# ──────────────────────────────────────────────────────────── errores comunes

md("""
---
## Cuatro formas de arruinar una gráfica correcta

**Cortar el eje vertical.** Una diferencia del dos por ciento se ve como del cincuenta. Los
números están bien y la gráfica miente. Ya lo viste con North contra South.

**Barras sin ordenar.** El lector tiene que hacer el ranking a ojo. Ordenarlas es gratis y
contesta la pregunta sola.

**Línea sobre categorías.** Conectar Norte con Sur sugiere un recorrido que no existe. Para
categorías van barras.

**Dejar el título por omisión.** Una gráfica sin título ni fuente es una opinión. Con las dos
cosas es evidencia.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Las soluciones están hasta abajo.

### Ejercicio 1 · Elegir sin dibujar

Para cada pregunta, di en un comentario qué gráfica usarías y por qué. No dibujes nada
todavía.

1. ¿Cuál de los tres canales vende más?
2. ¿El ingreso creció o bajó a lo largo del año?
3. ¿Los meses con más ventas son los de mayor ticket promedio?
4. ¿Qué tan parejo es el tamaño de las ventas?

### Ejercicio 2 · Las cuatro, con tus datos

Dibuja una de cada tipo usando las tablas del curso: una barra, una línea, una dispersión y un
histograma. Ponles a todas título, etiqueta de eje y base en cero donde aplique.

Usa una cuadrícula de dos por dos, con `plt.subplots(2, 2)`.

### Ejercicio 3 · De descripción a hallazgo

Toma la gráfica de ingreso por región y escríbele tres títulos distintos:

1. Uno que describa los ejes.
2. Uno que diga el hallazgo con una cifra.
3. Uno que diga el hallazgo con una comparación.

Dibuja la tercera versión completa, con subtítulo, ejes formateados y fuente.

### Ejercicio 4 · El histograma de las ventas

Haz un histograma de la columna `amount` de `ventas`. Dibuja encima el promedio y la mediana,
con colores y estilos distintos, y etiqueta las dos.

Después contesta en un comentario cuál de las dos describe mejor una venta típica, y por qué
están tan separadas.

### Ejercicio 5 · La misma cifra, honesta y tramposa

Toma el ingreso por canal y dibuja dos versiones lado a lado: una con el eje empezando en
cero, y otra con el eje cortado para que la diferencia parezca enorme.

Calcula e imprime la proporción real entre el canal mayor y el menor, para que quede claro
cuánto exagera la segunda.

### Ejercicio 6 · Texto alternativo verificable

Escribe el texto alternativo de la gráfica del ejercicio 3. Después escribe el código que
comprueba cada cifra que mencionaste, como se hizo arriba.

Si alguna cifra no se puede comprobar con una línea de pandas, quítala del texto.

### Ejercicio 7 · Una gráfica de tu proyecto, terminada

Produce una gráfica con los datos de tu proyecto: título que diga el hallazgo, subtítulo
descriptivo, ejes formateados, un elemento resaltado y la fuente al pie. Escribe también su
texto alternativo.

Nada de pastel, y el eje vertical empieza en cero.

La prueba: enséñala sin decir nada. Si tu compañero pregunta qué muestra, al título le falta
el hallazgo.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**La pregunta elige la gráfica.** Barra compara, línea cambia con el tiempo, dispersión
relaciona e histograma reparte. Elegir la forma primero y buscarle datos después es como
salen las gráficas bonitas que no dicen nada.

**Titula con el hallazgo.** El nombre de los ejes ya se ve. Lo que el lector no puede ver solo
es qué encontraste tú.

**El color nunca va solo.** Estilo de línea, marcador o etiqueta directa. Todo eso sobrevive a
una impresión en gris y a quien no distingue dos de tus colores.

La siguiente sesión es seaborn, que hace en una línea varias de las que hoy tomaron ocho, y el
cierre del proyecto integrador.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

### Ejercicio 1

```python
# 1. Barras. Son tres categorías con nombre y la pregunta es cómo se comparan.
#    Ordenadas, para que el orden conteste solo.
# 2. Línea. El eje es el tiempo y los meses van en un orden que significa algo.
# 3. Dispersión. Son dos cifras por mes y la pregunta es si se mueven juntas.
#    Un punto por mes, ventas en un eje y ticket promedio en el otro.
# 4. Histograma. Es una sola columna y la pregunta es cómo se reparte, no cómo
#    se compara contra otra cosa.
```

La cuarta es la que más se falla. "Qué tan parejo" suena a comparación y no lo es: hay una
sola variable, y lo que se quiere ver es su forma.

### Ejercicio 2

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

por_canal = ventas.groupby("channel")["amount"].sum().sort_values() / 1000
axes[0, 0].barh(por_canal.index, por_canal.values, color="#2B5F8F")
axes[0, 0].set_title("Mayoreo trae la mitad del ingreso", loc="left", fontweight="bold")
axes[0, 0].set_xlabel("Miles de pesos")

axes[0, 1].plot(MESES, mensual.values / 1000, marker="o", color="#2B5F8F", linewidth=2)
axes[0, 1].set_title("Diciembre rompe la escala", loc="left", fontweight="bold")
axes[0, 1].set_ylabel("Miles de pesos")
axes[0, 1].set_ylim(bottom=0)

axes[1, 0].scatter(ventas["units"], ventas["amount"] / 1000,
                   alpha=0.5, color="#2B5F8F", edgecolor="none")
axes[1, 0].set_title("Más unidades no siempre es más dinero", loc="left", fontweight="bold")
axes[1, 0].set_xlabel("Unidades")
axes[1, 0].set_ylabel("Miles de pesos")

axes[1, 1].hist(ventas["units"], bins=20, color="#2B5F8F", edgecolor="white")
axes[1, 1].set_title("La mayoría de las ventas son chicas", loc="left", fontweight="bold")
axes[1, 1].set_xlabel("Unidades")
axes[1, 1].set_ylabel("Ventas")

for ax in axes.flat:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()
```

La dispersión de abajo a la izquierda es la interesante: se ven bandas horizontales, una por
producto, porque el monto es unidades por un precio que solo toma cinco valores. Una gráfica
puede enseñarte la estructura del archivo además de la respuesta que buscabas.

### Ejercicio 3

```python
# 1. "Ingreso por región"                       describe los ejes
# 2. "North concentró el 34 % del ingreso"      hallazgo con cifra
# 3. "North vende casi el triple que South"     hallazgo con comparación

parte_norte = por_region["North"] / por_region.sum()
veces = por_region["North"] / por_region["South"]

orden = por_region.sort_values()
fig, ax = plt.subplots(figsize=(9, 4))
barras = ax.barh(orden.index, orden.values, color="#C7D6E8")
barras[-1].set_color("#2B5F8F")

ax.set_title(f"North vende {veces:.1f} veces lo de South",
             fontsize=15, fontweight="bold", loc="left", pad=18)
ax.text(0, 1.04, "Ingreso por región, 2025", transform=ax.transAxes,
        fontsize=10.5, color="#5B6B84")
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v / 1000:.1f}M"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.text(0.125, -0.03, "Fuente: sales_clean.csv, 306 registros, 2025",
         fontsize=9, color="#5B6B84")
plt.show()
```

La tercera es la más útil de las tres porque no obliga al lector a saber si 34 % es mucho.
Una comparación trae su propia referencia.

### Ejercicio 4

```python
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.hist(ventas["amount"] / 1000, bins=30, color="#2B5F8F", edgecolor="white")

promedio = ventas["amount"].mean() / 1000
mediana = ventas["amount"].median() / 1000

ax.axvline(promedio, color="#B4530A", linestyle="--", linewidth=2)
ax.axvline(mediana, color="#0B1B3A", linestyle=":", linewidth=2)
ax.annotate(f"promedio {promedio:,.0f}k", xy=(promedio, 0), xytext=(6, 40),
            textcoords="offset points", color="#B4530A", fontweight="bold")
ax.annotate(f"mediana {mediana:,.0f}k", xy=(mediana, 0), xytext=(-90, 60),
            textcoords="offset points", color="#0B1B3A", fontweight="bold")

ax.set_title("La venta típica es mucho más chica que el promedio",
             loc="left", fontweight="bold")
ax.set_xlabel("Miles de pesos por venta")
ax.set_ylabel("Ventas")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

# La mediana describe mejor una venta típica. El reparto tiene una cola larga a la
# derecha: unas pocas ventas de máquina de espresso valen veinte veces lo que una
# de tarros, y esas jalan el promedio hacia arriba sin que la mayoría se le acerque.
```

Esta es la razón por la que un reporte serio da promedio y mediana juntos. Cuando se separan
tanto, la separación es el hallazgo.

### Ejercicio 5

```python
canal = ventas.groupby("channel")["amount"].sum() / 1000

fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].bar(canal.index, canal.values, color="#2B5F8F")
axes[0].set_ylim(bottom=0)
axes[0].set_title("Honesta", loc="left", fontweight="bold")

axes[1].bar(canal.index, canal.values, color="#B4530A")
axes[1].set_ylim(canal.min() * 0.97, canal.max() * 1.01)
axes[1].set_title("Tramposa: el eje empieza cerca del mínimo", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Miles de pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()

print("Proporción real mayor contra menor:", round(canal.max() / canal.min(), 2))
```

La proporción real es cercana a cuatro y la versión tramposa la hace ver como veinte. Vale la
pena dibujarla una vez, porque es la manipulación que más vas a encontrar en gráficas ajenas.

### Ejercicio 6

```python
texto = (
    "Gráfica de barras horizontales del ingreso de 2025 por región, en millones de "
    "pesos. North es la más alta con 4.35 millones, seguida de Centre con 3.92 y West "
    "con 3.03. South es la más baja con 1.55 millones, casi un tercio de North."
)
print(texto)

print("North:", round(por_region['North'] / 1000, 2), "millones")
print("Centre:", round(por_region['Centre'] / 1000, 2))
print("West:", round(por_region['West'] / 1000, 2))
print("South:", round(por_region['South'] / 1000, 2))
print("South como parte de North:", round(por_region['South'] / por_region['North'], 2))
```

Nota que la descripción da el orden y las cifras, no adjetivos. "North domina claramente" no
le sirve a nadie que no pueda ver la gráfica; "4.35 contra 1.55 millones" sí.

### Ejercicio 7

No hay solución publicada porque los datos son distintos para cada quien. Se califica sobre
cinco cosas: título con hallazgo, subtítulo descriptivo, ejes formateados, un elemento
resaltado y la fuente al pie. El texto alternativo se califica aparte, y cada cifra que
mencione tiene que poder comprobarse.
"""),

]

write(OUT / "es" / "w16.1.ipynb", es)
print("wrote", OUT / "es" / "w16.1.ipynb")


# ════════════════════════════════════════════════════════════════════ ENGLISH

en = [

md("""
# Data Analysis · Week 16, session 1 of 2
## Visualisation and matplotlib

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

A chart is an argument. Everything in this session exists so that argument can be read by
somebody who was not in the room when you made it.

By the end of this notebook you will be able to:

1. Pick the chart from the question: bar, line, scatter or histogram.
2. Build a chart with `matplotlib`, using a figure and axes, and save it as an image.
3. Title the chart with the finding rather than with the names of the axes.
4. Format the axes so nobody has to count digits.
5. Choose accessible colour, and never let colour be the only signal.

### How to use this notebook

Run the cells in order. The charts appear below the cell that draws them, so you see the
effect of every change straight away.

Two cells draw a deliberately bad chart so you can compare. They carry a comment saying so.
"""),

md("""
---
## Setup
"""),

code("""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

print("pandas", pd.__version__)
print("matplotlib", plt.matplotlib.__version__)
"""),

bootstrap_cell("en"),

code(LIMPIEZA_EN),

md("""
---
# Block 1 · Which chart

This is not a style decision. Each shape answers one kind of question, and using the wrong one
makes a true number say something false.

| Chart | The question it answers | Example from the course |
|---|---|---|
| Bar | How do these categories compare? | Revenue per product |
| Line | How did this change over time? | Revenue per month |
| Scatter | Do these two numbers move together? | Salary against tenure |
| Histogram | How are the values spread out? | Distribution of salaries |

All four, drawn with the course data, one at a time.

## Bar: comparing categories

Sorted, because an unsorted bar chart makes the reader do the ranking by eye. Horizontal,
because the category names are words and words read across.
"""),

code("""
by_product = sales.groupby("product")["amount"].sum().sort_values() / 1000

fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(by_product.index, by_product.values, color="#2B5F8F")
ax.set_title("Which product brings the most revenue?", loc="left", fontweight="bold")
ax.set_xlabel("Thousands of pesos")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()
"""),

md("""
The espresso machine brings more than half the revenue, and the order of the bars has already
answered the question without anyone having to compare lengths.

## Line: change along an ordered axis

A line tells the reader the points are connected in an order that means something. That is
true between January and February.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(MONTHS, monthly.values / 1000, marker="o", linewidth=2, color="#2B5F8F")
ax.set_title("How did revenue move through the year?", loc="left", fontweight="bold")
ax.set_ylabel("Thousands of pesos")
ax.set_ylim(bottom=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()
"""),

md("""
### The rule that follows from that

Connecting two points with a line asserts there is a journey between them. Between January and
February that is true. Between North and South it is false, and the reader will believe it
because the shape is telling them so.
"""),

code("""
# DRAWS BADLY ON PURPOSE. A line across categories invents a journey.
by_region = sales.groupby("region")["amount"].sum() / 1000

fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))

axes[0].plot(by_region.index, by_region.values, marker="o", color="#B4530A", linewidth=2)
axes[0].set_title("Wrong: does North lead to Centre?", loc="left", fontweight="bold")

axes[1].bar(by_region.index, by_region.values, color="#2B5F8F")
axes[1].set_title("Right: four comparable things", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Thousands of pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()
"""),

md("""
Both charts carry exactly the same four numbers. The left one suggests the regions sit in a
sequence and that there is a fall from Centre to South, when the order is alphabetical and
means nothing.

## Scatter: the relationship between two numbers

One dot per row, positioned by two of its values. It is the chart that answers whether more of
this comes with more of that.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.scatter(employees["tenure_months"], employees["monthly_salary"],
           alpha=0.55, color="#2B5F8F", edgecolor="none")
ax.set_title("Does salary rise with tenure?", loc="left", fontweight="bold")
ax.set_xlabel("Tenure in months")
ax.set_ylabel("Monthly salary")

r = employees["tenure_months"].corr(employees["monthly_salary"])
ax.annotate(f"correlation = {r:.2f}", xy=(0.04, 0.92), xycoords="axes fraction",
            fontsize=10, color="#5B6B84")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

print("Correlation:", round(r, 3))
"""),

md("""
The correlation puts a number on what the eye is doing. It runs from minus one to one.

Here it comes out at 0.28, a weak relationship: the cloud drifts up to the right and there are
still people with two years earning more than people with ten. A number near zero means the
cloud has no direction, and a strong number **still does not mean** one caused the other.

## Histogram: how one column is spread out

A histogram slices one column into ranges and counts how many rows land in each. It answers
what typical looks like and how wide the spread is.

A bar chart compares named things; a histogram compares ranges of one thing. It is the
distinction people confuse most out of the four.
"""),

code("""
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.hist(employees["monthly_salary"], bins=15, color="#2B5F8F", edgecolor="white")
ax.set_title("How are salaries spread out?", loc="left", fontweight="bold")
ax.set_xlabel("Monthly salary")
ax.set_ylabel("Employees")

mean_salary = employees["monthly_salary"].mean()
ax.axvline(mean_salary, color="#B4530A", linestyle="--", linewidth=2)
ax.annotate(f"mean {mean_salary:,.0f}", xy=(mean_salary, 0), xytext=(6, 6),
            textcoords="offset points", color="#B4530A", fontsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

print("Mean:  ", round(mean_salary))
print("Median:", employees["monthly_salary"].median())
"""),

md("""
The mean drawn on top shows how much it hides. Most people earn below it, and a handful of
high salaries pull it to the right. Reporting only the mean of this column would give a wrong
idea of what a typical person earns.

## The one that almost never works

A pie chart asks the reader to compare angles, which people do badly. Past three slices it
stops being readable. Draw both with the same numbers and the difference shows itself.
"""),

code("""
# DRAWS BADLY ON PURPOSE, on the left. Both panels carry the same data.
shares = sales.groupby("product")["amount"].sum().sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

axes[0].pie(shares.values, labels=shares.index, autopct="%1.0f%%",
            startangle=90, colors=plt.cm.Blues(range(60, 260, 40)))
axes[0].set_title("As a pie: which two are closest?", loc="left", fontweight="bold")

axes[1].barh(shares.sort_values().index, shares.sort_values().values / 1000, color="#2B5F8F")
axes[1].set_title("As bars: now you can tell", loc="left", fontweight="bold")
axes[1].set_xlabel("Thousands of pesos")
axes[1].spines["top"].set_visible(False)
axes[1].spines["right"].set_visible(False)

fig.tight_layout()
plt.show()
"""),

md("""
---
# Block 2 · How a chart is built

Two objects, and every matplotlib chart starts with the same line.

A **figure** is the sheet of paper. An **axes** is one set of axes drawn on it. `subplots()`
hands you both at once, and that is how practically every chart you write will begin.

You draw on the axes, and you save the figure.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(MONTHS, monthly.values / 1000)

fig.savefig("first.png", dpi=150, bbox_inches="tight")
plt.show()
plt.close(fig)

print("Wrote first.png")
"""),

md("""
`dpi` controls how sharp the file comes out: 150 is enough to project, 300 for print.
`bbox_inches="tight"` trims the spare white margin.

`plt.close(fig)` closes the figure when you are done. A loop that draws fifty and closes none
keeps all fifty in memory, and matplotlib eventually warns you about it.

## What that chart is missing

The one above is technically correct and says nothing. It has no title, the axis numbers are
unlabelled, and the reader has to guess what 1 to 12 means.

| Element | What it adds | Method |
|---|---|---|
| Title | The finding, in one sentence | `set_title` |
| Axis label | What is measured, and in what unit | `set_ylabel` |
| Zero baseline | That the difference is not exaggerated | `set_ylim` |
| Source | Where the numbers came from | `fig.text` |

The same data, told properly.
"""),

code("""
fig, ax = plt.subplots(figsize=(9, 4.5))

ax.plot(MONTHS, monthly.values / 1000, marker="o", linewidth=2, color="#2B5F8F")

ax.set_title("Revenue by month, 2025", fontsize=14, fontweight="bold", loc="left")
ax.set_ylabel("Thousands of pesos")
ax.set_ylim(bottom=0)          # a bar or a line starts at zero, or it lies

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.show()
plt.close(fig)
"""),

md("""
Everything stripped from the frame was ink that was not saying anything.

## The cut axis, which is how you lie with true numbers

`set_ylim(bottom=0)` is not decoration. Cutting the axis exaggerates the difference, and doing
it on purpose is the most common way to lie with a chart that contains only correct numbers.
"""),

code("""
# DRAWS BADLY ON PURPOSE, on the left. The same four numbers in both.
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].bar(by_region.index, by_region.values, color="#B4530A")
axes[0].set_ylim(1400, 4500)                      # the cut axis
axes[0].set_title("Wrong: South looks like nothing", loc="left", fontweight="bold")

axes[1].bar(by_region.index, by_region.values, color="#2B5F8F")
axes[1].set_ylim(bottom=0)
axes[1].set_title("Right: South sells a third of North", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Thousands of pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()

print("North against South:", round(by_region["North"] / by_region["South"], 2), "times")
"""),

md("""
North sells 2.8 times what South does. On the left chart it looks like twenty times. The four
numbers are the same and none of them is wrong.

## Several charts at once

`subplots` takes a grid. The axes come back as an array you index into.
"""),

code("""
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

by_region_sorted = sales.groupby("region")["amount"].sum().sort_values() / 1000
by_channel = sales.groupby("channel")["amount"].sum().sort_values() / 1000

axes[0].barh(by_region_sorted.index, by_region_sorted.values, color="#3776AB")
axes[0].set_title("By region", loc="left", fontweight="bold")

axes[1].barh(by_channel.index, by_channel.values, color="#3776AB")
axes[1].set_title("By channel", loc="left", fontweight="bold")

for ax in axes:
    ax.set_xlabel("Thousands of pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.tight_layout()          # keeps one chart's labels off the other
plt.show()
plt.close(fig)
"""),

md("""
---
# Block 3 · Making it readable without you

The chart is going to travel alone in an email. Anything you would have to explain out loud is
something it is missing in writing.

## The title states the finding

"Revenue by month" describes the axes, which the reader can already see. "December carried
20 % of the year's revenue" is what you actually found.

A chart titled with its conclusion is read once. A chart titled with its axes is stared at
until somebody explains it.
"""),

code("""
peak = monthly.idxmax()
share = monthly.max() / monthly.sum()

print(f"The peak month is {peak} and it took {share:.1%} of the year")
"""),

code("""
fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(MONTHS, monthly.values, color="#C7D6E8", edgecolor="none")

# One bar carries the point, so one bar gets the strong colour.
bars[peak - 1].set_color("#2B5F8F")

ax.set_title(f"December carried {share:.0%} of the year's revenue",
             fontsize=15, fontweight="bold", loc="left", pad=18)

# The subtitle is where the description goes, now that the title says the point.
ax.text(0, 1.02, "Revenue by month, 2025", transform=ax.transAxes,
        fontsize=10.5, color="#5B6B84")

# 2567118.5 makes the reader count digits. 2.6M reads without thinking.
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v / 1_000_000:.1f}M"))
ax.set_ylabel("Revenue")
ax.set_ylim(bottom=0)

ax.annotate(f"{monthly.max() / 1_000_000:.2f}M",
            xy=(peak - 1, monthly.max()), xytext=(0, 8), textcoords="offset points",
            ha="center", fontweight="bold", color="#2B5F8F")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.grid(axis="y", alpha=0.3)
ax.tick_params(axis="y", length=0)

# A chart with no source is an opinion.
fig.text(0.125, -0.02, "Source: sales_clean.csv, 306 records, 2025",
         fontsize=9, color="#5B6B84")

plt.show()
plt.close(fig)
"""),

md("""
Four things changed from the previous version, and none of them touched the data.

The **title** states the finding and the subtitle kept the description. A **single bar**
carries the strong colour: if everything is emphasised, nothing is, and the other eleven are
still there and still comparable, they have only stopped competing for attention. The
**formatter** changes the axis labels without touching the underlying values. And the
**source** at the foot turns an opinion into evidence.

## Colour that survives greyscale

Around one man in twelve has some form of colour blindness, and every chart eventually gets
printed in black and white. Two defences:

1. **Use a palette designed for it.** Blue against orange separates for almost everyone; red
   against green does not.
2. **Do not let colour be the only signal.** Line style, marker shape and a direct label all
   survive being turned grey.
"""),

code("""
by_channel_month = sales.pivot_table(index=sales["date"].dt.month,
                                     columns="channel", values="amount", aggfunc="sum")

SAFE = {"Retail": "#2B5F8F", "Online": "#B4530A", "Wholesale": "#5B6B84"}
STYLE = {"Retail": "-", "Online": "--", "Wholesale": ":"}
MARKER = {"Retail": "o", "Online": "s", "Wholesale": "^"}

fig, ax = plt.subplots(figsize=(10, 5))

for channel in by_channel_month.columns:
    ax.plot(MONTHS, by_channel_month[channel] / 1000, label=channel, color=SAFE[channel],
            linestyle=STYLE[channel], marker=MARKER[channel], linewidth=2)

    # A label at the end of the line beats a legend: the reader's eye never has to
    # leave the data to find out which line is which.
    ax.annotate(channel, xy=(11, by_channel_month[channel].iloc[-1] / 1000),
                xytext=(8, 0), textcoords="offset points",
                color=SAFE[channel], fontweight="bold", va="center")

ax.set_title("Wholesale drives the December peak",
             fontsize=15, fontweight="bold", loc="left", pad=18)
ax.text(0, 1.02, "Revenue by channel and month, thousands of pesos",
        transform=ax.transAxes, fontsize=10.5, color="#5B6B84")
ax.set_ylim(bottom=0)
ax.set_xlim(-0.4, 12.6)          # room on the right for the end labels
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", alpha=0.3)

plt.show()
plt.close(fig)
"""),

md("""
That chart still reads printed in grey, because every line carries three signals besides
colour: its stroke style, its marker and its name written at the end.

## The alternative text

A chart in a report or on a web page needs a written description for anyone using a screen
reader. Write it as the sentence you would say out loud if the image failed to load: what it
shows, and what it shows you.

And write it against the table, not from memory. Describing a trend the data does not have is
the easiest way to make an accessible chart say something false.
"""),

code("""
print((by_channel_month / 1000).round(0).to_string())
"""),

code("""
alt_text = (
    "Line chart of 2025 revenue by month for three sales channels, in thousands of "
    "pesos. Retail stays between 120 and 320 all year. Online swings between 36 and 656 "
    "with no clear trend. Wholesale is the largest channel in ten of the twelve months "
    "and jumps from 322 in November to 1,611 in December, which is what produces the "
    "year-end peak."
)
print(alt_text)
"""),

md("""
Every figure in that paragraph can be checked against the table above, and that is why it can
be written without worry. Check it yourself.
"""),

code("""
table = (by_channel_month / 1000).round(0)

print("Retail runs from", table["Retail"].min(), "to", table["Retail"].max())
print("Online runs from", table["Online"].min(), "to", table["Online"].max())
print("Months where Wholesale is largest:",
      (table.idxmax(axis=1) == "Wholesale").sum(), "of 12")
print("Wholesale in November:", table["Wholesale"].iloc[10],
      "| in December:", table["Wholesale"].iloc[11])
"""),

md("""
---
## Four ways to ruin a correct chart

**Cutting the vertical axis.** A two per cent difference looks like fifty. The numbers are
right and the chart lies. You saw it with North against South.

**Unsorted bars.** The reader has to do the ranking by eye. Sorting is free and answers the
question on its own.

**A line across categories.** Connecting North to South suggests a journey that is not there.
Categories get bars.

**Leaving the default title.** A chart with no title and no source is an opinion. With both it
is evidence.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom.

### Exercise 1 · Choosing without drawing

For each question, say in a comment which chart you would use and why. Do not draw anything
yet.

1. Which of the three channels sells most?
2. Did revenue grow or fall through the year?
3. Are the months with more sales also the ones with the highest average ticket?
4. How even is the size of the sales?

### Exercise 2 · All four, with the course data

Draw one of each type using the course tables: a bar, a line, a scatter and a histogram. Give
all of them a title, an axis label and a zero baseline where it applies.

Use a two by two grid, with `plt.subplots(2, 2)`.

### Exercise 3 · From description to finding

Take the revenue-by-region chart and write three different titles for it:

1. One that describes the axes.
2. One that states the finding with a figure.
3. One that states the finding with a comparison.

Draw the third version in full, with subtitle, formatted axes and source.

### Exercise 4 · The histogram of the sales

Make a histogram of the `amount` column of `sales`. Draw the mean and the median on top, in
different colours and styles, and label both.

Then answer in a comment which of the two better describes a typical sale, and why they sit so
far apart.

### Exercise 5 · The same figure, honest and crooked

Take revenue by channel and draw two versions side by side: one with the axis starting at
zero, and one with the axis cut so the difference looks enormous.

Work out and print the real ratio between the biggest and smallest channel, so it is clear how
much the second one exaggerates.

### Exercise 6 · Verifiable alternative text

Write the alternative text for the chart from exercise 3. Then write the code that checks
every figure you mentioned, the way it was done above.

If any figure cannot be checked with one line of pandas, take it out of the text.

### Exercise 7 · A chart from your project, finished

Produce a chart with your project data: a title that states the finding, a descriptive
subtitle, formatted axes, one highlighted element and the source at the foot. Write its
alternative text too.

No pie charts, and the vertical axis starts at zero.

The test: show it without saying anything. If your classmate asks what it shows, the title is
missing the finding.
"""),

md("""
---
## Three ideas to take away

**The question picks the chart.** Bar compares, line changes over time, scatter relates and
histogram spreads. Picking the shape first and finding data for it afterwards is how pretty
charts that say nothing get made.

**Title with the finding.** The names of the axes are already visible. What the reader cannot
see on their own is what you found.

**Colour never travels alone.** Line style, marker or a direct label. All of those survive a
greyscale print and a reader who cannot tell two of your colours apart.

Next session is seaborn, which does in one line several of the things that took eight today,
plus the close of the integrating project.
"""),

md("""
---
# Solutions

### Exercise 1

```python
# 1. Bars. Three named categories and the question is how they compare.
#    Sorted, so the order answers on its own.
# 2. Line. The axis is time and the months sit in an order that means something.
# 3. Scatter. Two figures per month and the question is whether they move
#    together. One dot per month, sales on one axis and average ticket on the other.
# 4. Histogram. It is a single column and the question is how it is spread out,
#    not how it compares against something else.
```

The fourth is the one people get wrong. "How even" sounds like a comparison and it is not:
there is one variable, and what you want to see is its shape.

### Exercise 2

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

by_channel = sales.groupby("channel")["amount"].sum().sort_values() / 1000
axes[0, 0].barh(by_channel.index, by_channel.values, color="#2B5F8F")
axes[0, 0].set_title("Wholesale brings half the revenue", loc="left", fontweight="bold")
axes[0, 0].set_xlabel("Thousands of pesos")

axes[0, 1].plot(MONTHS, monthly.values / 1000, marker="o", color="#2B5F8F", linewidth=2)
axes[0, 1].set_title("December breaks the scale", loc="left", fontweight="bold")
axes[0, 1].set_ylabel("Thousands of pesos")
axes[0, 1].set_ylim(bottom=0)

axes[1, 0].scatter(sales["units"], sales["amount"] / 1000,
                   alpha=0.5, color="#2B5F8F", edgecolor="none")
axes[1, 0].set_title("More units is not always more money", loc="left", fontweight="bold")
axes[1, 0].set_xlabel("Units")
axes[1, 0].set_ylabel("Thousands of pesos")

axes[1, 1].hist(sales["units"], bins=20, color="#2B5F8F", edgecolor="white")
axes[1, 1].set_title("Most sales are small", loc="left", fontweight="bold")
axes[1, 1].set_xlabel("Units")
axes[1, 1].set_ylabel("Sales")

for ax in axes.flat:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()
```

The scatter at the bottom left is the interesting one: horizontal bands appear, one per
product, because the amount is units times a price that only takes five values. A chart can
show you the structure of the file as well as the answer you were after.

### Exercise 3

```python
# 1. "Revenue by region"                        describes the axes
# 2. "North carried 34 % of revenue"            finding with a figure
# 3. "North sells almost three times South"     finding with a comparison

north_share = by_region["North"] / by_region.sum()
times = by_region["North"] / by_region["South"]

ordered = by_region.sort_values()
fig, ax = plt.subplots(figsize=(9, 4))
bars = ax.barh(ordered.index, ordered.values, color="#C7D6E8")
bars[-1].set_color("#2B5F8F")

ax.set_title(f"North sells {times:.1f} times what South sells",
             fontsize=15, fontweight="bold", loc="left", pad=18)
ax.text(0, 1.04, "Revenue by region, 2025", transform=ax.transAxes,
        fontsize=10.5, color="#5B6B84")
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda v, _: f"{v / 1000:.1f}M"))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.text(0.125, -0.03, "Source: sales_clean.csv, 306 records, 2025",
         fontsize=9, color="#5B6B84")
plt.show()
```

The third is the most useful of the three because it does not require the reader to know
whether 34 % is a lot. A comparison brings its own reference.

### Exercise 4

```python
fig, ax = plt.subplots(figsize=(9, 4.5))
ax.hist(sales["amount"] / 1000, bins=30, color="#2B5F8F", edgecolor="white")

mean_sale = sales["amount"].mean() / 1000
median_sale = sales["amount"].median() / 1000

ax.axvline(mean_sale, color="#B4530A", linestyle="--", linewidth=2)
ax.axvline(median_sale, color="#0B1B3A", linestyle=":", linewidth=2)
ax.annotate(f"mean {mean_sale:,.0f}k", xy=(mean_sale, 0), xytext=(6, 40),
            textcoords="offset points", color="#B4530A", fontweight="bold")
ax.annotate(f"median {median_sale:,.0f}k", xy=(median_sale, 0), xytext=(-90, 60),
            textcoords="offset points", color="#0B1B3A", fontweight="bold")

ax.set_title("The typical sale is much smaller than the mean",
             loc="left", fontweight="bold")
ax.set_xlabel("Thousands of pesos per sale")
ax.set_ylabel("Sales")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()

# The median describes a typical sale better. The spread has a long tail to the
# right: a few espresso machine sales are worth twenty times what a mug sale is,
# and those pull the mean up without most of the data going anywhere near it.
```

This is why a serious report gives the mean and the median together. When they separate this
much, the separation is the finding.

### Exercise 5

```python
channel = sales.groupby("channel")["amount"].sum() / 1000

fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))

axes[0].bar(channel.index, channel.values, color="#2B5F8F")
axes[0].set_ylim(bottom=0)
axes[0].set_title("Honest", loc="left", fontweight="bold")

axes[1].bar(channel.index, channel.values, color="#B4530A")
axes[1].set_ylim(channel.min() * 0.97, channel.max() * 1.01)
axes[1].set_title("Crooked: the axis starts near the minimum", loc="left", fontweight="bold")

for ax in axes:
    ax.set_ylabel("Thousands of pesos")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
plt.show()

print("Real ratio, largest to smallest:", round(channel.max() / channel.min(), 2))
```

The real ratio is close to four and the crooked version makes it look like twenty. Worth
drawing once, because it is the manipulation you will meet most often in other people's
charts.

### Exercise 6

```python
text = (
    "Horizontal bar chart of 2025 revenue by region, in millions of pesos. North is "
    "the tallest at 4.35 million, followed by Centre at 3.92 and West at 3.03. South "
    "is the lowest at 1.55 million, roughly a third of North."
)
print(text)

print("North:", round(by_region['North'] / 1000, 2), "million")
print("Centre:", round(by_region['Centre'] / 1000, 2))
print("West:", round(by_region['West'] / 1000, 2))
print("South:", round(by_region['South'] / 1000, 2))
print("South as a share of North:", round(by_region['South'] / by_region['North'], 2))
```

Note that the description gives the order and the figures, not adjectives. "North clearly
dominates" is no use to somebody who cannot see the chart; "4.35 against 1.55 million" is.

### Exercise 7

There is no published solution, because the data is different for everyone. It is graded on
five things: a title with the finding, a descriptive subtitle, formatted axes, one highlighted
element and the source at the foot. The alternative text is graded separately, and every
figure it mentions has to be checkable.
"""),

]

write(OUT / "en" / "w16.1.ipynb", en)
print("wrote", OUT / "en" / "w16.1.ipynb")
