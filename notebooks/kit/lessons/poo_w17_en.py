"""notebooks/programacion-orientada-a-objetos/en/w17.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w17.en.yaml
Source code:  none new. This is a revision session, so the notebook goes back
              over the traps already cited and measured in weeks 3 to 16, each
              one with its origin week noted in the cell.

The four that open block 2 are the ones on the diagnosis slide, taken from the
submissions of the two midterms:

  Child constructor without super           -> AttributeError, week 7
  Attribute declared outside __init__       -> shared state, week 6
  A file opened without with                -> nothing reaches disk, week 12
  A bare except                             -> swallows the real error, week 11

The self-diagnosis in block 2 walks the seven units with twenty predictions.
Each one prints the week to go back to if it surprises you, and all twenty were
checked by running the notebook.

Weeks 14 and 15 carried no notebook, so the two graphical-interface predictions
do not run PyQt6: they check the Python mechanism underneath, which is the one
the exam evaluates. The notebook says so.

This is the last notebook of the course.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 17
## Final assessment

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

The closing session. What the final exam covers, where each topic was practised, and the four mistakes
that cost the most marks.

Last week ended by splitting the project into three pieces: the domain, the persistence and the window.
That split is also the shape of a final-exam question, because **integrating** means one question can
touch three units.

By the end you will be able to:

1. Locate every exam topic, with the session that covered it and the lab that practised it.
2. Recognise the four mistakes that turned up in most of the submissions across both midterms.
3. Solve a question that touches modelling, collections, files and persistence at the same time.
4. Diagnose yourself with twenty predictions covering the seven units.
5. Sit the exam with no format doubts, with the submission rules and permitted materials already settled.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Four fail on purpose and carry a comment saying so. They
are exactly the four mistakes that cost the most marks across the two midterms.

Three of the four **raise no exception at all**, which is half of what the whole term has been teaching:
the expensive mistake is hardly ever the one that blows up.

This notebook cites no new file from the repository. It goes back over the traps from weeks 3 to 16, with
the origin week noted in every cell.
"""),

md("""
---
# Block 1 · Scope of the final exam

Integrating means one question can touch three units. There are no sections split up by topic.

| Topic | What it covers |
|---|---|
| **T1** · Paradigm and building blocks | When a class is worth it, plus classes, objects, attributes, methods, access and properties |
| **T2** · Core properties | Encapsulation, hiding, reuse, inheritance, polymorphism and abstract classes |
| **T3** · Functions, collections and errors | Parameters, modularity, recursion, the four collections and exception handling |
| **T4** · Files, interfaces and data | Paths, modes, text and binary, windows with PyQt6, and tables with `sqlite3` |

And where to review each one:

| Topic | Sessions | Reference lab |
|---|---|---|
| Classes and access | 3 and 4 | The bank account from session 4 |
| Inheritance and polymorphism | 7 and 8 | The transport hierarchy from 7 |
| Collections and errors | 10 and 11 | The grade reader from 11 |
| Files | 12 and 13 | The report from CSV in 12 |
| Interface and data | 14 to 16 | The data entry form from 15 |

## What an integrating question looks like

The cell below is a whole question, solved. It touches all four topics and none of its pieces goes over
fifteen lines.
"""),

code("""
import csv
import sqlite3
from pathlib import Path


# ── T1 and T2: modelling, access and inheritance
class Material:
    \"\"\"Base class. The price is validated in the setter and nowhere else.\"\"\"

    def __init__(self, code: str, name: str, price: float) -> None:
        if not code.strip():
            raise ValueError("the code cannot be empty")
        self._code = code.strip()
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError(f"the price cannot be negative, got {value}")
        self._price = float(value)

    @property
    def code(self) -> str:
        return self._code

    def total_cost(self, quantity: int) -> float:
        return self.price * quantity

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._code!r}, {self.name!r}, {self._price})"


class PerishableMaterial(Material):
    \"\"\"Subclass. Chains the constructor and overrides a single method.\"\"\"

    def __init__(self, code, name, price, waste: float = 0.05) -> None:
        super().__init__(code, name, price)
        self.waste = waste

    def total_cost(self, quantity: int) -> float:
        return super().total_cost(quantity) * (1 + self.waste)


CATALOGUE = [
    Material("M001", "M6 bolt", 2.50),
    PerishableMaterial("M002", "Epoxy adhesive", 180.00, waste=0.12),
    Material("M003", "Steel plate", 940.00),
]

for m in CATALOGUE:
    print(f"  {m.code}  {m.name:<20}{m.total_cost(10):>10,.2f}")

print()
print("Polymorphism:", [type(m).__name__ for m in CATALOGUE])
print("The same method, two different sums, one single loop.")
"""),

code("""
# ── T3: collections and errors. The input boundary, with everything else trusting.
class InvalidEntry(Exception):
    def __init__(self, row, reason):
        self.row = row
        self.reason = reason
        super().__init__(f"row {row}: {reason}")


def read_catalogue(path):
    \"\"\"Returns domain objects and a list of problems. It prints nothing.\"\"\"
    materials, problems = [], []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            for number, row in enumerate(csv.DictReader(f), start=2):
                try:
                    materials.append(Material(row["code"], row["name"],
                                              float(row["price"])))
                except (KeyError, TypeError):
                    problems.append(InvalidEntry(number, "missing columns"))
                except ValueError as e:
                    problems.append(InvalidEntry(number, str(e)))
    except FileNotFoundError:
        problems.append(InvalidEntry(0, f"{path} is not there"))
    return materials, problems


Path("catalogue.csv").write_text(
    "code,name,price\\n"
    "M001,M6 bolt,2.50\\n"
    "M002,Epoxy adhesive,one hundred and eighty\\n"
    "M003,Steel plate,-940\\n"
    "M004,Aluminium profile,315.00\\n", encoding="utf-8")

materials, problems = read_catalogue("catalogue.csv")
print("Came in:", len(materials), materials)
for p in problems:
    print("  rejected ->", p)

print()
by_code = {m.code: m for m in materials}          # dictionary: lookup by key
codes = {m.code for m in materials}               # set: membership
print("Lookup by key:", by_code["M004"].name)
print("Is M002 there?", "M002" in codes)
print("Do they all add up?", len(materials) + len(problems) == 4)
"""),

code("""
# ── T4: persistence. All the SQL in one class, and it hands back domain objects.
class MaterialRepository:
    CREATE = ("CREATE TABLE IF NOT EXISTS Materials ("
              "code TEXT PRIMARY KEY, name TEXT NOT NULL, price REAL NOT NULL)")

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.execute(self.CREATE)
        self.connection.commit()

    def save_all(self, materials):
        self.connection.executemany(
            "INSERT OR REPLACE INTO Materials VALUES (?, ?, ?)",
            [(m.code, m.name, m.price) for m in materials])
        self.connection.commit()

    def all(self):
        return [Material(*row) for row in self.connection.execute(
            "SELECT code, name, price FROM Materials ORDER BY code")]

    def close(self):
        self.connection.close()


Path("store.db").unlink(missing_ok=True)

repo = MaterialRepository("store.db")
repo.save_all(materials)
repo.close()

repo = MaterialRepository("store.db")
recovered = repo.all()
repo.close()

print("Recovered from the database:", recovered)
print("Are they domain objects?", all(isinstance(m, Material) for m in recovered))
print("Did they survive the close?", len(recovered) == len(materials))
print()
print("Four layers, and none of them knows about the one above:")
print("  Material           knows nothing of csv or sqlite3")
print("  read_catalogue     knows csv, does not know sqlite3")
print("  MaterialRepository knows sqlite3, does not know csv")
print("  the window         does not exist here, and none of this needs it")
"""),

md("""
Three cells, four topics, and one single exam question.

Look at what is **not** there. No domain class imports `csv` or `sqlite3`. No function computes and prints
at the same time. No data check appears twice. No `except` without a type.

That is the shape of an answer that takes all four criteria on the rubric:

| Criterion | Weight | Where it shows above |
|---|---|---|
| Modelling | 30 % | `Material` and `PerishableMaterial`, with the price validated in the `setter` |
| Application | 35 % | The dictionary, the set, the CSV and the table, each one where it belongs |
| Robustness | 20 % | `InvalidEntry` carrying the row inside, and three `except` clauses by type |
| Execution | 15 % | The three cells run and produce the output the brief would ask for |

**What separates a 7 from a 10 is hardly ever the syntax.** It is where you put the checking and what each
function gives back.
"""),

md("""
---
# Block 2 · Review of what went wrong

Four concrete mistakes that turned up in most of the submissions across both midterms. All four are run
below.

## Predict before you run

```python
class Base:
    def __init__(self):
        self.items = []


class Child(Base):
    def __init__(self):
        self.name = "x"


c = Child()
print(len(c.items))
```

- **A.** `0`, because the list was created empty.
- **B.** `AttributeError`, `items` was never created.
- **C.** `TypeError`, `Child` is missing arguments.
- **D.** `1`, because `name` was added to the list.
"""),

code("""
# FAILS ON PURPOSE. First midterm: the child constructor without super. (Week 7)
class Base:
    def __init__(self):
        self.items = []


class Child(Base):
    def __init__(self):
        self.name = "x"            # super().__init__() is missing


c = Child()

print("The object was built without complaining:", vars(c))
print("Attributes:", len(vars(c)), "<- we expected 2")
print()
try:
    print(len(c.items))
except AttributeError as e:
    print("AttributeError:", e)

print()


class ChildWell(Base):
    def __init__(self):
        super().__init__()         # the parent's part first
        self.name = "x"


w = ChildWell()
print("With super():", vars(w), " items:", len(w.items))
"""),

md("""
The answer is **B**, and it is the number one mistake of the term.

Defining `__init__` in the child **replaces** the parent's, it does not add to it. Without
`super().__init__()`, `Base`'s constructor never runs and `items` does not exist.

Look at the order in which it gets found. The object was built without a single complaint, with one
attribute instead of two. The error turns up later, on the first line that reads `items`, which may sit in
another file and be written by somebody else.

## The attribute everybody shares
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. First midterm: the attribute outside __init__. (Week 6)
class Group:
    students = []                   # <- outside __init__: it belongs to the class

    def __init__(self, code):
        self.code = code

    def enrol(self, name):
        self.students.append(name)


com102 = Group("COM102")
com103 = Group("COM103")

com102.enrol("Ana")
com102.enrol("Luis")
com103.enrol("Sofia")

print("COM102:", com102.students)
print("COM103:", com103.students)
print("Is it the same list?", com102.students is com103.students)
print("And is it the class's as well?", com102.students is Group.students)
print()
print("What each object holds of its own:", vars(com102), vars(com103))
print("  <- students is not there: it belongs to no object")
print()


class GroupWell:
    def __init__(self, code):
        self.code = code
        self.students = []          # one list per object

    def enrol(self, name):
        self.students.append(name)


a, b = GroupWell("COM102"), GroupWell("COM103")
a.enrol("Ana")
b.enrol("Sofia")
print("With the list in __init__:", a.students, b.students, a.students is b.students)
"""),

md("""
Three students enrolled across two groups, and all three show up in both.

A name written in the body of the class belongs to **the class**, not to each object. When that value is
mutable, every object writes into the same one. `vars(com102)` proves it: `students` is not in the
object's state because it was never the object's.

It is the same mechanism as week 9's mutable default value and week 6's shared list. The rule that covers
all three: **if something is going to change per object, it gets assigned inside `__init__`.**

## What was written and never reached the disk
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Second midterm: the file without with. (Week 12)
from pathlib import Path

OPEN_FILES = []                     # the program keeps them to go on writing


def export(materials, path):
    file = open(path, "w", encoding="utf-8")
    OPEN_FILES.append(file)
    for m in materials:
        file.write(f"{m.code},{m.name},{m.price}\\n")
    # file.close() is missing


export(materials, "export.csv")

print("Materials exported:", len(materials))
print("Bytes on disk:", Path("export.csv").stat().st_size)
print("Still open?", not OPEN_FILES[0].closed)
print()
print("The program finished fine and the file is empty.")
print()

OPEN_FILES[0].close()

with open("export.csv", "w", encoding="utf-8") as file:
    for m in materials:
        file.write(f"{m.code},{m.name},{m.price}\\n")

print("With with:", Path("export.csv").stat().st_size, "bytes")
print(Path("export.csv").read_text(encoding="utf-8"))
"""),

md("""
Zero bytes, no exception, and a program that finished fine.

Writing fills a buffer in memory. Closing is what empties it onto the disk. Without `close`, and for as
long as something still points at the file, what was written does not exist outside the process.

In a submission this looks like "the program runs but the output file is empty", which is the sentence
that turned up most often in the second midterm.

## The `except` that hid the real error
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Second midterm: the except with no type. (Week 11)
def average_price(materials):
    try:
        total = 0
        for m in materials:
            total += m.price
        return total / len(materials)
    except:                              # noqa: E722
        return 0.0


print("Average:", average_price(materials))
print("Average of an empty list:", average_price([]))
print("Average of a list of strings:", average_price(["M001", "M002"]))
print()
print("All three gave back a number and only the first one means anything.")
print()


def average_well(materials):
    if not materials:
        raise ValueError("an empty list cannot be averaged")
    return sum(m.price for m in materials) / len(materials)


for entry, label in [(materials, "catalogue"), ([], "empty list"),
                     (["M001"], "list of strings")]:
    try:
        print(f"  {label:<18}{average_well(entry):.2f}")
    except (ValueError, AttributeError) as e:
        print(f"  {label:<18}{type(e).__name__}: {e}")
"""),

md("""
Three calls, three numbers, and two of them are lies.

A bare `except` turns any problem into the default value. The empty list would have given a
`ZeroDivisionError`; the list of strings, an `AttributeError`, because a string has no `price`. Both are
defects and both came out as `0.0`.

The version below does the opposite: **it refuses what it cannot process and lets what it did not expect
travel up.** An `AttributeError` that reaches the surface is information; turned into a zero it is a false
figure in a report.
"""),

md("""
---
## Self-diagnosis across the seven units

Twenty predictions, one per behaviour the exam may ask you to write. The cell marks itself and prints
which week to go back to.

The two on the graphical interface open no window: they check the Python mechanism underneath, which is
what the exam evaluates. Weeks 14 and 15 were worked through in class, in the editor.
"""),

code("""
import csv
import sqlite3
from pathlib import Path

P = []


def p(behaviour, week, got, expected):
    P.append((behaviour, week, got, expected))


# ── T1 · Paradigm and building blocks
class Point:
    def __init__(self, x):
        self.x = x


a, b = Point(1), Point(1)
p("Two objects with the same value are the same", 3, a is b, False)
p("State lives in the object", 3, vars(a), {"x": 1})


class Account:
    def __init__(self):
        self.__balance = 0


p("The double underscore changes the name", 4,
  "_Account__balance" in vars(Account()), True)


class Temp:
    def __init__(self):
        self._c = 0

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, v):
        self._c = max(-273, v)


t = Temp()
t.c = -400
p("The setter runs on assignment", 5, t.c, -273)

# ── T2 · Core properties
class Parent:
    def greet(self):
        return "parent"


class Child(Parent):
    def greet(self):
        return "child"


p("The child covers the parent's method", 7, Child().greet(), "child")
p("And it is still a Parent", 7, isinstance(Child(), Parent), True)
p("type() is not isinstance()", 7, type(Child()) is Parent, False)

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


try:
    Shape()
    abstract = "it was built"
except TypeError:
    abstract = "TypeError"
p("An abstract class cannot be instantiated", 8, abstract, "TypeError")

# ── T3 · Functions, collections and errors
def add_item(x, items=[]):
    items.append(x)
    return items


add_item(1)
p("The default value is evaluated once", 9, len(add_item(2)), 2)

values = [1, 2, 3]
alias = values
alias.append(4)
p("The equals sign does not copy, it shares", 10, len(values), 4)

p("A set keeps no repeats", 10, len({1, 1, 2, 2, 3}), 3)
p("zip stops at the shortest", 10, len(list(zip("abcde", "xyz"))), 3)

ran = []


def read():
    try:
        return 7
    finally:
        ran.append("finally")


read()
p("finally runs with a return waiting", 11, ran, ["finally"])


def classify():
    try:
        raise FileNotFoundError()
    except OSError:
        return "general"
    except FileNotFoundError:
        return "specific"


p("The general except hides the specific one", 11, classify(), "general")

# ── T4 · Files, interfaces and data
path = Path("final.txt")
path.write_text("first", encoding="utf-8")
f = open(path, "w", encoding="utf-8")
p("Mode w empties the file on opening", 12, path.stat().st_size, 0)
f.close()

Path("final.csv").write_text("n,v\\nAna,9.1\\n", encoding="utf-8")
with open("final.csv", newline="", encoding="utf-8") as f:
    row = next(csv.DictReader(f))
p("A CSV stores no types", 12, type(row["v"]).__name__, "str")

Path("final.bin").write_bytes(b"ABCDEFGH")
with open("final.bin", "rb") as f:
    f.seek(3)
    chunk = f.read(2)
p("Positions are counted from zero", 13, chunk, b"DE")


class Button:
    \"\"\"No PyQt6: the Python mechanism underneath connect().\"\"\"

    def __init__(self):
        self.slot = None

    def connect(self, function):
        self.slot = function


def on_click():
    return "click"


button = Button()
button.connect(on_click())                # with parentheses: it was called already
p("connect with parentheses stores the result", 14, button.slot, "click")
button.connect(on_click)                  # without them: the function is stored
p("connect without parentheses stores the function", 14, callable(button.slot), True)

Path("final.db").unlink(missing_ok=True)
c = sqlite3.connect("final.db")
c.execute("CREATE TABLE T (id INTEGER PRIMARY KEY)")
c.commit()
c.close()
c = sqlite3.connect("final.db")
c.execute("INSERT INTO T VALUES (1)")
c.close()
c = sqlite3.connect("final.db")
n = c.execute("SELECT COUNT(*) FROM T").fetchone()
c.close()
p("Closing without commit discards", 16, n, (0,))

matched = 0
print(f"{'#':<4}{'week':<6}{'behaviour':<50}{'result'}")
for i, (behaviour, week, got, expected) in enumerate(P, start=1):
    ok = got == expected
    matched += ok
    flag = "" if ok else f"   <- expected {expected!r}"
    print(f"{i:<4}{week:<6}{behaviour:<50}{got!r}{flag}")

print()
print(f"Predictions that matched: {matched} of {len(P)}")
print("The 'week' column says which notebook to go back to for each one that surprised you.")
"""),

md("""
Twenty behaviours, seven units, and not one of them is answered with a definition.

The final exam works the same way. **No question asks you to explain what encapsulation is**; they ask
you to write a class where the price cannot end up negative, which is the same thing said the only way it
can be marked.

The two week 14 questions use a `Button` class written here instead of `QPushButton`, and they check
exactly what the exam evaluates: passing a function without parentheses stores the function; with
parentheses it calls it there and then and stores what came back. The real `TypeError` shows up later,
when Qt tries to call what it was handed.
"""),

md("""
---
## How this gets studied

**No question asks for a definition.** Every one asks for code that runs, so the only preparation that
helps is solving the labs again without looking at the solution.

**What to practise.** One lab per unit, solved from scratch and without opening the solution file.

**What to review.** The diagnosis slides and the four errors on each one. They are the errors on the exam.

**What not to do.** Rereading the concept slides. They make sense on reading and vanish on writing.

## What to know before sitting down

| | |
|---|---|
| **Format** | At the keyboard, one `.py` file per question, named as the brief specifies |
| **Materials** | The course repository and the official Python documentation, open |
| **No outside help** | No people and no assistants. The University Honour Code applies. |
| **Submission** | Through Blackboard, within the exam window. Email submissions are not accepted. |

And the weights, so you know where the time goes:

| Criterion | Weight |
|---|---|
| Modelling | 30 % |
| Application | 35 % |
| Robustness | 20 % |
| Execution | 15 % |

**Execution is worth fifteen per cent and it conditions the other eighty-five.** A file that does not run
cannot be marked on modelling. The last five minutes go on running everything again from scratch, not on
improving an answer.
"""),

md("""
---
# Exercises

A mock final exam. Four questions, with the weights from the real rubric.

The solutions are at the very bottom of the notebook.

### Question 1 · Modelling (30 %)

Model a `Vehicle` with a plate, a make and an odometer reading, and an `ElectricVehicle` that inherits
from it and adds the range in kilometres.

The odometer can never go down, and that rule lives in the `setter`. The plate is read and not written.
`ElectricVehicle` overrides a cost-per-kilometre method and chains with `super()`.

Build three objects, one of each type, and show with a loop that the same method gives different sums.

### Question 2 · Application (35 %)

You are given a CSV with the `plate`, the `date` and the `kilometres` of each trip. Write functions that:

1. Read the file and give back objects, not dictionaries.
2. Group the kilometres by plate with an accumulator dictionary.
3. Give back the set of plates that appear.
4. Give back the plate with the most kilometres.

No function prints. None goes over fifteen lines.

### Question 3 · Robustness (20 %)

Define `InvalidTrip(Exception)` holding the row number and the reason. Raise it from the reading when the
kilometres are not a number or come out negative.

The program has to finish cleanly with a CSV that does not exist, with an empty one, with one missing a
column, and with one carrying three bad rows out of ten.

### Question 4 · Persistence and execution (15 %)

Write the data access class that saves the vehicles in `sqlite3` and gets them back as domain objects. All
the SQL lives there.

Show that the data survives closing the connection and opening it again. Hand in an
`if __name__ == "__main__":` block that runs the whole flow from start to finish.
"""),

md("""
---
## Three ideas to take from the term

**The class describes, the object remembers.** Everything else in the course leans on that distinction,
the application half included: a file, a connection and a window are objects with state and with a life
cycle.

**Whatever gets opened gets closed.** A file, a connection and a window share one life cycle and one and
the same trap. `with` solves it for the first two; the third closes itself when the event loop ends.

**Code that can be tested is the code that lasts.** Pulling the logic out of the slots, the loops and the
`print` calls is what lets you fix it without guessing. It is the same decision from week 9 through to
week 16: what a function takes, what it gives back, and what it leaves changed outside itself.

That closes COM102. The course repository stays open, and the nineteen notebooks in your language still
run whole in Colab with nothing to install.

What comes next is data structures: linked lists, trees, graphs and the cost of each operation. All of
this is the ground they stand on. Week 10 already measured why appending to the end of a list is cheap
and inserting at the front is not, and that question, asked seriously, is the whole subject.
"""),

md("""
---
# Solutions

### Question 1

```python
class Vehicle:
    def __init__(self, plate: str, make: str, odometer: float = 0.0) -> None:
        if not plate.strip():
            raise ValueError("the plate cannot be empty")
        self._plate = plate.strip().upper()
        self.make = make
        self._odometer = 0.0
        self.odometer = odometer

    @property
    def plate(self) -> str:
        return self._plate

    @property
    def odometer(self) -> float:
        return self._odometer

    @odometer.setter
    def odometer(self, value: float) -> None:
        if value < self._odometer:
            raise ValueError(f"the odometer cannot go down from "
                             f"{self._odometer} to {value}")
        self._odometer = float(value)

    def cost_per_km(self) -> float:
        return 3.80

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._plate!r}, {self.make!r}, {self._odometer})"


class ElectricVehicle(Vehicle):
    def __init__(self, plate, make, odometer=0.0, range_km=320) -> None:
        super().__init__(plate, make, odometer)
        self.range_km = range_km

    def cost_per_km(self) -> float:
        return super().cost_per_km() * 0.35


FLEET = [Vehicle("ABC123", "Nissan", 41_000),
         ElectricVehicle("XYZ789", "BYD", 12_400, range_km=400),
         Vehicle("JKL456", "Toyota", 88_200)]

for v in FLEET:
    print(f"{v.plate}  {type(v).__name__:<18}{v.cost_per_km():.2f} per km")

try:
    FLEET[0].odometer = 100
except ValueError as e:
    print("ValueError:", e)
```

### Question 2

```python
import csv


class Trip:
    def __init__(self, plate, date, kilometres):
        self.plate = plate
        self.date = date
        self.kilometres = kilometres

    def __repr__(self):
        return f"Trip({self.plate!r}, {self.date!r}, {self.kilometres})"


def read_trips(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [Trip(r["plate"], r["date"], float(r["kilometres"]))
                for r in csv.DictReader(f)]


def km_per_plate(trips):
    accumulated = {}
    for t in trips:
        accumulated[t.plate] = accumulated.get(t.plate, 0.0) + t.kilometres
    return accumulated


def plates(trips):
    return {t.plate for t in trips}


def most_travelled(trips):
    accumulated = km_per_plate(trips)
    return max(accumulated, key=accumulated.get)
```

### Question 3

```python
import csv
from pathlib import Path

COLUMNS = ["plate", "date", "kilometres"]


class InvalidTrip(Exception):
    def __init__(self, row, reason):
        self.row = row
        self.reason = reason
        super().__init__(f"row {row}: {reason}")


def read_trips(path):
    \"\"\"Input boundary. Gives back good trips and problems, and prints nothing.\"\"\"
    trips, problems = [], []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                return [], [InvalidTrip(0, "the file is empty")]
            missing = [c for c in COLUMNS if c not in reader.fieldnames]
            if missing:
                return [], [InvalidTrip(0, f"missing columns: {missing}")]
            for number, row in enumerate(reader, start=2):
                try:
                    km = float(row["kilometres"])
                except (TypeError, ValueError):
                    problems.append(InvalidTrip(
                        number, f"{row.get('kilometres')!r} is not a number"))
                    continue
                if km < 0:
                    problems.append(InvalidTrip(number, f"{km} is negative"))
                    continue
                trips.append(Trip(row["plate"], row["date"], km))
    except FileNotFoundError:
        problems.append(InvalidTrip(0, f"{path} is not there"))
    return trips, problems
```

### Question 4

```python
import sqlite3
from pathlib import Path


class VehicleRepository:
    CREATE = ("CREATE TABLE IF NOT EXISTS Vehicles ("
              "plate TEXT PRIMARY KEY, make TEXT NOT NULL, "
              "odometer REAL NOT NULL, kind TEXT NOT NULL, "
              "range_km INTEGER)")

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.execute(self.CREATE)
        self.connection.commit()

    def save(self, vehicle):
        self.connection.execute(
            "INSERT OR REPLACE INTO Vehicles VALUES (?, ?, ?, ?, ?)",
            (vehicle.plate, vehicle.make, vehicle.odometer,
             type(vehicle).__name__,
             getattr(vehicle, "range_km", None)))
        self.connection.commit()

    def all(self):
        vehicles = []
        for plate, make, km, kind, range_km in self.connection.execute(
                "SELECT plate, make, odometer, kind, range_km "
                "FROM Vehicles ORDER BY plate"):
            if kind == "ElectricVehicle":
                vehicles.append(ElectricVehicle(plate, make, km, range_km))
            else:
                vehicles.append(Vehicle(plate, make, km))
        return vehicles

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    Path("fleet.db").unlink(missing_ok=True)
    Path("trips.csv").write_text(
        "plate,date,kilometres\\n"
        "ABC123,2026-03-01,142.5\\n"
        "XYZ789,2026-03-01,88.0\\n"
        "ABC123,2026-03-02,two hundred\\n"
        "JKL456,2026-03-02,-30\\n"
        "XYZ789,2026-03-03,210.0\\n", encoding="utf-8")

    trips, problems = read_trips("trips.csv")
    print(f"{len(trips)} good trips, {len(problems)} rejected")
    for p in problems:
        print("  ", p)

    print("Kilometres per plate:", km_per_plate(trips))
    print("The one that travelled most:", most_travelled(trips))

    repo = VehicleRepository("fleet.db")
    for v in FLEET:
        repo.save(v)
    repo.close()

    repo = VehicleRepository("fleet.db")
    recovered = repo.all()
    repo.close()

    print("Recovered:", recovered)
    print("With their type:", [type(v).__name__ for v in recovered])

    _, problems = read_trips("missing.csv")
    print("Missing file:", problems[0])
```

Four decisions that carry the four criteria.

**The odometer is validated in the `setter` and nowhere else.** That is why `__init__` assigns to
`self.odometer` instead of `self._odometer`: the rule runs on construction too.

**`read_trips` gives back two lists and prints nothing.** The good trips and the problems come out
together, so whoever calls it decides what to do with each, and the function can be tested against a CSV
written by hand.

**The repository stores the type and uses it to rebuild the right subclass.** A table knows nothing about
inheritance, so the `kind` column is what lets `all()` give back an `ElectricVehicle` where one belongs.

**The `if __name__ == "__main__":` block runs the whole flow.** That is what gets marked in the fifteen
per cent for execution, and it is the first thing to check before handing in.
"""),

]

write(OUT / "en" / "w17.ipynb", en)
print("wrote", OUT / "en" / "w17.ipynb")
