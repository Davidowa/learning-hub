"""notebooks/programacion-orientada-a-objetos/en/w06.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w06.en.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code023.py
                  (the tag cloud, open and closed, and the KeyError at the end)
              docs/en/courses/python-course/02 - POO/6th Module/Code021.py
                  (composition: CPU, RAM, HardDrive and Computer)

Both files run to the end, checked.

This is the week the threads running since review 3 point at: the default list,
review 4's alias and week 3's class attribute. Block 2 collects on them
explicitly.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 06
## Topic 3 · Core properties

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Putting data together with whatever looks after it, deciding what shows from outside, and reusing
without inheriting.

This notebook settles an old debt. Since review 3 I have been promising that week 6 would make clear
why two objects end up sharing state without anyone asking for it. That paragraph arrives in block 2,
and you now have all the vocabulary needed to read it.

By the end you will be able to:

1. Tell encapsulating from hiding, which are not the same decision and are not taken at the same time.
2. Design a public interface and defend what was left out of it.
3. Spot a leak: the getter that hands back the internal structure and undoes all the work.
4. Apply the change test to find out whether a piece of data is stored in the right place.
5. Reuse by composition, and say in which case inheritance does earn its place.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Ten fail on purpose and carry a comment saying so.

Seven of the ten **raise no exception at all**. That proportion is no accident this week: an
encapsulation leak never raises. It produces a program that works today and breaks the day somebody
changes something they thought was internal.
"""),

md("""
---
# Block 1 · Encapsulation

The word sounds like a padlock, and to begin with that is not what it means.

**Encapsulating** is putting a piece of data and the behaviour that looks after it in the same class.
Nothing more.

**Hiding** is the later and separate decision not to let that data be seen from outside.

You can encapsulate without hiding anything, and that is where the trouble starts. The class below is
encapsulated: the dictionary and the rule that normalises it live together. It is not hidden.
"""),

code("""
class OpenCloud:
    def __init__(self) -> None:
        self.tags = {}               # public

    def add(self, tag: str) -> None:
        key = tag.lower()            # the class's only rule
        current = self.tags.get(key, 0)
        self.tags[key] = current + 1


cloud = OpenCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PYTHON")
cloud.add("sql")

print(cloud.tags)
print("Distinct tags:", len(cloud.tags))
"""),

md("""
Three spellings of "python" and a single key. The rule works.

The rule is `tag.lower()`, it lives inside `add`, and that is all the encapsulation this class has.
Anyone using `add` never needs to know it exists.

The trouble is that `add` is not the only door.
"""),

code("""
# FAILS ON PURPOSE. Reading a key that is not there, through the back door.
try:
    print(cloud.tags["c++"])
except KeyError as e:
    print("KeyError:", e)

print()
print("The same question, with the answer one would want:",
      cloud.tags.get("c++", 0))

print()
try:
    print(len(cloud))
except TypeError as e:
    print("TypeError:", e)
print("You have to know there is a dictionary inside:", len(cloud.tags))
"""),

md("""
Two symptoms of the same thing.

`cloud.tags["c++"]` blows up because asking about a tag nobody used goes through the dictionary, and a
dictionary answers with `KeyError`. That is not the answer the problem asks for: the answer is zero.

And `len(cloud)` does not even exist. To count you have to write `len(cloud.tags)`, which forces anyone
using the class to know there is a dictionary inside. Right there, on that line, the internal detail
became part of the contract without anybody deciding it.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Writing straight into the dictionary.
cloud.tags["Python"] = 99            # capitalised, skipping the rule

print(cloud.tags)
print("Distinct tags:", len(cloud.tags), "<- there were 2")
print()
print('cloud.tags["python"]:', cloud.tags["python"])
print('cloud.tags["Python"]:', cloud.tags["Python"])
print()
cloud.add("PYTHON")
print("After adding PYTHON again:", cloud.tags)
print("The 99 sits in a key that add will never touch.")
"""),

md("""
Two keys for the same tag, and the class never heard about it.

Whoever wrote that line was not sabotaging anything. They were using a public dictionary, which is
exactly what the class offered them. The normalising rule exists, but it only applies if you come in
through `add`, and nobody is making you.

That is the difference between encapsulating and hiding, and it fits in one question: **who has to
remember this rule?** If it lives inside the class and there is no other door, nobody. If the attribute
is open, every file that touches it, and one of them will forget.

## The rule that moves out of the class
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The rule repeated at every call site.
other = OpenCloud()

# Three different files in the project, each remembering to normalise:
other.tags["python"] = other.tags.get("python", 0) + 1     # file A
other.tags["sql".lower()] = 1                              # file B
other.tags["C++"] = 1                                      # file C, forgot

print(other.tags)
print()
lower = [k for k in other.tags if k == k.lower()]
print(f"{len(lower)} of {len(other.tags)} keys respect the rule")
print("The one that does not:", [k for k in other.tags if k != k.lower()])
"""),

md("""
Two out of three. The third was written in another file, by another person, six months later.

When the rule is repeated at every call site, the rule no longer lives in the class. It lives in a
team's memory, and that memory has turnover.

**If three files call `.lower()` before calling your method, the rule is in the wrong place.**

## The same class, with the dictionary inside
"""),

code("""
class Cloud:
    def __init__(self) -> None:
        self.__tags: dict[str, int] = {}

    def add(self, tag: str) -> None:
        key = tag.lower()
        self.__tags[key] = self.__tags.get(key, 0) + 1

    def __getitem__(self, tag: str) -> int:
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag: str, count: int) -> None:
        self.__tags[tag.lower()] = count

    def __len__(self) -> int:
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __repr__(self) -> str:
        return f"Cloud({self.__tags})"


closed = Cloud()
for tag in ["Python", "python", "PYTHON", "sql"]:
    closed.add(tag)

print(closed)
print()
print('closed["c++"]:', closed["c++"], "<- zero rather than KeyError")
closed["Python"] = 99                # the very same line as before
print("After closed['Python'] = 99:", closed)
print("Distinct tags:", len(closed))
"""),

md("""
The same line that created a duplicate key a moment ago now goes in through `__setitem__`, gets
normalised, and updates the key that was already there.

And `closed["c++"]` returned zero instead of blowing up, because asking about a tag nobody has used is
not an error: it is a question whose answer is zero.

Notice what did **not** change: the rule is still a single line, `tag.lower()`, written twice inside
the class. What changed is that there is no other door.

## The two clouds, counted
"""),

code("""
OPERATIONS = ["Python", "python", "PYTHON", "SQL", "sql", "C++"]

open_one = OpenCloud()
for tag in OPERATIONS:
    open_one.tags[tag] = open_one.tags.get(tag, 0) + 1

clean = Cloud()
for tag in OPERATIONS:
    clean.add(tag)

print("With the dictionary open, touched from outside:")
print("  ", open_one.tags)
print("  ", len(open_one.tags), "keys for", len(set(t.lower() for t in OPERATIONS)),
      "real tags")
print()
print("With the class closed:")
print("  ", clean)
print("  ", len(clean), "keys for", len(set(t.lower() for t in OPERATIONS)),
      "real tags")
"""),

md("""
Six keys against three, from exactly the same six operations.

That is the measured cost of leaving the internal structure open. There is no error, there is no
exception, there is a tag report claiming "Python" and "python" are different things and a user who
cannot see why.
"""),

md("""
---
# Block 2 · Information hiding

Everything you leave visible is a promise. The smaller the interface, the fewer promises to keep.

| Member | What it is | Who uses it |
|---|---|---|
| `add` | Public contract | Anyone |
| `__getitem__` | Public contract | The bracket operator |
| `__len__` | Public contract | The `len` function |
| `__tags` | Internal detail | Only the class |
| `tag.lower()` | Internal detail | Only the class |

The table reads in one direction that matters: the top half you cannot change without warning, the
bottom half you can.

## The change test

A piece of data is properly encapsulated if you **can change how it is stored inside without touching a
single line outside the class**.

That is not an opinion, it is a test you run. Here it is.
"""),

code("""
def check(cls):
    \"\"\"The same six checks, against any cloud that honours the contract.\"\"\"
    cloud = cls()
    for tag in ["Python", "python", "sql"]:
        cloud.add(tag)

    checks = [
        ("python counts 2", cloud["python"] == 2),
        ("PYTHON counts 2", cloud["PYTHON"] == 2),
        ("sql counts 1", cloud["sql"] == 1),
        ("c++ counts 0", cloud["c++"] == 0),
        ("there are 2 tags", len(cloud) == 2),
        ("it can be walked", sorted(cloud) == ["python", "sql"]),
    ]
    return checks


for name, ok in check(Cloud):
    print(f"  {'OK ' if ok else 'NO '}{name}")

print()
print("Passed:", sum(1 for _, ok in check(Cloud) if ok), "of 6")
"""),

code("""
class PairCloud:
    \"\"\"No dictionary inside. From outside you cannot tell.\"\"\"

    def __init__(self) -> None:
        self.__pairs: list[list] = []          # [[key, count], ...]

    def __find(self, key):
        for pair in self.__pairs:
            if pair[0] == key:
                return pair
        return None

    def add(self, tag: str) -> None:
        key = tag.lower()
        pair = self.__find(key)
        if pair is None:
            self.__pairs.append([key, 1])
        else:
            pair[1] += 1

    def __getitem__(self, tag: str) -> int:
        pair = self.__find(tag.lower())
        return pair[1] if pair else 0

    def __setitem__(self, tag: str, count: int) -> None:
        pair = self.__find(tag.lower())
        if pair is None:
            self.__pairs.append([tag.lower(), count])
        else:
            pair[1] = count

    def __len__(self) -> int:
        return len(self.__pairs)

    def __iter__(self):
        return iter(key for key, _ in self.__pairs)


results = check(PairCloud)
for name, ok in results:
    print(f"  {'OK ' if ok else 'NO '}{name}")

print()
print("Passed:", sum(1 for _, ok in results if ok), "of 6")
print("Lines of the check function that had to change: 0")
"""),

md("""
Six out of six, from an implementation that looks nothing like the first one inside, and the test
function was used exactly as written.

That is information hiding doing its job. The dictionary was never part of the contract, so swapping it
for a list of pairs broke nobody. Had `tags` been public, this same test would have needed rewriting on
every line that touched it.

The test works in reverse too, and that is where it helps you design: when you are unsure whether an
attribute should be public, ask yourself **whether you are willing to keep its exact shape for the next
two years**. If not, close it today.

## What the interface promised without anyone writing it down

Look at one line of the test function: `sorted(cloud) == ["python", "sql"]`. That `sorted` is not
decoration.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The ordering nobody promised and everybody uses.
class AlphabeticCloud(Cloud):
    \"\"\"Same contract, same methods, a different internal decision about walking.\"\"\"

    def __iter__(self):
        return iter(sorted(super().__iter__()))


def report(cloud):
    return " · ".join(f"{t}={cloud[t]}" for t in cloud)


ENTRIES = ["zeta", "alpha", "middle", "alpha"]

original = Cloud()
alphabetic = AlphabeticCloud()
for tag in ENTRIES:
    original.add(tag)
    alphabetic.add(tag)

print("Report from the first: ", report(original))
print("Report from the second:", report(alphabetic))
print()
print("Are the two reports equal?", report(original) == report(alphabetic))
print("And the same tags?       ", sorted(original) == sorted(alphabetic))
print("The same counts?         ",
      {t: original[t] for t in original} == {t: alphabetic[t] for t in alphabetic})
"""),

md("""
The same tags, the same counts, and two different reports.

Neither class broke the contract in the table: `add`, brackets, `len`. What changed is the walking
order, which **was never in the table** and which was nonetheless promised the moment the class exposed
`__iter__`.

That is the edge of this block. Every public method promises more than its name says: it promises its
result, its ordering, its speed, and even the exact type it hands back. That is why the test function
two cells ago wrote `sorted(cloud)` rather than `list(cloud)`: so as not to depend on something it did
not want to keep.

When you write an interface, the question is not only which methods you expose. It is **what can be
observed through them**.

## Predict before you run

```python
class Cart:
    def __init__(self):
        self.__products = []

    def fetch(self):
        return self.__products


c = Cart()
c.fetch().append("X1")
print(len(c.fetch()))
```

- **A.** 0, because `__products` is private.
- **B.** 1, because the getter handed back the real list.
- **C.** `AttributeError`, `fetch` cannot touch `__products`.
- **D.** `TypeError`, you cannot append to a method.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The leak: a getter that hands back the internals.
class LeakyCart:
    def __init__(self):
        self.__products = []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def fetch(self):
        return self.__products           # hands back the list, not a copy


cart = LeakyCart()
cart.add("X1")

print("Through the front door:", cart.fetch())

cart.fetch().append("unvalidated junk")
cart.fetch().append(42)

print("Through the leak:      ", cart.fetch())
print("Products:", len(cart.fetch()))
print()
print("Is the validation still worth anything?")
try:
    cart.add("Z9")
except ValueError as e:
    print("  Through add:", e)
print("  Through fetch: none at all. The list takes whatever.")
"""),

md("""
The quiz answer is **B**.

`fetch` handed back **the list**, not a copy, and from that moment whoever holds it can do as they
please. The validator in `add` is still there, untouched, and completely bypassed.

The two underscores protected the attribute's **name**. They did not protect the object inside it.
Encapsulating a name does not encapsulate a list.

**And here is the paragraph I have been promising since review 3.**

When two names point at the same mutable object, writing through either one is seen through both. That
is what happened in review 3 with the default list, which was one single list for every call. It is what
happened in review 4 with `b = a`, which copied nothing. It is what happened in week 3 with the cart
declared in the class body, which was one single cart for every object. It is what happened in week 5
with the list in the constructor's signature.

And it is what just happened here, with the difference that this time the second name is **outside the
class**, in the hands of somebody who does not even know a rule exists.

All four are the same sentence: **assignment does not copy**. What changes is who ends up with the
second name.

## The two fixes, and the one that is not enough
"""),

code("""
class CopyingCart:
    def __init__(self):
        self.__products = []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def fetch(self):
        return list(self.__products)     # a copy


class TupleCart:
    def __init__(self):
        self.__products = []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def fetch(self):
        return tuple(self.__products)    # something that cannot be modified


for cls in [CopyingCart, TupleCart]:
    c = cls()
    c.add("X1")
    try:
        c.fetch().append("junk")
    except AttributeError as e:
        print(f"{cls.__name__:<14}AttributeError: {e}")
    else:
        print(f"{cls.__name__:<14}the append worked, but on the copy")
    print(f"{'':<14}Real products: {len(c.fetch())}")
"""),

md("""
Both close the leak, and they do it in different ways.

`list(...)` hands back a copy. The outside `append` works and affects nobody, because the list it
modified is no longer the cart's.

`tuple(...)` hands back something that cannot be modified. The `append` blows up with an
`AttributeError`, and whoever wrote it finds out on the spot rather than believing they did something.

I prefer the tuple when I can. An error that raises on the wrong line is worth more than a silence that
works.

## The same leak, the other way round

We closed the way out. The way in is still open.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The class keeps the list it was handed.
class KeepingCart:
    def __init__(self, initial=None):
        self.__products = initial if initial is not None else []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def how_many(self):
        return len(self.__products)


mine = ["X1", "X2"]
cart = KeepingCart(mine)
print("At construction:", cart.how_many())

mine.append("unvalidated junk")          # touching my own list, not the cart's
mine.append(42)

print("After touching my list:", cart.how_many())
print("My list:", mine)
print()


class CopyingConstructorCart:
    def __init__(self, initial=None):
        self.__products = list(initial) if initial else []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def how_many(self):
        return len(self.__products)


mine = ["X1", "X2"]
safe = CopyingConstructorCart(mine)
mine.append("unvalidated junk")
print("With a defensive copy:", safe.how_many(), "<- it stayed at 2")
"""),

md("""
The cart grew without anyone calling `add`.

It is the leak from two cells ago in reverse. There the list went out of the class; here it came in, and
the person who built it kept the other name. The attribute is private, the validation exists, and the
object's state is controlled by somebody outside who does not know there are rules.

`list(initial)` in the constructor closes that door, and it is exactly the line that turned up in week 5
when we fixed the default value. It is called a **defensive copy**, and the rule is short: **copy what
comes in and copy what goes out.**

Now the fix that looks like a fix.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The copy that only copies the top level.
class Order:
    def __init__(self, customer):
        self.__customer = customer
        self.__lines = [{"sku": "X1", "quantity": 1}]

    def add(self, sku, quantity):
        if quantity <= 0:
            raise ValueError("the quantity has to be positive")
        self.__lines.append({"sku": sku, "quantity": quantity})

    def fetch(self):
        return list(self.__lines)        # copies the list, not the dictionaries

    def total(self):
        return sum(line["quantity"] for line in self.__lines)


order = Order("Ana")
order.add("X2", 3)

print("Total before:", order.total())

copy_of = order.fetch()
copy_of.append({"sku": "X9", "quantity": 5})   # this one stays outside
copy_of[0]["quantity"] = -1000                 # this one does not

print("Total after:", order.total())
print("Lines on the order:", len(order.fetch()))
print("First line:", order.fetch()[0])
"""),

md("""
The `append` on the copy never reached the order. The assignment inside the first line did.

`list(other_list)` builds a new list **with the same references inside**. The dictionaries were not
duplicated: the copy and the original point at the same ones. It is called a shallow copy, and it is the
half-fix I have seen more often than any other.

The ways out: `copy.deepcopy`, which duplicates everything downwards and costs what it costs; storing
immutable objects instead of dictionaries, which in week 8 becomes a class with `__eq__`; or not handing
back the structure at all and offering instead the methods that answer the questions people actually
ask, like `total()`.

The third is almost always the right one. **If nobody needs the list, do not hand it back.**

## Closing everything is not the answer either
"""),

code("""
# FAILS ON PURPOSE. A class where nothing is public.
class SealedInventory:
    def __init__(self):
        self.__products = {}

    def __add(self, sku, quantity):
        self.__products[sku] = quantity

    def __count(self):
        return len(self.__products)


inv = SealedInventory()
public = [n for n in dir(inv) if not n.startswith("_")]
print("Public members:", public, "->", len(public))

try:
    inv.__add("X1", 5)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("The only way to use it:")
inv._SealedInventory__add("X1", 5)
print("  inv._SealedInventory__add('X1', 5)")
print("  products:", inv._SealedInventory__count())
"""),

md("""
Zero public members, and the class is useless until somebody types the mangled name.

The moment the first person writes `inv._SealedInventory__add(...)`, that name has become the de facto
contract, and now you cannot change it without breaking their program. Closing everything did not
produce a safer class, it produced a worse interface with the same commitments.

**Start with everything public and close what you have a reason to close.** It is week 4's rule, and here
you can see why: the public interface is not what is left after closing, it is a design decision taken
by looking at who is going to use the class.

## Four ways to half-encapsulate

| | The error | How it looks |
|---|---|---|
| 01 | Encapsulate, then hand it back whole | The getter returns the internal list and anyone modifies it |
| 02 | Confusing encapsulating with hiding | Two underscores on everything, with no promise behind them |
| 03 | Closing everything on day one | The class is no use to anyone and you open it on the first request |
| 04 | The rule repeated outside the class | Three files call `.lower()` and the fourth forgets |
"""),

md("""
---
# Block 3 · Reuse

Three ways of not writing the same code twice, in order of increasing commitment.

**A function.** The behaviour depends on no state, so it does not need a class. It is the cheapest and
the one almost nobody considers.

**Composition.** The class takes instances of others and delegates the work that is not its own.
Changing a part costs one line.

**Inheritance.** The class takes its parent's behaviour and is tied to every change the parent makes. It
is the most rigid of the three and the one most often used out of habit.

`Code021.py` in module 6 builds a computer by composition. It is the deck's example.
"""),

code("""
class CPU:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def execute(self):
        print(f"  {self.brand} {self.model}: executing...")


class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity

    def read(self, file):
        print(f"  {self.capacity} hard drive: reading {file}...")


class Computer:
    def __init__(self, cpu, drive):
        self.cpu = cpu
        self.drive = drive

    def start(self, program):
        self.drive.read(f"{program}.exe")
        self.cpu.execute()


mine = Computer(CPU("Intel", "i7"), HardDrive("1TB"))
mine.start("Photoshop")
"""),

md("""
`Computer` inherits from nothing. It takes the parts already built and asks them for what it needs.

Notice what `Computer` knows about a drive: that it has a method called `read`. It does not know whether
it is spinning, solid state or sitting in a data centre, and it does not need to.
"""),

code("""
class SSD:
    def __init__(self, capacity):
        self.capacity = capacity

    def read(self, file):
        print(f"  {self.capacity} SSD: reading {file} (fast)...")


class NetworkDrive:
    def __init__(self, server):
        self.server = server

    def read(self, file):
        print(f"  Network: asking {self.server} for {file}...")


drives = [HardDrive("1TB"), SSD("500GB"), NetworkDrive("nas.local")]
built = []
for drive in drives:
    machine = Computer(CPU("Intel", "i7"), drive)
    machine.start("Photoshop")
    built.append(machine)

print()
print(f"{len(drives)} different drives, {len(built)} computers built")
print("Computer classes involved:", len({type(c) for c in built}))
print("The only thing Computer asks of them:  a method called read ->",
      all(hasattr(d, "read") for d in drives))
print("What else they have in common:",
      sorted(set.intersection(*[{n for n in dir(d) if not n.startswith("_")}
                                for d in drives])))
"""),

md("""
Three different drives, not one line of `Computer` touched, and a single `Computer` class in all three
cases.

The last line is the one that counts: the only thing the three drives have in common is the `read`
method. They share no parent class, no attributes, and they do not know about each other.

That is what makes composition flexible: the commitment between `Computer` and its parts is a method,
not a hierarchy. Any object that knows how to `read` will do.

In week 8 this gets a name. It is called **polymorphism**, and what you just wrote is the version Python
prefers: no base class, no declarations, nothing but the method that is needed.

## Inheritance used where it does not belong
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Inheriting in order to reuse, instead of composing.
class InheritingComputer(HardDrive, CPU):
    def __init__(self, capacity, brand, model):
        HardDrive.__init__(self, capacity)
        CPU.__init__(self, brand, model)

    def start(self, program):
        self.read(f"{program}.exe")
        self.execute()


odd = InheritingComputer("1TB", "Intel", "i7")
odd.start("Photoshop")

print()
print("Is a computer a hard drive?", isinstance(odd, HardDrive))
print("Is a computer a CPU?       ", isinstance(odd, CPU))
print("The computer's capacity:   ", odd.capacity)
print("Methods now on show:",
      sorted(n for n in dir(odd) if not n.startswith("_")))
"""),

md("""
It runs, it prints the same thing, and now a computer **is** a hard drive.

Nothing raises. What broke is the model: `odd.read("anything.txt")` is a legal call, the computer has a
`capacity` attribute that belongs to the drive, and if tomorrow you want two drives there is no way to
have them.

The proof is in the word. Inheritance says **"is a"**: a `Truck` is a `Vehicle`, a `Dog` is an `Animal`.
Composition says **"has a"**: a computer has a drive. When the "is a" sentence sounds odd out loud,
inheritance was not it.

It is the same error `Code021.py` flags with the chicken that inherits from `Bird` and therefore flies.
Week 7 gives it a whole block.

## What inheritance costs when the parent changes
"""),

code("""
# FAILS ON PURPOSE. The fragile base class.
class Store:
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value


class LoggingStore(Store):
    def __init__(self):
        super().__init__()
        self.log = []

    def save(self, key, value):
        self.log.append(key)
        super().save(key, value)


a = LoggingStore()
a.save("x", 1)
print("Works:", a._data, a.log)


# Six months later, somebody renames the method on the base class.
class Store:
    def __init__(self):
        self._data = {}

    def write(self, key, value):          # it used to be called save
        self._data[key] = value


class LoggingStore(Store):
    def __init__(self):
        super().__init__()
        self.log = []

    def save(self, key, value):
        self.log.append(key)
        super().save(key, value)


b = LoggingStore()
try:
    b.save("x", 1)
except AttributeError as e:
    print("AttributeError:", e)
"""),

md("""
The child class did not change a single line and stopped working.

It is called the **fragile base class problem**: a subclass depends on its parent's internal details, so
a change the parent considers internal breaks every descendant. The longer the chain, the further the
damage travels.

With composition this does not happen the same way. If `LoggingStore` took a store in its constructor
and delegated to it, the rename would break one line, the delegating one, and in a place you can see.

**Composition is preferred because one part changes without touching the others.** Inheritance earns its
place when there really is an "is a" relationship, and week 7 is devoted to that case.

## When neither: a function
"""),

code("""
def normalise(tag: str) -> str:
    return tag.strip().lower()


print(normalise("  Python  "))
print(normalise("SQL"))
print()
print("No class, no inheritance, no composition. It keeps nothing between calls.")
print("It is step 2 of last week's modelling method, applied in reverse.")
"""),

md("""
Before deciding between composition and inheritance, it is worth asking whether a class is needed at
all.

If the behaviour depends on no state, a loose function does the job, tests in two lines, and forces
nobody to build an object in order to use it. It is the cheapest of the three options and the least
considered, because it sounds like you are not doing OOP.
"""),

md("""
---
## Four errors from this session

**The getter that hands back the internal structure.** The list leaves the class and from then on
anybody modifies it without going through any validation. Return a copy, a tuple, or better: do not
return it.

**The shallow copy.** `list(other)` duplicates the container and not the contents. If there are
dictionaries or objects inside, they are still the same ones.

**Closing everything on day one.** A class with no public members is no use to anyone, and the first
person to type the mangled name turns that name into the contract.

**Inheriting in order to reuse.** If the "is a" sentence sounds odd, it was composition. And once
inherited, any change in the parent travels downwards.
"""),

md("""
---
# Exercises

This week's lab is closing an inventory without changing the test file. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The back door

Write a class with a public dictionary and a rule inside a method. Use it properly three times, then
write straight into the dictionary skipping the rule, and show with a count how many extra keys were
left behind.

### Exercise 2 · Closing it

Close the class from exercise 1 with two underscores and give it `__getitem__`, `__setitem__`, `__len__`
and `__iter__`. Repeat the same operations and compare the two counts.

### Exercise 3 · The change test

Write a function `check(cls)` with six checks against your closed class. Then write a second
implementation that uses a list of pairs internally instead of a dictionary.

Run the same function against both and report how many passed. If you had to change the function, say
which part of the contract had escaped you.

### Exercise 4 · The leak

Write a class with a private list, a method that validates before adding, and a getter that hands the
list back as is. Push junk in through the leak and show that the validation never heard about it.

### Exercise 5 · The three fixes

From exercise 4, write three versions of the getter: one that returns a copy, one that returns a tuple,
and one that does not return the list at all but the answer to a specific question.

Explain in a comment which you would pick and why.

### Exercise 6 · The copy that is not enough

Write a class holding a list of dictionaries and a getter that returns `list(...)`. Show that the
outside `append` does not reach it but modifying a dictionary does.

Fix it in two different ways.

### Exercise 7 · Composition

Write `Player` taking a `Speaker` and a `Screen` in its constructor. Then write a second speaker with
the same method and swap it in without touching `Player`.

Count how many lines of `Player` you had to modify.

### Exercise 8 · The inheritance that was not

Write `Player` inheriting from `Speaker` and `Screen` instead of composing them. Show with `isinstance`
what the model now claims, and say the "is a" sentence out loud to see whether it holds.

### Exercise 9 · The lab

You are handed an `Inventory` class with a public dictionary of products and a test file. Close it
without changing a single line of the test file.

The dictionary becomes private and the class exposes `add`, brackets and `len`. Asking for a product
that is not there has to return zero rather than raise `KeyError`.

Hand in the `.py` file with the closed class and the test file exactly as you received it.
"""),

md("""
---
## Three things to take away

**Encapsulating puts together, hiding decides.** The first puts the data and its rule in the same class;
the second chooses what shows. They are two separate decisions and the second is the hard one.

**A getter can undo all the encapsulation.** If it hands back the internal structure, the two underscores
protected a name and nothing else. It is the same sentence we have been dragging since review 3:
assignment does not copy.

**Composition reuses better than inheritance.** Changing a part that is handed in costs one line;
changing a parent costs the whole branch. And before choosing between the two, ask whether a class was
needed.

Week 7 is devoted to inheritance: what a class receives from its parent, how far the tree should grow,
and the single underscore that does have a technical use, opening the door to the children.

### The question that settles most of this week

Before leaving a member public, ask yourself: **am I willing to keep this unchanged for two years?** If
the answer is no, close it today, while nothing depends on it yet.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Contacts:
    def __init__(self):
        self.people = {}

    def save(self, name, phone):
        self.people[name.strip().title()] = phone


a = Contacts()
a.save("ana robles", "555-1111")
a.save("  LUIS FERRER ", "555-2222")
a.save("Paula Ines", "555-3333")
print(a.people)

a.people["ana robles"] = "555-9999"         # through the back door

print(a.people)
expected = len({n.strip().title() for n in
                ["ana robles", "  LUIS FERRER ", "Paula Ines"]})
print(f"{len(a.people)} keys for {expected} real contacts")
```

### Exercise 2

```python
class ClosedContacts:
    def __init__(self):
        self.__people = {}

    def __key(self, name):
        return name.strip().title()

    def save(self, name, phone):
        self.__people[self.__key(name)] = phone

    def __getitem__(self, name):
        return self.__people.get(self.__key(name), "")

    def __setitem__(self, name, phone):
        self.__people[self.__key(name)] = phone

    def __len__(self):
        return len(self.__people)

    def __iter__(self):
        return iter(self.__people)


b = ClosedContacts()
for name, phone in [("ana robles", "555-1111"), ("  LUIS FERRER ", "555-2222"),
                    ("Paula Ines", "555-3333")]:
    b.save(name, phone)

b["ana robles"] = "555-9999"                # the same line, now normalised

print(len(b), "keys")
print(b["ANA ROBLES"])
print(b["nobody"], "<- empty string rather than KeyError")
```

### Exercise 3

```python
def check(cls):
    a = cls()
    a.save("ana robles", "555-1111")
    a.save("Ana Robles", "555-9999")
    a.save("luis ferrer", "555-2222")
    return [
        ("ana normalises", a["ANA ROBLES"] == "555-9999"),
        ("luis is there", a["Luis Ferrer"] == "555-2222"),
        ("the missing one is empty", a["nobody"] == ""),
        ("there are 2 contacts", len(a) == 2),
        ("it walks", sorted(a) == ["Ana Robles", "Luis Ferrer"]),
        ("brackets write", (a.__setitem__("x y", "1"), a["X Y"])[1] == "1"),
    ]


class PairContacts:
    def __init__(self):
        self.__pairs = []

    def __key(self, name):
        return name.strip().title()

    def __find(self, key):
        for pair in self.__pairs:
            if pair[0] == key:
                return pair
        return None

    def save(self, name, phone):
        self[name] = phone

    def __getitem__(self, name):
        pair = self.__find(self.__key(name))
        return pair[1] if pair else ""

    def __setitem__(self, name, phone):
        key = self.__key(name)
        pair = self.__find(key)
        if pair is None:
            self.__pairs.append([key, phone])
        else:
            pair[1] = phone

    def __len__(self):
        return len(self.__pairs)

    def __iter__(self):
        return iter(k for k, _ in self.__pairs)


for cls in [ClosedContacts, PairContacts]:
    results = check(cls)
    print(cls.__name__, sum(1 for _, ok in results if ok), "of", len(results))
```

### Exercise 4

```python
class MailingList:
    def __init__(self):
        self.__addresses = []

    def subscribe(self, address):
        if "@" not in address:
            raise ValueError("that is not an address")
        self.__addresses.append(address)

    def fetch(self):
        return self.__addresses


mail = MailingList()
mail.subscribe("ana@up.edu.mx")

try:
    mail.subscribe("not an address")
except ValueError as e:
    print("Through the door:", e)

mail.fetch().append("not an address")       # through the leak
mail.fetch().append(None)

print(mail.fetch())
print("Valid addresses:",
      sum(1 for a in mail.fetch() if isinstance(a, str) and "@" in a),
      "of", len(mail.fetch()))
```

### Exercise 5

```python
class SafeList:
    def __init__(self):
        self.__addresses = []

    def subscribe(self, address):
        if "@" not in address:
            raise ValueError("that is not an address")
        self.__addresses.append(address)

    def fetch_copy(self):
        return list(self.__addresses)

    def fetch_tuple(self):
        return tuple(self.__addresses)

    def how_many(self):
        return len(self.__addresses)

    def is_subscribed(self, address):
        return address in self.__addresses


mail = SafeList()
mail.subscribe("ana@up.edu.mx")

mail.fetch_copy().append("junk")
print("After touching the copy:", mail.how_many())

try:
    mail.fetch_tuple().append("junk")
except AttributeError as e:
    print("The tuple defends itself:", e)

print("Is Ana subscribed?", mail.is_subscribed("ana@up.edu.mx"))

# I would pick the third. Nobody using this class needs the list: they need to
# know how many there are and whether somebody is on it. Answering those two
# questions closes the leak without copying anything, and it lets me swap the
# list for a set tomorrow.
```

### Exercise 6

```python
import copy


class Cart:
    def __init__(self):
        self.__lines = [{"sku": "X1", "quantity": 1}]

    def fetch_shallow(self):
        return list(self.__lines)

    def fetch_deep(self):
        return copy.deepcopy(self.__lines)

    def fetch_frozen(self):
        return tuple(tuple(sorted(line.items())) for line in self.__lines)

    def total(self):
        return sum(l["quantity"] for l in self.__lines)


c = Cart()
c.fetch_shallow().append({"sku": "X9", "quantity": 9})
print("After the append:", c.total())

c.fetch_shallow()[0]["quantity"] = 999
print("After touching the dictionary:", c.total(), "<- it got through")

d = Cart()
d.fetch_deep()[0]["quantity"] = 999
print("With deepcopy:", d.total())

e = Cart()
print("Frozen:", e.fetch_frozen())
```

### Exercise 7

```python
class Speaker:
    def play(self, track):
        print(f"  speaker: playing {track}")


class BluetoothSpeaker:
    def __init__(self, name):
        self.name = name

    def play(self, track):
        print(f"  {self.name} over bluetooth: playing {track}")


class Screen:
    def show(self, text):
        print(f"  screen: {text}")


class Player:
    def __init__(self, speaker, screen):
        self.speaker = speaker
        self.screen = screen

    def play(self, track):
        self.screen.show(f"Now playing: {track}")
        self.speaker.play(track)


Player(Speaker(), Screen()).play("Bohemian Rhapsody")
Player(BluetoothSpeaker("JBL"), Screen()).play("Bohemian Rhapsody")

# Zero lines of Player. The commitment is a method called play, and any object
# that has one gets in.
```

### Exercise 8

```python
class InheritingPlayer(Speaker, Screen):
    def run(self, track):
        self.show(f"Now playing: {track}")
        self.play(track)


p = InheritingPlayer()
p.run("Bohemian Rhapsody")

print("Is a player a speaker?", isinstance(p, Speaker))
print("Is a player a screen?", isinstance(p, Screen))

# "A player is a speaker" is false and sounds false when you say it. A player has
# a speaker. On top of that, inheritance gives no way to hand it two speakers, and
# changing the speaker means changing the class declaration.
```

### Exercise 9

```python
# tests.py, exactly as you received it. Not to be touched.
def run_tests(Inventory):
    inv = Inventory()
    inv.add("X1", 5)
    inv.add("X2", 3)
    inv.add("X1", 2)

    assert inv["X1"] == 7, "quantities add up"
    assert inv["X2"] == 3
    assert inv["MISSING"] == 0, "a product that is not there is zero"
    assert len(inv) == 2
    inv["X3"] = 10
    assert inv["X3"] == 10
    return "all 5 tests passed"


# inventory.py, the closed class.
class Inventory:
    def __init__(self):
        self.__products = {}

    def add(self, sku, quantity):
        if quantity <= 0:
            raise ValueError("the quantity has to be positive")
        self.__products[sku] = self.__products.get(sku, 0) + quantity

    def __getitem__(self, sku):
        return self.__products.get(sku, 0)

    def __setitem__(self, sku, quantity):
        self.__products[sku] = quantity

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return iter(self.__products)


print(run_tests(Inventory))
```

Three decisions worth defending when you hand this in.

**`__getitem__` returns zero rather than raising.** A product that is not in the inventory has quantity
zero; that is an answer, not an error. `KeyError` would force every place that queries to wrap itself in
a `try`, and that is the rule moving out of the class again.

**There is no `get_products` method.** Nobody outside needs the dictionary. If somebody asks for it
tomorrow, the right question is what they want to do with it, because the answer is almost always a new
method rather than a leak.

**The validation lives in `add`.** Negative quantities are refused at the one place quantities come in
through the front door. Notice that `__setitem__` does not validate, and that is a real hole in this
solution: if the test file allowed it, closing that would be the next line.
"""),

]

write(OUT / "en" / "w06.ipynb", en)
print("wrote", OUT / "en" / "w06.ipynb")
