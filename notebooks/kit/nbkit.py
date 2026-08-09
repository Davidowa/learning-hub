"""Shared machinery for building the course notebooks.

One module so the setup cell, the Colab metadata and the writer live in a single
place instead of being copy-pasted into every week.
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# ─────────────────────────────────────────────────────────────── nbformat bits


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _lines(text)}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": _lines(text)}


def _lines(text):
    """nbformat stores source as a list of lines, each keeping its newline."""
    text = text.strip("\n")
    out = text.splitlines(keepends=True)
    return out


def write(path, cells):
    nb = {
        "cells": cells,
        "metadata": {
            "colab": {"provenance": [], "toc_visible": True},
            "kernelspec": {"name": "python3", "display_name": "Python 3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 0,
    }
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    return path


# ────────────────────────────────────────────────── the data bootstrap cell

BASE_URL = ('BASE = ("https://raw.githubusercontent.com/Davidowa/learning-hub/main/"\n'
            '        "docs/en/courses/python-course/06%20-%20Advanced/data/")')

# The generator below reproduces the three CSV files byte for byte, because the
# seed is fixed. Kept as one string so every data notebook carries the identical
# block and a fix lands everywhere at once.
_GEN = '''
def _reconstruir_datos():
    """@DOC@"""
    import csv, random
    from datetime import date, timedelta

    rng = random.Random(20260808)
    REGIONS = ["North", "South", "Centre", "West"]
    CHANNELS = ["Retail", "Online", "Wholesale"]
    PRODUCTS = {"Espresso machine": 8990.0, "Coffee grinder": 2450.0,
                "Filter kettle": 1290.0, "Bean subscription": 690.0,
                "Travel mug": 349.0}
    RW = {"North": 1.30, "South": 0.80, "Centre": 1.55, "West": 0.95}
    CW = {"Retail": 1.00, "Online": 1.25, "Wholesale": 2.10}
    MW = [0.72, 0.78, 0.90, 0.95, 1.00, 1.05, 0.98, 0.92, 1.08, 1.15, 1.45, 1.60]

    rows, start = [], date(2025, 1, 6)
    for week in range(52):
        day = start + timedelta(weeks=week)
        for region in REGIONS:
            for _ in range(rng.randint(1, 2)):
                product = rng.choice(list(PRODUCTS))
                channel = rng.choice(CHANNELS)
                base = 9 * RW[region] * CW[channel] * MW[day.month - 1]
                units = max(1, round(rng.gauss(base, base * 0.28)))
                price = PRODUCTS[product] * rng.choice([1.0, 1.0, 1.0, 0.9, 0.85])
                rows.append({"date": day.isoformat(), "region": region,
                             "channel": channel, "product": product,
                             "units": str(units),
                             "unit_price": f"$ {price:,.2f}"})

    # @DIRT@
    for i in rng.sample(range(len(rows)), 24):
        rows[i]["region"] = rng.choice(["north", "NORTH", " North", "North "])
    for i in rng.sample(range(len(rows)), 11):
        rows[i]["units"] = ""
    for i in rng.sample(range(len(rows)), 7):
        rows.append(dict(rows[i]))
    rng.shuffle(rows)

    with open("sales.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "region", "channel",
                                          "product", "units", "unit_price"])
        w.writeheader()
        w.writerows(rows)

    with open("regions.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["region", "manager", "country", "monthly_target"])
        w.writerows([["North", "Ana Robles", "Mexico", 480000],
                     ["South", "Luis Ferrer", "Mexico", 300000],
                     ["Centre", "Paula Ines", "Mexico", 560000],
                     ["West", "Marco Duarte", "Mexico", 360000],
                     ["East", "Sofia Lara", "Mexico", 220000]])

    AREAS = {
        "Sales": (["Account executive", "Sales analyst", "Sales manager"], 24000, 62000),
        "Marketing": (["Content specialist", "Campaign analyst", "Brand manager"], 22000, 58000),
        "Finance": (["Accounts clerk", "Financial analyst", "Controller"], 26000, 74000),
        "People": (["Recruiter", "People analyst", "People manager"], 21000, 55000),
        "Operations": (["Warehouse lead", "Logistics analyst", "Operations manager"], 20000, 60000),
    }
    CITIES = ["Mexico City", "Guadalajara", "Monterrey", "Queretaro"]
    emp = []
    for n in range(1, 121):
        area = rng.choice(list(AREAS))
        titles, low, high = AREAS[area]
        idx = rng.choices([0, 1, 2], weights=[5, 3, 1])[0]
        tenure = rng.randint(2, 132)
        salary = round(low + (high - low) * (idx / 2) * rng.uniform(0.82, 1.10)
                       + tenure * 45, -2)
        emp.append({"employee_id": f"E{n:04d}", "area": area,
                    "job_title": titles[idx], "city": rng.choice(CITIES),
                    "tenure_months": tenure, "monthly_salary": int(salary)})
    with open("employees.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(emp[0]))
        w.writeheader()
        w.writerows(emp)
'''.strip("\n")


def bootstrap_cell(lang):
    """The one setup cell every Data Analysis notebook opens with."""
    if lang == "es":
        head = (
            "# Plomería, no lección. Esta celda deja los tres CSV del curso al\n"
            "# alcance de pandas y no vuelve a hacer falta.\n"
            "#\n"
            "# Primero los busca en el repositorio, que es público y se lee por URL.\n"
            "# Si no responde, los reconstruye aquí mismo con la semilla fija del\n"
            "# curso, así que salen idénticos por cualquiera de los dos caminos.\n"
            "# En ningún caso hay que subir un archivo a mano."
        )
        ok = '    print("Datos leídos del repositorio.")'
        gen = '    print("El repositorio no respondió. Datos reconstruidos en esta sesión.")'
        listo = 'print("Listos:", ", ".join(ARCHIVOS))'
    else:
        head = (
            "# Plumbing, not the lesson. This cell puts the three course CSVs within\n"
            "# reach of pandas, and it never needs running again.\n"
            "#\n"
            "# It looks for them in the repository first, which is public and reads\n"
            "# over a URL. If that does not answer, it rebuilds them right here from\n"
            "# the course's fixed seed, so both routes produce identical files.\n"
            "# Nothing ever has to be uploaded by hand."
        )
        ok = '    print("Data read from the repository.")'
        gen = '    print("The repository did not answer. Data rebuilt in this session.")'
        listo = 'print("Ready:", ", ".join(FILES))'

    if lang == "es":
        doc = ("Vuelve a escribir los tres CSV con la semilla fija del curso.\n\n"
               "    Salen idénticos byte por byte a los del repositorio, así que los\n"
               "    números de la diapositiva siguen coincidiendo con los del cuaderno.\n    ")
        dirt = ("la suciedad deliberada: una región tecleada de cuatro formas,\n"
                "    # celdas en blanco, y renglones capturados dos veces")
    else:
        doc = ("Write the three CSV files again from the course's fixed seed.\n\n"
               "    They come out byte for byte identical to the ones in the repository,\n"
               "    so the numbers on the slide still match the ones in the notebook.\n    ")
        dirt = ("the deliberate dirt: one region typed four ways, blank cells, and\n"
                "    # rows captured twice")

    gen_src = _GEN.replace("@DOC@", doc).replace("@DIRT@", dirt)
    names = "ARCHIVOS" if lang == "es" else "FILES"
    return code(f"""{head}
import urllib.request
from pathlib import Path

{BASE_URL}
{names} = ["sales.csv", "regions.csv", "employees.csv"]


def _descargar():
    for nombre in {names}:
        with urllib.request.urlopen(BASE + nombre, timeout=15) as r:
            Path(nombre).write_bytes(r.read())


{gen_src}


try:
    _descargar()
{ok}
except Exception:
    _reconstruir_datos()
{gen}

{listo}""")
