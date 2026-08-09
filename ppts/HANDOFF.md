# COM102: the state of the decks

Every row of the syllabus now exists in both languages. This file records what
was decided, what turned out to be wrong in the source material, and the limits
that stay invisible until a card refuses to fit.

Read [`README.md`](README.md) for the layout catalogue and
[`IMAGES.md`](IMAGES.md) for the figures.

## The state

```
ppts/
  kit/            tokens, deck, build, preflight, lint, sizes, preview, doodle, figures, ct
  img/{es,en}/    28 drawn figures each, .svg and .png
  brand/          the duck logo, traced from logo.png
  python/programacion-orientada-a-objetos/
    syllabus-com102.docx
    es/  w01, w01.1 … w01.5, w02 … w17  (.yaml + .pptx)
    en/  same
```

Forty-four decks, twenty-two per language: sixteen teaching weeks, the final exam
session, and the five review sessions that hang off week 1.

**The review sessions.** `w01.1` to `w01.5` sit between week 1 and week 2, one per
module of `01 - Basics`: data and text, decisions and loops, functions,
collections, errors. They started as a single deck that tried to hold all five
modules, which covered too much too fast. Splitting them let each operator group
be shown complete and in order rather than only the confusing ones, which is what
the instructor asked for.

Slide count is not a constraint. Segmenting so the knowledge builds gradually
matters more than keeping a deck short.

```bash
cd ppts
python -m kit.preflight python   # before building: the caps below
python -m kit.build      python  # every lesson, .pptx lands next to its .yaml
python -m kit.lint       python  # text spilling past the safe area
python -m kit.sizes      python  # type below the 18 pt floor
python -m kit.figures --list     # the figures already drawn
python -m kit.preview python/.../es/w14.es.pptx w14 --cols 4
```

All four checks come back clean today, on all forty-four decks.

## What was decided, and by whom

These came from the instructor. Breaking one silently is worse than asking.

**The GUI toolkit is PyQt6.** See the correction below. Weeks 14 and 15 use
`QApplication`, `QMainWindow`, the four layouts and `clicked.connect`.

**Session numbering stays "de 17".** The syllabus has seventeen rows and the
covers count all of them, even though week 17 is the exam rather than a class.

**Weeks 8, 13 and 16 teach their full topic and close with the exam or project
logistics.** They are not review sessions. Week 17 is, and its deck is
deliberately short at sixteen slides, because the hour goes on questions.

## A correction to the previous handoff

The earlier version of this file said `05 - GUI/9th Module/` was "entirely
tkinter". It is not. All eight files, `Code037` to `Code044`, are PyQt6, with
twenty-six imports of it and no tkinter anywhere.

What does teach Tkinter is
[`docs/en/courses/python-course/05-gui.md`](../docs/en/courses/python-course/05-gui.md),
which describes `pack`, `grid` and `place` and then links to a folder of Qt code.
The page contradicts its own source link. The instructor chose to leave it alone
for now, so treat it as a known inconsistency rather than a bug to fix on sight.

This also settles the old open question. The instructor said the course would not
use tkinter because the course never did.

## Where the code comes from

Every Python example on a slide is taken from the repository, so what a student
sees on screen matches what they can clone. The cover speaker notes of each
lesson name its sources.

| Weeks | Folder |
|---|---|
| 4–8 | `02 - POO/6th Module/` — Code019 to Code028, MagicMethods.md |
| 9 | `01 - Basics/3rd–4th Module/` and `07 - Activities/Projects/02 - Hanoi Tower/` |
| 10 | `01 - Basics/4th Module/` — Code012, Code016, Code017 |
| 11 | `01 - Basics/5th Module/Code028.py` and `02 - POO/6th Module/Code026.py` |
| 12 | `03 - Paths and Files/7th Module/` — Code029 to Code035 |
| 13 | `03 - Paths and Files/7th Module/Code34.py` |
| 14–15 | `05 - GUI/9th Module/` — Code037 to Code044, PyQt6 |
| 16 | `04 - SQLite/8th Module/Code036.py` and `05 - GUI/9th Module/Code044.py` |

**Read the file before quoting it.** `Code013.py` has a real bug: line 31 calls
`this_tuple.extend(...)` and tuples have no `extend`, so it raises
`AttributeError`. Assume there are others.

Two topics have no example in the repository: binary mode with `seek` and `tell`
in week 13, and anything beyond `zipfile`. Those slides were written for the
course and the cover notes say so, which keeps the next person from hunting for
a file that does not exist.

## The caps that are not obvious

A code card shrinks its type to fit and stops at the 18 pt projection floor. Past
that it overflows instead of shrinking, so the width and the height of the source
are hard limits rather than suggestions. `kit/preflight.py` checks all of them
against the `.yaml`, which is cheaper than hearing it from `lint` after a build.

| Layout | Longest line | Rows |
|---|---|---|
| `code` and `code_output` | 63 characters | 13.9 |
| `quiz` | 57 characters | 12.4 |
| `compare`, each side | 51 characters | 8 |
| `output` panel | 36 characters | 10 lines |

A blank line counts as half a row, since it carries no code. In practice a
thirteen-line class with two blank lines fits and a sixteen-line one does not, so
most examples want a helper variable rather than one long expression.

`lint` also measures every built code line against its card. It does that with the
whole string rather than through `wrap_lines`, because that helper splits on
words, which collapses runs of spaces: a comment aligned with three spaces
measures two characters short and a line that really overflows comes back as
fitting. PowerPoint keeps every space. That single-character difference is what
let two broken slides pass every check for a week.

**The cover subtitle has its own budget: about 130 characters.** Past that it
wraps to a third line, which ends 0.06 in above the rule over the meta row. It
does not overflow and no check complains, it just looks cramped. Two lines leave
0.62 in of air. Every cover in the course sits at two.

## The YAML traps

Three of them, and the first bit on three separate weeks.

A plain scalar containing a colon followed by a space ends the key early. `subtitle: Lo que controla
cómo nace: modificadores` fails with "mapping values are not allowed here" and a
column number that points nowhere useful. Quote the whole value. `preflight`
catches it before the build does.

Commas split a flow list. `[Parcial 1, Unidades 1, 2 y 3, Semana 8]` becomes four
cells, not three. Quote any cell with a comma.

`01` parses as the integer 1. Quote numeric labels: `key: '01'`.

## The conventions, and why each one exists

**The cover names the subject.** `title` is always the course name, the session
topic goes in `subtitle`. A student opening any deck sees which course it belongs
to before anything else.

**No durations anywhere on a slide.** No "90 minutos" on the cover, no "20 min"
on the agenda cards, no "· 25 minutos" on the lab eyebrow. Minutes belong in
`notes`, which is the speaker's business.

**The accent means one thing: this is the risk.** `accent: true` belongs only on
a code annotation whose label already says so, "Riesgo" or "Si falla". Never on
an agenda card, a grading table row, a tier or a tool list. Colouring an item
because a slide looked plain is what makes a deck read as decoration.

**Two or three figures per deck, at most.** A figure earns its place by carrying
a mechanism the surrounding slides cannot.

**Show a group of operators complete, and in order.** Not only the ones that trip
people up. `w01.1` lists all seven arithmetic and all seven assignment operators;
`w01.2` lists all six comparison, all three logical, and the four membership and
identity ones. A partial table teaches that the rest do not exist.

**Python 3.12 or newer.** Consistent across every deck.

**No em dashes in the prose.** Commas, periods, colons, parentheses. The middle
dot `·` is the separator the template already uses. There are none in any deck,
including in a `tiers` key, where using one as a placeholder is tempting. Use a
word instead.

**Spanish is Mexican neutral.** No `vosotros`, no `ordenador`, no peninsular
present perfect where the preterite reads better.

## Writing a lesson

Copy the closest existing file. `w06` is the best model for a topic week, `w08`
for a week that also carries exam logistics, `w17` for a short review, `w01.1`
for a module review, and `w01` for anything administrative.

A typical topic week runs 22 to 25 slides:

```
cover · agenda · objectives · roadmap
divider(block 1) · concept · figure · code · code_output
divider(block 2) · code · code · table · pitfalls
divider(block 3) · quiz · trace · lab · method
takeaways · homework · closing
```

Set `roadmap` phase states so `now` matches the week, and set `blocks:` to the
number of dividers, since it drives the footer pips. Week 17 uses two.

## Drawing a new figure

If a week needs a diagram that does not exist yet, draw it rather than generating
it: `kit/doodle.py` has the pen, the duck, and the shape primitives, and
`kit/figures.py` shows the pattern. Labels drawn from a font are always spelled
correctly, which an image model cannot promise.

Add every label to the `T` dict in both languages, add the entry to `FIGURES`
with `about` and `reuse` text, then `python -m kit.figures <name> --overwrite`
and `python -m kit.figures --catalogue > IMAGES.md`.

Two things learned drawing the last ten. Leave at least 90 px between two boxes
when an arrow runs between them, or the arrowhead lands inside a box and the
arrow reads as a stub. And when several arrows fan out from one point to targets
at different heights, put any cross or label three quarters along the arrow, not
at the midpoint, where it sits ambiguously between two of them.

Scenes with atmosphere, a duck at a desk, two ducks at a laptop, are the ones
worth asking an image model for. Those prompts are in [`PROMPTS.md`](PROMPTS.md),
and the image quota on the instructor's Gemini key is currently zero, so they are
blocked until billing is enabled.

## The verification loop

After each week, in this order:

1. `python -m kit.preflight python` — the caps above, before anything is built
2. `python -m kit.build python` — must print no `!` lines
3. `python -m kit.lint python` — 0 issues
4. `python -m kit.sizes python` — 0 runs below 18 pt
5. `python -m kit.preview` the new deck and actually look at the contact sheet

Step 5 is not optional. The first four catch geometry; only looking catches a
slide that is correct and still says nothing. It is what caught a `w17` agenda
promising three blocks across four cards.

## What is still open

**`docs/05-gui.md` still teaches Tkinter** while linking to PyQt6 source, in both
languages. See the correction above.

**Week 16 leans on `Code044.py` for the PyQt6 and sqlite3 pairing**, and that file
deletes and recreates `user.db` on every run. Fine as a demonstration, wrong as a
model for a project. The deck does not quote that part, and a future session
expanding week 16 should not start.

**File ordering.** `w01.1` sorts before `w01` because `.` precedes letters. If
more half-weeks appear, `w01b` reads better.
