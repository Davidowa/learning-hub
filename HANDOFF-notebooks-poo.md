# Sesión A · Cuadernos de Colab para COM102 (POO)

Corre en paralelo con la sesión B, que trabaja los cuadernos de Análisis de
Datos. Las dos tocan `notebooks/kit/`. Lee la sección de convivencia antes de
editar nada del kit.

## Encargo

Terminar los cuadernos de COM102. Van tres semanas de diecisiete, en los dos
idiomas, así que faltan **catorce semanas por dos idiomas**.

Empieza por `w01.4` y sigue en orden hasta `w17`.

## Estado al arrancar

```
notebooks/kit/lessons/   poo_w01_1.py, poo_w01_2.py, poo_w01_3.py  (+ _en)
notebooks/programacion-orientada-a-objetos/{es,en}/   w01.1, w01.2, w01.3 .ipynb
```

Todo eso ya está commiteado. `w01.3` quedó en 35 celdas por idioma y cero
errores de ejecución.

## Lo que hay que leer antes de escribir

En este orden, y no te saltes el último:

1. `notebooks/kit/README.md` y `notebooks/kit/HANDOFF-poo.md`
2. Los tres módulos ya escritos, sobre todo `poo_w01_3.py`, que es el modelo
   más maduro
3. El deck de la semana que vas a escribir, en `ppts/python/programacion-orientada-a-objetos/`
4. El código fuente que vas a citar, y **córrelo antes de citarlo**

## Errores conocidos en las fuentes, sin corregir

`Code013.py` tiene tres llamadas a métodos que las tuplas no tienen, y los tres
caen justo en el bloque de tuplas de `w01.4`, que es la semana con la que vas a
empezar:

- línea 31, `this_tuple.extend(...)`
- línea 50, `this_tuple.copy()`
- línea 117, `this_tuple.clear()`

Además, las líneas 46 y 47 afirman que copiar una tupla por asignación propaga
cambios. No hay cambios que propagar: una tupla es inmutable.

`Code010.py` define `print_name` dos veces, en las líneas 82 y 144, con firmas
distintas. El archivo corre porque las llamadas están antes de la segunda
definición.

Ninguno se ha corregido. Decide si el cuaderno los enseña como trampa o los
esquiva, pero no los cites como si funcionaran.

## Lo que hace bueno a un cuaderno aquí

Del `w01.3` que ya está escrito, y que conviene sostener:

**Las celdas que fallan a propósito enseñan más que las que funcionan.** En
`w01.3` hay diez, y siete de ellas no lanzan ninguna excepción: definir sin
llamar, el nombre sin paréntesis, la anotación de tipo mentida, la lista por
omisión que acumula, redefinir una función. El error silencioso es el que vale.

**Los números se miden, no se afirman.** Si la prosa dice una cifra, que salga
de una celda que el lector puede correr. En `w01.3` la celda cuenta las
categorías de FizzBuzz con los dos órdenes y da 6/27/14/53 contra 0/33/14/53, y
la prosa cita eso.

**Cose hilos hacia adelante.** Alcance apunta al `self` de la semana 3; la lista
por omisión apunta al estado compartido de la semana 6.

## Sin notas de orador

Los decks de los cuatro cursos ya no llevan `notes:`. Se quitaron 309 bloques.
Si un cuaderno necesitaba contexto que vivía ahí, ya no está: sácalo del deck
mismo o del HANDOFF del curso.

## Convivencia con la sesión B

Las dos sesiones editan `notebooks/kit/`. Regla: **quien toque `nbkit.py`,
`build.py` o `verify.py` lo dice en su reporte antes de seguir.** Si necesitas
un cambio en el kit, hazlo mínimo y corre la verificación de los dos cursos,
no solo del tuyo, antes de darlo por bueno.

Los `lessons/*.py` y los árboles de salida no se pisan: los tuyos empiezan con
`poo_`, los de la sesión B con `da_`.

## Verificar

```bash
cd notebooks
python -m kit.build          # los cuadernos salen junto a su modulo
python -m kit.verify         # ejecuta cada celda, cuenta errores
```

Cero errores en los dos idiomas antes de dar una semana por terminada.

## Cuidado con esto

`notebooks/kit/lessons/da_w01_1.py` aparece como modificado en `git status` y
**no lo está**. El blob en disco y el del índice son el mismo hash; `git diff`
sale vacío. Es caché de fechas rancio. No lo revierta ni lo commitees "para
limpiarlo".
