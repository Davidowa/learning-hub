# 03 · Archivos y rutas

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/folder-open.svg" width="32" height="32" alt="">

Los programas que **recuerdan** cosas necesitan leer y escribir archivos.

## Lo que aprenderás

- **Rutas (paths)** — dónde vive un archivo en el disco. Absoluta vs relativa. `pathlib.Path` (la forma moderna y multiplataforma).
- **Leer y escribir texto** — `open()`, la sentencia `with` (asegura que el archivo se cierre incluso si hay errores).
- **Codificaciones** — por qué importa `utf-8` (pista: es la diferencia entre `niño` y `ni�o`).
- **Formatos estructurados:**
  - **CSV** — datos tabulares tipo hoja de cálculo (módulo `csv`).
  - **JSON** — datos anidados, amigable para la web (módulo `json`).
  - **Pickle** — objetos Python directo a disco (con cuidado; no seguro con fuentes externas).

## Analogía sencilla

Una ruta de archivo es como una **dirección postal**: el sistema operativo necesita la dirección completa (`C:\Users\tu\notas.txt`) para encontrar tu documento. Una ruta relativa es "dos casas más allá de donde estás parado".

## Errores comunes

- Olvidar cerrar archivos → usa `with open(...) as f:` y no te preocupes más.
- Mezclar separadores de ruta entre sistemas operativos → usa `pathlib.Path`, nunca concatenación de strings.
- Desajuste de codificación → siempre especifica `encoding="utf-8"` salvo razón específica.

## Código fuente

[`courses/python-course/03 - Paths and Files/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/03%20-%20Paths%20and%20Files)
