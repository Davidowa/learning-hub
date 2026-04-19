# 04 · SQLite

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/database.svg" width="32" height="32" alt="">

A real **database** (organized, queryable data store) — lives inside a single file, ships with Python, no server to install.

## What you'll learn

- **Relational databases** — data organized into tables with rows and columns; tables linked by keys.
- **SQL basics** — `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, `JOIN`.
- **Python + SQLite** — `sqlite3` module: connections, cursors, `execute()`, `fetchall()`.
- **Parameterized queries** — always use `?` placeholders, never string-format SQL (prevents **SQL injection**, a security vulnerability where user input becomes executable SQL).
- **Transactions** — grouping changes so either all succeed or none do.
- Schema design — primary keys, foreign keys, indexes.

## Plain-language analogy

A database table is a **filing cabinet**: each drawer is a table, each folder a row, each tab a column. SQL is the librarian you ask to "bring me every student whose grade is above 8".

## Security: never do this

```python
# DANGEROUS — user input becomes SQL:
cur.execute(f"SELECT * FROM users WHERE name = '{name}'")

# SAFE — parameterized:
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
```

The second form treats `name` as data, not code. This matters.

## Source code

[`courses/python-course/04 - SQLite/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/04%20-%20SQLite)
