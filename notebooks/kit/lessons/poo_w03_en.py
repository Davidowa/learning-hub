"""notebooks/programacion-orientada-a-objetos/en/w03.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w03.en.yaml
Source code:  punto.py, dos_puntos.py, persona.py, rectangulo.py and
              compartido.py were written for the deck. The repository's class
              code starts in 02 - POO/6th Module, which feeds weeks 4 to 8.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 03
## Topic 2 · Basic elements

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Classes, objects and the state they hold. The minimum vocabulary of the paradigm, with code that runs
today.

Last week ended with a clue: `vars(ana)` returned a dictionary. This notebook explains where that
dictionary comes from, who fills it, and why two objects of the same class can end up pointing at the
same one.

By the end you will be able to:

1. Tell a class from an object, and say which of the two takes up memory.
2. Write a constructor and explain when it runs without anyone calling it.
3. Declare methods with `self`, and say exactly what happens if you forget it.
4. Use `@property` to expose a calculation with the syntax of an attribute.
5. Recognise the shared class attribute before it costs you an afternoon.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Eleven fail on purpose and carry a comment saying so.

Seven of the eleven **raise no exception at all**. Two of those seven are the ones this term charges
most for: the attribute with the misspelled name, and the list declared in the class body.
"""),

md("""
---
# Block 1 · The class and the object

Two words that stay confused all term unless they get separated today.

A **class** is a template describing what an object remembers and what it knows how to do. It gets
written once.

An **object** is a thing built from that template, with its own copy of the data. You make as many as
you need.

The cookie cutter against the cookies. The blueprint against the house.
"""),

code("""
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def draw(self) -> None:
        print(f"Point at ({self.x}, {self.y})")


p = Point(1, 2)
p.draw()
"""),

md("""
Eight lines, and nearly the whole vocabulary of the topic is in them.

`class Point:` opens the template. The convention is a singular name with an initial capital, because
it describes one thing and not a pile of them.

`def __init__(self, x, y)` is the **constructor**. Nobody calls it by hand: it runs on its own, at the
exact moment you write `Point(1, 2)`. The two underscores on each side are how Python marks the
methods the language calls for you, and in week 8 you will write several more.

`self.x = x` creates an attribute on **that** object. The left-hand one is the attribute and the
right-hand one is the parameter; they share a name out of habit, not obligation.

`def draw(self)` is a **method**. It takes `self` as its first parameter, which is the object it was
called on.

## Two objects, two states
"""),

code("""
a = Point(1, 2)
b = Point(9, 9)

a.x = 100

a.draw()
b.draw()

print()
print("same object?", a is b)
print("equal?      ", a == b)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
"""),

md("""
Changing `a.x` did not touch `b`. Each object carries its own attribute dictionary, and that
dictionary is literally the object's state.

`a == b` gives `False` even though both were `Point`s. By default, comparing two objects with `==` is
the same as comparing them with `is`: it asks whether they are the same object, not whether they are
worth the same. Week 8 teaches how to change that by writing `__eq__`.

## Methods live once
"""),

code("""
print("The class dictionary has the method:")
print("  ", [n for n in vars(Point) if not n.startswith("__")])
print()
print("Each object's does not:")
print("   vars(a):", list(vars(a)))
print("   vars(b):", list(vars(b)))
print()
print("Do a and b share the same draw function?",
      a.draw.__func__ is b.draw.__func__)
print("And is it the one on the class?         ",
      a.draw.__func__ is Point.draw)
"""),

md("""
The `draw` function exists exactly once, stored on the class. Neither `a` nor `b` has it; both borrow
it when somebody writes the dot.

That is what makes objects cheap to create. Ten thousand points are ten thousand dictionaries with two
numbers each, not ten thousand copies of the method.

## What `self` is, without the mystery
"""),

code("""
Point.draw(a)             # calling through the class, passing the object by hand
a.draw()                  # the normal form, exactly the same thing

print()
print("a.draw is of type    ", type(a.draw).__name__)
print("Point.draw is of type", type(Point.draw).__name__)
"""),

md("""
Both lines do the same thing. `a.draw()` is syntactic sugar for `Point.draw(a)`.

That is all `self` is: **the object you called the method on, handed over as the first argument by the
language**. It is not a keyword, it is not magic, and you could in fact name it `me` and it would
work. Do not: `self` is the universal convention and changing it only confuses whoever reads your
code.

What matters is that you already knew it. In review 4 you wrote `items.append(3)`, which is
`list.append(items, 3)` wearing another face. List methods always received their object as the first
parameter.
"""),

code("""
# FAILS ON PURPOSE. A method without self in its definition.
class BrokenPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw():              # no self
        print("I never get printed")


broken = BrokenPoint(1, 2)
try:
    broken.draw()
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
"takes 0 positional arguments but 1 was given". The message confuses everybody the first time, because
the call was `broken.draw()` and there is no argument in sight.

Python put the argument there. `broken.draw()` becomes `BrokenPoint.draw(broken)`, and that function
accepts none. When you read that message, the first thing to check is whether `self` is missing.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The method without brackets.
print(p.draw)
print()
print("Did the point get printed? No. The method reference did.")
print("Type:", type(p.draw).__name__)
"""),

md("""
It is the same mistake as review 3's with plain functions, in another costume. Without brackets, the
name is only the name.

It hurts more here because the `@property` coming up in a moment **is** read without brackets, so
`r.area` and `r.compute()` live in the same class and you have to know which is which.
"""),

md("""
---
# Block 2 · Attributes, methods and properties

What the object remembers, what it knows how to do, and what pretends to be data without being it.

## Attributes can be created from anywhere
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A misspelled attribute gets created in silence.
point = Point(1, 2)
point.draw()

point.coordinate_x = 500     # we meant point.x

point.draw()
print()
print("Object state:", vars(point))
print("Attributes it has:", len(vars(point)))
"""),

md("""
The point is still at (1, 2) and now carries one extra attribute that nobody will ever read.

Python lets you add attributes to an object at any time, and it does not check against the class.
Writing `point.coordinate_x` instead of `point.x` is not a naming error, it is a new attribute, and
the only symptom is that the value you assigned shows up nowhere.

It is the same mechanism as review 4's dictionary: `d["misspelled_key"] = 5` does not fail either, it
creates a key. And that is no coincidence, because **the object's state is a dictionary**, the one
`vars` prints.

## The attribute you do not touch from outside
"""),

code("""
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name           # two leading underscores
        self.age = age               # age changes with the years, kept public

    def speak(self) -> None:
        print(f"Hello, my name is {self.__name}")


ana = Person("Ana", 20)
ana.speak()
ana.age = 21
print("Age:", ana.age)

print()
print("What the object actually stores:", vars(ana))
"""),

md("""
The attribute is not called `__name` in the dictionary. It is called `_Person__name`.

That is **name mangling**: when Python sees an attribute starting with two underscores inside a class,
it glues the class name in front. Inside the methods the translation is automatic, which is why
`self.__name` works; from outside you have to write the long name.
"""),

code("""
# FAILS ON PURPOSE. From outside, that name does not exist.
try:
    print(ana.__name)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("But with the real name it does:", ana._Person__name)
"""),

md("""
It is not a lock. It is the kind of latch that opens if you push: the data is still there and the full
name reads it without any trouble.

What it does prevent is touching it by accident, which is its real purpose. And it prevents something
else that shows up in week 7: a subclass defining an attribute with the same name and overwriting the
parent's without noticing.

## The consequence nobody expects
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Assigning the short name from outside.
ana.__name = "impostor"

ana.speak()
print()
print("Object state:", vars(ana))
print("Attributes:", len(vars(ana)))
"""),

md("""
The object now has two attributes that look like the same one, `_Person__name` holding `"Ana"` and
`__name` holding `"impostor"`, and `speak` still says Ana.

Whoever wrote that line believed they were changing the name. They changed nothing visible, got no
error, and left rubbish in the object. It is the typo from a few cells ago, made worse because here it
looks like you know what you are doing.

## Properties: a calculation that reads like data
"""),

code("""
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


r = Rectangle(3, 4)
print("Area:     ", r.area)          # no brackets
print("Perimeter:", r.perimeter)

r.width = 10
print()
print("After changing the width to 10:")
print("Area:     ", r.area)
print("Perimeter:", r.perimeter)
print()
print("What the object stores:", vars(r))
"""),

md("""
The area went from 12 to 40 on its own. And look at the last line: **the area is not in the object's
dictionary**. It is not stored, it is computed every time somebody reads it.

`@property` turns a method into something read without brackets. That is not cosmetic, it is a
guarantee: a value computed at the moment of reading cannot go stale.

The version without the property shows why that matters.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The area stored as an ordinary attribute.
class BrokenRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height    # computed once, at construction


box = BrokenRectangle(3, 4)
print("Area at construction:", box.area)

box.width = 10

print("Width:", box.width, "· height:", box.height)
print("Area it reports:  ", box.area)
print("Area for real:    ", box.width * box.height)
print()
print("State:", vars(box))
"""),

md("""
A 10 by 4 rectangle reporting an area of 12.

The number got computed once, when the width was 3, and there it stayed. Nobody looked at it again. It
is the parallel-lists problem from week 2, shrunk down to fit inside a single object: two pieces of
data that should stay in sync and nothing keeping them there.

With `@property` that impossible state cannot be reached, because the area does not exist until you
ask for it.
"""),

code("""
# FAILS ON PURPOSE. A read-only property does not accept assignment.
try:
    r.area = 99
except AttributeError as e:
    print("AttributeError:", e)

print()
print("The area is still:", r.area)
"""),

md("""
`AttributeError: property 'area' of 'Rectangle' object has no setter`.

That is a guarantee too, not a nuisance. The area is a consequence of the width and the height, so
setting it directly would make no sense: which of the two sides would change?

When you do want to allow the assignment, `@area.setter` exists and week 4 covers it alongside access
modifiers.

**When not to use a property.** If the calculation is expensive, hide it behind an ordinary method.
The brackets are the signal that something is about to happen, and `r.area` suggests that reading is
free.

## The five words of the topic

| Term | What it is | Syntax |
|---|---|---|
| Class | The template | `class Point:` |
| Object | An instance with its own state | `p = Point(1, 2)` |
| Attribute | Data the object remembers | `self.x = x` |
| Method | Something the object can do | `def draw(self):` |
| Property | A calculation read like data | `@property` |
"""),

md("""
---
# Block 3 · The class attribute

## Predict before you run

What does the last line print?

```python
class Cart:
    products = []

    def __init__(self, owner):
        self.owner = owner

    def add(self, sku):
        self.products.append(sku)


a = Cart("Ana")
b = Cart("Luis")
a.add("X1")
print(len(b.products))
```

- **A.** 0, because `b` never added anything.
- **B.** 1, because the list lives on the class.
- **C.** An error, `products` is not defined in `__init__`.
- **D.** 2, because each cart duplicates the list.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. This is the expensive one of the week.
class Cart:
    products = []

    def __init__(self, owner):
        self.owner = owner

    def add(self, sku):
        self.products.append(sku)


a = Cart("Ana")
b = Cart("Luis")
a.add("X1")

print("len(b.products):", len(b.products))
print("Luis's cart:", b.products)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
print("Cart.products:", Cart.products)
print()
print("is it the same list?",
      a.products is b.products is Cart.products)
"""),

md("""
The answer is **B**.

Both instance dictionaries hold only the owner. `products` is in neither of them, because it was never
assigned on `self`: it was declared in the class body, and there it exists exactly once for every
cart.

| Step | Statement | a.owner | b.owner | Cart.products |
|---|---|---|---|---|
| 1 | `a = Cart('Ana')` | Ana | does not exist | `[]` |
| 2 | `b = Cart('Luis')` | Ana | Luis | `[]` |
| 3 | `a.add('X1')` | Ana | Luis | `['X1']` |
| 4 | `len(b.products)` | Ana | Luis | `['X1']` |

When you write `b.products`, Python looks for `products` in `b`'s dictionary, does not find it, and
goes up to the class. It finds everybody's list and hands it over. That is why both carts see the same
thing.

**You have seen this mechanism twice already.** In review 3, with the list used as a function's
default value, created once and accumulating across calls. In review 4, with the assignment that does
not copy and leaves two names on one object. It is the same one, with a class on top.

## The fix that looks like a fix
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. "Fixing" it by assigning on one instance.
b.products = []              # now b really does have its own

print("vars(b):", vars(b))
print()
b.add("Y1")
a.add("X2")

print("Ana's cart: ", a.products)
print("Luis's cart:", b.products)
print("On the class:", Cart.products)
print()
c = Cart("Carla")
print("Carla's cart:", c.products, "<- starts out with Ana's shopping")
"""),

md("""
Luis's cart came out fine and Ana's is still the class's. The third customer through the door starts
out with whatever Ana bought.

Assigning on the instance does not delete the class attribute: it lays one on top for that object
only. The problem is patched for whoever reported it and stays alive for everybody else, which is the
worst way to fix a bug.

## The real fix
"""),

code("""
class GoodCart:
    def __init__(self, owner):
        self.owner = owner
        self.products = []           # a new list per object

    def add(self, sku):
        self.products.append(sku)


a = GoodCart("Ana")
b = GoodCart("Luis")
a.add("X1")

print("Ana: ", a.products)
print("Luis:", b.products)
print("the same list?", a.products is b.products)
print()
print("vars(a):", vars(a))
print("vars(b):", vars(b))
"""),

md("""
The fix fits on one line, and so does the rule: **anything that has to be different in each object
gets assigned inside `__init__`, on `self`.**

`self.products = []` runs once for every object created, so there are as many lists as carts.

## When a class attribute is the right call
"""),

code("""
class Loan:
    MAX_DAYS = 14                    # a constant, the same for everybody
    total_created = 0                # a counter for the whole class

    def __init__(self, title, day_borrowed):
        self.title = title
        self.day_borrowed = day_borrowed
        Loan.total_created += 1      # on the class, on purpose

    def overdue(self, today):
        return today - self.day_borrowed > Loan.MAX_DAYS


one = Loan("Data structures", 1)
two = Loan("Calculus II", 5)

print("Maximum days:", Loan.MAX_DAYS)
print("Loans created:", Loan.total_created)
print()
for loan in [one, two]:
    print(f"{loan.title:<20}overdue on day 20: {loan.overdue(20)}")
"""),

md("""
Here sharing is what you want. `MAX_DAYS` is a rule of the library, not of each loan, and if it
changes to twenty-one tomorrow it changes in one place. `total_created` counts objects, so by
definition it cannot live inside one of them.

The difference from the cart is not in the syntax, it is in the question: **is this data the object's
or the concept's?** The products belong to the cart. The maximum term belongs to the library.

Watch the detail in `Loan.total_created += 1`. Writing it as `self.total_created += 1` would work
halfway and in the worst possible way: it would read the class's, add one, and store the result as an
instance attribute. Every object would end up with its own counter sitting at 1.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. self.counter += 1 on a class attribute.
class Counter:
    total = 0

    def __init__(self):
        self.total += 1          # looks like it increments the class's


for _ in range(5):
    Counter()

print("Counter.total:", Counter.total, "<- stuck at zero")
print("Each object took its own:", vars(Counter()))
"""),

md("""
Five objects created and the class counter is still at zero.

`self.total += 1` expands to `self.total = self.total + 1`. The read on the right finds the class's
zero; the assignment on the left **always** writes to the instance. It is exactly review 3's scope
rule, the one about assigning inside a function creating a local, moved from a function's scope to an
object's.

With the cart's list that did not happen because `append` does not assign: it modifies the object
that was already there, and that object was the class's. **Mutables get shared by accident and
immutables get copied by accident**, and the two halves of that sentence hurt at different moments.
"""),

md("""
---
## Four errors from this session

**Forgetting `self` in the definition.** `TypeError: takes 0 positional arguments but 1 was given`.
The object gets passed on its own, so the signature has to accept it.

**Declaring the attribute outside `__init__`.** It sticks to the class and every object shares the
same list or the same counter. The fix is one line inside the constructor.

**Calling the method without brackets.** `p.draw` prints the reference. `p.draw()` runs it. With a
`@property` in the same class, you have to be clear on which is which.

**A constructor that does too much.** If `__init__` opens files or hits the network, the object fails
before it exists and there is nothing to inspect when it does.
"""),

code("""
# FAILS ON PURPOSE. A constructor that does real work.
class BrokenReport:
    def __init__(self, path):
        self.path = path
        with open(path) as f:        # the object depends on this going well
            self.content = f.read()


try:
    report = BrokenReport("missing.csv")
except FileNotFoundError as e:
    print("FileNotFoundError:", e.filename)

print()
print("Does the report variable exist?", "report" in dir())


class Report:
    def __init__(self, path):
        self.path = path
        self.content = None          # the object is born valid and empty

    def load(self):
        with open(self.path) as f:
            self.content = f.read()
        return self


report = Report("missing.csv")
print("The object does exist:", vars(report))
try:
    report.load()
except FileNotFoundError:
    print("The load failed, but the object can be inspected:", report.path)
"""),

md("""
In the first version the exception happened halfway through construction, so no object was left to
look at: you cannot even tell which path was attempted, because the variable never got assigned.

In the second, the constructor only stores data and the work goes in a separate method. When the load
fails, the object is there, with its path, ready to retry or to appear in a useful error message.

**A constructor takes what is indispensable and leaves the object ready to use.** Nothing more.
"""),

md("""
---
# Exercises

This week's lab is modelling a library. The exercises build toward it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The smallest class

Write a `Book` class with a title and an author, and a `describe` method that prints them. Create
three books and describe them.

Then print `vars` of all three and say what they have in common and what they do not.

### Exercise 2 · The missing `self`

Write a method without `self` on purpose, call it and catch the `TypeError`. Then call the same method
through the class, passing the object by hand, and explain in a comment why that form works.

### Exercise 3 · The ghost attribute

Create an object and assign it an attribute with a misspelled name. Show with `vars` that the object
ended up with one extra piece of data and that the one you meant to change is unchanged.

Write in a comment how you would spot this in a thousand-line program.

### Exercise 4 · The property that does not age

Write `Circle` with a radius and two properties, `area` and `perimeter`. Change the radius and check
that both update.

Then write `BrokenCircle` storing the area as an ordinary attribute and show that it goes stale.

### Exercise 5 · The shared list

Write `Group` with a student list declared in the class body. Create two groups, add a student to one,
and show what the other one sees.

Then fix it and prove with `is` that they are now two separate lists.

### Exercise 6 · The counter that does not count

Write a class with a class attribute `total` that tries to increment itself with `self.total += 1`.
Create five objects and show that the total is still zero.

Fix it and explain in a comment why exercise 5's list did get shared and the integer did not.

### Exercise 7 · Loan

Write `Loan` with a title, a borrowing day and a class constant for the maximum term. Add an
`overdue(today)` method.

Test it with three loans and two different dates, including the exact due day.

### Exercise 8 · The honest constructor

Write a class that needs to read a file. Do it first with the reading inside `__init__` and show that
a missing file leaves you with no object. Then split it out into a `load` method.

### Exercise 9 · The lab

Write the `Book` and `Loan` classes so the system can say whether a loan is overdue.

Three attributes per class at most, no external libraries, one public method per class. Hand in a file
with the two classes and three test objects printed to the console.

The criterion is that the names make sense without reading the bodies of the methods.
"""),

md("""
---
## Three things to take away

**The class describes, the object remembers.** One definition in the code, as many independent states
as instances you create. Methods live once and `__func__ is` proves it.

**What goes in `__init__` belongs to each object.** What gets declared in the class body is shared,
almost always by accident. It is the third costume of the same mechanism you already met in reviews 3
and 4.

**A property is a method in disguise.** It reads like data and is computed on the fly, so it never
goes out of date. It does not show up in `vars` because it is not stored anywhere.

Week 4 continues with what was left half-done today: access modifiers, the `@setter` that completes
`@property`, and static members, which are cousins of this notebook's `total_created`.

### A debugging method for the lab

Explain your code out loud, line by line, to somebody who cannot help you. It is called **rubber duck
debugging** and it works because saying things out loud forces you to check the assumptions that
reading skips over. Use it once you have gone ten minutes without a new hypothesis about the bug.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"{self.title}, by {self.author}")


books = [
    Book("The Aleph", "Borges"),
    Book("Pedro Paramo", "Rulfo"),
    Book("The Truce", "Benedetti"),
]

for book in books:
    book.describe()

print()
for book in books:
    print(vars(book))

# All three have the same two keys, because they came out of the same
# constructor. None shares a value with another, because each self.title = title
# ran in its own call. The class gives the shape; the object supplies the
# contents.
```

### Exercise 2

```python
class Example:
    def __init__(self, value):
        self.value = value

    def show():
        print("I never get there")


e = Example(7)

try:
    e.show()
except TypeError as error:
    print("TypeError:", error)

# Through the class, passing the object by hand:
try:
    Example.show(e)
except TypeError as error:
    print("TypeError:", error)

Example.show()             # with no object, this one runs

# e.show() becomes Example.show(e), so one argument arrives at a function that
# accepts none. Calling it through the class with no arguments works because
# nobody inserts the object: it is an ordinary function that happens to live
# inside a class.
```

### Exercise 3

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


p = Product("coffee", 45.0)
p.pirce = 39.0             # the typo

print("Price:", p.price)
print("State:", vars(p))
print("Attributes:", len(vars(p)))

# In a thousand lines I would spot it by the symptom, not by an error: the
# discount gets applied and the total does not go down. To catch it earlier,
# print vars() of the object right after the assignment, or use __slots__, which
# makes Python reject any attribute that was not declared.
```

### Exercise 4

```python
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


class BrokenCircle:
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * radius ** 2


c = Circle(1)
print(f"radius 1 -> area {c.area:.4f}  perimeter {c.perimeter:.4f}")
c.radius = 3
print(f"radius 3 -> area {c.area:.4f}  perimeter {c.perimeter:.4f}")

print()
broken = BrokenCircle(1)
broken.radius = 3
print(f"radius {broken.radius} -> reported area {broken.area:.4f}")
print(f"            real area     {math.pi * broken.radius ** 2:.4f}")
```

The broken circle reports the area of radius 1 while holding radius 3. No error, a perfectly
reasonable-looking number, and a factor of nine.

### Exercise 5

```python
class SharedGroup:
    students = []

    def __init__(self, code):
        self.code = code

    def enrol(self, name):
        self.students.append(name)


one = SharedGroup("COM102-01")
two = SharedGroup("COM102-02")
one.enrol("Ana")

print("Group 1:", one.students)
print("Group 2:", two.students, "<- without enrolling anybody")
print("the same list?", one.students is two.students)

print()


class Group:
    def __init__(self, code):
        self.code = code
        self.students = []

    def enrol(self, name):
        self.students.append(name)


one = Group("COM102-01")
two = Group("COM102-02")
one.enrol("Ana")

print("Group 1:", one.students)
print("Group 2:", two.students)
print("the same list?", one.students is two.students)
```

### Exercise 6

```python
class BrokenCounter:
    total = 0

    def __init__(self):
        self.total += 1


for _ in range(5):
    BrokenCounter()
print("Broken:", BrokenCounter.total)


class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1


for _ in range(5):
    Counter()
print("Good:", Counter.total)

# The list got shared because append does not assign: it modifies the object
# that was already there, and that object was the class's. An integer is
# immutable, so adding one builds a new integer and the assignment has to write
# it somewhere. It writes to the instance, always. That is why mutables get
# shared by accident and immutables get copied by accident.
```

### Exercise 7

```python
class Loan:
    MAX_DAYS = 14

    def __init__(self, title, day_borrowed):
        self.title = title
        self.day_borrowed = day_borrowed

    def overdue(self, today):
        return today - self.day_borrowed > Loan.MAX_DAYS


loans = [
    Loan("The Aleph", 1),
    Loan("Pedro Paramo", 5),
    Loan("The Truce", 12),
]

for day in [15, 20]:
    print(f"On day {day}:")
    for loan in loans:
        print(f"  {loan.title:<15}borrowed on {loan.day_borrowed:>2}  overdue: {loan.overdue(day)}")
    print()

# The exact due day: borrowed on 1, term of 14, due on 15.
one = Loan("Probe", 1)
print("day 15:", one.overdue(15), "· day 16:", one.overdue(16))
```

With `>`, day 15 is not yet overdue and day 16 is. With `>=` it would fall due a day earlier. The
boundary is set by the library's rules, not by what is convenient in code, which is why it has to be
tested with the exact value.

### Exercise 8

```python
class BrokenSettings:
    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.lines = f.readlines()


try:
    cfg = BrokenSettings("missing.txt")
except FileNotFoundError:
    print("No object left to inspect. You cannot even tell which path it was.")


class Settings:
    def __init__(self, path):
        self.path = path
        self.lines = []

    def load(self):
        with open(self.path) as f:
            self.lines = f.readlines()
        return self


cfg = Settings("missing.txt")
try:
    cfg.load()
except FileNotFoundError:
    print(f"Loading {cfg.path} failed, and the object is still available.")
    print("State:", vars(cfg))
```

### Exercise 9

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def summary(self):
        return f"{self.title} · {self.author} · ISBN {self.isbn}"


class Loan:
    MAX_DAYS = 14

    def __init__(self, book, member, day_borrowed):
        self.book = book
        self.member = member
        self.day_borrowed = day_borrowed

    def overdue(self, today):
        return today - self.day_borrowed > Loan.MAX_DAYS


catalogue = [
    Book("The Aleph", "Borges", "978-84-206-3311-0"),
    Book("Pedro Paramo", "Rulfo", "978-968-16-7729-7"),
    Book("The Truce", "Benedetti", "978-84-206-3350-9"),
]

loans = [
    Loan(catalogue[0], "Ana", 1),
    Loan(catalogue[1], "Luis", 5),
    Loan(catalogue[2], "Carla", 12),
]

TODAY = 20
for loan in loans:
    status = "OVERDUE" if loan.overdue(TODAY) else "in time"
    print(f"{loan.member:<7}{loan.book.summary():<48}{status}")
```

Three decisions worth defending.

`Loan` holds the whole `Book` object rather than the title, so there are no two places where the title
could differ. That is week 2's lesson applied inside a class.

`MAX_DAYS` is a class attribute because it is a rule of the library and not of each loan. If the
policy changes tomorrow, it changes once.

`summary` returns rather than prints, which lets the loop above line it up in a column. That is review
3's lesson, and it is also what will let that same text come out of `__str__` in week 8.
"""),

]

write(OUT / "en" / "w03.ipynb", en)
print("wrote", OUT / "en" / "w03.ipynb")
