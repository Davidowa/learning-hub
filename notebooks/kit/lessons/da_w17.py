"""notebooks/analisis-de-datos/es/w17.ipynb

Source deck: ppts/python/analisis-de-datos/es/w17.es.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 17
## Repaso y examen final

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Este cuaderno no vuelve a explicar temas. Recorre el mapa del semestre, pone a correr los seis
errores que más se cobran, y te deja un ejercicio integrador para que midas dónde estás parado.

Al terminar vas a poder:

1. Ubicar cada tema en el mapa y decir de qué depende.
2. Reconocer los seis errores caros con solo ver el síntoma.
3. Resolver un ejercicio integrador de archivo a hallazgo.
4. Llegar al examen sabiendo qué entra y qué se permite.

### El examen final

| Aspecto | Detalle |
|---|---|
| Contenido | Las ocho unidades, con peso en archivos, pandas y visualización |
| Peso | 20 % de la calificación final |
| Formato | En la computadora del salón, y se sube comprimido a Blackboard |
| Puedes llevar | Apuntes, tareas, libros y lo que hayas generado con IA antes |
| No puedes | Teléfono, audífonos, lentes con IA ni mensajería |
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
---
# Bloque 1 · El semestre en un mapa

Nada de lo que vimos está suelto. Cada tema es la pieza que hace posible el siguiente.

| Tema | Se apoya en | Lo habilita |
|---|---|---|
| Tipos y operadores | El algoritmo en papel | Cualquier cálculo correcto |
| Selección | Comparaciones booleanas | Reglas de negocio |
| Repetición | Selección | Recorrer una tabla entera |
| Funciones | Repetición | Código que se puede probar |
| Colecciones | Funciones | Listas, y el diccionario de `groupby` |
| Archivos y pandas | Colecciones | El análisis sobre datos reales |

## La cadena que atraviesa todo el curso

Una lista es una columna. Una columna con índice es una `Series`. Varias `Series` emparejadas son
un `DataFrame`. Un diccionario es un `BUSCARV`, y agrupar por llave es lo que hace una tabla
dinámica.

Cada una de esas frases es la misma idea con más herramienta encima. Aquí está, en cuatro celdas.
"""),

code("""
# Semana 12: una lista es una columna, con posiciones.
pagos = [9038.10, 6344.53, 7220.66]
print("Lista:", pagos, "· el primero:", pagos[0])
"""),

code("""
# Semana 15.1: una Series es esa columna con etiquetas encima.
serie = pd.Series(pagos, index=["A", "B", "C"])
print(serie)
print("El primero, por etiqueta:", serie["A"])
"""),

code("""
# Semana 15.1: un DataFrame son varias Series emparejadas.
tabla = pd.DataFrame({"credito": ["A", "B", "C"], "pago": pagos,
                      "region": ["Norte", "Sur", "Norte"]})
print(tabla)
"""),

code("""
# Semana 9 con diccionario, y semana 15.3 con groupby. El mismo resultado.
acumulado = {}
for region, pago in zip(tabla["region"], tabla["pago"]):
    acumulado[region] = acumulado.get(region, 0) + pago

print("Con diccionario:", {k: round(v, 2) for k, v in acumulado.items()})
print("Con groupby:    ", tabla.groupby("region")["pago"].sum().round(2).to_dict())
"""),

md("""
Los mismos dos números. La sintaxis cambia y la idea es la misma, y por eso **no hay que memorizar
pandas por separado**: si sabes qué hace un ciclo con acumulador, sabes qué hace un `groupby`.
"""),

md("""
---
# Bloque 2 · Lo que más se cobra

Seis errores. No son los más difíciles, son los que aparecieron en cada entrega del semestre.

Los seis corren aquí abajo. Míralos una vez más antes del examen: lo que hay que reconocer es el
**síntoma**, no la causa.

## 1 · Contar desde uno
"""),

code("""
meses = ["ene", "feb", "mar", "abr", "may"]

try:
    print(meses[5])
except IndexError as e:
    print("Síntoma -> IndexError:", e)

print("El último es meses[4]:", meses[4], "· o meses[-1]:", meses[-1])
"""),

md("""
## 2 · Calcular sin convertir
"""),

code("""
a, b = "5074", "320"

print("Síntoma -> un total absurdo y ningún error:", a + b)
print("Correcto:", int(a) + int(b))
"""),

md("""
Este es el único de los seis que **no lanza nada**. Por eso es el más caro: el número entra al
reporte.

## 3 · Confundir modificar con devolver
"""),

code("""
ventas = [300, 100, 200]
resultado = ventas.sort()

print("Síntoma -> None donde esperabas una lista:", resultado)
print("La lista sí se ordenó:", ventas)
print("Correcto, con sorted:", sorted([300, 100, 200]))
"""),

md("""
## 4 · Declarar el acumulador adentro
"""),

code("""
numeros = [100, 200, 300]

for n in numeros:
    total_mal = 0
    total_mal += n

total_bien = 0
for n in numeros:
    total_bien += n

print("Síntoma -> el total es el último valor:", total_mal)
print("Correcto:", total_bien)
"""),

md("""
## 5 · La asignación encadenada
"""),

code("""
import warnings

df = pd.DataFrame({"region": ["Norte", "Sur", "Norte"], "canal": ["Retail"] * 3})
antes = (df["canal"] == "Online").sum()

with warnings.catch_warnings(record=True) as avisos:
    warnings.simplefilter("always")
    df[df["region"] == "Norte"]["canal"] = "Online"
    print("Aviso:", [type(a.message).__name__ for a in avisos] or "ninguno")

print("Síntoma -> nada cambió:", (df["canal"] == "Online").sum(), "de", antes)

df.loc[df["region"] == "Norte", "canal"] = "Online"
print("Con loc, en un paso:", (df["canal"] == "Online").sum())
"""),

md("""
## 6 · Agrupar antes de limpiar
"""),

code("""
crudo = pd.read_csv("sales.csv")

print("Síntoma -> más grupos de los que existen:", crudo["region"].nunique(), "regiones")
print(sorted(crudo["region"].unique()))

limpio = crudo.copy()
limpio["region"] = limpio["region"].str.strip().str.title()
print()
print("Después de normalizar:", limpio["region"].nunique(), "regiones")
"""),

md("""
### Los seis, en una tabla

| Error | El síntoma que lo delata |
|---|---|
| Contar desde uno | `IndexError: list index out of range` |
| Calcular sin convertir | Un total absurdo, y **ningún error** |
| Modificar contra devolver | `None` donde esperabas datos, o `TypeError: NoneType` |
| Acumulador adentro | El total es el último registro |
| Asignación encadenada | Un warning, y nada cambió en la tabla |
| Agrupar sin limpiar | Más grupos de los que la empresa tiene |

Los dos del medio son los peligrosos, porque el programa corre.
"""),

md("""
---
# Bloque 3 · De archivo a hallazgo

El ejercicio integrador. El orden importa: **inspeccionar, limpiar, agrupar, concluir.** Saltarse el
primero es cómo se llega a un número equivocado.

Corre las celdas y sigue el hilo.

## Inspeccionar
"""),

code("""
ventas = pd.read_csv("sales.csv")

print(ventas.shape)
ventas.info()
"""),

code("""
print("Faltantes:", ventas.isna().sum().sum())
print("Duplicados:", ventas.duplicated().sum())
print("Regiones que cree el archivo:", ventas["region"].nunique())
"""),

md("""
Tres problemas antes de calcular nada: once huecos, siete duplicados y ocho regiones.

## Limpiar
"""),

code("""
ventas = ventas.drop_duplicates()
ventas["region"] = ventas["region"].str.strip().str.title()
ventas["unit_price"] = (ventas["unit_price"]
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.strip().astype(float))
ventas["date"] = pd.to_datetime(ventas["date"])
ventas = ventas.dropna(subset=["units"])
ventas["units"] = ventas["units"].astype(int)
ventas["amount"] = ventas["units"] * ventas["unit_price"]

print(f"{len(ventas)} renglones limpios · {ventas['region'].nunique()} regiones "
      f"· total {ventas['amount'].sum():,.2f}")
"""),

md("""
## Agrupar
"""),

code("""
rejilla = ventas.pivot_table(index="region", columns="channel", values="amount",
                             aggfunc="sum", margins=True, margins_name="Total")

print((rejilla / 1000).round(0))
"""),

code("""
detalle = ventas.groupby(["region", "channel"]).agg(
    ingreso=("amount", "sum"),
    ventas=("amount", "count"),
    ticket=("amount", "mean"),
).round(0).sort_values("ingreso", ascending=False)

print(detalle.head(5))
"""),

md("""
## Concluir

La respuesta es **una frase con dos cifras**. No una tabla, no una gráfica: la conclusión, dicha.
"""),

code("""
mejor = detalle.index[0]
ingreso = detalle.iloc[0]["ingreso"]
parte = ingreso / ventas["amount"].sum()

print(f"{mejor[0]} por {mejor[1]} concentra {ingreso:,.0f} pesos, "
      f"el {parte:.0%} del año. Ahí conviene atender primero.")
"""),

md("""
Fíjate en lo que **no** hay en esa frase: no dice cómo se limpió el archivo, ni cuántas líneas de
código costó. Eso va después, cuando alguien pregunte.

La conclusión primero, la evidencia detrás.

## La trampa del ejercicio

Si hubieras agrupado antes de normalizar la región, el reporte diría otra cosa. Compruébalo.
"""),

code("""
sin_limpiar = pd.read_csv("sales.csv")
sin_limpiar["unit_price"] = (sin_limpiar["unit_price"]
                             .str.replace("$", "", regex=False)
                             .str.replace(",", "", regex=False)
                             .str.strip().astype(float))
sin_limpiar["amount"] = sin_limpiar["units"].fillna(0) * sin_limpiar["unit_price"]

print("Sin limpiar, el norte reporta:")
print(sin_limpiar[sin_limpiar["region"] == "North"]["amount"].sum().round(2))
print()
print("Limpio, el norte reporta:")
print(ventas[ventas["region"] == "North"]["amount"].sum().round(2))
"""),

md("""
Casi un millón de pesos de diferencia en una sola región, y las dos cifras salen del mismo archivo.
La de arriba deja fuera los renglones que decían `" North"` y `"north"`.

Ninguna de las dos lanza error. Solo una es cierta.
"""),

md("""
---
# Autoevaluación

Contesta sin correr nada, y después comprueba. Si fallas más de dos, ese es el tema que hay que
repasar.

### 1 · Índices

`datos = [10, 20, 30, 40]`. ¿Qué devuelve `datos[1:3]`, y cuántos elementos tiene?

### 2 · Tipos

¿Qué imprime `print("3" * 3)` y qué imprime `print(3 * 3)`?

### 3 · Selección

Con `x = 5`, ¿qué imprime esto y por qué?

```python
if x > 10:
    print("alto")
elif x > 3:
    print("medio")
elif x > 4:
    print("nunca")
```

### 4 · Ciclos

¿Cuántas veces se imprime algo con `for i in range(2, 11, 4)`?

### 5 · Funciones

¿Qué vale `r` después de `r = print("hola")`?

### 6 · Colecciones

`{1, 2, 2, 3}` tiene cuántos elementos, y `{"a": 1, "a": 2}` cuántos?

### 7 · Archivos

¿Qué le pasa a un archivo existente al abrirlo con `open(ruta, "w")`?

### 8 · pandas

¿Qué diferencia hay entre `ventas["units"]` y `ventas[["units"]]`?

### 9 · pandas

`pivot_table` sin `aggfunc`, ¿suma o promedia?

### 10 · Visualización

`sns.barplot` sin `estimator`, ¿suma o promedia?
"""),

code("""
# Las respuestas, comprobadas. Córrela después de contestar.
datos = [10, 20, 30, 40]
print("1 ·", datos[1:3], "y tiene", len(datos[1:3]), "elementos")
print("2 ·", repr("3" * 3), "contra", 3 * 3)

x = 5
resultado = "alto" if x > 10 else ("medio" if x > 3 else "otra")
print("3 ·", resultado, "· la tercera rama es inalcanzable, x > 3 la atrapa antes")

print("4 ·", len(list(range(2, 11, 4))), "veces:", list(range(2, 11, 4)))
print("5 ·", repr(print("   (esto es el print de adentro)")), "· print devuelve None")
print("6 ·", len({1, 2, 2, 3}), "y", len({"a": 1, "a": 2}), "· los dos quitan el repetido")
print("7 · lo vacía en el instante en que abre, antes de que puedas leer")

print("8 ·", type(ventas["units"]).__name__, "contra", type(ventas[["units"]]).__name__)

sin_agg = ventas.pivot_table(index="region", columns="channel", values="amount")
con_sum = ventas.pivot_table(index="region", columns="channel", values="amount",
                             aggfunc="sum")
print("9 · promedia:", round(sin_agg.loc["North", "Retail"], 2),
      "contra la suma:", round(con_sum.loc["North", "Retail"], 2))
print("10 · promedia también, igual que pivot_table")
"""),

md("""
---
## Tres ideas para llevarse

**Programar es escribir el procedimiento.** Y por eso el análisis se puede repetir, revisar y
defender cuando alguien pregunte en marzo.

**Limpiar antes de calcular.** Un número equivocado nunca se anuncia solo, y siempre se ve tan
razonable como el correcto. Casi un millón de pesos en una región, de la misma tabla.

**El hallazgo va en el título.** Lo que el lector no puede ver por su cuenta es qué encontraste tú,
y eso es todo tu trabajo.

Cualquier duda sobre la calificación o sobre qué sigue, por correo o por Google Chat.
"""),

]

write(OUT / "es" / "w17.ipynb", es)
print("wrote", OUT / "es" / "w17.ipynb")
