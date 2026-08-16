"""notebooks/programacion-orientada-a-objetos/en/w08.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w08.en.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code027.py
                  (Animal, Dog, Cat: overriding and the polymorphic loop)
              docs/en/courses/python-course/02 - POO/6th Module/Code020.py
                  (Shape, Circle, Rectangle, with the "Area of Shape: None" ending)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (ABC, abstractmethod and the Stream hierarchy)

All three files run to the end, checked. Code020.py prints
"Area of Shape: None" on its last line and the file documents that as the
expected result; it is quoted here as the silent failure that justifies
abstract classes.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 08
## Topic 3 · Core properties

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

The same message answered in different ways, the contract that forces an answer, and the close of the
first three units.

Last week ended with a loop that walked three data streams without knowing which class each one was.
That was already polymorphism. What is missing is the contract that forces the children to answer, and
the vocabulary to say why that loop is the pillar the whole paradigm rests on.

By the end you will be able to:

1. Override a method and decide deliberately whether you extend the parent or replace it.
2. Recognise polymorphism where it actually shows, which is in the calling loop and not in the class.
3. Write an abstract class with `ABC` and `@abstractmethod`, and say what happens if either is missing.
4. Turn a chain of `if isinstance` into a polymorphic call.
5. Reach the first midterm knowing exactly what is on it.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Ten fail on purpose and carry a comment saying so.

Seven of the ten **raise no exception at all**. One of those seven comes from the course code:
`Code020.py` ends by printing `Area of Shape: None` and the file itself notes that as the expected
result. That line is the best argument for abstract classes anywhere in the repository.
"""),

md("""
---
# Block 1 · Polymorphism and overriding

Objects of different classes answering the same message, each in their own way, with the caller not
having to know which one it has.

We start with the easy half, which is overriding.
"""),

code("""
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Animal sound")


class Dog(Animal):
    def talk(self):
        print("Woof")


class Cat(Animal):
    def talk(self):
        print("Meow")


animals = [Dog("Bobby"), Cat("Kitty"), Dog("Rex"), Cat("Luna")]

for animal in animals:
    animal.talk()

LOOP = "for animal in animals:\\n    animal.talk()"

print()
print("The whole loop:", repr(LOOP))
print("Distinct classes that went through it:", len({type(a) for a in animals}))
print("Times the loop names a class:",
      sum(LOOP.count(n) for n in ["Animal", "Dog", "Cat", "isinstance", "type("]))
"""),

md("""
Four objects, two classes, one line calling them.

Overriding is defining again a method that already existed above. `Dog.talk` covers `Animal.talk` for
dogs and does nothing to cats, because each class has its own dictionary.

**Overriding is not overloading.** Overloading would be two methods with the same name and different
signatures, which week 5 showed Python does not do. Overriding is changing the body in the child, and
that does exist.

## Where polymorphism shows

Not in the classes. In the loop.

Look at the line `animal.talk()`: it does not mention `Dog`, it does not mention `Cat`, and it will
never change. That is the property that matters.
"""),

code("""
class Cow(Animal):
    def talk(self):
        print("Moo")


animals.append(Cow("Lola"))

for animal in animals:           # the same loop, not a letter different
    animal.talk()

print()
print("Classes now going through the same line:", len({type(a) for a in animals}))
print("Is the loop identical to the previous cell's?",
      LOOP == "for animal in animals:\\n    animal.talk()")
"""),

md("""
A new class, and the code that uses it never heard about it.

That is what polymorphism buys you, and it is why it is a pillar rather than a trick: **adding a case
does not force you to touch code that already worked**. In the structured paradigm the same change means
hunting down every `if` that enumerated the types and adding a branch.

You will see that clearly two cells from now, when I write that version.

## Extending rather than replacing
"""),

code("""
class Document:
    def save(self):
        print("  validating fields")


class Invoice(Document):
    def save(self):
        super().save()                # the parent's part first
        print("  stamping the invoice")


class Draft(Document):
    def save(self):
        print("  saving without validating")     # replaces, does not extend


print("Invoice:")
Invoice().save()
print()
print("Draft:")
Draft().save()
"""),

md("""
Both children override `save`. One calls the parent and the other does not, and both decisions are
defensible.

`Invoice` **extends**: it does the parent's work and something more. `Draft` **replaces**: it does
something different and the parent's work would be in the way.

The order is a decision too. Putting `super().save()` last reverses the sequence, and sometimes that is
exactly what you want. What is not worth doing is writing it out of habit without looking at what
happens before and after.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The child forgets to call the parent.
class Audit:
    def __init__(self):
        self.records = []

    def save(self, item):
        self.records.append(item)
        print(f"  saved: {item}")


class NotifyingAudit(Audit):
    def save(self, item):
        print(f"  notice sent for {item}")     # super().save(item) is missing


a = NotifyingAudit()
a.save("invoice 001")
a.save("invoice 002")

print()
print("Rows in the record:", len(a.records), "<- we expected 2")
print("Record:", a.records)
print("The method that ran is written on:",
      next(c.__name__ for c in NotifyingAudit.__mro__ if "save" in vars(c)))
"""),

md("""
Two notices sent and zero rows saved.

Overriding a method without calling the parent **deletes** what the parent did. What was lost here is the
entire record, and the symptom is that the audit is empty, not that something raises.

It is the silent face of overriding, and it is easy to cause by accident: somebody opens the child class,
sees a method with the right name, adds their line, and never looks at the mother.

## And the opposite face: the method the child should have overridden and did not
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The child adds a field and inherits an __eq__ that ignores it.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"


a = Point3D(1, 2, 3)
b = Point3D(1, 2, 99)

print("a:", a, " b:", b)
print("a == b?", a == b, "<- they have different z")
print()
print("The __eq__ that ran is written on:",
      next(c.__name__ for c in Point3D.__mro__ if "__eq__" in vars(c)))
print("Coordinates it compares:", 2, "of", len(vars(a)))
print()
points = [Point3D(1, 2, 3), Point3D(1, 2, 99), Point3D(0, 0, 0)]
print("Distinct points according to ==:", len([p for i, p in enumerate(points)
                                               if p not in points[:i]]))
"""),

md("""
Two points with the same `x`, the same `y` and a different `z`, and `==` says they are equal.

`Point3D` overrode `__repr__` because the need was obvious, and did not override `__eq__` because nothing
was obvious. The inherited method still compares two of the three coordinates, and since it works, nobody
checks it.

**Every time a child adds an attribute, ask which inherited methods stopped being complete.** The usual
suspects are `__eq__`, `__hash__`, `__repr__` and any method that walks the object's state.

The fix here is writing `__eq__` and `__hash__` on the child, with the tuple of all three coordinates,
which is week 5's rule.

## Predict before you run

```python
class Shape:
    def area(self):
        return 0

    def show(self):
        print(self.area())


class Circle(Shape):
    def area(self):
        return 12.56


Circle().show()
```

- **A.** `0`, because `show` lives on `Shape` and uses `Shape`'s `area`.
- **B.** `12.56`, because `self` is a `Circle` and its `area` wins.
- **C.** `AttributeError`, `Circle` has no `show`.
- **D.** `TypeError`, `area` gets one argument too many.
"""),

code("""
class Shape:
    def area(self):
        return 0

    def show(self):
        print(f"  {type(self).__name__}: {self.area()}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2


Circle(2).show()

print()
print("show is written on:",
      next(c.__name__ for c in Circle.__mro__ if "show" in vars(c)))
print("the area that ran is written on:",
      next(c.__name__ for c in Circle.__mro__ if "area" in vars(c)))
print("Type of self during show:", type(Circle(2)).__name__)
"""),

md("""
The answer is **B**.

`show` was inherited from `Shape`, but `self` is still a `Circle`. Python looks `area` up starting from
the object's real class and not from the class where the calling method was written.

It is the same rule that in week 7 made the parent's constructor call the child's method. Seen from here
it is a tool: **the parent can write the algorithm and leave holes for the children to fill**. That
pattern has a name, the template method, and it is half of what makes an abstract class useful.

## The line in `Code020.py` that spoils everything
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. This one comes from the course file.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Shape(), Circle(5), Rectangle(4, 5)]

for shape in shapes:
    shape.show()

print()
print("Area of the generic shape:", Shape().area())
print("Type of that result:", type(Shape().area()).__name__)
print()
total = sum(s.area() for s in shapes)
print(f"Total of the three areas: {total:.2f}")
print("What the generic shape contributed:", Shape().area())
"""),

md("""
`Shape: 0` on the first line, and a total that includes a shape with no shape.

In the original file `Shape.area` is `pass`, so it returns `None` and the file's documented output reads
`Area of Shape: None`. Here it returns zero, which is worse: `None` at least looks odd and breaks the
sum. Zero adds up without complaint and disappears.

The underlying problem is not the return value. **It is that `Shape()` could be constructed at all.** A
shape with no shape is nothing; it exists only because nobody stopped it. Whatever its `area` returns is
going to be a lie.

That is where block 2 starts.
"""),

md("""
---
# Block 2 · Abstract classes and interfaces

A class that exists in order to force others to write a method. It cannot be instantiated, and that is
where all its usefulness lives.
"""),

code("""
from abc import ABC, abstractmethod


class AbstractShape(ABC):
    def show(self):
        print(f"  {type(self).__name__}: {self.area():.2f}")

    @abstractmethod
    def area(self):
        \"\"\"Every child has to write this.\"\"\"


class GoodCircle(AbstractShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2


class GoodRectangle(AbstractShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


for shape in [GoodCircle(5), GoodRectangle(4, 5)]:
    shape.show()

print()
print("Methods AbstractShape forces you to write:",
      sorted(AbstractShape.__abstractmethods__))
"""),

code("""
# FAILS ON PURPOSE. The abstract class cannot be built.
try:
    AbstractShape()
except TypeError as e:
    print("TypeError:", e)

print()


class Triangle(AbstractShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    # we forgot to write area


try:
    Triangle(3, 4)
except TypeError as e:
    print("TypeError:", e)

print()
print("What Triangle is missing:", sorted(Triangle.__abstractmethods__))
"""),

md("""
Both constructions fail, and both fail **at construction time**, which is what you want.

`AbstractShape()` cannot be built because it declares an abstract method and does not implement it.
`Triangle(3, 4)` cannot either, because it inherited the hole and did not fill it.

Compare that with the cell a moment ago. There the generic shape was built, went into the list, added
zero and nobody ever heard about it. Here the error appears on the line that caused it, naming the method
that is missing.

**That is the deal: an abstract class trades a silent, late failure for a loud, early error.**

## Both ingredients have to go together
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The decorator without inheriting from ABC.
class LazyShape:                      # does not inherit from ABC
    @abstractmethod
    def area(self):
        ...


class LazyCircle(LazyShape):
    pass                              # does not write area either


lazy = LazyShape()
lazy_circle = LazyCircle()

print("The abstract one was built:", lazy)
print("The incomplete child too:", lazy_circle)
print()
print("Does it have __abstractmethods__?", hasattr(LazyShape, "__abstractmethods__"))
print("Metaclass of LazyShape:    ", type(LazyShape).__name__)
print("Metaclass of AbstractShape:", type(AbstractShape).__name__)
print()
print("And calling the empty method gives:", lazy_circle.area())
"""),

md("""
Both classes were built without a word of complaint, and `area()` returned `None`.

`@abstractmethod` on its own **prevents nothing**. All it does is put a mark on the function. The thing
that reads that mark and refuses to build the object is `ABCMeta`, the metaclass you get by inheriting
from `ABC`, and the last lines of the cell show it: `type(LazyShape)` is plain `type`, while
`type(AbstractShape)` is `ABCMeta`.

It is error 02 on the slide and it is especially treacherous because the code **looks** right. The
decorator is there, it reads well, and it does absolutely nothing.

## Four ways to declare a contract

| Kind of class | Instantiable | Carries code | In Python |
|---|---|---|---|
| Concrete | Yes | All of it | `class Dog(Animal):` |
| Abstract | No | Some of it | `class Stream(ABC):` |
| Interface | No | None | `@abstractmethod` only |
| Protocol | Not applicable | None | `typing.Protocol` |

The middle two differ by how much code they carry, not by syntax. An interface is an abstract class where
**every** method is abstract: it declares the whole contract and implements nothing.

The fourth is different and worth seeing, because it is what you have been using since week 6 without
naming it.
"""),

code("""
from typing import Protocol


class CanRead(Protocol):
    def read(self) -> str:
        ...


class FileReader:                    # inherits from nothing
    def read(self):
        return "contents of the file"


class NetworkReader:                 # neither does this one
    def read(self):
        return "contents from the network"


def process(source: CanRead) -> None:
    print("  ", source.read())


for source in [FileReader(), NetworkReader()]:
    process(source)

print()
print("Is CanRead in FileReader's chain?", CanRead in FileReader.__mro__)
print("FileReader chain:   ", [c.__name__ for c in FileReader.__mro__])
print("NetworkReader chain:", [c.__name__ for c in NetworkReader.__mro__])
print("All they share:", sorted(
    {n for n in dir(FileReader) if not n.startswith("_")} &
    {n for n in dir(NetworkReader) if not n.startswith("_")}))
"""),

md("""
Neither class inherits from `CanRead`, and both work.

That is **duck typing**: if it walks like a duck and quacks like a duck, it is a duck. In Python all an
object needs in order to be usable is the method, and that is why in week 6 the computer accepted three
drives that shared nothing.

`typing.Protocol` puts a name on that expectation so analysis tools can check it, without forcing anyone
to inherit. It is the closest thing Python has to a Java interface, and it changes nothing at runtime.

**When to use which.** If you want to share code as well as a contract, abstract class. If you only want
to declare which methods are needed and the classes already exist or come from another library, protocol.

Two things about protocols that surprise people.
"""),

code("""
# FAILS ON PURPOSE. A protocol cannot be used with isinstance just like that.
try:
    print(isinstance(FileReader(), CanRead))
except TypeError as e:
    print("TypeError:", e)

print()

from typing import runtime_checkable


@runtime_checkable
class CheckableCanRead(Protocol):
    def read(self) -> str:
        ...


print("With @runtime_checkable:", isinstance(FileReader(), CheckableCanRead))
print("And with something that cannot read:", isinstance(42, CheckableCanRead))
"""),

md("""
A protocol, as written, is a declaration for analysis tools and does not exist at runtime. To use it with
`isinstance` you have to mark it `@runtime_checkable`, and even then it only checks that the method
exists, not that it does what it promises.

That last part is duck typing's underlying weakness, and it shows better with an example.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Two classes, one method name, two meanings.
class Circle3:
    def draw(self):
        return "a small circle on the canvas"


class Cowboy:
    def draw(self):
        return "the cowboy draws his gun"        # draw, as in pulling a weapon


canvas = [Circle3(), Circle3(), Cowboy()]

for figure in canvas:
    print(" ", figure.draw())

print()
print("They all have the method:", all(hasattr(f, "draw") for f in canvas))
print("They all pass the protocol:", all(callable(getattr(f, "draw")) for f in canvas))
print("They all mean the same thing: no")
"""),

md("""
The cowboy passed every check Python can make and still had no business on a canvas.

A method name is not a contract: it is half a word. `isinstance` with a protocol checks the signature,
`hasattr` checks the name, and neither of them can check the meaning.

When that matters, the abstract class wins: inheriting from `AbstractShape` is an explicit declaration of
intent, and the cowboy would never have written it. Duck typing is more flexible and cheaper; the
abstract class is stricter and clearer. Both get used, and knowing which one you asked for is the part
you learn.

## The `if isinstance` that does polymorphism by hand
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The chain of ifs that forgets the new class.
def area_of(shape):
    if isinstance(shape, GoodCircle):
        return 3.1416 * shape.radius ** 2
    elif isinstance(shape, GoodRectangle):
        return shape.width * shape.height
    return 0                          # the case that swallows everything


class GoodTriangle(AbstractShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


figures = [GoodCircle(5), GoodRectangle(4, 5), GoodTriangle(3, 4)]

print("With the chain of ifs:")
for f in figures:
    print(f"  {type(f).__name__:<16}{area_of(f):.2f}")

print()
print("With the polymorphic call:")
for f in figures:
    print(f"  {type(f).__name__:<16}{f.area():.2f}")

print()
agree = sum(1 for f in figures if abs(area_of(f) - f.area()) < 1e-9)
print(f"{agree} of {len(figures)} agree with the class's own method")
print("Difference on the triangle:", f"{figures[2].area() - area_of(figures[2]):.2f}")
"""),

md("""
The triangle measures six and the chain of `if` says it measures zero.

The class was written correctly, it inherits from the abstract one, and its `area` works. What failed is a
function that enumerated types and that nobody updated, because nothing forces it to be complete.

The `return 0` at the end is why it does not raise. An `else: raise` would have turned this into a loud
error, and that is the minimum fix when the chain genuinely cannot be avoided. The real fix is the line
below: `f.area()`, which enumerates nothing.

**If your loop has an `if` by type, you are not using polymorphism yet.**

## When the signature changes
"""),

code("""
# FAILS ON PURPOSE. The child overrides asking for different arguments.
class Exporter:
    def export(self, rows):
        return f"exporting {len(rows)} rows"


class CsvExporter(Exporter):
    def export(self, rows):
        return f"csv with {len(rows)} rows"


class PdfExporter(Exporter):
    def export(self, rows, template):          # one argument too many
        return f"pdf with {len(rows)} rows, template {template}"


ROWS = [1, 2, 3]
for exp in [Exporter(), CsvExporter(), PdfExporter()]:
    try:
        print(" ", exp.export(ROWS))
    except TypeError as e:
        print("  TypeError:", e)
"""),

md("""
The first two answered and the third blew up, in the same loop, with nothing odd about the list.

Overriding changes the body. If you also change the signature, the method is no longer the same method:
it is a different one with the same name, and the polymorphic loop cannot call it.

It is error 01 on the slide, and it is a cousin of what week 7 called substitution: **where the mother
worked, the child has to keep working**. A different signature breaks that in the most direct way there
is.

The way out when the child genuinely needs more data: take it in the constructor.
`PdfExporter(template="invoice")` stores the template and `export(rows)` reads it off `self`. The
signature lines up again and the loop works again.

## Four ways to break the contract

| | The error | How it looks |
|---|---|---|
| 01 | Overriding with a different signature | The polymorphic loop blows up on the third object |
| 02 | `@abstractmethod` without inheriting from `ABC` | The decorator prevents nothing and the class instantiates |
| 03 | Asking the type before calling | Polymorphism by hand, to be edited on every new class |
| 04 | An abstract class with a single child | An extra layer that abstracts nothing |
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. An abstraction with a single child.
class AbstractRepository(ABC):
    @abstractmethod
    def save(self, item): ...

    @abstractmethod
    def read(self, key): ...

    @abstractmethod
    def delete(self, key): ...


class InMemoryRepository(AbstractRepository):
    def __init__(self):
        self.items = {}

    def save(self, item):
        self.items[item["id"]] = item

    def read(self, key):
        return self.items.get(key)

    def delete(self, key):
        self.items.pop(key, None)


repo = InMemoryRepository()
repo.save({"id": "X1", "name": "coffee"})
print("Read:", repo.read("X1"))

print()
children = AbstractRepository.__subclasses__()
print("Children of the abstract class:", [c.__name__ for c in children], "->", len(children))
print("Methods declared on the abstract class:", len(AbstractRepository.__abstractmethods__))
print("Classes that declare save:",
      [c.__name__ for c in InMemoryRepository.__mro__ if "save" in vars(c)])
"""),

md("""
It works perfectly, and it is good for nothing.

An abstract class with a single child does not abstract: it duplicates. Every method is declared twice,
every change has to be made in two places, and understanding one call means opening two classes instead
of one. The contract protects nobody because there is nobody on the other side.

Abstraction earns its place when there are two **real** implementations, not when you imagine there will
someday be a second. If one really does arrive, extracting the abstract class that day takes ten minutes
and you already know which methods it has to declare, because both cases are in front of you.

**The rule: write the second class first, then extract the abstract one.**
"""),

md("""
---
# Block 3 · The first midterm

The exam closes units 1, 2 and 3. It is sat this same week, on a machine, with the course repository open
and no outside help.

| Unit | What is on it |
|---|---|
| U1 · Introduction | Paradigms, the concept of an object, the benefits of the approach and where it gets in the way |
| U2 · Basic elements | Classes, objects, attributes, methods, properties, access, constructors, class members |
| U3 · Core properties | Encapsulation, hiding, reuse, inheritance, hierarchy, polymorphism, abstract classes |
| Not on it | Files, graphical interfaces and databases, which belong to the second midterm |

## How to prepare

**The exam asks you to write classes, not describe them.** If you cannot type from memory a class with a
constructor, a private attribute, a property and a child that overrides a method, you do not know it yet.

**What to practise.** The labs from weeks 4, 6 and 7, solved again without opening the solution.

**What to review.** Each week's diagnosis tables. The four errors in each one are the exam's.

**What not to do.** Memorising definitions. No question asks for the definition of encapsulation.

The cell below is a single-pass revision: it packs almost everything on the exam into one class.
"""),

code("""
class Loan(ABC):
    \"\"\"All three units revised in a single class.\"\"\"

    BASE_DAYS = 14                          # class attribute, week 4

    def __init__(self, title: str, day: int) -> None:
        self.title = title                  # public, week 3
        self.__day = day                    # private, week 4
        self._history = []                  # protected, week 7

    @property                               # property, week 3
    def day(self) -> int:
        return self.__day

    @property
    def history(self):
        return tuple(self._history)         # defensive copy, week 6

    @abstractmethod                         # contract, week 8
    def max_days(self) -> int: ...

    def overdue(self, today: int) -> bool:  # template method
        self._history.append(today)
        return today - self.__day > self.max_days()

    def __repr__(self) -> str:              # magic method, week 5
        return f"{type(self).__name__}({self.title!r})"


class BookLoan(Loan):
    def max_days(self):
        return Loan.BASE_DAYS


class MagazineLoan(Loan):
    def max_days(self):
        return 7


class StaffLoan(BookLoan):                  # two-level inheritance, week 7
    def max_days(self):
        return super().max_days() * 3


loans = [BookLoan("The Aleph", 1),
         MagazineLoan("Nature", 1),
         StaffLoan("Calculus II", 1)]

for loan in loans:                          # polymorphism, week 8
    print(f"  {loan!r:<28}limit {loan.max_days():>2}  overdue on 20: {loan.overdue(20)}")

print()
print("History of the first one:", loans[0].history)
try:
    loans[0].history.append(99)
except AttributeError as e:
    print("And it cannot be touched from outside:", e)
"""),

md("""
Nine concepts from the term in forty lines, and every one of them is in the exam's rubric.

Walk it again pointing at each: the class attribute, the private with two underscores, the protected with
one, the two properties, the defensive copy, the abstract method, the template method that calls the
abstract one, the `__repr__`, the two levels of inheritance, and the loop that asks no types.

If you can write that class from scratch explaining every decision, the midterm is passed.
"""),

md("""
---
## Four errors from this session

**Overriding without calling the parent.** What the parent did is lost, and the symptom is an empty list,
not an exception.

**`@abstractmethod` without `ABC`.** The decorator only puts a mark on the function. What refuses to build
the object is the metaclass that arrives with `ABC`.

**The `if isinstance` chain with a default case.** The new class falls into the `return 0` and hands back
a believable number.

**Overriding with a different signature.** The polymorphic loop blows up on the object that changed it,
and the error points at the call rather than at the class.
"""),

md("""
---
# Exercises

This week's lab is a midterm rehearsal in pairs. The exercises cover what is on it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · Three voices

Write `Instrument` with a `play` method, and three children that override it. Walk them in a loop, then
add a fourth class without touching the loop.

Count how many lines of the loop you had to edit.

### Exercise 2 · Extend against replace

Write a parent with a validating method, and two children: one that calls `super()` and one that does not.
Show with a list of results what was lost in the second.

### Exercise 3 · The template method

Write a class with a method that calls another method on the same object, and a child that overrides only
the second. Check that the first one, inherited unchanged, uses the child's version.

Print which class each one is written on using `__mro__`.

### Exercise 4 · The abstract class

Turn exercise 3's class into an abstract one with `ABC` and `@abstractmethod`. Try to build it, catch the
`TypeError`, then write an incomplete child and catch the other one.

Print `__abstractmethods__` for both.

### Exercise 5 · The decorator on its own

Write the same class with `@abstractmethod` but **without** inheriting from `ABC`. Build it, call the
abstract method, and print `type()` of both classes to show the difference.

### Exercise 6 · The chain of ifs

Write a function that computes something with `if isinstance` for two classes and a default case. Add a
third class and show the difference between what the function returns and what the method returns.

Then rewrite it in one line.

### Exercise 7 · The signature that does not fit

Write three classes with the same method, and make the third ask for one argument more. Walk them in a
loop and catch the `TypeError`.

Fix it by passing that value through the constructor and run the same loop again.

### Exercise 8 · Duck typing

Write two classes with no common parent but the same method, and a function that uses both. Check with
`__mro__` that they share nothing above `object`.

Declare the protocol with `typing.Protocol` and explain in a comment what changed at runtime.

### Exercise 9 · The lab

In pairs, write three code questions in the style of the ones we have seen, one per unit, and none that
can be answered with a definition.

Swap them with another pair and mark the answers with a two-line rubric.

The criterion is that every question has one correct answer and one trap that sounds reasonable.
"""),

md("""
---
## Three things to take away

**Overriding changes the body, not the name.** The child replaces the parent's method and the caller never
hears about the change. Add a `super()` call and you extend rather than replace, and that decision is
taken deliberately.

**An abstract class declares the contract.** It says which methods will exist without writing the how, and
forces every child to complete it. It turns a silent, late failure into a loud error at construction time.

**Polymorphism deletes the `if` on types.** Adding a new class does not touch a line of the code that is
about to use it, and that property is why the paradigm exists.

That closes topic 3 and the first midterm. Week 9 opens the application unit with functions that test
themselves, code split into pieces, and functions that call themselves.

### What you take from the three units

An object puts data and behaviour together. A class describes how one is made. What you leave public is a
promise. What is declared on the class is shared. Assignment does not copy. And a loop that does not ask
which class each object is, is a loop you will not have to open again.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Instrument:
    def play(self):
        print("generic sound")


class Guitar(Instrument):
    def play(self):
        print("twang")


class Drums(Instrument):
    def play(self):
        print("boom")


class Violin(Instrument):
    def play(self):
        print("eeee")


band = [Guitar(), Drums(), Violin()]
for i in band:
    i.play()


class Trumpet(Instrument):
    def play(self):
        print("toot")


band.append(Trumpet())
for i in band:                # the same loop, unchanged
    i.play()

# Zero lines of the loop. The only thing that changed is the list, which is data
# and not code.
```

### Exercise 2

```python
class Form:
    def __init__(self):
        self.errors = []

    def validate(self, value):
        if not value:
            self.errors.append("empty field")
        return len(self.errors) == 0


class NotifyingForm(Form):
    def validate(self, value):
        print("  checking", repr(value))
        return super().validate(value)


class SilentForm(Form):
    def validate(self, value):
        print("  checking", repr(value))
        return True                    # it swallowed the validation


a = NotifyingForm()
b = SilentForm()

for f in [a, b]:
    print(type(f).__name__, "->", f.validate(""))
    print("  errors recorded:", f.errors)
```

### Exercise 3

```python
class Report:
    def render(self):
        print(f"  {self.header()} | {self.body()}")

    def header(self):
        return "REPORT"

    def body(self):
        return "no data"


class SalesReport(Report):
    def body(self):
        return "sales: 120"


SalesReport().render()

for name in ["render", "header", "body"]:
    owner = next(c.__name__ for c in SalesReport.__mro__ if name in vars(c))
    print(f"  {name:<8}written on {owner}")
```

### Exercise 4

```python
from abc import ABC, abstractmethod


class Report(ABC):
    def render(self):
        print(f"  {self.header()} | {self.body()}")

    def header(self):
        return "REPORT"

    @abstractmethod
    def body(self): ...


try:
    Report()
except TypeError as e:
    print("TypeError:", e)


class EmptyReport(Report):
    pass


try:
    EmptyReport()
except TypeError as e:
    print("TypeError:", e)

print(sorted(Report.__abstractmethods__))
print(sorted(EmptyReport.__abstractmethods__))
```

### Exercise 5

```python
class LazyReport:
    @abstractmethod
    def body(self): ...


r = LazyReport()
print("It was built:", r)
print("The abstract method returns:", r.body())
print("type(LazyReport):", type(LazyReport).__name__)
print("type(Report):    ", type(Report).__name__)

# The decorator only puts a mark on the function. What reads it is ABCMeta, which
# arrives by inheriting from ABC. Without it, nobody reads the mark.
```

### Exercise 6

```python
class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.1416 * self.r ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


def area_of(f):
    if isinstance(f, Circle):
        return 3.1416 * f.r ** 2
    elif isinstance(f, Square):
        return f.side ** 2
    return 0


for f in [Circle(1), Square(2), Triangle(3, 4)]:
    print(f"{type(f).__name__:<10}ifs: {area_of(f):>7.2f}   method: {f.area():>7.2f}")

# The one-line version:
print([round(f.area(), 2) for f in [Circle(1), Square(2), Triangle(3, 4)]])
```

### Exercise 7

```python
class Notifier:
    def send(self, message):
        return f"generic: {message}"


class ByEmail(Notifier):
    def send(self, message):
        return f"email: {message}"


class BrokenBySms(Notifier):
    def send(self, message, number):
        return f"sms to {number}: {message}"


for n in [Notifier(), ByEmail(), BrokenBySms()]:
    try:
        print(" ", n.send("hello"))
    except TypeError as e:
        print("  TypeError:", e)


class BySms(Notifier):
    def __init__(self, number):
        self.number = number

    def send(self, message):
        return f"sms to {self.number}: {message}"


for n in [Notifier(), ByEmail(), BySms("555-1111")]:
    print(" ", n.send("hello"))
```

### Exercise 8

```python
from typing import Protocol


class Printable(Protocol):
    def render(self) -> None: ...


class Receipt:
    def render(self):
        print("  purchase receipt")


class Label:
    def render(self):
        print("  shipping label")


def send_to_printer(thing: Printable) -> None:
    thing.render()


for thing in [Receipt(), Label()]:
    send_to_printer(thing)

print([c.__name__ for c in Receipt.__mro__])
print([c.__name__ for c in Label.__mro__])

# At runtime nothing changed: Python never checked the protocol. What changed is
# that an analysis tool can now warn me before I run the program if I pass in
# something without render, and that the signature documents what the function
# expects.
```

### Exercise 9

Three sample questions, one per unit, with the trap that makes each one useful.

**U1.** This program solves the same problem with functions and with a class. In which of the two does
adding a third customer field mean touching more lines, and why? The trap: the class version is longer, so
it looks like the worse one.

**U2.** This class has a `@property` with no setter and an attribute with two underscores. Write two lines
that try to break it from outside and say which one raises and which does not. The trap: both look
equivalent.

**U3.** This hierarchy has three classes and a loop that walks them. Add a fourth class and say how many
lines of the loop change. The trap: the loop has an `if isinstance` hidden halfway down.

The two-line rubric: **the correct answer is worth half and explaining why the trap was a trap is worth
the other half.**
"""),

]

write(OUT / "en" / "w08.ipynb", en)
print("wrote", OUT / "en" / "w08.ipynb")
