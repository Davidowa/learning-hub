"""notebooks/analisis-de-datos/{es,en}/w15.2.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w15.2.*.yaml
Source code:  A05 - Pandas/03_select_and_filter.py, 04_clean.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, bootstrap_cell, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

# ════════════════════════════════════════════════════════════════════ ESPAÑOL

es = [

md("""
# Análisis de Datos · Semana 15, sesión 2 de 3
## Selección, filtrado y limpieza

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

La sesión pasada diagnosticaste el archivo y no lo tocaste. Hoy se arregla. Vas a escribir
el autofiltro en lugar de picarle, y después vas a reparar los cuatro defectos que trae
`sales.csv`, diciendo en voz alta qué decidiste en cada uno.

Al terminar este cuaderno vas a poder:

1. Elegir columnas por nombre y renglones por condición, con corchetes y con `loc` e `iloc`.
2. Construir una máscara booleana y devolverla a la tabla.
3. Combinar condiciones con `&`, `|`, `~` e `isin`, y explicar por qué las palabras `and` y
   `or` no sirven aquí.
4. Reparar duplicados, texto inconsistente, números guardados como texto y celdas vacías.
5. Asignar con `loc` y explicar por qué la asignación encadenada no hace nada.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Cinco fallan a propósito y llevan un comentario que lo dice.

Esta sesión escribe un archivo, `sales_clean.csv`, en la sesión de Colab. Vive mientras la
sesión esté abierta y desaparece cuando se cierra. Eso está bien: la sesión 15.3 lo vuelve a
crear cuando lo necesite.
"""),

md("""
---
## Preparación
"""),

code("""
import pandas as pd

print("pandas", pd.__version__)
"""),

md("""
### La versión importa hoy más que la sesión pasada

Además del nombre del tipo de una columna de texto (`object` en 2.x, `str` en 3.0), esta
sesión toca Copy-on-Write, y ahí las dos versiones no se comportan igual. El bloque 3 lo
demuestra con las dos salidas escritas, así que no te vas a quedar con la duda de cuál te
tocó.
"""),

bootstrap_cell("es"),

# ──────────────────────────────────────────────────────────── bloque 1

md("""
---
# Bloque 1 · Elegir y filtrar

En la hoja esto es hacer scroll, ocultar columnas y prender y apagar el autofiltro. En
pandas describes lo que quieres y recibes una tabla nueva. La original nunca se toca, así
que puedes probar un filtro sin miedo a arruinar nada.

Este bloque trabaja sobre `employees.csv`, que trae 120 renglones y viene limpio. Practicar
el filtrado sobre datos sucios mezcla dos problemas, y hoy queremos uno a la vez.
"""),

code("""
empleados = pd.read_csv("employees.csv")

print(empleados.shape)
print(empleados.head())
"""),

md("""
## Elegir columnas

Un corchete con un nombre devuelve una `Series`, la columna sola.
"""),

code("""
print(empleados["monthly_salary"].head(3))
"""),

md("""
Un corchete con una lista de nombres devuelve un `DataFrame`. Los corchetes dobles confunden
a todo mundo una vez: el par de afuera es la selección, el par de adentro es la lista de
nombres que estás seleccionando.
"""),

code("""
print(empleados[["employee_id", "area", "monthly_salary"]].head(3))
"""),

md("""
## Elegir renglones

Una condición aplicada a una columna devuelve una columna de verdaderos y falsos, uno por
renglón. Eso es la máscara, y es la idea completa detrás del filtrado en pandas.
"""),

code("""
mascara = empleados["monthly_salary"] > 50000

print(mascara.head())
print()
print("Renglones que cumplen:", mascara.sum())
"""),

md("""
`sum` sobre booleanos funciona porque `True` vale uno y `False` vale cero. Sumar la máscara
cuenta cuántos cumplen, sin escribir un contador.

Devuelta a la tabla entre corchetes, la máscara deja solo los renglones marcados.
"""),

code("""
bien_pagados = empleados[mascara]

print("Ganan más de 50 mil:", len(bien_pagados))
print(bien_pagados.head(3))
"""),

md("""
Normalmente la máscara se escribe en el mismo renglón en lugar de guardarla con nombre. Las
dos formas hacen lo mismo, y la de arriba solo sirve para ver la máscara por dentro.
"""),

code("""
print("Solo el área de Finance:", len(empleados[empleados["area"] == "Finance"]))
"""),

md("""
## Combinar condiciones

| Símbolo | Significa | La regla |
|---|---|---|
| `&` | Las dos | Nunca la palabra `and` |
| `|` | Cualquiera | Nunca la palabra `or` |
| `~` | Lo contrario | Va antes de la condición |
| `isin` | Está en la lista | Reemplaza una fila de barras |

Dos reglas que deben cumplirse a la vez. Fíjate en el `&` y fíjate en los paréntesis: sin
ellos Python aplica la comparación en el orden equivocado.
""".replace("`|`", "`\\|`")),

code("""
finanzas_senior = empleados[(empleados["area"] == "Finance") &
                            (empleados["tenure_months"] > 60)]

print("Finance con más de cinco años:", len(finanzas_senior))
"""),

code("""
cualquiera = empleados[(empleados["area"] == "Finance") |
                       (empleados["area"] == "Sales")]

print("Finance o Sales:", len(cualquiera))
"""),

md("""
Para más de dos opciones, `isin` se lee mejor que una cadena de barras. Es la respuesta de
pandas a un filtro con varias casillas palomeadas.
"""),

code("""
front = empleados[empleados["area"].isin(["Sales", "Marketing"])]
print("Sales o Marketing:", len(front))

back = empleados[~empleados["area"].isin(["Sales", "Marketing"])]
print("Todo lo demás:     ", len(back))

print("Suman el total:", len(front) + len(back), "de", len(empleados))
"""),

md("""
## Dos celdas que fallan a propósito

Las dos reglas de arriba no son estilo. Romperlas produce los dos errores más confusos de
pandas, y vale la pena verlos una vez para reconocerlos después.

### Usar la palabra `and`
"""),

code("""
# FALLA A PROPÓSITO. Con dos Series hay que usar &, no la palabra and.
try:
    empleados[(empleados["area"] == "Finance") and (empleados["tenure_months"] > 60)]
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
El mensaje habla del valor de verdad de una Series y no menciona `and` por ningún lado. La
razón es que `and` le pide a Python un único verdadero o falso, y una máscara trae 120. El
`&` sí sabe trabajar renglón por renglón.

### Olvidar los paréntesis
"""),

code("""
# FALLA A PROPÓSITO. Sin paréntesis, & se evalúa antes que ==.
try:
    empleados[empleados["area"] == "Finance" & empleados["tenure_months"] > 60]
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`&` tiene más precedencia que `==` en Python, así que sin paréntesis lo primero que se
intenta es `"Finance" & empleados["tenure_months"]`, que no significa nada. Cada condición
va entre sus propios paréntesis, siempre, aunque se vea redundante.

## Filtrar sobre texto

Las columnas de texto tienen sus propias herramientas bajo `.str`, y se aplican a la columna
completa. Aquí es donde van a dar los comodines de la hoja de cálculo.
"""),

code("""
gerentes = empleados[empleados["job_title"].str.contains("manager", case=False)]

print("Gerentes de cualquier tipo:", len(gerentes))
print(gerentes[["job_title", "area"]].head(3))
"""),

md("""
`case=False` hace la búsqueda sin distinguir mayúsculas, que es casi siempre lo que quieres
cuando el dato lo capturó una persona.

## Renglones y columnas al mismo tiempo

`loc` toma renglones primero, columnas después, y trabaja con etiquetas.
"""),

code("""
print(gerentes.loc[:, ["area", "job_title", "monthly_salary"]].head(3))
"""),

md("""
`iloc` hace lo mismo con posiciones en lugar de etiquetas. Los números cuentan desde 0 y el
final de un rango no se incluye, igual que las rebanadas de la semana 12.
"""),

code("""
print(empleados.iloc[0:2, 0:3])
"""),

md("""
Los dos puntos solos significan "todo", así que `loc[:, [...]]` es "todos los renglones,
estas columnas". Es el mismo `:` de las rebanadas.

## Ordenar
"""),

code("""
top = empleados.sort_values("monthly_salary", ascending=False)

print(top[["employee_id", "area", "job_title", "monthly_salary"]].head())
"""),

md("""
Con varias columnas, el orden de la lista es el orden de desempate: primero área
alfabéticamente, y dentro de cada área el salario de mayor a menor.
"""),

code("""
por_area = empleados.sort_values(["area", "monthly_salary"], ascending=[True, False])

print(por_area[["area", "job_title", "monthly_salary"]].head())
"""),

md("""
**Predice antes de correr.** `sort_values` devolvió una tabla ordenada. ¿La tabla
`empleados` quedó ordenada también?
"""),

code("""
print("Primer renglón de empleados:")
print(empleados[["employee_id", "monthly_salary"]].head(1))
print()
print("Primer renglón de top:")
print(top[["employee_id", "monthly_salary"]].head(1))
"""),

md("""
`empleados` sigue igual. Casi todos los métodos de pandas devuelven una tabla nueva y dejan
la original intacta, que es exactamente por qué puedes filtrar sin miedo. Si quieres que el
cambio se quede, hay que reasignar: `empleados = empleados.sort_values(...)`.
"""),

# ──────────────────────────────────────────────────────────── bloque 2

md("""
---
# Bloque 2 · Las cuatro reparaciones

Limpiar es la mayor parte del trabajo. `sales.csv` tiene cuatro defectos, y cada uno es de
los que salen en una exportación real.

| Defecto | Cuántos | Se arregla con |
|---|---|---|
| Renglones duplicados | 7 | `drop_duplicates` |
| Región mal capturada | 8 formas | `str.strip` y `str.title` |
| Precio como texto | 324 | `str.replace` y `astype` |
| Unidades vacías | 11 | `dropna` o `fillna` |

Van uno por uno, y cada arreglo deja escrito qué decidió. Eso mismo se te va a pedir en el
proyecto.
"""),

code("""
ventas = pd.read_csv("sales.csv")

print(f"Cargados {len(ventas)} renglones")
"""),

md("""
## Defecto 1 · Los renglones duplicados

Siete registros se capturaron dos veces. Si se quedan, inflan todos los totales.
"""),

code("""
print("Renglones duplicados:", ventas.duplicated().sum())

ventas = ventas.drop_duplicates()
print("Renglones después de quitarlos:", len(ventas))
"""),

md("""
`drop_duplicates` compara renglones completos por omisión. Para tratar un renglón como
duplicado cuando solo se repiten algunas columnas, hay que nombrarlas:

```python
ventas.drop_duplicates(subset=["date", "region", "product"])
```

Eso es una decisión de negocio, no técnica. Dos ventas reales del mismo producto a la misma
región el mismo día no son un duplicado, y la computadora no tiene forma de distinguirlas.

## Defecto 2 · El texto inconsistente

La misma región se tecleó como `"North"`, `"north"`, `"NORTH"` y `" North"`.
"""),

code("""
print("Valores de region antes:", ventas["region"].nunique())

ventas["region"] = ventas["region"].str.strip().str.title()

print("Valores de region después:", ventas["region"].nunique())
print()
print(ventas["region"].value_counts())
"""),

md("""
`.str` da acceso a cualquier método de texto, aplicado a la columna completa. Es el ciclo de
la semana 8 sin escribirlo. `strip` quita los espacios de los extremos y `title` normaliza
las mayúsculas, así que `" North"`, `"north"`, `"NORTH"` y `"North "` terminan siendo el
mismo valor.

Ocho se volvieron cuatro, y el norte pasó de 75 renglones a 95. Esos veinte renglones son
los que un `groupby` de la sesión pasada habría repartido entre regiones que no existen.

## Defecto 3 · El número guardado como texto

`unit_price` llegó como `"$ 2,082.50"`. El símbolo y la coma son formato, y tienen que salir
antes de que el texto pueda volverse número.

Primero, la conversión directa, que no funciona.
"""),

code("""
# FALLA A PROPÓSITO. El signo de pesos y la coma impiden la conversión.
try:
    ventas["unit_price"].astype(float)
except ValueError as e:
    print("ValueError:", str(e)[:120])
"""),

md("""
Ahora en el orden correcto: quitar el formato, y solo entonces convertir.
"""),

code("""
print("unit_price antes:", ventas["unit_price"].iloc[0], "|", ventas["unit_price"].dtype)

ventas["unit_price"] = (
    ventas["unit_price"]
    .str.replace("$", "", regex=False)   # regex=False: trata $ como carácter literal
    .str.replace(",", "", regex=False)   # el separador de miles
    .str.strip()
    .astype(float)                       # hasta aquí el texto puede volverse número
)

print("unit_price después:", ventas["unit_price"].iloc[0], "|", ventas["unit_price"].dtype)
"""),

md("""
`regex=False` importa. Sin él, pandas interpreta el signo de pesos como un símbolo de patrón
y no como el carácter que quieres borrar.

La columna de fecha merece el mismo trato. Como texto se ordena de milagro; como fecha real
se puede comparar, restar y agrupar por mes.
"""),

code("""
ventas["date"] = pd.to_datetime(ventas["date"])

print("dtype de date:", ventas["date"].dtype)
print("La venta más antigua:", ventas["date"].min().date())
print("La más reciente:     ", ventas["date"].max().date())
"""),

md("""
Ese `.min()` es la prueba de que la conversión sirvió. Sobre texto habría comparado
alfabéticamente, y solo salía bien por casualidad, porque el formato pone el año primero.

## Defecto 4 · Las celdas vacías

Once renglones no traen conteo de unidades. Hay tres respuestas honestas, y elegir una es
trabajo del analista, no de la biblioteca.

Antes de elegir, vale la pena ver a qué número lleva cada una.
"""),

code("""
faltan = ventas["units"].isna().sum()
print("Renglones sin conteo de unidades:", faltan)
print()
print("Opción A, descartarlos:   ", round(ventas["units"].dropna().mean(), 2),
      "sobre", ventas["units"].dropna().count(), "renglones")
print("Opción B, rellenar con 0: ", round(ventas["units"].fillna(0).mean(), 2),
      "sobre", ventas["units"].fillna(0).count(), "renglones")
print("Opción C, dejarlos:       ", round(ventas["units"].mean(), 2),
      "sobre", ventas["units"].count(), "renglones")
"""),

md("""
Aquí el monto no se puede calcular sin las unidades, así que el renglón se descarta y la
decisión queda escrita en la salida en lugar de esconderse.
"""),

code("""
antes = len(ventas)
ventas = ventas.dropna(subset=["units"])
print(f"Descartados {antes - len(ventas)} renglones sin conteo de unidades")

ventas["units"] = ventas["units"].astype(int)
print("dtype de units:", ventas["units"].dtype)
print("Renglones que quedan:", len(ventas))
"""),

md("""
Ya sin huecos, la columna puede volver a ser de enteros. Es la conversión que fallaba en la
sesión pasada, y funciona ahora por una sola razón: los faltantes ya no están.

## La columna que en realidad queríamos
"""),

code("""
ventas["amount"] = ventas["units"] * ventas["unit_price"]

print(ventas.head())
print()
print("Total del año:", f"{ventas['amount'].sum():,.2f}")
"""),

md("""
Doce millones ochocientos cincuenta y tres mil, sobre 306 renglones. Ese número solo
significa algo porque las cuatro reparaciones ocurrieron antes. Calculado sobre el archivo
crudo habría salido distinto y con la misma cara de correcto.

## Guardar el archivo limpio
"""),

code("""
ventas.to_csv("sales_clean.csv", index=False)

print(f"Escritos {len(ventas)} renglones limpios en sales_clean.csv")
print(open("sales_clean.csv", encoding="utf-8").readline().strip())
"""),

md("""
`index=False` evita que pandas agregue sus números de renglón como primera columna, que es
casi siempre lo que quieres cuando el archivo va de regreso a una hoja de cálculo.

El archivo queda en la sesión de Colab, junto a los CSV que trajo la celda de preparación.
Se puede volver a leer en cualquier celda de abajo, y desaparece cuando cierras la sesión.
"""),

# ──────────────────────────────────────────────────────────── bloque 3

md("""
---
# Bloque 3 · La trampa que hay que ver una vez

Hay una forma de escribir en la tabla que no escribe nada. No lanza error y no cambia nada.
Es una operación silenciosa que no hace absolutamente nada, y ese silencio es lo peligroso.

Cuando encadenas dos operaciones para asignar, la primera mitad construye una tabla temporal
con los renglones que coinciden. La asignación cae sobre esa copia temporal, que se descarta
en el renglón siguiente.

La demostración corre sobre una copia, para que el archivo que acabas de guardar conserve
sus valores reales. `copy()` es como se dice "de aquí en adelante quiero una tabla aparte".
"""),

code("""
demo = ventas.copy()
del_norte = (demo["region"] == "North").sum()

print("Renglones del norte:", del_norte)
print(demo.loc[demo["region"] == "North", "channel"].value_counts())
"""),

md("""
**Predice antes de correr.** La siguiente celda intenta poner `"Retail"` en el canal de
todos los renglones del norte, con una asignación encadenada. ¿Qué pasa?

- **A.** Todos los renglones del norte quedan en Retail.
- **B.** No cambia nada, y tampoco se lanza ningún error.
- **C.** Se lanza `KeyError` porque `channel` no existe.
- **D.** Se crea una columna nueva llamada `channel`.
"""),

code("""
# FALLA A PROPÓSITO. Esto parece editar la tabla y no la edita.
import warnings

with warnings.catch_warnings(record=True) as avisos:
    warnings.simplefilter("always")
    demo[demo["region"] == "North"]["channel"] = "Retail"
    print("Avisos:", [type(a.message).__name__ for a in avisos] or "ninguno")

print()
print(demo.loc[demo["region"] == "North", "channel"].value_counts())
"""),

md("""
La respuesta es **B**. Los canales del norte siguen repartidos entre Retail, Online y
Wholesale, exactamente como antes.

El aviso que aparece depende de tu versión: `ChainedAssignmentError` en pandas 3.0,
`SettingWithCopyWarning` en 2.x. Los dos dicen lo mismo con distinto nombre, y los dos son
advertencias, no errores. El código sigue corriendo.

### La variante que sí cambia según la versión

Hay otra forma de escribir lo mismo, con la columna primero y la condición después. Esta es
la que de verdad se comporta distinto entre versiones, y por eso vale la pena verla.

| | pandas 2.x | pandas 3.0 |
|---|---|---|
| `df[mask]["col"] = v` | no hace nada | no hace nada |
| `df["col"][mask] = v` | **sí modifica la tabla** | no hace nada |

Corre la celda y compara el número contra la tabla.
"""),

code("""
demo2 = ventas.copy()
antes = (demo2["channel"] == "Retail").sum()

with warnings.catch_warnings(record=True) as avisos:
    warnings.simplefilter("always")
    demo2["channel"][demo2["region"] == "North"] = "Retail"
    print("Avisos:", [type(a.message).__name__ for a in avisos] or "ninguno")

despues = (demo2["channel"] == "Retail").sum()
print()
print("Renglones en Retail antes: ", antes)
print("Renglones en Retail después:", despues)
print("¿Cambió algo?", "sí, esto es pandas 2.x" if antes != despues else "no, esto es pandas 3.0")
"""),

md("""
El mismo código, dos resultados, según qué versión te tocó. Nada te avisa cuál estás
corriendo salvo un warning que es fácil ignorar.

Eso es todo el argumento contra la asignación encadenada: no es que esté mal escrita, es que
su resultado depende de algo que no está en tu código.

## La forma correcta: `loc`, en un solo paso

`ventas.loc[condición, "columna"] = valor`. Una sola instrucción, renglones primero, columna
después. Así pandas sabe que quieres escribir en la tabla original.
"""),

code("""
demo3 = ventas.copy()

demo3.loc[demo3["region"] == "North", "channel"] = "Retail"

print(demo3.loc[demo3["region"] == "North", "channel"].value_counts())
"""),

md("""
Noventa y dos renglones en Retail, que son todos los del norte. Una sola instrucción, sin
advertencias, y el mismo resultado en cualquier versión de pandas.

Y sí, hace un rato el norte tenía 95. Bajó a 92 porque tres de los once renglones sin
unidades eran del norte y se descartaron después. Los dos números son correctos en su
momento del proceso, y eso es justamente por qué conviene imprimir el conteo en cada paso en
lugar de confiar en el de hace cinco celdas.

Esta es la regla que se lleva al proyecto: **todo lo que escriba en la tabla va con `loc`.**
"""),

# ──────────────────────────────────────────────────────── el pago

md("""
---
## El pago: filtrar sobre datos limpios

Ahora sí se puede hacer la pregunta de negocio que abrió la sesión. Ventas del norte por más
de cincuenta mil pesos, que es un filtro de dos condiciones sobre una columna que solo existe
porque limpiaste.
"""),

code("""
sel = ventas[(ventas["region"] == "North") &
             (ventas["amount"] > 50000)]

print("Ventas grandes del norte:", len(sel))
print("Canales por los que entraron:", sorted(sel["channel"].unique()))
print()
print(sel[["date", "channel", "product", "units", "amount"]].head())
"""),

md("""
Veintidós ventas, por los tres canales. Fíjate en el camino que hizo falta para llegar a un
número de dos dígitos: quitar duplicados, normalizar el texto, convertir el precio, resolver
los huecos, calcular el monto, y hasta entonces filtrar.

Si hubieras filtrado sobre el archivo crudo, `amount` no existía, `region` valía ocho cosas
distintas y siete renglones estaban contados doble. El filtro habría corrido igual de rápido
y habría dado otro número.
"""),

# ──────────────────────────────────────────────────────────── errores comunes

md("""
---
## Cuatro errores al limpiar

**Calcular antes de limpiar.** Una suma sobre datos sucios devuelve un número, y ese número
está mal sin decírtelo nunca.

**Usar `and` en lugar de `&`.** El error que sale habla del valor de verdad de una Series y
no ayuda en nada. Ya lo viste arriba, y reconocerlo te ahorra media hora.

**Olvidar los paréntesis.** Sin ellos Python evalúa en el orden equivocado, porque `&` tiene
más precedencia que `==`. Cada condición va entre sus propios paréntesis.

**Rellenar huecos sin decirlo.** Poner cero donde faltaba un dato es una decisión de negocio.
Se toma a propósito y se deja escrita, no se hereda del valor por omisión de un método.
"""),

# ──────────────────────────────────────────────────────────── ejercicios

md("""
---
# Ejercicios

Las soluciones están hasta abajo. Los primeros cuatro son de filtrado sobre `employees.csv`,
los tres siguientes son de limpieza, y el último es tu archivo.

## Filtrar

### Ejercicio 1 · Tres filtros sencillos

Sobre `empleados`, cuenta cuántas personas hay en cada uno de estos casos y imprime los tres
números con su etiqueta:

1. Ganan menos de 30 mil al mes.
2. Tienen más de ocho años de antigüedad, o sea más de 96 meses.
3. Trabajan en Monterrey y ganan más de 40 mil.

### Ejercicio 2 · La negación

Imprime cuántas personas **no** están en Ciudad de México, de dos formas distintas: con `!=`
y con `~` más `isin`. Comprueba que dan el mismo número.

### Ejercicio 3 · Analistas de cualquier área

Usa `.str.contains` para encontrar a todas las personas cuyo puesto incluya la palabra
"analyst", sin importar mayúsculas. Imprime cuántas son y cómo se reparten por área.

### Ejercicio 4 · Los cinco mejor pagados de Sales

Filtra el área de Sales, ordena por salario de mayor a menor y muestra los cinco primeros
con identificador, puesto, antigüedad y salario. Todo en una sola cadena de métodos.

## Limpiar

### Ejercicio 5 · La limpieza como función

Escribe una función `limpiar_ventas(ruta)` que lea el CSV crudo, aplique las cuatro
reparaciones, agregue la columna `amount` y devuelva la tabla limpia. Que imprima una
bitácora de una línea por reparación, diciendo qué encontró y qué hizo.

Pruébala desde cero sobre `sales.csv` y comprueba que llega a los mismos 306 renglones.

### Ejercicio 6 · Los tres totales

Reporta el total del año bajo tres escenarios y ponlos en la misma salida:

1. Sobre el archivo crudo, sin quitar duplicados, tratando los huecos como cero.
2. Después de quitar duplicados, tratando los huecos como cero.
3. Después de quitar duplicados y descartar los renglones sin unidades.

Di en un comentario cuál reportarías y por qué los otros dos estarían mal.

Ojo: para calcular un monto sobre el archivo crudo tienes que convertir el precio primero.

### Ejercicio 7 · La decisión de negocio del duplicado

`drop_duplicates` sin argumentos quitó siete renglones idénticos. Prueba ahora
`drop_duplicates(subset=["date", "region", "product"])` sobre el archivo crudo y compara
cuántos renglones quedan.

Después explica en un comentario por qué el segundo número es mucho más chico, y por qué
usarlo sería un error en este archivo.

## Con tus datos

### Ejercicio 8 · Limpia tu archivo y deja constancia

Aplica a tu propio CSV las reparaciones que necesite y guarda una versión limpia. Por cada
arreglo escribe un renglón diciendo qué encontraste, qué decidiste y cuántos registros se
vieron afectados.

Ninguna asignación encadenada: todo lo que escriba en la tabla va con `loc`.

La prueba: compara el total antes y después de limpiar. Si no cambió, o el archivo estaba
limpio o no limpiaste.
"""),

# ──────────────────────────────────────────────────────────── resumen

md("""
---
## Tres ideas para llevarse

**Un filtro es una columna de verdadero y falso.** Devuelta a la tabla entre corchetes, deja
solo los renglones marcados y no toca la original. Por eso puedes probar sin miedo.

**Limpiar antes de calcular.** La suma sobre datos sucios devuelve un número, y un número
equivocado nunca se anuncia solo. Los doce millones de hoy solo significan algo por las
cuatro reparaciones que ocurrieron antes.

**Escribe con `loc`, en un paso.** La asignación encadenada no hace nada y no lanza error,
que es la peor combinación posible, y encima su resultado cambia entre versiones de pandas.

La siguiente sesión es agrupar y unir. La tabla dinámica y el `BUSCARV`, en una línea cada
uno.
"""),

# ──────────────────────────────────────────────────────────── soluciones

md("""
---
# Soluciones

### Ejercicio 1

```python
print("Ganan menos de 30 mil:",
      len(empleados[empleados["monthly_salary"] < 30000]))

print("Más de ocho años:",
      len(empleados[empleados["tenure_months"] > 96]))

print("Monterrey y más de 40 mil:",
      len(empleados[(empleados["city"] == "Monterrey") &
                    (empleados["monthly_salary"] > 40000)]))
```

El tercero es el único que necesita paréntesis, porque combina dos condiciones. Los otros dos
también pueden llevarlos y no estorban.

### Ejercicio 2

```python
con_distinto = empleados[empleados["city"] != "Mexico City"]
con_isin = empleados[~empleados["city"].isin(["Mexico City"])]

print("Con !=:  ", len(con_distinto))
print("Con ~isin:", len(con_isin))
print("¿Iguales?", len(con_distinto) == len(con_isin))
```

Con un solo valor las dos formas dan lo mismo y `!=` se lee mejor. `~isin` empieza a ganar
en cuanto son tres o cuatro ciudades, porque `!=` encadenado con `&` se vuelve ilegible.

### Ejercicio 3

```python
analistas = empleados[empleados["job_title"].str.contains("analyst", case=False)]

print("Analistas:", len(analistas))
print(analistas["area"].value_counts())
```

`case=False` es lo que hace que "Analyst" y "analyst" cuenten igual. Sin eso el resultado
depende de cómo capturó los puestos quien llenó el archivo.

### Ejercicio 4

```python
print(
    empleados[empleados["area"] == "Sales"]
    .sort_values("monthly_salary", ascending=False)
    [["employee_id", "job_title", "tenure_months", "monthly_salary"]]
    .head()
)
```

Se lee de arriba hacia abajo: filtra, ordena, elige columnas, corta cinco. Cada paso recibe
la tabla que dejó el anterior, y ninguno toca `empleados`.

### Ejercicio 5

```python
def limpiar_ventas(ruta):
    df = pd.read_csv(ruta)
    print(f"Cargados {len(df)} renglones")

    duplicados = df.duplicated().sum()
    df = df.drop_duplicates()
    print(f"Duplicados: {duplicados} encontrados, {duplicados} quitados, quedan {len(df)}")

    antes = df["region"].nunique()
    df["region"] = df["region"].str.strip().str.title()
    print(f"Region: {antes} valores distintos, normalizados a {df['region'].nunique()}")

    df["unit_price"] = (df["unit_price"]
                        .str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.strip()
                        .astype(float))
    df["date"] = pd.to_datetime(df["date"])
    print("unit_price convertido a float, date convertido a fecha")

    huecos = df["units"].isna().sum()
    df = df.dropna(subset=["units"])
    df["units"] = df["units"].astype(int)
    print(f"Units: {huecos} huecos, renglones descartados, quedan {len(df)}")

    df["amount"] = df["units"] * df["unit_price"]
    print(f"Listo: {len(df)} renglones, total {df['amount'].sum():,.2f}")
    return df


limpia = limpiar_ventas("sales.csv")
```

Llega a los mismos 306 renglones y al mismo total. Que la limpieza quepa en una función es
lo que la vuelve repetible, y repetible es lo que la vuelve auditable: cualquiera puede
correrla sobre el archivo original y llegar a tu número.

### Ejercicio 6

```python
crudo = pd.read_csv("sales.csv")
crudo["unit_price"] = (crudo["unit_price"]
                       .str.replace("$", "", regex=False)
                       .str.replace(",", "", regex=False)
                       .str.strip()
                       .astype(float))

esc1 = crudo["units"].fillna(0) * crudo["unit_price"]
sin_dup = crudo.drop_duplicates()
esc2 = sin_dup["units"].fillna(0) * sin_dup["unit_price"]
limpio = sin_dup.dropna(subset=["units"])
esc3 = limpio["units"] * limpio["unit_price"]

print(f"1. Crudo, huecos como cero:      {esc1.sum():>15,.2f}  sobre {len(crudo)} renglones")
print(f"2. Sin duplicados, huecos cero:  {esc2.sum():>15,.2f}  sobre {len(sin_dup)} renglones")
print(f"3. Sin duplicados, sin huecos:   {esc3.sum():>15,.2f}  sobre {len(limpio)} renglones")

# Va el tercero. El primero cuenta siete ventas dos veces, así que infla el total
# con dinero que no entró. El segundo ya no las cuenta doble, pero le asigna cero
# pesos a once ventas que sí ocurrieron, y eso subestima el año.
```

Los escenarios dos y tres dan el mismo total, porque un renglón con cero unidades aporta cero
pesos. Lo que cambia es el conteo de renglones, y por lo tanto cualquier promedio por venta.
Vale la pena notarlo: dos caminos distintos pueden coincidir en el total y separarse en todo
lo demás.

### Ejercicio 7

```python
crudo = pd.read_csv("sales.csv")

print("Renglones:                        ", len(crudo))
print("Sin duplicados exactos:           ", len(crudo.drop_duplicates()))
print("Sin repetir fecha, región, producto:",
      len(crudo.drop_duplicates(subset=["date", "region", "product"])))

# El segundo número es mucho más chico porque el archivo tiene 52 semanas y solo
# cinco productos y cuatro regiones, así que la misma combinación aparece muchas
# veces de forma legítima. Usar ese subset aquí borraría ventas reales: dos ventas
# del mismo producto a la misma región el mismo día son dos ventas, no un error
# de captura. El subset sirve cuando la combinación de columnas identifica de
# verdad al registro, como un folio o una clave de cliente más una fecha.
```

Este ejercicio existe para que `subset` no se vuelva un reflejo. Es la herramienta correcta
cuando hay una clave real, y es un borrador de datos cuando no la hay.

### Ejercicio 8

No hay solución publicada porque el archivo es distinto para cada quien. Se califica sobre
tres cosas: que la bitácora tenga un renglón por reparación con el conteo afectado, que no
haya ninguna asignación encadenada, y que el total antes y después esté reportado.
"""),

]

write(OUT / "es" / "w15.2.ipynb", es)
print("wrote", OUT / "es" / "w15.2.ipynb")
