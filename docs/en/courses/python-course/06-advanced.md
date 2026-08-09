# 06 · Advanced

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/rocket.svg" width="32" height="32" alt="">

Features that separate "I can write Python" from "I can write **Pythonic**, efficient, maintainable Python".

## What you'll learn

- **Decorators** — functions that wrap other functions to add behavior (logging, timing, caching) without changing them. Think of it as a wrapping paper that adds features.
- **Generators** (`yield`) — produce values one at a time, lazily. Memory-friendly for huge datasets.
- **Context managers** (`with` / `__enter__` / `__exit__`) — automatic setup and cleanup. You already use them with `open()`; now learn to write your own.
- **Iterators and iterables** — what actually powers `for` loops.
- **Comprehensions** — compact syntax for building lists, dicts, sets, generators.
- **Typing** — optional type hints (`def add(a: int, b: int) -> int:`) that catch bugs early and document intent.
- **Async / await** — concurrent I/O without threads. For network calls, disk reads, UI responsiveness.
- **Testing** — `pytest`, fixtures, parametrization.

## Plain-language analogy

If basic Python is cooking one dish at a time, advanced Python is running a restaurant kitchen — decorators are the sous chefs who plate every dish the same way, generators are the conveyor belt serving plates only when a diner sits down, and async is juggling the grill, fryer, and oven so none sits idle.

## Working with data

Three modules on turning a file of records into an answer somebody can act on. They are written for readers who already do this work in a spreadsheet, so every idea is introduced next to the spreadsheet feature it replaces.

| Module | What it covers |
|---|---|
| `A04 - Tabular Data` | Reading a CSV with the standard library, and summarising it by hand with dictionaries. Eighty lines that make the next module obvious. |
| `A05 - Pandas` | Series and DataFrames, loading and inspecting, selecting and filtering, cleaning, grouping and aggregating, joining and exporting. |
| `A06 - Data Visualization` | matplotlib's figure and axes, which chart answers which question, labels and accessibility, and the seaborn one-liners. |

The mapping worth keeping in mind:

| In the spreadsheet | In pandas |
|---|---|
| A column | A `Series` |
| The sheet | A `DataFrame` |
| `SUM`, `AVERAGE`, `COUNT` | `.sum()`, `.mean()`, `.count()` |
| AutoFilter | A boolean mask |
| A PivotTable | `.groupby()` and `.pivot_table()` |
| `VLOOKUP` | `.merge()` |
| Insert chart | matplotlib and seaborn |

### The data

`06 - Advanced/data/` holds three CSV files. The sales table is deliberately dirty, and each defect exists to teach one cleaning step: rows captured twice, blank cells, a region name typed four different ways, and a price stored as `$ 2,082.50` rather than as a number. `make_datasets.py` rebuilds all three from a fixed seed, so the numbers never drift from what a lesson quotes.

### Installing

`A04` needs nothing beyond the standard library. The other two need three packages:

```console
pip install pandas matplotlib seaborn
```

Writing the Excel report at the end of `06_merge_and_export.py` also needs `openpyxl`. The script skips that step and says so if the package is missing.

Everything here was checked against **pandas 3.0**, where two defaults changed: Copy-on-Write is always on, so chained assignment silently does nothing and `.loc` is the only correct way to write into a table; and text columns report the dedicated `str` dtype instead of the old `object`.

## Source code

[`courses/python-course/06 - Advanced/`](https://github.com/davidowa/learning-hub/tree/main/courses/python-course/06%20-%20Advanced)
