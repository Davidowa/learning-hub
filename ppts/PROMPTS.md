# Image prompts, deck palette

The sketchbook illustrations in `docs/*/courses/computational-thinking-course/assets`
stay with that course. Everything for the programming decks gets made fresh in the
deck palette, so a slide never mixes two visual systems.

Two sources feed the decks.

- **Drawn by code** — the nine schematic diagrams in [IMAGES.md](IMAGES.md), plus
  the duck character the drawing engine now has. Exact labels, no cost, versioned
  as SVG. Anything where a specific word has to be legible belongs here.
- **Asked of Gemini** — scenes with people, gesture and atmosphere. The prompts
  below, one per request, for the Gemini web app.

---

## The style block

Paste it verbatim at the end of every prompt. Do not paraphrase it: the set
holding together depends on it being identical in every request.

```text
Style: hand-drawn doodle sketch on a plain off-white #F7F8FA background. Loose,
imperfect, confident ink line art drawn entirely in deep navy #0B1B3A, never
black, never grey. The recurring character is a small rubber duck, drawn simply:
one rounded body with the head merged into it as a single silhouette, never two
separate circles stacked; a short wide flat beak; one small solid dot eye; a
teardrop wing lying on the flank; two thin legs with webbed feet. The duck is
pale yellow. Colour appears only as flat washes filling a few shapes, and only
two colours exist: a muted Python blue #3776AB and a soft Python yellow #FFD43B,
both at about 20 percent strength. Everything else is navy line work on
off-white. No paper texture, no spiral binding, no outer frame, no pencil
shading, no gradients, no drop shadows, no 3D, no photorealism. Wide panoramic
composition with generous empty space. Any labels in sketchy handwritten
lettering, spelled exactly as given.
```

Ask for **16:9**. The `figure` layout on a slide is 17.9 in wide by about 6.5 in
tall, so anything from 16:9 to 21:9 drops in cleanly.

Two things about text inside a picture. First, the model will sometimes misspell
it, which is why `CT-08` in the other course ended up with a speech bubble reading
`SHEAT LOTH WORLD AT LLAI LING SOON END... IT WELT!`. Second, Spanish labels come
out worse than English ones, because there is less of it in the training data. So
where the exact word carries the teaching, ask for the picture with no label and
let the slide caption say it, or tell me and I will draw it instead.

---

## The prompts

One image per request. The filename is what the deck expects: drop the result in
`ppts/img/es/` or `ppts/img/en/`, or `ppts/img/shared/` when the picture has no
text in it.

### 1 · `lab-pairs.png` — pair work · any lab slide

> Two ducks sit side by side at a single open laptop on a desk. The one on the
> left points at the screen with a wing; the one on the right stands over a small
> notebook. A small speech bubble floats between them with a single question
> mark in it. The laptop screen carries a flat soft Python blue wash; the notebook
> carries a flat soft Python yellow wash. Nothing else is coloured and nothing is
> labelled.
>
> …then the STYLE BLOCK above.

No text inside, so it works in both languages and never needs redoing. Start with
this one: it is the cleanest test of whether the style block is landing.

### 2 · `duck.png` — rubber duck debugging · w01.1, w03

> A duck stands at a desk beside an open laptop, reading its code out loud. Three
> little curved speech marks float from its beak toward the screen. A lightbulb
> doodle glows above its head. The duck carries a flat Python yellow wash and is
> the brightest thing in the picture; the laptop screen carries a soft Python blue
> wash. No labels anywhere.
>
> …then the STYLE BLOCK above.

Deliberately unlabelled so the same file serves both languages. The slide title
already says rubber duck debugging.

### 3 · `honour-code.png` — where the AI line sits · w01

> A wide image split into two halves by a wavy vertical navy line. On the left, a
> duck writes its own code on a sheet of paper while a small friendly robot beside
> it points at an open book; a lightbulb glows above the duck. On the right, the
> same robot hands a finished sheet of code to a duck that takes it without
> looking, and a large hand-drawn X crosses the sheet. The open book carries a
> Python blue wash; the crossed sheet carries a Python yellow wash. No labels.
>
> …then the STYLE BLOCK above.

The slide supplies "permitido" and "no permitido" as headings, so the picture
stays language-neutral and lives in `img/shared/`.

### 4 · `confusion-to-clarity.png` — a divider · any block opener

> Three ducks in a row, left to right, telling one story. The first stands
> under a dense tangled scribble ball and looks confused, with a downturned mouth.
> The second holds one thin thread pulled out of the tangle and looks
> thoughtful, one stick arm bent up to its chin. The third stands beside four
> tidy separate loops of thread, arms raised, smiling. The tangle is navy line
> work only; the four tidy loops carry flat washes, two in Python blue and two in
> Python yellow. No labels.
>
> …then the STYLE BLOCK above.

**Where it goes.** The divider that opens the paradigm block in w02, or the
review block in w01.1. Carries the whole "structure beats mess" argument without
a word.

### 5 · `class-cookies.png` — the cutter and the cookies · w03

> A wide image reading left to right. A duck holds up a star-shaped cookie
> cutter. A navy arrow leads right to a small oven with its door open. A second
> navy arrow leads right to three finished star cookies cooling on a wire rack,
> each decorated differently. The cutter is navy outline only; the three cookies
> carry flat washes, the first Python blue, the second Python yellow, the third
> half of each. No labels.
>
> …then the STYLE BLOCK above.

Unlabelled on purpose. The drawn `class-object` figure already carries the words
`clase`, `__init__` and `objetos`; this is the warmer version for the divider or
the concept slide, with the caption doing the naming.

### 6 · `cover-desk.png` — a quiet band · covers and closing slides

> A hand-drawn still life seen slightly from above: an open laptop at an angle
> with a few squiggles suggesting code on the screen, a coffee cup beside it, a
> small rubber duck sitting on the desk, and a closed notebook with a pencil
> lying on top. Nothing is labelled. The duck carries a flat Python yellow wash
> and the laptop screen a soft Python blue wash; everything else is navy outline
> on off-white.
>
> …then the STYLE BLOCK above.

**Where it goes.** A band across the bottom of a cover, or the closing slide.
Reusable across every deck in the course, both languages.

---

## When the files arrive

```bash
python -m kit.build python
python -m kit.lint  python
```

Place one from a lesson with the `figure` layout:

```yaml
- figure:
    eyebrow: Método de depuración
    title: Explícaselo al pato
    image: img/shared/duck.png
    caption: Verbalizar obliga a revisar las suposiciones que al leer se saltan
    alt: Un estudiante lee su código en voz alta a un pato de hule
```

A slide pointing at a file that is not there still builds: the layout draws a
placeholder box with the filename in it, so a missing picture never blocks a
rebuild.

## If a prompt disappoints

Tell me which one and what went wrong. Most of these can be drawn instead: the
engine in `kit/doodle.py` now has a duck with four moods and four wing
positions, plus speech bubbles and lightbulbs, all in the deck palette. The trade
is warmth for precision, and for anything with a label in it, precision usually
wins.
