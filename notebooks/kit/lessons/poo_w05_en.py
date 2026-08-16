"""notebooks/programacion-orientada-a-objetos/en/w05.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w05.en.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code022.py
                  (magic methods block, lines 70 to 206)
              docs/en/courses/python-course/02 - POO/6th Module/Code023.py
                  (custom containers: __getitem__, __setitem__, __len__, __iter__)
              docs/en/courses/python-course/02 - POO/6th Module/MagicMethods.md

Code022.py does not run to the end: it stops on its line 62, which is the trap
week 4 quotes. The magic methods block lives after that line, so in the original
file it never executes. The code from line 92 onwards is quoted here, checked by
hand, and the notebook says so.

The modules and the package in block 3 are written with open() into the working
directory before being imported, which is what the rest of the kit does.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 05
## Topic 2 · Basic elements

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

One name for several ways of calling, the operators you can teach to work with your objects, where each
class lives once the project grows, and the step from a written brief to a model.

This week closes topic 2. The previous three built a class; this one teaches it to be usable, findable,
and thought through before it was written.

By the end you will be able to:

1. Explain why the second `def` with the same name erases the first.
2. Cover several call shapes with a single method, using defaults, `*args` and `**kwargs`.
3. Overload `__str__`, `__eq__` and `__add__`, and say what breaks when each one is missing.
4. Split classes across modules and packages, and know what runs at import time.
5. Pull the classes out of a written brief without inventing one called Manager.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Twelve fail on purpose and carry a comment saying so.

Nine of the twelve **raise no exception at all**, which is the highest proportion in the course so far.
Almost everything this week fails without a word, because almost everything produces an object that
exists and output that looks reasonable. Block 3 writes real files into the notebook's working
directory, so run those cells in order or the `import` statements will find nothing.
"""),

md("""
---
# Block 1 · Overloaded methods

In Java or C# you can write two methods with the same name and different signatures, and the compiler
decides which to call from the arguments. That is called overloading, and **Python does not have it**.

It is worth understanding why not, because the reason explains half a dozen behaviours that otherwise
look arbitrary.

## Predict before you run

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


c = Calculator()
print(c.add(1, 2))
```

- **A.** 3, because Python picks the two-parameter method.
- **B.** `TypeError`, a positional argument is missing.
- **C.** 6, because `c` is zero when it is not passed.
- **D.** `SyntaxError`, `add` is defined twice.
"""),

code("""
# FAILS ON PURPOSE. Two methods with the same name, and only one survives.
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


calc = Calculator()

try:
    print(calc.add(1, 2))
except TypeError as e:
    print("TypeError:", e)

print()
print("With three arguments it works:", calc.add(1, 2, 3))
print()
print("Methods left on the class:", [n for n in vars(Calculator) if not n.startswith("__")])
print("Parameters add accepts:", Calculator.add.__code__.co_varnames[:4])
"""),

md("""
The answer is **B**.

The class kept **one** `add`, not two. A class body runs top to bottom like any other block, and every
`def` is an assignment: it puts a function into the class dictionary under that name. The second
assignment covers the first, exactly like `x = 1` followed by `x = 2`.

It is the same mechanism as the redefined function in review 3 and the redefined class in week 4. Third
appearance, third disguise, same sentence: **a name holds one value**.

What Python offers instead is better, and it fits on one line.
"""),

code("""
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c


calc = Calculator()
print("Two arguments:  ", calc.add(1, 2))
print("Three arguments:", calc.add(1, 2, 3))
print()
print("A single method:", [n for n in vars(Calculator) if not n.startswith("__")])
"""),

md("""
One method, two ways to call it, and no ambiguity about which one runs.

The equivalence table, so it sits in one place.

| What you need | In Java or C# | In Python |
|---|---|---|
| An optional parameter | Two methods with different signatures | `def greet(self, formal=False)` |
| However many values | One method per count | `def add(self, *skus)` |
| Named options | A configuration object | `def create(self, **options)` |
| Different types | One signature per type | `isinstance` or `functools.singledispatch` |
| Your own operators | operator overloading | `__add__` · `__eq__` · `__str__` |

## When you do not know how many are coming
"""),

code("""
class Cart:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.products: list[str] = []

    def add(self, *skus: str, **options: bool) -> None:
        for sku in skus:
            self.products.append(sku)
        if options.get("announce"):
            print(f"{len(skus)} products added")


cart = Cart("Ana")

cart.add("X1")
cart.add("X2", "X3", announce=True)
cart.add()                               # zero arguments is valid too

print()
print("Cart:", cart.products)
print("Products:", len(cart.products))
"""),

md("""
`*skus` collects however many positional arguments arrive into a **tuple**, including none.
`**options` collects the named ones into a **dictionary**.

The two asterisks are the same idea applied to the two halves of a call. And the names `args` and
`kwargs` are pure habit: the asterisk does the work, not the word.

Now the two ways this goes wrong on you without anyone saying a thing.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Handing a list to a method that expects loose arguments.
other = Cart("Luis")
other.add(["X1", "X2", "X3"])

print("Cart:", other.products)
print("Products:", len(other.products), "<- we expected 3")
print("Type of the first one:", type(other.products[0]).__name__)
print()
print("With the asterisk at the call site:")
third = Cart("Sofia")
third.add(*["X1", "X2", "X3"])
print("Products:", len(third.products))
"""),

md("""
One product that is a list of three products.

`*skus` does not unpack whatever arrives, it collects whatever was sent. Send it a list and the whole
list is one positional argument, so `skus` is `(["X1", "X2", "X3"],)`, a one-element tuple.

The asterisk on the calling side is the one that unpacks. `add(*items)` spreads the three elements
across three arguments, which is why the second half of the cell counts three.

The symptom shows up late and in disguise: the cart says it holds one product, and the first time
somebody writes `sku.upper()` they get an `AttributeError` about a list, a long way from here.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. An option with a misspelled name.
fourth = Cart("Marco")
fourth.add("X1", "X2", anounce=True)         # we meant announce

print("Added:", fourth.products)
print("Was the notice printed? No.")
print()


class StrictCart(Cart):
    KNOWN = {"announce"}

    def add(self, *skus, **options):
        unknown = set(options) - self.KNOWN
        if unknown:
            raise TypeError(f"unknown option: {', '.join(sorted(unknown))}")
        super().add(*skus, **options)


fifth = StrictCart("Marco")
try:
    fifth.add("X1", anounce=True)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`**options` accepts any word at all. That is its job: it collects everything that arrives with a name
and has no way of knowing which ones you were expecting.

It is exactly the misspelled attribute from week 3 in another disguise. There, `point.coordinate_x =
500` created a new key in the object's dictionary; here `anounce=True` creates a new key in the options
dictionary. In both cases the value is stored, nobody reads it, and there is no error.

The second half of the cell shows the price of fixing it: if you accept anything, you have to write the
check the language no longer does. That is why `**kwargs` is not free. **A method that accepts anything
tells nobody what may be passed to it.**

## Different types in the same method
"""),

code("""
class Report:
    def __init__(self, title):
        self.title = title
        self.rows = []

    def add(self, data):
        if isinstance(data, str):
            self.rows.append(data)
        elif isinstance(data, (list, tuple)):
            self.rows.extend(data)
        elif isinstance(data, dict):
            self.rows.extend(f"{k}: {v}" for k, v in data.items())
        else:
            raise TypeError(f"no idea what to do with a {type(data).__name__}")


r = Report("Sales")
r.add("total: 120")
r.add(["north: 40", "south: 30"])
r.add({"centre": 50})

for row in r.rows:
    print(" ", row)

print()
print("Rows:", len(r.rows))
try:
    r.add(3.14)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
It works, and it is still a warning sign.

When a method body fills up with `if isinstance`, it was almost always two or three methods with
different names. `add_text`, `add_many` and `add_pairs` read better, test separately, and do not force
anyone to follow the whole chain to find out what happens to their data.

The working rule: **one method, one responsibility**. If you genuinely need to dispatch on type, the
standard library ships `functools.singledispatch`, which does the same without the ladder of `if`.

## The default value you did not want
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A list as a method's default value.
class BrokenCart:
    def __init__(self, owner, products=[]):
        self.owner = owner
        self.products = products

    def add(self, sku):
        self.products.append(sku)


ana = BrokenCart("Ana")
luis = BrokenCart("Luis")

ana.add("X1")

print("Ana's cart: ", ana.products)
print("Luis's cart:", luis.products, "<- having added nothing")
print("Is it the same list?", ana.products is luis.products)
print()
print("The list lives in the method's signature:")
print("  ", BrokenCart.__init__.__defaults__)
"""),

md("""
That last line solves the mystery: **the list is stored on the function**, in `__defaults__`, and it was
created once, when Python read the `def`.

Every `BrokenCart("Ana")` that does not pass products gets that same list. Not a copy. The same one.

This is the fourth place the same mechanism turns up, and it is worth seeing them in a row:

| Where | How it looked |
|---|---|
| Review 3 | `def f(items=[])` piled up between calls |
| Review 4 | `b = a` left two names on one list |
| Week 3 | `products = []` in the class body was shared between objects |
| Today | `products=[]` in the constructor signature is shared between objects |

The fix is the usual one and it fits in two lines.
"""),

code("""
class GoodCart:
    def __init__(self, owner, products=None):
        self.owner = owner
        self.products = list(products) if products else []

    def add(self, sku):
        self.products.append(sku)


ana = GoodCart("Ana")
luis = GoodCart("Luis")
ana.add("X1")

print("Ana: ", ana.products)
print("Luis:", luis.products)
print("The same list?", ana.products is luis.products)
print()
print("The default now:", GoodCart.__init__.__defaults__)

starting = ["Y1", "Y2"]
sofia = GoodCart("Sofia", starting)
sofia.add("Y3")
print()
print("The list we handed over:", starting, "<- untouched")
print("The cart's own:         ", sofia.products)
"""),

md("""
`None` as the default, the list built inside, and a copy of whatever is passed in.

That `list(products)` on the third line is the part almost nobody writes. Without it, the cart keeps the
list belonging to whoever built it and the two change together, which is review 4's alias all over
again. With it, the person handing you data does not have to find out what your class does to it.

In week 6 this has a name: it is called **not sharing mutable state**, and it is the practical half of
encapsulation.
"""),

md("""
---
# Block 2 · Your own operators

Operators do overload. That is the part of overloading Python does have, and it does more for a class's
readability than anything else in this notebook.

`02 - POO/6th Module/Code022.py` covers the topic from its line 70 onwards. One warning, because it
matters: **that file stops at line 62** because of the error we saw last week, so everything after it
never runs when you execute the file. The code in this section is that file's code, checked cell by
cell here.

## What an object without `__str__` prints
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Printing an object that cannot describe itself.
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


p = Point(1, 2)
print(p)
print(f"In an f-string: {p}")
print("In a list:", [Point(1, 2), Point(3, 4)])
"""),

md("""
`<__main__.Point object at 0x...>`, three times, with a different memory address each time.

It is not an error. It is what `object` does by default when nobody tells it otherwise, and it is true
information: the class, and where the object lives. It is just of no use for anything anyone does with
a `print`.

Look at the third line. Inside a list it comes out worse still, because there Python uses `__repr__`
rather than `__str__`, so it will not even respect what you fix with the first one.
"""),

code("""
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


p = Point(1, 2)
print(p)
print(f"In an f-string: {p}")
print("In a list:", [Point(1, 2), Point(3, 4)])
print()
print("str(p): ", str(p))
print("repr(p):", repr(p))
"""),

md("""
Two methods with different jobs.

`__str__` is for the person who will read the output. `__repr__` is for whoever is debugging, and the
convention is that it looks like the call that would build the object. When you only write one, write
`__repr__`: Python falls back to it when `__str__` is missing, so lists come out right too.

And notice what `__str__` does: it **returns** a string. It does not print. That is last week's
sentence, the one about the private method inside the f-string, this time on the right side of it.

## What happens to `==` without `__eq__`
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Two equal points that are not equal.
p1 = Point(1, 2)
p2 = Point(1, 2)

print("p1:", p1, " p2:", p2)
print("p1 == p2?", p1 == p2)
print("p1 is p2?", p1 is p2)
print()
print("Looking for it in a list:", p1 in [Point(1, 2), Point(3, 4)])
print("Putting both in a set:", len({p1, p2}), "elements for two identical points")
items = [Point(1, 2), Point(3, 4)]
try:
    items.remove(Point(1, 2))
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
Two points with the same coordinates, and `==` says no.

By default, `==` between objects asks the same thing as `is`: are these the same object in memory. We
saw that in week 3 and I promised it got fixed today.

What makes the omission expensive is not the bare comparison, it is everything that uses it internally.
`in` over a list compares with `==`. `list.remove` compares with `==`, which is why the last line ended
in `ValueError: list.remove(x): x not in list` with the point right there in front of it. `index`,
`count` and half the tests you will write compare with `==`.
"""),

code("""
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)

print("p1 == Point(1, 2):", p1 == Point(1, 2))
print("p1 + p2:          ", p1 + p2)
print()
points = [Point(1, 2), Point(3, 4), Point(5, 6)]
print("Is Point(3, 4) in the list?", Point(3, 4) in points)
points.remove(Point(3, 4))
print("After remove:", points)
"""),

md("""
`remove` found the point because `in` and `remove` use `__eq__`, and now there is one.

`__add__` returns a **new point**. That decision is not cosmetic: `a + b` should change neither `a` nor
`b`, because nobody reading that line expects it to. When an operator modifies its operands, what
follows is an afternoon of debugging.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. An operator that modifies its left operand.
class MutatingPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        self.x += other.x        # modifies self instead of building a new one
        self.y += other.y
        return self


a = MutatingPoint(1, 2)
b = MutatingPoint(3, 4)

print("Before: a =", a, " b =", b)
c = a + b
print("After:  a =", a, "<- changed with nobody asking it to")
print("        c =", c)
print("Are a and c the same object?", a is c)

total = MutatingPoint(0, 0)
for point in [MutatingPoint(1, 1), MutatingPoint(2, 2)]:
    total = total + point
print()
print("Running total:", total, "<- this one is right, by accident")
"""),

md("""
`a` changed value on a line that only read it, and `c` is not a new point but a second name for `a`. It
is review 4's alias, served up by an operator.

The last part is the uncomfortable one: the accumulating loop gives the right answer. That is why this
bug survives the tests, ships, and surfaces the day somebody adds two points and then uses the first
one again.

**An operator builds and returns.** If you really want the one that modifies in place, it exists and has
its own name: `__iadd__`, which is what backs `+=`.

## The side effect of writing `__eq__`
"""),

code("""
# FAILS ON PURPOSE. Defining __eq__ leaves the class with no hash.
print("Does Point have __hash__?", Point.__hash__)

try:
    group = {Point(1, 2), Point(3, 4)}
except TypeError as e:
    print("TypeError:", e)

try:
    table = {Point(1, 2): "origin"}
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
`unhashable type: 'Point'`. The class lost the ability to go into a set or to be a dictionary key, and
nobody wrote it that way on purpose.

When you define `__eq__`, Python sets `__hash__` to `None`. It sounds arbitrary and it is not: two
objects that are equal have to produce the same hash, or dictionaries stop working. Since Python cannot
guess your new definition of equality, it would rather switch the hash off than leave you one that lies.

The fix is one line, and it has to agree with `__eq__`.
"""),

code("""
class FullPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"FullPoint({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))     # the same data as __eq__


group = {FullPoint(1, 2), FullPoint(1, 2), FullPoint(3, 4)}
print("Distinct points in the set:", len(group))
print(group)
print()
print("As a dictionary key:", {FullPoint(0, 0): "origin"})
"""),

md("""
Three points went into the set, two came out. The duplicate dropped itself, which is exactly what one
wants from a set.

Notice that `__hash__` uses **the same tuple** as `__eq__`. That is the whole rule: if two objects are
equal, their hashes have to match.

## Your class with collection syntax

`Code023.py` builds a tag cloud and keeps adding magic methods until it behaves like a dictionary. It is
worth seeing whole.
"""),

code("""
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        key = tag.lower()
        self.__tags[key] = self.__tags.get(key, 0) + 1

    def __str__(self):
        return str(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __contains__(self, tag):
        return tag.lower() in self.__tags


cloud = TagCloud()
for tag in ["python", "Python", "PYTHON", "sql", "c++"]:
    cloud.add(tag)

print(cloud)
print()
print('cloud["python"]:', cloud["python"])
print('cloud["java"]:  ', cloud["java"], "<- a tag that is not there")
print("len(cloud):     ", len(cloud))
print('"SQL" in cloud: ', "SQL" in cloud)
print()
cloud["c++"] = 10
for tag in cloud:
    print(f"  {tag:<8}{cloud[tag]}")
"""),

md("""
Five tags added, three distinct, and the three spellings of "python" landed in the same count.

That last part is what justifies the class. A bare dictionary would have stored `python`, `Python` and
`PYTHON` separately, and the only way to avoid it would be remembering to write `.lower()` in every
single place the thing is touched. The class remembers for you, and that is a class's job.

The five magic methods give it familiar syntax: brackets to read and write, `len` to count, `in` to ask,
and `for` to walk it. Nobody using your class has to learn anything new.

## How many magic methods your class already had before you wrote one
"""),

code("""
class Empty:
    pass


magic_empty = [n for n in dir(Empty) if n.startswith("__") and n.endswith("__")]
magic_cloud = [n for n in dir(TagCloud) if n.startswith("__") and n.endswith("__")]

print("An empty class already carries", len(magic_empty), "magic methods inherited from object")
print("The tag cloud carries", len(magic_cloud))
print()

SYNTAX = ["__str__", "__getitem__", "__setitem__", "__len__", "__iter__", "__contains__"]
written = [n for n in SYNTAX if n in vars(TagCloud)]
inherited = [n for n in SYNTAX if hasattr(object, n)]

print("Written on the cloud:", len(written), "->", written)
print("Of those, the ones object already had:", len(inherited), "->", inherited)
print()
for name in SYNTAX:
    print(f"  {name:<15}does object have it? {hasattr(object, name)}")
"""),

md("""
A class with nothing but `pass` inside already inherits close to thirty magic methods, which is why
`p1 == p2` worked from day one: `__eq__` was there, it just compared identity.

Of the six that give the cloud its syntax, `object` carried exactly one, `__str__`. That is the
difference between the two cases. When the method exists and does not do what you want, you override it
and the symptom is a quietly wrong result, like the `print` that shows a memory address. When it does
not exist, `len(obj)` raises `TypeError` and you find out at once.

`MagicMethods.md`, in the same module 6 folder, has the full list. It is not for memorising: it is for
knowing it exists, and going there the day you need your class to behave like something familiar.
"""),

md("""
---
# Block 3 · Organising classes

A thousand-line file works exactly as well as ten files of a hundred. The difference shows up when you
have to find something.

The cells in this block **write real files** into the notebook's working directory and then import them.
Run them in order.

## A module is a file
"""),

code("""
from pathlib import Path

Path("sales.py").write_text('''
VAT_RATE = 0.16


def vat(amount: float) -> float:
    return amount * VAT_RATE


print("Hello from the body of sales.py")

if __name__ == "__main__":
    print("This only runs if you execute the file")
''', encoding="utf-8")

print("File written:", Path("sales.py").exists())
print("Lines:", len(Path("sales.py").read_text(encoding="utf-8").splitlines()))
"""),

code("""
import sales

print()
print("sales.__name__ is:", repr(sales.__name__))
print("VAT on 100:", sales.vat(100))
print("The rate:", sales.VAT_RATE)
"""),

md("""
The import printed the loose `print` and did **not** print the `__main__` block.

That is the whole difference between importing and executing. When you import, `__name__` holds the
module's name, `"sales"`. When you run the file directly it holds `"__main__"`, which is why the `if` at
the bottom is the standard way of saying "this is for when you run me, not for when you import me".

Let us see both outputs side by side.
"""),

code("""
import subprocess
import sys

as_script = subprocess.run([sys.executable, "sales.py"],
                           capture_output=True, text=True)
on_import = subprocess.run([sys.executable, "-c", "import sales"],
                           capture_output=True, text=True)

print("Run as a script:")
for line in as_script.stdout.splitlines():
    print("  ", line)

print()
print("Imported from another file:")
for line in on_import.stdout.splitlines():
    print("  ", line)

print()
print("Lines when executed:", len(as_script.stdout.splitlines()))
print("Lines when imported:", len(on_import.stdout.splitlines()))
"""),

md("""
Two lines against one. The `__main__` block ran only in the first case.

And now the uncomfortable part: the loose `print` came out **both** times. Everything outside a function
or a class runs at import time, always, no exceptions. A module that prints, opens a file or connects to
something while being imported turns every `import` into a side effect.

**The convention: any module in the project should be importable without anything visible happening.**
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A module that does work while being imported.
Path("catalogue.py").write_text('''
PRODUCTS = {}

with open("catalogue.txt", "w", encoding="utf-8") as f:
    f.write("file created by catalogue.py")

print("catalogue.py: loading the catalogue...")
''', encoding="utf-8")

print("Does catalogue.txt exist before the import?", Path("catalogue.txt").exists())

import catalogue

print("And afterwards?                          ", Path("catalogue.txt").exists())
print()
print("Nobody called a single function, and the disk has already changed.")
"""),

md("""
An `import` that wrote a file. No call in between.

In a notebook it looks harmless. In a real project this is what makes tests pass or fail depending on
the order modules were imported, makes an `import` take three seconds, or makes running a static
analysis tool send an email.

## Three ways to bring in the same class, and a real package
"""),

code("""
Path("store").mkdir(exist_ok=True)
Path("store/__init__.py").write_text("", encoding="utf-8")

Path("store/cart.py").write_text('''
class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.products = []

    def __repr__(self):
        return f"Cart({self.owner!r}, {len(self.products)} products)"
''', encoding="utf-8")

Path("store/customer.py").write_text('''
class Customer:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Customer({self.name!r})"
''', encoding="utf-8")

print("Package created:")
for path in sorted(Path("store").rglob("*.py")):
    print("  ", path.as_posix())
"""),

code("""
import store.cart
from store.cart import Cart
from store import cart as ct

a = store.cart.Cart("Ana")
b = Cart("Luis")
d = ct.Cart("Sofia")

print(a)
print(b)
print(d)
print()
print("Are all three the same class?",
      type(a) is type(b) is type(d))
print("store modules loaded:",
      sorted(n for n in sys.modules if n.startswith("store")))
"""),

md("""
Three syntaxes, one class. The module loads once and all three names point at the same object.

`import store.cart` brings the whole module. The calls get long, and in exchange you can see where every
name came from.

`from store.cart import Cart` brings a single name. It is the most common form and the quietest inside
the file.

`from store import cart as ct` renames. It earns its keep when two modules share a name, and gets in the
way when it is used to type less.

The fourth one is missing, and it is the one to avoid.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The asterisk brings everything, and the second wins.
Path("colours.py").write_text('''
def render(text):
    return f"[colour] {text}"
''', encoding="utf-8")

Path("dates.py").write_text('''
def render(text):
    return f"[date] {text}"
''', encoding="utf-8")

from colours import *
from dates import *

print(render("hello"))
print()
print("Which of the two won? The one from the last import.")
print("And if somebody swaps those two lines, the program changes behaviour.")
"""),

md("""
`from module import *` brings every public name in the module and drops it into your file. Two modules
with a function of the same name and the second one wins, without a word.

Notice what was lost: reading `render("hello")`, there is no way to tell where that function came from.
With `import colours` and `colours.render(...)`, the line says it by itself.

## Circular imports
"""),

code("""
# FAILS ON PURPOSE. Two modules that import each other.
Path("order.py").write_text('''
import invoice


class Order:
    def bill(self):
        return invoice.Invoice()
''', encoding="utf-8")

Path("invoice.py").write_text('''
from order import Order


class Invoice:
    def __init__(self):
        self.order = Order()
''', encoding="utf-8")

for name in ["order", "invoice"]:
    sys.modules.pop(name, None)

try:
    import order
except ImportError as e:
    print("ImportError:", e)
"""),

md("""
Python loads `order`, whose first line asks for `invoice`, whose first line asks for a name from
`order`, which has not finished loading and therefore does not have that name yet.

The message talks about a "partially initialized" module, and that is the exact description of what
happened.

A circular import is almost never an import problem: **it is a design problem**. If `order` needs
`invoice` and `invoice` needs `order`, either both classes belong in the same module because they are
one idea, or there is a third piece missing that should coordinate them.

## Four ways to organise a project badly

| | The error | When you notice |
|---|---|---|
| 01 | One file with everything | Past three hundred lines, finding a class costs more than rewriting it |
| 02 | One file per class, no exceptions | Ten fifteen-line files to understand a single idea |
| 03 | Circular imports | `ImportError` mid-load, with a message that does not point at the design |
| 04 | Loose code in a module | Every `import` fires the prints, the tests and whatever else is lying around |

**A module earns its place when two classes in the same file no longer read together.** A package earns
its place when the module names start repeating a prefix: if you have `store_cart.py`,
`store_customer.py` and `store_payment.py`, what you have is a folder.
"""),

md("""
---
# Block 4 · Basic modelling

The step almost nobody takes and that decides half the result: draw before you type.

The UML box has three compartments and each one matches a part of the class. The name on top, what it
remembers in the middle, what it knows how to do at the bottom.

```
┌─────────────────────────────┐
│            Loan             │   class Loan:
├─────────────────────────────┤
│ - book: Book                │       def __init__(self, book, member, day):
│ - member: Member            │           self.book = book
│ - day_out: int              │           ...
├─────────────────────────────┤
│ + overdue(day): bool        │       def overdue(self, day): ...
│ + fine(day): float          │       def fine(self, day): ...
└─────────────────────────────┘
```

The minus means private and the plus means public, which is UML notation and not Python's. In Python the
minus is written with two underscores.

## From the brief to the boxes, in five steps

The lab brief:

> The library lends books to members for fourteen days. If a member returns a book late, they pay a fine
> of five pesos per day overdue. A member may not hold more than three books at the same time.

**Step 1. Underline the nouns.** library, book, member, days, fine, day overdue.

**Step 2. Drop the ones that remember nothing.** "Days" and "day overdue" are numbers, not things.
"Fine" is the result of a calculation, so it is probably a method rather than a class.

**Step 3. List what each one remembers.** A book remembers its title and author. A member remembers
their name and what they have out. A loan remembers which book, which member and which day it went out.

**Step 4. Underline the verbs.** lend, return, pay, hold. Each verb goes to the class that owns the data
it works with.

**Step 5. Draw the box.** If the three compartments do not fit on half a page, the class does too much.

Notice that "loan" is not on the list from step 1. It came out of the verb "lend", and it is the most
important class in the model. Nouns are the starting point, not the answer.
"""),

code("""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book({self.title!r})"


class Member:
    MAXIMUM = 3

    def __init__(self, name):
        self.name = name
        self.loans = []

    def may_borrow(self):
        return len(self.loans) < Member.MAXIMUM

    def __repr__(self):
        return f"Member({self.name!r}, {len(self.loans)} books)"


class Loan:
    DAYS = 14
    FINE_PER_DAY = 5.0

    def __init__(self, book, member, day_out):
        self.book = book
        self.member = member
        self.day_out = day_out

    def overdue(self, today):
        return today - self.day_out > Loan.DAYS

    def fine(self, today):
        late = today - self.day_out - Loan.DAYS
        return max(0, late) * Loan.FINE_PER_DAY

    def __repr__(self):
        return f"Loan({self.book.title!r} -> {self.member.name})"


ana = Member("Ana")
catalogue = [Book("The Aleph", "Borges"), Book("Pedro Paramo", "Rulfo"),
             Book("La tregua", "Benedetti"), Book("Aura", "Fuentes")]

for book in catalogue:
    if ana.may_borrow():
        ana.loans.append(Loan(book, ana, 1))
    else:
        print("Refused, over the limit:", book.title)

print()
print(ana)
for loan in ana.loans:
    print(f"  {loan}  overdue on day 20: {loan.overdue(20)}  fine: ${loan.fine(20):.2f}")
"""),

md("""
Three classes, three attributes each, and every rule from the brief lives in exactly one place.

`MAXIMUM` and `DAYS` are class attributes because they are rules of the library and not of each member
or each loan. That is week 3's lesson, used this time for what it is for.

`fine` returns a number rather than printing it, which is why the loop below could line it up in a
column. That is review 3's lesson, again.

## The class almost everyone writes instead
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The class that is a file of functions with a roof.
class LibraryManagerSystem:
    def __init__(self):
        pass

    def lend_book(self, title, member, day):
        return {"title": title, "member": member, "day": day}

    def is_overdue(self, loan, today):
        return today - loan["day"] > 14

    def compute_fine(self, loan, today):
        return max(0, today - loan["day"] - 14) * 5.0

    def may_borrow(self, member_loans):
        return len(member_loans) < 3


system = LibraryManagerSystem()
loan = system.lend_book("The Aleph", "Ana", 1)

print("Loan:", loan)
print("Overdue on 20?", system.is_overdue(loan, 20))
print("Fine:", system.compute_fine(loan, 20))
print()
print("System state:", vars(system))
print("Attributes it remembers:", len(vars(system)))
print()
print("The library moves the loan period from 14 days to 21.")
Loan.DAYS = 21                   # one line, and done

from_model = Loan(Book("The Aleph", "Borges"), ana, 1)
print("  With the model,  overdue on day 20?", from_model.overdue(20))
print("  With the system, overdue on day 20?", system.is_overdue(loan, 20))
print()
print("Same loan, same day, two answers.")
Loan.DAYS = 14
"""),

md("""
It runs, it gives the same numbers, and the object remembers absolutely nothing. `vars(system)` is
empty.

A class whose state is an empty dictionary is not a class, it is a file of functions with a roof on it.
The proof is step 2 of the method: if it keeps nothing between one call and the next, it was a function.
You already met this one in week 2, when we compared the paradigm with structured programming; what is
new is that you now have the vocabulary to say what it is missing.

The second half of the cell is the proof that matters. The library moves to twenty-one days, and in the
model that is one line, `Loan.DAYS = 21`. The loan stops being overdue immediately.

In the manager-system the fourteen is written inside `is_overdue` and again inside `compute_fine`, so
there is no line to change from outside and there are two to hunt for inside. Same loan, same day, two
different answers.

That is the entire argument for modelling. It is not that it looks nicer: it is that each rule from the
brief ends up in one place, and that place has a name.

**The lab criterion: no class may be called Manager, Handler or System.** None of the three is a noun
from the brief, and all three are ways of postponing the decision about what classes there are.
"""),

md("""
---
## Four errors from this session

**Expecting the second `def` to coexist with the first.** Only one survives, the lower one. Default
parameters cover the real case.

**Handing a list to a method that declares `*args`.** One argument arrives, and it is a list, not three
arguments. The unpacking asterisk goes on the calling side.

**Defining `__eq__` and forgetting `__hash__`.** The class stops working as a dictionary key and as a
set element, with a `TypeError` that never mentions `__eq__`.

**Leaving loose code in a module.** It runs at import time, always, and turns every `import` into a side
effect nobody can see from the line that triggers it.
"""),

md("""
---
# Exercises

This week's lab is modelling the library loan, in pairs, handing in the boxes before the code.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The second def

Write a class with two methods of the same name and different signatures. Call the first signature,
catch the error, and print the class dictionary to show only one survived.

Then rewrite it with a default value and try both ways of calling it.

### Exercise 2 · However many

Write a class `Log` with a method `record(*messages)` that accepts zero, one or several. Try all three
counts and count the lines.

Then call it with a list and no asterisk, and show what actually got stored.

### Exercise 3 · Named options

Add to `Log` a `**options` that accepts `uppercase=True` and `prefix="..."`. Call it with a correctly
spelled option and a misspelled one, and show that the second does nothing and says nothing.

Add the check that does say something.

### Exercise 4 · The list in the signature

Write a class with a list as a default value in the constructor. Create two objects, add to one, and
show with `is` that they share the list.

Print the constructor's `__defaults__` to show where that list lives, then fix it.

### Exercise 5 · Make it printable

Write `Fraction` with a numerator and a denominator. Print it before writing `__str__` and after. Add
`__repr__` and show the difference by putting two fractions in a list.

### Exercise 6 · Make it comparable

Add `__eq__` to `Fraction` so that 1/2 equals 2/4. Check it with `in` over a list and with `remove`.

Then put two fractions in a set, catch the `TypeError`, and fix it with `__hash__`.

### Exercise 7 · Make it addable

Add `__add__` to `Fraction` so that it returns a new fraction. Show with `is` that both operands came
out untouched.

Then deliberately write the version that modifies `self` and show where it shows.

### Exercise 8 · A package

Create a package `library` with two modules, one for `Book` and one for `Member`, and an
`if __name__ == "__main__"` in each. Import them all three ways and check the class is the same one.

Then run one of the two as a script and compare the outputs.

### Exercise 9 · The lab

Model the library loan. Who borrows, what is lent, when it falls due and who collects the fine.

At most four classes and three attributes per class, with the methods declared and their bodies empty.
Hand in a diagram with the boxes and a `.py` file with the classes and their method signatures.

No class may be called Manager, Handler or System, because none of the three is a noun from the problem.
"""),

md("""
---
## Three things to take away

**Python does not overload by signature.** The second `def` overwrites the first because a method name
is a dictionary entry. Defaults, `*args` and `**kwargs` cover the real case with less code.

**Operators do overload.** `__str__`, `__eq__` and `__add__` give your class the syntax everyone already
knows, and the missing one shows up in the least expected place: a `remove` that finds nothing, or a
`print` that shows a memory address.

**The model gets drawn before it gets written.** Nouns to boxes, verbs to methods, and only then the
editor. The five steps take ten minutes and save the afternoon you discover the wrong class holds the
data.

That closes topic 2. Week 6 opens topic 3 with encapsulation, information hiding and reuse, and that is
where everything so far comes due: week 4's property, the shared state we have been dragging since
review 3, and the defensive copy from block 1 today.

### An exercise for the week

Take the longest file you have written this term and split it into modules without changing a single
line of logic. If you cannot, it is because something depends on everything, and that is exactly what
needs finding.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


calc = Calculator()

try:
    calc.add(1, 2)
except TypeError as e:
    print("TypeError:", e)

print(vars(Calculator))
print("Methods:", [n for n in vars(Calculator) if not n.startswith("__")])


class GoodCalculator:
    def add(self, a, b, c=0):
        return a + b + c


good = GoodCalculator()
print(good.add(1, 2), good.add(1, 2, 3))
```

### Exercise 2

```python
class Log:
    def __init__(self):
        self.lines = []

    def record(self, *messages):
        for message in messages:
            self.lines.append(message)


a = Log()
a.record()
a.record("one")
a.record("two", "three", "four")
print(a.lines, "->", len(a.lines), "lines")

b = Log()
b.record(["one", "two"])
print(b.lines, "->", len(b.lines), "line")
print("Type of the first:", type(b.lines[0]).__name__)

# With the list and no asterisk one single line got stored, and it is a list. The
# method does not unpack: it collects whatever was sent.
```

### Exercise 3

```python
class Log:
    KNOWN = {"uppercase", "prefix"}

    def __init__(self, strict=False):
        self.lines = []
        self.strict = strict

    def record(self, *messages, **options):
        if self.strict:
            unknown = set(options) - Log.KNOWN
            if unknown:
                raise TypeError(f"unknown option: {sorted(unknown)}")
        prefix = options.get("prefix", "")
        for message in messages:
            text = f"{prefix}{message}"
            self.lines.append(text.upper() if options.get("uppercase") else text)


a = Log()
a.record("spelled right", uppercase=True)
a.record("spelled wrong", upercase=True)
for line in a.lines:
    print(" ", line)

strict = Log(strict=True)
try:
    strict.record("x", upercase=True)
except TypeError as e:
    print("TypeError:", e)
```

### Exercise 4

```python
class BrokenGroup:
    def __init__(self, code, students=[]):
        self.code = code
        self.students = students

    def enrol(self, name):
        self.students.append(name)


one = BrokenGroup("01")
two = BrokenGroup("02")
one.enrol("Ana")

print("Group 1:", one.students)
print("Group 2:", two.students)
print("The same list?", one.students is two.students)
print("Where it lives:", BrokenGroup.__init__.__defaults__)


class Group:
    def __init__(self, code, students=None):
        self.code = code
        self.students = list(students) if students else []

    def enrol(self, name):
        self.students.append(name)


one = Group("01")
two = Group("02")
one.enrol("Ana")
print("Now:", one.students, two.students, one.students is two.students)
```

### Exercise 5

```python
from math import gcd


class MuteFraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den


print(MuteFraction(1, 2))


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"


f = Fraction(1, 2)
print(f)
print([Fraction(1, 2), Fraction(3, 4)])

# Inside a list Python uses __repr__, not __str__. If you are only going to write
# one, write __repr__: print falls back to it when __str__ is missing.
```

### Exercise 6

```python
class Fraction:
    def __init__(self, num, den):
        factor = gcd(num, den)
        self.num = num // factor
        self.den = den // factor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __eq__(self, other):
        return (self.num, self.den) == (other.num, other.den)


print(Fraction(1, 2) == Fraction(2, 4))

fractions = [Fraction(1, 2), Fraction(3, 4)]
print(Fraction(2, 4) in fractions)
fractions.remove(Fraction(2, 4))
print(fractions)

try:
    {Fraction(1, 2), Fraction(2, 4)}
except TypeError as e:
    print("TypeError:", e)


class FullFraction(Fraction):
    def __hash__(self):
        return hash((self.num, self.den))


print(len({FullFraction(1, 2), FullFraction(2, 4), FullFraction(3, 4)}))

# Reducing in the constructor is what makes 1/2 and 2/4 the same pair of numbers,
# and therefore what makes __eq__ and __hash__ agree without any effort.
```

### Exercise 7

```python
class Fraction:
    def __init__(self, num, den):
        factor = gcd(num, den)
        self.num = num // factor
        self.den = den // factor

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)


a = Fraction(1, 2)
b = Fraction(1, 3)
c = a + b

print(a, "+", b, "=", c)
print("Did a change?", a, "· is c a?", c is a)


class MutatingFraction(Fraction):
    def __add__(self, other):
        self.num = self.num * other.den + other.num * self.den
        self.den = self.den * other.den
        return self


a = MutatingFraction(1, 2)
b = MutatingFraction(1, 3)
c = a + b
print("a ended up as", a, "and c is a:", c is a)

# The running total comes out right with both versions, which is why the bug
# passes the tests. It shows the day somebody adds and then reuses the left
# operand.
```

### Exercise 8

```python
from pathlib import Path
import sys, subprocess

Path("library").mkdir(exist_ok=True)
Path("library/__init__.py").write_text("", encoding="utf-8")

Path("library/book.py").write_text('''
class Book:
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f"Book({self.title!r})"


if __name__ == "__main__":
    print("test:", Book("The Aleph"))
''', encoding="utf-8")

Path("library/member.py").write_text('''
class Member:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Member({self.name!r})"


if __name__ == "__main__":
    print("test:", Member("Ana"))
''', encoding="utf-8")

import library.book
from library.book import Book
from library import book as bk

print(type(library.book.Book("A")) is type(Book("B")) is type(bk.Book("C")))

output = subprocess.run([sys.executable, "library/book.py"],
                        capture_output=True, text=True)
print("As a script:", output.stdout.strip() or "(no output)")
print("On import: no output, which is how it should be")
```

### Exercise 9

```python
class Book:
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def details(self) -> str:
        ...


class Member:
    MAX_AT_ONCE = 3

    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number
        self.loans: list["Loan"] = []

    def may_borrow(self) -> bool:
        ...


class Loan:
    DAYS = 14

    def __init__(self, book: Book, member: Member, day_out: int) -> None:
        self.book = book
        self.member = member
        self.day_out = day_out

    def overdue(self, today: int) -> bool:
        ...

    def days_late(self, today: int) -> int:
        ...


class Fine:
    PER_DAY = 5.0

    def __init__(self, loan: Loan, days_late: int) -> None:
        self.loan = loan
        self.days_late = days_late
        self.paid = False

    def amount(self) -> float:
        ...
```

Four decisions worth defending when you hand this in.

**There is no `Library` class.** The brief mentions one, but it holds nothing the other four do not hold
already. The moment it has a list of books and a list of members it earns its place; with this brief, it
does not.

**`Fine` is a class rather than a method.** That was decided at step 3: a fine remembers whether it has
been paid, and that survives the operation that created it. If the brief said nothing about paying,
`fine()` would be a method on `Loan` and that would be enough.

**`Loan` holds the whole `Book` object**, not the title. That way there are not two places where the
title could differ. It is week 2's lesson inside a model.

**Constants live on the class they belong to.** The period belongs to the loan, the simultaneous limit
to the member, the rate to the fine. When the library changes its rules, each number is in one place and
you know which.
"""),

]

write(OUT / "en" / "w05.ipynb", en)
print("wrote", OUT / "en" / "w05.ipynb")
