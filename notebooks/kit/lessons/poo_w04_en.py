"""notebooks/programacion-orientada-a-objetos/en/w04.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w04.en.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code019.py
              docs/en/courses/python-course/02 - POO/6th Module/Code022.py

Two real bugs in the sources, quoted as traps and never as if they ran:

  Code019.py line 146 puts self.__say_age() inside an f-string. The method
  prints and returns None, so the output comes out in the wrong order and ends
  in "and None". The comment on line 159 claims otherwise. Nothing is raised.

  Code022.py line 62 calls Person.get_species() on the second of the file's
  four Person definitions, which carries the method but not the species
  attribute. AttributeError, and the file stops there.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 04
## Topic 2 · Basic elements

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Who gets to touch what inside an object, and the three pieces that decide how it is born: access
modifiers, access functions and constructors.

Last week left two things half finished. `@property` showed up read-only, and I promised `@setter`
completed it. `total_created` showed up as a counter that had to be written on the class, and I
promised static members were its topic. Both come due today.

By the end you will be able to:

1. Pick an access level for each member and say who enforces it in each case.
2. Write a getter and a setter that validate, and explain why validating in the constructor is not
   enough.
3. Turn them into a property without changing a single line of the code that already used the class.
4. Separate what belongs to the class from what belongs to each object.
5. Write an alternative constructor with `@classmethod`, and know when `cls` cannot be swapped for the
   class name.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Twelve fail on purpose and carry a comment saying so.

Seven of the twelve **raise no exception at all**. Two of the twelve are not mine: they come out of the
course code, from `Code019.py` and `Code022.py` in module 6. One of those two is among the silent ones,
and it is the worst in the notebook. Both are flagged where they appear.
"""),

md("""
---
# Block 1 · Access modifiers

Python has no `private` keyword. It has a convention and a renaming trick, and it pays to know which
is which before trusting either one.

In Java or C# the compiler enforces the access level: write to a private field from outside and the
program will not build. In Python the interpreter almost never objects. What you get is an agreement
between the people reading the code, plus a renaming that gets in the way just enough that nobody
crosses the line by accident.

We start with the class from module 6, exactly as it sits in the repository.
"""),

code("""
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name           # private: two underscores
        self.age = age               # public: an age changes every year

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name}")


person = Person("Ana", 20)
person.talk()

print("Age:", person.age)
person.age = 21
print("Age afterwards:", person.age)
"""),

md("""
The age reads and writes from outside with no ceremony at all, because that is how it was declared.
The name does not.

The question that matters is not which of the two is right, it is which of the two decisions you can
defend. An age changes every year and whoever uses the class has to be able to change it. A name
almost never changes, and if it did you would not want it happening through a loose assignment in the
middle of some function.

## What reads from outside, measured
"""),

code("""
class Account:
    def __init__(self, holder, bank, balance):
        self.holder = holder         # public
        self._bank = bank            # protected by convention
        self.__balance = balance     # private by renaming


account = Account("Ana", "Barclays", 1500)

names = ["holder", "_bank", "__balance"]
readable = 0
for name in names:
    if hasattr(account, name):
        readable += 1
        print(f"  account.{name:<10} -> {getattr(account, name)}")
    else:
        print(f"  account.{name:<10} -> no such name")

print()
print(f"{readable} of {len(names)} read under the name written in the class")
print("What the object actually holds:", list(vars(account)))
print("Under its real name, the third one reads too:", account._Account__balance)
"""),

md("""
Two out of three. The single underscore stopped nothing.

The only one of the three prefixes that changes what the interpreter does is the double one. With it,
Python rewrites `__balance` as `_Account__balance` while compiling the class body. Inside the methods
the translation is automatic, which is why `self.__balance` works; from outside you have to type the
long name, and that is the whole obstacle.

`_bank` was not renamed. It reads, it writes, and nobody complains. What the underscore says is "this
is internal, do not build anything on top of it", and whoever ignores it will not get an error: they
will get a program that breaks the day you change the internals.
"""),

code("""
# FAILS ON PURPOSE. Under the short name, the private one does not exist.
try:
    print(account.__balance)
except AttributeError as e:
    print("AttributeError:", e)

print()
print("hasattr under the short name:", hasattr(account, "__balance"))
print("hasattr under the real name: ", hasattr(account, "_Account__balance"))
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The single underscore is an agreement, not a lock.
print("Bank before: ", account._bank)

account._bank = "some other bank"    # nobody objects

print("Bank after:  ", account._bank)
print()
print("Object state:", vars(account))
print("Attributes:", len(vars(account)))
"""),

md("""
It was written, it stuck, and the object came out exactly as long as before.

This cell is why the single underscore belongs in the vocabulary table and not in the list of
mechanisms. It is there to talk to another programmer. It is not there to prevent anything.

Compare it with the previous cell: that one raised an `AttributeError`, so you find out at once. Here
there is no symptom.

## Methods close too
"""),

code("""
class FullPerson:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name}")
        self.__say_age()

    def __say_age(self) -> None:
        print(f"and I am {self.age} years old")


ana = FullPerson("Ana", 20)
ana.talk()

print()
print("The class's own methods and attributes:")
print("  ", [n for n in vars(FullPerson) if not n.startswith("__")])
"""),

md("""
`__say_age` makes no sense outside `talk`. It is not a service the class offers, it is a chunk of
`talk` with a name of its own, and closing it says exactly that.

Look at the class dictionary: the method shows up as `_FullPerson__say_age`. The renaming is the same
one the attributes got, because it is the same rule applied to any name starting with two underscores
inside a class body.
"""),

code("""
# FAILS ON PURPOSE. Calling the private method from outside.
try:
    ana.__say_age()
except AttributeError as e:
    print("AttributeError:", e)

print()
print("Under its real name it runs:")
ana._FullPerson__say_age()
"""),

md("""
The message says `'FullPerson' object has no attribute '__say_age'`, and it says nothing about
permissions. As far as the interpreter is concerned that method does not exist under that name, full
stop.

That also explains why the renaming is not security. The second line called it with no trouble at all.
What it prevents is somebody building their program on top of an internal method **without noticing**,
which is a far more common accident than sabotage.

## The trap in the course file

`02 - POO/6th Module/Code019.py` ends with this class. I am writing it exactly as it sits there, and
the comment on line 159 of the file says it prints `Hi, my name is John and I am 20 years old`.

Run it before believing it.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. This one comes from the course file, line 146.
class ChattyPerson:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age

    def talk(self) -> None:
        print(f"Hi, my name is {self.__name} and {self.__say_age()}")

    def __say_age(self) -> None:
        print(f"I am {self.age} years old")


chatty = ChattyPerson("Ana", 20)
chatty.talk()

print()
print("What __say_age returns:", chatty._ChattyPerson__say_age())
"""),

md("""
One call to `talk()` and out came two lines, in the wrong order, ending in `None`.

What happened fits in one sentence: **to build the f-string, Python had to call `__say_age` first**.
That method prints on its own, so its line came out before the outer one. And since it has no
`return`, it handed back `None`, which is what got glued to the end of the text.

It is the lesson from review 3 inside a class: **printing is not returning**. A function that prints is
good for looking at; one that returns is good for using. Putting the first where the second was needed
raises nothing at all, because `None` converts to text without a word of protest.

This week's slide already shows the fixed version: it calls `self.__say_age()` on its own line, after
the `print`. Put the two side by side and the difference is a single brace.

Both possible corrections, so they sit together.
"""),

code("""
class ReturningPerson:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def talk(self):
        print(f"Hi, my name is {self.__name} and {self.__say_age()}")

    def __say_age(self):
        return f"I am {self.age} years old"      # returns, does not print


class PrintingPerson:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def talk(self):
        print(f"Hi, my name is {self.__name}")
        self.__say_age()                         # outside the f-string

    def __say_age(self):
        print(f"and I am {self.age} years old")


ReturningPerson("Ana", 20).talk()
print()
PrintingPerson("Ana", 20).talk()
"""),

md("""
The first is the one I would defend. A method that returns text can be printed, embedded in other
text, written to a file and compared in a test. One that prints is only good for the first of those.

In week 8 that decision comes back with a name of its own. `__str__` **returns** a string, and that is
why `print(object)` works without the class knowing anything about the console.

## The four prefixes, and who enforces each one

| Prefix | What it means | Enforced by | Example |
|---|---|---|---|
| None | Public, part of the contract | Nobody | `self.age` |
| `_one` | Internal, please leave it | The convention | `self._bank` |
| `__two` | Private, gets renamed | The interpreter | `self.__balance` |
| `__both__` | A Python magic method | The language | `__init__` |

The working rule: **start with everything public**. Close an attribute the day you find that outside
code can leave the object in an impossible state, not the day a book tells you to. An object with
twelve private attributes and twelve getter/setter pairs is exactly as open as one with twelve public
attributes, and it carries three times the code.
"""),

md("""
---
# Block 2 · Access functions

A closed attribute is no use if there is no way to read it. Here is the long way, and then the one
nobody notices.

## Getter and setter, the version with parentheses
"""),

code("""
class LongProduct:
    def __init__(self, price: float) -> None:
        self.set_price(price)            # the constructor goes through the setter

    def get_price(self) -> float:
        return self.__price

    def set_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


coffee = LongProduct(45)
print("Price:", coffee.get_price())

coffee.set_price(52)
print("New price:", coffee.get_price())
print()
print("Object state:", vars(coffee))
"""),

md("""
The setter exists for exactly one reason: **a public attribute cannot refuse a value**. That is the
entire point and there is no other.

Look at the first line of the constructor. It does not say `self.__price = price`, it says
`self.set_price(price)`. With that, validation runs on the very first value that enters the object,
and there is no way to build a product with a negative price.
"""),

code("""
# FAILS ON PURPOSE. The setter refuses, and the constructor inherits that refusal.
try:
    LongProduct(-5)
except ValueError as e:
    print("ValueError:", e)

try:
    coffee.set_price(-1)
except ValueError as e:
    print("ValueError:", e)

print()
print("The price did not move:", coffee.get_price())
"""),

md("""
Both entry points closed by the same `if`, written once.

Now the version that looks reasonable and is not.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Validating in the constructor with a public attribute.
class NaiveProduct:
    def __init__(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price


tea = NaiveProduct(38)
print("Price at construction:", tea.price)

tea.price = -1000              # the validation stayed behind, in the constructor

print("Price afterwards:     ", tea.price)
print()
print("Is the object valid?", tea.price >= 0)
print("Did anyone find out?  No. No exception, no message.")
"""),

md("""
The object was born correct and turned invalid on the next line.

Validating only in the constructor protects the first instant of the object's life and none of the
following ones. It is the trap the slide calls Error 02, and it is the most common of the four because
it feels like the work is already done.

The question that takes it apart: **how many ways are there to change this attribute?** If the answer
is more than one, the validation belongs where it changes, not where it is created.

## The same validation, without the parentheses
"""),

code("""
class Product:
    def __init__(self, price: float) -> None:
        self.price = price               # this calls the setter below

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


bread = Product(28)
print("Price:", bread.price)             # no parentheses

bread.price = 31
print("New price:", bread.price)

print()
print("Object state:", vars(bread))
"""),

md("""
The class validates just like the previous one, and whoever uses it writes `bread.price` instead of
`bread.get_price()`.

Three details worth stopping on.

`self.price = price` inside the constructor **does not create an attribute**. Since `price` is a
property declared on the class, the assignment goes through the setter, `if` and all.

The method is written twice under the same name, and that is correct. `@price.setter` takes the
property that already exists and adds the writing half to it, so the name has to repeat exactly. Get
one letter wrong and you end up with two separate properties, one of them with no getter.

The object dictionary still shows `_Product__price`. The property lives on the class, the data lives on
the object, which is why `vars` shows the mangled name and not the pretty one.

## Both versions refuse the same values, measured
"""),

code("""
CANDIDATES = [10, 0, -1, 99.99, -0.01, 250, -1000]

def try_all(cls, put):
    accepted, refused = [], []
    for value in CANDIDATES:
        try:
            obj = cls(1)
            put(obj, value)
            accepted.append(value)
        except ValueError:
            refused.append(value)
    return accepted, refused


long_way = try_all(LongProduct, lambda o, v: o.set_price(v))
short_way = try_all(Product, lambda o, v: setattr(o, "price", v))

print("With getters:   ", len(long_way[1]), "refused of", len(CANDIDATES), "->", long_way[1])
print("With a property:", len(short_way[1]), "refused of", len(CANDIDATES), "->", short_way[1])
print()
print("Do both refuse exactly the same?", long_way[1] == short_way[1])
print("And accept exactly the same?    ", long_way[0] == short_way[0])
"""),

md("""
Three of seven, the same three, in both implementations.

That is what makes the property worth having, and it is not that it is shorter. The validation did not
move a millimetre; the only thing that changed is the syntax at the call site. If tomorrow you decide
to close an attribute that has been public for two years, with `@property` the code that already wrote
`object.price` keeps compiling and keeps running. With getters, somebody has to go and edit every line.

## The error the slide marks in red
"""),

code("""
# FAILS ON PURPOSE. The setter that calls itself.
import sys


class RecursiveProduct:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.price = value           # missing the two underscores


print("Recursion limit for this session:", sys.getrecursionlimit())
try:
    RecursiveProduct(45)
except RecursionError as e:
    print("RecursionError:", str(e)[:60])
"""),

md("""
`self.price = value` inside the setter enters the setter again, which enters the setter again.

The fix is to write `self.__price = value`, with the two underscores, because that one is an ordinary
attribute and does not go through the property. The rule: **inside the property you touch the
attribute, not the property**.

At least this error raises, and raises loudly. The three that follow do not.

## Encapsulating nothing at all
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Getters and setters for everything, validating nothing.
class Employee:
    def __init__(self, name, salary, tenure):
        self.__name = name
        self.__salary = salary
        self.__tenure = tenure

    def get_name(self):
        return self.__name

    def set_name(self, v):
        self.__name = v

    def get_salary(self):
        return self.__salary

    def set_salary(self, v):
        self.__salary = v

    def get_tenure(self):
        return self.__tenure

    def set_tenure(self, v):
        self.__tenure = v


emp = Employee("Ana", 42000, 36)
emp.set_salary(-8000)
emp.set_tenure(-14)

print("Salary:", emp.get_salary())
print("Tenure:", emp.get_tenure(), "months")
print()
methods = [n for n in vars(Employee) if not n.startswith("__")]
print(f"{len(methods)} access methods, {len([m for m in methods if 'set' in m])} of them writers")
print("Validations in total: 0")
"""),

md("""
An employee on minus eight thousand a month with negative tenure, written through the class's official
interface.

Six access methods, zero validations, and the object is exactly as open as it would be with three
public attributes. The only thing achieved is that everyone now has to type parentheses.

**A setter with no validation is a public attribute with extra steps.** If the attribute takes
anything, leave it public and save the noise. Close it the day you have a rule to defend, and write
the rule inside the setter that same day.

## The property that works behind your back
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A property with a side effect.
class Sensor:
    def __init__(self, temperature):
        self.__temperature = temperature
        self.log = []

    @property
    def temperature(self):
        self.log.append(self.__temperature)      # writes while reading
        return self.__temperature


s = Sensor(21.5)

print(f"Reading: {s.temperature} degrees")
if s.temperature > 20:
    print("Above the threshold")
print(f"Final report: {s.temperature}")

print()
print("Lines in the log:", len(s.log))
print("Log:", s.log)
"""),

md("""
Count how many times `s.temperature` appears in the cell above. Three. The log carries three lines too,
and not one of those three mentions looks like a write.

Here the log is a list in memory and the damage is zero. Swap the list for an `INSERT` in the database
or a request to a server and you have a program making three network round trips because somebody added
a condition and a debug message.

**Reading a property has to look free, because it reads like an attribute.** If there is work behind
it, give it parentheses and call it a method: the parentheses are the sign that something is about to
happen.

## Four ways to encapsulate nothing at all

| | The error | How it looks when it bites |
|---|---|---|
| 01 | A getter and a setter for every attribute | The object is still open and there is twice the code |
| 02 | Validating in the constructor, not in the setter | The object is born valid and rots on the next line |
| 03 | Trusting the single underscore | Somebody built on top of `_bank` and you never heard |
| 04 | Properties with side effects | Three reads, three writes to disk |

All four have one thing in common, which is why they travel together: in all four the code **looks**
encapsulated.
"""),

md("""
---
# Block 3 · Constructors and static members

What `__init__` is responsible for, and which things belong to the whole class rather than to each
object.

## How far the constructor goes

Last week we left it at one sentence: a constructor takes what is essential and leaves the object ready
to use. With block 2 in hand it can be sharpened.

**Its job** is to take what is essential, check it, and leave it assigned on `self`, preferably through
the setter so the rule lives in exactly one place.

**Not its job**: opening files, calling the network, or asking a database anything.

**The test** is a question: can this constructor fail for something that is not the caller's doing? If
the answer is yes, that part belongs in another method. A negative price is the caller's doing. A file
that is not there is not.

## What belongs to the class

Here we pick up `Code022.py` from module 6, whose title is exactly "Class vs Instance attributes".
"""),

code("""
class Person:
    species = "human"                # class attribute

    def __init__(self, name: str, age: int) -> None:
        self.name = name             # instance attributes
        self.age = age


john = Person("John", 36)
print(john.name, john.age, john.species)
print("From the class:", Person.species)

print()
print("vars(john):        ", vars(john))
print("Is species in there?", "species" in vars(john))
"""),

md("""
`john.species` answered `human`, and `species` is not in the object's dictionary.

The mechanism is last week's, the one from the shopping cart. When you ask for an attribute, Python
looks in the object first and, failing that, goes up to the class. Here it fails, goes up, and there it
is.

The difference from the cart is the one that matters: **species really does belong to the concept and
not to the object**. Every person is human, so storing that word a hundred and twenty times would be
waste, and it would also let two people disagree about it.

## Predict before you run

```python
class Person:
    species = "human"

    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person("John", 36)
john.species = "alien"

print(john.species, Person.species)
```

- **A.** `alien alien`, because assigning on the object changes the class's value.
- **B.** `alien human`, because the assignment creates an attribute on the object.
- **C.** `human human`, because a class attribute cannot be shadowed.
- **D.** An error, `species` is not declared in `__init__`.
"""),

code("""
john.species = "alien"

print("john.species:  ", john.species)
print("Person.species:", Person.species)
print()
print("vars(john):", vars(john))
print("Attributes on the object:", len(vars(john)), "<- there were 2")

other = Person("Ana", 20)
print()
print("A brand new person:", other.species)
"""),

md("""
The answer is **B**.

Assigning on the instance never writes to the class. What it does is lay an attribute on top, in the
object's dictionary, and from then on the lookup finds it before going up. The class's value is
untouched and any new person still reads it.

It is the same cell from last week where `b.products = []` "fixed" one cart and left every other one
broken. And it is the same mechanism that makes `self.total += 1` fail to count: the read goes up to
the class, the write stays on the object, always.

Now the other way round.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Changing the class attribute with two objects alive.
Person.species = "animal"

print("john.species:  ", john.species, "<- kept its own")
print("other.species: ", other.species, "<- followed the class")
print("Person.species:", Person.species)
print()
print("Do the two objects agree?", john.species == other.species)
"""),

md("""
Two people of the same class with different species, and no error anywhere along the way.

Reassigning a class attribute changes what every object sees **except** the ones that shadowed it. The
ones that did keep their copy and stop listening. The result is a state that depends on the order of
the lines and that, in a real program, depends on the order in which two functions in two different
files happened to run.

Which is why the course file's advice is sound: **class attributes are for constants**. A value nobody
ever reassigns does not have this problem.

## The second trap in the course code

`Code022.py` defines the class `Person` four times, on lines 8, 44, 92 and 107. It is a teaching file
and redefining the class is its way of adding pieces one at a time.

The second definition keeps the class method and loses the attribute. **The file does not run**: it
stops on its line 62 and the two definitions that follow never execute. This cell reproduces that
second definition as it stands.
"""),

code("""
# FAILS ON PURPOSE. This one comes from the course file, lines 44 to 62.
class SecondPerson:
    @classmethod
    def get_species(cls):
        return cls.species           # species is no longer declared here

    @classmethod
    def zero(cls):
        return cls("", 0)

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


somebody = SecondPerson("John", 36)

try:
    print(somebody.get_species())
except AttributeError as e:
    print("AttributeError:", e)

print()
print("What the class does carry:", [n for n in vars(SecondPerson) if not n.startswith("__")])
print("Does it have species?", hasattr(SecondPerson, "species"))
"""),

md("""
`type object 'SecondPerson' has no attribute 'species'`.

`class Person:` written a second time does not continue the earlier class, it **builds a brand new
class object** and rebinds the name. Anything that does not appear in the new body does not exist on
the new class. The `species` attribute stayed on the first one, which from that line on has no name and
goes to the garbage collector.

It is the redefined function from review 3, one level up. There the second `def` covered the first, and
the calls in between kept working because they came earlier. Here the second `class` covers the first,
and the call that comes after no longer finds what it was looking for.

There is a second detail in that same file. The comment on line 61 says the output is
`<bound method Person.get_species of <class '__main__.Person'>>`, and that is the output of
`my_person.get_species` **without parentheses**. Line 62 does have them. The comment describes a line
that was never written, which is exactly last week's method-without-parentheses mistake, this time
committed inside a comment.

Two ways to leave it running, and both say something.
"""),

code("""
class PersonWithSpecies:
    species = "human"                # declared again on the new class

    @classmethod
    def get_species(cls):
        return cls.species

    def __init__(self, name, age):
        self.name = name
        self.age = age


class InheritingPerson(Person):      # continues the first one instead of replacing it
    @classmethod
    def get_species(cls):
        return cls.species


print("Redeclaring:", PersonWithSpecies("John", 36).get_species())
print("Inheriting: ", InheritingPerson("John", 36).get_species())
print()
print("The inheriting one reads the parent class's current value:", Person.species)
"""),

md("""
The second prints `animal` rather than `human`, because a few cells ago we reassigned `Person.species`
and the child class reads today's value, not the one that was there when it was written.

That line is a preview of week 7. For now, keep the shape: when you want to add something to a class
that already exists, do not write it again, extend it.

## `cls`, and why it is not the same as the class name
"""),

code("""
# The census.py class from the slide. I am giving it a different name on purpose, so as
# not to do to Person what Code022.py did to it three cells ago.
class CensusPerson:
    species = "human"
    census = 0

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        CensusPerson.census += 1     # on the class, deliberately

    @classmethod
    def anonymous(cls) -> "CensusPerson":
        return cls("No name", 0)

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18             # needs neither the object nor the class

    def greet(self) -> None:
        print(f"Hi, I am {self.name}")


ana = CensusPerson("Ana", 20)
nobody = CensusPerson.anonymous()

print("Census:", CensusPerson.census)
nobody.greet()
print()
print("Is 20 an adult?", CensusPerson.is_adult(20))
print("Is 15 an adult?", CensusPerson.is_adult(15))
print()
print("The static method also reads from the object:", ana.is_adult(ana.age))
"""),

md("""
Three kinds of method in the same class, and the difference is the first parameter.

`greet(self)` takes the object. It needs to know who it is talking about.

`anonymous(cls)` takes the class. There is no object yet, because its job is to build one. That is why
these are called **alternative constructors**, or factory methods: when `__init__` can only have one
signature and you need several ways of creating the object, each one gets its own `@classmethod`.

`is_adult(age)` takes nothing at all. It is an ordinary function that lives inside the class because
that is where somebody will go looking for it. `@staticmethod` is how you say that.

And `CensusPerson.census += 1` goes on the class, written with the full name. With `self.census += 1`
every object would walk off with its own counter sitting at one, which was last week's quiz.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The factory that writes the class name instead of cls.
class Vehicle:
    def __init__(self, plates, wheels):
        self.plates = plates
        self.wheels = wheels

    @classmethod
    def unplated(cls):
        return Vehicle("PENDING", 4)         # should say cls(...)


class Truck(Vehicle):
    def __init__(self, plates, wheels=6):
        super().__init__(plates, wheels)


fresh = Truck.unplated()

print("We asked for a truck and got a:", type(fresh).__name__)
print("Wheels:", fresh.wheels)
print("Is it a Truck?", isinstance(fresh, Truck))
print("Is it a Vehicle?", isinstance(fresh, Vehicle))
"""),

md("""
We asked for a truck at the truck counter and got a four-wheeled vehicle.

`cls` is the class **the method was called on**, not the class it was written in. `Truck.unplated()`
passes `Truck`, so `cls("PENDING", 4)` would have built a truck. Typing the name by hand freezes the
factory on the parent class, and every child inherits a method that is useless to it.

None of this raises. The object exists, it has plates, it has wheels, and `isinstance` against
`Vehicle` says `True`. The symptom turns up much later, the day somebody calls a method that only
trucks have.

This is why `cls` exists when the class name is right there, and week 7 picks it up with the full
hierarchy.
"""),

md("""
---
## Four errors from this session

**Trusting the single underscore.** `_bank` reads and writes from outside without a single complaint.
It is an agreement between people and it only works with people who know about it.

**Validating in the constructor and not in the setter.** The object is born correct and turns invalid
on the next line. If there is more than one way to change the attribute, the validation goes where it
changes.

**Writing `self.price` inside the setter for `price`.** The property calls itself until the
`RecursionError`. Inside the property you touch the attribute.

**Putting a method that prints inside an f-string.** You get `None` glued to the text and the lines in
the wrong order. Printing is not returning, and that sentence has been collecting for three weeks now.
"""),

md("""
---
# Exercises

This week's lab is closing a bank account, in pairs. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The three prefixes

Write a class `Student` with three attributes, one public, one with a single underscore and one with
two. From outside, try to read all three under the name written in the class and count how many answer.

Then print `vars` of the object and explain in a comment why the third one looks different.

### Exercise 2 · The method that stays inside

Add to `Student` a private method that computes something intermediate, and a public method that uses
it. Call the private one from outside, catch the `AttributeError`, and then call it under its real name.

Explain in a comment what that tells you about the protection the renaming offers.

### Exercise 3 · Printing is not returning

Write a class with a private method that **prints** and use it inside an f-string. Show the scrambled
output and the `None`.

Then write the version that returns and compare both outputs in the same cell.

### Exercise 4 · The setter that earns its keep

Write `Product` with a private price, `get_price` and `set_price`, and a validation that refuses
negatives. Try seven prices, three of them invalid, and count how many got in.

The constructor has to go through the setter. Prove it by trying to build a negative product.

### Exercise 5 · The same class with a property

Convert exercise 4 to `@property` and `@price.setter`. Run the same seven prices and check in a single
line that it refuses exactly the same ones.

Write in a comment how many lines of the calling code you had to change.

### Exercise 6 · The validation that arrived late

Write a class that validates only in the constructor and leaves the attribute public. Build it
correctly, break it with an assignment, and show that the object went invalid with no error at all.

Fix it with a property and repeat exactly the same two lines.

### Exercise 7 · Class against instance

Write `Course` with a class attribute `SUBJECT_CODE` and two instance attributes. Create three courses,
shadow the class attribute on one of them only, and then reassign the class attribute.

Print what each of the three sees and explain in a comment why they do not agree.

### Exercise 8 · The alternative constructor

Add to `Course` a `@classmethod` called `empty` that builds a course with no students, written with
`cls`. Then write the version with the class name typed by hand, inherit from `Course`, and show that
the two factories return different types.

### Exercise 9 · The lab

Write the class `Account` with a public holder, a private balance and a read-only property that exposes
it, plus the methods `deposit` and `withdraw`.

`withdraw` may not leave the balance negative, and `balance` gets no setter. Hand in a file with the
class and five test operations printed to the console, at least two of which have to be refused.

The criterion is that it should be impossible to leave the account in an invalid state from outside the
class. Prove it: try to break it and show the failed attempt.
"""),

md("""
---
## Three things to take away

**One underscore asks, two take away.** The first is an agreement between people and nobody enforces
it. The second renames the attribute inside the interpreter, and that prevents accidents, not sabotage.

**A property is the setter nobody notices.** It validates like a method and reads like an attribute, so
the day you close a public attribute, not one line of anyone else's code has to change.

**What sits in the class body is shared.** Constants and counters live there; the state of each object
is assigned inside `__init__`. It is the fourth disguise of the same mechanism: the default list from
review 3, the alias from review 4, the shopping cart from week 3, and today's species.

Week 5 goes on with methods that accept several ways of being called, with where each class lives once
the project grows, and with the step from a written brief to a model. Week 6 picks up encapsulation in
earnest, this time with today's property already in hand.

### How to tell whether you encapsulated anything

One question, applied to each closed attribute: **what impossible state does it prevent?** If you have
an answer, the lock is justified. If the answer is "none, but it looks more professional this way",
take it off and leave the attribute public.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Student:
    def __init__(self, name, group, average):
        self.name = name
        self._group = group
        self.__average = average


a = Student("Ana", "COM102-01", 9.2)

answered = 0
for name in ["name", "_group", "__average"]:
    if hasattr(a, name):
        answered += 1
        print(f"  a.{name:<11} -> {getattr(a, name)}")
    else:
        print(f"  a.{name:<11} -> no such name")

print()
print(f"{answered} of 3 answered")
print(vars(a))

# The third one shows up as _Student__average because Python glued the class name
# on while compiling the body. The data is all there; the only thing that changed
# is the name you ask for. The other two were stored exactly as written.
```

### Exercise 2

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def report(self):
        print(f"{self.name}: average {self.__average():.2f}")

    def __average(self):
        return sum(self.marks) / len(self.marks)


a = Student("Ana", [8, 9, 10])
a.report()

try:
    a.__average()
except AttributeError as e:
    print("AttributeError:", e)

print("Under its real name:", a._Student__average())

# The renaming does not protect, it obstructs. Anyone who knows the rule reaches
# the method in one line. What it does prevent is somebody calling it without
# knowing it was internal, and therefore a change of mine breaking their code.
```

### Exercise 3

```python
class Report:
    def __init__(self, title, rows):
        self.title = title
        self.rows = rows

    def broken_header(self):
        print(f"{self.title} ({self.__count()})")

    def __count(self):
        print(f"{len(self.rows)} rows")

    def header(self):
        print(f"{self.title} ({self.__count_text()})")

    def __count_text(self):
        return f"{len(self.rows)} rows"


r = Report("Sales", [1, 2, 3])

r.broken_header()
print()
r.header()

# The first prints "3 rows" and then "Sales (None)". The internal method had to
# run to build the text, printed on its own, and returned None.
# The second prints "Sales (3 rows)" on one line and in the order you read it in
# the code.
```

### Exercise 4

```python
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


CANDIDATES = [10, 0, -1, 99.99, -0.01, 250, -1000]

p = Product(1)
accepted = 0
for value in CANDIDATES:
    try:
        p.set_price(value)
        accepted += 1
    except ValueError:
        pass

print(f"{accepted} of {len(CANDIDATES)} got in")
print("Final price:", p.get_price())

try:
    Product(-5)
except ValueError as e:
    print("The constructor refuses too:", e)
```

### Exercise 5

```python
class PropertyProduct:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


def refused(put):
    out = []
    for value in CANDIDATES:
        try:
            put(value)
        except ValueError:
            out.append(value)
    return out


old = Product(1)
new = PropertyProduct(1)

a = refused(old.set_price)
b = refused(lambda v: setattr(new, "price", v))

print("Getters: ", a)
print("Property:", b)
print("Identical?", a == b)

# Zero lines of the code that reads the price. p.price already worked when the
# attribute was public and it still works now that it goes through the getter.
# That is the entire argument for properties.
```

### Exercise 6

```python
class NaiveCourse:
    def __init__(self, seats):
        if seats <= 0:
            raise ValueError("Seats must be positive")
        self.seats = seats


c = NaiveCourse(30)
c.seats = -5
print("Seats:", c.seats, "· valid?", c.seats > 0)


class Course:
    def __init__(self, seats):
        self.seats = seats

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if value <= 0:
            raise ValueError("Seats must be positive")
        self.__seats = value


c = Course(30)
try:
    c.seats = -5
except ValueError as e:
    print("ValueError:", e)
print("Seats:", c.seats, "· valid?", c.seats > 0)
```

### Exercise 7

```python
class Course:
    SUBJECT_CODE = "COM102"

    def __init__(self, group, seats):
        self.group = group
        self.seats = seats


one = Course("01", 30)
two = Course("02", 28)
three = Course("03", 25)

two.SUBJECT_CODE = "COM102-B"         # only this one shadows it
Course.SUBJECT_CODE = "COM103"        # and now the class value changes

for course in [one, two, three]:
    print(f"Group {course.group}: {course.SUBJECT_CODE}")

print("On the class:", Course.SUBJECT_CODE)
print("vars(two):", vars(two))

# Group 02 does not agree because its assignment created an instance attribute,
# and the lookup finds it before going up to the class. The other two have
# nothing of their own, so they go up and read today's value. Reassigning on the
# class reaches everyone who has not gone independent, and nobody else.
```

### Exercise 8

```python
class Course:
    def __init__(self, group, students):
        self.group = group
        self.students = students

    @classmethod
    def empty(cls, group):
        return cls(group, [])

    @classmethod
    def frozen_empty(cls, group):
        return Course(group, [])      # the name typed by hand


class Workshop(Course):
    pass


good = Workshop.empty("01")
bad = Workshop.frozen_empty("01")

print("With cls:   ", type(good).__name__)
print("With Course:", type(bad).__name__)
print("Is the second a Workshop?", isinstance(bad, Workshop))

# cls is the class the method was called on. Workshop.empty passes Workshop and
# the factory builds a workshop. The other version always builds a Course, so
# everything Workshop adds is left out and nobody gets an error.
```

### Exercise 9

```python
class Account:
    def __init__(self, holder, opening_balance=0):
        self.holder = holder
        self.__balance = 0
        if opening_balance:
            self.deposit(opening_balance)

    @property
    def balance(self):
        return self.__balance         # read-only: there is no setter

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit has to be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("A withdrawal has to be positive")
        if amount > self.__balance:
            raise ValueError(f"Insufficient funds: there is {self.__balance}")
        self.__balance -= amount
        return self.__balance


account = Account("Ana", 1000)

OPERATIONS = [
    ("deposit", 500),
    ("withdraw", 200),
    ("withdraw", 5000),     # more than there is
    ("deposit", -50),       # negative
    ("withdraw", 1300),
]

refused = 0
for action, amount in OPERATIONS:
    try:
        balance = getattr(account, action)(amount)
        print(f"  {action:<10}{amount:>7}  ->  balance {balance}")
    except ValueError as e:
        refused += 1
        print(f"  {action:<10}{amount:>7}  ->  REFUSED: {e}")

print()
print(f"{refused} of {len(OPERATIONS)} refused")
print("Final balance:", account.balance)

# The attempt to break it from outside:
try:
    account.balance = 1000000
except AttributeError as e:
    print("AttributeError:", e)

account.__balance = 1000000           # this does not raise, and does not work either
print("Balance after the attempt:", account.balance)
print("The rubbish left on the object:", vars(account))
```

The last two lines are the part of the exercise that is worth anything.

`account.balance = 1000000` raises, because `balance` is a property with no setter and Python refuses.

`account.__balance = 1000000` does not raise. It creates a new attribute called `__balance`, distinct
from `_Account__balance`, that nobody ever reads. The real balance did not move. It is last week's
phantom attribute, with the added alibi that it looks like you know what you are doing.

Both ways of attacking the account from outside failed, one loudly and one quietly. That is what it
means for the invalid state to be unreachable.
"""),

]

write(OUT / "en" / "w04.ipynb", en)
print("wrote", OUT / "en" / "w04.ipynb")
