"""notebooks/programacion-orientada-a-objetos/en/w01.5.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w01.5.en.yaml
Source code:  docs/en/courses/python-course/01 - Basics/5th Module/Code028.py

Code028.py calls input seven times and does not run headless. The notebook
reproduces its blocks with assigned values and keeps a single real input cell.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Review 5 of 5
## Module 5 · Errors

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Read a traceback, catch the error you expected and let the one you did not through.

The four previous reviews left errors scattered along the way: the `TypeError` from the lying
annotation, the `ValueError` from unpacking, the `IndexError` from the short list, the `KeyError`
from the grant that was not there. All of them were caught with `try` so the notebook could keep
running, and so far nobody explained how that works. This notebook explains it.

By the end you will be able to:

1. Read a traceback from the bottom up and say which line the problem started on.
2. Name the seven errors you will meet most, and what causes each one.
3. Write one `except` per type, and explain what a bare `except` hides.
4. Use `else` and `finally`, and say exactly when each one runs.
5. Choose between an `if` and a `try` with a single question.

### How to use this notebook

Run the cells in order with **Shift + Enter**. This is the notebook where nearly everything fails on
purpose, so the marker changes meaning: here what gets flagged is **the error that slips through
unnoticed**.

One single cell waits for you to type something. It is marked and it will not block a "Run all".
"""),

md("""
---
# Block 1 · Reading the error

Python already told you what happened and on which line. The problem is almost never the message, it
is not reading it.

The cell below causes a real error and prints it in full with `traceback.print_exc()`. It is the same
text you would see if the program had stopped, except here it does not stop.
"""),

code("""
import traceback


def divide(a, b):
    return a / b


try:
    print(divide(10, 0))
except ZeroDivisionError:
    traceback.print_exc()
"""),

md("""
It reads **from the bottom up**, and that is the whole trick.

| Line | What it tells you |
|---|---|
| The last one | The error type and the message. Always start here. |
| The one above | The file, the line and the function where it happened |
| The ones further up | The path the program followed to get there |
| The first one | The original call, the one you wrote |

The type and the line give you almost everything. The rest of the path only matters when the error
comes from a distant function, and there it is worth its weight in gold.
"""),

code("""
def level_3(x):
    return 10 / x


def level_2(x):
    return level_3(x)


def level_1(x):
    return level_2(x)


try:
    level_1(0)
except ZeroDivisionError:
    traceback.print_exc()
"""),

md("""
Four lines of path, each with its own line number.

The bottom one says where it blew up: in `level_3`, at the division. The top one says who started it
all: the `level_1(0)` call. The fix almost never goes on the bottom line, because the division is
written correctly. It goes up top, where somebody passed a zero.

That is the real value of the full path: **the error happens at the bottom and the blame sits at the
top**.

## The seven errors of the semester
"""),

code("""
examples = [
    ("'5' + 1", lambda: '5' + 1),
    ("int('hello')", lambda: int("hello")),
    ("print(totl)", lambda: totl),                  # noqa: F821
    ("[1, 2][5]", lambda: [1, 2][5]),
    ("{'a': 1}['b']", lambda: {"a": 1}["b"]),
    ("10 / 0", lambda: 10 / 0),
    ("(1, 2).append(3)", lambda: (1, 2).append(3)),
]

for text, trigger in examples:
    try:
        trigger()
        print(f"{text:<18}did not fail")
    except Exception as e:
        print(f"{text:<18}{type(e).__name__:<20}{e}")
"""),

md("""
The messages are worth reading slowly, because they are written to tell you what to do.

`invalid literal for int() with base 10: 'hello'` gives you the exact value it could not convert,
which is the first thing you were going to ask. `can only concatenate str (not "int") to str` tells
you which of the two operands is fine and which one is out of place.

Two pairs that get mixed up a lot:

**`TypeError` against `ValueError`.** The type is wrong against the value is wrong. `int([1, 2])` is
a `TypeError` because a list does not convert to an integer under any circumstances. `int("hello")`
is a `ValueError` because a string does convert, just not that one.

**`NameError` against `AttributeError`.** The name does not exist against the object does not have
that piece. `totl` is a name nobody defined; `append` does exist in the world, just not on a tuple,
as you saw in review 4.

## Errors come in families
"""),

code("""
for exception in (ZeroDivisionError, ValueError, IndexError, KeyError,
                  TypeError, AttributeError, NameError):
    chain, current = [], exception
    while current is not object:
        chain.append(current.__name__)
        current = current.__bases__[0]
    print(" <- ".join(chain))
"""),

md("""
`IndexError` and `KeyError` are the two children of `LookupError`, which means "you looked for
something and it was not there". `ZeroDivisionError` hangs off `ArithmeticError`. And all seven end
at `Exception`.

That is not trivia. An `except` catches the type you name **and every descendant of it**, so
`except LookupError` catches both failed lookups at once, and `except Exception` catches all seven.
That inheritance is the same one you will build yourself in week 7, with your own classes instead of
exceptions.
"""),

code("""
def look_up(collection, where):
    try:
        return collection[where]
    except LookupError as e:
        return f"{type(e).__name__} caught by except LookupError"


print(look_up([1, 2, 3], 5))
print(look_up({"a": 1}, "b"))
print(look_up([1, 2, 3], 1), "<- this one is there")
"""),

md("""
---
# Block 2 · Catching the error

`try` fixes nothing on its own. It decides what happens when something fails.

The full structure has four clauses and only the first is compulsory.

| Clause | When it runs | Compulsory? |
|---|---|---|
| `try` | Always. It is what gets watched. | Yes |
| `except` | Only when that type of error happens | At least one, or a `finally` |
| `else` | Only when the `try` finished without an error | No |
| `finally` | Always, whether it failed or not | No |
"""),

code("""
def compute_factor(age_text):
    \"\"\"The course's Code028.py version, with the input already resolved.\"\"\"
    try:
        age = int(age_text)
        factor = 10 / age
    except ValueError:
        print("  That is not a number")
    except ZeroDivisionError:
        print("  Age cannot be 0")
    else:
        print("  Factor:", factor)
    finally:
        print("  Done trying")


for entry in ["20", "zero", "0"]:
    print(f"With {entry!r}:")
    compute_factor(entry)
    print()
"""),

md("""
Three inputs, three paths, and `finally` on all three.

With `"20"` there was no exception, so the `else` ran and no `except` did. With `"zero"` the `int`
raised `ValueError` before the division was ever reached. With `"0"` the conversion went through fine
and the division was the one that blew up.

That order matters. The `try` is abandoned at the first line that fails, so the lines below it never
run. That is why `factor` does not exist when there is an exception, and why printing it has to go in
the `else` rather than at the end of the `try`.

## Why the `else` and not the end of the `try`
"""),

code("""
# The version without else: the print sits inside the watched block.
def without_else(age_text):
    try:
        age = int(age_text)
        factor = 10 / age
        print("  Factor:", factor["oops"])     # deliberate typo
    except ValueError:
        print("  That is not a number")
    except TypeError:
        print("  That is not a number")        # the same message, lying


without_else("20")
"""),

md("""
The program says "That is not a number" and `20` was perfectly a number.

The `print` with the typo was inside the `try`, so its `TypeError` landed in an `except` that was
talking about something else. With the `print` in the `else`, that error would have surfaced with its
traceback and its line number.

**The `try` wraps the least that can fail.** Two or three lines inside, and the `except` knows exactly
what it is talking about.

## `finally` runs whatever happens
"""),

code("""
def with_finally(x, y):
    try:
        result = x / y
        return f"result {result}"
    except ZeroDivisionError:
        return "division by zero"
    finally:
        print("  finally ran")


print(with_finally(10, 5))
print(with_finally(10, 0))
"""),

md("""
The `finally` printed **before** the returned value, in both cases. It is not that it runs after the
`return`: it runs between the `return` and the handover, because Python stores the value, executes
the `finally`, and only then leaves the function.

That is its reason to exist. What gets opened has to be closed, failure or no failure: a file, a
database connection, a cursor. In week 12 you will see that Python ships something better for that,
the `with` block, and `finally` is what sits underneath it.

## Predict before you run

What does this program print?

```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except ValueError:
    print("value")
except IndexError:
    print("index")
finally:
    print("end")
```

- **A.** `value`, then `end`.
- **B.** `index`, then `end`.
- **C.** Only `end`, because no `except` applies.
- **D.** It crashes before reaching `finally`.
"""),

code("""
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except ValueError:
    print("value")
except IndexError:
    print("index")
finally:
    print("end")
"""),

md("""
The answer is **B**.

| Step | What happens | Result |
|---|---|---|
| 1 | `numbers[5]` on a list of 3 | raises `IndexError` |
| 2 | `except ValueError` | does not match, skipped |
| 3 | `except IndexError` | matches, prints `index` |
| 4 | `finally` | runs regardless, prints `end` |

The `except` clauses are checked **in order** and only the first match runs. That detail about order
has a consequence that bites.
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The second except is never reached.
try:
    10 / 0
except Exception:
    print("it went in here, the generic one")
except ZeroDivisionError:
    print("and this line is never reached")
"""),

md("""
`ZeroDivisionError` descends from `Exception`, so the first `except` already matched and the second
one is dead code. Python does not complain: no syntax error, no warning.

It is exactly the same problem as the FizzBuzz ordering in review 3. The more general branch written
first makes every branch after it unreachable. **From most specific to most general, always.**

## The bare `except`, and why the deck flags it as a risk
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The message lies about what happened.
marks = [8, 9, 10]

try:
    total = sum(marks)
    average = total / len(mark)      # typo: mark, not marks
    print("Average:", average)
except:
    print("The grades could not be read")
"""),

md("""
The grades were read perfectly. What failed was a misspelled name, `mark` instead of `marks`, and the
bare `except` turned it into a message about reading data.

A `NameError` is your own mistake, the kind you fix in five seconds if you hear about it. That
`except` buried it. Multiplied across a thousand-line program, it is the difference between an
afternoon and a week.
"""),

code("""
# The same cell with the type named.
try:
    total = sum(marks)
    average = total / len(mark)      # the same typo
    print("Average:", average)
except ZeroDivisionError:
    print("There are no grades to average")
except NameError as e:
    print("It surfaces:", type(e).__name__ + ":", e)
"""),

md("""
Now the message tells the truth, and even names the variable.

In a real program you would not even write that second `except`: you would let the `NameError`
propagate with its full traceback, which is exactly what you want to see.

## A bare `except` catches more than you think
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A bare except catches the program's own exit.
try:
    raise SystemExit(3)
except Exception as e:
    print("except Exception caught:", type(e).__name__)
except BaseException as e:
    print("only BaseException catches it:", type(e).__name__)
"""),

md("""
`SystemExit` does not descend from `Exception`, it descends straight from `BaseException`. The same
goes for `KeyboardInterrupt`, the one Control C fires.

A bare `except:` is equivalent to `except BaseException:`, so it swallows both. A program with a loop
protected that way **cannot be stopped with Control C**, and in Colab that means restarting the
runtime.

If you genuinely need to catch everything, write `except Exception`. Leave `BaseException` alone.
"""),

md("""
## The most expensive mistake: catching and doing nothing
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The pass eats the bad entries and the report lies.
ENTRIES = ["8", "9", "ten", "7", ""]

valid = []
for entry in ENTRIES:
    try:
        valid.append(int(entry))
    except Exception:
        pass

print("Group average:", sum(valid) / len(valid))
print("Entries recorded:", len(ENTRIES))
"""),

md("""
The average came out at 8.0 and it was computed over three of five. The report says "group average"
and it is not the group's.

`except Exception: pass` is the fastest way to make a program stop crashing and carry on being wrong.
Nothing warns you, and the number that comes out is the right size and the right order of magnitude.

The honest version does not cost more lines.
"""),

code("""
valid, rejected = [], []
for entry in ENTRIES:
    try:
        valid.append(int(entry))
    except ValueError:
        rejected.append(entry)

print(f"Average: {sum(valid) / len(valid):.2f}")
print(f"Computed over {len(valid)} of {len(ENTRIES)} entries")
print("Rejected:", rejected)
"""),

md("""
The average is the same. What changed is that the report now says how many entries it was computed
over and which ones dropped out, so whoever reads it can decide whether that is good enough.

That distinction between a result and its coverage is the same one from review 3 with `None` against
zero, and it is what separates a correct number from a defensible one.
"""),

md("""
## The cell that waits for you
"""),

code("""
# THIS CELL WAITS FOR YOU. In Colab it opens a text box at the top.
# The outer try is so a keyboardless "Run all" does not hang.
try:
    text = input("Type your age: ")
except Exception:
    text = "zero"
    print("(no keyboard available, using 'zero' to show the error path)")

try:
    age = int(text)
except ValueError as e:
    print("ValueError:", e)
    print("What arrived was", repr(text), "and int() has no idea what to do with it.")
else:
    print("Age converted:", age, type(age).__name__)
finally:
    print("The cell finished, with an age or without one.")
"""),

md("""
`input` always returns text, as you saw in review 1. That is why the conversion is the only line that
can genuinely fail, and why it is the only one inside the `try`.

This week's homework rubric asks for exactly that under "Scope of the try": the `try` wraps the
conversion, not the whole program.
"""),

md("""
---
# Block 3 · When not to use `try`

Wrapping everything in a `try` does not make a program robust. It makes it mute.

The rule comes down to one question: **can I check it with an `if` before I try it?**

If the answer is yes, use an `if`. If it depends on something you do not control, use a `try`.

| Situation | Use |
|---|---|
| The list may be empty | `if` |
| The divisor may be zero | `if` |
| The key may be missing | `if` with `in`, or `get` |
| The user types anything | `try` |
| The file may not exist | `try` |
| The network may go down | `try` |

The three at the top you can check yourself with data already in your hands. The three at the bottom
depend on the world, and between checking and using, the world can change.
"""),

code("""
def average_with_if(marks):
    if not marks:
        return None
    return sum(marks) / len(marks)


def average_with_try(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return None


for group in [[8, 9, 10], []]:
    print(f"{str(group):<12} if: {average_with_if(group)}  "
          f"try: {average_with_try(group)}")
"""),

md("""
Both give the same result, and the `if` version reads better because it states the condition in
words: "if there are no marks". The `try` version makes you reconstruct in your head that an empty
list makes `len` zero and that this causes the division.

## What an exception costs

`Code028.py` measures this with `timeit` and reaches a reasonable conclusion. It is worth measuring
again, because the complete conclusion is more interesting than the file's.
"""),

code("""
import timeit

WITH_RAISE = '''
def factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    factor(-1)
except ValueError:
    pass
'''

WITH_IF = '''
def factor(age):
    if age <= 0:
        return None
    return 10 / age

if factor(-1) is None:
    pass
'''

t_raise = timeit.timeit(WITH_RAISE, number=10000)
t_if = timeit.timeit(WITH_IF, number=10000)

print("When the error DOES happen, 10,000 times:")
print(f"  with raise/except: {t_raise * 1000:7.1f} ms")
print(f"  with if/None:      {t_if * 1000:7.1f} ms")
print(f"  the exception cost {t_raise / t_if:.1f} times more")
"""),

code("""
HAPPY_TRY = '''
d = {"a": 1}
try:
    x = d["a"]
except KeyError:
    x = None
'''

HAPPY_IF = '''
d = {"a": 1}
if "a" in d:
    x = d["a"]
else:
    x = None
'''

t_try = timeit.timeit(HAPPY_TRY, number=200000)
t_if2 = timeit.timeit(HAPPY_IF, number=200000)

print("When the error does NOT happen, 200,000 times:")
print(f"  with try/except: {t_try * 1000:7.1f} ms")
print(f"  with if:         {t_if2 * 1000:7.1f} ms")
"""),

md("""
The two cells say different things and both are true.

**Raising an exception costs.** Building the object, assembling the traceback and unwinding the stack
is real work, and with the error firing every single time the `raise` comes out several times more
expensive.

**Entering a `try` that does not fail costs nothing.** The `try` on the happy path comes out as fast
or faster than the `if`, because the `if` evaluates a condition on every pass and the `try` evaluates
nothing while no exception happens.

The exact numbers change with the machine, and the conclusion does not: exceptions are expensive when
they happen often, and free when they are the exception. Hence the name.

The criterion is not about speed anyway. It is about readability, and on that ground the `if` wins for
the predictable and the `try` wins for what comes from outside.

## Raising your own exceptions
"""),

code("""
def compute_factor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    compute_factor(-1)
except ValueError as error:
    print("ValueError:", error)

print("With a valid age:", compute_factor(25))
"""),

md("""
`raise` fires an exception on purpose, with whatever message you write.

It is for when a function spots that its arguments make no sense and it is not its job to decide what
to do about it. `compute_factor` knows a negative age is wrong, but it does not know whether the
program should ask the user again, write it to a log, or abort. It raises, and the caller decides.

Returning `None` is also an option, and the difference is whether the problem is easy to ignore.
`None` can be ignored; an exception cannot. When bad data has to stop the process, `raise`.

Week 11 picks this up properly, with custom exceptions inheriting from `Exception` and with
validation at the edge of the program.
"""),

md("""
---
## Four errors from this module

**A bare `except`.** Catches everything, your own typos included, and turns them into a message that
lies. It also catches `KeyboardInterrupt`, so the program stops responding to Control C.

**A thirty-line `try`.** When it fires, nobody knows which of the thirty failed. Wrap only what can
break and move the rest into the `else`.

**Catching and doing nothing.** An `except` containing only `pass` hides the problem and saves it for
later, usually for after the number has already been reported.

**Using `try` where an `if` would do.** Checking that the list is not empty is an `if`. Checking the
file exists is a `try`.

All four ran above, and none of them raised anything.
"""),

md("""
---
# Exercises

The solutions are at the very bottom of the notebook.

### Exercise 1 · Reading the traceback

Write three chained functions where the last one converts a non-numeric string to an integer. Call the
first one inside a `try` and print the full traceback with `traceback.print_exc()`.

Say in a comment which line has the error and which line has the blame.

### Exercise 2 · The seven errors

Write an expression that triggers each of the seven errors in the table, and catch them all in a loop
that prints the type and the message. Do not repeat any.

### Exercise 3 · From most specific to most general

Write a block with three `except` clauses: `ZeroDivisionError`, `ArithmeticError` and `Exception`, in
that order. Test it with a division by zero.

Then reverse the order and show that a different one runs. Explain in a comment why Python flags
nothing in the reversed version.

### Exercise 4 · The message that lies

Write a block with a bare `except` where the real error is a `NameError` from a misspelled name. Print
a message about something else entirely.

Then fix it by naming the type, and show the true message.

### Exercise 5 · `else` and `finally`

Write a function `divide_reporting(a, b)` with all four clauses. The `try` holds only the division,
the `else` prints the result and the `finally` prints a closing line.

Call it with `(10, 2)`, `(10, 0)` and `(10, "x")`. Explain in a comment how many times the `finally`
ran.

### Exercise 6 · `if` or `try`

For each of these six situations, write the solution with `if` or with `try`, whichever fits, and say
in a comment why:

1. Taking the first item of a list that may be empty.
2. Converting what the user typed to an integer.
3. Dividing by a variable that may be zero.
4. Reading the `"grant"` key from a student dictionary.
5. Opening a file whose name you were given on the console.
6. Taking the square root of a number that may be negative.

### Exercise 7 · The honest average

Take the list `["8", "9", "ten", "7", "", "10"]` and compute the average of the entries that really
are numbers. Report the average, how many entries it was computed over, and which ones were rejected.

Do it first with `except Exception: pass` and show what it reports. Then with the type named and the
list of rejects.

### Exercise 8 · Your own exception

Write `withdraw(balance, amount)` that raises `ValueError` with a different message depending on
whether the amount is negative or exceeds the balance, and that returns the new balance when all is
well.

Test it with three cases and catch the error printing the message.

### Exercise 9 · The homework

Write a program that reads five grades, computes the average in a function, and does not crash on
anything the user types.

The average is computed in a function with a parameter and a return. The `try` wraps only the
conversion, not the whole program. Every `except` names its type. And the final report says how many
of the five it was computed over.
"""),

md("""
---
## Three things to take away

**A traceback reads from the bottom up.** The last line says what happened, the one above says where,
and the full path says who caused it. The error happens at the bottom and the blame is usually at the
top.

**Naming the exception is what helps.** A bare `except` turns your own mistake into a message that
lies, and swallows Control C on the way. From most specific to most general, always.

**If you can check it with an `if`, do not use `try`.** `try` is for what comes from outside and
cannot be foreseen: the keyboard, a file, a connection.

That closes the review of all five modules. Week 2 brings no new code: it brings the question of why
object-oriented programming exists and what problem it came to solve. Everything you reviewed across
these five notebooks is the material that question gets explained with, and from week 3 onward it
starts having names of its own.
"""),

md("""
---
# Solutions

### Exercise 1

```python
import traceback


def convert(text):
    return int(text)


def process(text):
    return convert(text)


def main(text):
    return process(text)


try:
    main("twenty")
except ValueError:
    traceback.print_exc()

# The error is in convert, on the int() line. The blame is on the main("twenty")
# call at the top, because convert does its job correctly: it was handed text
# that is not a number. The fix goes where the data is born.
```

### Exercise 2

```python
cases = [
    ("TypeError", lambda: "5" + 1),
    ("ValueError", lambda: int("hello")),
    ("NameError", lambda: name_that_does_not_exist),   # noqa: F821
    ("IndexError", lambda: [1, 2][5]),
    ("KeyError", lambda: {"a": 1}["b"]),
    ("ZeroDivisionError", lambda: 10 / 0),
    ("AttributeError", lambda: (1, 2).append(3)),
]

for expected, trigger in cases:
    try:
        trigger()
        print(f"{expected:<20}did not fail")
    except Exception as e:
        mark = "ok" if type(e).__name__ == expected else "OTHER"
        print(f"{expected:<20}{type(e).__name__:<20}{mark}  {e}")
```

The right-hand column checks that each expression fired the error it was supposed to, instead of
taking it on trust.

### Exercise 3

```python
print("From specific to general:")
try:
    10 / 0
except ZeroDivisionError:
    print("  ZeroDivisionError")
except ArithmeticError:
    print("  ArithmeticError")
except Exception:
    print("  Exception")

print("The other way round:")
try:
    10 / 0
except Exception:
    print("  Exception")
except ArithmeticError:
    print("  ArithmeticError")
except ZeroDivisionError:
    print("  ZeroDivisionError")

# Python flags nothing because an except with a general type is perfectly valid
# syntax: nobody can know by reading the file which exceptions the try will
# raise. Only at run time does it turn out that the bottom two never run, and
# finding that out takes somebody noticing that their message never appears.
```

### Exercise 4

```python
data = [1, 2, 3]

try:
    total = sum(datum)         # typo: datum, not data
    print(total)
except:
    print("The data file could not be read")

try:
    total = sum(datum)
    print(total)
except NameError as e:
    print("NameError:", e)
```

The first message talks about a file that was never opened. The second gives the exact missing name,
which is what you need in order to fix it.

### Exercise 5

```python
def divide_reporting(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("  cannot divide by zero")
    except TypeError as e:
        print("  incompatible types:", e)
    else:
        print("  result:", result)
    finally:
        print("  ---")


for a, b in [(10, 2), (10, 0), (10, "x")]:
    print(f"divide_reporting({a}, {b!r}):")
    divide_reporting(a, b)

# The finally ran three times, once per call. It does not care whether there was
# an exception, whether it was caught, or which one it was.
```

### Exercise 6

```python
items, text, divisor = [], "42", 0
student = {"name": "Ana"}

# 1. if. The list is right here and I can ask it for its length.
print(items[0] if items else "empty list")

# 2. try. A person typed it and it can be anything.
try:
    print(int(text))
except ValueError:
    print("not a number")

# 3. if. The divisor's value is in my hands before dividing.
print(10 / divisor if divisor != 0 else "divisor is zero")

# 4. if with get. The key is either there or not, and I can ask.
print(student.get("grant", "no grant"))

# 5. try. Between checking that it exists and opening it, the file can vanish.
try:
    with open("does_not_exist.txt") as f:
        print(f.read())
except FileNotFoundError as e:
    print("FileNotFoundError:", e.filename)

# 6. if. The sign of a number is checked with a comparison.
number = -9
print(number ** 0.5 if number >= 0 else "root of a negative")
```

The fifth is the interesting one. Asking whether the file exists and then opening it leaves a gap
between the two lines where another program can delete it. That is why files go with `try` even when
it looks like you could check first.

### Exercise 7

```python
ENTRIES = ["8", "9", "ten", "7", "", "10"]

# The version that hides.
valid = []
for entry in ENTRIES:
    try:
        valid.append(int(entry))
    except Exception:
        pass
print("With pass -> average", sum(valid) / len(valid))

# The version that reports.
valid, rejected = [], []
for entry in ENTRIES:
    try:
        valid.append(int(entry))
    except ValueError:
        rejected.append(entry)

print(f"Average: {sum(valid) / len(valid):.2f}")
print(f"Over {len(valid)} of {len(ENTRIES)} entries")
print("Rejected:", rejected)
```

Both print the same average. Only one says that two of the six entries never made it into the count.

### Exercise 8

```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError(f"The amount has to be positive, got {amount}")
    if amount > balance:
        raise ValueError(f"Insufficient funds: {balance} available, {amount} requested")
    return balance - amount


for amount in [500, -100, 5000]:
    try:
        print(f"Withdraw {amount}: {withdraw(1000, amount)} left")
    except ValueError as e:
        print(f"Withdraw {amount}: ValueError: {e}")
```

Both messages carry the numbers from the actual case. A message that just says "invalid amount" makes
you go and read the code to find out which of the two rules was broken.

### Exercise 9

```python
ENTRIES = ["8", "nine", "10", "", "7"]      # stands in for what gets typed


def compute_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


valid, rejected = [], []
for entry in ENTRIES:
    try:
        valid.append(float(entry))
    except ValueError:
        rejected.append(entry)

average = compute_average(valid)

if average is None:
    print("No valid grade was recorded.")
else:
    print(f"Average: {average:.2f}")
    print(f"Computed over {len(valid)} of {len(ENTRIES)} grades")

if rejected:
    print("Rejected:", rejected)
```

The three rubric items are kept apart on purpose. The `try` wraps one single line, the conversion. The
average lives in a function that takes and returns, printing nothing. And the `except` names
`ValueError`, which is the only thing `float` can raise on a string.

With a real `input`, the only line that changes is the one filling `ENTRIES`:

```python
ENTRIES = [input(f"Grade {i + 1}: ") for i in range(5)]
```

The rest of the program has no idea where the data came from, and that is precisely what makes it
testable without a keyboard.
"""),

]

write(OUT / "en" / "w01.5.ipynb", en)
print("wrote", OUT / "en" / "w01.5.ipynb")
