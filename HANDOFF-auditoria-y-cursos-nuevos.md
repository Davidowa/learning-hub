# Auditoría de los decks y cursos nuevos: dónde quedó y cómo seguir

Estado al detener (6 de octubre de 2026): todo en `main`. Los 334 decks construyen sin errores ni
avisos, y preflight, lint y sizes están en cero en las 22 carpetas de idioma. La sesión se detuvo
a pedido del profesor con la auditoría casi terminada y los cursos nuevos en borrador.

Lo que se pidió, y en qué quedó cada parte:

| Pedido | Estado |
|---|---|
| Auditar que todas las slides describan bien y funcionen | 166 de 167 semanas auditadas; 68 con revisión adversarial completa |
| Compilar todas las slides en PDF | Scripts en la raíz que generan los PDFs en cada computadora; los PDFs no van en git |
| Pasar the-writer sobre cómo se explica todo | Herramientas listas y probadas; la pasada no se corrió |
| Curso de móviles, React Native y SwiftUI, mismo temario, es y en | Dos de tres propuestas de diseño; falta sintetizar el temario y escribir los decks |
| Auditar el temario de móviles para que trascienda en el tiempo | Las dos propuestas traen la auditoría renglón por renglón; falta la síntesis |
| Curso de fundamentos de comercio electrónico, es y en | Temario de 17 sesiones sintetizado en `plan.json`, sin verificar; faltan documentos y decks |

## 1. La auditoría de los 334 decks

**Cómo se hizo.** Una semana es el par es/en. Por cada semana, un agente auditor leyó las dos
versiones completas, notas incluidas, y corrió todo el código que se podía correr: Python 3.11
(con pandas, seaborn y PyQt6 sin pantalla), g++ y clang con `-std=c++20 -Wall -Wextra`, .NET 10 y
MariaDB 10.11 en lugar de MySQL 8. Comparó cada panel de salida con la salida real. Además revisó
referencias de línea, respuestas de quiz, trazas, afirmaciones técnicas y títulos que no
describen su diapositiva. También cuidó la paridad es/en, el español de México y el inglés de
EE. UU., y que cada ejercicio use solo lo enseñado hasta esa semana. Corrigió lo que confirmó.
Después, un segundo agente intentó refutar cada corrección: revirtió lo que no era defecto,
arregló correcciones mal hechas e hizo su propia pasada.

**Lo que salió.**

- 2,748 ejemplos de código ejecutados o compilados.
- 2,588 hallazgos de la primera pasada; 1,760 corregidos ahí.
- La revisión adversarial, sobre las semanas que alcanzó: confirmó 585 correcciones, rehízo 117,
  declaró 181 hallazgos como no defectos y encontró 216 nuevos, de los que corrigió 177.

Ejemplos de lo que se corrigió:

- Paneles de salida que el código mostrado no podía producir (C++ w09, C# w09, y otros).
- Referencias "Línea N" que apuntaban a otra línea (POO w03 y w07).
- Afirmaciones falsas: un `math.py` local no sombrea al `math` integrado en CPython, pero
  `statistics.py` sí; un `int` sí cabe en un `float` en C#.
- Consultas SQL que ordenaban meses alfabéticamente.
- Títulos que anunciaban "tres" sobre tablas de cinco.
- 225 hallazgos de ortografía británica (per cent, recognise, behaviour y similares).
- Covers en inglés con kicker en español.
- Las fórmulas con separador `;` de España donde el Excel de México usa `,`; solo en las semanas
  que se alcanzaron.

**Dónde está todo.**

| Archivo | Qué tiene |
|---|---|
| [`ppts/audit/estado.md`](ppts/audit/estado.md) | Qué semanas tienen las dos pasadas, cuáles solo la primera y qué revisiones se cortaron a medias |
| [`ppts/audit/prioritarios.md`](ppts/audit/prioritarios.md) | 169 hallazgos abiertos de severidad alta o media, o confirmados por la revisión, que esperan una decisión tuya |
| [`ppts/audit/abiertos.md`](ppts/audit/abiertos.md) | Los 958 hallazgos abiertos, con los de severidad baja |
| [`ppts/audit/no-verificado.md`](ppts/audit/no-verificado.md) | Lo que no se pudo ejecutar (VBA, fórmulas de Excel, C# de Unity, datos externos) y se revisó leyendo |
| [`ppts/audit/hallazgos.json`](ppts/audit/hallazgos.json) | Todo lo que reportó cada agente, crudo |
| `ppts/audit/wip/` | Dos correcciones a medias que se retiraron (ver abajo) |
| `ppts/audit/herramientas/` | `check.sh`, el extractor de prosa para the-writer y los scripts de los workflows |

**Normalizaciones que hice al cerrar**, porque los agentes, cada uno en su semana, habían dejado
cosas inconsistentes entre semanas:

- El título de objetivos en español vuelve a "Al terminar la sesión el alumno podrá…" en los 167
  decks. Algunos agentes lo cambiaron a "podrás" y otros no. Si prefieres tú en todo el
  repositorio, es una sola sustitución: `el alumno podrá…` por `podrás…` en los `*.es.yaml`.
- Los 17 decks en inglés de office tenían el kicker "Facultad de Empresariales" y la clave
  "TIA501 · Empresariales". Quedan "School of Business" y "TIA501 · Business", como VBA.

**Figuras.** Se corrigieron en `kit/figures.py` los siete defectos de la lista del profesor, y la
revisión agregó un octavo:

- C++ w06 tiene su propia figura de clase y objeto, sin el `__init__` de Python.
- Las flechas de `slicing` y `seek-tell` ya no tachan el índice que explican.
- La cinta en español dice "HOLA A TODOS", un byte por casilla.
- `exceptions` usa `edad` y su etiqueta ya no queda bajo la flecha.
- La jerarquía en español dice `ArchivoStream`.
- `value-vs-reference` en inglés dice `twiceRef`, como el código.

Ink Free y Consolas no existen en Linux, así que se dibujaron con los contornos sacados de los
SVG ya publicados; coinciden a 0.1 px. En Windows, `python -m kit.figures` las redibuja con las
fuentes reales sin cambio visible.

### Lo que falta de la auditoría, en orden

1. **La revisión adversarial de 98 semanas.** La primera pasada ya las corrigió; falta el segundo
   agente. La lista está en `estado.md`, junto con las 32 revisiones que se detuvieron a medio
   camino. Sus ediciones parciales se conservaron porque pasan los cuatro chequeos, pero hay que
   volver a correrlas.
2. **office w09, desde cero.** Su auditoría se cortó dos veces. El avance sin verificar está en
   `ppts/audit/wip/office-w09-auditoria.diff`, pero no se aplicó.
3. **csharp w02, partir una diapositiva.** La revisión encontró un defecto real: en el plan de
   arranque de la impresora, el programa imprime "iniciando impresion" también después de
   "ABORTAR", y el ciclo no tiene tope. Corregirlo deja tarjetas de 16 y 18 líneas, que no caben.
   Hay que partir el ejemplo en dos diapositivas, en los dos idiomas. La corrección a medias está
   en `ppts/audit/wip/csharp-w02-revision.diff`.
4. **Las decisiones de `prioritarios.md`.** Las que cruzan cursos enteros:
   - Separador de argumentos en Excel. Los decks en español de Análisis de Datos y de Algoritmos
     en Python usan `;` en w01.1, w06, w13 y w15.3. Si las máquinas del salón están en es-MX, va
     `,`, como ya lo hace TIA501.
   - Ningún quiz de los cursos de Python tiene notas con la respuesta ni con qué representa cada
     distractor. Los agentes confirmaron que la clave es única en cada uno, pero no inventaron
     las notas.
   - C++ w00: la tabla de velocidad y memoria y los porcentajes por sector vienen de la
     infografía original. Las notas que decían que son una valoración editorial se borraron en
     `6818abb`, y los números no coinciden con benchmarks publicados.
   - Visual Studio 2026 puede crear `.slnx` en lugar de `.sln` (C++ w01). Hay que comprobarlo en
     la máquina del salón.
   - MySQL w01: la tabla `inscripcion` de la diapositiva 7 no es la misma que usa el `INSERT` de
     la diapositiva 17.
   - Análisis de Datos w01.0: la tarea se entrega como `.png`, y la misma presentación dice que un
     archivo solo de imágenes vale cero.

## 2. Los PDFs

En la raíz están `generar-pdfs.bat` (que corre `generar-pdfs.ps1`) para Windows y
`generar-pdfs.command` para macOS. Hacen lo siguiente:

1. Crean `.venv/` e instalan `ppts/requirements.txt`.
2. Construyen los decks desde el YAML.
3. Los exportan a `pdf/`: uno por presentación en `pdf/decks/` y uno por curso e idioma, con un
   marcador por sesión. `pdf/` está en `.gitignore`.

En Windows exportan con PowerPoint por COM si está instalado, y si no, con LibreOffice; en macOS,
con LibreOffice. Para un solo curso: `generar-pdfs.bat python` o
`./generar-pdfs.command cpp/programacion-avanzada`. Por debajo es `python -m kit.pdf`.

Probados de punta a punta en Linux, el `.ps1` con PowerShell 7. Dos agentes los revisaron con
lente de Windows (PowerShell 5.1) y de macOS (bash 3.2), pero nadie los ha corrido en una
máquina Windows o Mac real. La primera corrida en cada una es la prueba que falta.

Dos cambios del kit los hicieron posibles:

- **Sombra de tema.** python-pptx deja en cada forma una referencia a la sombra del tema. Ahora
  `Deck.save` la apunta a ningún efecto. PowerPoint no cambia, y LibreOffice dejó de exportar
  cada línea de texto como imagen borrosa: un deck pasó de 9.5 MB a 434 KB de PDF.
- **Fuentes.** `kit/fonts.py` encuentra Arial, Georgia y Courier New en Windows, macOS y Linux.
  Antes el kit solo las buscaba en `C:\Windows\Fonts`, y en una Mac medía el texto con una
  aproximación.

## 3. The-writer

No se corrió. Lo que quedó listo:

- `ppts/audit/herramientas/extraer_prosa.py` saca la prosa de cada deck a un `.md`: un campo por
  párrafo, más un `.map.tsv` que dice de qué diapositiva y campo viene cada renglón.
- Se probó contra `scripts/lint.py` de
  [the-writer](https://github.com/Davidowa/Skills/tree/main/the-writer) con
  `--audience essay --register formal`.

Lo que conviene saber antes de correrlo:

- El lint marca como "choppy paragraphs" que cada campo sea un fragmento corto. En diapositivas
  es normal; se ignora.
- Lo que sí vale: ortografía británica (encontró "catalogue" y "practising" en C++ w03 en),
  primera persona del plural y formas peninsulares. Ojo: "matrícula" sale marcada, y en México sí
  es el número de alumno.
- Corre en modo review por curso y por idioma, con la plantilla de `references/review-report.md`.
  Aplica solo las correcciones del bloque A (piso), y vuelve a correr `check.sh` en cada deck que
  toques.
- Hazlo después de terminar la auditoría, para que los dos procesos no editen los mismos
  archivos.

## 4. Los cursos nuevos

**Comercio electrónico** (`ppts/ecommerce/fundamentos-del-comercio-electronico/`):

- `plan.json`: temario de 17 sesiones sintetizado a partir de tres propuestas (durabilidad,
  práctica y pedagogía, en `propuestas/`, en inglés), con la auditoría renglón por renglón del temario
  original, las sesiones en es y en, la evaluación (dos parciales, proyecto, final y tareas, 20 %
  cada uno), un caso que corre todo el curso y un anexo fechado de herramientas y leyes.
- Las sesiones: modelos y canales; cliente y propuesta de valor; la economía de un pedido;
  plataformas; catálogo; experiencia de compra y embudo; pagos; checkout y conversión; pedidos,
  inventario y riesgo; fulfillment; devoluciones y facturación; adquisición; medición; retención;
  ley, privacidad y ética; evaluar la siguiente herramienta; examen final.
- **No está verificado.** El fact-check se cortó: hay que revisar, sobre todo, la ley de datos
  personales de 2025 y el regulador que sustituyó al INAI, PROFECO, la NOM-247-SE, CFDI,
  SPEI/CoDi/DiMo, BNPL en México, PCI DSS y GA4.
- Siguen los documentos de temario en es y en, la auditoría del temario y los 34 decks.

**Móviles, React Native y SwiftUI** (`ppts/react-native/desarrollo-de-aplicaciones-moviles/`,
compartido por los dos cursos):

- Dos de tres propuestas, durabilidad y práctica, en `propuestas/` (en inglés, como las escribieron
  los agentes); cada una con la auditoría del temario original renglón por renglón. Ahí aparece, por ejemplo, que la máquina virtual Dalvik se sustituyó por ART
  desde Android 5.0, y que los storyboards dejaron de ser el camino principal en iOS.
- Faltan la propuesta de pedagogía, la síntesis, el fact-check, los documentos y los 68 decks.
- Versiones comprobadas en el registro de npm el 5 de octubre de 2026, en
  `versiones-verificadas-2026-10-05.txt`: Expo SDK 57 trae React Native 0.86.3 y React 19.2.3.
- En el contenedor de la nube no hay compilador de Swift; el código SwiftUI solo se puede
  revisar leyendo.

**El kit ya está listo para los tres:**

- Paletas `react`, `swift` y `commerce` en `kit/tokens.py`, con todo el texto a 4.5:1 o más.
- Resaltado de TSX/JavaScript, Swift, Kotlin, Java, JSON y shell en `kit/highlight.py`.

El script `ppts/audit/herramientas/workflows/diseno-de-temario.js` retoma el diseño. Lee el
temario original de la carpeta del curso y escribe ahí `plan.json`.

**Decisiones pendientes para los cursos nuevos:**

- La clave de cada curso. Mientras tanto, el cover puede llevar "Plataforma" en lugar de "Clave".
- La facultad del kicker de comercio electrónico. "Facultad de Empresariales", como TIA501 y
  TIA503, es la suposición.
- El año del kicker: los demás dicen 2026, y estos cursos seguramente empiezan en 2027.

## 5. Cómo retomar

En Windows o macOS, los chequeos del kit corren con las fuentes del sistema:

    cd ppts
    ../.venv/Scripts/python.exe -m kit.build <carpeta>        # macOS: ../.venv/bin/python
    ../ppts/audit/herramientas/check.sh <archivo.yaml>        # build + preflight + lint + sizes

En un contenedor Linux en la nube hay que instalar antes lo que se usó aquí:

- **Fuentes.** Arial, Georgia y Courier New, sacadas con `cabextract` de `arial32.exe`,
  `georgi32.exe` y `courie32.exe` de `downloads.sourceforge.net/corefonts`, copiadas a
  `/usr/share/fonts/truetype/mscore/`. Sin ellas el lint mide con una aproximación y reporta
  cientos de avisos falsos.
- **Paquetes de apt:** `dotnet-sdk-10.0`, `mariadb-server`, `libreoffice-impress`.
- **Python:** `pip install python-pptx pyyaml pillow pypdf pandas matplotlib seaborn PyQt6`.
- **React Native:** para revisar su código, `typescript`, `react-native@0.86.3`, `react@19.2.3`,
  `expo` y `expo-router` con npm, y `tsc --noEmit`.

Los workflows de `ppts/audit/herramientas/workflows/` son los que se usaron:

- `auditoria-de-decks.js` recibe `{course, dir, weeks}`; por ejemplo,
  `{"course": "vba", "dir": "ppts/vba/analisis-y-procesamiento-de-la-informacion",
  "weeks": ["w03", "w04"]}`. Para los tracks de Unity, `dir` es `ppts/unity` y cada semana va como
  `"essentials|w01"`.
- Para terminar solo las revisiones, conviene recortar el script a la segunda pasada y darle la
  lista de `estado.md`.

**Dos avisos de cómo se trabajó:**

- Un agente de auditoría hizo commit y push directo a `main` (`aba4d08`, `20e80a7`, `9c1c864`),
  aunque sus instrucciones se lo prohibían. Lo más probable es que lo empujara el mismo gancho que
  pide commit al terminar cada turno. El contenido son sus dos YAML por semana y es correcto. En
  la siguiente corrida, dile a cada agente que no haga commit ni push aunque se lo pida un gancho.
- El límite semanal de uso cortó la corrida una vez a la hora. Los workflows se reanudan desde
  caché con `resumeFromRunId` sin perder lo terminado.
