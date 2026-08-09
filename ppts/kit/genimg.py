"""Generate the course illustrations with the Gemini image models.

Hand-drawn doodle diagrams, drawn in the deck palette so they sit on a slide
instead of looking pasted in. The style block is fixed and shared by every image,
which is what keeps a sixteen-week series looking like one series.

    python -m kit.genimg --list                 # what exists and who uses it
    python -m kit.genimg slicing --lang es      # one image
    python -m kit.genimg --all --lang es        # the whole catalogue
    python -m kit.genimg slicing --print-prompt # the prompt, without calling the API
    python -m kit.genimg --catalogue > IMAGES.md

Images land in ``ppts/img/<lang>/<id>.png``, outside any one subject, because
most of them explain a language feature rather than a lesson and get reused.

The API key comes from GEMINI_API_KEY. A VS Code window opened before the
variable was set will not have inherited it, so the Windows User scope is read
directly as a fallback.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

# The deck palette, restated for the prompt. Kept in sync with tokens.PYTHON.
INK, BLUE, YELLOW, PAPER = '#0B1B3A', '#3776AB', '#FFD43B', '#F7F8FA'

STYLE = f"""
Style, identical for every image in this series: hand-drawn doodle sketch, loose
and imperfect strokes, as if drawn with a fine-liner. Line art only in deep navy
{INK}, never black. Flat colour washes used sparingly behind a few elements, only
two accent colours: a muted Python blue {BLUE} and a soft Python yellow {YELLOW}.
Plain off-white {PAPER} background, no texture, no paper grain, no spiral binding,
no outer frame. Generous white space. No shading, no gradients, no 3D, no
photorealism, no drop shadows. Clean, airy, educational whiteboard feel. All
labels in sketchy handwritten lettering, spelled exactly as given.
""".strip()


# ── prompt shapes, so the diagrams stay consistent with each other
def hub(centre: str, spokes: list[tuple[str, str]]) -> str:
    items = '\n'.join(f'- {icon}, labelled "{label}"' for icon, label in spokes)
    return (f'A doodle diagram. Center: a hand-drawn circle labelled "{centre}" in '
            f'sketchy handwritten capitals, with short radiating rays around it.\n\n'
            f'{len(spokes)} wavy hand-drawn connector lines run outward from the '
            f'centre, each ending in a small doodle icon with a handwritten label '
            f'beneath it:\n{items}\n\n{STYLE}')


def flow(steps: list[tuple[str, str]], caption: str = '') -> str:
    items = '\n'.join(f'{i + 1}. {icon}, labelled "{label}"'
                      for i, (icon, label) in enumerate(steps))
    tail = f'\nA short handwritten caption underneath reads "{caption}".' if caption else ''
    return (f'A doodle diagram: {len(steps)} hand-drawn boxes in a horizontal row, '
            f'joined left to right by wavy hand-drawn arrows.\n{items}{tail}\n\n{STYLE}')


def split(left_title: str, left: str, right_title: str, right: str,
          caption: str = '') -> str:
    tail = f'\nA handwritten caption underneath reads "{caption}".' if caption else ''
    return (f'A doodle diagram in two halves separated by a wavy vertical hand-drawn '
            f'line.\nLeft half, headed "{left_title}" in handwritten capitals: {left}\n'
            f'Right half, headed "{right_title}" in handwritten capitals: {right}'
            f'{tail}\n\n{STYLE}')


def scene(prompt_es, prompt_en, ratio, about, reuse, used_by, model='pro'):
    return dict(es=prompt_es, en=prompt_en, ratio=ratio, model=model,
                about=about, reuse=reuse, used_by=used_by)


SCENES: dict[str, dict] = {

    # ───────────────────────────────── week 1, orientation
    'course-arc': scene(
        lambda: flow([
            ('a signpost at a trailhead', 'paradigmas'),
            ('a set of building bricks', 'elementos básicos'),
            ('a tree whose branches repeat the trunk shape', 'propiedades'),
            ('a small finished house with a window and a database drum', 'aplicación'),
        ], 'semanas 1 a 17, de por qué existe la POO a una aplicación que corre'),
        lambda: flow([
            ('a signpost at a trailhead', 'paradigms'),
            ('a set of building bricks', 'building blocks'),
            ('a tree whose branches repeat the trunk shape', 'core properties'),
            ('a small finished house with a window and a database drum', 'application'),
        ], 'weeks 1 to 17, from why OOP exists to an application that runs'),
        ratio='21:9',
        about='The four phases of the semester as a path, so the roadmap slide has a '
              'picture to sit next to rather than four more boxes.',
        reuse='Any COM102 session. Swap the four labels and it fits any course whose '
              'syllabus splits into four blocks.',
        used_by=['w01.es', 'w01.en'],
    ),

    'honour-code': scene(
        lambda: split(
            'PERMITIDO',
            'a student at a desk asking a small robot a question; the robot points at '
            'a book and the student writes their own code. A handwritten note reads '
            '"te explica".',
            'NO PERMITIDO',
            'the same robot handing over a finished page of code that the student '
            'copies without reading; a small hand-drawn X sits over the page. A '
            'handwritten note reads "lo escribe por ti".',
            'la prueba es si puedes explicar cualquier línea en el escritorio'),
        lambda: split(
            'ALLOWED',
            'a student at a desk asking a small robot a question; the robot points at '
            'a book and the student writes their own code. A handwritten note reads '
            '"it explains".',
            'NOT ALLOWED',
            'the same robot handing over a finished page of code that the student '
            'copies without reading; a small hand-drawn X sits over the page. A '
            'handwritten note reads "it writes it for you".',
            'the test is whether you can explain any line at your desk'),
        ratio='16:9',
        about='Where the line sits on AI use: a tutor you question versus a ghostwriter '
              'you copy.',
        reuse='Every course in the academy. Language-neutral idea, only the two labels '
              'and the caption change.',
        used_by=['w01.es', 'w01.en'],
    ),

    # ───────────────────────────────── week 1.1, Python review
    'variables-types': scene(
        lambda: (
            'A doodle diagram: a single luggage tag labelled "student_count" tied by a '
            'wavy string. The string is drawn three times in a row, left to right, each '
            'time tied to a differently shaped doodle box: first a box holding "1000" '
            'with a small handwritten "int" beneath, then a box holding "4.99" with '
            '"float" beneath, then a box holding \'"1000"\' with "str" beneath. A '
            'handwritten caption underneath reads "el nombre no tiene tipo, el valor '
            'sí".\n\n' + STYLE),
        lambda: (
            'A doodle diagram: a single luggage tag labelled "student_count" tied by a '
            'wavy string. The string is drawn three times in a row, left to right, each '
            'time tied to a differently shaped doodle box: first a box holding "1000" '
            'with a small handwritten "int" beneath, then a box holding "4.99" with '
            '"float" beneath, then a box holding \'"1000"\' with "str" beneath. A '
            'handwritten caption underneath reads "the name has no type, the value '
            'does".\n\n' + STYLE),
        ratio='21:9',
        about='Dynamic typing: the label stays put while the thing it is tied to changes '
              'shape.',
        reuse='Any dynamically typed language. For C# or C++ it becomes the counter-'
              'example, so the same drawing works with a crossed-out third box.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'slicing': scene(
        lambda: (
            'A doodle diagram: the word "PYTHON" drawn as six square hand-drawn tiles in '
            'a row, one letter per tile. Above the tiles, a hand-drawn ruler numbers '
            'them 0 1 2 3 4 5. Below the tiles, a second ruler numbers them -6 -5 -4 -3 '
            '-2 -1. A curly hand-drawn bracket spans the first three tiles with a '
            'handwritten label "[0:3]", and a small arrow points at the boundary after '
            'the third tile with a handwritten note "el segundo índice no entra".\n\n'
            + STYLE),
        lambda: (
            'A doodle diagram: the word "PYTHON" drawn as six square hand-drawn tiles in '
            'a row, one letter per tile. Above the tiles, a hand-drawn ruler numbers '
            'them 0 1 2 3 4 5. Below the tiles, a second ruler numbers them -6 -5 -4 -3 '
            '-2 -1. A curly hand-drawn bracket spans the first three tiles with a '
            'handwritten label "[0:3]", and a small arrow points at the boundary after '
            'the third tile with a handwritten note "the second index is excluded".\n\n'
            + STYLE),
        ratio='21:9',
        about='Why course[0:3] returns three characters, and how negative indexing lines '
              'up with positive.',
        reuse='Strings and lists share the rule, so this one drawing serves the string '
              'slide and the list slide.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'short-circuit': scene(
        lambda: (
            'A doodle diagram: a corridor with two hand-drawn gates in a row. A small '
            'walking figure approaches. The first gate is labelled "datos" and is shut, '
            'with a hand-drawn X on it. The second gate, labelled "datos[0]", stays '
            'closed and untouched, with a dashed line showing the figure never reaches '
            'it. A handwritten caption reads "si la primera es falsa, la segunda ni se '
            'evalúa".\n\n' + STYLE),
        lambda: (
            'A doodle diagram: a corridor with two hand-drawn gates in a row. A small '
            'walking figure approaches. The first gate is labelled "data" and is shut, '
            'with a hand-drawn X on it. The second gate, labelled "data[0]", stays '
            'closed and untouched, with a dashed line showing the figure never reaches '
            'it. A handwritten caption reads "if the first is false, the second is never '
            'evaluated".\n\n' + STYLE),
        ratio='16:9',
        about='Short-circuit evaluation, and why it is what makes the guard idiom safe.',
        reuse='Identical in C#, C++ and VBA. Change only the two gate labels.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'scope': scene(
        lambda: (
            'A doodle diagram: a large hand-drawn rounded rectangle labelled "global", '
            'containing a smaller rounded rectangle labelled "función". Inside the small '
            'box sits a doodle jar labelled "local" holding two little labelled balls. '
            'An arrow starting outside the small box tries to reach the jar and is '
            'stopped by a hand-drawn X, with a handwritten note beside it reading '
            '"NameError".\n\n' + STYLE),
        lambda: (
            'A doodle diagram: a large hand-drawn rounded rectangle labelled "global", '
            'containing a smaller rounded rectangle labelled "function". Inside the small '
            'box sits a doodle jar labelled "local" holding two little labelled balls. '
            'An arrow starting outside the small box tries to reach the jar and is '
            'stopped by a hand-drawn X, with a handwritten note beside it reading '
            '"NameError".\n\n' + STYLE),
        ratio='16:9',
        about='Local versus global scope, and what exactly raises NameError.',
        reuse='Week 3 reuses it verbatim: swap the jar label for "self" and the same '
              'drawing explains why an attribute survives a call and a local does not.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'collections': scene(
        lambda: flow([
            ('a numbered shopping list on a notepad', 'lista'),
            ('the same notepad with a padlock through it', 'tupla'),
            ('a bag of distinct shapes, one duplicate crossed out', 'conjunto'),
            ('a card index where each tab points to its own drawer', 'diccionario'),
        ], 'ordenada · inmutable · sin repetidos · por llave'),
        lambda: flow([
            ('a numbered shopping list on a notepad', 'list'),
            ('the same notepad with a padlock through it', 'tuple'),
            ('a bag of distinct shapes, one duplicate crossed out', 'set'),
            ('a card index where each tab points to its own drawer', 'dictionary'),
        ], 'ordered · immutable · no duplicates · by key'),
        ratio='21:9',
        about='The four containers side by side, each drawn as the property that '
              'distinguishes it.',
        reuse='The comparison table on the same slide gives the syntax; this gives the '
              'intuition. Works for any language with the same four structures.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'exceptions': scene(
        lambda: (
            'A doodle diagram: a hand-drawn box labelled "try" with a crack in one side. '
            'Two labelled paper darts fly out of the crack, one reading "ValueError" and '
            'one reading "ZeroDivisionError". Below them, two open doodle baskets each '
            'catch one dart, labelled "except ValueError" and "except '
            'ZeroDivisionError". To the right, a clean straight arrow leaves the box '
            'without cracking it and reaches a small flag labelled "else".\n\n' + STYLE),
        lambda: (
            'A doodle diagram: a hand-drawn box labelled "try" with a crack in one side. '
            'Two labelled paper darts fly out of the crack, one reading "ValueError" and '
            'one reading "ZeroDivisionError". Below them, two open doodle baskets each '
            'catch one dart, labelled "except ValueError" and "except '
            'ZeroDivisionError". To the right, a clean straight arrow leaves the box '
            'without cracking it and reaches a small flag labelled "else".\n\n' + STYLE),
        ratio='16:9',
        about='Why one except per type beats a bare except, and where the else clause '
              'runs.',
        reuse='Week 11 covers exceptions properly; the same drawing opens that session.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    'reference-vs-copy': scene(
        lambda: split(
            'copia = numeros',
            'two luggage tags, one labelled "numeros" and one labelled "copia", both '
            'tied by wavy strings to the same single doodle box holding "[1, 2, 3, 4]".',
            'copia = numeros.copy()',
            'two luggage tags with the same two labels, each tied to its own separate '
            'doodle box, one holding "[1, 2, 3]" and the other "[1, 2, 3, 4]".',
            'el signo igual copia la referencia, no el contenido'),
        lambda: split(
            'copy = numbers',
            'two luggage tags, one labelled "numbers" and one labelled "copy", both tied '
            'by wavy strings to the same single doodle box holding "[1, 2, 3, 4]".',
            'copy = numbers.copy()',
            'two luggage tags with the same two labels, each tied to its own separate '
            'doodle box, one holding "[1, 2, 3]" and the other "[1, 2, 3, 4]".',
            'the equals sign copies the reference, not the contents'),
        ratio='21:9',
        about='Aliasing. The single most common surprise in the review quiz, drawn.',
        reuse='Week 3 reuses it for the shared class attribute, which is the same bug '
              'wearing a class costume.',
        used_by=['w01.1.es', 'w01.1.en'],
    ),

    # ───────────────────────────────── week 2, paradigms
    'paradigms': scene(
        lambda: hub('PROGRAMACIÓN', [
            ('interlocking gears', 'imperativo'),
            ('two stacked blocks marked with a small f', 'estructurado'),
            ('a character profile card with a face and two bullet lines', 'orientado a objetos'),
            ('a funnel turning a list into one arrow', 'funcional'),
            ('a lightning bolt hitting a button', 'orientado a eventos'),
            ('four interlocking lego bricks', 'visual'),
        ]),
        lambda: hub('PROGRAMMING', [
            ('interlocking gears', 'imperative'),
            ('two stacked blocks marked with a small f', 'structured'),
            ('a character profile card with a face and two bullet lines', 'object-oriented'),
            ('a funnel turning a list into one arrow', 'functional'),
            ('a lightning bolt hitting a button', 'event-driven'),
            ('four interlocking lego bricks', 'visual'),
        ]),
        ratio='21:9',
        about='The paradigm map. Object orientation is one of six, not the only way.',
        reuse='Opens the paradigm session of every language course in the academy, '
              'unchanged.',
        used_by=['w02.es', 'w02.en'],
    ),

    'parallel-lists': scene(
        lambda: split(
            'CUATRO LISTAS',
            'four horizontal rows of doodle boxes stacked vertically, labelled '
            '"nombres", "notas", "carrera", "semestre". One box is being torn out of the '
            'top row, and the rows below it are drawn shifted sideways so the columns no '
            'longer line up. A small hand-drawn X marks the mismatch.',
            'UN OBJETO',
            'three small doodle cards, each holding all four fields together as tidy '
            'handwritten lines. One whole card is being torn out and the other two stay '
            'intact and aligned.',
            'el mismo dato, y solo uno de los dos se desalinea al borrar'),
        lambda: split(
            'FOUR LISTS',
            'four horizontal rows of doodle boxes stacked vertically, labelled "names", '
            '"grades", "degree", "term". One box is being torn out of the top row, and '
            'the rows below it are drawn shifted sideways so the columns no longer line '
            'up. A small hand-drawn X marks the mismatch.',
            'ONE OBJECT',
            'three small doodle cards, each holding all four fields together as tidy '
            'handwritten lines. One whole card is being torn out and the other two stay '
            'intact and aligned.',
            'the same data, and only one of the two goes out of step when you delete'),
        ratio='21:9',
        about='The failure that made object orientation worth the extra lines: parallel '
              'lists drifting out of sync.',
        reuse='This is the argument of the whole paradigm session. Works for any '
              'language, since the failure is structural rather than syntactic.',
        used_by=['w02.es', 'w02.en'],
    ),

    # ───────────────────────────────── week 3, classes and objects
    'class-object': scene(
        lambda: flow([
            ('a blueprint sheet showing a dashed cookie-cutter outline', 'clase'),
            ('a small factory with a funnel on top', '__init__'),
            ('three finished cookies, each with different icing', 'objetos'),
        ], 'un molde, muchas galletas, cada una con su propio estado'),
        lambda: flow([
            ('a blueprint sheet showing a dashed cookie-cutter outline', 'class'),
            ('a small factory with a funnel on top', '__init__'),
            ('three finished cookies, each with different icing', 'objects'),
        ], 'one cutter, many cookies, each with its own state'),
        ratio='21:9',
        about='Class against object, with the constructor drawn as the step between '
              'them.',
        reuse='The cookie-cutter analogy is already in docs/02-oop.md, so the drawing '
              'and the written notes reinforce each other.',
        used_by=['w03.es', 'w03.en'],
    ),

    'class-vs-instance': scene(
        lambda: split(
            'EN EL CUERPO DE LA CLASE',
            'a single doodle basket labelled "productos" drawn once, with wavy strings '
            'running from it to two separate little carts labelled "a" and "b". One item '
            'dropped in the basket appears for both carts.',
            'DENTRO DE __init__',
            'two little carts labelled "a" and "b", each carrying its own separate '
            'basket labelled "productos". An item dropped in one basket stays there.',
            'lo que se declara en la clase se comparte, casi siempre sin querer'),
        lambda: split(
            'IN THE CLASS BODY',
            'a single doodle basket labelled "items" drawn once, with wavy strings '
            'running from it to two separate little carts labelled "a" and "b". One item '
            'dropped in the basket appears for both carts.',
            'INSIDE __init__',
            'two little carts labelled "a" and "b", each carrying its own separate '
            'basket labelled "items". An item dropped in one basket stays there.',
            'what you declare in the class body is shared, almost always by accident'),
        ratio='21:9',
        about='The shared mutable class attribute, which is the quiz answer of week 3.',
        reuse='Same mechanism as reference-vs-copy from the review session, so showing '
              'both back to back lands the point.',
        used_by=['w03.es', 'w03.en'],
    ),

    'duck': scene(
        lambda: (
            'A doodle scene: a student sits at a desk reading lines of code out loud to '
            'a rubber duck placed on the desk. Small handwritten speech marks come out '
            'of the student. A lightbulb doodle appears above the student\'s head. A '
            'handwritten label under the duck reads "rubber duck debugging".\n\n'
            + STYLE),
        lambda: (
            'A doodle scene: a student sits at a desk reading lines of code out loud to '
            'a rubber duck placed on the desk. Small handwritten speech marks come out '
            'of the student. A lightbulb doodle appears above the student\'s head. A '
            'handwritten label under the duck reads "rubber duck debugging".\n\n'
            + STYLE),
        ratio='16:9',
        about='The debugging method the course is named after, and the reason the duck '
              'is the academy mark.',
        reuse='Any session with a lab. It is the one image that belongs to the whole '
              'programme rather than to a topic.',
        used_by=['w01.1.es', 'w01.1.en', 'w03.es', 'w03.en'],
    ),
}

MODELS = {
    # text inside the picture survives far better on the pro model
    'pro': 'gemini-3-pro-image',
    'flash': 'gemini-3.1-flash-image',
    'nano': 'gemini-2.5-flash-image',
}


def api_key() -> str:
    key = os.environ.get('GEMINI_API_KEY') or os.environ.get('GOOGLE_API_KEY')
    if not key and os.name == 'nt':
        out = subprocess.run(
            ['powershell', '-NoProfile', '-Command',
             "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')"],
            capture_output=True, text=True)
        key = out.stdout.strip()
    if not key:
        sys.exit('GEMINI_API_KEY not found in the environment or the Windows User scope')
    return key


def generate(prompt, out_path, ratio='21:9', model='pro', overwrite=False):
    from google import genai
    from google.genai import types

    if os.path.exists(out_path) and not overwrite:
        print(f'  skip {os.path.basename(out_path)} (already there, --overwrite replaces)')
        return out_path

    client = genai.Client(api_key=api_key())
    response = client.models.generate_content(
        model=MODELS.get(model, model),
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=['IMAGE'],
            image_config=types.ImageConfig(aspect_ratio=ratio),
        ),
    )
    for part in response.parts:
        if part.inline_data:
            os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
            part.as_image().save(out_path)
            print(f'  wrote {out_path}  ({ratio}, {MODELS.get(model, model)})')
            return out_path
    raise RuntimeError(f'no image came back for {out_path}')


def catalogue() -> str:
    """The reuse documentation, as markdown."""
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lines = [
        '# Illustration catalogue', '',
        'Doodle diagrams for the course decks, generated by `kit/genimg.py` with a',
        'style block shared by every image. They live in `ppts/img/<lang>/` rather than',
        'inside a subject folder, because most of them explain a language feature and',
        'get reused across sessions and courses.', '',
        '```bash',
        'python -m kit.genimg --all --lang es      # fill every missing image',
        'python -m kit.genimg slicing --lang en    # redo just one',
        'python -m kit.genimg slicing --print-prompt',
        '```', '',
        f'{len(SCENES)} images. A slide referencing one that has not been generated yet',
        'still builds: the layout draws a placeholder with the filename in it.', '',
        '| Image | Ratio | Used by | Files |', '|---|---|---|---|',
    ]
    for name, spec in SCENES.items():
        have = [lang for lang in ('es', 'en')
                if os.path.exists(os.path.join(root, 'img', lang, f'{name}.png'))]
        state = ', '.join(have) if have else 'not generated'
        lines.append(f'| `{name}` | {spec["ratio"]} | '
                     f'{", ".join(spec["used_by"])} | {state} |')
    lines += ['', '---', '']
    for name, spec in SCENES.items():
        lines += [
            f'## `{name}`', '',
            f'**Shows.** {spec["about"]}', '',
            f'**Reuse.** {spec["reuse"]}', '',
            f'**Ratio** {spec["ratio"]} · **model** `{MODELS[spec["model"]]}` · '
            f'**used by** {", ".join(spec["used_by"])}', '',
            '<details><summary>Prompt (es)</summary>', '',
            '```', spec['es'](), '```', '', '</details>', '',
        ]
    return '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('scene', nargs='?')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--catalogue', action='store_true', help='write IMAGES.md to stdout')
    ap.add_argument('--lang', default='es', choices=('es', 'en'))
    ap.add_argument('--out')
    ap.add_argument('--outdir')
    ap.add_argument('--model', choices=list(MODELS))
    ap.add_argument('--ratio')
    ap.add_argument('--overwrite', action='store_true')
    ap.add_argument('--print-prompt', action='store_true')
    a = ap.parse_args(argv)

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if a.catalogue:
        print(catalogue())
        return 0

    if a.list or (not a.scene and not a.all):
        print(f'{"image":<20}{"ratio":>7}  {"model":<8} used by')
        for name, spec in SCENES.items():
            print(f'  {name:<18}{spec["ratio"]:>7}  {spec["model"]:<8} '
                  f'{", ".join(spec["used_by"])}')
        return 0

    outdir = a.outdir or os.path.join(root, 'img', a.lang)
    names = list(SCENES) if a.all else [a.scene]
    failed = []
    for name in names:
        if name not in SCENES:
            sys.exit(f'unknown image {name!r}. Known: {", ".join(SCENES)}')
        spec = SCENES[name]
        prompt = spec[a.lang]()
        if a.print_prompt:
            print(f'\n===== {name} ({a.lang}) =====\n{prompt}')
            continue
        out = a.out if (a.out and not a.all) else os.path.join(outdir, f'{name}.png')
        try:
            generate(prompt, out, a.ratio or spec['ratio'], a.model or spec['model'],
                     a.overwrite)
        except Exception as e:
            failed.append((name, f'{type(e).__name__}: {str(e)[:90]}'))
            print(f'  FAILED {name}: {type(e).__name__}')
    if failed:
        print(f'\n{len(failed)} of {len(names)} failed:')
        for name, err in failed:
            print(f'  {name}: {err}')
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
