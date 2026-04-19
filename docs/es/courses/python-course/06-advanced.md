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

## Código fuente

[`courses/python-course/06 - Advanced/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/06%20-%20Advanced)
