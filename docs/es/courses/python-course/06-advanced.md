# 06 · Avanzado

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/rocket.svg" width="32" height="32" alt="">

Funciones que separan "sé escribir Python" de "sé escribir Python **Pythonic**, eficiente y mantenible".

## Lo que aprenderás

- **Decoradores** — funciones que envuelven otras funciones para añadir comportamiento (logging, medición, caché) sin modificarlas. Piénsalo como un papel envolvente que añade características.
- **Generadores** (`yield`) — producen valores uno a uno, de forma perezosa. Amables con la memoria para datasets grandes.
- **Gestores de contexto** (`with` / `__enter__` / `__exit__`) — configuración y limpieza automáticas. Ya los usas con `open()`; ahora aprende a escribir los tuyos.
- **Iteradores e iterables** — lo que realmente hace funcionar los ciclos `for`.
- **Comprehensiones** — sintaxis compacta para construir listas, diccionarios, conjuntos, generadores.
- **Tipado** — anotaciones opcionales (`def add(a: int, b: int) -> int:`) que atrapan bugs temprano y documentan intención.
- **Async / await** — concurrencia de E/S sin hilos. Para llamadas de red, lecturas de disco, interfaces que no se congelan.
- **Pruebas** — `pytest`, fixtures, parametrización.

## Analogía sencilla

Si el Python básico es cocinar un platillo a la vez, el Python avanzado es dirigir la cocina de un restaurante — los decoradores son los sous chefs que emplatan igual cada orden, los generadores son la banda transportadora que sirve platos solo cuando alguien se sienta, y async es juegar malabares con la parrilla, freidora y horno para que ninguno esté ocioso.

## Trabajo con datos

Tres módulos sobre convertir un archivo de registros en una respuesta con la que alguien pueda decidir. Están escritos para quien ya hace este trabajo en una hoja de cálculo, así que cada idea aparece junto a la función de Excel que viene a reemplazar.

| Módulo | Qué cubre |
|---|---|
| `A04 - Tabular Data` | Leer un CSV con la biblioteca estándar y resumirlo a mano con diccionarios. Ochenta líneas que vuelven evidente el módulo siguiente. |
| `A05 - Pandas` | Series y DataFrames, cargar e inspeccionar, seleccionar y filtrar, limpiar, agrupar y agregar, unir y exportar. |
| `A06 - Data Visualization` | La figura y los ejes de matplotlib, qué gráfica responde a qué pregunta, etiquetas y accesibilidad, y las líneas de seaborn. |

La equivalencia que conviene tener presente:

| En la hoja de cálculo | En pandas |
|---|---|
| Una columna | Una `Series` |
| La hoja completa | Un `DataFrame` |
| `SUMA`, `PROMEDIO`, `CONTAR` | `.sum()`, `.mean()`, `.count()` |
| Autofiltro | Una máscara booleana |
| Tabla dinámica | `.groupby()` y `.pivot_table()` |
| `BUSCARV` | `.merge()` |
| Insertar gráfico | matplotlib y seaborn |

### Los datos

`06 - Advanced/data/` contiene tres archivos CSV. La tabla de ventas está sucia a propósito, y cada defecto enseña un paso de limpieza: filas capturadas dos veces, celdas en blanco, una región escrita de cuatro formas distintas y un precio guardado como `$ 2,082.50` en lugar de como número. `make_datasets.py` los reconstruye desde una semilla fija, así que los números nunca se despegan de lo que cita una lección.

### Instalación

`A04` no necesita nada fuera de la biblioteca estándar. Los otros dos necesitan tres paquetes:

```console
pip install pandas matplotlib seaborn
```

El reporte de Excel al final de `06_merge_and_export.py` también necesita `openpyxl`. Si falta, el script se salta ese paso y lo dice.

Todo esto se verificó contra **pandas 3.0**, donde cambiaron dos comportamientos por omisión: Copy-on-Write siempre está activo, así que la asignación encadenada no hace nada en silencio y `.loc` es la única forma correcta de escribir en una tabla; y las columnas de texto reportan el tipo `str` dedicado en vez del antiguo `object`.

## Código fuente

[`courses/python-course/06 - Advanced/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/06%20-%20Advanced)
