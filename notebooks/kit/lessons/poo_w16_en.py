"""notebooks/programacion-orientada-a-objetos/en/w16.ipynb

Source deck: ppts/python/programacion-orientada-a-objetos/en/w16.en.yaml
Source code:  docs/en/courses/python-course/04 - SQLite/8th Module/Code036.py
                  (sqlite3: connect, CREATE TABLE, INSERT with placeholders,
                   SELECT, WHERE, the foreign key and the INNER JOIN)
              docs/en/courses/python-course/03 - Paths and Files/7th Module/Code33.py
                  (the pixar_movies.json that Code036.py loads)

Code036.py is NOT run out of the repository: it writes pixar_movies.db inside
docs/. The notebook reproduces its code in the session's working directory,
which on Colab is /content.

DISCREPANCY WITH THE DECK, MEASURED. The "Quick question" slide of w16.en.yaml
claims this code prints (0,):

    with sqlite3.connect(path) as c:
        c.execute("INSERT INTO Movies VALUES (1, 'Up')")

    with sqlite3.connect(path) as c:
        cursor = c.execute("SELECT COUNT(*) FROM Movies")
        print(cursor.fetchone())

Measured on Python 3.14 / SQLite 3.50: it prints (1,). The sqlite3 context
manager DOES commit the transaction when the block is left without an exception;
what it does not do is close the connection. The slide has the two halves
swapped.

This is not a version detail. The Python documentation has always said so, in
library/sqlite3: "If the with block completes without exceptions, the transaction
is committed. If an exception occurs, the transaction is rolled back." and "The
context manager does not implicitly open new transactions or close the
connection."

The notebook teaches the measured behaviour, with all four combinations run side
by side:

    with that ends cleanly   -> commit, the row stays        (1,)
    with that raises inside  -> rollback, the row is dropped (0,)
    close() without commit   -> the row is dropped           (0,)
    after the with           -> the connection is still open and usable

Other measured things from the repository, quoted without correcting them:

  Code036.py lines 40 to 42 delete the .db file before every run. That deletion
  is the only reason the file can be run twice: CREATE TABLE IF NOT EXISTS
  survives a second run perfectly well, and what breaks is the second INSERT of
  the same id, which raises IntegrityError on the primary key. The comment on
  line 38 ("table already exists or repeated data") is therefore only half
  right; what actually happens is the second half.

  Code036.py lines 81 to 84 comment out a fetchall() and explain that it comes
  out empty because the cursor has already been walked. That is correct and
  worth measuring: an exhausted cursor returns [] and raises nothing.

  Code036.py line 141 uses a placeholder for the INNER JOIN title, which is the
  right thing, and line 96 pastes the year straight into the string. There is no
  risk there because 2010 is written by hand, but the habit is.

Weeks 14 and 15 had no notebook, because a PyQt6 window needs a screen and Colab
does not have one. The thread comes from week 13: there, to jump to record n of a
file whose records are different lengths, you would have to write an index by
hand. Here that index comes included.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import md, code, write, REPO

OUT = REPO / "notebooks" / "programacion-orientada-a-objetos"

en = [

md("""
# Object-Oriented Programming · Week 16
## Topic 7 · Databases and project

**COM102 · School of Engineering · Instructor David Escobar-Castillejos**

Storing data that gets searched, filtered and outlives the program. And the session where the whole
semester lands in one submission.

Week 13 closed on an open problem: to jump to record `n` of a file whose records are different lengths,
you have to keep a separate list saying which byte each one starts at. That is an index, and writing it by
hand is work. Here it comes included.

Weeks 14 and 15 were graphical interfaces and had no notebook, because a window needs a screen and Colab
has none. What can be tried out here is the architecture decision those two weeks left open, and block 3
tries it.

By the end you will be able to:

1. Choose between a file and a database by how the data will be queried, not by how many records there
   will be.
2. Create a table, insert with placeholders and query, knowing what `commit` does and what happens
   without it.
3. Explain what the `sqlite3` `with` commits and what it closes, with the four combinations measured.
4. Write a query with parameters and say exactly what that prevents.
5. Split the project into three pieces that get tested separately.

### How to use this notebook

Run the cells in order with **Shift + Enter**. Nine fail on purpose and carry a comment saying so.

Three of the nine **raise no exception at all**. One of them inserts a thousand rows, complains about
nothing, and leaves the database empty.

This notebook creates `.db` files in the session's working directory. It touches nothing in the
repository.
"""),

md("""
---
# Block 1 · Databases

A file stores data. A database stores data and also knows how to answer questions about it.

That difference is invisible with a hundred records and decides the whole program at a hundred thousand.
"""),

code("""
import csv
import sqlite3
import time
from pathlib import Path

N = 100_000
GENRES = ["Animation", "Adventure", "Comedy", "Drama"]

rows = [(i, f"Movie {i}", 1995 + i % 30, GENRES[i % 4]) for i in range(1, N + 1)]

# The same data, stored both ways
with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "title", "year", "genre"])
    w.writerows(rows)

Path("movies.db").unlink(missing_ok=True)
connection = sqlite3.connect("movies.db")
connection.execute("CREATE TABLE Movies (id INTEGER PRIMARY KEY, title TEXT, "
                   "year INTEGER, genre TEXT)")
connection.executemany("INSERT INTO Movies VALUES (?, ?, ?, ?)", rows)
connection.commit()

print("CSV:", f"{Path('movies.csv').stat().st_size:,}", "bytes")
print("DB: ", f"{Path('movies.db').stat().st_size:,}", "bytes")
print()

WANTED = 99_999

start = time.perf_counter()
with open("movies.csv", newline="", encoding="utf-8") as f:
    found = next(row for row in csv.DictReader(f)
                 if int(row["id"]) == WANTED)
with_file = time.perf_counter() - start

start = time.perf_counter()
found_db = connection.execute(
    "SELECT * FROM Movies WHERE id = ?", (WANTED,)).fetchone()
with_table = time.perf_counter() - start

print("From the CSV:", found)
print("From the DB: ", found_db)
print()
print(f"Searching the file:  {with_file:.5f} s")
print(f"Searching the table: {with_table:.6f} s")
print(f"The file took about {with_file / with_table:,.0f} times longer.")
connection.close()
"""),

md("""
The same hundred thousand records, the same answer, and a difference of hundreds of times that the cell
just measured in your own session.

In a file, searching means **reading all of it** until you find what you want. That is week 13's
sequential walk, and there is no way around it short of writing an index by hand.

In a table, searching means **asking**, and the engine decides how to get there. When the column is
`INTEGER PRIMARY KEY`, SQLite already has that index built and goes straight to the row without looking at
the others.

That is the only thing to take from this block: **the decision is not how many records you will have, it
is how you will query them.** If you are only going to store and read everything back, a file is enough.
The moment you have to search, filter or sort without reading it all, the table pays for itself.

## The three pieces of the model
"""),

code("""
# Code036.py, lines 44 to 55, with three movies
import sqlite3
from pathlib import Path

pixar_movies = [
    {"id": 1, "title": "Toy Story", "year": 1995},
    {"id": 19, "title": "Coco", "year": 2017},
    {"id": 25, "title": "Turning Red", "year": 2022},
]

database_file = Path("pixar_movies.db")
database_file.unlink(missing_ok=True)

with sqlite3.connect(database_file) as connection:
    create_command = ("CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, "
                      "title TEXT NOT NULL, year INTEGER NOT NULL)")
    connection.execute(create_command)

    for movie in pixar_movies:
        insert_command = "INSERT INTO Movies VALUES (?, ?, ?)"
        connection.execute(insert_command,
                           (movie["id"], movie["title"], movie["year"]))
    connection.commit()

with sqlite3.connect(database_file) as connection:
    for row in connection.execute("SELECT * FROM Movies ORDER BY title"):
        print(" ", row)
    print()
    print("Each row arrives as:", type(row).__name__)
    print("The columns of the table:")
    for col in connection.execute("PRAGMA table_info(Movies)"):
        print(f"   {col[1]:<8}{col[2]:<10}"
              f"{'NOT NULL' if col[3] else '':<10}"
              f"{'PRIMARY KEY' if col[5] else ''}")
connection.close()
"""),

md("""
Three pieces, and all three have an exact equivalent in what you have done this semester.

**One table per noun.** `Movies` holds movies and only movies. It is week 5's question when modelling a
class.

**One column per attribute, with its type.** `PRAGMA table_info` prints them with the type and the
constraints, which is the database's version of a type annotation.

**One primary key that identifies.** `id INTEGER PRIMARY KEY` is what tells one row apart from every
other, and it is what makes the search in the previous cell immediate.

Each row comes back as a **tuple**, which is week 10's container for a record that does not change. The
match is no accident.

## Running the file twice
"""),

code("""
# FAILS ON PURPOSE. What Code036.py avoids by deleting the .db on its line 42.
import sqlite3
from pathlib import Path

path = Path("twice.db")
path.unlink(missing_ok=True)

connection = sqlite3.connect(path)
connection.execute("CREATE TABLE IF NOT EXISTS Movies (id INTEGER PRIMARY KEY, "
                   "title TEXT NOT NULL)")
connection.execute("INSERT INTO Movies VALUES (?, ?)", (1, "Toy Story"))
connection.commit()
print("First run:", connection.execute("SELECT COUNT(*) FROM Movies").fetchone())

try:
    connection.execute("INSERT INTO Movies VALUES (?, ?)", (1, "Toy Story"))
except sqlite3.IntegrityError as e:
    print("Second run:", type(e).__name__ + ":", e)

print()
print("CREATE TABLE IF NOT EXISTS does survive the second run.")
print("The INSERT of the same id does not.")
print()
connection.execute("INSERT OR REPLACE INTO Movies VALUES (?, ?)", (1, "Toy Story"))
connection.commit()
print("With INSERT OR REPLACE:", connection.execute("SELECT * FROM Movies").fetchall())
connection.close()
"""),

md("""
`UNIQUE constraint failed: Movies.id`.

`Code036.py` deletes the `.db` file before every run, in its lines 40 to 42, and its comment says it is to
avoid *"an error of 'table already exists' or repeated data"*. The first half is not true:
`CREATE TABLE IF NOT EXISTS` survives the second run perfectly well. The one that breaks is the second,
the `INSERT` of the same `id`.

That constraint is what makes a primary key useful: **the engine refuses to store two rows with the same
identity**, and it refuses on the line that tries, not three screens later.

Deleting the whole database so the program can be run again works in a classroom example and is not what
gets done. `INSERT OR REPLACE` updates what was already there, and it is the operation you actually
wanted.
"""),

md("""
---
# Block 2 · Access and queries

A connection is opened, used and closed. It is week 12's file life cycle, with one extra trap called
`commit`.

## Predict before you run

```python
with sqlite3.connect(path) as c:
    c.execute("INSERT INTO Movies VALUES (1, 'Up')")

with sqlite3.connect(path) as c:
    cursor = c.execute("SELECT COUNT(*) FROM Movies")
    print(cursor.fetchone())
```

- **A.** `(1,)`, because the `with` commits on the way out.
- **B.** `(0,)`, because `commit` was never called.
- **C.** An error, the connection was already closed.
- **D.** `(1,)`, because `sqlite3` saves every `INSERT` at once.
"""),

code("""
import sqlite3
from pathlib import Path

path = Path("prediction.db")


def clean_database():
    path.unlink(missing_ok=True)
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE Movies (id INTEGER PRIMARY KEY, title TEXT)")
    c.commit()
    c.close()


def how_many():
    c = sqlite3.connect(path)
    n = c.execute("SELECT COUNT(*) FROM Movies").fetchone()
    c.close()
    return n


clean_database()
with sqlite3.connect(path) as c:
    c.execute("INSERT INTO Movies VALUES (1, 'Up')")
c.close()

print("Result:", how_many())
"""),

md("""
The answer is **A**, and it is not the one most people give.

The `sqlite3` context manager **commits the transaction** when the block is left without an exception.
That is what the cell just printed, and it is what the Python documentation says, in `library/sqlite3`,
in these words: *"If the `with` block completes without exceptions, the transaction is committed"*, and
two lines later, *"The context manager does not implicitly open new transactions or close the
connection"*.

What the `with` does **not** do is close the connection. That is where the real trap is, and it is exactly
the other way round from how it sounds: it is like a file's `with` in that it protects the work, and
different in that it does not release the resource.

The four combinations, run side by side, are in the next cell.
"""),

code("""
import sqlite3

print(f"{'situation':<38}{'rows on disk':>16}")

# 1. with, no exception, no explicit commit
clean_database()
with sqlite3.connect(path) as c:
    c.execute("INSERT INTO Movies VALUES (1, 'Up')")
c.close()
print(f"{'with that ends cleanly':<38}{str(how_many()):>16}")

# 2. with, an exception raised inside
clean_database()
try:
    with sqlite3.connect(path) as c:
        c.execute("INSERT INTO Movies VALUES (1, 'Up')")
        raise ValueError("something went wrong mid-transaction")
except ValueError:
    pass
c.close()
print(f"{'with that raises inside':<38}{str(how_many()):>16}")

# 3. no with, with commit
clean_database()
c = sqlite3.connect(path)
c.execute("INSERT INTO Movies VALUES (1, 'Up')")
c.commit()
c.close()
print(f"{'no with, with commit':<38}{str(how_many()):>16}")

# 4. no with, no commit
clean_database()
c = sqlite3.connect(path)
c.execute("INSERT INTO Movies VALUES (1, 'Up')")
c.close()
print(f"{'no with, no commit':<38}{str(how_many()):>16}")
"""),

md("""
Four combinations, two results, and a rule that comes out on its own.

**A transaction ends one of two ways: committed or discarded.** The `with` commits when the block ended
cleanly and discards when an exception came out of it. Without `with`, the commit has to be written, and
closing without having written it discards.

Row four is error 01 from the slide in its real form: the `INSERT`s ran, the program did not complain, and
reopening the database shows nothing.

Row two is the same result for the opposite reason, and it is a **good** property: if the program breaks
halfway through a load, you are not left with fifty of the hundred movies that were going in. Either they
all go in or none does.

## A thousand rows and an empty database
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. A thousand inserts and no commit.
import sqlite3

clean_database()

connection = sqlite3.connect(path)
for i in range(1, 1001):
    connection.execute("INSERT INTO Movies VALUES (?, ?)", (i, f"Movie {i}"))

print("What the connection sees before closing:",
      connection.execute("SELECT COUNT(*) FROM Movies").fetchone())
connection.close()

print("What is on disk afterwards:             ", how_many())
print()
print("No exception, no warning, and a thousand rows that do not exist.")
print()

clean_database()
connection = sqlite3.connect(path)
connection.executemany("INSERT INTO Movies VALUES (?, ?)",
                       [(i, f"Movie {i}") for i in range(1, 1001)])
connection.commit()
connection.close()
print("With commit:", how_many())
"""),

md("""
The same connection that inserted the thousand rows sees them. Nobody else does.

An uncommitted transaction lives inside the session that opened it. That is why the first query returns a
thousand and the second, from another connection and after closing, returns zero. **The checking `SELECT`
from the same connection checks nothing**, and that is why this error survives so long.

Look at `executemany` as well. It sends the thousand inserts in one go and it is the right form when the
data comes from a list, which is exactly what `Code036.py`'s loop does one at a time in its lines 48 to 53.

## The connection that stayed open
"""),

code("""
# FAILS ON PURPOSE. The sqlite3 with closes nothing.
import sqlite3
from pathlib import Path

clean_database()

with sqlite3.connect(path) as c:
    c.execute("INSERT INTO Movies VALUES (1, 'Up')")

print("Is the connection still alive after the with?")
print("  ", c.execute("SELECT COUNT(*) FROM Movies").fetchone(), "<- yes, it answered")
print()

c.close()
print("After close():")
try:
    c.execute("SELECT COUNT(*) FROM Movies")
except sqlite3.ProgrammingError as e:
    print("  ProgrammingError:", e)

print()
print("The form that really closes:")
with sqlite3.connect(path) as connection:
    connection.execute("INSERT OR REPLACE INTO Movies VALUES (2, 'Coco')")
connection.close()
print("  rows:", how_many(), " closed?", True)
"""),

md("""
The `with` was left, the transaction was committed, and the connection stayed open and answering.

This is not a matter of style. An open connection keeps a file open, and on Windows an open file **cannot
be deleted or moved**. A program that opens one connection per operation and never closes any runs out of
descriptors in a few hours.

The complete form is the one in the last lines: `with` for the transaction and `close()` for the resource.
If you want a single block to do both, there is `contextlib.closing`, and in a project the usual thing is
a class that opens in its constructor and closes in a `close` method.

## The cursor that stopped working
"""),

code("""
# FAILS ON PURPOSE. Keeping the cursor for later.
import sqlite3

clean_database()
c = sqlite3.connect(path)
c.executemany("INSERT INTO Movies VALUES (?, ?)",
              [(1, "Up"), (2, "Coco"), (3, "Luca")])
c.commit()

cursor = c.execute("SELECT * FROM Movies ORDER BY title")
c.close()

try:
    print(cursor.fetchall())
except sqlite3.ProgrammingError as e:
    print("ProgrammingError:", e)

print()
print("The right thing is to take the data out before closing:")
c = sqlite3.connect(path)
rows = c.execute("SELECT * FROM Movies ORDER BY title").fetchall()
c.close()
print(" ", rows)
print("  type:", type(rows).__name__, "of", type(rows[0]).__name__)
"""),

md("""
`Cannot operate on a closed database.`

It is error 04 from the slide. **A cursor does not carry the rows: it points at them.** While the
connection is alive it hands them over; the moment it closes, the cursor stops working and the error turns
up far from where it was caused, which is what makes it expensive.

The fix is one word: `fetchall()` before closing. What it returns is a list of tuples, which by then is an
ordinary Python object and survives anything.

That `fetchall` is also the boundary week 11 talked about. What comes out of the database enters the
program once, in one place, and from there on it is Python structures.

## The cursor that has already been walked
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. Code036.py, lines 81 to 84.
import sqlite3

c = sqlite3.connect(path)
cursor = c.execute("SELECT * FROM Movies ORDER BY title")

for row in cursor:
    print(" ", row)

fetched = cursor.fetchall()
print()
print("And now fetchall() returns:", fetched)
print("With no error at all, and the table full:",
      c.execute("SELECT COUNT(*) FROM Movies").fetchone())
print()
print("It is week 10's generator again: it gets walked once.")
c.close()
"""),

md("""
The `for` consumed the cursor and `fetchall()` returned an empty list.

`Code036.py` documents it in its lines 83 and 84 and is entirely right: *"as we have already iterated
through the cursor, it is empty"*. It is worth measuring because the empty list comes with no warning at
all, and whoever receives that `[]` will conclude the table has no data.

It is exactly week 10's exhausted generator under another name. **What is produced while it is walked gets
walked once.**

## Gluing the value inside the query
"""),

code("""
# FAILS ON PURPOSE. A title with a quote in it breaks the query.
import sqlite3

clean_database()
c = sqlite3.connect(path)
c.executemany("INSERT INTO Movies VALUES (?, ?)",
              [(1, "Up"), (2, "Coco"), (3, "O'Brien")])
c.commit()

wanted = "O'Brien"

bad = "SELECT * FROM Movies WHERE title = '" + wanted + "'"
print("The query that got built:", bad)
try:
    print(c.execute(bad).fetchall())
except sqlite3.OperationalError as e:
    print("  OperationalError:", e)

print()
print("With a placeholder:", c.execute(
    "SELECT * FROM Movies WHERE title = ?", (wanted,)).fetchall())
c.close()
"""),

md("""
An apostrophe in the data and the query stopped being a query.

The quote in the data closed the SQL string early, and what came after it became syntax. The engine has no
way of knowing that apostrophe was part of a surname: it received text and read it as text.

With a placeholder, the value is **never read as SQL**. It travels separately, in a tuple, and the engine
puts it where the question mark is already knowing it is data.

And now the version that is not an accident.
"""),

code("""
# FAILS ON PURPOSE. The same thing, typed in on purpose by whoever is at the keyboard.
import sqlite3

c = sqlite3.connect(path)

wanted = input("Title: ") if False else "x' OR '1'='1"

bad = f"SELECT * FROM Movies WHERE title = '{wanted}'"
print("What somebody typed:", repr(wanted))
print("The query it left:  ", bad)
print()
print("It returns the whole table:")
for row in c.execute(bad):
    print(" ", row)

print()
print("With a placeholder, the same thing typed in:")
print(" ", c.execute("SELECT * FROM Movies WHERE title = ?",
                     (wanted,)).fetchall())
print("  <- no movie is called that, and that is exactly right")
c.close()
"""),

md("""
They asked for a movie and were handed the whole table.

`x' OR '1'='1` closes the quote, adds an `OR` that is always true, and leaves a loose quote that pairs
with the one the program was going to put at the end. The `WHERE` condition stops filtering.

It is error 02 from the slide and it is called **SQL injection**. With a `SELECT` the consequence is that
somebody sees data that was not theirs; with a `DELETE` or an `UPDATE`, the consequence is worse.

The fix is not escaping the quotes by hand, nor checking that the text carries no odd characters. It is
the placeholder, always, with no exceptions, and also when the data "comes from inside", because today's
inside data is tomorrow's input field.

## The comma that turns brackets into a tuple
"""),

code("""
# FAILS ON PURPOSE. The one-item tuple, without its comma.
import sqlite3

c = sqlite3.connect(path)

print('type(("Coco")) is', type(("Coco")).__name__, "<- just brackets")
print('type(("Coco",)) is', type(("Coco",)).__name__, "<- now it is")
print()

try:
    c.execute("SELECT * FROM Movies WHERE title = ?", ("Coco"))
except sqlite3.ProgrammingError as e:
    print("Without the comma:", type(e).__name__)
    print(" ", e)

print()
print("With the comma:", c.execute(
    "SELECT * FROM Movies WHERE title = ?", ("Coco",)).fetchall())
c.close()
"""),

md("""
`Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.`

Four, because `"Coco"` has four letters. Without the comma, the brackets do not create a tuple: they group
an expression, the same as in arithmetic. What arrived was the string, and `sqlite3` walked it character
by character looking for parameters.

**The comma is what makes the tuple, not the brackets.** It is true everywhere in Python and here it gets
charged on the first query with a single parameter anyone writes.

## Relating two tables
"""),

code("""
# Code036.py, lines 117 to 144: the foreign key and the INNER JOIN
import sqlite3
from pathlib import Path

join_path = Path("join.db")
join_path.unlink(missing_ok=True)

movie_viewers = [
    {"id": 1, "movie_id": 1, "name": "Ana", "last_name": "Robles"},
    {"id": 2, "movie_id": 1, "name": "Luis", "last_name": "Ferrer"},
    {"id": 3, "movie_id": 19, "name": "Sofia", "last_name": "Ines"},
]

with sqlite3.connect(join_path) as connection:
    connection.execute("CREATE TABLE Movies (id INTEGER PRIMARY KEY, "
                       "title TEXT NOT NULL, year INTEGER NOT NULL)")
    connection.executemany("INSERT INTO Movies VALUES (?, ?, ?)",
                           [(1, "Toy Story", 1995), (19, "Coco", 2017)])
    connection.execute(
        "CREATE TABLE IF NOT EXISTS MovieViewers (id INTEGER PRIMARY KEY, "
        "movie_id INTEGER NOT NULL, name TEXT NOT NULL, last_name TEXT NOT NULL, "
        "FOREIGN KEY (movie_id) REFERENCES Movies(id))")
    for viewer in movie_viewers:
        connection.execute("INSERT INTO MovieViewers VALUES (?, ?, ?, ?)",
                           (viewer["id"], viewer["movie_id"], viewer["name"],
                            viewer["last_name"]))
    connection.commit()

movie_title = "Toy Story"
with sqlite3.connect(join_path) as connection:
    select_command = ("SELECT Movies.title, MovieViewers.name, MovieViewers.last_name "
                      "FROM Movies INNER JOIN MovieViewers "
                      "ON Movies.id = MovieViewers.movie_id "
                      "WHERE Movies.title = ?")
    for row in connection.execute(select_command, (movie_title,)):
        print(" ", row)
connection.close()
"""),

md("""
Two tables, one foreign key, and a query that puts them together.

`movie_id INTEGER NOT NULL, FOREIGN KEY (movie_id) REFERENCES Movies(id)` says that column holds a movie's
`id`. It is week 6's composition relationship, written in the table instead of in the object.

`INNER JOIN ... ON` is the operation that follows it: it takes the rows of both tables where the foreign
key matches the primary one. What comes out is one row per viewer with the title attached.

Notice that the title goes through a placeholder, as it should. `Code036.py` gets that right in its line
142.
"""),

md("""
---
# Block 3 · The integrating project

The submission that pulls the seven units together. Code and report are both marked, and the code carries
more than twice the weight.

**The four pieces.** Object-oriented modelling, persistence, graphical interface and written report.

**How to split it.** Start with the domain classes, no window and no database. Once those run from a
terminal, everything after that is connecting wires.

The cell below is that whole architecture, in miniature and running.
"""),

code("""
import sqlite3
from pathlib import Path


# ── Layer 1: the domain. It imports neither sqlite3 nor PyQt6.
class Loan:
    def __init__(self, student_id: str, title: str, days: int = 14) -> None:
        if not student_id.strip():
            raise ValueError("the student id cannot be empty")
        if days <= 0:
            raise ValueError(f"the days must be positive, got {days}")
        self.student_id = student_id.strip()
        self.title = title
        self.days = days

    @property
    def fine(self) -> float:
        return max(0, self.days - 14) * 12.50

    def __repr__(self) -> str:
        return f"Loan({self.student_id!r}, {self.title!r}, {self.days})"


# ── Layer 2: persistence. All the SQL lives here and nowhere else.
class LoanRepository:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.execute(
            "CREATE TABLE IF NOT EXISTS Loans ("
            "student_id TEXT NOT NULL, title TEXT NOT NULL, days INTEGER NOT NULL, "
            "PRIMARY KEY (student_id, title))")
        self.connection.commit()

    def save(self, loan):
        self.connection.execute(
            "INSERT OR REPLACE INTO Loans VALUES (?, ?, ?)",
            (loan.student_id, loan.title, loan.days))
        self.connection.commit()

    def for_student(self, student_id):
        rows = self.connection.execute(
            "SELECT student_id, title, days FROM Loans WHERE student_id = ?",
            (student_id,)).fetchall()
        return [Loan(s, t, d) for s, t, d in rows]

    def close(self):
        self.connection.close()


# The domain gets tested with no database and no window
p = Loan("A001", "Don Quixote", 20)
print("Without touching the disk:", p, " fine:", p.fine)
print("On time:", Loan("A002", "Hopscotch", 10).fine)
try:
    Loan("  ", "The Aleph")
except ValueError as e:
    print("And it validates:", e)

print()
Path("library.db").unlink(missing_ok=True)
repo = LoanRepository("library.db")
for loan in [p, Loan("A001", "Hopscotch", 30), Loan("A002", "Aura", 7)]:
    repo.save(loan)

recovered = repo.for_student("A001")
print("Recovered from the database:", recovered)
print("Did they come back as domain objects?",
      all(isinstance(x, Loan) for x in recovered))
print("Total fine for A001:", sum(x.fine for x in recovered))
repo.close()
"""),

md("""
Two classes, two responsibilities, and neither knows more about the other than it has to.

`Loan` does not import `sqlite3`. It gets built, validates in the constructor like week 11, works out the
fine with a property like week 5, and gets tested from the console without a database existing.

`LoanRepository` is the only class that writes SQL. Every query in the project passes through here, and
that is why changing one column gets fixed in one file. Look at `for_student()`: it receives rows and
**returns domain objects**, so the rest of the program never sees a tuple.

What is missing is the third layer, the window, and its rule fits on one line: **a slot reads the
controls, calls these two classes, and shows the result.** Nothing else. If a slot works out a fine, the
fine has become impossible to test.

## SQL scattered across the window
"""),

code("""
# FAILS ON PURPOSE, and nothing is raised. The same query written in four places.
import sqlite3
from pathlib import Path

path = Path("scattered.db")
path.unlink(missing_ok=True)
c = sqlite3.connect(path)
c.execute("CREATE TABLE Loans (student_id TEXT, title TEXT, days INTEGER)")
c.executemany("INSERT INTO Loans VALUES (?, ?, ?)",
              [("A001", "Don Quixote", 20), ("A002", "Hopscotch", 10)])
c.commit()

# Four slots of the window, each with its own SELECT
SLOTS = {
    "on_search": "SELECT student_id, title FROM Loans WHERE student_id = ?",
    "on_list":   "SELECT student_id, title, days FROM Loans",
    "on_count":  "SELECT COUNT(*) FROM Loans WHERE student_id = ?",
    "on_export": "SELECT title, days FROM Loans ORDER BY title",
}

print("With the table as it is:")
for name, sql in SLOTS.items():
    parameters = ("A001",) if "?" in sql else ()
    print(f"  {name:<14}ok  {c.execute(sql, parameters).fetchall()[:1]}")

# Tomorrow somebody renames a column
c.execute("ALTER TABLE Loans RENAME COLUMN days TO loan_days")
c.commit()

print()
print("After renaming the 'days' column:")
broken = 0
for name, sql in SLOTS.items():
    parameters = ("A001",) if "?" in sql else ()
    try:
        c.execute(sql, parameters).fetchall()
        print(f"  {name:<14}still works")
    except sqlite3.OperationalError as e:
        broken += 1
        print(f"  {name:<14}broken: {e}")

print()
print(f"{broken} of {len(SLOTS)} slots broke, and they have to be found one by one.")
c.close()
"""),

md("""
One change to the table and two broken slots, in two different files.

It is error 03 from the slide. SQL scattered across the interface turns any change to the model into a
hunt: you have to open the whole project and search for the word `days`, with the risk that some query
lives inside a string built in pieces and never turns up in the search.

With the data access layer from the previous example, that same change touches **one file**, and the slots
never find out, because they receive `Loan` objects and not tuples.

Notice as well that the two slots that survived did so by accident: they did not mention the column.
**A change not breaking everything does not mean the design holds; it means you got lucky this time.**
"""),

md("""
---
## Four errors from this session

**Forgetting the `commit`.** The `INSERT`s run, the connection that made them sees them, and closing
without committing throws them away. The checking `SELECT` from the same connection checks nothing.

**Gluing values in with f-strings.** An apostrophe breaks the query and a string written on purpose turns
it into a different one. The placeholder keeps data as data.

**SQL scattered across the window.** Changing one column means auditing the whole project. All the SQL
lives in one class.

**Keeping a cursor for later.** Once the connection closes the cursor is dead, and a cursor already walked
returns an empty list without complaining.
"""),

md("""
---
# Exercises

This week's lab is turning two of your project's classes into tables. The exercises build towards it.

The solutions are at the very bottom of the notebook.

### Exercise 1 · File against table

Store ten thousand records in a CSV and in a table with a primary key. Search for the last one both ways
and measure with `time.perf_counter`.

Explain in a comment why the difference grows with the number of records.

### Exercise 2 · The primary key

Create a table with `id INTEGER PRIMARY KEY` and insert the same `id` twice. Catch the `IntegrityError`
and print its message.

Repeat it with `INSERT OR REPLACE` and show how many rows were left.

### Exercise 3 · The four combinations

Write the four situations from block 2's table and check each one from a fresh connection. Print a table
with the result.

### Exercise 4 · The cursor

Run a `SELECT`, walk the cursor with a `for` and then call `fetchall()`. Print what it returns.

Then close the connection before calling `fetchall()` and catch the `ProgrammingError`.

### Exercise 5 · The placeholder

Insert a title carrying an apostrophe. Search for it gluing the data into the string and with a
placeholder, and show what happens in each case.

Try the text `x' OR '1'='1` as well.

### Exercise 6 · The tuple of one

Run a query with one parameter passing `("Coco")` and `("Coco",)`. Catch the first one's error and explain
in a comment how many parameters `sqlite3` thought it had received.

### Exercise 7 · Two tables

Model `Student` and `Enrolment` with a foreign key. Insert three students and five enrolments, and write
an `INNER JOIN` listing the student's name and the subject.

### Exercise 8 · The access layer

Take one class from your project and write its repository: a class with `save`, `for_student` and `close`,
where all the SQL lives inside and the methods return domain objects, never tuples.

### Exercise 9 · The lab

In pairs, take two classes from your project and write the `CREATE TABLE` each of them needs, plus the
`save` and `load` methods turning them into rows and back.

Constraints: all the SQL lives in one data access class, and nothing else writes any.

You hand in a `.py` file with the classes and a test script that saves, closes, reopens and recovers. The
criterion is that the domain classes still run without importing `sqlite3` or `PyQt6`.
"""),

md("""
---
## Three things to take away

**A table answers, a file only stores.** The difference shows up once you have to search, filter or sort
without reading it all, and it does not depend on how many records there are.

**The `sqlite3` `with` commits the transaction and does not close the connection.** It is the other way
round from how it sounds. Closing without committing throws away what was pending, and an exception inside
the block does too, which in that case is what you want.

**Values travel as parameters.** The placeholder keeps data as data, and a quote loses its power to change
the query. With the comma in place, which is what makes the tuple.

Week 17 is the last one: general review and the final integrating exam. A single question can touch
modelling, files and persistence at the same time, so the closing notebook goes back over the errors that
cost the most marks in the two mid-terms.
"""),

md("""
---
# Solutions

### Exercise 1

```python
import csv, sqlite3, time
from pathlib import Path

N = 10_000
rows = [(i, f"record {i}") for i in range(1, N + 1)]

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(rows)

Path("data.db").unlink(missing_ok=True)
c = sqlite3.connect("data.db")
c.execute("CREATE TABLE R (id INTEGER PRIMARY KEY, text TEXT)")
c.executemany("INSERT INTO R VALUES (?, ?)", rows)
c.commit()

start = time.perf_counter()
with open("data.csv", newline="", encoding="utf-8") as f:
    last = [row for row in csv.reader(f) if int(row[0]) == N][0]
print(f"file:  {time.perf_counter() - start:.5f} s")

start = time.perf_counter()
c.execute("SELECT * FROM R WHERE id = ?", (N,)).fetchone()
print(f"table: {time.perf_counter() - start:.6f} s")
c.close()

# Searching the file compares against every record, so its cost grows with N.
# The table's search uses the primary key's index and reaches the row without
# walking, so its cost barely moves.
```

### Exercise 2

```python
import sqlite3
from pathlib import Path

Path("key.db").unlink(missing_ok=True)
c = sqlite3.connect("key.db")
c.execute("CREATE TABLE M (id INTEGER PRIMARY KEY, t TEXT)")
c.execute("INSERT INTO M VALUES (1, 'Up')")

try:
    c.execute("INSERT INTO M VALUES (1, 'Coco')")
except sqlite3.IntegrityError as e:
    print("IntegrityError:", e)

c.execute("INSERT OR REPLACE INTO M VALUES (1, 'Coco')")
c.commit()
print(c.execute("SELECT COUNT(*) FROM M").fetchone())
print(c.execute("SELECT * FROM M").fetchall())
c.close()
```

### Exercise 3

```python
import sqlite3
from pathlib import Path

path = Path("four.db")


def clean():
    path.unlink(missing_ok=True)
    c = sqlite3.connect(path)
    c.execute("CREATE TABLE M (id INTEGER PRIMARY KEY)")
    c.commit()
    c.close()


def how_many():
    c = sqlite3.connect(path)
    n = c.execute("SELECT COUNT(*) FROM M").fetchone()[0]
    c.close()
    return n


clean()
with sqlite3.connect(path) as c:
    c.execute("INSERT INTO M VALUES (1)")
c.close()
print("with that ends cleanly:", how_many())

clean()
try:
    with sqlite3.connect(path) as c:
        c.execute("INSERT INTO M VALUES (1)")
        raise ValueError()
except ValueError:
    pass
c.close()
print("with an exception:     ", how_many())

clean()
c = sqlite3.connect(path)
c.execute("INSERT INTO M VALUES (1)")
c.commit()
c.close()
print("no with, with commit:  ", how_many())

clean()
c = sqlite3.connect(path)
c.execute("INSERT INTO M VALUES (1)")
c.close()
print("no with, no commit:    ", how_many())
```

### Exercise 4

```python
import sqlite3

c = sqlite3.connect("four.db")
c.execute("INSERT OR REPLACE INTO M VALUES (1)")
c.commit()

cur = c.execute("SELECT * FROM M")
for row in cur:
    print(row)
print("fetchall after the for:", cur.fetchall())

cur = c.execute("SELECT * FROM M")
c.close()
try:
    cur.fetchall()
except sqlite3.ProgrammingError as e:
    print("ProgrammingError:", e)
```

### Exercise 5

```python
import sqlite3
from pathlib import Path

Path("quotes.db").unlink(missing_ok=True)
c = sqlite3.connect("quotes.db")
c.execute("CREATE TABLE P (title TEXT)")
c.executemany("INSERT INTO P VALUES (?)", [("Up",), ("O'Brien",)])
c.commit()

for wanted in ["O'Brien", "x' OR '1'='1"]:
    sql = "SELECT * FROM P WHERE title = '" + wanted + "'"
    try:
        print("glued:      ", c.execute(sql).fetchall())
    except sqlite3.OperationalError as e:
        print("glued:      ", type(e).__name__, e)
    print("placeholder:", c.execute(
        "SELECT * FROM P WHERE title = ?", (wanted,)).fetchall())
c.close()
```

### Exercise 6

```python
import sqlite3

c = sqlite3.connect("quotes.db")
try:
    c.execute("SELECT * FROM P WHERE title = ?", ("Up"))
except sqlite3.ProgrammingError as e:
    print(e)
print(c.execute("SELECT * FROM P WHERE title = ?", ("Up",)).fetchall())
c.close()

# sqlite3 thought it had received two parameters, one per letter of "Up",
# because without the comma what arrived was the string, and a string is
# iterable.
```

### Exercise 7

```python
import sqlite3
from pathlib import Path

Path("school.db").unlink(missing_ok=True)
c = sqlite3.connect("school.db")
c.execute("CREATE TABLE Student (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
c.execute("CREATE TABLE Enrolment (id INTEGER PRIMARY KEY, "
          "student_id INTEGER NOT NULL, subject TEXT NOT NULL, "
          "FOREIGN KEY (student_id) REFERENCES Student(id))")

c.executemany("INSERT INTO Student VALUES (?, ?)",
              [(1, "Ana Robles"), (2, "Luis Ferrer"), (3, "Sofia Ines")])
c.executemany("INSERT INTO Enrolment VALUES (?, ?, ?)",
              [(1, 1, "COM102"), (2, 1, "COM101"), (3, 2, "COM102"),
               (4, 3, "COM103"), (5, 3, "COM102")])
c.commit()

for row in c.execute(
        "SELECT Student.name, Enrolment.subject FROM Student "
        "INNER JOIN Enrolment ON Student.id = Enrolment.student_id "
        "ORDER BY Student.name, Enrolment.subject"):
    print(row)
c.close()
```

### Exercises 8 and 9

```python
import sqlite3


class Student:
    \"\"\"Pure domain: it does not import sqlite3 and runs from the console.\"\"\"

    def __init__(self, student_id: str, name: str, average: float = 0.0) -> None:
        if not student_id.strip():
            raise ValueError("the student id cannot be empty")
        if not 0 <= average <= 10:
            raise ValueError(f"the average must run from 0 to 10, got {average}")
        self.student_id = student_id.strip()
        self.name = name
        self.average = average

    @property
    def passing(self) -> bool:
        return self.average >= 7

    def __repr__(self) -> str:
        return f"Student({self.student_id!r}, {self.name!r}, {self.average})"


class StudentRepository:
    \"\"\"The only class in the project that writes SQL.\"\"\"

    CREATE = ("CREATE TABLE IF NOT EXISTS Students ("
              "student_id TEXT PRIMARY KEY, name TEXT NOT NULL, "
              "average REAL NOT NULL)")

    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.connection.execute(self.CREATE)
        self.connection.commit()

    def save(self, student):
        self.connection.execute(
            "INSERT OR REPLACE INTO Students VALUES (?, ?, ?)",
            (student.student_id, student.name, student.average))
        self.connection.commit()

    def load(self, student_id):
        row = self.connection.execute(
            "SELECT student_id, name, average FROM Students WHERE student_id = ?",
            (student_id,)).fetchone()
        return Student(*row) if row else None

    def all_students(self):
        return [Student(*r) for r in self.connection.execute(
            "SELECT student_id, name, average FROM Students ORDER BY student_id")]

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    from pathlib import Path

    Path("school2.db").unlink(missing_ok=True)

    # The domain, with no disk
    ana = Student("A001", "Ana Robles", 9.2)
    print(ana, ana.passing)

    # Save, close, reopen and recover
    repo = StudentRepository("school2.db")
    repo.save(ana)
    repo.save(Student("A002", "Luis Ferrer", 6.4))
    repo.close()

    repo = StudentRepository("school2.db")
    print(repo.load("A001"))
    print(repo.all_students())
    print("Passing:", [s.student_id for s in repo.all_students() if s.passing])
    repo.close()
```

Three decisions worth defending when you hand this in.

**`Student` does not import `sqlite3`.** It gets built, validates and calculates from the console. If the
project moves from SQLite to a JSON file tomorrow, this class is not touched.

**`load` and `all_students` return domain objects, never tuples.** That is the whole point of the layer:
the boundary converts once, and inward there is only `Student`.

**The `CREATE TABLE` is a class constant.** It is written once, it is read in the same file as the
queries, and when a column has to be added there is one place to look.
"""),

]

write(OUT / "en" / "w16.ipynb", en)
print("wrote", OUT / "en" / "w16.ipynb")
