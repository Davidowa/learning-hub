# Course decks

Slide generator for the Academia de Cómputo courses. Lessons are written as YAML,
the kit turns them into `.pptx` files that match
`Programming_course_slide_template.pptx` down to the coordinate.

The point is that a sixteen-week course in two languages is 34 decks. Hand-placing
text boxes 34 times is how a template drifts. Here the design lives in one file
and the lessons live in another, so a change to the look reaches every deck on the
next build.

## Build

```bash
cd ppts
python -m kit.build python                        # every lesson under python/
python -m kit.build python/programacion-orientada-a-objetos/es/w03.es.yaml
python -m kit.lint  python/programacion-orientada-a-objetos/es
python -m kit.preview python/programacion-orientada-a-objetos/es/w03.es.pptx w03 --cols 3
```

Each `.pptx` lands next to the `.yaml` it came from. Requires `python-pptx`,
`pyyaml` and `Pillow`.

## Layout

```
ppts/
  kit/
    tokens.py     type, geometry, and one colour palette per language
    highlight.py  syntax highlighting for Python, C#, C++, VBA, SQL
    deck.py       the Deck class, one method per slide archetype
    build.py      YAML -> .pptx
    preflight.py  YAML checks that are cheaper to run than a build
    lint.py       overflow check against the safe area
    preview.py    .pptx -> PNG, for reviewing a build without PowerPoint
  brand/          the duck, as SVG and PNG
  python/
    programacion-orientada-a-objetos/     COM102, written
      syllabus-com102.docx
      es/         w01.es.yaml + w01.es.pptx, w02…, w17…
      en/         same
  cpp/
    programacion-avanzada/                COM103, written
      HANDOFF.md  what was decided, measured and left open
      syllabus-com103.docx
      es/  w00 … w17  (.yaml + .pptx)
      en/  same
  vba/
    analisis-y-procesamiento-de-la-informacion/   TIA503, week 1 written
      HANDOFF.md
      syllabus-tia503.xlsx
      es/  w01  (.yaml + .pptx)
      en/  same
```

One folder per language of instruction, then one per subject, then `es` and `en`.
The generated deck sits beside its source so a lesson is one place, not two, and
the subject folder keeps its syllabus above the two language folders, since the
agenda, the grading table and the roadmap all trace back to it.

## Writing a lesson

A lesson file is a `meta` block and a list of slides. Each slide is a single key
naming a layout, and its value is that layout's arguments.

```yaml
meta:
  course: Programación Orientada a Objetos
  code: COM102
  lang: es                 # run language, for spellcheck and screen readers
  language: python         # which colour palette the deck uses
  footer: PROGRAMACIÓN ORIENTADA A OBJETOS · COM102 · PYTHON
  blocks: 3                # progress pips in the footer

slides:
  - cover:
      kicker: Facultad de Ingeniería · 2026
      unit: Semana 03 · Tema 2 · Elementos básicos
      title: Programación Orientada a Objetos      # the subject, on every cover
      subtitle: Clases, objetos y el estado que guardan. El vocabulario mínimo del paradigma.
      meta:
        - [Profesor, David Escobar-Castillejos]
        - [Clave, COM102 · Semestre 2]
        - [Sesión, 3 de 17]
      notes: |
        Speaker notes go here. They end up in the notes pane, not on the slide.

  - code:
      eyebrow: Python
      title: La clase más pequeña que ya sirve de algo
      filename: punto.py
      lang: python
      source: |
        class Punto:
            def __init__(self, x: float, y: float) -> None:
                self.x = x
      annotations:
        - label: Línea 2
          text: El constructor corre solo, al escribir Punto(1, 2)
        - label: Riesgo
          text: Si olvidas self, Python reclama un argumento de más
          accent: true       # see "the accent" below
```

Two conventions the decks follow, worth keeping when you add a week:

**The cover names the subject.** The session topic goes in the subtitle. A student
who opens any deck sees which course it belongs to before anything else.

**No durations on the slides.** Minutes belong in the speaker notes, not in front
of the group. The agenda cards carry a title and a blurb, nothing else.

### Two YAML traps

Commas split a flow list, so `[Parcial 1, Unidades 1, 2 y 3, Semana 8]` becomes
four cells instead of three. Quote any cell containing a comma. The build fails
with the row printed, so you will know.

`01` parses as the number 1. Quote numeric labels: `key: '01'`.

## Layouts

| Layout | What it is for |
|---|---|
| `cover` | Dark opener with unit, title, instructor and session |
| `agenda` | Four cards with a number, a title, a blurb and a duration |
| `objectives` | Arrow list, up to six, two per row |
| `roadmap` | Where the session sits in the semester, `state: done / now / todo` |
| `divider` | Dark block break, sets the footer progress pip |
| `concept` | Definition on the left, numbered steps in a card on the right |
| `diagram` | Two to four blocks joined by arrows, one may be `dark: true` |
| `code` | Code card plus up to four margin annotations |
| `code_output` | Code card plus a console output panel |
| `figure` | A drawn diagram from `img/`, centred, with a caption and optional side note |
| `compare` | Before and after, light card against dark card |
| `table` | Comparison grid, up to seven rows, `accent_row` marks one |
| `trace` | Execution trace with a verdict line underneath |
| `steps` | Up to five numbered columns with a rule on top |
| `stat` | One dark slide, one big number |
| `pitfalls` | Four common errors in a 2 x 2 grid |
| `method` | A statement in serif with supporting columns |
| `lab` | Exercise brief in a card, with constraints below |
| `quiz` | Question, optional code card, lettered options |
| `tiers` | Rows of key, title and description (costs, tools, principles) |
| `quote` | Dark slide, pull quote, attribution |
| `takeaways` | Numbered list with a rule between rows |
| `homework` | Brief, submission metadata and a rubric |
| `closing` | Dark slide with contact details |

Every layout except `cover`, `divider`, `stat`, `quote` and `closing` takes
`eyebrow` and `title`. All of them take `notes`.

## Design tokens

Measured off the template, in `kit/tokens.py`. Surfaces and neutrals are fixed:

| Token | Value | Where it goes |
|---|---|---|
| `NAVY` | `#0B1B3A` | Covers, dividers, code cards, the "process" block. The two Office palettes override it to `#0B2A1B`, a deep Excel green, so a VBA deck is not dark blue in a course about a green program. |
| `PAPER` | `#F7F8FA` | Content slides |
| `INK` / `MUTED` | `#0F172A` / `#5B6B84` | Primary and secondary text on paper |
| `BORDER` | `#DBE3EF` | Hairlines at 0.75 pt |

The accent pair and the syntax theme change with `meta.language`, following the
"use colours related to the language" rule in `guidelines.md`:

| Slot | `generic` (the template) | `python` | `cpp` | `csharp` | `vba` |
|---|---|---|---|---|---|
| `BLUE` structure text | `#2563EB` | `#306998` brand blue, 5.5:1 | `#00599C` logo blue, 6.8:1 | `#65549F` brand purple at 70 %, 6.0:1 | `#107C41` Excel forest green, 5.0:1 |
| `BLUE_FILL` chips and bars | `#2563EB` | `#306998`, white text at 5.8:1 | `#00599C`, white text at 7.2:1 | `#65549F`, white text at 6.3:1 | `#107C41`, white text at 5.3:1 |
| `ACCENT` on the dark canvas | `#E8871E` duck orange | `#FFD43B` logo yellow, 12.0:1 | `#E8871E` duck orange, 6.4:1 | `#E8871E` duck orange, 6.4:1 | `#E8871E` duck orange, 5.8:1 |
| `ACCENT_LO` on paper | `#B4530A` | `#8A6A00` logo yellow, darkened to 4.8:1 | `#B4530A` duck orange, 4.7:1 | `#B4530A` duck orange, 4.7:1 | `#B4530A` duck orange, 4.7:1 |

`csharp` and `mysql` have no decks yet. They are defined so the first lesson of
either does not start by inventing colours.

`mysql` is the only palette that overrides the dark canvas for a reason other than
brand: MySQL teal `#00758F` and the C++ blue `#00599C` are close enough that a
navy deck in teal reads as a C++ deck at a glance, and both courses run in the
same term. Its canvas is `#0A1F2B`, a deep teal, which separates them on sight.

`excel` is a fifth palette, for a deck whose code cards hold spreadsheet formulas
rather than VBA. It carries the same Excel green and the same duck orange, and
differs in the syntax theme: the formula scanner never emits a comment, since
Excel has no comment syntax, so its `com` slot carries an error value like `#N/A`
and takes the accent rather than comment grey. Literals drop to the neutral,
because in a formula the reference and the error matter more than the number
typed inside it.

C++ has no second brand colour, so its accent pair stays the academy's duck
orange. Two blues would collapse the one thing the accent is for. VBA is in the
same position and takes the same way out: Excel green carries the structure, the
duck keeps the accent.

### The published brand colours, and what the kit does with them

Checked against brandcolorcode.com. The brand hex is the starting point; the
contrast is the requirement. Where the two agree the kit uses the brand colour
untouched, and where they disagree the colour gets darkened or lightened until it
clears 4.5:1 against the surface it actually lands on.

| Language | Published | In the kit | |
|---|---|---|---|
| MySQL | `#00758F`, `#F29111` | both, split by surface | The only palette besides Python whose accent is the language's own rather than the duck. The teal is 5.0:1 on paper and 3.2:1 on a dark canvas, so it carries structure on light; the orange is 2.2:1 on paper and 7.1:1 on the canvas, so it carries the accent on dark and darkens to `#91570A` for white. |
| C++ | `#00599C`, `#004482` | the same two | Brand exact. The third brand blue `#659AD2` is 2.8:1 on paper, so it stays out of every text slot. |
| Python | `#306998` | `#306998` | Brand exact, and it replaced the older `#3776AB`. That one only reached 4.55:1 on paper, which is why it had to be darkened to `#2B5F8F` for text. `#306998` needs no darkening: 5.5:1 on paper, 5.8:1 under white, so one colour now fills both slots. |
| Python | `#FFD43B` | `#FFD43B` on navy, `#8A6A00` on paper | The yellow is 1.34:1 on paper, unreadable. It never touches a light surface; the darkened gold stands in there at 4.8:1. |
| C# | `#9179E4` | `#65549F` on paper, `#A18DE8` on navy | The purple is 3.3:1 on paper and 3.5:1 under white, so it gets the same split the Python yellow gets. |
| Excel | `#33C481`, `#21A366`, `#107C41`, `#185C37` | `#107C41`, `#185C37`, `#33C481` | Three of the four brand exact, split by surface. See below. |

**How the Excel greens split.** All four published greens are in use, each on the
surface where it clears the bar, which is the same trick the Python yellow gets.
`#107C41` carries the structure at 5.0:1 on paper; `#185C37` is the deepest at
7.5:1; `#33C481` is useless on paper at 2.1:1 but reads 6.9:1 on the green canvas,
so it carries the keywords in the dark code card. `#21A366` is the one left out,
since it fits nowhere comfortably: 3.0:1 on paper and 4.8:1 on the canvas.

The kit used to carry `#217346`, which is not a published Excel green at all. It
read slightly better than `#107C41`, 5.5:1 against 5.0:1, and both clear the bar,
so the brand-exact colour won.

Every text colour in every palette is at or above 4.5:1. That is 198 measured
slots across six palettes, code themes included.

In the Python syntax theme, blue marks the language (`class`, `def`, `for`) and
yellow marks the names you wrote (functions, `self`, numbers). Adding a language
means adding one `Palette` to `kit/tokens.py`; nothing in `deck.py` changes.

Canvas is 20 x 11.25 in. The left margin is 1.04 in and everything hangs off it.

Georgia, Arial and Courier New stand in for Instrument Serif, Inter Tight and
JetBrains Mono, the same substitution the original template makes so the file
renders on a machine that has none of them installed.

## What the kit enforces

The rules in [`guidelines.md`](guidelines.md) are built in rather than left to
discipline:

- **Nothing below 18 pt.** That is roughly 24 px projected, the floor for a
  lecture hall. Code cards shrink to fit the card and stop at 18 pt; past that
  the build prints a warning telling you to split the example.
- **Contrast at WCAG AA.** Every palette carries two accents: the bright one only
  ever appears on navy, the darkened one only on paper. Python yellow `#FFD43B`
  reads at 12.0:1 on navy and 1.3:1 on paper, so on paper it becomes `#8A6A00`.
- **Text is measured before it is placed.** Headings shrink instead of spilling,
  cards grow to the tallest one in the row, and annotation blocks stack by their
  real height. `python -m kit.lint` re-checks the built file.
- **One code line, one text box.** Line breaks collapse inside a single frame, so
  each line is placed on its own and can be edited without disturbing the rest.
- **The accent means one thing: this is the risk.** `accent: true` belongs on a
  code annotation whose label already says so ("Riesgo", "Si falla"), and nowhere
  else. Colouring an item because a slide looked plain is what makes a deck read
  as decoration, so the lessons here carry at most one accent per slide and none
  on the agenda, the grading table or the tool list.
- **`lang` on every run** and `alt=""` on the decorative footer duck, so a screen
  reader skips the logo and pronounces the text correctly.

## The duck

`brand/duck.svg` is a trace of the original PNG, recoloured to the deck palette:
body `#E8871E`, shading and beak `#B4530A`, highlights `#F5B461`, outline `#0B1B3A`.
It came out of `logo.png` by k-means clustering the colours into four layers,
cleaning each with a median filter, then tracing the contours and smoothing them
into cubic curves.

- `duck.svg` for light backgrounds, `duck-512.png` for the footer
- `duck-on-dark.svg` lifts the outline to `#1E3A6B` so it reads on navy;
  `duck-on-dark-512.png` is on the cover
- `duck-mono.svg` uses `currentColor` for single-colour contexts

## Adding a week

Copy the closest existing lesson, change `meta.week` and the content. The session
counter in `cover.meta` and the `roadmap` states are the two things easy to forget.

## Adding a course

Make `python/<subject>/es` and `python/<subject>/en`. Nothing in the kit is
specific to COM102, but the footer string, the roadmap phases and the grading
table come from that course's syllabus, so they live in the lesson files rather
than in the kit.

A course in another language gets its own top-level folder next to `python/`, and
a `Palette` in `kit/tokens.py` so the decks read in that language's colours.

## Where the examples come from

The Python code on the slides is taken from
[`docs/en/courses/python-course/`](../docs/en/courses/python-course), so what a
student sees on screen matches what is in the repository. Week 3 uses `Point`,
`Person` and `ShoppingCart` from `02 - POO/6th Module/Code019.py`. Each lesson
names its sources in the cover speaker notes.
