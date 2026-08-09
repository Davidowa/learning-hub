"""notebooks/analisis-de-datos/{es,en}/w09.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w09.*.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

DATOS_ES = """
campanas = ["Instagram", "Meta", "Google", "TikTok"]
clics = [5074, 3820, 6910, 1240]
inversion = [38500, 29800, 51200, 9600]
conversiones = [173, 118, 241, 39]

print(f"{'Campaña':<12}{'Clics':>8}{'Inversión':>12}{'CPC':>8}")
for i in range(len(campanas)):
    print(f"{campanas[i]:<12}{clics[i]:>8,}{inversion[i]:>12,}{inversion[i] / clics[i]:>8.2f}")
"""

DATOS_EN = """
campaigns = ["Instagram", "Meta", "Google", "TikTok"]
clicks = [5074, 3820, 6910, 1240]
spend = [38500, 29800, 51200, 9600]
conversions = [173, 118, 241, 39]

print(f"{'Campaign':<12}{'Clicks':>8}{'Spend':>12}{'CPC':>8}")
for i in range(len(campaigns)):
    print(f"{campaigns[i]:<12}{clicks[i]:>8,}{spend[i]:>12,}{spend[i] / clicks[i]:>8.2f}")
"""

es = [

md("""
# Análisis de Datos · Semana 9
## Acumuladores, banderas y ciclos anidados

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Tres patrones que resuelven casi todo lo que se hace dentro de un ciclo. No son tres temas: son
tres formas de la misma estructura, y reconocer cuál pide el enunciado es la mitad de resolverlo.

Vale la pena decir a dónde va esto. **Todo lo de hoy reaparece en la semana 15 como una sola línea
de pandas.** El acumulador se vuelve `.sum()`, el contador se vuelve `.count()`, la bandera se
vuelve `.any()` y el ciclo anidado se vuelve `groupby` con dos columnas. Practicarlo a mano ahora
es lo que después te deja confiar en la línea corta.

Al terminar este cuaderno vas a poder:

1. Escribir un acumulador, un contador y una bandera, y decir qué pregunta contesta cada uno.
2. Interrumpir o saltar una vuelta con `break` y `continue`.
3. Usar el `else` del `for`, que casi nadie conoce.
4. Leer un ciclo anidado y predecir cuántas vueltas da antes de ejecutarlo.

### Cómo se usa este cuaderno

Ejecuta las celdas en orden. Tres fallan a propósito o dan un resultado inesperado a propósito.

Los datos son las cuatro campañas de la semana pasada.
"""),

code(DATOS_ES),

md("""
---
# Bloque 1 · Los tres patrones

Acumular, contar y marcar.

| Patrón | La pregunta | Valor inicial | Dentro del ciclo |
|---|---|---|---|
| Acumulador | ¿Cuánto suman? | `0` | `total += valor` |
| Contador | ¿Cuántos cumplen? | `0` | `if condición: n += 1` |
| Bandera | ¿Existe al menos uno? | `False` | `if condición: hallado = True` |

Los tres comparten la misma estructura. **Se declara una variable antes del ciclo**, con un valor
inicial que representa "todavía nada". **Dentro del ciclo se actualiza** en cada vuelta. **Al
terminar**, esa variable tiene la respuesta.
"""),

code("""
total_inversion = 0
campanas_grandes = 0
hay_cara = False

for i in range(len(campanas)):
    total_inversion += inversion[i]

    if clics[i] > 5000:
        campanas_grandes += 1

    if inversion[i] / clics[i] > 7.75:
        hay_cara = True

print(f"Inversión total:  ${total_inversion:,}")
print(f"Campañas grandes: {campanas_grandes}")
print(f"Hay alguna cara:  {hay_cara}")
"""),

md("""
Un solo recorrido, tres respuestas.

**Las tres variables se declaran antes del `for`**, y por eso sobreviven a todas las vueltas.

**El acumulador** suma cuánto. Contesta una pregunta de magnitud.

**El contador** suma uno. Contesta una pregunta de cuántos, no de cuánto.

**La bandera** solo pasa de `False` a `True`, y ya nunca regresa. Contesta si existe alguno.

## Contar y sumar no son lo mismo

Este es el error de lectura que más aparece en un parcial. Léelo con cuidado: "cuántas campañas
superan la meta" y "cuánto suman las campañas que superan la meta" son dos preguntas.
"""),

code("""
META = 0.03

cuantas = 0
cuanto = 0

for i in range(len(campanas)):
    conversion = conversiones[i] / clics[i]
    if conversion >= META:
        cuantas += 1
        cuanto += inversion[i]

print(f"¿Cuántas superan la meta?      {cuantas}")
print(f"¿Cuánto suman esas campañas?  ${cuanto:,}")
"""),

md("""
Tres campañas y 119 500 pesos. Los dos números salen del mismo recorrido y contestan cosas
distintas.

La señal en el enunciado: **"cuántos" es un contador, "cuánto" es un acumulador.** Casi siempre
está en la primera palabra de la pregunta.

## El error clásico: declararla adentro

**Predice antes de correr.** ¿Cuánto vale `total` al terminar?

- **A.** 600, porque suma las tres.
- **B.** 300, porque se reinicia en cada vuelta.
- **C.** 0, porque el total se declara al final.
- **D.** Un error, porque `total` no existe antes del ciclo.
"""),

code("""
# FALLA A PROPÓSITO. El acumulador está dentro del ciclo.
ventas = [100, 200, 300]

for v in ventas:
    total = 0
    total += v

print(total)
"""),

md("""
La respuesta es **B**, 300. Cada vuelta borra el total y vuelve a empezar, así que al final vale lo
del último registro.

El programa corre, no marca error, y el resultado equivocado se ve perfectamente normal. Trescientos
es un número creíble para una suma de tres ventas.

**La sangría es lo que decide cuál es cuál.** Compara las dos versiones.
"""),

code("""
print("Con el acumulador DENTRO:")
for v in ventas:
    total = 0
    total += v
    print(f"  vuelta con v={v}, total queda en {total}")
print("  final:", total)

print()
print("Con el acumulador FUERA:")
total = 0
for v in ventas:
    total += v
    print(f"  vuelta con v={v}, total queda en {total}")
print("  final:", total)
"""),

md("""
El rastro vuelta por vuelta lo hace evidente. Cuando un total no cuadre, imprimirlo dentro del
ciclo es la forma más rápida de ver dónde se pierde.

## Acumular el máximo y el mínimo

Hay una cuarta forma del mismo patrón, y es la que sirve para "el mejor" y "el peor".
"""),

code("""
mejor_i = 0
peor_i = 0

for i in range(len(campanas)):
    if inversion[i] / clics[i] < inversion[mejor_i] / clics[mejor_i]:
        mejor_i = i
    if inversion[i] / clics[i] > inversion[peor_i] / clics[peor_i]:
        peor_i = i

print(f"Mejor CPC: {campanas[mejor_i]:<12} ${inversion[mejor_i] / clics[mejor_i]:.2f}")
print(f"Peor CPC:  {campanas[peor_i]:<12} ${inversion[peor_i] / clics[peor_i]:.2f}")
"""),

md("""
El valor inicial no es cero: es **el primer elemento**. Empezar en cero rompería la búsqueda del
mínimo, porque ningún costo por clic es menor que cero y el resultado sería siempre el cero
inicial.

Es el error de "valor inicial imposible", y aparece cada vez que alguien inicializa un mínimo en
cero.
"""),

code("""
# FALLA A PROPÓSITO. Inicializar un mínimo en cero.
minimo_mal = 0

for i in range(len(campanas)):
    cpc = inversion[i] / clics[i]
    if cpc < minimo_mal:
        minimo_mal = cpc

print("Mínimo empezando en cero:", minimo_mal, "<- ninguna campaña es más barata que gratis")
"""),

md("""
---
# Bloque 2 · Romper el flujo

Tres instrucciones que cambian el recorrido normal de un ciclo. La tercera casi nadie la conoce.

| Instrucción | Qué hace | Cuándo se usa |
|---|---|---|
| `break` | Sale del ciclo de inmediato | Ya encontraste lo que buscabas y seguir es desperdicio |
| `continue` | Salta a la siguiente vuelta | Este registro no aplica y no quieres anidar un `if` enorme |
| `else` del `for` | Corre solo si el ciclo terminó sin `break` | Para decir "recorrí todo y no encontré nada" |
"""),

code("""
for i in range(len(campanas)):
    if clics[i] < 2000:
        continue

    if inversion[i] / clics[i] > 7.75:
        print(f"Primera cara: {campanas[i]}")
        break
else:
    print("Ninguna campaña rebasa el umbral.")
"""),

md("""
**`continue`.** Las campañas con menos de 2 000 clics no tienen suficiente volumen para juzgarlas.
Se saltan sin anidar un `if` alrededor de todo lo demás.

**`break`.** En cuanto encuentra la primera, sale. Recorrer las demás no cambiaría la respuesta.

**El `else`.** Va alineado con el `for`, no con el `if`. Corre solo si el ciclo llegó al final sin
toparse con un `break`.

La traza:

| `i` | Campaña | clics | Qué hace |
|---|---|---|---|
| 0 | Instagram | 5074 | Pasa el filtro. 7.59 no rebasa 7.75, sigue |
| 1 | Meta | 3820 | Pasa el filtro. 7.80 sí rebasa, imprime y sale |
| 2 | Google | 6910 | No se evalúa, el `break` ya salió |
| 3 | TikTok | 1240 | No se evalúa |

El `else` del `for` no corre, porque el ciclo salió por `break`. Ese es exactamente su propósito.

Súbele el umbral para ver el otro caso.
"""),

code("""
UMBRAL = 20.00

for i in range(len(campanas)):
    if clics[i] < 2000:
        continue

    if inversion[i] / clics[i] > UMBRAL:
        print(f"Primera cara: {campanas[i]}")
        break
else:
    print(f"Ninguna campaña rebasa los ${UMBRAL:.2f} por clic.")
"""),

md("""
Ahora sí corrió el `else`, porque el ciclo llegó al final sin `break`.

Sin ese `else`, para conseguir lo mismo harías falta una bandera y un `if` después del ciclo. El
`else` del `for` es exactamente eso, empaquetado.
"""),

code("""
# Lo mismo, con bandera. Funciona igual y ocupa dos líneas más.
encontrada = False

for i in range(len(campanas)):
    if clics[i] < 2000:
        continue
    if inversion[i] / clics[i] > UMBRAL:
        print(f"Primera cara: {campanas[i]}")
        encontrada = True
        break

if not encontrada:
    print(f"Ninguna campaña rebasa los ${UMBRAL:.2f} por clic.")
"""),

md("""
Las dos formas son correctas. La de la bandera se entiende sin conocer el `else` del `for`, y por
eso mucha gente la prefiere. La otra es más corta y no puede olvidársele actualizar la bandera.

## El riesgo del `else` mal alineado
"""),

code("""
# FALLA A PROPÓSITO. El else está alineado con el if, no con el for.
for i in range(len(campanas)):
    if inversion[i] / clics[i] > 7.75:
        print(f"Cara: {campanas[i]}")
    else:
        print(f"  (barata: {campanas[i]})")
"""),

md("""
Ese `else` pertenece al `if` y corre en cada vuelta que no cumple, que es una cosa completamente
distinta. Los dos programas son válidos y hacen cosas diferentes, y lo único que los separa son
cuatro espacios.
"""),

md("""
---
# Bloque 3 · Ciclos anidados

Un ciclo dentro de otro. El de adentro da todas sus vueltas por cada vuelta del de afuera.
"""),

code("""
regiones = ["Norte", "Centro"]
canales = ["Retail", "Online"]

for region in regiones:
    for canal in canales:
        print(f"{region} · {canal}")
"""),

md("""
**La multiplicación.** Dos regiones por dos canales dan cuatro vueltas. Con cuatro y tres serían
doce.

**El orden.** El de afuera avanza una posición solo cuando el de adentro terminó todas las suyas.

**El límite.** Cien por cien son diez mil vueltas. Anidar tres niveles sobre listas largas se vuelve
lento rápido.

Cuéntalas en lugar de suponerlas.
"""),

code("""
regiones = ["Norte", "Centro", "Sur", "Oeste"]
canales = ["Retail", "Online", "Mayoreo"]

vueltas = 0
for region in regiones:
    for canal in canales:
        vueltas += 1

print(f"{len(regiones)} regiones × {len(canales)} canales = {vueltas} vueltas")
"""),

md("""
## Un cruce con datos

El anidado se vuelve útil cuando cada combinación produce un renglón de reporte.
"""),

code("""
# Una cifra por combinación, escrita a mano para el ejemplo.
VENTAS = {
    ("Norte", "Retail"): 1331426, ("Norte", "Online"): 978286, ("Norte", "Mayoreo"): 2042264,
    ("Centro", "Retail"): 490472, ("Centro", "Online"): 1291740, ("Centro", "Mayoreo"): 2136767,
    ("Sur", "Retail"): 271090, ("Sur", "Online"): 420216, ("Sur", "Mayoreo"): 861697,
    ("Oeste", "Retail"): 738049, ("Oeste", "Online"): 589081, ("Oeste", "Mayoreo"): 1702889,
}

print(f"{'Región':<10}" + "".join(f"{c:>12}" for c in canales) + f"{'Total':>12}")
print("-" * 58)

gran_total = 0
for region in regiones:
    fila = 0
    for canal in canales:
        fila += VENTAS[(region, canal)]
    gran_total += fila
    celdas = "".join(f"{VENTAS[(region, canal)] / 1000:>12,.0f}" for canal in canales)
    print(f"{region:<10}{celdas}{fila / 1000:>12,.0f}")

print("-" * 58)
print(f"{'Total':<10}{'':>36}{gran_total / 1000:>12,.0f}")
"""),

md("""
Un acumulador por fila y otro global, dentro de un anidado. Esas veinte líneas son exactamente lo
que la semana 15.3 escribe así:

```python
ventas.pivot_table(index="region", columns="channel", values="amount",
                   aggfunc="sum", margins=True)
```

Vale la pena verlas juntas una vez. Lo que pandas te quita no es el concepto, es la contabilidad.

## Reusar la variable del ciclo interno
"""),

code("""
# FALLA A PROPÓSITO. Los dos ciclos usan i.
for i in range(3):
    for i in range(2):        # el de adentro pisa al de afuera
        pass
    print("Vuelta de afuera, i vale:", i)
"""),

md("""
El `i` de afuera se perdió: al terminar el interno vale 1, siempre. Con listas cortas el síntoma es
sutil; con índices de verdad, el recorrido se descompone en silencio.

**Las variables de los dos ciclos tienen que llamarse distinto**, y de preferencia decir qué
recorren: `region` y `canal` en lugar de `i` y `j`.

## ¿Hacía falta anidar?

Antes de meter un ciclo dentro de otro, pregunta si un `continue` en el primero resolvía lo mismo.
"""),

code("""
# Anidado innecesario: recorrer todo y filtrar dentro.
print("Con anidado:")
for region in regiones:
    for canal in canales:
        if canal == "Mayoreo":
            print(f"  {region} · {canal}: {VENTAS[(region, canal)] / 1000:,.0f}")

# Lo mismo, sin el ciclo interno.
print()
print("Sin anidado:")
for region in regiones:
    print(f"  {region} · Mayoreo: {VENTAS[(region, 'Mayoreo')] / 1000:,.0f}")
"""),

md("""
Doce vueltas contra cuatro, para el mismo resultado. El ciclo interno existía solo para descartar
dos de cada tres casos.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## Los tres patrones

### Ejercicio 1 · Uno de cada uno

En un solo recorrido de las cuatro campañas, calcula: el total de clics, cuántas tienen más de
150 conversiones, y si existe alguna con conversión por debajo del 3 %.

### Ejercicio 2 · Contar contra sumar

Contesta las cuatro preguntas, distinguiendo bien cuál es contador y cuál acumulador:

1. ¿Cuántas campañas cuestan más de 7.60 por clic?
2. ¿Cuánto se invirtió en esas campañas?
3. ¿Cuántas conversiones trajeron entre todas?
4. ¿Cuánto costó cada conversión, en promedio, en esas campañas?

### Ejercicio 3 · El mejor por otra métrica

Encuentra la campaña con el mejor costo por conversión, no por clic. Imprime su nombre, su costo
por conversión y cuánto mejor es que el peor.

Inicializa con el primer elemento, no con cero.

## Romper el flujo

### Ejercicio 4 · `continue` que evita un `if` grande

Escribe un ciclo que reporte el costo por conversión solo de las campañas con más de 100
conversiones, usando `continue` para saltar las demás.

Después escríbelo con un `if` que envuelva todo el cuerpo, y compara cuál se lee mejor.

### Ejercicio 5 · `break` con `else`

Busca la primera campaña que cumpla dos condiciones a la vez: más de 5 000 clics y conversión por
arriba del 3.4 %. Si no hay ninguna, dilo con el `else` del `for`.

Prueba con un umbral que sí encuentre y con uno que no.

### Ejercicio 6 · Contar sin recorrer de más

Escribe un ciclo que se detenga en cuanto la inversión acumulada rebase 100 000, e imprima cuántas
campañas hicieron falta.

## Anidados

### Ejercicio 7 · Predecir las vueltas

Sin correr nada, di cuántas veces se imprime algo en cada uno de estos tres, y después compruébalo.

```python
for a in range(3):
    for b in range(4):
        print(a, b)

for a in range(3):
    for b in range(a):
        print(a, b)

for a in range(3):
    for b in range(4):
        if b == 2:
            break
        print(a, b)
```

El segundo y el tercero son los interesantes. Explica por qué en un comentario.

### Ejercicio 8 · Un reporte cruzado

Con dos listas de categorías de tu área, por ejemplo región y producto, escribe un ciclo anidado
que imprima cada combinación con una métrica calculada. Agrega un acumulador y un contador al
recorrido.

Las variables de los dos ciclos tienen que llamarse distinto y decir qué recorren.

La prueba: cuenta a mano cuántas líneas debería imprimir. Si no coincide, el anidado está mal.
"""),

md("""
---
## Tres ideas para llevarse

**La variable vive fuera del ciclo.** Declararla adentro la reinicia en cada vuelta, y el resultado
equivocado se ve perfectamente normal.

**Contar y sumar no son lo mismo.** "Cuántos cumplen" es un contador, "cuánto suman" es un
acumulador, y el enunciado casi siempre lo dice en la primera palabra.

**Las vueltas se multiplican.** Dos por dos son cuatro, y cien por cien son diez mil. Ahí es donde un
anidado deja de ser gratis.

La siguiente sesión es cómo empaquetar un cálculo para no volver a escribirlo nunca.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
total_clics = 0
muchas_conversiones = 0
hay_baja = False

for i in range(len(campanas)):
    total_clics += clics[i]
    if conversiones[i] > 150:
        muchas_conversiones += 1
    if conversiones[i] / clics[i] < 0.03:
        hay_baja = True

print(f"Total de clics:            {total_clics:,}")
print(f"Con más de 150 conversiones: {muchas_conversiones}")
print(f"Hay alguna bajo el 3 %:     {hay_baja}")
```

Un solo recorrido para tres respuestas. Recorrer tres veces también funciona y cuesta tres veces
más, lo cual con cuatro campañas da igual y con trescientas mil no.

### Ejercicio 2

```python
UMBRAL = 7.60

cuantas = 0
invertido = 0
conv_totales = 0

for i in range(len(campanas)):
    if inversion[i] / clics[i] > UMBRAL:
        cuantas += 1
        invertido += inversion[i]
        conv_totales += conversiones[i]

print(f"1. Cuántas cuestan más de {UMBRAL}: {cuantas}")
print(f"2. Cuánto se invirtió:            ${invertido:,}")
print(f"3. Cuántas conversiones trajeron:  {conv_totales}")
print(f"4. Costo por conversión promedio: ${invertido / conv_totales:,.2f}")
```

La cuarta es la interesante: es el acumulado entre el acumulado, no el promedio de los promedios.
Es el mismo cuidado del costo por clic global de la semana pasada.

### Ejercicio 3

```python
mejor = 0
peor = 0

for i in range(len(campanas)):
    cpa = inversion[i] / conversiones[i]
    if cpa < inversion[mejor] / conversiones[mejor]:
        mejor = i
    if cpa > inversion[peor] / conversiones[peor]:
        peor = i

cpa_mejor = inversion[mejor] / conversiones[mejor]
cpa_peor = inversion[peor] / conversiones[peor]

print(f"Mejor: {campanas[mejor]:<12} ${cpa_mejor:>8,.2f} por conversión")
print(f"Peor:  {campanas[peor]:<12} ${cpa_peor:>8,.2f} por conversión")
print(f"El mejor cuesta {cpa_peor / cpa_mejor:.2f} veces menos que el peor")
```

Inicializar en `0` como **índice** es correcto; inicializar el costo en `0` como **valor** no lo
sería. La diferencia está en que aquí el cero es una posición válida de la lista, no un valor
imposible de la métrica.

### Ejercicio 4

```python
print("Con continue:")
for i in range(len(campanas)):
    if conversiones[i] <= 100:
        continue
    print(f"  {campanas[i]:<12} ${inversion[i] / conversiones[i]:>8,.2f}")

print("\\nCon if envolvente:")
for i in range(len(campanas)):
    if conversiones[i] > 100:
        print(f"  {campanas[i]:<12} ${inversion[i] / conversiones[i]:>8,.2f}")
```

Con una sola línea dentro no se nota la diferencia. Se nota cuando el cuerpo tiene quince líneas:
el `continue` las deja todas a un nivel de sangría, y el `if` envolvente las mete todas un nivel
más adentro.

### Ejercicio 5

```python
for umbral_conv in [0.034, 0.10]:
    print(f"Buscando conversión sobre {umbral_conv:.1%}:")
    for i in range(len(campanas)):
        if clics[i] <= 5000:
            continue
        if conversiones[i] / clics[i] > umbral_conv:
            print(f"  Encontrada: {campanas[i]}")
            break
    else:
        print("  Ninguna cumple las dos condiciones.")
    print()
```

Con 3.4 % encuentra Google; con 10 % no encuentra nada y corre el `else`. Meter los dos umbrales en
un ciclo de afuera es lo que permite probar los dos caminos sin duplicar el código.

### Ejercicio 6

```python
LIMITE = 100000
acumulado = 0
cuantas = 0

for i in range(len(campanas)):
    acumulado += inversion[i]
    cuantas += 1
    if acumulado > LIMITE:
        break

print(f"Hicieron falta {cuantas} campañas para rebasar {LIMITE:,}")
print(f"Acumulado al detenerse: {acumulado:,}")
```

Tres campañas y 119 500. Nota que el contador sube **antes** del `break`, porque la campaña que
rebasó el límite sí cuenta. Ponerlo después daría dos, y las dos lecturas necesitan que decidas
cuál querías.

### Ejercicio 7

```python
# El primero: 12 veces. Tres por cuatro, sin condiciones.
# El segundo: 3 veces. range(a) da cero vueltas cuando a es 0, una cuando es 1
#   y dos cuando es 2. Cero más uno más dos son tres.
# El tercero: 6 veces. El break corta el ciclo interno en b == 2, así que cada
#   vuelta de afuera imprime b = 0 y b = 1, y son tres vueltas de afuera.

n = 0
for a in range(3):
    for b in range(4):
        n += 1
print("Primero:", n)

n = 0
for a in range(3):
    for b in range(a):
        n += 1
print("Segundo:", n)

n = 0
for a in range(3):
    for b in range(4):
        if b == 2:
            break
        n += 1
print("Tercero:", n)
```

El segundo es el patrón de "cada uno contra los anteriores", y aparece cuando comparas todos los
pares de una lista sin repetir. El tercero enseña que un `break` en el ciclo interno **solo sale del
interno**, no de los dos.

### Ejercicio 8

No hay solución publicada porque las categorías son distintas para cada quien. Se califica sobre
cuatro cosas: que las variables de los dos ciclos tengan nombres que digan qué recorren, que el
acumulador y el contador estén declarados fuera de los dos ciclos, que la cuenta a mano de los
renglones coincida con la salida, y que el reporte tenga encabezado.
"""),

]

write(OUT / "es" / "w09.ipynb", es)
print("wrote", OUT / "es" / "w09.ipynb")


en = [

md("""
# Data Analysis · Week 9
## Accumulators, flags and nested loops

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

Three patterns that solve nearly everything done inside a loop. They are not three topics: they
are three forms of the same structure, and recognising which one the question is asking for is
half of solving it.

It is worth saying where this goes. **Everything from today comes back in week 15 as a single line
of pandas.** The accumulator becomes `.sum()`, the counter becomes `.count()`, the flag becomes
`.any()`, and the nested loop becomes `groupby` on two columns. Practising it by hand now is what
later lets you trust the short line.

By the end of this notebook you will be able to:

1. Write an accumulator, a counter and a flag, and say what question each answers.
2. Interrupt or skip a pass with `break` and `continue`.
3. Use the `for` loop's `else`, which almost nobody knows about.
4. Read a nested loop and predict how many passes it makes before running it.

### How to use this notebook

Run the cells in order. Three fail on purpose or give a deliberately surprising result.

The data is the four campaigns from last week.
"""),

code(DATOS_EN),

md("""
---
# Block 1 · The three patterns

Accumulate, count and mark.

| Pattern | The question | Starting value | Inside the loop |
|---|---|---|---|
| Accumulator | How much do they add up to? | `0` | `total += value` |
| Counter | How many qualify? | `0` | `if condition: n += 1` |
| Flag | Is there at least one? | `False` | `if condition: found = True` |

All three share the same structure. **A variable is declared before the loop**, with a starting
value meaning "nothing yet". **Inside the loop it gets updated** on every pass. **When it ends**,
that variable holds the answer.
"""),

code("""
total_spend = 0
large_campaigns = 0
any_expensive = False

for i in range(len(campaigns)):
    total_spend += spend[i]

    if clicks[i] > 5000:
        large_campaigns += 1

    if spend[i] / clicks[i] > 7.75:
        any_expensive = True

print(f"Total spend:      ${total_spend:,}")
print(f"Large campaigns:  {large_campaigns}")
print(f"Any expensive:    {any_expensive}")
"""),

md("""
One pass, three answers.

**All three variables are declared before the `for`**, which is why they survive every pass.

**The accumulator** adds how much. It answers a question of magnitude.

**The counter** adds one. It answers a question of how many, not how much.

**The flag** only goes from `False` to `True`, and never comes back. It answers whether any exist.

## Counting and summing are not the same

This is the reading error that turns up most in an exam. Read it carefully: "how many campaigns
beat the target" and "how much do the campaigns that beat the target add up to" are two questions.
"""),

code("""
TARGET = 0.03

how_many = 0
how_much = 0

for i in range(len(campaigns)):
    conversion = conversions[i] / clicks[i]
    if conversion >= TARGET:
        how_many += 1
        how_much += spend[i]

print(f"How many beat the target?      {how_many}")
print(f"How much did they add up to?  ${how_much:,}")
"""),

md("""
Three campaigns and 119,500 pesos. Both numbers come from the same pass and answer different
things.

The signal in the wording: **"how many" is a counter, "how much" is an accumulator.** It is almost
always in the first word of the question.

## The classic error: declaring it inside

**Predict before you run.** What is `total` when it finishes?

- **A.** 600, because it adds all three.
- **B.** 300, because it resets on every pass.
- **C.** 0, because the total is declared at the end.
- **D.** An error, because `total` does not exist before the loop.
"""),

code("""
# FAILS ON PURPOSE. The accumulator sits inside the loop.
sales_list = [100, 200, 300]

for v in sales_list:
    total = 0
    total += v

print(total)
"""),

md("""
The answer is **B**, 300. Every pass wipes the total and starts again, so at the end it holds the
last record.

The program runs, raises nothing, and the wrong result looks perfectly normal. Three hundred is a
believable number for the sum of three sales.

**Indentation is what decides which is which.** Compare the two versions.
"""),

code("""
print("With the accumulator INSIDE:")
for v in sales_list:
    total = 0
    total += v
    print(f"  pass with v={v}, total is now {total}")
print("  final:", total)

print()
print("With the accumulator OUTSIDE:")
total = 0
for v in sales_list:
    total += v
    print(f"  pass with v={v}, total is now {total}")
print("  final:", total)
"""),

md("""
The pass-by-pass trace makes it obvious. When a total does not add up, printing it inside the loop
is the fastest way to see where it goes.

## Accumulating the maximum and minimum

There is a fourth form of the same pattern, and it is the one for "the best" and "the worst".
"""),

code("""
best_i = 0
worst_i = 0

for i in range(len(campaigns)):
    if spend[i] / clicks[i] < spend[best_i] / clicks[best_i]:
        best_i = i
    if spend[i] / clicks[i] > spend[worst_i] / clicks[worst_i]:
        worst_i = i

print(f"Best CPC:  {campaigns[best_i]:<12} ${spend[best_i] / clicks[best_i]:.2f}")
print(f"Worst CPC: {campaigns[worst_i]:<12} ${spend[worst_i] / clicks[worst_i]:.2f}")
"""),

md("""
The starting value is not zero: it is **the first element**. Starting at zero would break the
search for a minimum, because no cost per click is below zero and the answer would always be the
initial zero.

That is the "impossible starting value" error, and it turns up every time somebody initialises a
minimum at zero.
"""),

code("""
# FAILS ON PURPOSE. Initialising a minimum at zero.
wrong_min = 0

for i in range(len(campaigns)):
    cpc = spend[i] / clicks[i]
    if cpc < wrong_min:
        wrong_min = cpc

print("Minimum starting at zero:", wrong_min, "<- no campaign is cheaper than free")
"""),

md("""
---
# Block 2 · Breaking the flow

Three statements that change a loop's normal path. Almost nobody knows the third.

| Statement | What it does | When it is used |
|---|---|---|
| `break` | Leaves the loop immediately | You already found what you were looking for and continuing is waste |
| `continue` | Skips to the next pass | This record does not apply and you do not want to nest a huge `if` |
| `for` loop `else` | Runs only if the loop finished without a `break` | To say "I walked it all and found nothing" |
"""),

code("""
for i in range(len(campaigns)):
    if clicks[i] < 2000:
        continue

    if spend[i] / clicks[i] > 7.75:
        print(f"First expensive one: {campaigns[i]}")
        break
else:
    print("No campaign clears the threshold.")
"""),

md("""
**`continue`.** Campaigns with fewer than 2,000 clicks do not have enough volume to judge. They get
skipped without nesting an `if` around everything else.

**`break`.** As soon as it finds the first one, it leaves. Walking the rest would not change the
answer.

**The `else`.** It lines up with the `for`, not with the `if`. It runs only if the loop reached the
end without hitting a `break`.

The trace:

| `i` | Campaign | clicks | What it does |
|---|---|---|---|
| 0 | Instagram | 5074 | Passes the filter. 7.59 does not clear 7.75, carries on |
| 1 | Meta | 3820 | Passes the filter. 7.80 does clear it, prints and leaves |
| 2 | Google | 6910 | Not evaluated, the `break` already left |
| 3 | TikTok | 1240 | Not evaluated |

The `for` loop's `else` does not run, because the loop left through a `break`. That is exactly its
purpose.

Raise the threshold to see the other case.
"""),

code("""
THRESHOLD = 20.00

for i in range(len(campaigns)):
    if clicks[i] < 2000:
        continue

    if spend[i] / clicks[i] > THRESHOLD:
        print(f"First expensive one: {campaigns[i]}")
        break
else:
    print(f"No campaign clears ${THRESHOLD:.2f} per click.")
"""),

md("""
Now the `else` did run, because the loop reached the end without a `break`.

Without that `else`, getting the same result would need a flag and an `if` after the loop. The
`for` loop's `else` is exactly that, packaged.
"""),

code("""
# The same thing, with a flag. It works identically and takes two more lines.
found = False

for i in range(len(campaigns)):
    if clicks[i] < 2000:
        continue
    if spend[i] / clicks[i] > THRESHOLD:
        print(f"First expensive one: {campaigns[i]}")
        found = True
        break

if not found:
    print(f"No campaign clears ${THRESHOLD:.2f} per click.")
"""),

md("""
Both forms are correct. The flag version is understandable without knowing the `for` loop's `else`,
which is why many people prefer it. The other is shorter and cannot forget to update the flag.

## The risk of a misaligned `else`
"""),

code("""
# FAILS ON PURPOSE. The else lines up with the if, not with the for.
for i in range(len(campaigns)):
    if spend[i] / clicks[i] > 7.75:
        print(f"Expensive: {campaigns[i]}")
    else:
        print(f"  (cheap: {campaigns[i]})")
"""),

md("""
That `else` belongs to the `if` and runs on every pass that fails, which is a completely different
thing. Both programs are valid and do different things, and all that separates them is four
spaces.
"""),

md("""
---
# Block 3 · Nested loops

A loop inside another. The inner one makes all of its passes for every pass of the outer one.
"""),

code("""
regions = ["North", "Centre"]
channels = ["Retail", "Online"]

for region in regions:
    for channel in channels:
        print(f"{region} · {channel}")
"""),

md("""
**The multiplication.** Two regions by two channels give four passes. With four and three it would
be twelve.

**The order.** The outer one advances a position only when the inner one has finished all of its.

**The limit.** A hundred by a hundred is ten thousand passes. Nesting three levels over long lists
gets slow quickly.

Count them rather than assuming.
"""),

code("""
regions = ["North", "Centre", "South", "West"]
channels = ["Retail", "Online", "Wholesale"]

passes = 0
for region in regions:
    for channel in channels:
        passes += 1

print(f"{len(regions)} regions × {len(channels)} channels = {passes} passes")
"""),

md("""
## A cross-tab with data

Nesting becomes useful when every combination produces a report row.
"""),

code("""
# One figure per combination, written by hand for the example.
SALES = {
    ("North", "Retail"): 1331426, ("North", "Online"): 978286, ("North", "Wholesale"): 2042264,
    ("Centre", "Retail"): 490472, ("Centre", "Online"): 1291740, ("Centre", "Wholesale"): 2136767,
    ("South", "Retail"): 271090, ("South", "Online"): 420216, ("South", "Wholesale"): 861697,
    ("West", "Retail"): 738049, ("West", "Online"): 589081, ("West", "Wholesale"): 1702889,
}

print(f"{'Region':<10}" + "".join(f"{c:>12}" for c in channels) + f"{'Total':>12}")
print("-" * 58)

grand_total = 0
for region in regions:
    row = 0
    for channel in channels:
        row += SALES[(region, channel)]
    grand_total += row
    cells = "".join(f"{SALES[(region, channel)] / 1000:>12,.0f}" for channel in channels)
    print(f"{region:<10}{cells}{row / 1000:>12,.0f}")

print("-" * 58)
print(f"{'Total':<10}{'':>36}{grand_total / 1000:>12,.0f}")
"""),

md("""
One accumulator per row and another overall, inside a nesting. Those twenty lines are exactly what
week 15.3 writes like this:

```python
sales.pivot_table(index="region", columns="channel", values="amount",
                  aggfunc="sum", margins=True)
```

Worth seeing them side by side once. What pandas takes away is not the concept, it is the
bookkeeping.

## Reusing the inner loop's variable
"""),

code("""
# FAILS ON PURPOSE. Both loops use i.
for i in range(3):
    for i in range(2):        # the inner one overwrites the outer
        pass
    print("Outer pass, i is:", i)
"""),

md("""
The outer `i` is lost: when the inner one finishes it is 1, always. With short lists the symptom is
subtle; with real indices, the walk falls apart silently.

**The two loops' variables have to be named differently**, and preferably say what they walk:
`region` and `channel` rather than `i` and `j`.

## Was nesting even needed?

Before putting a loop inside another, ask whether a `continue` in the first would have done the
same.
"""),

code("""
# Unnecessary nesting: walk everything and filter inside.
print("With nesting:")
for region in regions:
    for channel in channels:
        if channel == "Wholesale":
            print(f"  {region} · {channel}: {SALES[(region, channel)] / 1000:,.0f}")

# The same thing, without the inner loop.
print()
print("Without nesting:")
for region in regions:
    print(f"  {region} · Wholesale: {SALES[(region, 'Wholesale')] / 1000:,.0f}")
"""),

md("""
Twelve passes against four, for the same result. The inner loop existed only to discard two out of
every three cases.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## The three patterns

### Exercise 1 · One of each

In a single pass over the four campaigns, work out: the total clicks, how many have more than 150
conversions, and whether any has a conversion rate below 3 %.

### Exercise 2 · Counting against summing

Answer all four questions, carefully distinguishing counter from accumulator:

1. How many campaigns cost more than 7.60 per click?
2. How much was spent on those campaigns?
3. How many conversions did they bring between them?
4. What did each conversion cost, on average, in those campaigns?

### Exercise 3 · The best by another metric

Find the campaign with the best cost per conversion, not per click. Print its name, its cost per
conversion and how much better it is than the worst.

Initialise with the first element, not with zero.

## Breaking the flow

### Exercise 4 · `continue` that avoids a big `if`

Write a loop that reports the cost per conversion only for campaigns with more than 100
conversions, using `continue` to skip the rest.

Then write it with an `if` wrapping the whole body, and compare which reads better.

### Exercise 5 · `break` with `else`

Find the first campaign that satisfies two conditions at once: more than 5,000 clicks and a
conversion rate above 3.4 %. If there is none, say so with the `for` loop's `else`.

Test with a threshold that finds one and with one that does not.

### Exercise 6 · Counting without walking too far

Write a loop that stops as soon as accumulated spend passes 100,000, and prints how many campaigns
it took.

## Nesting

### Exercise 7 · Predicting the passes

Without running anything, say how many times something prints in each of these three, then check.

```python
for a in range(3):
    for b in range(4):
        print(a, b)

for a in range(3):
    for b in range(a):
        print(a, b)

for a in range(3):
    for b in range(4):
        if b == 2:
            break
        print(a, b)
```

The second and third are the interesting ones. Explain why in a comment.

### Exercise 8 · A cross-tab report

With two lists of categories from your field, for example region and product, write a nested loop
printing every combination with a computed metric. Add an accumulator and a counter to the pass.

The two loops' variables have to be named differently and say what they walk.

The test: count by hand how many lines it should print. If it does not match, the nesting is wrong.
"""),

md("""
---
## Three ideas to take away

**The variable lives outside the loop.** Declaring it inside resets it every pass, and the wrong
result looks perfectly normal.

**Counting and summing are not the same.** "How many qualify" is a counter, "how much do they add up
to" is an accumulator, and the wording almost always says which in its first word.

**The passes multiply.** Two by two is four, and a hundred by a hundred is ten thousand. That is
where nesting stops being free.

Next session is how to package a calculation so you never have to write it again.
"""),

md("""
---
# Solutions

### Exercise 1

```python
total_clicks = 0
many_conversions = 0
any_low = False

for i in range(len(campaigns)):
    total_clicks += clicks[i]
    if conversions[i] > 150:
        many_conversions += 1
    if conversions[i] / clicks[i] < 0.03:
        any_low = True

print(f"Total clicks:                {total_clicks:,}")
print(f"With more than 150 conversions: {many_conversions}")
print(f"Any below 3 %:               {any_low}")
```

One pass for three answers. Walking three times also works and costs three times as much, which with
four campaigns makes no difference and with three hundred thousand does.

### Exercise 2

```python
THRESHOLD = 7.60

how_many = 0
spent = 0
total_conversions = 0

for i in range(len(campaigns)):
    if spend[i] / clicks[i] > THRESHOLD:
        how_many += 1
        spent += spend[i]
        total_conversions += conversions[i]

print(f"1. How many cost more than {THRESHOLD}: {how_many}")
print(f"2. How much was spent:              ${spent:,}")
print(f"3. How many conversions they brought: {total_conversions}")
print(f"4. Average cost per conversion:     ${spent / total_conversions:,.2f}")
```

The fourth is the interesting one: it is the accumulated over the accumulated, not the average of
the averages. It is the same care as the overall cost per click from last week.

### Exercise 3

```python
best = 0
worst = 0

for i in range(len(campaigns)):
    cpa = spend[i] / conversions[i]
    if cpa < spend[best] / conversions[best]:
        best = i
    if cpa > spend[worst] / conversions[worst]:
        worst = i

cpa_best = spend[best] / conversions[best]
cpa_worst = spend[worst] / conversions[worst]

print(f"Best:  {campaigns[best]:<12} ${cpa_best:>8,.2f} per conversion")
print(f"Worst: {campaigns[worst]:<12} ${cpa_worst:>8,.2f} per conversion")
print(f"The best costs {cpa_worst / cpa_best:.2f} times less than the worst")
```

Initialising at `0` as an **index** is correct; initialising the cost at `0` as a **value** would not
be. The difference is that here zero is a valid position in the list, not an impossible value of the
metric.

### Exercise 4

```python
print("With continue:")
for i in range(len(campaigns)):
    if conversions[i] <= 100:
        continue
    print(f"  {campaigns[i]:<12} ${spend[i] / conversions[i]:>8,.2f}")

print("\\nWith a wrapping if:")
for i in range(len(campaigns)):
    if conversions[i] > 100:
        print(f"  {campaigns[i]:<12} ${spend[i] / conversions[i]:>8,.2f}")
```

With a single line inside, the difference does not show. It shows when the body is fifteen lines:
`continue` keeps them all at one level of indentation, and the wrapping `if` pushes them all one
level deeper.

### Exercise 5

```python
for conv_threshold in [0.034, 0.10]:
    print(f"Looking for a conversion above {conv_threshold:.1%}:")
    for i in range(len(campaigns)):
        if clicks[i] <= 5000:
            continue
        if conversions[i] / clicks[i] > conv_threshold:
            print(f"  Found: {campaigns[i]}")
            break
    else:
        print("  None satisfies both conditions.")
    print()
```

At 3.4 % it finds Google; at 10 % it finds nothing and the `else` runs. Putting both thresholds in an
outer loop is what lets you test both paths without duplicating the code.

### Exercise 6

```python
LIMIT = 100000
accumulated = 0
how_many = 0

for i in range(len(campaigns)):
    accumulated += spend[i]
    how_many += 1
    if accumulated > LIMIT:
        break

print(f"It took {how_many} campaigns to pass {LIMIT:,}")
print(f"Accumulated on stopping: {accumulated:,}")
```

Three campaigns and 119,500. Note the counter goes up **before** the `break`, because the campaign
that crossed the limit does count. Putting it after would give two, and both readings need you to
decide which you meant.

### Exercise 7

```python
# The first: 12 times. Three by four, no conditions.
# The second: 3 times. range(a) gives zero passes when a is 0, one when it is 1
#   and two when it is 2. Zero plus one plus two is three.
# The third: 6 times. The break cuts the inner loop at b == 2, so every outer
#   pass prints b = 0 and b = 1, and there are three outer passes.

n = 0
for a in range(3):
    for b in range(4):
        n += 1
print("First:", n)

n = 0
for a in range(3):
    for b in range(a):
        n += 1
print("Second:", n)

n = 0
for a in range(3):
    for b in range(4):
        if b == 2:
            break
        n += 1
print("Third:", n)
```

The second is the "each against the earlier ones" pattern, and it shows up when you compare every
pair in a list without repeating. The third teaches that a `break` in the inner loop **only leaves
the inner one**, not both.

### Exercise 8

There is no published solution, because the categories differ for everyone. It is graded on four
things: that the two loops' variables have names saying what they walk, that the accumulator and
counter are declared outside both loops, that the hand count of rows matches the output, and that
the report has a header.
"""),

]

write(OUT / "en" / "w09.ipynb", en)
print("wrote", OUT / "en" / "w09.ipynb")
