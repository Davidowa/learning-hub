"""notebooks/programacion-orientada-a-objetos/en/w01.3.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w01.3.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/3rd Module/
              Code010.py, Code011.py, Exercise002.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Review 3 of 5
## Module 3 · Functions

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Giving a piece of work a name. Parameters, return values and where each variable lives.

This is the heaviest of the five reviews. In three weeks you will write your first class, and a class
is nothing more than functions living together and sharing data. Everything called function,
parameter and scope here will be called method, argument and `self` there, and it will work the same
way.

By the end of this notebook you will be able to:

1. Define a function with `def`, and tell defining it from calling it.
2. Separate a parameter from an argument, and use default values without falling into the list trap.
3. Return a value with `return`, and explain what a function without one hands back.
4. Explain the scope of a variable, and why `NameError` and `UnboundLocalError` appear exactly where
   they appear.
5. Write FizzBuzz in full and say why the order of its conditions is not negotiable.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Ten fail on purpose and carry a comment saying so.

Watch which of those ten **raise nothing at all**. Those are the dangerous ones: the program keeps
running, hands back a believable result, and is wrong.
"""),

md("""
---
# Block 1 · Defining and calling

A function is a named block of code that only runs when something calls it.

It earns its place three ways, and they are worth keeping separate in your head. So you do not repeat
yourself, because the code is written once and used many times. So you can test one part without
running the whole program. And so what you wrote reads as a list of intentions instead of a wall of
instructions.

**The naming rule: a verb and a noun.** `calculate_average`, `read_file`, `is_even`. If you cannot
name it that way, it probably does more than one thing and wants splitting.
"""),

code("""
def greet():
    print("Hello from a function")


greet()                        # Hello from a function


def greet_by_name(name):
    print(f"Hello, {name}")


greet_by_name("Ana")           # Hello, Ana
greet_by_name("Beto")          # same function, different argument
"""),

md("""
The colon and the indent are what say which lines belong to the function. Everything indented under
the `def` is its body, and the first line back at the margin is already outside.

## Defining is not calling

The `def` only creates the function and files it under that name. Nothing in the body runs until
something calls it.
"""),

code("""
# FAILS ON PURPOSE, and this is one of the ones that raise nothing.
def calculate_tax(amount):
    print(f"Tax: {amount * 0.16:.2f}")


print("The program finished without printing a single tax.")
"""),

md("""
No error, no warning, no line of output. Python read the `def`, stored the function and moved on.

That silence is the problem. A script that defines twenty functions and calls eighteen runs clean and
delivers two things short.
"""),

code("""
calculate_tax(1500)            # now the body runs
"""),

code("""
# FAILS ON PURPOSE, and raises nothing either. Without parentheses it is not a call.
print(calculate_tax)
print(type(calculate_tax))
print()
print("Is that the same as calling it?", calculate_tax is calculate_tax)
"""),

md("""
Without parentheses, the name is only the name. Python prints the reference to the function, memory
address and all, and runs nothing.

That matters more than it looks: **a function is a value**, like a number or a string. It can be
stored in a variable, put in a list and passed to another function as an argument. That is where the
parentheses stop being decoration and become the difference between handing over the recipe and
handing over the dish.
"""),

code("""
another_name = calculate_tax       # no parentheses: stores the function
another_name(2000)                 # with parentheses: runs it

operations = [greet, calculate_tax]
print("Stored in a list:", len(operations))
operations[0]()                    # calls greet from the list
"""),

md("""
## Four words that get confused

| Term | What it is | Where it appears | Example |
|---|---|---|---|
| Parameter | The slot you declare | In the `def` | `def greet_by_name(name)` |
| Argument | The value you pass | In the call | `greet_by_name("Ana")` |
| Return value | What it hands back | In the `return` | `return total / n` |
| Call | The order to run it | Wherever you use it | `greet_by_name("Ana")` |

The first two are the pair people mix up. The parameter is written once, at definition. The argument
changes with every call.
"""),

code("""
def describe(product, quantity):        # product and quantity are parameters
    print(f"{quantity} x {product}")


describe("coffee", 3)                   # "coffee" and 3 are arguments
describe("filter", 12)                  # other arguments, same parameters
describe(quantity=5, product="mug")     # by name, in any order
"""),

md("""
The last call uses **keyword arguments**. Writing the parameter name at the call site frees the order
and lets the line read on its own.

Compare `increment(2, 1)` with `increment(number=2, by=1)`. The first one forces you to go and find
the definition to know which is which.

## Default values

A parameter with a default value becomes optional. If the call does not bring it, the value written
in the `def` is used.
"""),

code("""
def introduce(first, last, greeting="Hello"):
    print(f"{greeting}, {first} {last}")


introduce("Ana", "Lopez")                     # uses the default
introduce("Ana", "Lopez", "Good morning")     # replaces it
introduce(last="Lopez", first="Ana")          # by name, no order
"""),

md("""
## The ones with a default go last

And this is not a style convention. It is a syntax error, because with the order reversed Python
would have no way of knowing which argument was left out.
"""),

code("""
# FAILS ON PURPOSE. A parameter without a default cannot follow one with a default.
try:
    compile("def introduce(greeting='Hello', name):\\n    pass", "<example>", "exec")
except SyntaxError as e:
    print("SyntaxError:", e.msg)
"""),

md("""
Python rejects it while reading the file, before executing a single line. It is the same early
rejection you saw in review 2 with the single-equals `if`, and in both cases it saves you from a bug
that would be far more expensive to find later.

## Type annotations document, they do not enforce

You can write what type you expect for each parameter and what type the function returns. Python
**does not check any of it at run time**.
"""),

code("""
def print_age(age: int) -> None:
    print("Age:", age)


def rectangle_area(base: float, height: float) -> float:
    return base * height


print_age(20)
print("Area:", rectangle_area(2, 3))
"""),

code("""
# FAILS ON PURPOSE, and raises nothing. The annotation says int and we pass a string.
print_age("twenty")
print_age([1, 2, 3])

print()
print("The annotation is still there, having served no purpose:")
print(print_age.__annotations__)
"""),

md("""
All three calls worked. The annotation sat in `__annotations__` and nothing consulted it.

So why write them. For two reasons that have nothing to do with running the program: the editor
completes better, and a tool like `mypy` or VS Code itself flags the mistake while you type instead
of once the program is already in production.

## The default list trap

This is the most famous trap in the language, and the only one in this module that produces wrong
data without saying a word.
"""),

code("""
# FAILS ON PURPOSE, and raises nothing. The default list is created ONCE.
def add_grade(grade, grades=[]):
    grades.append(grade)
    return grades


print("First call: ", add_grade(8))
print("Second call:", add_grade(9))
print("Third call: ", add_grade(10))
print()
print("The list stored in the definition:", add_grade.__defaults__)
"""),

md("""
The third call handed back three grades, and only one was passed to it.

The default value is evaluated **once**, when Python reads the `def`. That list lives attached to the
function, in `__defaults__`, and every call that arrives without an argument appends to it. A server
running that function for weeks accumulates everything that ever passed through.

The fix is `None` as the default, and building the list inside.
"""),

code("""
def add_grade_properly(grade, grades=None):
    if grades is None:
        grades = []         # a fresh list on every call
    grades.append(grade)
    return grades


print("First call: ", add_grade_properly(8))
print("Second call:", add_grade_properly(9))
print("Third call: ", add_grade_properly(10))
"""),

md("""
This is where the `is None` from review 2 finds its first real use. You do not compare with `==`,
because an empty list is also falsy in an `if`, and then an explicit `grades=[]` would be
indistinguishable from "nothing was passed".

Keep this cell. In week 6, when two objects of the same class share one list and nobody can see why,
it will be exactly this mechanism wearing a different costume.

## Redefining a function replaces it in silence
"""),

code("""
# FAILS ON PURPOSE, and raises nothing at first. Two functions with the same name.
def print_name(first, last="Doe"):
    print(first, last)


print_name("John")             # works, uses the default


def print_name(first, last):               # same name, different signature
    print(first, last)


try:
    print_name("John")         # the very same call as above
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
The call did not change. What changed is which function that name points to.

A `def` is an assignment: it builds the function and ties it to that name, exactly like `x = 5`. If
further down the file there is another `def` with the same name, the second one overwrites the first
and nobody warns you.

This is not an invented example. The course's `Code010.py` defines `print_name` on line 82 and
defines it again on line 144 with a different signature. The file runs clean because every call sits
before the second definition, but anyone adding a line at the end walks into the surprise.
"""),

md("""
---
# Block 2 · Returning

Printing and returning are not the same thing, and confusing them breaks half the exercises in the
course.

`print` writes to the console and leaves nothing usable behind. `return` hands a value to whoever
called, so it can be stored, added to, or passed on.
"""),

code("""
def average_prints(grades):
    print(sum(grades) / len(grades))


def average_returns(grades):
    return sum(grades) / len(grades)


a = average_prints([8, 9, 10])
b = average_returns([8, 9, 10])

print("a is", a, "of type", type(a).__name__)
print("b is", b, "of type", type(b).__name__)
"""),

md("""
Both functions computed the same thing. Only one handed it over.

**A function without `return` gives back `None`.** Every time, no exceptions, and without warning.
That is why `a` ended up as `None` even though 9.0 appeared on screen: that nine was written by the
`print` inside and was lost right there.
"""),

code("""
# FAILS ON PURPOSE. Doing arithmetic on what a printing function handed back.
try:
    print("The average times ten is", a * 10)
except TypeError as e:
    print("TypeError:", e)

print("With the one that returns:", b * 10)
"""),

md("""
The `TypeError` shows up on the multiplication line, which is not where the problem is. The problem
is in the function, several lines above, and nothing breaks there.

That pattern of "the error appears far from its cause" is the same one from review 1 with dynamic
typing. You will meet it again and again.

## `return` also ends the function
"""),

code("""
def check(age):
    if age < 0:
        return "invalid age"       # leaves right here
    print("This line only runs when the age is valid")
    return "age accepted"


print(check(-5))
print()
print(check(30))
"""),

md("""
With `-5` the middle line never printed. The `return` handed over the value and abandoned the
function at that point.

A function can hold several `return` statements, but **only one executes**. That is the early-exit
pattern, and it is what saves you from six levels of nested `if`/`else`.
"""),

code("""
def classify_age(age):
    if age < 0:
        return "invalid"
    if age < 18:
        return "minor"
    if age < 65:
        return "adult"
    return "senior"


for age in [-1, 10, 30, 70]:
    print(f"{age:>3} -> {classify_age(age)}")
"""),

md("""
## Handing back several things at once
"""),

code("""
def square_and_cube(number):
    return number * number, number * number * number


result = square_and_cube(2)
print("Returns:", result, "of type", type(result).__name__)

square, cube = square_and_cube(3)       # unpacking
print("Square:", square, "· cube:", cube)
"""),

md("""
The comma in the `return` builds a tuple. There is no special syntax for returning two values, there
is only a tuple being unpacked on the other side.

Tuples are review 4's topic. For now it is enough to know that the number of names on the left has to
match the number of values.
"""),

code("""
# FAILS ON PURPOSE. Three names for two values.
try:
    a1, a2, a3 = square_and_cube(4)
except ValueError as e:
    print("ValueError:", e)
"""),

md("""
## The risk the slide flags

`calculate_average` divides by `len(grades)`. With an empty list, that is a division by zero.
"""),

code("""
def calculate_average(grades: list) -> float:
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)


print("With data:", calculate_average([8, 9, 10]))

# FAILS ON PURPOSE. An empty list has nothing to average.
try:
    print(calculate_average([]))
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
"""),

md("""
An empty list is not an exotic case. It is what arrives when a filter matched nothing, when the file
came without rows, or when the group has no grades recorded yet.

Review 5 catches it with `try`. For now, the defensive version is deciding what the average of
nothing means and writing that down.
"""),

code("""
def calculate_average_safely(grades):
    if not grades:              # an empty list is falsy
        return None             # "no average" is not the same as "zero"
    return sum(grades) / len(grades)


for group in [[8, 9, 10], [], [7]]:
    print(f"{str(group):<12} -> {calculate_average_safely(group)}")
"""),

md("""
Returning `None` rather than `0` is a decision, not a detail. An average of zero says the group
failed. `None` says there is nothing to compute with, which is what actually happened.
"""),

md("""
---
# Block 3 · Scope

Where a variable lives and how long it lasts.

A variable declared inside a function exists only while that function runs. Outside it, Python does
not know the name.
"""),

code("""
def my_function():
    message = "Hello World"     # local: born and destroyed with the call
    print("Inside:", message)


my_function()

# FAILS ON PURPOSE. Out here, that name does not exist.
try:
    print(message)
except NameError as e:
    print("NameError:", e)
"""),

code("""
# FAILS ON PURPOSE. Parameters are local too.
def my_function2(phrase):
    print("Inside:", phrase)


my_function2("a phrase")

try:
    print(phrase)
except NameError as e:
    print("NameError:", e)
"""),

md("""
## The lookup rule

When Python meets a name inside a function, it looks for it in this order:

1. In the function's local scope.
2. If it is not there, outside, in the global scope.
3. If it is nowhere, it raises `NameError`.

Reading a global from inside works with no ceremony.
"""),

code("""
VAT = 0.16          # global, in CAPITALS by the constant convention


def with_tax(amount):
    return amount * (1 + VAT)     # reads the global without declaring anything


print(with_tax(1000))
"""),

md("""
## Assigning inside is another story
"""),

code("""
message = "global"


def change():
    message = "local"       # does NOT modify the outer one: it creates a new one
    print("Inside:", message)


change()
print("Outside:", message)
"""),

md("""
Inside it printed `local` and outside it still says `global`. They are two different variables that
share a name and know nothing about each other.

**If you assign to a name inside a function, Python treats it as local.** Even when a global of that
name exists, even when the assignment is on the last line.

Changing the global for real needs a declaration.
"""),

code("""
message = "global"


def change_for_real():
    global message          # now it is the outer one
    message = "changed from inside"


change_for_real()
print("Outside:", message)
"""),

md("""
It works, and it is still almost never what you want.

A function that modifies globals cannot be read on its own: to know what it does you have to check
who else touches that variable anywhere in the file. It cannot be tested in isolation either, because
its result depends on what happened before.

**The alternative is returning the value.** The function ends up with one way in and one way out.
"""),

code("""
def change_by_returning(current):
    return current.upper() + " (processed)"


message = "global"
message = change_by_returning(message)
print(message)
"""),

md("""
In week 3 this changes shape. An object carries its own data, and a method modifies it by writing
`self.message = ...` with no need for `global` and nothing to hand back. That is what classes came to
solve: giving a group of functions a shared place to keep things, without polluting the global scope.

## Predict before you run

What does the last line print?

- **A.** 5, because `total` was 0 and it added 5.
- **B.** `UnboundLocalError`, because `total` is local and is read before being assigned.
- **C.** 0, because the global never changed.
- **D.** `None`, because the function returns nothing.
"""),

code("""
# FAILS ON PURPOSE. The quiz answer, caught so the notebook keeps going.
total = 0


def add(n):
    total = total + n
    return total


try:
    print(add(5))
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
"""),

md("""
The answer is **B**.

| Step | What Python sees | Decision |
|---|---|---|
| 1 | `total = 0` outside the function | it is global |
| 2 | inside there is an assignment to `total` | treats it as local throughout |
| 3 | the right-hand side reads `total` | the local does not exist yet |
| 4 | raises `UnboundLocalError` | before adding anything |

What throws people is that the decision is made **before a single line executes**. Python scans the
whole body when compiling the function: if it finds an assignment to `total` on any line, the name is
local on all of them, including the line that reads it first.

Both fixes below, and only one is good.
"""),

code("""
# The clean one: take it in, hand it back.
def add_properly(total, n):
    return total + n


total = 0
total = add_properly(total, 5)
print("With a parameter and a return:", total)


# The one that works but ties the function to that variable.
total = 0


def add_global(n):
    global total
    total = total + n
    return total


print("With global:                  ", add_global(5))
"""),

md("""
The first version can be called with any pair of numbers and tested without setting anything up. The
second only works if a variable called `total` exists, and returns something different depending on
how many times it was called before.

## Every call gets brand new locals
"""),

code("""
def count():
    n = 0           # created on entry
    n += 1
    return n        # and destroyed on exit


print([count() for _ in range(5)])
"""),

md("""
Five calls and five ones. One call's `n` knows nothing about the previous call's `n`, because each
lived inside its own execution.

That gap is exactly what an object fills. When you write `self.n += 1` in week 3, the value will
survive between calls, because it does not live in the function but in the object.
"""),

md("""
---
# FizzBuzz, the exercise that uses everything above

Print the numbers from 1 to 100, swapping multiples of three for `Fizz`, multiples of five for
`Buzz`, and multiples of both for `FizzBuzz`.

It fits in ten lines and reviews function, loop, remainder, chained conditionals and a default `else`.
It has been an interview question for twenty years, and the reason is that the order of the
conditions separates whoever understood `elif` from whoever memorised it.
"""),

code("""
def fizz_buzz(up_to=100):
    \"\"\"Print 1 to up_to, with the FizzBuzz substitutions.\"\"\"
    for number in range(1, up_to + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizz_buzz(15)      # the first fifteen, to keep the screen readable
"""),

md("""
Fifteen is enough to show all four cases: 3 came out `Fizz`, 5 came out `Buzz`, 15 came out
`FizzBuzz` and the rest came out as numbers.

## Why the double condition goes first

Because `elif` stops at the first true branch. If `number % 3 == 0` is evaluated first, 15 lands
there and never reaches the `FizzBuzz` branch.

Rather than assert that, count it.
"""),

code("""
def count_fizz_buzz(correct_order):
    \"\"\"Count how many of 1 to 100 land in each category.\"\"\"
    tally = {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "number": 0}
    for number in range(1, 101):
        if correct_order and number % 3 == 0 and number % 5 == 0:
            tally["FizzBuzz"] += 1
        elif number % 3 == 0:
            tally["Fizz"] += 1
        elif number % 5 == 0:
            tally["Buzz"] += 1
        elif number % 3 == 0 and number % 5 == 0:
            tally["FizzBuzz"] += 1          # unreachable with the wrong order
        else:
            tally["number"] += 1
    return tally


# FAILS ON PURPOSE, and raises nothing. Compare the two orders.
good = count_fizz_buzz(True)
bad = count_fizz_buzz(False)

print(f"{'Category':<12}{'Good order':>12}{'Bad order':>12}")
for key in good:
    print(f"{key:<12}{good[key]:>12}{bad[key]:>12}")
"""),

md("""
With the bad order, `FizzBuzz` comes out at zero and `Fizz` climbs from 27 to 33. The six that went
missing are 15, 30, 45, 60, 75 and 90, and they all landed in `Fizz`.

Not one of the hundred lines raised an error. The program runs, prints a hundred rows and six of them
are wrong. A category with zero cases after sweeping the whole range is the signature of an
unreachable branch, the same one from review 2.
"""),

code("""
print("The six that change category:",
      [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0])
"""),

md("""
## The version that returns

`fizz_buzz` prints, which means it cannot be tested without reading the screen. A function that
**returns** the label can be checked with a comparison.
"""),

code("""
def evaluate_fizz_buzz(number: int) -> str:
    \"\"\"Return the label a number deserves.\"\"\"
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


EXPECTED = {1: "1", 3: "Fizz", 5: "Buzz", 9: "Fizz", 10: "Buzz", 15: "FizzBuzz",
            30: "FizzBuzz", 98: "98"}

for number, expected in EXPECTED.items():
    got = evaluate_fizz_buzz(number)
    mark = "ok" if got == expected else "FAILS"
    print(f"{number:>3} -> {got:<9} expected {expected:<9} {mark}")
"""),

md("""
Notice there is no final `else` any more: since each `return` leaves the function, the last line is
only reached when no condition held.

And printing is now the caller's business, not the function's.
"""),

code("""
for number in range(1, 16):
    print(evaluate_fizz_buzz(number), end="  ")
print()
"""),

md("""
## Four errors from this module

**Defining and never calling.** The `def` only creates the function. Without a call with parentheses
it never runs, and nothing warns you.

**Printing instead of returning.** The function shows the result and hands back `None`, so the caller
is left empty-handed.

**Expecting the local to change the global.** Assigning inside creates a new variable. To change the
outer one, return it.

**A list as a default value.** `def f(x=[])` shares one list across every call. Use `None` and build
it inside.

All four ran above, and three of them without raising a single error.
"""),

md("""
---
# Exercises

The solutions are at the very bottom of the notebook.

### Exercise 1 · The smallest one

Write a function `introduce_yourself` that takes nothing and prints your name and your degree. Call
it three times. Then write a line that mentions it **without** parentheses and print what comes out.

### Exercise 2 · Parameter against argument

Write `calculate_total(price, quantity, discount=0)` that prints the total. Call it four ways: by
position, by name, mixing the two, and leaving the discount out.

Say in a comment which of the four reads best and why.

### Exercise 3 · Printing against returning

Write two versions of a function that computes the area of a circle, one that prints and one that
returns. Try to use the result of both to add up the area of three circles.

Catch the first one's error and print it.

### Exercise 4 · Early exit

Write `classify_bmi(weight, height)` that returns the category by body mass index: under 18.5
underweight, under 25 normal, under 30 overweight, and above that obesity.

Use several `return` statements instead of nested `if`/`elif`. Test it with the exact value of every
boundary.

### Exercise 5 · Handing back several things

Write `statistics(numbers)` that returns the minimum, the maximum and the average in a single
`return`. Unpack it into three variables when calling it.

Then try unpacking it into two and catch the `ValueError`.

### Exercise 6 · The list trap

Reproduce the default list bug with a function `record_attendance(student, roll=[])`. Call it four
times with different students and show what each call hands back.

Then fix it with `None` and prove with the same four calls that it now behaves.

### Exercise 7 · Scope

Write a function that tries to modify a global variable three ways: assigning directly, using
`global`, and returning the value. Show what the global holds after each one.

Say in a comment which of the three you would use in a real program.

### Exercise 8 · The counter that does not count

Write a function `next_invoice_number()` that you want to return 1, 2, 3 on successive calls. Build
it first with a local variable and prove that it always returns 1.

Then fix it with `global` and explain in a comment why that solution does not scale to two
independent counters.

### Exercise 9 · Homework

Write three functions that take a list of grades and return the average, the highest, and how many
passed with 7 or more.

All three hand back with `return` and none prints from inside. All three take the list as a parameter
and none reads a global. Each name is a verb and a noun.

Test them with a normal list and with an empty one.
"""),

md("""
---
## Three things to take away

**A function is a responsibility with a name.** In three weeks the same thing will be called a method
and will live inside a class, with the same rules for parameters and return values you just saw.

**`return` hands over, `print` only shows.** A calculating function that prints leaves the caller
holding `None`, and the `TypeError` shows up several lines later.

**Assigning inside creates a local.** Even when a global of that name exists, and even when the
assignment is on the function's last line.

Next review, the four collections and when to reach for each. The default list from this notebook
comes back there under the name aliasing, and it is what explains in week 6 why two objects share
state.
"""),

md("""
---
# Solutions

### Exercise 1

```python
def introduce_yourself():
    print("David Escobar, Systems Engineering")


introduce_yourself()
introduce_yourself()
introduce_yourself()

print(introduce_yourself)      # no parentheses: the reference, not the run
```

The last line prints something like `<function introduce_yourself at 0x7f...>`. The address changes
every session and means nothing useful beyond "there is a function here, not a result".

### Exercise 2

```python
def calculate_total(price, quantity, discount=0):
    total = price * quantity * (1 - discount)
    print(f"Total: {total:,.2f}")


calculate_total(150, 3, 0.10)                              # position
calculate_total(price=150, quantity=3, discount=0.10)      # name
calculate_total(150, quantity=3, discount=0.10)            # mixed
calculate_total(150, 3)                                    # no discount

# The second reads best. In the first one, 0.10 does not say whether it is a
# discount, a tax or a commission, and you have to go find the definition to
# know. The cost of writing the names is paid once; the cost of hunting for the
# signature is paid every time somebody reads that line.
```

### Exercise 3

```python
import math


def circle_area_prints(radius):
    print(math.pi * radius ** 2)


def circle_area_returns(radius):
    return math.pi * radius ** 2


try:
    total = (circle_area_prints(1) + circle_area_prints(2)
             + circle_area_prints(3))
except TypeError as e:
    print("TypeError:", e)

total = (circle_area_returns(1) + circle_area_returns(2)
         + circle_area_returns(3))
print(f"Sum of the three areas: {total:.4f}")
```

The first version prints the three numbers and then breaks trying to add three `None` values. The
numbers did appear on screen, which is the deceiving part: it looks like the function worked.

### Exercise 4

```python
def classify_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obesity"


# The exact value of every boundary, at 1.70 m to keep the arithmetic clean.
for target_bmi in [18.4, 18.5, 24.9, 25.0, 29.9, 30.0]:
    weight = target_bmi * 1.70 ** 2
    print(f"BMI {target_bmi:>5} (weight {weight:>6.2f}) -> {classify_bmi(weight, 1.70)}")
```

At all three limits the exact value moves up a category, because the conditions use `<`. A BMI of
exactly 25 comes out `normal` with `<=` and `overweight` with `<`, and the medical definition says 25
is already overweight. The boundary is decided by the definition, not by what is convenient to type.

### Exercise 5

```python
def statistics(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


data = [8, 3, 10, 6, 9]

lowest, highest, average = statistics(data)
print(f"Minimum {lowest} · maximum {highest} · average {average}")

try:
    a, b = statistics(data)
except ValueError as e:
    print("ValueError:", e)
```

The `ValueError` message says how many values arrived and how many names were waiting. It is one of
the few Python errors that hands you the full diagnosis in one line.

### Exercise 6

```python
def record_attendance(student, roll=[]):
    roll.append(student)
    return roll


for student in ["Ana", "Beto", "Carla", "Diego"]:
    print(f"{student:<7} -> {record_attendance(student)}")

print()


def record_attendance_properly(student, roll=None):
    if roll is None:
        roll = []
    roll.append(student)
    return roll


for student in ["Ana", "Beto", "Carla", "Diego"]:
    print(f"{student:<7} -> {record_attendance_properly(student)}")
```

The first version reaches four students on the last call, and not one of them was recorded during
that call. The second hands back a list of one each time, which is what the function's name promises.

### Exercise 7

```python
counter = 10


def assign_directly():
    counter = 99


def with_global():
    global counter
    counter = 99


def by_returning(current):
    return current + 89


assign_directly()
print("After assigning directly:", counter)

with_global()
print("After global:           ", counter)

counter = 10
counter = by_returning(counter)
print("After returning:        ", counter)

# In a real program, the third. The function does not depend on a variable called
# counter existing, it can be tested with any number, and reading the call line
# already tells you what changed. With global you have to search the whole file
# for everyone else who touches it before you can claim anything.
```

### Exercise 8

```python
def next_invoice_number_local():
    number = 0
    number += 1
    return number


print("With a local: ", [next_invoice_number_local() for _ in range(3)])

invoice_counter = 0


def next_invoice_number_global():
    global invoice_counter
    invoice_counter += 1
    return invoice_counter


print("With global:  ", [next_invoice_number_global() for _ in range(3)])

# The global version does not scale because the variable name is written inside
# the function. To keep two independent counters, one for invoices and one for
# credit notes, you would need two globals and two nearly identical functions.
# That is precisely the problem a class solves: each object brings its own
# counter and the function is written once.
```

### Exercise 9

```python
def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


def find_highest(grades):
    if not grades:
        return None
    return max(grades)


def count_passing(grades, pass_mark=7):
    return sum(1 for grade in grades if grade >= pass_mark)


GROUP = [8, 5, 10, 6.5, 9, 7, 4, 8.5]

print(f"Average: {calculate_average(GROUP):.2f}")
print(f"Highest: {find_highest(GROUP)}")
print(f"Passing: {count_passing(GROUP)} of {len(GROUP)}")

print()
print("With an empty list:", calculate_average([]), find_highest([]),
      count_passing([]))
```

`count_passing` can legitimately return zero for an empty list, and there zero is the right answer:
nobody passed because there is nobody. The other two return `None`, because the average and the
maximum of an empty set do not exist.

That distinction between "the result is zero" and "there is no result" is what makes a report tell
the truth. `max([])` in fact raises `ValueError` for the same reason, and review 5 will catch it.
"""),

]

write(OUT / "en" / "w01.3.ipynb", en)
print("wrote", OUT / "en" / "w01.3.ipynb")
