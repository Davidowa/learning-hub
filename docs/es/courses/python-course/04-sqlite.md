# 04 · SQLite

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/database.svg" width="32" height="32" alt="">

Una **base de datos** real (almacén organizado y consultable) — vive en un solo archivo, viene con Python, sin servidor que instalar.

## Lo que aprenderás

- **Bases de datos relacionales** — datos organizados en tablas con filas y columnas; tablas enlazadas por claves.
- **SQL básico** — `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `JOIN`.
- **Python + SQLite** — módulo `sqlite3`: conexiones, cursores, `execute()`, `fetchall()`.
- **Consultas parametrizadas** — siempre usa marcadores `?`, nunca formatees SQL con strings (previene **inyección SQL**, una vulnerabilidad de seguridad donde la entrada del usuario se vuelve SQL ejecutable).
- **Transacciones** — agrupar cambios para que todos tengan éxito o ninguno.
- Diseño de esquemas — claves primarias, foráneas, índices.

## Analogía sencilla

Una tabla de base de datos es un **archivero**: cada cajón es una tabla, cada carpeta una fila, cada pestaña una columna. SQL es la bibliotecaria a la que pides "tráeme todos los alumnos con calificación mayor a 8".

## Seguridad: nunca hagas esto

```python
# PELIGROSO — la entrada del usuario se vuelve SQL:
cur.execute(f"SELECT * FROM users WHERE name = '{name}'")

# SEGURO — parametrizado:
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
```

La segunda forma trata a `name` como dato, no como código. Esto importa.

## Código fuente

[`courses/python-course/04 - SQLite/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/04%20-%20SQLite)
