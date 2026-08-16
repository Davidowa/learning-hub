"""notebooks/programacion-orientada-a-objetos/en/w02.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w02.en.yaml
Source code:  the deck's two code blocks, grupo_estructurado.py and grupo_poo.py,
              were written for the course. There is no repository file for this
              week; the topic is conceptual and the class code starts in
              02 - POO/6th Module from week 4 onward.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 02
## Topic 1 · Introduction to OOP

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Why the paradigm exists. What was breaking in 1970s programs and what got invented to fix it.

The five reviews are behind you, and with them all the Python this session needs. There is no new
syntax to memorise here. There is one question: why would anyone write ten lines where four would
do, and what do they get for it.

By the end of this notebook you will be able to:

1. Define what a paradigm is, and why one language can support several at once.
2. Solve the same problem in three styles and measure how they differ.
3. Name the four principles of the paradigm and spot them in code you already use.
4. Decide when a class gets in the way and a plain function does the job better.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Five fail on purpose, and **four of the five raise no
exception**. This is the notebook where that matters most: the whole argument of the session is that
the structured style breaks silently as a program grows, and the only honest way to make that case is
to show it breaking.
"""),

md("""
---
# Block 1 · What a paradigm is

A paradigm is not a syntax. It is an agreement about how the code gets divided up before you write
it.

It does not change what the computer executes in the end, because everything turns into machine
instructions. It changes **where each piece of the logic lives and who is allowed to touch it**.

We are going to solve the same problem three times. The problem is deliberately tiny: a group of
students with a name and a grade, the average, and who passed.

## Imperative style: instructions in sequence
"""),

code("""
names = ["Ana", "Luis", "Sofia", "Beto", "Carla"]
marks = [8.5, 7.0, 9.5, 5.5, 9.0]

total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)

passing = []
i = 0
while i < len(names):
    if marks[i] >= 7.0:
        passing.append(names[i])
    i = i + 1

print("Average:", average)
print("Passing:", passing)
"""),

md("""
It works, and it is the style of the 1950s: instructions one after another, without a single
function.

What it lacks is not correctness, it is a name. To know that the first loop computes an average you
have to read all of it. And if tomorrow the average is needed somewhere else, it gets copied and
pasted.

## Structured style: instructions get grouped
"""),

code("""
names = ["Ana", "Luis", "Sofia", "Beto", "Carla"]
marks = [8.5, 7.0, 9.5, 5.5, 9.0]
degrees = ["Mechatronics", "Systems", "Mechatronics", "Industrial", "Systems"]


def average(values):
    return sum(values) / len(values)


def passing(names, marks, minimum=7.0):
    return [n for n, m in zip(names, marks) if m >= minimum]


def report(names, marks):
    for name, mark in zip(names, marks):
        print(f"  {name:<7}{mark}")


print("Average:", average(marks))
print("Passing:", passing(names, marks))
print("Report:")
report(names, marks)
"""),

md("""
This is the 1970s style, and with five students there is nothing to criticise. Every function has a
name, can be tested on its own and gets used in several places. It is exactly what review 3 asked
for.

The problem is not in the functions. It is in the three lists.

**What keeps a student together with their grade is the position.** Nothing else. `names[1]` and
`marks[1]` are the same person because both sit at index 1, and that agreement is written down
nowhere: it lives in the head of whoever wrote the file.

## What happens when somebody drops the course
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Luis drops out and gets deleted from one list only.
names.remove("Luis")

print("Lengths:", len(names), len(marks), len(degrees))
print()
print("The report that comes out:")
report(names, marks)
print()
print("Average:", average(marks))
print("Passing:", passing(names, marks))
"""),

md("""
No error. No warning. A complete report, with real names and real grades.

And it is wrong in three different ways at once.

**Sofia shows up with 7.0 and she had 9.5.** From the position Luis used to occupy onward, every name
got paired with the next student's grade. Beto went from 5.5 to 9.5 and passed without passing.

**One grade lost its owner.** `zip` stops at the shortest list, so the four remaining names consumed
four of the five grades and Carla's 9.0 never got printed. `zip` never warns about that.

**The average still says 7.9**, which is the correct average of five grades spread across four
students. An exact number for a population that no longer exists.

The cell below measures the damage instead of describing it.
"""),

code("""
ORIGINAL = {"Ana": 8.5, "Luis": 7.0, "Sofia": 9.5, "Beto": 5.5, "Carla": 9.0}

print(f"{'Student':<9}{'Real':>7}{'Reported':>11}   ")
for name, mark in zip(names, marks):
    flag = "ok" if ORIGINAL[name] == mark else "WRONG"
    print(f"{name:<9}{ORIGINAL[name]:>7}{mark:>11}   {flag}")

missing = set(ORIGINAL) - set(names)
print()
print("Students who no longer appear:", sorted(missing))
print("Pairs zip produced:", len(list(zip(names, marks))),
      "out of", len(marks), "grades")
"""),

md("""
Three of four lines are wrong and the program never said a word.

This is the whole argument of the session, and no other one is needed. The structured style has no
mechanism whatsoever to stop two lists that belong together from drifting apart. The programmer's
discipline is the only thing holding them, and discipline fails.

## The second way to break it
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Sorting the marks to build a ranking.
names = ["Ana", "Luis", "Sofia", "Beto", "Carla"]
marks = [8.5, 7.0, 9.5, 5.5, 9.0]

sorted_marks = sorted(marks, reverse=True)

print("Class ranking:")
for place, (name, mark) in enumerate(zip(names, sorted_marks), start=1):
    real = ORIGINAL[name]
    flag = "" if real == mark else f"  (their real mark is {real})"
    print(f"  {place}. {name:<7}{mark}{flag}")
"""),

md("""
Ana tops the ranking with a 9.5 that belongs to Sofia. Beto comes out with 7.0 and passes on a grade
of 5.5.

Sorting one of the two lists breaks the positional agreement in one stroke, and it is the first thing
anybody reaches for when building a ranking. In the object version this cannot be written wrong,
because there are no two lists to sort.

## Object-oriented style: the data travels with its functions
"""),

code("""
class Student:
    def __init__(self, name: str, mark: float, degree: str) -> None:
        self.name = name
        self.mark = mark
        self.degree = degree

    def passed(self, minimum: float = 7.0) -> bool:
        return self.mark >= minimum

    def __repr__(self) -> str:
        return f"Student({self.name!r}, {self.mark})"


group = [
    Student("Ana", 8.5, "Mechatronics"),
    Student("Luis", 7.0, "Systems"),
    Student("Sofia", 9.5, "Mechatronics"),
    Student("Beto", 5.5, "Industrial"),
    Student("Carla", 9.0, "Systems"),
]

print(group)
print("Average:", sum(s.mark for s in group) / len(group))
print("Passing:", [s.name for s in group if s.passed()])
"""),

md("""
Ten lines where there used to be four. That is the bill, and it has to be acknowledged before the
benefit gets collected.

None of the syntax is entirely new: `class`, `def`, parameters with defaults, type annotations that
do not enforce anything, `return`. The only thing you have not seen is `self`, and week 3 is devoted
to it. For now, read it as "this object".

Now the two operations that broke the previous version.
"""),

code("""
# Drop Luis.
group = [s for s in group if s.name != "Luis"]

print(len(group), "students left")
for s in group:
    print(f"  {s.name:<7}{s.mark}")
print("Average:", sum(s.mark for s in group) / len(group))

print()
# The ranking.
for place, s in enumerate(sorted(group, key=lambda s: -s.mark), start=1):
    print(f"  {place}. {s.name:<7}{s.mark}")
"""),

md("""
The average moved from 7.9 to 8.125 because it is now computed over the four students who are
actually there, rather than over five grades spread across four people. And the ranking is right
without anybody having to be careful.

It is not that the code above is smarter. It is that **the question that broke the program can no
longer be asked**. There is no way to delete the name and keep the grade, because they do not live in
two places. There is no way to sort the marks without taking the names along, because there is no
loose list of marks.

That is the exact benefit of OOP: it does not make anything possible that was impossible before, it
makes a certain class of error impossible.

## The cost of a change, measured
"""),

code("""
# Adding a new field: the enrolment date.

# Structured version: one more list, and every function that uses it has to change.
dates = ["2026-01-15", "2026-01-16", "2026-01-15", "2026-01-20", "2026-01-15"]
LISTS = ["names", "marks", "degrees", "dates"]
print("Structured:", len(LISTS), "parallel lists to keep aligned")
print("           ", len(LISTS) * (len(LISTS) - 1) // 2,
      "pairs that can drift apart")


# Object version: one line in the constructor.
class StudentWithDate(Student):
    def __init__(self, name, mark, degree, date):
        super().__init__(name, mark, degree)
        self.date = date


ana = StudentWithDate("Ana", 8.5, "Mechatronics", "2026-01-15")
print()
print("OOP:", len(vars(ana)), "attributes in 1 object")
print("     0 pairs that can drift apart")
print(vars(ana))
"""),

md("""
With four lists there are six pairs that can fall out of sync, and each one is a bug waiting. With
five lists there would be ten. The number grows faster than the amount of data, and that is the exact
moment the structured style stops scaling.

Notice what `vars(ana)` printed as well: a dictionary. **A Python object keeps its attributes in an
actual dictionary**, the same type from review 4. Week 3 starts right there.

## A fourth style, to complete the map
"""),

code("""
from collections import namedtuple

StudentTuple = namedtuple("StudentTuple", "name mark degree")

functional_group = [
    StudentTuple("Ana", 8.5, "Mechatronics"),
    StudentTuple("Luis", 7.0, "Systems"),
    StudentTuple("Sofia", 9.5, "Mechatronics"),
]

# Nothing gets modified: every operation returns something new.
raised = [s._replace(mark=s.mark + 0.5) for s in functional_group]

print("Originals:", [(s.name, s.mark) for s in functional_group])
print("Raised:   ", [(s.name, s.mark) for s in raised])

# FAILS ON PURPOSE. This one does raise, and that is the style's guarantee.
try:
    functional_group[0].mark = 10.0
except AttributeError as e:
    print()
    print("AttributeError:", e)
"""),

md("""
The functional style takes the idea to the opposite extreme: data never changes, and every operation
returns a new structure.

A `namedtuple` is a tuple with names, so it inherits the immutability from review 4 and that is why
the assignment raises. What looks like a limitation is the style's entire guarantee: if nothing
changes, nothing can drift apart.

| Question | Structured | Object-oriented | Functional |
|---|---|---|---|
| Basic unit | The function | The class | The pure function |
| Where the data lives | Loose variables | Inside the object | Passed in and returned |
| Who modifies it | Any function | Only its methods | Nobody, new ones get made |
| It breaks when | There is a lot of linked data | There is little real state | State has to be kept |

All three styles are in Python and none is compulsory. One language supports several paradigms at
once, and the decision stays yours in every file.

## Three answers to the same problem

**1950s, imperative.** Instructions one after another, with `GOTO` jumps to anywhere in the program.

**1970s, structured.** Instructions get grouped into functions with defined inputs and outputs.

**1980s, object-oriented.** Data travels with the functions that work on it, in a single unit.

Each jump happened when the previous style stopped scaling. The first language with classes and
objects is **Simula 67**, from 1967, twelve years before the term became common. Ole-Johan Dahl and
Kristen Nygaard designed it in Norway to simulate physical systems, not to write business software,
and OOP only became common once programs went from thousands to hundreds of thousands of lines.
"""),

md("""
---
# Block 2 · The four principles

Abstraction, encapsulation, inheritance and polymorphism. They hold each other up, which is why they
get taught together.

Each has its own week later on. Here they only get named, with the shortest version that runs,
because you have been using all four without calling them that.

## Abstraction: describing a thing by what it does

Keeping what is essential and hiding the rest.
"""),

code("""
for value in ["text", [1, 2, 3], {"a": 1, "b": 2}, {1, 2, 3}, (1, 2)]:
    print(f"{str(value):<18}{type(value).__name__:<7}len = {len(value)}")
"""),

md("""
`len` gave you the length of five structures that look nothing alike on the inside. A string counts
characters, a dictionary counts keys, a set counts unique items.

You wrote `len(value)` five times and not once did you know how it was implemented. **That is
abstraction**: using something for what it does rather than for how it is built. You were already
doing it.

## Encapsulation: the object decides what it exposes
"""),

code("""
class Account:
    def __init__(self, holder, balance=0.0):
        self.holder = holder
        self._balance = balance      # the underscore says "this is my business"
        self.movements = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit has to be positive")
        self._balance += amount
        self.movements.append(("deposit", amount))

    def balance(self):
        return self._balance


account = Account("Ana", 1000.0)
account.deposit(500)
print("Balance:", account.balance())
print("Movements:", account.movements)

try:
    account.deposit(-200)
except ValueError as e:
    print("ValueError:", e)
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The underscore is an agreement, not a lock.
account._balance = 999999

print("Balance:", account.balance())
print("Movements:", account.movements)
print()
print("The balance says", account.balance(), "and the movements add up to",
      sum(m for _, m in account.movements) + 1000.0)
"""),

md("""
The object is now lying. The balance says one number and the movement list tells another story, and
both live in the same object.

`deposit` refused a negative amount, but touching `_balance` directly skipped that validation
entirely. The underscore is a convention between programmers, not a language mechanism: it says "this
is my business", and Python does not enforce it.

Week 4 covers access modifiers and week 6 covers encapsulation properly, including the double
underscore, which does change something. For now hold on to the idea: **encapsulating means the
object is the only one that can leave its data in an impossible state**, and one assignment from
outside breaks that without a word.

## Inheritance: reuse without copying
"""),

code("""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def greet(self):
        return f"{super().greet()} and I teach {self.subject}"


for someone in [Person("Ana"), Teacher("David", "COM102")]:
    print(someone.greet())

print()
print("Is a teacher a person?", isinstance(Teacher("D", "X"), Person))
print("Inheritance chain:", [c.__name__ for c in Teacher.__mro__])
"""),

md("""
`Teacher` did not write out how a name gets stored again. It inherited that, and only added its own
part.

That chain printed by `__mro__` is the same one you saw in review 5 with exceptions: `IndexError`
descends from `LookupError` which descends from `Exception`. Python uses one mechanism for the
standard library's exceptions and for the classes you write. Weeks 7 and 8 are about it.

## Polymorphism: the same message, different answers
"""),

code("""
print(3 + 4)
print("ab" + "cd")
print([1, 2] + [3])
print((1,) + (2,))

print()
print(3 * 3)
print("ab" * 2)
print([1] * 3)
"""),

md("""
The same `+` added, joined text, joined lists and joined tuples. None of the four operations resembles
the others on the inside.

That is already polymorphism, and you have been using it since review 1. What week 8 will teach is
how to make **your** objects answer to `+`, to `len` and to `print`, which is what magic methods are
for.

With the classes above the same mechanism looks like this.
"""),

code("""
class Undergrad(Person):
    def greet(self):
        return f"Hi, I am {self.name} and I am in my second year"


for someone in [Person("Ana"), Teacher("David", "COM102"), Undergrad("Beto")]:
    print(f"{type(someone).__name__:<10}{someone.greet()}")
"""),

md("""
The loop never asks what type each one is. It calls `greet` and each object answers its own way.

Notice what that buys: adding a new class does not force you to touch the loop. In the version with
`if type(someone) == ...` you would have to open it and add a branch every time.
"""),

md("""
---
# Block 3 · When the paradigm gets in the way

Four signs that you are forcing a class where there never was one.

## Sign 1: the class with no state
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A class that stores nothing.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
print(calc.add(2, 3), calc.subtract(9, 4), calc.multiply(3, 3))

print()
print("What the object remembers:", vars(calc), "->", len(vars(calc)), "attributes")
print("And after three operations it still remembers:", vars(calc))
"""),

md("""
The object's dictionary is empty before and after. `calc` stores absolutely nothing between one call
and the next.

That means `self` is unused in all three methods, and that the class exists purely to force you to
type `calc.` before every call. Three plain functions do the same with less ceremony and import just
as well.

Compare it with the bank account from a few cells ago.
"""),

code("""
account = Account("Ana", 1000.0)
print("Freshly built:", vars(account))

account.deposit(500)
account.deposit(250)
print("After two deposits:", vars(account))
print()
print("Attributes that change between calls:", len(vars(account)))
"""),

md("""
Here there is something to remember, and that memory is what gets called **state**. The balance
depends on every previous deposit, so the account cannot be a function: a function that takes and
returns the balance every time hands the problem back to its caller.

## The other three signs

**Getters and setters for everything.** If every private attribute has a method to read it and
another to write it, you encapsulated nothing: you built a back door with extra steps. A `set_balance`
that assigns without checking is exactly the cell that left the account lying.

**Five levels of inheritance.** When you have to climb four classes to understand what a method does,
the hierarchy has lost the plot. Week 7 draws the line in practice.

**A thirty-line script.** To read a CSV and compute an average, a plain function wins every time. The
bill of ten lines against four only pays off when the program lives long enough to change.

## The name test

Try naming the class with a concrete noun. If the best name you can think of is a verb, or ends in
"-er" or "-manager", it was probably a function.
"""),

code("""
CANDIDATES = [
    ("Student", "concrete noun", "class"),
    ("Account", "concrete noun", "class"),
    ("Invoice", "concrete noun", "class"),
    ("Calculator", "a noun, but with nothing to remember", "function"),
    ("DataProcessor", "a verb in disguise", "function"),
    ("FileManager", "a verb in disguise", "function"),
    ("EmailValidator", "a verb in disguise", "function"),
]

print(f"{'Name':<18}{'What it is':<40}{'Verdict'}")
for name, what, verdict in CANDIDATES:
    print(f"{name:<18}{what:<40}{verdict}")
"""),

md("""
`EmailValidator` with a `validate` method is a function called `validate_email` that got given a
house. `Invoice` holds concepts, lines, taxes and a total that depends on all of them, so it is a
class.

## Predict before you run

Which of these four is the only one that calls for a class?

- **A.** Converting Celsius to Fahrenheit.
- **B.** A bank account with a balance and movements.
- **C.** Counting how many vowels a word has.
- **D.** Sorting a list of numbers from low to high.

Rather than answering from memory, the cell below applies the criterion: **does the object remember
anything between one call and the next?**
"""),

code("""
class CelsiusToFahrenheit:
    def convert(self, c):
        return c * 9 / 5 + 32


class VowelCounter:
    def count(self, word):
        return sum(1 for letter in word.lower() if letter in "aeiou")


class Sorter:
    def sort(self, numbers):
        return sorted(numbers)


probes = [
    ("Celsius to Fahrenheit", CelsiusToFahrenheit(), lambda o: o.convert(100)),
    ("Bank account", Account("Ana", 1000.0), lambda o: o.deposit(500)),
    ("Counting vowels", VowelCounter(), lambda o: o.count("onomatopoeia")),
    ("Sorting a list", Sorter(), lambda o: o.sort([3, 1, 2])),
]

print(f"{'Case':<24}{'Before':>8}{'After':>7}{'Changed?':>10}   Verdict")
for label, obj, operation in probes:
    before = dict(vars(obj))
    operation(obj)
    after = dict(vars(obj))
    changed = "yes" if before != after else "no"
    verdict = "class" if after else "function"
    print(f"{label:<24}{len(before):>8}{len(after):>7}{changed:>10}   {verdict}")
"""),

md("""
The answer is **B**.

Three of the four objects still have zero attributes after doing their job, and the changed column
says no. The bank account has three attributes and their contents did change with the operation: the
balance went from 1000 to 1500 and a movement got recorded.

| Option | Keeps state? | Linked data? | Verdict |
|---|---|---|---|
| Celsius to Fahrenheit | No | No | Function |
| Bank account | Yes, the balance | Yes, balance and movements | Class |
| Counting vowels | No | No | Function |
| Sorting a list | No | No | Function |

Only the account remembers anything between one operation and the next. That memory is the state, and
it is the only solid reason to write a class.

> The big idea is messaging. The focus should be on how objects communicate, not on how they are made
> inside.
>
> Alan Kay, correspondence on the design of Smalltalk, 1998
"""),

md("""
---
# Exercises

The solutions are at the very bottom of the notebook.

### Exercise 1 · Breaking the parallel lists

With three lists of products, prices and stock levels, delete a product from one list only and show
the report that comes out. Point out how many lines are wrong and how many products disappeared.

### Exercise 2 · The same problem with objects

Rewrite exercise 1 with a `Product` class. Delete the same product and show that the report stays
correct.

Explain in a comment which operation from the previous version can no longer be written wrong.

### Exercise 3 · Measuring the coupling

Write a function `misalignable_pairs(n)` returning how many pairs of lists can fall out of sync with
`n` parallel lists. Compute it for 2, 3, 4, 5 and 10 lists.

Say in a comment at how many lists the number starts looking unmanageable to you.

### Exercise 4 · Abstraction you were already using

Find three Python functions besides `len` that work across different types without you having to know
how they are implemented. Test each with at least three types.

### Exercise 5 · The object that lies

Write a `Thermometer` class with a `record(temperature)` method that rejects values below -273.15.
Then leave the object in an impossible state by modifying the attribute directly, and show that the
object is no longer coherent.

### Exercise 6 · Minimal inheritance

Write `Vehicle` with a `describe` method, and two subclasses that override it. Walk them in a loop
that never asks about the type.

Add a third subclass and check that the loop did not change.

### Exercise 7 · Class or function

For each of these six cases decide class or function, justifying with the state test:

1. Computing the tax on an amount.
2. A shopping cart.
3. Converting a date from text to an object.
4. A timer that can be paused and resumed.
5. Counting words in a text.
6. A chess game.

### Exercise 8 · The calculator that does have state

Turn the stateless `Calculator` into one that does keep state: it remembers the previous result and
lets you chain operations. Show with `vars` that it now stores something.

### Exercise 9 · The homework

Pick a system you use every day, the transport app, the cafeteria or the gym, and describe the same
module in all three paradigms.

Hand in a three-column table with the basic unit, where the data lives and who modifies it. The module
has to fit in half a page. The OOP column names concrete objects, not categories like "manager" or
"handler".

Add a paragraph on which paradigm you would pick for that system and why, arguing from the system you
chose and not from generalities.
"""),

md("""
---
## Three things to take away

**The paradigm solves a problem of scale.** At a hundred lines any of the three works. The difference
shows up as the program grows, and it shows up as lists drifting apart without a single exception.

**The four principles are a set.** Abstraction, encapsulation, inheritance and polymorphism hold each
other up, and all four were already in the Python you were using before this session.

**Forcing classes is expensive.** A class with no state is a function with extra steps and a worse
name. The empty dictionary from `vars` is the proof, and it fits on one line.

Week 3 starts with the first code that really runs: what a class is, what an object is, and what on
earth `self` is. The clue is already in this notebook: `vars(ana)` returned a dictionary.
"""),

md("""
---
# Solutions

### Exercise 1

```python
products = ["coffee", "filter", "mug", "press"]
prices = [45.0, 12.0, 89.0, 340.0]
stock = [30, 120, 45, 8]

REAL = dict(zip(products, prices))

products.remove("filter")

print("Report:")
wrong = 0
for product, price in zip(products, prices):
    correct = REAL[product] == price
    wrong += 0 if correct else 1
    print(f"  {product:<8}{price:>8}  {'ok' if correct else 'WRONG'}")

print()
print("Wrong lines:", wrong, "of", len(list(zip(products, prices))))
print("Products that vanished:", sorted(set(REAL) - set(products)))
print("Stock counts with no owner:", len(stock) - len(products))
```

Two lines come out wrong, one product drops off the report and one stock count is left without a
product. Not a single line raises anything.

### Exercise 2

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.name!r}, {self.price}, {self.stock})"


inventory = [
    Product("coffee", 45.0, 30),
    Product("filter", 12.0, 120),
    Product("mug", 89.0, 45),
    Product("press", 340.0, 8),
]

inventory = [p for p in inventory if p.name != "filter"]

for p in inventory:
    print(f"  {p.name:<8}{p.price:>8}{p.stock:>6}")

print("Inventory value:", sum(p.price * p.stock for p in inventory))

# The operation that can no longer be written wrong is deleting from one list
# and not the others. There are no others: the price and the stock live inside
# the same object as the name, so they go with it or stay with it.
```

### Exercise 3

```python
def misalignable_pairs(n):
    return n * (n - 1) // 2


for n in [2, 3, 4, 5, 10]:
    print(f"{n:>3} lists -> {misalignable_pairs(n):>3} pairs")

# From five lists on it is already ten pairs, and nobody checks ten invariants
# by hand on every change. That is where the style stops scaling, and it does
# not line up with the program being long: it lines up with the data being
# linked together.
```

### Exercise 4

```python
VALUES = ["text", [1, 2, 3], (4, 5), {"a": 1}, {7, 8, 9}]

for function in [len, sorted, list]:
    print(function.__name__)
    for value in VALUES:
        print(f"  {str(value):<14}{function(value)}")
    print()

print("bool on each one:", [bool(v) for v in VALUES])
print("bool on the empty ones:", [bool(v) for v in ["", [], (), {}, set()]])
```

`sorted`, `list` and `bool` work on all five without you knowing anything about their implementation.
`bool` is the most interesting: each type decides what being empty means, and they all answer the same
question.

### Exercise 5

```python
class Thermometer:
    ABSOLUTE_ZERO = -273.15

    def __init__(self, location):
        self.location = location
        self._readings = []

    def record(self, temperature):
        if temperature < self.ABSOLUTE_ZERO:
            raise ValueError(f"Impossible: {temperature} is below absolute zero")
        self._readings.append(temperature)

    def lowest(self):
        return min(self._readings) if self._readings else None


t = Thermometer("laboratory")
t.record(21.5)
t.record(19.0)
print("Lowest:", t.lowest())

try:
    t.record(-300)
except ValueError as e:
    print("ValueError:", e)

# And now through the back door.
t._readings.append(-300)
print("Lowest afterwards:", t.lowest())
print("The object reports a temperature its own method refused.")
```

The validation lives in `record` and the list is exposed, so all it takes is not calling the method.
Week 6 shuts that door.

### Exercise 6

```python
class Vehicle:
    def __init__(self, plate):
        self.plate = plate

    def describe(self):
        return f"Vehicle {self.plate}"


class Car(Vehicle):
    def describe(self):
        return f"Car {self.plate}, four wheels"


class Motorbike(Vehicle):
    def describe(self):
        return f"Motorbike {self.plate}, two wheels"


class Lorry(Vehicle):
    def describe(self):
        return f"Lorry {self.plate}, six wheels"


fleet = [Car("ABC-123"), Motorbike("XY-99"), Lorry("TRK-001")]
for v in fleet:
    print(v.describe())
```

The loop is identical before and after adding `Lorry`. That is the property that makes polymorphism
useful: the code that uses the objects does not change when new types show up.

### Exercise 7

```python
CASES = [
    ("Computing tax", "function", "an amount goes in, another comes out, nothing is remembered"),
    ("Shopping cart", "class", "the lines and the total live between calls"),
    ("Text date to object", "function", "a conversion with no memory"),
    ("Timer with pause", "class", "the accumulated time and whether it is running"),
    ("Counting words", "function", "the text goes in and a number comes out"),
    ("Chess game", "class", "the board, the turn and the move list"),
]

for case, verdict, reason in CASES:
    print(f"{case:<22}{verdict:<10}{reason}")
```

The three that call for a class have one thing in common: the next operation depends on the previous
ones. Pausing a timer only means something if the object remembers how far it had got.

### Exercise 8

```python
class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []

    def add(self, n):
        self.result += n
        self.history.append(f"+ {n}")
        return self

    def multiply(self, n):
        self.result *= n
        self.history.append(f"× {n}")
        return self


calc = Calculator()
print("Freshly built:", vars(calc))

calc.add(5).multiply(3).add(2)

print("After three operations:", vars(calc))
print("Result:", calc.result)
print("History:", " ".join(calc.history))
```

Each method returns `self`, which is why the calls chain. That only makes sense because there is
state: with no stored result, chaining would mean nothing.

### Exercise 9

The lab table, using the faculty cafeteria as the example and the orders module.

| Question | Structured | Object-oriented | Functional |
|---|---|---|---|
| Basic unit | `compute_total`, `add_product` | `Order`, `Product`, `Customer` | `add(order, product) -> order` |
| Where the data lives | Parallel lists of products, quantities and prices | Each `Order` holds its lines and its total | In the order that goes in and the one that comes out |
| Who modifies it | Any function in the file | Only `Order`'s methods | Nobody, every operation returns a new order |

For the cafeteria I would pick object-oriented, and the reason is concrete: an order changes several
times before it closes. A coffee gets added, then removed, the student discount gets applied, it gets
marked as paid. Each of those steps depends on the previous one, and the total has to match the lines
at every moment. That is linked state, which is exactly the case the paradigm solves.

If the module were the menu board, which only reads a price list and prints it, I would pick plain
functions. There is nothing to remember between one printing and the next.

Notice that the OOP column names `Order`, `Product` and `Customer`, which are things that exist in the
cafeteria and that the staff would call by the same names. If the column said `OrderManager` it would
be naming the code instead of the problem.
"""),

]

write(OUT / "en" / "w02.ipynb", en)
print("wrote", OUT / "en" / "w02.ipynb")
