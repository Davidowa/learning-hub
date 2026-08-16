"""notebooks/programacion-orientada-a-objetos/en/w07.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w07.en.yaml
Source code:  docs/en/courses/python-course/02 - POO/6th Module/Code020.py
                  (Animal, Mammal, Fish; Person and Student; the single underscore)
              docs/en/courses/python-course/02 - POO/6th Module/Code021.py
                  (multi-level with the chicken, multiple inheritance and ordering)
              docs/en/courses/python-course/02 - POO/6th Module/Code026.py
                  (the Stream hierarchy)

All three files run to the end, checked.

This week pays off week 3's promise: "a child class defines an attribute with
the same name and covers its mother's without noticing". It is in block 2.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 07
## Topic 3 · Core properties

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

What a class receives from its parent, how far the tree should grow, and the underscore that opens the
door to the children.

Last week ended by saying composition is preferred. That does not mean inheritance is wrong: it means it
commits you to more, and you should know to what. This notebook teaches the syntax in ten minutes and
spends the rest on the four places it breaks.

By the end you will be able to:

1. Write a subclass, chain constructors with `super`, and say what happens if you forget.
2. Choose between one underscore and two, now knowing which of the two reaches the children.
3. Explain why two levels are almost always enough and what breaks from the third onwards.
4. Read an `__mro__` and predict which method runs with two parents.
5. Apply the "is a" test and rewrite with composition the relationship that fails it.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Eleven fail on purpose and carry a comment saying so.

Seven of the eleven **raise no exception at all**. Among them is the one week 3 announced: a child class
that defines an attribute with the same name as its mother's and covers it without anyone noticing.
"""),

md("""
---
# Block 1 · Inheritance

A class that starts where another one finished. The easy part is the syntax.
"""),

code("""
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} eats")


class Fish(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def swim(self) -> None:
        print(f"{self.name} swims")


shark = Fish("shark")
shark.eat()
shark.swim()

print()
print("Is a fish an animal?", isinstance(shark, Animal))
print("Does Fish inherit from object?", issubclass(Fish, object))
print("Object state:", vars(shark))
"""),

md("""
`Fish` has `name` and `eat` without writing them. That is the whole of inheritance, in two lines.

`super().__init__(name)` runs the parent's constructor. Without that line `self.name` is never assigned,
and `eat` blows up the first time anyone calls it.

`swim` lives only on `Fish`. The parent does not know about it and should not: if tomorrow `Animal`
learns to swim, every dog and chicken in the program learns too.

## What gets inherited, counted
"""),

code("""
animal_members = {n for n in dir(Animal) if not n.startswith("__")}
fish_members = {n for n in dir(Fish) if not n.startswith("__")}

print("Members of Animal:", sorted(animal_members))
print("Members of Fish:  ", sorted(fish_members))
print()
print("Inherited without writing them:", sorted(fish_members & animal_members))
print("Written on Fish:               ", sorted(fish_members - animal_members))
print()
print("Written in the body of Fish:",
      sorted(n for n in vars(Fish) if not n.startswith("__")))
print("Lookup chain:", [c.__name__ for c in Fish.__mro__])
"""),

md("""
`dir(Fish)` includes `eat` although `vars(Fish)` does not. The difference between the two is exactly
inheritance: `vars` shows what the class wrote, `dir` shows what the class can reach.

The last line is the lookup chain, the **MRO**, which stands for method resolution order. When you ask
for `shark.eat`, Python walks that list left to right and keeps the first one carrying the name. It is
worth getting used to reading it, because in block 3 it is what decides which method runs.

## Predict before you run

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed


d = Dog("Bobby", "collie")
print(d.name)
```

- **A.** `Bobby`, because the parent stored the name.
- **B.** `AttributeError`, the object has no name.
- **C.** `None`, because `name` was left unassigned.
- **D.** `TypeError`, `Dog` is missing arguments.
"""),

code("""
# FAILS ON PURPOSE. The parent constructor that never ran.
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed        # super().__init__(name) is missing


bobby = Dog("Bobby", "collie")

print("Object state:", vars(bobby))
print("Attributes:", len(vars(bobby)), "<- we expected 2")
print()
try:
    print(bobby.name)
except AttributeError as e:
    print("AttributeError:", e)

print()
try:
    bobby.eat()
except AttributeError as e:
    print("And eat does not work either:", e)
"""),

md("""
The answer is **B**.

Defining `__init__` on the subclass **replaces** the parent's, it does not add to it. It is the same
mechanism as last week's second `def`, applied along the inheritance chain: `Dog.__init__` covers
`Animal.__init__`, and if nobody calls it, the parent's never runs.

Notice the order in which you find out. The object was built without complaint, carrying a single
attribute. The error turns up later, on the first line that reads `name`, which may be in another file.

That is error 03 on the slide and it is the most common one in the whole unit.
"""),

code("""
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)        # the parent's part first
        self.breed = breed            # then its own

    def bark(self):
        print(f"{self.name} ({self.breed}) barks")


bobby = Dog("Bobby", "collie")
bobby.eat()
bobby.bark()

print()
print("Object state:", vars(bobby))
print("Attributes:", len(vars(bobby)))
"""),

md("""
Two attributes, one from each constructor.

The order matters and there is a reason: `super().__init__` goes first because your own part may depend
on the inherited one, and hardly ever the other way round.

## The parent constructor that calls a child method
"""),

code("""
# FAILS ON PURPOSE. The parent uses something the child has not assigned yet.
class Employee:
    def __init__(self, name):
        self.name = name
        print("  record:", self.record())     # the parent calls the method

    def record(self):
        return self.name


class SalesRep(Employee):
    def __init__(self, name, region):
        super().__init__(name)                # record() runs right here
        self.region = region                  # and region does not exist yet

    def record(self):
        return f"{self.name} ({self.region})"


print("An ordinary employee:")
Employee("Ana")

print()
print("A sales rep:")
try:
    SalesRep("Luis", "North")
except AttributeError as e:
    print("  AttributeError:", e)
"""),

md("""
The parent called `record`, and the one that ran was the child's, because the object was already a
`SalesRep` before the first constructor started.

That is the part that takes seeing: **an object's type is decided when it is built, not halfway
through**. From the first line of `Employee.__init__`, `self` is already a `SalesRep`, so any method the
parent calls will be the overridden version, working on a half-built object.

The rule that falls out: **a constructor does not call methods that can be overridden**. If the parent
needs the result, it should take it as a parameter, or the work should happen afterwards in a separate
method, as in week 3 with the constructor that opened files.

## `type` is not `isinstance`
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A filter written with type instead of isinstance.
animals = [Animal("generic"), Fish("shark"), Dog("Bobby", "collie")]

by_type = [a for a in animals if type(a) is Animal]
by_isinstance = [a for a in animals if isinstance(a, Animal)]

print("With type is Animal:      ", len(by_type), "of", len(animals))
print("With isinstance(a, Animal):", len(by_isinstance), "of", len(animals))
print()
for a in animals:
    same = "yes" if type(a) is Animal else "no"
    kind = "yes" if isinstance(a, Animal) else "no"
    print(f"  {type(a).__name__:<8}type: {same:<4}isinstance: {kind}")
"""),

md("""
One against three. The `type` filter left out the fish and the dog, which are animals.

`type(x) is Animal` asks whether the object is **exactly** that class. `isinstance(x, Animal)` asks
whether it is that class or anything inheriting from it, which is almost always what you meant.

It does not raise, it does not warn, and it produces the wrong count. In a program with hierarchies, a
`type ==` is nearly always a bug waiting for somebody to add the first subclass.
"""),

md("""
---
# Block 2 · The protected modifier

One underscore opens the door to the children. Two close it even to them, and that surprises almost
everyone.

Here, at last, the single underscore has a technical use rather than just an agreement. It still
prevents nothing from outside, but inside a hierarchy it says something precise: **this is mine and my
children's**.
"""),

code("""
class Person:
    def __init__(self, name: str) -> None:
        self._name = name               # protected: mine and my children's
        self.__key = "secret"           # private: mine only

    def introduce(self):
        print(f"I am {self._name} and my key starts with {self.__key[0]}")


class Student(Person):
    def greet(self):
        print(f"Hi, I am {self._name}")          # the protected one comes down


ana = Student("Ana")
ana.introduce()
ana.greet()

print()
print("Object state:", vars(ana))
print("From outside, the protected one too:", ana._name)
"""),

code("""
# FAILS ON PURPOSE. The parent's private does not come down under that name.
class NosyStudent(Person):
    def snoop(self):
        return self.__key               # translates to self._NosyStudent__key


nosy = NosyStudent("Luis")

try:
    nosy.snoop()
except AttributeError as e:
    print("AttributeError:", e)

print()
print("What the object does hold:", list(vars(nosy)))
print("Under the mother's name:", nosy._Person__key)
"""),

md("""
The message says `'NosyStudent' object has no attribute '_NosyStudent__key'`, and the whole explanation
is right there.

The renaming uses the name of **the class where the line was written**, not the object's. `self.__key`
inside `Person` translates to `_Person__key`; the same expression written inside `NosyStudent`
translates to `_NosyStudent__key`, which never existed.

| Member | In the class | In the subclass | From outside |
|---|---|---|---|
| `age` | Yes | Yes | Yes |
| `_name` | Yes | Yes | Yes, though you should not |
| `__key` | Yes | No | No, not under that name |
| `eat()` | Yes | Yes | Yes |
| `__say()` | Yes | No | No, not under that name |

## The collision week 3 announced

Back in week 3 I wrote that the renaming prevents "a child class defining an attribute with the same
name and covering its mother's without noticing". Here is that cell.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The child covers its mother's attribute.
class Session:
    def __init__(self, user):
        self._user = user
        self._state = "open"            # the session's state

    def close(self):
        self._state = "closed"

    def is_open(self):
        return self._state == "open"


class ExamSession(Session):
    def __init__(self, user, exam):
        super().__init__(user)
        self.exam = exam
        self._state = "not started"     # the exam's state, same name

    def submit(self):
        self._state = "submitted"


s = ExamSession("Ana", "COM102-P1")
print("Object state:", vars(s))
print("Attributes:", len(vars(s)), "<- two states in a single key")
print()
print("Is the session open?", s.is_open(), "<- it was just created")
s.submit()
print("After submitting the exam:")
print("  _state:", s._state)
print("  is the session open?", s.is_open())
s.close()
print("After closing the session, the exam says:", s._state)
"""),

md("""
A single `_state` key for two different ideas, and the two take turns covering each other.

The session was born closed because the child's constructor overwrote the parent's value. Submitting the
exam did not close the session and yet left it "not open". Closing the session wiped the exam's state.

Nobody wrote a bug. Both classes are correct on their own, and the collision happened because both chose
the same word for different things. The bigger the tree, the likelier it is, and the symptom never
points at inheritance.

With two underscores this does not happen.
"""),

code("""
class SafeSession:
    def __init__(self, user):
        self.__state = "open"

    def close(self):
        self.__state = "closed"

    def is_open(self):
        return self.__state == "open"


class SafeExam(SafeSession):
    def __init__(self, user, exam):
        super().__init__(user)
        self.exam = exam
        self.__state = "not started"        # the same name, a different class

    def submit(self):
        self.__state = "submitted"

    def exam_state(self):
        return self.__state


e = SafeExam("Ana", "COM102-P1")
print("Object state:", vars(e))
print("Attributes:", len(vars(e)), "<- two states, two keys")
print()
print("Is the session open?", e.is_open())
e.submit()
print("Exam:", e.exam_state(), "· session open:", e.is_open())
e.close()
print("Exam:", e.exam_state(), "· session open:", e.is_open())
"""),

md("""
Two keys, `_SafeSession__state` and `_SafeExam__state`, and each class rules its own.

**That is the double underscore's real use**, not security. It stops a long hierarchy from stepping on
its own names, which is a far more frequent accident than an attack.

The rule that falls out of the two cells:

- **One underscore** when you want the children to use it. It is part of the contract downwards.
- **Two underscores** when the data is your business and nobody else's, not even your children's.
- **Nothing** when it is part of the contract outwards.
"""),

md("""
---
# Block 3 · Class hierarchy

Every new level is one more file to open in order to understand a single call. The tree is paid for in
reading.

`Code026.py` in module 6 builds the healthy hierarchy: one parent with what is shared and three siblings
with what changes.
"""),

code("""
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self) -> None:
        if self.opened:
            raise InvalidOperationError("the stream was already open")
        self.opened = True

    def close(self) -> None:
        if not self.opened:
            raise InvalidOperationError("the stream was already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("  reading from a file")


class NetworkStream(Stream):
    def read(self):
        print("  reading from the network")


class MemoryStream(Stream):
    def read(self):
        print("  reading from memory")


for stream in [FileStream(), NetworkStream(), MemoryStream()]:
    print(type(stream).__name__)
    stream.open()
    stream.read()
    stream.close()

print()
print("Levels in the tree:", len(FileStream.__mro__) - 1,
      "->", [c.__name__ for c in FileStream.__mro__])
"""),

md("""
Three siblings hanging off the same parent, two levels counting `object`, and understanding any call
means reading two classes.

`open` and `close` were written once. `read` was written three times because it genuinely differs
between one child and another, which is exactly what justifies three classes.

**The healthy-hierarchy rule: siblings hang off the same parent, none hangs off another sibling.**

## The class attribute, now shared among cousins
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A list declared on the parent.
class LoggingStream(Stream):
    log = []                         # in the class body

    def record(self, message):
        self.log.append(f"{type(self).__name__}: {message}")


class FromFile(LoggingStream):
    pass


class FromNetwork(LoggingStream):
    pass


from_file = FromFile()
from_net = FromNetwork()

from_file.record("opened a file")
from_net.record("opened a socket")

print("File log:   ", from_file.log)
print("Network log:", from_net.log)
print()
print("Is it the same list?", from_file.log is from_net.log is LoggingStream.log)
print("vars(from_file):", vars(from_file))
print("Objects with a log of their own:",
      sum(1 for o in [from_file, from_net] if "log" in vars(o)), "of 2")
"""),

md("""
Two different classes, two different objects, one single list.

It is week 3's shopping cart, now spread across a whole branch of the tree. Attribute lookup walks up the
`__mro__` until it finds `log`, finds it on `LoggingStream`, and returns it; the `append` modifies that
one list.

What inheritance adds to the problem is reach. In week 3 the objects of one class shared it; here it is
shared by the objects of every class in the branch, including the ones somebody writes next year. The
fix is the usual one: `self.log = []` inside `__init__`, and in a hierarchy that means inside the
`__init__` that actually runs, chained with `super`.

## What happens from the third level onwards
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The chain that teaches a chicken to fly.
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} flies")


class Chicken(Bird):
    def __init__(self, name):
        super().__init__(name)


chicken = Chicken("Lola")
chicken.eat()
chicken.fly()            # nobody wrote it and there it is

print()
print("Lookup chain:", [c.__name__ for c in Chicken.__mro__])
print("Levels up to object:", len(Chicken.__mro__) - 1)
print("Can the chicken fly?", hasattr(chicken, "fly"))

owner = next(c for c in Chicken.__mro__ if "fly" in vars(c))
print("fly is written on:", owner.__name__,
      "· step in the chain:", Chicken.__mro__.index(owner))
"""),

md("""
A chicken that flies, with not one line saying so.

`Chicken` did not write `fly`. It got it from `Bird`, which wrote it because most birds fly. The chain
made true a claim nobody wanted to make.

And notice the reading cost. To understand what `chicken.fly()` does you have to climb up to `Bird`,
skipping `Chicken`. One more level and you climb two. That is error 01 on the slide: **understanding one
call means opening four files, and along the way the chicken learns to fly.**

The fix is not to give `Chicken` a `fly` that prints "I cannot". It is that `Bird` had no business
promising flight: flying belongs to some birds, not to birds. That calls for a separate `Flyer` class,
or better, composition.

## Two parents, and the ordering that decides in silence
"""),

code("""
class GreetingPerson:
    def greet(self):
        print("Hello, I am a person")


class Worker:
    def greet(self):
        print("Hello, I am an employee")


class Manager(Worker, GreetingPerson):
    pass


class ReversedManager(GreetingPerson, Worker):
    pass


Manager().greet()
ReversedManager().greet()

print()
print("Manager.__mro__:        ", [c.__name__ for c in Manager.__mro__])
print("ReversedManager.__mro__:", [c.__name__ for c in ReversedManager.__mro__])
"""),

md("""
Two classes identical apart from the order in the parentheses, and two different behaviours.

Python looks the method up by walking the `__mro__` left to right and keeps the first one carrying it.
`Worker` comes first in the first class, so its `greet` wins.

Now the uncomfortable part.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Somebody reorders the parents in a refactor.
class Manager(GreetingPerson, Worker):        # it used to say (Worker, GreetingPerson)
    pass


print("The same calling code as always:")
Manager().greet()
print()
print("No error, no warning, and not one line of difference at the call site.")
print("The only thing that changed is in the class declaration:")
print("  ", [c.__name__ for c in Manager.__mro__])
"""),

md("""
The program changed behaviour and nobody touched a line of the code that uses it.

That is error 04 on the slide, and the real risk is not somebody reordering parents on purpose. It is
that the order never gets read: `class Manager(Worker, Person)` looks like a list of labels rather than
a precedence decision, and whoever edits it six months later will not know they were deciding anything.

When two parents bring the same method, the signal is that one of the two was not a parent. With
composition the same case is written unambiguously, because the call says which is which:
`self.worker.greet()` or `self.person.greet()`.

## And `super()` does not call both either
"""),

code("""
# FAILS ON PURPOSE. super() with two parents only reaches the first.
class Staff:
    def __init__(self, number):
        self.number = number


class Human:
    def __init__(self, name):
        self.name = name


class ManagerWithSuper(Staff, Human):
    def __init__(self, number, name):
        super().__init__(number)          # only Staff.__init__ runs


m = ManagerWithSuper(1, "Ana")
print("Object state:", vars(m))
print("Attributes:", len(vars(m)), "<- we expected 2")

try:
    print(m.name)
except AttributeError as e:
    print("AttributeError:", e)

print()


class ExplicitManager(Staff, Human):
    def __init__(self, number, name):
        Staff.__init__(self, number)
        Human.__init__(self, name)


m = ExplicitManager(1, "Ana")
print("Calling both by hand:", vars(m))
"""),

md("""
`super()` does not mean "the parents". It means **the next one in the chain**, and the chain here is
`ManagerWithSuper -> Staff -> Human -> object`. Since `Staff.__init__` does not call `super()`, the chain
stops there and `Human.__init__` never runs.

The way out that `Code021.py` uses is calling both constructors by name, which works and reads. The
other way out is for **every** class in the chain to call `super().__init__()`, which is called
cooperative inheritance and forces the signatures to line up.

Both are extra work that composition does not ask for. It is one more reason multiple inheritance
hardly ever pays.

## Four ways to abuse inheritance

| | The error | How it looks |
|---|---|---|
| 01 | A four-level tree | Four files to understand one call, and the chicken flies |
| 02 | Inheriting to avoid repeating code | The relationship was one of use, and a parameter did the same job |
| 03 | Forgetting `super().__init__` | The object is born incomplete and blows up on the first line that uses it |
| 04 | Two parents with the same method | The order of the list decides in silence |
"""),

md("""
---
# Block 4 · Inherit or compose

The test fits in a sentence said out loud: **the child is a particular case of the parent**.

If it sounds true without explanation, inheritance holds. If it needs a "well, sort of", what you had was
composition.

| Sentence | Does it hold? | What it was |
|---|---|---|
| A fish is an animal | Yes | Inheritance |
| An open file is a data stream | Yes | Inheritance |
| A cart is a list | No | The cart **has** a list |
| An order is a customer | No | The order **has** a customer |
| A chicken is a bird that flies | With caveats | The "that flies" was the problem |

## The sentence that sounds true and still fails

A square is a rectangle. In geometry that is true without a single caveat, and inheritance breaks anyway.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A square that inherits from a rectangle.
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value):
        self._width = value
        self._height = value        # a square has to stay a square


def stretch_and_measure(rect):
    \"\"\"Written for rectangles, long before Square existed.\"\"\"
    rect.width = 10
    return rect.area


print("With a 3x4 rectangle:", stretch_and_measure(Rectangle(3, 4)), "-> 10 * 4")
print("With a square of side 4:", stretch_and_measure(Square(4)), "-> 10 * 4?")
print()
print("Is a square a rectangle?", issubclass(Square, Rectangle))
print("Does the function know which one it has? No.")
"""),

md("""
Forty against a hundred, from the same function and without a single error.

`stretch_and_measure` was written with a promise in mind: changing the width does not change the height.
It is a promise `Rectangle` keeps and one `Square` cannot keep without ceasing to be a square.

Here is the uncomfortable part. The "is a" sentence is true, geometry is on your side, and the subclass
still breaks code written for the mother. The "is a" test is necessary and it is not sufficient.

The full version is called the **Liskov substitution principle** and it asks for something stricter:
anywhere the mother works, it has to keep working if you hand it a child. When the child takes away
freedom the mother had, it no longer substitutes.

The way out: if the square cannot make the same promise, it is not a subclass of the mutable rectangle.
Either they are two separate classes, or the rectangle is immutable and `with_width(10)` returns a new
one, which is week 5's `__add__` lesson.

## The same relationship, written both ways
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A cart that inherits from list.
class InheritingCart(list):
    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.append(sku)


c = InheritingCart()
c.add("X1")
print("Through the front door:", c)

c.append("unvalidated junk")         # inherited from list, no validation
c.extend([1, 2, 3])
c += ["more junk"]

print("Through the other doors:", c)
print("Products:", len(c))
print()
list_methods = [n for n in dir(list) if not n.startswith("_")]
MUTATORS = {"append", "extend", "insert", "pop", "remove", "clear", "sort", "reverse"}

print("Public methods the cart inherited by accident:", len(list_methods))
print("  ", list_methods)
print()
print("Of those, the ones that can change the contents:",
      len(MUTATORS & set(list_methods)))
print("Of those, the ones that go through the validation:",
      len(MUTATORS & set(vars(InheritingCart))))
"""),

md("""
A cart with eleven ways in, and only one of them checks the SKU.

Inheriting from `list` handed the cart `append`, `extend`, `insert`, `__iadd__` and everything else, and
none of those knows about your rule. The validation is not protecting anything: it is decorating one of
the eleven entrances.

On top of that, "a cart is a list" is false. A cart **has** a list, and it also has an owner, a date and
a total. Inheriting from `list` forces it to be a list forever.
"""),

code("""
class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.__products = []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return iter(self.__products)

    def __repr__(self):
        return f"Cart({self.owner!r}, {list(self.__products)})"


c = Cart("Ana")
c.add("X1")

for attempt in ["append", "extend", "insert"]:
    print(f"c.{attempt} exists:", hasattr(c, attempt))

try:
    c.add("junk")
except ValueError as e:
    print()
    print("ValueError:", e)

print("Cart:", c, "· products:", len(c))
print()
print("Ways in:", len([n for n in vars(Cart) if n == "add"]))
"""),

md("""
One way in, and the rule guards it.

Notice what was not lost: `len(c)` works, the `for` works, and the cart prints properly. Week 5's magic
methods give it a list's syntax without inheriting from `list`, which is the difference between
**looking like** and **being**.

## When inheritance does win
"""),

code("""
class InventoryError(Exception):
    pass


class OutOfStock(InventoryError):
    def __init__(self, sku, wanted, available):
        super().__init__(f"{sku}: you asked for {wanted} and there are {available}")
        self.sku = sku
        self.missing = wanted - available


class InvalidSku(InventoryError):
    pass


for error in [OutOfStock("X1", 10, 3), InvalidSku("Z9 does not start with X")]:
    try:
        raise error
    except InventoryError as e:
        print(f"{type(e).__name__:<14}{e}")

print()
try:
    raise OutOfStock("X2", 5, 1)
except InventoryError as e:
    print("Caught by the parent:", e)
    print("And with the child's data:", e.sku, "missing", e.missing)
"""),

md("""
Here the sentence holds on its own: **an out-of-stock error is an inventory error**.

And inheritance does a job composition could not: `except InventoryError` catches both children and any
added tomorrow, without touching the `except`. That is what you buy when you inherit, and it is why
exception hierarchies are the case hardly anyone argues about.

You saw it from the other side in review 5, when `except Exception` caught all seven exceptions in that
notebook. That hierarchy is the same one, and now you are writing it.

In week 11 this comes back with custom exceptions in earnest.
"""),

md("""
---
## Four errors from this session

**Forgetting `super().__init__`.** The object is born without the parent's attributes. The error turns up
later, on the first line that uses them, which may be in another file.

**Using `type(x) == Class` in a filter.** It leaves out every subclass, without a word, and the count
comes out wrong.

**Reusing a protected name in the child.** Two different ideas in one key, and the two classes cover each
other by turns. With two underscores it does not happen.

**Inheriting from `list` or `dict` to reuse.** You inherit ten ways in and the validation only guards
one.
"""),

md("""
---
# Exercises

This week's lab is tidying a transport hierarchy into two levels at most. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · The minimal subclass

Write `Vehicle` with plates and a `describe` method. Then write `Motorcycle` inheriting from it and
adding the number of cylinders.

Print `vars` of the object and the `__mro__` chain, and say which constructor each thing came from.

### Exercise 2 · The omission

Write the same `Motorcycle` without calling `super().__init__`. Show that the object builds without
complaint, then catch the `AttributeError` from the first line that reads the plates.

### Exercise 3 · type against isinstance

Build a list with three objects from three classes in your hierarchy. Filter it with
`type(x) is Vehicle` and with `isinstance(x, Vehicle)` and compare the two counts.

Write in a comment when you would use `type` on purpose.

### Exercise 4 · Protected against private

Write a class with one single-underscore attribute and one double. From a subclass, try to read both.
Catch the second one's error and print `vars` to show both real names.

### Exercise 5 · The collision

Write a mother class with `_state` and a child that also uses `_state` for something else. Show with
three calls that the two cover each other.

Fix it two ways: with two underscores, and by renaming one of them. Say which you prefer.

### Exercise 6 · The healthy hierarchy

Write a parent `Document` with `open` and `close`, and three children that only change `read`. Walk them
in a loop and check the loop does not know which class each one is.

Count with `__mro__` how many levels your tree has.

### Exercise 7 · The ordering that decides

Write two classes with a method of the same name and a third inheriting from both. Print the `__mro__`,
run the method, then swap the order of the parents and run it again.

Explain in a comment why this is dangerous on a project with several people.

### Exercise 8 · The "is a" test

Write `Cart(list)` with a validating method, and show with three different calls that the validation can
be walked around. Then rewrite it by composition with `__len__` and `__iter__`.

Say both sentences out loud, the "is a" and the "has a", and note which one sounds true.

### Exercise 9 · The lab

You are handed seven loose classes from a transport system. Arrange them into a hierarchy of at most two
levels, justifying each parent in one line.

Two levels at most, no multiple inheritance, and every repeated method moves up to the parent. Hand in
the hierarchy diagram and a `.py` file with the classes and their chained constructors.

The criterion is that every relationship passes the "is a" test, said out loud to your partner.
"""),

md("""
---
## Three things to take away

**The child receives everything except the private.** Public and protected members are inherited; the
double underscore changes name and stays upstairs. And that renaming, which in week 4 looked like a loose
padlock, turns out here to be what stops two classes in the same branch from stepping on a name.

**Two levels are almost always enough.** Every extra level is one more file to open in order to
understand a single call, and along the way promises appear that nobody wanted to make, like the chicken
that flies.

**Inheriting commits, composing lends.** If the type sentence does not sound true, the relationship was
one of use and a parameter settles it. Where inheritance does win is exception hierarchies, because an
`except` on the parent catches every child.

Week 8 closes topic 3 with polymorphism, overriding, abstract classes and interfaces, plus the first
midterm. The loop that walks the three `Stream` objects in this notebook without knowing which class each
one is already is polymorphism; what is missing is the contract that forces the children to implement
`read`.
"""),

md("""
---
# Solutions

### Exercise 1

```python
class Vehicle:
    def __init__(self, plates):
        self.plates = plates

    def describe(self):
        print(f"{type(self).__name__} with plates {self.plates}")


class Motorcycle(Vehicle):
    def __init__(self, plates, cylinders):
        super().__init__(plates)
        self.cylinders = cylinders


m = Motorcycle("ABC-123", 2)
m.describe()
print(vars(m))
print([c.__name__ for c in Motorcycle.__mro__])

# plates came from Vehicle's constructor, called with super. cylinders came from
# Motorcycle's. describe was inherited and does not show in vars, because methods
# live on the class rather than on the object.
```

### Exercise 2

```python
class BrokenMotorcycle(Vehicle):
    def __init__(self, plates, cylinders):
        self.cylinders = cylinders


m = BrokenMotorcycle("ABC-123", 2)
print("It built without complaint:", vars(m))

try:
    m.describe()
except AttributeError as e:
    print("AttributeError:", e)
```

### Exercise 3

```python
class Truck(Vehicle):
    pass


fleet = [Vehicle("A"), Motorcycle("B", 2), Truck("C")]

print("type:      ", len([v for v in fleet if type(v) is Vehicle]))
print("isinstance:", len([v for v in fleet if isinstance(v, Vehicle)]))

# I would use type on purpose to tell the base case apart from its
# specialisations, for instance when serialising: a plain Vehicle is stored
# differently from a Motorcycle. Outside of that, isinstance is what you mean.
```

### Exercise 4

```python
class Account:
    def __init__(self, holder):
        self._holder = holder
        self.__pin = "1234"


class SavingsAccount(Account):
    def read_protected(self):
        return self._holder

    def read_private(self):
        return self.__pin


a = SavingsAccount("Ana")
print("Protected:", a.read_protected())

try:
    a.read_private()
except AttributeError as e:
    print("AttributeError:", e)

print(vars(a))
print("Under its real name:", a._Account__pin)
```

### Exercise 5

```python
class Task:
    def __init__(self, title):
        self.title = title
        self._state = "pending"

    def finish(self):
        self._state = "done"

    def is_pending(self):
        return self._state == "pending"


class ReviewedTask(Task):
    def __init__(self, title, reviewer):
        super().__init__(title)
        self.reviewer = reviewer
        self._state = "unreviewed"        # another idea, same name

    def approve(self):
        self._state = "approved"


t = ReviewedTask("Assignment 1", "Ana")
print("Pending on creation?", t.is_pending())
t.approve()
print("After approving, pending?", t.is_pending())
t.finish()
print("After finishing, the review state says:", t._state)
print(vars(t))


# Fix 1: two underscores in each class.
# Fix 2: different names, _state and _review.
class ClearTask(Task):
    def __init__(self, title, reviewer):
        super().__init__(title)
        self.reviewer = reviewer
        self._review = "unreviewed"

    def approve(self):
        self._review = "approved"


t = ClearTask("Assignment 1", "Ana")
t.approve()
print(vars(t))
print("Pending?", t.is_pending())

# I prefer the second. The double underscore covers the symptom and leaves two
# different things sharing a name, which is the real problem. Giving them
# different names forces you to decide what each one is, and that reads.
```

### Exercise 6

```python
class Document:
    def __init__(self):
        self.opened = False

    def open(self):
        self.opened = True

    def close(self):
        self.opened = False


class PdfDocument(Document):
    def read(self):
        print("  reading a PDF")


class WordDocument(Document):
    def read(self):
        print("  reading a Word file")


class TextDocument(Document):
    def read(self):
        print("  reading plain text")


for doc in [PdfDocument(), WordDocument(), TextDocument()]:
    doc.open()
    doc.read()
    doc.close()

print("Levels:", len(PdfDocument.__mro__) - 1)
print([c.__name__ for c in PdfDocument.__mro__])
```

### Exercise 7

```python
class Recorder:
    def process(self):
        print("writing to the log")


class Validator:
    def process(self):
        print("validating the data")


class Pipeline(Recorder, Validator):
    pass


print([c.__name__ for c in Pipeline.__mro__])
Pipeline().process()


class Pipeline(Validator, Recorder):
    pass


print([c.__name__ for c in Pipeline.__mro__])
Pipeline().process()

# It is dangerous because the parent list reads as an enumeration rather than a
# decision. Nobody alphabetises a list knowing they are changing the program's
# behaviour, and yet that is what happens.
```

### Exercise 8

```python
class InheritingCart(list):
    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.append(sku)


c = InheritingCart()
c.add("X1")
c.append("junk")
c.insert(0, "more junk")
c += [42]
print(c, "->", len(c), "items and a single validation")


class Cart:
    def __init__(self):
        self.__products = []

    def add(self, sku):
        if not sku.startswith("X"):
            raise ValueError("a SKU has to start with X")
        self.__products.append(sku)

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return iter(self.__products)


c = Cart()
c.add("X1")
print(hasattr(c, "append"), len(c), list(c))

# "A cart is a list" sounds false: a cart has an owner, a date and a total, and a
# list has none of those. "A cart has a list" sounds true.
```

### Exercise 9

```python
class Vehicle:
    def __init__(self, plates: str, capacity: int) -> None:
        self.plates = plates
        self.capacity = capacity

    def describe(self) -> str:
        return f"{type(self).__name__} {self.plates}, capacity {self.capacity}"


class Car(Vehicle):
    def __init__(self, plates, capacity, doors):
        super().__init__(plates, capacity)
        self.doors = doors


class Bus(Vehicle):
    def __init__(self, plates, capacity, route):
        super().__init__(plates, capacity)
        self.route = route


class Truck(Vehicle):
    def __init__(self, plates, capacity, tonnes):
        super().__init__(plates, capacity)
        self.tonnes = tonnes


class Motorcycle(Vehicle):
    def __init__(self, plates, capacity, cylinders):
        super().__init__(plates, capacity)
        self.cylinders = cylinders


fleet = [
    Car("AAA-111", 5, 4),
    Bus("BBB-222", 40, "Centre-North"),
    Truck("CCC-333", 2, 12.5),
    Motorcycle("DDD-444", 2, 2),
]

for v in fleet:
    print(v.describe())

print()
print("Levels in the tree:", max(len(type(v).__mro__) for v in fleet) - 1)
```

The justifications, one line each.

**`Vehicle` is the parent** because all four have plates and capacity, and `describe` would be written
identically four times.

**All four hang directly off `Vehicle`** and none off another sibling. A bus is not a large car: it is a
vehicle with a route.

**There is no `FreightVehicle` class between `Vehicle` and `Truck`.** With a single child, that level
gathers nothing and only adds a file to open.

**None inherits from two parents.** If an amphibious vehicle turns up tomorrow it will be tempting; the
way out is taking a marine engine in the constructor rather than hanging off a second branch.
"""),

]

write(OUT / "en" / "w07.ipynb", en)
print("wrote", OUT / "en" / "w07.ipynb")
