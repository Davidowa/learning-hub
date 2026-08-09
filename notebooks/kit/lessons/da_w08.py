"""notebooks/analisis-de-datos/{es,en}/w08.ipynb

Source deck: ppts/python/analisis-de-datos/{es,en}/w08.*.yaml

The deck provokes an infinite loop live, with Ctrl-C at hand. A notebook cannot:
it would hang the kernel and every "run all" after it. The loop is shown with a
bounded guard and the guard is the lesson.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "analisis-de-datos"

es = [

md("""
# Análisis de Datos · Semana 8
## Repetición · Primer parcial

**TIA502 · Facultad de Empresariales · Profesor David Escobar-Castillejos**

Llevas años arrastrando una fórmula hacia abajo en una hoja de cálculo. Eso es un ciclo, y lo
único que faltaba era el nombre.

Al terminar este cuaderno vas a poder:

1. Explicar para qué sirve un ciclo y reconocer el trabajo repetido que ya haces a mano.
2. Recorrer una lista con `for`, elemento por elemento.
3. Usar `range` con sus tres formas.
4. Escribir un `while` que termina, con una condición que cambia dentro del cuerpo.
5. Elegir entre los dos por la pregunta que contestan, no por costumbre.

### Sobre el ciclo infinito

En clase conviene provocar uno en vivo, con Control C a la mano. **En un cuaderno no**: un ciclo
infinito cuelga el kernel y hay que reiniciarlo, perdiendo todas las variables.

Aquí se muestra con un tope de seguridad, y el tope es parte de la lección.

### El primer parcial

| Aspecto | Detalle |
|---|---|
| Contenido | Unidades 1 a 4: algoritmos, paradigmas, tipos, operadores, selección y repetición |
| Peso | 20 % de la calificación final |
| Formato | Se resuelve en la computadora del salón y se sube comprimido a Blackboard |
| Puedes llevar | Tus apuntes, tus tareas, los libros y lo que hayas generado con IA antes |
| No puedes | Teléfono, audífonos, lentes con IA, ni ningún medio de mensajería |
"""),

md("""
---
# Bloque 1 · Por qué existe un ciclo

Porque el trabajo repetido a mano se equivoca, y porque cuatro campañas hoy son cuatrocientas el
año que entra.

En la hoja escribes `=C2/B2` y arrastras hasta la fila 500. Arrastrar es repetir la misma
operación cambiando el número de fila. Un `for` hace eso mismo, y no se detiene en la fila 500
porque se te acabó la paciencia.

| Ciclo | Cuándo se usa | La pregunta que contesta |
|---|---|---|
| `for` | Sabes cuántas veces, o tienes algo que recorrer | ¿Para cada uno de estos? |
| `while` | No sabes cuántas, solo cuándo parar | ¿Mientras se cumpla esto? |

Empecemos por lo que ya sabes hacer sin ciclo, para ver qué se gana.
"""),

code("""
# Cuatro campañas, a mano. Funciona y no escala.
print("Instagram   $", round(38500 / 5074, 2))
print("Meta        $", round(29800 / 3820, 2))
print("Google      $", round(51200 / 6910, 2))
print("TikTok      $", round(9600 / 1240, 2))
"""),

md("""
Cuatro líneas casi idénticas. Cambia dos números y nada más, que es la señal inequívoca de que
ahí va un ciclo.
"""),

md("""
---
# Bloque 2 · El ciclo `for`

Recorre algo, elemento por elemento, y se detiene solo cuando ya no queda ninguno.
"""),

code("""
campanas = ["Instagram", "Meta", "Google", "TikTok"]
clics = [5074, 3820, 6910, 1240]
inversion = [38500, 29800, 51200, 9600]

for i in range(len(campanas)):
    cpc = inversion[i] / clics[i]
    print(f"{campanas[i]:<12} ${cpc:>6.2f}")
"""),

md("""
Cuatro cosas de esas cuatro líneas.

**Las tres listas** son tres columnas. La posición 0 de las tres pertenece a la misma campaña.

**`range(len(campanas))`.** `len` da cuántas hay, `range` genera las posiciones 0, 1, 2 y 3. La
lista puede crecer sin tocar el ciclo.

**La variable `i`** vale 0 en la primera vuelta, 1 en la segunda, y así. Es el número de fila del
ciclo.

**El riesgo**: si una lista tiene un elemento menos que las otras, el ciclo lanza `IndexError` al
llegar al final. Es el mismo problema de las listas desemparejadas de la semana 1.1.

Agrega una campaña y córrelo otra vez sin tocar el ciclo.
"""),

code("""
campanas.append("LinkedIn")
clics.append(640)
inversion.append(7200)

for i in range(len(campanas)):
    cpc = inversion[i] / clics[i]
    print(f"{campanas[i]:<12} ${cpc:>6.2f}")
"""),

md("""
Cinco renglones, y el ciclo es el mismo. Ese es el punto entero.

## Recorrer sin índice

Cuando solo necesitas los valores de una lista, no hace falta el índice.
"""),

code("""
for canal in campanas:
    print(canal)
"""),

md("""
Se lee mejor y no puede equivocarse de posición. Úsalo siempre que puedas.

Cuando necesitas el valor **y** su posición, existe `enumerate`.
"""),

code("""
for posicion, canal in enumerate(campanas):
    print(f"{posicion}  {canal}")
"""),

md("""
Y cuando necesitas recorrer dos listas emparejadas, existe `zip`, que ya usaste en la semana 5.
"""),

code("""
for canal, c, inv in zip(campanas, clics, inversion):
    print(f"{canal:<12} {c:>6,} clics   ${inv / c:>6.2f}")
"""),

md("""
`zip` es más seguro que `range(len(...))` por una razón concreta: **si las listas tienen distinto
largo, se detiene en la más corta** en lugar de lanzar `IndexError`.

Eso puede ser bueno o malo, y conviene saber cuál te toca.
"""),

code("""
cortas = ["Instagram", "Meta"]
largas = [5074, 3820, 6910, 1240, 640]

print("Con zip, se detiene en la más corta:")
for canal, c in zip(cortas, largas):
    print(" ", canal, c)

print()
print("Con range(len(largas)), truena:")
try:
    for i in range(len(largas)):
        print(" ", cortas[i], largas[i])
except IndexError as e:
    print("  IndexError:", e)
"""),

md("""
`zip` calla y procesa dos; `range` truena en el tercero. Ninguno de los dos es "el correcto": si
un desemparejamiento es un error de datos, quieres que truene.

## Las tres formas de `range`

| Forma | Qué genera | Ejemplo | Produce |
|---|---|---|---|
| `range(n)` | De 0 hasta n, sin incluir n | `range(4)` | `0, 1, 2, 3` |
| `range(a, b)` | De a hasta b, sin incluir b | `range(1, 5)` | `1, 2, 3, 4` |
| `range(a, b, p)` | De a hasta b, de p en p | `range(0, 10, 3)` | `0, 3, 6, 9` |
"""),

code("""
print("range(4)        ->", list(range(4)))
print("range(1, 5)     ->", list(range(1, 5)))
print("range(0, 10, 3) ->", list(range(0, 10, 3)))
print("range(10, 0, -2)->", list(range(10, 0, -2)), "<- también va hacia atrás")
"""),

md("""
El `list(...)` de esas líneas es solo para verlo. `range` por su cuenta no construye la lista
completa, va generando los números conforme se necesitan, y por eso `range(1000000)` no ocupa
memoria.

**Predice antes de correr.** ¿Cuántas veces se imprime algo?

- **A.** Ocho veces, de 2 a 9.
- **B.** Tres veces: 2, 5 y 8.
- **C.** Cuatro veces: 2, 5, 8 y 11.
- **D.** Diez veces, de 0 a 9.
"""),

code("""
for i in range(2, 10, 3):
    print(i)
"""),

md("""
La respuesta es **B**. Empieza en 2, avanza de tres en tres, y se detiene **antes** del 10. El 11
nunca aparece porque ya pasó el límite.

Que el final no se incluya es la fuente del error de "por uno" más común del semestre. La regla:
`range(a, b)` produce exactamente `b - a` números.
"""),

code("""
print("range(0, 4) produce", len(list(range(0, 4))), "números")
print("range(1, 5) produce", len(list(range(1, 5))), "números")
print("Y el último de range(1, 5) es", list(range(1, 5))[-1], "no 5")
"""),

md("""
---
# Bloque 3 · El ciclo `while`

Repite mientras la condición sea verdadera. Si nada la cambia dentro del cuerpo, repite para
siempre.
"""),

code("""
presupuesto = 100000
gasto_diario = 12500
dia = 0

while presupuesto > 0:
    presupuesto -= gasto_diario
    dia += 1

print(f"El presupuesto aguanta {dia} días.")
"""),

md("""
**La condición** se revisa antes de cada vuelta. Si es falsa desde el principio, el cuerpo no corre
ni una vez.

**Lo que cambia** es la resta de la primera línea del cuerpo. Sin ella la condición sería verdadera
para siempre.

**El contador** empieza en cero y sube uno por vuelta. Es cómo se cuenta cuántas veces se repitió
algo.

Las últimas vueltas:

| Vuelta | Al entrar | ¿> 0? | Al salir | `dia` |
|---|---|---|---|---|
| 6 | 37500 | Sí | 25000 | 6 |
| 7 | 25000 | Sí | 12500 | 7 |
| 8 | 12500 | Sí | 0 | 8 |
| – | 0 | No | 0 | 8 |

La novena nunca empieza. El presupuesto alcanza para ocho días exactos.

Míralo vuelta por vuelta.
"""),

code("""
presupuesto = 100000
gasto_diario = 12500
dia = 0

while presupuesto > 0:
    antes = presupuesto
    presupuesto -= gasto_diario
    dia += 1
    print(f"Día {dia}: entra con {antes:>7,}, sale con {presupuesto:>7,}")

print(f"\\nSe detuvo porque {presupuesto} > 0 es {presupuesto > 0}")
"""),

md("""
## El ciclo infinito

Quita la resta y la condición nunca cambia. En un archivo `.py` eso se detiene con Control C; en
un cuaderno hay que interrumpir el kernel y se pierden las variables.

Así que aquí va con un tope, y el tope es la lección.
"""),

code("""
# CICLO INFINITO A PROPÓSITO, con tope de seguridad. Sin el tope, esta celda
# nunca terminaría y habría que reiniciar el kernel.
presupuesto = 100000
vueltas = 0
TOPE = 1000

while presupuesto > 0:
    vueltas += 1
    # falta la resta: presupuesto nunca baja
    if vueltas >= TOPE:
        print(f"Detenido por el tope después de {vueltas:,} vueltas.")
        print(f"El presupuesto sigue en {presupuesto:,} y la condición sigue siendo verdadera.")
        break
"""),

md("""
Mil vueltas y el presupuesto intacto. Sin el `break` habrían sido mil millones y seguiría igual.

Ese `if` con contador es una técnica real, no solo didáctica: cuando escribas un `while` cuya
condición depende de algo que no controlas del todo, un tope de seguridad convierte un programa
colgado en un programa que se queja.

**La revisión de todo `while`**: señala con el dedo la línea del cuerpo que cambia la condición. Si
no la encuentras, el ciclo no termina.

## Cuándo `while` y cuándo `for`

`for` cuando sabes cuántas veces o tienes algo que recorrer. `while` cuando solo sabes cuándo
parar.

Este es un caso donde `for` no sirve: no sabes de antemano cuántos días aguanta el presupuesto,
eso es justamente lo que quieres averiguar.
"""),

code("""
def dias_que_aguanta(presupuesto, gasto_diario):
    \"\"\"Cuántos días completos cubre el presupuesto.\"\"\"
    dias = 0
    while presupuesto > 0:
        presupuesto -= gasto_diario
        dias += 1
    return dias


for gasto in [12500, 8000, 33400, 100000]:
    print(f"Gastando {gasto:>7,} al día, aguanta {dias_que_aguanta(100000, gasto):>3} días")
"""),

md("""
Y este es un caso donde `while` sería un rodeo: sabes exactamente cuántas campañas hay.
"""),

code("""
# Con for, natural.
for canal in campanas:
    print(canal, end="  ")
print()

# Con while, el mismo resultado y tres líneas de contabilidad de más.
i = 0
while i < len(campanas):
    print(campanas[i], end="  ")
    i += 1
print()
"""),

md("""
La versión con `while` funciona y tiene tres formas de equivocarse que la de `for` no tiene:
olvidar el `i = 0`, olvidar el `i += 1`, o escribir `<=` en lugar de `<`.

Elegir por la pregunta que contestan, no por costumbre.

## Cuatro errores de ciclos

**El ciclo infinito.** Nada dentro del cuerpo cambia la condición. Ya lo viste.

**Errar por uno.** `range(4)` da cuatro vueltas, de 0 a 3. El 4 nunca aparece, y eso es lo correcto.

**Definir el acumulador dentro.** Si `total = 0` está dentro del ciclo, se reinicia en cada vuelta y
al final vale solo la última.
"""),

code("""
# FALLA A PROPÓSITO. El acumulador se reinicia en cada vuelta.
for c in clics:
    total_mal = 0
    total_mal += c
print("Acumulador dentro:", total_mal, "<- solo el último")

total_bien = 0
for c in clics:
    total_bien += c
print("Acumulador fuera: ", total_bien, "<- la suma real")
"""),

md("""
El primero no lanza error y devuelve un número. Es 640, el último de la lista, y se parece lo
bastante a un total como para pasar desapercibido.

**Recorrer listas de distinto largo.** Ya lo viste con `zip` y `range`.
"""),

md("""
---
# Ejercicios

Las soluciones están hasta abajo del cuaderno.

## for

### Ejercicio 1 · Las tres formas de recorrer

Con la lista `campanas`, escribe tres ciclos que impriman lo mismo: uno con
`range(len(...))`, uno recorriendo la lista directo, y uno con `enumerate`.

Di en un comentario cuál usarías y por qué.

### Ejercicio 2 · Las tres formas de `range`

Escribe un ciclo con cada forma de `range` que imprima: los números del 0 al 5, los meses del 1 al
12, y los años pares de 2020 a 2030.

### Ejercicio 3 · Tu propia tabla

Toma seis registros de tu área en tres listas paralelas y recórrelos con un `for`, calculando una
métrica por renglón e imprimiéndola alineada con encabezado.

Después agrega un séptimo registro. Si tuviste que tocar el ciclo, el ciclo estaba mal escrito.

## while

### Ejercicio 4 · El presupuesto que sí sobra

Modifica `dias_que_aguanta` para que devuelva también cuánto dinero sobra el último día, en lugar
de dejar el presupuesto en negativo.

Pruébala con 100 000 y gasto de 12 500, y con 100 000 y gasto de 33 400.

### Ejercicio 5 · El tope de seguridad

Escribe un `while` que busque el primer número mayor a 1 000 que sea divisible entre 7 y entre 11
al mismo tiempo. Ponle un tope de seguridad de 100 000 vueltas.

Después quita el tope y comprueba que igual termina, porque la condición sí cambia.

### Ejercicio 6 · Contar con `while`

Escribe un `while` que cuente cuántas campañas superan un umbral de costo por clic, recorriendo
las listas con un índice. Después escribe lo mismo con `for` y compara cuál se lee mejor.

## Los dos

### Ejercicio 7 · Elegir el ciclo

Para cada situación, di en un comentario cuál ciclo usarías y por qué:

1. Calcular el IVA de cada renglón de una factura.
2. Pedir una contraseña hasta que sea correcta.
3. Sumar las ventas de los doce meses del año.
4. Ir descontando de un inventario hasta que se agote.
5. Revisar los 324 renglones de `sales.csv`.

### Ejercicio 8 · El reporte de la tarea

Recorre las cinco campañas del cuaderno y reporta cuál tiene el mejor costo por clic, cuál el
peor, y el costo por clic global de las cinco juntas.

Ojo con el global: **no** es el promedio de los cinco costos por clic. Es la inversión total entre
los clics totales, y la diferencia importa.
"""),

md("""
---
## Tres ideas para llevarse

**Un `for` es arrastrar la fórmula.** La misma operación aplicada a cada fila, y sin detenerse
donde se acabó tu paciencia.

**`for` cuando sabes cuántas, `while` cuando solo sabes cuándo parar.** Elegir por la pregunta, no
por costumbre.

**Algo dentro tiene que cambiar.** Si el cuerpo del `while` no toca la condición, el ciclo no
termina nunca. Señala con el dedo la línea que la cambia antes de correrlo.

La siguiente sesión son acumuladores, banderas y ciclos que viven dentro de otros ciclos.
"""),

md("""
---
# Soluciones

### Ejercicio 1

```python
print("Con range(len(...)):")
for i in range(len(campanas)):
    print(" ", campanas[i])

print("Recorriendo directo:")
for canal in campanas:
    print(" ", canal)

print("Con enumerate:")
for i, canal in enumerate(campanas):
    print(f"  {i}  {canal}")

# Uso el segundo cuando solo necesito el valor, que es casi siempre. El tercero
# cuando además necesito la posición. El primero casi nunca: es el único de los
# tres que puede salirse del rango, y no aporta nada que los otros dos no den.
```

`range(len(...))` sigue haciendo falta cuando recorres varias listas por índice y no quieres el
comportamiento de `zip`, que es callar cuando difieren en largo.

### Ejercicio 2

```python
for n in range(6):
    print(n, end=" ")
print()

for mes in range(1, 13):
    print(mes, end=" ")
print()

for anio in range(2020, 2031, 2):
    print(anio, end=" ")
print()
```

El de los meses es el que más se equivoca: `range(1, 13)` y no `range(1, 12)`, porque el final no
se incluye. Doce meses necesitan que el límite sea trece.

### Ejercicio 3

```python
productos = ["Espresso", "Molino", "Hervidor", "Suscripción", "Termo", "Prensa"]
piezas = [42, 18, 65, 130, 210, 27]
precios = [8990.0, 2450.0, 1290.0, 690.0, 349.0, 1890.0]

print(f"{'Producto':<14}{'Piezas':>8}{'Precio':>11}{'Ingreso':>13}")
print("-" * 46)
for i in range(len(productos)):
    ingreso = piezas[i] * precios[i]
    print(f"{productos[i]:<14}{piezas[i]:>8,}{precios[i]:>11,.2f}{ingreso:>13,.2f}")

productos.append("Filtros")
piezas.append(480)
precios.append(120.0)
# volver a correr el ciclo: sale el séptimo renglón sin tocar nada
```

Que el séptimo aparezca sin editar el ciclo es la prueba. Si hubieras escrito `range(6)` en vez de
`range(len(productos))`, habrías tenido que cambiar el número.

### Ejercicio 4

```python
def dias_y_sobrante(presupuesto, gasto_diario):
    dias = 0
    while presupuesto >= gasto_diario:
        presupuesto -= gasto_diario
        dias += 1
    return dias, presupuesto


for gasto in [12500, 33400]:
    dias, sobra = dias_y_sobrante(100000, gasto)
    print(f"Gasto {gasto:>7,}: {dias} días completos, sobran {sobra:,.2f}")
```

El cambio está en la condición: `>= gasto_diario` en vez de `> 0`. Con la original, el último día
se cobraba aunque el dinero no alcanzara, y el presupuesto acababa en negativo.

Con 12 500 salen 8 días y sobra 0; con 33 400 salen 2 días y sobran 33 200.

### Ejercicio 5

```python
n = 1000
vueltas = 0
TOPE = 100000

while True:
    n += 1
    vueltas += 1
    if n % 7 == 0 and n % 11 == 0:
        print(f"Encontrado: {n} después de {vueltas} vueltas")
        break
    if vueltas >= TOPE:
        print("Detenido por el tope")
        break
```

Sale 1001, en una sola vuelta, porque 7 por 11 por 13 es 1001. El tope nunca se activa.

Vale la pena dejarlo puesto de todos modos: el día que la condición sea imposible, el tope es la
diferencia entre un programa que se queja y uno que se cuelga.

### Ejercicio 6

```python
UMBRAL = 7.60

i = 0
cuantas = 0
while i < len(campanas):
    if inversion[i] / clics[i] > UMBRAL:
        cuantas += 1
    i += 1
print("Con while:", cuantas)

cuantas = 0
for inv, c in zip(inversion, clics):
    if inv / c > UMBRAL:
        cuantas += 1
print("Con for:  ", cuantas)
```

Dos campañas pasan el umbral. La versión con `for` tiene tres líneas menos y ninguna de ellas era
sobre el problema: eran sobre llevar la cuenta del índice.

### Ejercicio 7

```python
# 1. for. Sabes cuántos renglones tiene la factura y los tienes todos.
# 2. while. No sabes cuántos intentos va a necesitar la persona.
# 3. for. Son doce, siempre doce.
# 4. while. Depende de cuánto haya en inventario y de cuánto pida cada quien.
# 5. for. Son 324 y están todos en el archivo desde antes de empezar.
```

La regla de bolsillo: si puedes contar las vueltas antes de empezar, es `for`. Si solo puedes
describir cuándo parar, es `while`.

### Ejercicio 8

```python
mejor_i = 0
peor_i = 0

for i in range(len(campanas)):
    cpc = inversion[i] / clics[i]
    if cpc < inversion[mejor_i] / clics[mejor_i]:
        mejor_i = i
    if cpc > inversion[peor_i] / clics[peor_i]:
        peor_i = i

print(f"Mejor: {campanas[mejor_i]:<12} ${inversion[mejor_i] / clics[mejor_i]:.2f}")
print(f"Peor:  {campanas[peor_i]:<12} ${inversion[peor_i] / clics[peor_i]:.2f}")

global_cpc = sum(inversion) / sum(clics)
promedio_cpc = sum(inversion[i] / clics[i] for i in range(len(campanas))) / len(campanas)

print(f"\\nCosto por clic global:   ${global_cpc:.4f}")
print(f"Promedio de los cinco:   ${promedio_cpc:.4f}")
print("No son el mismo número.")
```

El global es la inversión total entre los clics totales. El promedio de los cinco pesa igual a
LinkedIn, con 640 clics, que a Google con 6 910, y por eso se separa del global.

Es el mismo error de promediar porcentajes de bases distintas que aparece en la semana 5, y va a
volver en la 15.3 cuando agrupes.
"""),

]

write(OUT / "es" / "w08.ipynb", es)
print("wrote", OUT / "es" / "w08.ipynb")


en = [

md("""
# Data Analysis · Week 8
## Repetition · First midterm

**TIA502 · School of Business · Instructor David Escobar-Castillejos**

You have spent years dragging a formula down a spreadsheet. That is a loop, and the only thing
missing was the name.

By the end of this notebook you will be able to:

1. Explain what a loop is for and recognise the repeated work you already do by hand.
2. Walk a list with `for`, element by element.
3. Use `range` in all three of its forms.
4. Write a `while` that terminates, with a condition that changes inside the body.
5. Choose between the two by the question they answer, not by habit.

### About the infinite loop

In class it is worth provoking one live, with Ctrl-C at hand. **Not in a notebook**: an infinite
loop hangs the kernel and it has to be restarted, losing every variable.

Here it is shown with a safety cap, and the cap is part of the lesson.

### The first midterm

| Aspect | Detail |
|---|---|
| Content | Units 1 to 4: algorithms, paradigms, types, operators, selection and repetition |
| Weight | 20 % of the final grade |
| Format | Solved on the classroom computer and uploaded zipped to Blackboard |
| You may bring | Your notes, your assignments, the books and anything you generated with AI beforehand |
| You may not | Phone, headphones, AI glasses, or any messaging channel |
"""),

md("""
---
# Block 1 · Why a loop exists

Because repeated work done by hand gets things wrong, and because four campaigns today are four
hundred next year.

In the sheet you write `=C2/B2` and drag it down to row 500. Dragging is repeating the same
operation with a different row number. A `for` does exactly that, and it does not stop at row 500
because you ran out of patience.

| Loop | When it is used | The question it answers |
|---|---|---|
| `for` | You know how many times, or you have something to walk | For each of these? |
| `while` | You do not know how many, only when to stop | While this holds? |

Start with what you already know how to do without a loop, to see what is gained.
"""),

code("""
# Four campaigns, by hand. It works and it does not scale.
print("Instagram   $", round(38500 / 5074, 2))
print("Meta        $", round(29800 / 3820, 2))
print("Google      $", round(51200 / 6910, 2))
print("TikTok      $", round(9600 / 1240, 2))
"""),

md("""
Four nearly identical lines. Two numbers change and nothing else, which is the unmistakable sign
that a loop belongs there.
"""),

md("""
---
# Block 2 · The `for` loop

It walks something, element by element, and stops on its own when none are left.
"""),

code("""
campaigns = ["Instagram", "Meta", "Google", "TikTok"]
clicks = [5074, 3820, 6910, 1240]
spend = [38500, 29800, 51200, 9600]

for i in range(len(campaigns)):
    cpc = spend[i] / clicks[i]
    print(f"{campaigns[i]:<12} ${cpc:>6.2f}")
"""),

md("""
Four things about those four lines.

**The three lists** are three columns. Position 0 of all three belongs to the same campaign.

**`range(len(campaigns))`.** `len` gives how many there are, `range` generates the positions 0, 1,
2 and 3. The list can grow without touching the loop.

**The variable `i`** is 0 on the first pass, 1 on the second, and so on. It is the loop's row
number.

**The risk**: if one list has one element fewer than the others, the loop raises `IndexError` on
reaching the end. It is the same problem as the unpaired lists in week 1.1.

Add a campaign and run it again without touching the loop.
"""),

code("""
campaigns.append("LinkedIn")
clicks.append(640)
spend.append(7200)

for i in range(len(campaigns)):
    cpc = spend[i] / clicks[i]
    print(f"{campaigns[i]:<12} ${cpc:>6.2f}")
"""),

md("""
Five rows, and the loop is the same. That is the whole point.

## Walking without an index

When you only need the values of a list, the index is unnecessary.
"""),

code("""
for channel in campaigns:
    print(channel)
"""),

md("""
It reads better and cannot get the position wrong. Use it whenever you can.

When you need the value **and** its position, there is `enumerate`.
"""),

code("""
for position, channel in enumerate(campaigns):
    print(f"{position}  {channel}")
"""),

md("""
And when you need to walk two paired lists, there is `zip`, which you already used in week 5.
"""),

code("""
for channel, c, s in zip(campaigns, clicks, spend):
    print(f"{channel:<12} {c:>6,} clicks   ${s / c:>6.2f}")
"""),

md("""
`zip` is safer than `range(len(...))` for one concrete reason: **if the lists differ in length, it
stops at the shortest** rather than raising `IndexError`.

That can be good or bad, and it is worth knowing which you are getting.
"""),

code("""
short = ["Instagram", "Meta"]
long = [5074, 3820, 6910, 1240, 640]

print("With zip, it stops at the shortest:")
for channel, c in zip(short, long):
    print(" ", channel, c)

print()
print("With range(len(long)), it blows up:")
try:
    for i in range(len(long)):
        print(" ", short[i], long[i])
except IndexError as e:
    print("  IndexError:", e)
"""),

md("""
`zip` says nothing and processes two; `range` blows up on the third. Neither is "the right one": if
a mismatch is a data error, you want it to blow up.

## The three forms of `range`

| Form | What it generates | Example | Produces |
|---|---|---|---|
| `range(n)` | From 0 up to n, not including n | `range(4)` | `0, 1, 2, 3` |
| `range(a, b)` | From a up to b, not including b | `range(1, 5)` | `1, 2, 3, 4` |
| `range(a, b, s)` | From a up to b, in steps of s | `range(0, 10, 3)` | `0, 3, 6, 9` |
"""),

code("""
print("range(4)         ->", list(range(4)))
print("range(1, 5)      ->", list(range(1, 5)))
print("range(0, 10, 3)  ->", list(range(0, 10, 3)))
print("range(10, 0, -2) ->", list(range(10, 0, -2)), "<- it also runs backwards")
"""),

md("""
The `list(...)` in those lines is only so you can see it. `range` on its own does not build the
whole list, it generates the numbers as they are needed, which is why `range(1000000)` takes no
memory.

**Predict before you run.** How many times does something print?

- **A.** Eight times, from 2 to 9.
- **B.** Three times: 2, 5 and 8.
- **C.** Four times: 2, 5, 8 and 11.
- **D.** Ten times, from 0 to 9.
"""),

code("""
for i in range(2, 10, 3):
    print(i)
"""),

md("""
The answer is **B**. It starts at 2, steps by three, and stops **before** 10. The 11 never appears
because it is already past the limit.

That the end is excluded is the source of the commonest off-by-one error of the term. The rule:
`range(a, b)` produces exactly `b - a` numbers.
"""),

code("""
print("range(0, 4) produces", len(list(range(0, 4))), "numbers")
print("range(1, 5) produces", len(list(range(1, 5))), "numbers")
print("And the last of range(1, 5) is", list(range(1, 5))[-1], "not 5")
"""),

md("""
---
# Block 3 · The `while` loop

It repeats while the condition is true. If nothing changes it inside the body, it repeats forever.
"""),

code("""
budget = 100000
daily_spend = 12500
day = 0

while budget > 0:
    budget -= daily_spend
    day += 1

print(f"The budget lasts {day} days.")
"""),

md("""
**The condition** is checked before each pass. If it is false from the start, the body does not run
even once.

**What changes** is the subtraction on the first line of the body. Without it the condition would be
true forever.

**The counter** starts at zero and goes up by one per pass. That is how you count how many times
something repeated.

The last passes:

| Pass | On entry | `> 0`? | On exit | `day` |
|---|---|---|---|---|
| 6 | 37500 | Yes | 25000 | 6 |
| 7 | 25000 | Yes | 12500 | 7 |
| 8 | 12500 | Yes | 0 | 8 |
| – | 0 | No | 0 | 8 |

The ninth never starts. The budget covers exactly eight days.

Watch it pass by pass.
"""),

code("""
budget = 100000
daily_spend = 12500
day = 0

while budget > 0:
    before = budget
    budget -= daily_spend
    day += 1
    print(f"Day {day}: enters with {before:>7,}, leaves with {budget:>7,}")

print(f"\\nIt stopped because {budget} > 0 is {budget > 0}")
"""),

md("""
## The infinite loop

Remove the subtraction and the condition never changes. In a `.py` file that is stopped with
Ctrl-C; in a notebook the kernel has to be interrupted and the variables are lost.

So here it comes with a cap, and the cap is the lesson.
"""),

code("""
# INFINITE LOOP ON PURPOSE, with a safety cap. Without the cap this cell would
# never finish and the kernel would have to be restarted.
budget = 100000
passes = 0
CAP = 1000

while budget > 0:
    passes += 1
    # the subtraction is missing: budget never goes down
    if passes >= CAP:
        print(f"Stopped by the cap after {passes:,} passes.")
        print(f"The budget is still {budget:,} and the condition is still true.")
        break
"""),

md("""
A thousand passes and the budget untouched. Without the `break` it would have been a billion and it
would still be the same.

That `if` with a counter is a real technique, not just a teaching one: when you write a `while`
whose condition depends on something you do not fully control, a safety cap turns a hung program
into one that complains.

**The review for every `while`**: point at the line in the body that changes the condition. If you
cannot find it, the loop does not end.

## When `while` and when `for`

`for` when you know how many times or have something to walk. `while` when you only know when to
stop.

This is a case where `for` is no use: you do not know in advance how many days the budget lasts,
which is exactly what you want to find out.
"""),

code("""
def days_it_lasts(budget, daily_spend):
    \"\"\"How many complete days the budget covers.\"\"\"
    days = 0
    while budget > 0:
        budget -= daily_spend
        days += 1
    return days


for spend_per_day in [12500, 8000, 33400, 100000]:
    print(f"Spending {spend_per_day:>7,} a day, it lasts {days_it_lasts(100000, spend_per_day):>3} days")
"""),

md("""
And this is a case where `while` would be a detour: you know exactly how many campaigns there are.
"""),

code("""
# With for, natural.
for channel in campaigns:
    print(channel, end="  ")
print()

# With while, the same result and three extra lines of bookkeeping.
i = 0
while i < len(campaigns):
    print(campaigns[i], end="  ")
    i += 1
print()
"""),

md("""
The `while` version works and has three ways to go wrong that the `for` version does not: forgetting
`i = 0`, forgetting `i += 1`, or writing `<=` instead of `<`.

Choose by the question they answer, not by habit.

## Four loop errors

**The infinite loop.** Nothing in the body changes the condition. You saw it.

**Off by one.** `range(4)` gives four passes, from 0 to 3. The 4 never appears, and that is correct.

**Defining the accumulator inside.** If `total = 0` sits inside the loop, it resets every pass and
at the end it holds only the last one.
"""),

code("""
# FAILS ON PURPOSE. The accumulator resets on every pass.
for c in clicks:
    wrong_total = 0
    wrong_total += c
print("Accumulator inside:", wrong_total, "<- only the last one")

right_total = 0
for c in clicks:
    right_total += c
print("Accumulator outside:", right_total, "<- the real sum")
"""),

md("""
The first raises nothing and returns a number. It is 640, the last of the list, and it looks enough
like a total to go unnoticed.

**Walking lists of different lengths.** You saw it with `zip` and `range`.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

## for

### Exercise 1 · The three ways of walking

With the `campaigns` list, write three loops printing the same thing: one with `range(len(...))`,
one walking the list directly, and one with `enumerate`.

Say in a comment which you would use and why.

### Exercise 2 · The three forms of `range`

Write a loop with each form of `range` printing: the numbers 0 to 5, the months 1 to 12, and the
even years from 2020 to 2030.

### Exercise 3 · Your own table

Take six records from your field in three parallel lists and walk them with a `for`, computing a
metric per row and printing it aligned with a header.

Then add a seventh record. If you had to touch the loop, the loop was badly written.

## while

### Exercise 4 · The budget that has something left

Modify `days_it_lasts` so it also returns how much money is left on the last day, instead of
leaving the budget negative.

Test it with 100,000 and a spend of 12,500, and with 100,000 and a spend of 33,400.

### Exercise 5 · The safety cap

Write a `while` that looks for the first number above 1,000 divisible by both 7 and 11. Give it a
safety cap of 100,000 passes.

Then remove the cap and check it still terminates, because the condition genuinely changes.

### Exercise 6 · Counting with `while`

Write a `while` that counts how many campaigns exceed a cost-per-click threshold, walking the lists
with an index. Then write the same with `for` and compare which reads better.

## Both

### Exercise 7 · Choosing the loop

For each situation, say in a comment which loop you would use and why:

1. Computing the tax on each line of an invoice.
2. Asking for a password until it is correct.
3. Summing the sales of the twelve months of the year.
4. Drawing down an inventory until it runs out.
5. Checking the 324 rows of `sales.csv`.

### Exercise 8 · The homework report

Walk the five campaigns in the notebook and report which has the best cost per click, which the
worst, and the overall cost per click of all five together.

Careful with the overall one: it is **not** the average of the five costs per click. It is total
spend over total clicks, and the difference matters.
"""),

md("""
---
## Three ideas to take away

**A `for` is dragging the formula.** The same operation applied to every row, and it does not stop
where your patience ran out.

**`for` when you know how many, `while` when you only know when to stop.** Choose by the question,
not by habit.

**Something inside has to change.** If the body of the `while` does not touch the condition, the
loop never ends. Point at the line that changes it before running.

Next session is accumulators, flags and loops that live inside other loops.
"""),

md("""
---
# Solutions

### Exercise 1

```python
print("With range(len(...)):")
for i in range(len(campaigns)):
    print(" ", campaigns[i])

print("Walking directly:")
for channel in campaigns:
    print(" ", channel)

print("With enumerate:")
for i, channel in enumerate(campaigns):
    print(f"  {i}  {channel}")

# I use the second when I only need the value, which is nearly always. The third
# when I also need the position. The first almost never: it is the only one of the
# three that can run off the end, and it adds nothing the other two do not give.
```

`range(len(...))` is still needed when you walk several lists by index and do not want `zip`'s
behaviour, which is to say nothing when they differ in length.

### Exercise 2

```python
for n in range(6):
    print(n, end=" ")
print()

for month in range(1, 13):
    print(month, end=" ")
print()

for year in range(2020, 2031, 2):
    print(year, end=" ")
print()
```

The months one is the most commonly got wrong: `range(1, 13)` and not `range(1, 12)`, because the
end is excluded. Twelve months need the limit to be thirteen.

### Exercise 3

```python
products = ["Espresso", "Grinder", "Kettle", "Subscription", "Mug", "Press"]
pieces = [42, 18, 65, 130, 210, 27]
prices = [8990.0, 2450.0, 1290.0, 690.0, 349.0, 1890.0]

print(f"{'Product':<14}{'Pieces':>8}{'Price':>11}{'Revenue':>13}")
print("-" * 46)
for i in range(len(products)):
    revenue = pieces[i] * prices[i]
    print(f"{products[i]:<14}{pieces[i]:>8,}{prices[i]:>11,.2f}{revenue:>13,.2f}")

products.append("Filters")
pieces.append(480)
prices.append(120.0)
# rerun the loop: the seventh row appears without touching anything
```

That the seventh appears without editing the loop is the test. Had you written `range(6)` instead of
`range(len(products))`, you would have had to change the number.

### Exercise 4

```python
def days_and_remainder(budget, daily_spend):
    days = 0
    while budget >= daily_spend:
        budget -= daily_spend
        days += 1
    return days, budget


for spend_per_day in [12500, 33400]:
    days, left = days_and_remainder(100000, spend_per_day)
    print(f"Spend {spend_per_day:>7,}: {days} full days, {left:,.2f} left over")
```

The change is in the condition: `>= daily_spend` rather than `> 0`. With the original, the last day
got charged even when the money did not cover it, and the budget ended negative.

At 12,500 that gives 8 days and 0 left; at 33,400 it gives 2 days and 33,200 left.

### Exercise 5

```python
n = 1000
passes = 0
CAP = 100000

while True:
    n += 1
    passes += 1
    if n % 7 == 0 and n % 11 == 0:
        print(f"Found: {n} after {passes} passes")
        break
    if passes >= CAP:
        print("Stopped by the cap")
        break
```

It comes out at 1001, on a single pass, because 7 times 11 times 13 is 1001. The cap never fires.

It is worth leaving in all the same: the day the condition is impossible, the cap is the difference
between a program that complains and one that hangs.

### Exercise 6

```python
THRESHOLD = 7.60

i = 0
how_many = 0
while i < len(campaigns):
    if spend[i] / clicks[i] > THRESHOLD:
        how_many += 1
    i += 1
print("With while:", how_many)

how_many = 0
for s, c in zip(spend, clicks):
    if s / c > THRESHOLD:
        how_many += 1
print("With for:  ", how_many)
```

Two campaigns clear the threshold. The `for` version has three fewer lines and none of them was
about the problem: they were about keeping track of the index.

### Exercise 7

```python
# 1. for. You know how many lines the invoice has and you have them all.
# 2. while. You do not know how many attempts the person will need.
# 3. for. There are twelve, always twelve.
# 4. while. It depends on how much stock there is and how much each order takes.
# 5. for. There are 324 and they are all in the file before you start.
```

The pocket rule: if you can count the passes before starting, it is `for`. If you can only describe
when to stop, it is `while`.

### Exercise 8

```python
best_i = 0
worst_i = 0

for i in range(len(campaigns)):
    cpc = spend[i] / clicks[i]
    if cpc < spend[best_i] / clicks[best_i]:
        best_i = i
    if cpc > spend[worst_i] / clicks[worst_i]:
        worst_i = i

print(f"Best:  {campaigns[best_i]:<12} ${spend[best_i] / clicks[best_i]:.2f}")
print(f"Worst: {campaigns[worst_i]:<12} ${spend[worst_i] / clicks[worst_i]:.2f}")

overall_cpc = sum(spend) / sum(clicks)
average_cpc = sum(spend[i] / clicks[i] for i in range(len(campaigns))) / len(campaigns)

print(f"\\nOverall cost per click: ${overall_cpc:.4f}")
print(f"Average of the five:    ${average_cpc:.4f}")
print("They are not the same number.")
```

The overall figure is total spend over total clicks. The average of the five gives LinkedIn, with
640 clicks, the same weight as Google with 6,910, which is why it drifts from the overall.

It is the same error of averaging percentages with different bases that turns up in week 5, and it
comes back in 15.3 when you start grouping.
"""),

]

write(OUT / "en" / "w08.ipynb", en)
print("wrote", OUT / "en" / "w08.ipynb")
