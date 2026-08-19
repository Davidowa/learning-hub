# Practice workbooks, as markdown

The instructor's own Excel practice material, converted out of .xlsx and .docx so it can be read,
corrected and versioned. Twenty-five exercises and twenty-three homework sets.

These are not the fifty-one course exercises. Those live in [../exercises.en.md](../exercises.en.md)
and follow the seventeen weeks of the syllabus. What is here already existed, kept because the
students use it and rewritten because the spelling and the steps needed it.

## How the data works

The original workbooks hold 103,702 rows, so the instructions became markdown and the data became
CSV under `data/`. A sheet of forty rows or fewer is also written inline as a table, so the exercise
can be rebuilt by typing. Anything larger links its CSV. 128 files, 4.8 MB, all of it text that
diffs and versions.

What CSV does not carry: cell formatting, conditional formatting rules, charts, data validation
lists and sheet protection. Several exercises teach exactly those, so each one was written out as
text before the original workbooks were retired: the exact range, the exact condition, the colour
as a hex value, the validation list, the protection settings. There turned out to be fewer of them
than feared, ten workbooks out of seventy-two and no PivotTable layouts at all.

Three things were harder to find and are worth knowing about, because they are the same shape of
problem and none of them shows up in a directory listing.

**Instructions in floating text boxes.** A text box is drawn over the sheet, not stored in a cell,
so the CSV export never saw one. Eight thousand six hundred characters of task text were sitting in
them, which is why several homework files here used to be twenty-line stubs that described the data
and then went quiet. They are written in now.

**Instructions on a sheet with a misleading name.** Homework 19 keeps its task list on a sheet
called `Exercise1` that holds no data at all, and Homework 10 keeps its two prize rules in a wide
column beside the table. Neither was caught by looking for a sheet named Instructions.

**Formulas as pictures.** Legacy homework 4 carried its six statistical formulas as Windows
metafiles. They were rendered, read and transcribed.

## Previous years

[legacy/](legacy/) holds seventeen exercises and nine homework sets from earlier runs of the course,
plus the second-partial comprehensive exam. That material was never converted before and is a third
of the total data. It is archive rather than assignment; nothing in it is set to students today.

## Pictures of the dialogs

The `Exam routes used here` section of every file that has one now carries screenshots of the boxes
its routes walk to: 91 figures across 34 files, 35 distinct images, all of them taken from the
running product and kept in `ppts/img/en/`. A route gets a picture when the shot is of the window
that route actually opens, and gets none when it is not; the ribbon galleries, Auto Fill, freeze
panes and the Document Inspector have no shot and are left without one on purpose.

Three captions disclose a near miss rather than hide it. `find-and-replace.png` was taken with the
Replace tab in front, `insert-chart.png` opens on Recommended Charts, and `function-arguments-if.png`
is the argument dialog loaded with IF, so where those sit on a route about the other tab or another
function the caption says so and says what the reader will see in its place. The alternative was a
gap, and a disclosed near miss teaches more than a gap does.

Every image is English, because the machine that took them edits in English. The Spanish files will
need their own set from a machine with the language pack, written to `ppts/img/es/`, and the routes
here are where they go.

## Exercises

| # | What it covers | Objectives | Data |
|---|---|---|---|
| [1](ex01.en.md) | Cell formats and styles | MO-200 2.1.2, 2.1.3, 2.1.4, 2.2.1, 2.2.2, 2.2.3, 2.2.4, 2.2.5, 2.2.6, 2.2.7, 2.2.8 | 2 |
| [2](ex02.en.md) | Managing worksheets, named ranges and freeze panes | MO-200 1.2.2, 1.3.2, 1.4.3, 2.1.2, 2.1.3, 2.3.1; MO-201 2.1.2 | 0 |
| [3](ex03.en.md) | Conditional formatting, sparklines and links | MO-200 1.2.3, 1.4.3, 2.1.4, 2.4.1, 2.4.2, 4.1.1, 4.2.1; MO-201 2.3.1 | 3 |
| [4](ex04.en.md) | Page setup, print area and workbook views | MO-200 1.3.1, 1.4.2, 1.4.3, 1.4.4, 1.5.1, 1.5.3, 2.1.3, 2.2.2 | 1 |
| [5](ex05.en.md) | Operator precedence, references and defined names | MO-200 2.3.1, 4.1.1, 4.1.2, 4.2.1; MO-201 3.5.1, 3.5.2 in the optional extension | 2 |
| [06](ex06.en.md) | Basic functions and COUNTIF | MO-200 4.2.1, MO-200 4.2.2, MO-200 2.1.2, MO-200 3.1.1, MO-200 3.1.2, MO-201 3.1.1 | 2 |
| [07](ex07.en.md) | The IF function | MO-200 4.2.3, MO-200 4.1.1, MO-200 4.1.2, MO-200 2.3.1, MO-200 2.1.1, MO-200 4.2.1, MO-200 4.2.2, MO-201 3.1.1, MO-210 2.1.5 | 3 |
| [08](ex08.en.md) | Nested IF | MO-200 4.2.3, MO-200 2.1.2, MO-200 2.3.1, MO-200 4.1.2, MO-201 3.1.1, MO-201 3.5.4 | 3 |
| [09](ex09.en.md) | SUMIF, COUNTIF and AVERAGEIF | MO-201 3.1.1, MO-200 2.2.5, MO-200 2.2.6, MO-200 4.2.1, MO-200 4.2.2, MO-200 4.1.1 | 2 |
| [10](ex10.en.md) | AND, OR and wildcards | MO-200 4.2.3, MO-200 1.2.1, MO-200 2.3.1, MO-201 3.1.1 | 3 |
| [11](ex11.en.md) | Multi-criteria totals with SUMIFS, COUNTIFS and AVERAGEIFS | MO-201 3.1.1 | 2 |
| [12](ex12.en.md) | The IFS function against nested IF | MO-200 4.2.3, MO-200 2.2.5, MO-201 3.1.1 | 2 |
| [13](ex13.en.md) | Text functions, date codes and custom number formats | MO-200 4.3.1, MO-200 4.3.2, MO-200 4.3.3, MO-200 2.2.6, MO-201 2.2.1 | 2 |
| [14](ex14.en.md) | Remove duplicates, import and sort, and data validation | MO-200 1.1.2, MO-200 3.1.3, MO-200 3.3.2, MO-200 1.5.4, MO-201 2.2.5, MO-201 2.2.2 | 5 |
| [15](ex15.en.md) | AutoFilter over an appliance sales log | MO-200 1.3.2, MO-200 2.2.4, MO-200 2.2.5, MO-200 2.2.6, MO-200 2.4.2, MO-200 3.3.1, MO-200 3.3.2, MO-200 4.1.1, MO-201 2.3.1 | 1 |
| [16](ex16.en.md) | Excel tables and structured references | MO-200 2.1.1, 2.3.2, 2.4.2, 3.1.1, 3.1.2, 3.2.1, 3.2.2, 3.2.3, 4.1.2, MO-201 3.1.1 | 3 |
| [17](ex17.en.md) | Charts, twenty of them | MO-200 5.1.1, 5.2.3, 5.3.1, 5.3.2, MO-201 4.1.1, 4.1.2 | 5 |
| [18](ex18.en.md) | Accessibility, comments and protection | MO-200 1.5.4, 2.2.6, 2.3.1, MO-201 1.2.2, 1.2.3, 1.2.5, 3.3.1 | 1 |
| [19](ex19.en.md) | VLOOKUP inside a payroll model | MO-200 2.2.5, 2.4.2, 3.1.1, 3.1.2, MO-201 2.3.1, 3.1.1, 3.2.1, 3.3.1 | 4 |
| [20](ex20.en.md) | VLOOKUP over a student record | MO-200 2.2.5, 4.3.3, MO-201 2.2.2, 3.1.1, 3.2.1 | 4 |
| [21](ex21.en.md) | Lookups across three table shapes | MO-200 2.3.1, MO-200 4.1.2, MO-201 3.2.1 | 3 |
| [22](ex22.en.md) | Automatic subtotals and outline levels | MO-200 3.3.2, MO-201 2.2.3, MO-201 2.2.4 | 1 |
| [23](ex23.en.md) | PivotTables, from a warm-up to a full report | MO-200 2.4.2, MO-200 3.1.1, MO-200 3.2.3, MO-201 4.2.1, MO-201 4.2.2, MO-201 4.2.3, MO-201 4.2.4, MO-201 4.2.5, MO-201 4.2.6, MO-201 4.3.1, MO-201 4.3.2, MO-201 4.3.3, MO-201 4.3.4 | 2 |
| [24](ex24.en.md) | Advanced filters and criteria ranges | MO-200 3.3.1, MO-200 4.2.1, MO-201 2.2.5 | 1 |
| [25](ex25.en.md) | What-if analysis with Goal Seek, data tables and PMT | MO-200 2.2.5, MO-201 2.2.2, MO-201 3.4.2, MO-201 3.4.4 | 0 |

## Homework

| # | What it covers | Objectives | Data |
|---|---|---|---|
| [1](homework/hw01.en.md) | Cell and range formatting | MO-200 1.3.2, 2.2.1, 2.2.2, 2.2.4, 2.2.5, 2.2.6 | 2 |
| [2](homework/hw02.en.md) | Managing sheets, cells, rows and columns | MO-200 1.3.2, 2.1.3, 2.1.4, 2.2.2 | 5 |
| [3](homework/hw03.en.md) | Conditional formatting | MO-200 2.4.2, 2.4.3, MO-201 2.3.1, 2.3.4 | 2 |
| [4](homework/hw04.en.md) | Page setup, print area and workbook views | MO-200 1.3.1, 1.3.2, 1.3.3, 1.4.2, 1.4.3, 1.5.1, 1.5.2, 2.2.5, 2.2.6, 2.2.7, MO-201 2.2.1 | 2 |
| [5](homework/hw05.en.md) | Operator order, absolute and mixed references | MO-200 2.2.5, 4.1.1, 4.2.1 | 6 |
| [6](homework/hw06.en.md) | Statistical functions, counting and text built by formula | MO-200 1.4.3, 2.1.2, 2.1.3, 2.2.2, 2.2.5, 4.2.1, 4.2.2, 4.3.3, MO-201 3.1.1, 3.3.1 | 1 |
| [7](homework/hw07.en.md) | The IF function | MO-200 2.2.5, 4.2.3, MO-201 3.1.1 | 3 |
| [8](homework/hw08.en.md) | Nested IF | MO-200 4.2.3, MO-201 3.1.1, 3.5.4 | 6 |
| [9](homework/hw09.en.md) | SUMIF, COUNTIF and AVERAGEIF | MO-201 3.1.1, MO-200 4.2.1, 2.2.5 | 3 |
| [10](homework/hw10.en.md) | Conditional logic on real decisions | MO-200 4.2.3 · MO-201 3.4.3 | 5 |
| [11](homework/hw11.en.md) | Payroll and service counts under criteria | MO-200 4.2.2 · MO-201 3.4.3 | 4 |
| [12](homework/hw12.en.md) | Three years of unit sales, ready to summarise | MO-201 4.2.1 · MO-201 2.2.4 | 2 |
| [13](homework/hw13.en.md) | Cereal nutrition, sorted and filtered | MO-200 3.3.1 · MO-200 3.3.2 | 1 |
| [14](homework/hw14.en.md) | Sorting on more than one key | MO-200 3.3.2 · MO-201 2.2.4 | 5 |
| [15](homework/hw15.en.md) | Five filters on the same table | MO-200 3.3.1 · MO-201 2.2.4 | 1 |
| [17](homework/hw17.en.md) | Charts that answer a question | MO-200 5.1.1 · 5.2.3 · 5.3.1 | 3 |
| [17b](homework/hw17b.en.md) | Climate data, seven chart families | MO-200 5.1.1 · 5.2.3 · MO-201 4.1.1 | 4 |
| [19](homework/hw19.en.md) | Looking a value up instead of finding it by eye | MO-201 3.2.1 | 3 |
| [20](homework/hw20.en.md) | Two lookups pointing at each other | MO-201 3.2.1 | 8 |
| [21](homework/hw21.en.md) | An income statement, five years wide | MO-200 2.2.5 · 2.2.6 · MO-201 2.2.1 | 2 |
| [22](homework/hw22.en.md) | Subtotals on an order log | MO-201 2.2.4 | 1 |
| [23](homework/hw23.en.md) | Twenty-six thousand orders, one PivotTable | MO-201 4.2.1 · 4.2.2 · 4.2.4 | 1 |
| [24](homework/hw24.en.md) | Farmers market sales, sliced three ways at once | MO-201 2.2.4 · 3.4.2 | 1 |

## Gaps worth knowing

There is no homework for exercises 16, 18 and 25, which are tables, protection and what-if analysis.
Those are three of the heavier topics and the three with no take-home practice.

Homework 12 and 13 arrived with an Instructions sheet holding no cell content, because the original
wording sits in a floating text box that does not survive conversion. Both files say so and describe
the data rather than inventing tasks.

Homework 21 stores its whole income statement as comma separated text inside one column. That is now
the first step of the exercise rather than a defect, and both the raw and the split CSV are there.

Exercise 2 and exercise 25 have instructions and no workbook. Exercises 8 and 20 have a workbook and
no instructions.
