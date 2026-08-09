"""Flowchart figures for the notebooks, as inline SVG.

Colab does not render mermaid in a markdown cell, so a diagram has to arrive as
an image. A base64 data URI costs no network call, no package and no code cell:
the markdown holds the whole picture.

The palette is the deck's, and every figure paints its own light background so it
still reads when Colab is in dark mode.
"""
import base64

NAVY = "#0B1B3A"
PAPER = "#F7F8FA"
INK = "#0F172A"
MUTED = "#5B6B84"
BORDER = "#DBE3EF"
BLUE = "#2B5F8F"
ACCENT = "#8A6A00"

MONO = "ui-monospace, 'JetBrains Mono', 'Courier New', monospace"
SANS = "'Inter Tight', Inter, Arial, sans-serif"


def data_uri(svg):
    """An <svg> string as a markdown-embeddable data URI."""
    packed = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{packed}"


def figure(svg, alt):
    """A whole markdown image line, ready to drop into a cell."""
    return f"![{alt}]({data_uri(svg)})"


# ────────────────────────────────────────────────────────────── the primitives

def _oval(x, y, w, h, text):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" '
            f'fill="{NAVY}"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{PAPER}" '
            f'font-family="{SANS}" font-size="15" font-weight="600" '
            f'text-anchor="middle">{text}</text>')


def _rect(x, y, w, h, text):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
            f'fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="14" text-anchor="middle">{text}</text>')


def _para(x, y, w, h, text):
    """Parallelogram: input or output."""
    slant = 14
    pts = f"{x + slant},{y} {x + w},{y} {x + w - slant},{y + h} {x},{y + h}"
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{MUTED}" '
            f'stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13.5" text-anchor="middle">{text}</text>')


def _diamond(cx, cy, w, h, text):
    pts = f"{cx},{cy - h / 2} {cx + w / 2},{cy} {cx},{cy + h / 2} {cx - w / 2},{cy}"
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{ACCENT}" '
            f'stroke-width="2"/>'
            f'<text x="{cx}" y="{cy + 5}" fill="{INK}" font-family="{MONO}" '
            f'font-size="13.5" text-anchor="middle">{text}</text>')


def _subroutine(x, y, w, h, text):
    """Predefined process: a step defined somewhere else. A function call."""
    bar = 12
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
            f'fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>'
            f'<line x1="{x + bar}" y1="{y}" x2="{x + bar}" y2="{y + h}" '
            f'stroke="{BLUE}" stroke-width="2"/>'
            f'<line x1="{x + w - bar}" y1="{y}" x2="{x + w - bar}" y2="{y + h}" '
            f'stroke="{BLUE}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13.5" text-anchor="middle">{text}</text>')


def _connector(cx, cy, r, text):
    """On-page connector: the chart continues at the circle with the same letter."""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF" '
            f'stroke="{ACCENT}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy + 6}" fill="{ACCENT}" font-family="{SANS}" '
            f'font-size="16" font-weight="700" text-anchor="middle">{text}</text>')


def _offpage(x, y, w, h, text):
    """Off-page connector: it continues on another sheet."""
    tip = h * 0.35
    pts = (f"{x},{y} {x + w},{y} {x + w},{y + h - tip} "
           f"{x + w / 2},{y + h} {x},{y + h - tip}")
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{ACCENT}" '
            f'stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 2}" fill="{ACCENT}" '
            f'font-family="{SANS}" font-size="14" font-weight="700" '
            f'text-anchor="middle">{text}</text>')


def _prep(x, y, w, h, text):
    """Preparation: setting up a loop. Where the counter gets initialised."""
    cut = 22
    pts = (f"{x + cut},{y} {x + w - cut},{y} {x + w},{y + h / 2} "
           f"{x + w - cut},{y + h} {x + cut},{y + h} {x},{y + h / 2}")
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{BLUE}" '
            f'stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _database(x, y, w, h, text):
    """Stored data: a table, a file that persists, a database."""
    ry = 9
    return (f'<path d="M {x} {y + ry} '
            f'A {w / 2} {ry} 0 0 1 {x + w} {y + ry} '
            f'L {x + w} {y + h - ry} '
            f'A {w / 2} {ry} 0 0 1 {x} {y + h - ry} Z" '
            f'fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>'
            f'<path d="M {x} {y + ry} A {w / 2} {ry} 0 0 0 {x + w} {y + ry}" '
            f'fill="none" stroke="{MUTED}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 8}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _document(x, y, w, h, text):
    """Document: output meant to be read by a person. A report, a printout."""
    wave = 12
    return (f'<path d="M {x} {y} L {x + w} {y} L {x + w} {y + h - wave} '
            f'Q {x + w * 0.75} {y + h + wave * 0.6} {x + w / 2} {y + h - wave / 2} '
            f'Q {x + w * 0.25} {y + h - wave * 1.6} {x} {y + h - wave} Z" '
            f'fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 2}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _manual_input(x, y, w, h, text):
    """Manual input: somebody types it. This is input()."""
    slope = 12
    pts = f"{x},{y + slope} {x + w},{y} {x + w},{y + h} {x},{y + h}"
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{MUTED}" '
            f'stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 7}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _display(x, y, w, h, text):
    """Display: it goes to a screen. This is print()."""
    curve = 18
    return (f'<path d="M {x + curve} {y} L {x + w - curve} {y} '
            f'Q {x + w} {y + h / 2} {x + w - curve} {y + h} '
            f'L {x + curve} {y + h} '
            f'Q {x} {y + h / 2} {x + curve} {y} Z" '
            f'fill="#FFFFFF" stroke="{MUTED}" stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _manual_op(x, y, w, h, text):
    """Manual operation: a step a person does, not the machine."""
    cut = 18
    pts = f"{x},{y} {x + w},{y} {x + w - cut},{y + h} {x + cut},{y + h}"
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="{MUTED}" '
            f'stroke-width="2"/>'
            f'<text x="{x + w / 2}" y="{y + h / 2 + 5}" fill="{INK}" '
            f'font-family="{MONO}" font-size="13" text-anchor="middle">{text}</text>')


def _arrow(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MUTED}" '
            f'stroke-width="2" marker-end="url(#tip)"/>')


def _elbow(points):
    """A polyline through the given points, arrowhead on the last leg."""
    d = " ".join(f"{x},{y}" for x, y in points)
    return (f'<polyline points="{d}" fill="none" stroke="{MUTED}" '
            f'stroke-width="2" marker-end="url(#tip)"/>')


def _label(x, y, text, anchor="middle", color=None):
    return (f'<text x="{x}" y="{y}" fill="{color or MUTED}" font-family="{SANS}" '
            f'font-size="12.5" font-weight="600" text-anchor="{anchor}">{text}</text>')


def _canvas(width, height, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
            f'height="{height}" viewBox="0 0 {width} {height}" '
            f'role="img" aria-label="{title}">'
            f'<defs><marker id="tip" viewBox="0 0 10 10" refX="9" refY="5" '
            f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{MUTED}"/></marker></defs>'
            f'<rect width="{width}" height="{height}" fill="{PAPER}" rx="8"/>'
            f'{body}</svg>')


# ─────────────────────────────────────────────────────────── the actual figures

def bonus_flowchart(lang):
    """The annual bonus algorithm from week 2, as a flowchart."""
    t = {
        "es": {
            "start": "INICIO", "end": "FIN",
            "read": "LEER sueldo, antiguedad, evaluacion",
            "write": "ESCRIBIR bono",
            "d1": "¿antiguedad &lt; 12?", "d2": "¿evaluacion &gt;= 4.5?",
            "a1": "bono = 0", "a2": "bono = sueldo * 0.20", "a3": "bono = sueldo * 0.10",
            "yes": "Sí", "no": "No",
            "title": "Diagrama de flujo del cálculo del bono anual",
        },
        "en": {
            "start": "START", "end": "END",
            "read": "READ salary, tenure, review",
            "write": "WRITE bonus",
            "d1": "tenure &lt; 12?", "d2": "review &gt;= 4.5?",
            "a1": "bonus = 0", "a2": "bonus = salary * 0.20", "a3": "bonus = salary * 0.10",
            "yes": "Yes", "no": "No",
            "title": "Flowchart of the annual bonus calculation",
        },
    }[lang]

    W, H = 700, 620
    cx = 230                      # main column
    rx = 500                      # right-hand branch column
    merge = 660                   # where the branches come back down

    body = [
        _oval(cx - 60, 20, 120, 38, t["start"]),
        _arrow(cx, 58, cx, 82),

        _para(cx - 165, 84, 330, 40, t["read"]),
        _arrow(cx, 124, cx, 152),

        _diamond(cx, 190, 260, 76, t["d1"]),
        _label(cx + 145, 185, t["yes"]),
        _arrow(cx + 130, 190, rx - 90, 190),
        _rect(rx - 90, 170, 180, 40, t["a1"]),

        _label(cx + 14, 246, t["no"], anchor="start"),
        _arrow(cx, 228, cx, 262),

        _diamond(cx, 300, 260, 76, t["d2"]),
        _label(cx + 145, 295, t["yes"]),
        _arrow(cx + 130, 300, rx - 90, 300),
        _rect(rx - 90, 280, 180, 40, t["a2"]),

        _label(cx + 14, 356, t["no"], anchor="start"),
        _arrow(cx, 338, cx, 372),

        _rect(cx - 90, 372, 180, 40, t["a3"]),

        # the three branches meet
        _elbow([(rx + 90, 190), (merge, 190), (merge, 460), (cx, 460), (cx, 484)]),
        _elbow([(rx + 90, 300), (merge - 20, 300), (merge - 20, 452), (cx, 452)]),
        _arrow(cx, 412, cx, 484),

        _para(cx - 110, 486, 220, 40, t["write"]),
        _arrow(cx, 526, cx, 552),

        _oval(cx - 60, 554, 120, 38, t["end"]),
    ]
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


def symbols_figure(lang):
    """The four flowchart symbols and what each one means."""
    t = {
        "es": {
            "title": "Los cuatro símbolos de un diagrama de flujo",
            "rows": [("INICIO · FIN", "Óvalo: dónde empieza y dónde acaba"),
                     ("LEER · ESCRIBIR", "Paralelogramo: entra o sale un dato"),
                     ("bono = sueldo * 0.20", "Rectángulo: un cálculo o una asignación"),
                     ("¿antiguedad &lt; 12?", "Rombo: una decisión con dos salidas")],
        },
        "en": {
            "title": "The four flowchart symbols",
            "rows": [("START · END", "Oval: where it begins and where it ends"),
                     ("READ · WRITE", "Parallelogram: a value goes in or comes out"),
                     ("bonus = salary * 0.20", "Rectangle: a calculation or an assignment"),
                     ("tenure &lt; 12?", "Diamond: a decision with two exits")],
        },
    }[lang]

    W, H = 700, 330
    body = []
    y = 26
    shapes = [_oval, _para, _rect, None]
    for i, (label, meaning) in enumerate(t["rows"]):
        if i == 0:
            body.append(_oval(30, y, 240, 44, label))
        elif i == 1:
            body.append(_para(30, y, 240, 44, label))
        elif i == 2:
            body.append(_rect(30, y, 240, 44, label))
        else:
            body.append(_diamond(150, y + 22, 240, 60, label))
        body.append(f'<text x="300" y="{y + 28}" fill="{MUTED}" font-family="{SANS}" '
                    f'font-size="14">{meaning}</text>')
        y += 76
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


def symbol_catalogue(lang):
    """Every flowchart symbol this course uses, beyond the basic four."""
    t = {
        "es": {
            "title": "El resto de los símbolos de un diagrama de flujo",
            "heads": ["Los cuatro básicos", "Los que faltan"],
            "basic": [("INICIO · FIN", "Terminal"),
                      ("LEER · ESCRIBIR", "Entrada y salida"),
                      ("bono = sueldo * .2", "Proceso"),
                      ("¿antiguedad &lt; 12?", "Decisión")],
            "extra": [("calcular_bono()", "Proceso predefinido: una función que ya escribiste"),
                      ("i = 0, i &lt; n, i++", "Preparación: donde arranca un ciclo"),
                      ("A", "Conector: el diagrama sigue en el círculo con la misma letra"),
                      ("pág. 2", "Conector fuera de página: sigue en otra hoja"),
                      ("ventas.csv", "Datos almacenados: un archivo o una tabla"),
                      ("Reporte", "Documento: una salida hecha para que alguien la lea"),
                      ("sueldo", "Entrada manual: alguien lo teclea. Esto es input()"),
                      ("total", "Despliegue: va a la pantalla. Esto es print()"),
                      ("Autorizar", "Operación manual: la hace una persona, no la máquina")],
        },
        "en": {
            "title": "The rest of the flowchart symbols",
            "heads": ["The basic four", "The ones missing"],
            "basic": [("START · END", "Terminal"),
                      ("READ · WRITE", "Input and output"),
                      ("bonus = salary * .2", "Process"),
                      ("tenure &lt; 12?", "Decision")],
            "extra": [("compute_bonus()", "Predefined process: a function you already wrote"),
                      ("i = 0, i &lt; n, i++", "Preparation: where a loop is set up"),
                      ("A", "Connector: the chart continues at the circle with the same letter"),
                      ("page 2", "Off-page connector: it continues on another sheet"),
                      ("sales.csv", "Stored data: a file or a table"),
                      ("Report", "Document: output made for a person to read"),
                      ("salary", "Manual input: somebody types it. This is input()"),
                      ("total", "Display: it goes to the screen. This is print()"),
                      ("Approve", "Manual operation: a person does it, not the machine")],
        },
    }[lang]

    W, H = 780, 880
    body = [f'<text x="30" y="34" fill="{INK}" font-family="{SANS}" font-size="15" '
            f'font-weight="700">{t["heads"][0]}</text>']

    y = 48
    for i, (label, meaning) in enumerate(t["basic"]):
        if i == 0:
            body.append(_oval(30, y, 210, 40, label))
        elif i == 1:
            body.append(_para(30, y, 210, 40, label))
        elif i == 2:
            body.append(_rect(30, y, 210, 40, label))
        else:
            body.append(_diamond(135, y + 20, 210, 54, label))
        body.append(f'<text x="272" y="{y + 25}" fill="{MUTED}" font-family="{SANS}" '
                    f'font-size="13.5">{meaning}</text>')
        y += 62

    y += 14
    body.append(f'<line x1="30" y1="{y - 22}" x2="{W - 30}" y2="{y - 22}" '
                f'stroke="{BORDER}" stroke-width="1.5"/>')
    body.append(f'<text x="30" y="{y + 4}" fill="{INK}" font-family="{SANS}" '
                f'font-size="15" font-weight="700">{t["heads"][1]}</text>')
    y += 20

    drawers = [_subroutine, _prep, None, _offpage, _database,
               _document, _manual_input, _display, _manual_op]
    for (label, meaning), draw in zip(t["extra"], drawers):
        if draw is None:
            body.append(_connector(135, y + 22, 22, label))
        elif draw is _offpage:
            body.append(_offpage(75, y, 120, 46, label))
        else:
            body.append(draw(30, y, 210, 44, label))
        body.append(f'<text x="272" y="{y + 27}" fill="{MUTED}" font-family="{SANS}" '
                    f'font-size="13.5">{meaning}</text>')
        y += 58

    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


def connector_figure(lang):
    """How a chart too long for one page gets cut with a connector."""
    t = {
        "es": {
            "title": "Cómo se parte un diagrama que ya no cabe",
            "left": "Se corta aquí", "right": "Y sigue aquí",
            "n1": "LEER datos", "n2": "¿válidos?", "n3": "limpiar",
            "n4": "agrupar", "n5": "ESCRIBIR",
            "note": "El círculo no es un paso. Solo dice dónde continúa la línea.",
        },
        "en": {
            "title": "How a chart too long for the page gets cut",
            "left": "It stops here", "right": "And carries on here",
            "n1": "READ data", "n2": "valid?", "n3": "clean",
            "n4": "group", "n5": "WRITE",
            "note": "The circle is not a step. It only says where the line continues.",
        },
    }[lang]

    W, H = 700, 330
    lx, rx = 165, 505
    body = [
        f'<text x="{lx}" y="26" fill="{MUTED}" font-family="{SANS}" font-size="13" '
        f'font-weight="600" text-anchor="middle">{t["left"]}</text>',
        f'<text x="{rx}" y="26" fill="{MUTED}" font-family="{SANS}" font-size="13" '
        f'font-weight="600" text-anchor="middle">{t["right"]}</text>',
        f'<line x1="350" y1="14" x2="350" y2="{H - 14}" stroke="{BORDER}" '
        f'stroke-width="1.5" stroke-dasharray="6 5"/>',

        _para(lx - 85, 44, 170, 38, t["n1"]),
        _arrow(lx, 82, lx, 106),
        _diamond(lx, 140, 170, 58, t["n2"]),
        _arrow(lx, 169, lx, 194),
        _rect(lx - 85, 194, 170, 38, t["n3"]),
        _arrow(lx, 232, lx, 254),
        _connector(lx, 278, 22, "A"),

        _connector(rx, 66, 22, "A"),
        _arrow(rx, 88, rx, 114),
        _rect(rx - 85, 114, 170, 38, t["n4"]),
        _arrow(rx, 152, rx, 176),
        _para(rx - 85, 176, 170, 38, t["n5"]),
        _arrow(rx, 214, rx, 238),
        _oval(rx - 55, 240, 110, 36, "FIN" if lang == "es" else "END"),

        f'<text x="{W / 2}" y="{H - 16}" fill="{MUTED}" font-family="{SANS}" '
        f'font-size="12.5" text-anchor="middle">{t["note"]}</text>',
    ]
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


# ─────────────────────────────────────────────────────────────────────── UML

def _uml_class(x, y, w, name, attrs, methods, dark=False):
    """A UML class box: name, attributes, operations."""
    line_h = 22
    head_h = 34
    a_h = max(len(attrs), 1) * line_h + 10
    m_h = max(len(methods), 1) * line_h + 10
    h = head_h + a_h + m_h
    fill_head = NAVY if dark else "#FFFFFF"
    text_head = PAPER if dark else INK

    parts = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#FFFFFF" '
             f'stroke="{BLUE}" stroke-width="2"/>',
             f'<path d="M {x} {y + 4} q 0 -4 4 -4 L {x + w - 4} {y} q 4 0 4 4 '
             f'L {x + w} {y + head_h} L {x} {y + head_h} Z" fill="{fill_head}" '
             f'stroke="{BLUE}" stroke-width="2"/>',
             f'<text x="{x + w / 2}" y="{y + 22}" fill="{text_head}" '
             f'font-family="{SANS}" font-size="14" font-weight="700" '
             f'text-anchor="middle">{name}</text>',
             f'<line x1="{x}" y1="{y + head_h + a_h}" x2="{x + w}" '
             f'y2="{y + head_h + a_h}" stroke="{BLUE}" stroke-width="2"/>']

    ty = y + head_h + 20
    for a in attrs:
        parts.append(f'<text x="{x + 12}" y="{ty}" fill="{INK}" font-family="{MONO}" '
                     f'font-size="12.5">{a}</text>')
        ty += line_h
    ty = y + head_h + a_h + 20
    for m in methods:
        parts.append(f'<text x="{x + 12}" y="{ty}" fill="{INK}" font-family="{MONO}" '
                     f'font-size="12.5">{m}</text>')
        ty += line_h
    return "".join(parts), h


def _hollow_triangle(cx, cy, size, up=True):
    """The inheritance arrowhead: a hollow triangle pointing at the parent."""
    if up:
        pts = f"{cx},{cy} {cx - size},{cy + size * 1.4} {cx + size},{cy + size * 1.4}"
    else:
        pts = f"{cx},{cy} {cx - size},{cy - size * 1.4} {cx + size},{cy - size * 1.4}"
    return f'<polygon points="{pts}" fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>'


def _filled_diamond(cx, cy, size):
    """Composition: the part cannot live without the whole."""
    pts = f"{cx},{cy} {cx - size},{cy + size * 1.5} {cx},{cy + size * 3} {cx + size},{cy + size * 1.5}"
    return f'<polygon points="{pts}" fill="{BLUE}" stroke="{BLUE}" stroke-width="2"/>'


def uml_class_figure(lang):
    """A class box and an inheritance relationship, for the OOP weeks."""
    t = {
        "es": {
            "title": "Una clase en UML, y la herencia",
            "parent": "Empleado",
            "p_attrs": ["- nombre: str", "- sueldo: float"],
            "p_meths": ["+ pagar(): float", "+ __str__(): str"],
            "child": "Gerente",
            "c_attrs": ["- equipo: list"],
            "c_meths": ["+ pagar(): float"],
            "n_head": "Nombre de la clase",
            "n_attr": "Atributos: lo que el objeto guarda",
            "n_meth": "Métodos: lo que el objeto sabe hacer",
            "n_arrow": "El triángulo hueco apunta al padre",
            "n_vis": "- privado   + público",
        },
        "en": {
            "title": "A UML class, and inheritance",
            "parent": "Employee",
            "p_attrs": ["- name: str", "- salary: float"],
            "p_meths": ["+ pay(): float", "+ __str__(): str"],
            "child": "Manager",
            "c_attrs": ["- team: list"],
            "c_meths": ["+ pay(): float"],
            "n_head": "The class name",
            "n_attr": "Attributes: what the object holds",
            "n_meth": "Methods: what the object knows how to do",
            "n_arrow": "The hollow triangle points at the parent",
            "n_vis": "- private   + public",
        },
    }[lang]

    W, H = 700, 430
    cx = 210
    parent, ph = _uml_class(cx - 110, 20, 220, t["parent"], t["p_attrs"], t["p_meths"], dark=True)
    child, _ = _uml_class(cx - 110, 280, 220, t["child"], t["c_attrs"], t["c_meths"])

    body = [
        parent, child,
        _hollow_triangle(cx, 20 + ph + 4, 11, up=True),
        f'<line x1="{cx}" y1="{20 + ph + 4 + 15}" x2="{cx}" y2="280" stroke="{BLUE}" '
        f'stroke-width="2"/>',
        f'<text x="{cx + 18}" y="{20 + ph + 42}" fill="{MUTED}" font-family="{SANS}" '
        f'font-size="12.5">{t["n_arrow"]}</text>',

        # callouts on the parent box
        f'<line x1="{cx + 112}" y1="37" x2="440" y2="37" stroke="{BORDER}" stroke-width="1.5"/>',
        f'<text x="448" y="41" fill="{MUTED}" font-family="{SANS}" font-size="13">{t["n_head"]}</text>',
        f'<line x1="{cx + 112}" y1="80" x2="440" y2="80" stroke="{BORDER}" stroke-width="1.5"/>',
        f'<text x="448" y="84" fill="{MUTED}" font-family="{SANS}" font-size="13">{t["n_attr"]}</text>',
        f'<line x1="{cx + 112}" y1="140" x2="440" y2="140" stroke="{BORDER}" stroke-width="1.5"/>',
        f'<text x="448" y="144" fill="{MUTED}" font-family="{SANS}" font-size="13">{t["n_meth"]}</text>',
        f'<text x="448" y="176" fill="{ACCENT}" font-family="{MONO}" font-size="12.5" '
        f'font-weight="700">{t["n_vis"]}</text>',
    ]
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


def uml_relations_figure(lang):
    """The four relationships between classes, with their arrowheads."""
    t = {
        "es": {
            "title": "Las cuatro relaciones entre clases",
            "rows": [("Herencia", "Gerente ES UN Empleado", "triangle"),
                     ("Composición", "Pedido TIENE Renglones, y mueren con él", "filled"),
                     ("Agregación", "Equipo TIENE Empleados, que le sobreviven", "hollow"),
                     ("Asociación", "Cliente USA Catálogo, sin poseerlo", "plain")],
        },
        "en": {
            "title": "The four relationships between classes",
            "rows": [("Inheritance", "Manager IS AN Employee", "triangle"),
                     ("Composition", "Order HAS Lines, and they die with it", "filled"),
                     ("Aggregation", "Team HAS Employees, who outlive it", "hollow"),
                     ("Association", "Customer USES Catalogue, without owning it", "plain")],
        },
    }[lang]

    W, H = 700, 300
    body = []
    y = 40
    for name, meaning, kind in t["rows"]:
        body.append(f'<text x="30" y="{y + 5}" fill="{INK}" font-family="{SANS}" '
                    f'font-size="14" font-weight="700">{name}</text>')
        x1, x2 = 170, 290
        body.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{BLUE}" '
                    f'stroke-width="2"/>')
        if kind == "triangle":
            body.append(f'<polygon points="{x2 + 16},{y} {x2},{y - 9} {x2},{y + 9}" '
                        f'fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>')
        elif kind == "filled":
            body.append(f'<polygon points="{x1},{y} {x1 - 13},{y - 8} {x1 - 26},{y} '
                        f'{x1 - 13},{y + 8}" fill="{BLUE}" stroke="{BLUE}" stroke-width="2"/>')
        elif kind == "hollow":
            body.append(f'<polygon points="{x1},{y} {x1 - 13},{y - 8} {x1 - 26},{y} '
                        f'{x1 - 13},{y + 8}" fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>')
        else:
            body.append(f'<line x1="{x2}" y1="{y}" x2="{x2 + 14}" y2="{y}" '
                        f'stroke="{BLUE}" stroke-width="2" marker-end="url(#tip)"/>')
        body.append(f'<text x="330" y="{y + 5}" fill="{MUTED}" font-family="{SANS}" '
                    f'font-size="13">{meaning}</text>')
        y += 62
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])


def structures_figure(lang):
    """Sequence, selection and repetition, side by side."""
    t = {
        "es": {
            "title": "Las tres estructuras de la programación estructurada",
            "names": ["Secuencia", "Selección", "Repetición"],
            "subs": ["una tras otra", "un camino u otro", "otra vez, mientras"],
        },
        "en": {
            "title": "The three structures of structured programming",
            "names": ["Sequence", "Selection", "Repetition"],
            "subs": ["one after another", "one path or the other", "again, while"],
        },
    }[lang]

    W, H = 700, 260
    body = []
    for i, (name, sub) in enumerate(zip(t["names"], t["subs"])):
        ox = 20 + i * 230
        body.append(f'<rect x="{ox}" y="14" width="200" height="230" rx="8" '
                    f'fill="#FFFFFF" stroke="{BORDER}" stroke-width="1.5"/>')
        body.append(f'<text x="{ox + 100}" y="40" fill="{INK}" font-family="{SANS}" '
                    f'font-size="15" font-weight="700" text-anchor="middle">{name}</text>')
        body.append(f'<text x="{ox + 100}" y="60" fill="{MUTED}" font-family="{SANS}" '
                    f'font-size="12" text-anchor="middle">{sub}</text>')
        cxx = ox + 100
        if i == 0:
            for k in range(3):
                yy = 80 + k * 52
                body.append(f'<rect x="{cxx - 55}" y="{yy}" width="110" height="30" rx="4" '
                            f'fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>')
                if k < 2:
                    body.append(_arrow(cxx, yy + 30, cxx, yy + 50))
        elif i == 1:
            body.append(_diamond(cxx, 100, 110, 46, ""))
            body.append(_elbow([(cxx - 55, 100), (cxx - 65, 100), (cxx - 65, 165)]))
            body.append(_elbow([(cxx + 55, 100), (cxx + 65, 100), (cxx + 65, 165)]))
            for dx in (-65, 65):
                body.append(f'<rect x="{cxx + dx - 38}" y="165" width="76" height="30" '
                            f'rx="4" fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>')
        else:
            body.append(_diamond(cxx, 100, 110, 46, ""))
            body.append(_arrow(cxx, 123, cxx, 162))
            body.append(f'<rect x="{cxx - 48}" y="164" width="96" height="32" rx="4" '
                        f'fill="#FFFFFF" stroke="{BLUE}" stroke-width="2"/>')
            body.append(_elbow([(cxx - 48, 180), (cxx - 84, 180), (cxx - 84, 100),
                                (cxx - 58, 100)]))
    return figure(_canvas(W, H, "".join(body), t["title"]), t["title"])
