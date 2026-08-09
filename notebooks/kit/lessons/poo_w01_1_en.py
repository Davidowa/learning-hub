"""notebooks/programacion-orientada-a-objetos/en/w01.1.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w01.1.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/1st Module/Code001-Code005.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object Oriented Programming · Review 1 of 5
## Module 1 · Data and text

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

The first of five review sessions, one per module of `01 - Basics`. This one covers module 1 in
full, from `Code001` to `Code005`.

It is not new material. It is the floor everything else stands on, and a couple of things here come
back in week 3 under another name: when you see an attribute break a method, this will be why.

By the end of this notebook you will be able to:

1. Declare variables of the five basic types and know which suits each value.
2. Explain dynamic typing: why the name has no type and the value does.
3. Slice and compose text with indexes, slices and f-strings.
4. Use the seven arithmetic operators and their seven shorthands.
5. Convert what arrives from `input`, and recognise the `TypeError` of not doing it.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Six fail on purpose and carry a comment saying so.

There is **exactly one cell with a real `input`**, marked. In Colab it opens a text box and waits;
everything else uses values already assigned so "Run all" never stops.
"""),

md("""
---
# Block 1 · Variables and types

The first thing any program does is store something and give it a name so it can be found again.

A variable is a name tied to a value. **The name has no type; the value does.**

| Type | What it holds | Example | Its falsy value |
|---|---|---|---|
| `int` | Whole numbers, no size limit | `student_count = 1000` | `0` |
| `float` | Decimals, with limited precision | `rating = 4.99` | `0.0` |
| `bool` | True or false | `is_published = False` | `False` |
| `str` | Text, in quotes | `course = "Python"` | `""` empty |
| `NoneType` | The absence of a value | `result = None` | `None` |
"""),

code("""
student_count = 1000          # int
rating = 4.99                 # float
is_published = False          # bool
course_name = "Python"        # str
result = None                 # NoneType

print(type(student_count), type(rating), type(is_published))
print(type(course_name), type(result))
"""),

md("""
## Dynamic typing

The same variable can hold a number and then a string, with Python raising no objection.
"""),

code("""
student_count = 1000
print(student_count, type(student_count))

student_count = "1000"        # now it is a str
print(student_count, type(student_count))
"""),

md("""
**No error warns you at that moment.** The program blows up later, when somebody tries to operate on
what has stopped being a number.
"""),

code("""
# FAILS ON PURPOSE. The error surfaces far from its cause.
student_count = 1000
student_count = "1000"        # <- the cause is here

print("The program carries on...")

try:
    print(student_count + 500)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
A name that holds something else halfway through the program is the cheapest class of bug to avoid:
you avoid it by not reassigning.

That idea returns in week 3. An object's attribute is exactly a variable with a different scope, and
reassigning it to another type breaks any method that uses it.

## Multiple assignment
"""),

code("""
x, y = 1, 2
print(x, y)

x, y = y, x                   # the swap, with no temporary variable
print(x, y)

a = b = c = 0                 # all three to the same value
print(a, b, c)
"""),

md("""
## The falsy values

Every type has one value that counts as false in a condition. Everything else counts as true.
"""),

code("""
for value in [0, 0.0, False, "", None, [], {}]:
    print(f"{str(value)!r:<8} -> {bool(value)}")
"""),

code("""
# FAILS INTUITION ON PURPOSE. Any non-empty string is true.
print('bool("0")     ->', bool("0"), "<- surprising")
print('bool(" ")     ->', bool(" "), "<- a single space too")
print('bool("")      ->', bool(""))
print('bool("False") ->', bool("False"), "<- even this one")
"""),

md("""
`bool("0")` is true because `"0"` is a string with one character in it. What Python looks at is
whether it is empty, not what it says.

That is the error behind validations that let everything through.
"""),

md("""
---
# Block 2 · Text

A string is a sequence of characters, and nearly everything you learn about it applies to lists
afterwards.
"""),

code("""
course = "Python Programming"

print("Length:       ", len(course))
print("The first:    ", course[0])
print("The last:     ", course[-1])
print("From 0 to 2:  ", course[0:3])
print("From 7 on:    ", course[7:])
print("Up to 6:      ", course[:6])
print("Reversed:     ", course[::-1])
"""),

md("""
The first index is included, the second is not. That is why `course[0:3]` returns three characters,
and why `course[0:3] + course[3:]` rebuilds the whole string.
"""),

code("""
print(course[0:3] + course[3:] == course)
"""),

md("""
## Methods return copies

A string **cannot be modified**. Every string method returns something new.
"""),

code("""
# FAILS ON PURPOSE. A string is immutable.
try:
    course[0] = "J"
except TypeError as e:
    print("TypeError:", e)
"""),

code("""
# FAILS ON PURPOSE. Calling the method and not keeping what it returns.
course = "Python Programming"
course.upper()

print("After course.upper():", course, "<- unchanged")

course = course.upper()
print("Keeping the result:  ", course)
"""),

md("""
That is the module's third error, and it is the same pattern you will meet with `sort` in review 4:
some things return and others modify, and confusing them makes the program run without doing
anything.
"""),

code("""
course = "Python Programming"

print("upper:      ", course.upper())
print("lower:      ", course.lower())
print("title:      ", course.title())
print("strip:      ", repr("  hello  ".strip()))
print("replace:    ", course.replace("Python", "Java"))
print("split:      ", course.split())
print("find:       ", course.find("Pro"))
print("startswith: ", course.startswith("Py"))
print("in:         ", "Program" in course)
print()
print("And the original is still:", course)
"""),

md("""
## f-strings
"""),

code("""
name = "Ana"
age = 21
average = 9.4567

print(f"{name} is {age} years old")
print(f"Her average is {average:.2f}")
print(f"In five years she will be {age + 5}")
print(f"In capitals: {name.upper()}")
print(f"Aligned: [{name:>10}] [{name:<10}]")
"""),

md("""
Inside the braces you can put a variable, an expression or a call. After the colon goes the
formatting, and it does not change the stored value.
"""),

md("""
---
# Block 3 · Operators

All seven arithmetic ones.

| Operator | What it does | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Product | `10 * 3` | `30` |
| `/` | Decimal division | `10 / 3` | `3.333…` |
| `//` | Integer division | `10 // 3` | `3` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Power | `10 ** 3` | `1000` |
"""),

code("""
for op, result in [("10 + 3", 10 + 3), ("10 - 3", 10 - 3), ("10 * 3", 10 * 3),
                   ("10 / 3", 10 / 3), ("10 // 3", 10 // 3),
                   ("10 % 3", 10 % 3), ("10 ** 3", 10 ** 3)]:
    print(f"{op:<10} = {result}")
"""),

md("""
## The two divisions are not the same

The single slash **always** returns a `float`, even when the division is exact. The double slash
discards the decimal part.
"""),

code("""
print("10 / 5  =", 10 / 5, type(10 / 5).__name__, "<- float even when exact")
print("10 // 5 =", 10 // 5, type(10 // 5).__name__)
print()
print("10 / 4  =", 10 / 4)
print("10 // 4 =", 10 // 4)
print("10 % 4  =", 10 % 4)
print()
print("The quotient and remainder rebuild the original:", 10 // 4 * 4 + 10 % 4)
"""),

md("""
The remainder answers a different question: what was left after sharing out.
"""),

code("""
for n in range(1, 11):
    print(f"{n:>3} is even: {n % 2 == 0:<6} multiple of 3: {n % 3 == 0}")
"""),

md("""
`n % 2 == 0` is the even test and `n % 3 == 0` the multiple-of-three test. That is exactly what
FizzBuzz asks for in review 3.

## The seven, in short form

| Operator | Equivalent to | Starting from `x = 10` | `x` ends at |
|---|---|---|---|
| `+=` | `x = x + 3` | `x += 3` | `13` |
| `-=` | `x = x - 3` | `x -= 3` | `7` |
| `*=` | `x = x * 3` | `x *= 3` | `30` |
| `/=` | `x = x / 3` | `x /= 3` | `3.333…` |
| `//=` | `x = x // 3` | `x //= 3` | `3` |
| `%=` | `x = x % 3` | `x %= 3` | `1` |
| `**=` | `x = x ** 3` | `x **= 3` | `1000` |
"""),

code("""
for label, operation in [("+=", lambda x: x + 3), ("-=", lambda x: x - 3),
                         ("*=", lambda x: x * 3), ("/=", lambda x: x / 3),
                         ("//=", lambda x: x // 3), ("%=", lambda x: x % 3),
                         ("**=", lambda x: x ** 3)]:
    x = 10
    x = operation(x)
    print(f"x = 10; x {label:<4} 3  ->  {x}")
"""),

md("""
Watch `/=`: it turns an integer into a decimal, and `//=` does not. That difference sneaks into
reports where suddenly everything prints with a `.0` on the end.
"""),

md("""
---
# Block 4 · Console input

`input` **always** returns text. Without exception.

This is the only cell in the notebook that waits for you.
"""),

code("""
# THIS CELL WAITS FOR YOU. In Colab it opens a text box above.
# The try is so a headless "Run all" does not hang.
try:
    x = input("Type a number: ")
except Exception:
    x = "5"
    print("(no keyboard available, using 5)")

print("What arrived:", repr(x), type(x))
print("Converted:   ", int(x), type(int(x)))
"""),

md("""
From here on everything uses values already assigned. But it is worth seeing what happens without
converting.

**Predict before you run.** What does the last line print?

- **A.** 3, because 200 has three digits.
- **B.** 6, because it repeated the text "100" twice.
- **C.** An error, text cannot be multiplied.
- **D.** 2, because `total` is 200 and `len` counts two things.
"""),

code("""
price = "100"

total = price * 2

print(total)
print(len(total))
"""),

md("""
The answer is **B**, six.

| Step | Statement | `price` | `total` | Type of `total` |
|---|---|---|---|---|
| 1 | `price = "100"` | `"100"` | – | `str` |
| 2 | `total = price * 2` | `"100"` | `"100100"` | `str` |
| 3 | `len(total)` | `"100"` | `"100100"` | `6` |

Multiplying a string by an integer **repeats it**. To work with numbers you need `int(price)`
first.

And it raised nothing, which is the dangerous part.
"""),

code("""
price = "100"

print("Unconverted:", price * 2)
print("Converted:  ", int(price) * 2)
"""),

code("""
# FAILS ON PURPOSE. Adding text and a number does raise.
try:
    print("100" + 2)
except TypeError as e:
    print("TypeError:", e)
"""),

md("""
Multiplying text by an integer works and adding them does not. That inconsistency is why the error
shows up sometimes and sometimes not.

## The conversions
"""),

code("""
for value in ["100", "4.99", "abc", "", "  7  "]:
    for conv in (int, float):
        try:
            print(f"{conv.__name__}({value!r:<8}) -> {conv(value)}")
        except ValueError:
            print(f"{conv.__name__}({value!r:<8}) -> ValueError")
"""),

md("""
`int("4.99")` fails and `float("4.99")` works: `int` does not round text with a decimal point.

## Four errors from this module

**Operating on what came from `input`.** `TypeError`, because `input` returns `str`.

**Believing `bool("0")` is `False`.** Any non-empty string is true.

**Calling a method and not keeping it.** `course.upper()` does not change `course`.

**Confusing the single slash with the double.** The single one always gives a `float`.

All four ran above.
"""),

md("""
---
# Exercises

The solutions sit at the very bottom of the notebook.

### Exercise 1 · The five types

Declare one variable of each of the five types, with names saying what they hold, and print each
with its `type` and its truth value.

### Exercise 2 · The type that changes

Write a five-line program where a variable starts as a number, becomes text halfway, and blows up
three lines later when operated on. Catch the error and print it.

### Exercise 3 · Slices

With `course = "Object Oriented Programming"`, extract: the first word, the last, the first ten
characters, the last eleven, and the string reversed.

Check that the original did not change.

### Exercise 4 · The methods you do not keep

Take a string and apply five methods without storing the result. Print the string after each to
confirm it is unchanged. Then do it properly.

### Exercise 5 · The seven operators

With `a = 17` and `b = 5`, print all seven results with labels. Then check that
`a // b * b + a % b` rebuilds `a`.

### Exercise 6 · Even, odd and multiple

Write a program walking 1 to 20 and printing, for each number, whether it is even and whether it is
a multiple of five. Use only the remainder.

### Exercise 7 · The conversion that is needed

These values arrived as text. Work out the total and the average, and handle the one that cannot be
converted without the program stopping.

```python
ENTRIES = ["100", "250", "not captured", "75", "300"]
```

### Exercise 8 · The homework

Write a program that asks for a name and an age from the keyboard, and greets with an f-string
saying which year they turned that age.

Write it in a new cell at the end and run it yourself, by hand.
"""),

md("""
---
## Three ideas to take away

**The name has no type, the value does.** In three weeks that same fact will explain why an
attribute can break a method.

**Strings are not modified, they are copied.** Every string method returns something new, so it has
to be stored.

**`input` returns text, always.** Converting is your responsibility, and forgetting is the commonest
`TypeError` of the course.

The next review is comparison, logic and the two kinds of loop.
"""),

md('''
---
# Solutions

### Exercise 1

```python
enrolled_students = 42
group_average = 8.73
is_published = False
course_name = "Object Oriented Programming"
close_date = None

for name, value in [("enrolled_students", enrolled_students),
                    ("group_average", group_average),
                    ("is_published", is_published),
                    ("course_name", course_name),
                    ("close_date", close_date)]:
    print(f"{name:<20} {str(value):<30} {type(value).__name__:<9} {bool(value)}")
```

`is_published` and `close_date` are the two falsy ones, for different reasons: one because it is
`False` and the other because it is `None`.

### Exercise 2

```python
student_id = 20240315
print("It is a number:", student_id, type(student_id).__name__)

student_id = "20240315"
print("Now it is text:", student_id, type(student_id).__name__)

try:
    print(student_id + 1)
except TypeError as e:
    print("TypeError:", e)
```

A student number is exactly the case where this happens for real: it gets read from a file as text,
somebody converts it to a number to compare it, and it loses its leading zeros.

### Exercise 3

```python
course = "Object Oriented Programming"

print("First word:  ", course[:6])
print("Last word:   ", course[-11:])
print("First ten:   ", course[:10])
print("Last eleven: ", course[-11:])
print("Reversed:    ", course[::-1])
print("Unchanged:   ", course)
```

The first word can also come from `course.split()[0]`, which does not depend on counting characters.
That version survives the course name changing and the slice one does not.

### Exercise 4

```python
text = "  Python Programming  "

text.strip()
text.upper()
text.replace("Python", "Java")
text.lower()
text.title()
print("After five methods:", repr(text))

clean = text.strip().upper()
print("Keeping the result:", repr(clean))
```

All five ran and none changed anything, because nobody kept what they returned. The chain on the
last line works because each method returns a new string the next one can be called on.

### Exercise 5

```python
a, b = 17, 5

print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b  = {a % b}")
print(f"a ** b = {a ** b}")
print()
print("a // b * b + a % b =", a // b * b + a % b, "· is it a?", a // b * b + a % b == a)
```

That identity holds for any pair of positive integers, and it is why `//` and `%` usually turn up
together.

### Exercise 6

```python
for n in range(1, 21):
    parity = "even" if n % 2 == 0 else "odd"
    five = "yes" if n % 5 == 0 else "no"
    print(f"{n:>3}  {parity:<5} multiple of 5: {five}")
```

Not one nested `if` and no helper lists. The remainder answers both questions.

### Exercise 7

```python
ENTRIES = ["100", "250", "not captured", "75", "300"]

valid = []
rejected = []

for entry in ENTRIES:
    try:
        valid.append(int(entry))
    except ValueError:
        rejected.append(entry)

print("Total:  ", sum(valid))
print("Average:", round(sum(valid) / len(valid), 2))
print("Over", len(valid), "of", len(ENTRIES), "entries")
print("Rejected:", rejected)
```

The average is computed over four, not five, and the program says so. Reporting 181.25 without
mentioning that one entry was discarded is what makes a correct number indefensible.

### Exercise 8

```python
name = input("What is your name? ")
age = int(input("How old are you? "))

current_year = 2026
print(f"Hello {name}, you turned {age} in {current_year}")
print(f"So you were born around {current_year - age}")
```

The detail almost everyone gets wrong: `int()` wraps the `input`, not the result of the
subtraction. Without it, `current_year - age` raises `TypeError` because `age` is still text.
'''),

]

write(OUT / "en" / "w01.1.ipynb", en)
print("wrote", OUT / "en" / "w01.1.ipynb")
