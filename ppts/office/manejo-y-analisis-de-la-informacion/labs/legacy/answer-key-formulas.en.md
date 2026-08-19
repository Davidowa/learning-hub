# The formulas, recovered from the solved workbooks

Four of the previous years' workbooks shipped with formulas in them rather than only data.
Ten thousand two hundred and seventy-two cells held one. This file is all of them, and it
exists because the CSV export next door does not carry a single one: a CSV records what a
formula evaluated to, never the formula itself. Delete the workbooks without this file and
the answer key to the second-partial comprehensive exam is gone.

## Why it is short

Ten thousand formulas is not ten thousand ideas. A column filled down 1,689 rows is one
formula written once and copied, so the list below collapses each column to its distinct
patterns and records the range the copies cover. Twenty-seven patterns account for all
10,272 cells. Every formula is quoted exactly as the workbook stores it, in the cell where
it first appears, so filling it down the stated range rebuilds the column.

## Comprehensive_2ndPartial_SOLVED.xlsx

The worked version of the second-partial comprehensive exam. The blank version students
receive is `Comprehensive_2ndPartial.xlsx`, and the difference between the two is this table.

### Sheet `Times`, 1,695 rows

| Cell | Filled to | Copies | Formula |
|---|---|---|---|
| `A6` | `A1693` | 1,688 | `=+A5+1` |
| `A1694` | | 1 | `=COUNT(A5:A1693)` |
| `D5` | `D1693` | 1,689 | `=VLOOKUP(C5,Machines!$A$2:$C$11,2,FALSE)` |
| `F5` | `F1693` | 1,689 | `=VLOOKUP(E5,Participants!$A$3:$B$72,2,FALSE)` |
| `G5` | `G1693` | 1,689 | `=ROUND((FNAC-VLOOKUP(F5,Participants!$B$3:$F$72,5,FALSE))/365,0)` |
| `H1694` | | 1 | `=SUM(H5:H1693)` |
| `H1695` | | 1 | `=H1694/60` |
| `I5` | `I1693` | 1,689 | `=B5` |
| `J5` | `J1693` | 1,689 | `=MONTH(I5)` |

`G5` is the one to read twice. `FNAC` is a defined name, not a function, and it points at the
single cell `Times!$J$2`, which holds the date the ages are measured against. The formula
takes that fixed date, subtracts the participant's date of birth pulled out of the fifth
column of `Participants`, divides by 365 and rounds, which is age in whole years by the rough
method rather than by `DATEDIF`. Without the defined name the column cannot be rebuilt, which
is why the names are listed at the end of this file.

`H1694` sums the minutes and `H1695` divides that by 60, so the sheet reports total use in
minutes and again in hours.

### Sheet `Machines`

| Cell | Filled to | Copies | Formula |
|---|---|---|---|
| `C12` | | 1 | `=SUM(C2:C11)` |
| `D2` | `D11` | 10 | `=SUMIF(Times!$C$4:$C$1693,Machines!A2,Times!$H$4:$H$1693)` |

### Sheet `Participants`

| Cell | Filled to | Copies | Formula |
|---|---|---|---|
| `F3` | `F72` | 70 | `=DATE(E3,D3,C3)` |

Three columns hold year, month and day as separate numbers and `DATE` assembles them, which
is the whole point of that column: the sheet stores the parts and derives the date rather
than storing a date and parsing it.

### Sheet `Report`

| Cell | Filled to | Copies | Formula |
|---|---|---|---|
| `B2` | | 1 | `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,2,FALSE)` |
| `B3` | | 1 | `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,3,FALSE)` |
| `B4` | | 1 | `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,5,FALSE)` |
| `B7` | `B16` | 10 | `=SUMIFS(Times!$H$4:$H$1693,Times!$F$4:$F$1693,Report!$B$2,Times!$C$4:$C$1693,Report!A7,Times!$J$4:$J$1693,8)` |
| `C7` | `C16` | 10 | `=SUMIFS(Times!$H$4:$H$1693,Times!$F$4:$F$1693,Report!$B$2,Times!$C$4:$C$1693,Report!$A7,Times!$J$4:$J$1693,9)` |
| `D7` | `D16` | 10 | `=SUMIFS(Times!$H$4:$H$1693,Times!$F$4:$F$1693,Report!$B$2,Times!$C$4:$C$1693,Report!A7,Times!$J$4:$J$1693,10)` |
| `E7` | `E16` | 10 | `=SUMIFS(Times!$H$4:$H$1693,Times!$F$4:$F$1693,Report!$B$2,Times!$C$4:$C$1693,Report!A7,Times!$J$4:$J$1693,11)` |

Three things worth saying about this block, because they are the kind of detail a student
gets marked on.

`_xlfn.CONCAT` is not something anyone typed. It is how a workbook stores `CONCAT` when the
function is newer than the file format expects, and Excel displays it as plain `CONCAT`.
Written by hand the formula is `=VLOOKUP(CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,2,FALSE)`.
The lookup builds the participant's label from a number typed in `B1`, so changing that one
cell redraws the whole report.

The four `SUMIFS` columns are the same formula with one number changed: the last criterion is
the month, 8, 9, 10 and 11, so the four columns are August through November. That is the
report the five charts plot.

The mixed referencing is inconsistent and it is worth knowing before copying anything. `C7`
locks the column of its machine reference, `Report!$A7`, while `B7`, `D7` and `E7` leave it
relative as `Report!A7`. All four happen to give the same answer where they sit, because they
are only ever filled downward, and the difference would show the moment someone dragged one
of them sideways.

## The other three workbooks

### `10.1 Charts and Tables (students).xlsx`

| Sheet | Cell | Filled to | Formula |
|---|---|---|---|
| `Exercise1` | `D2` | `D6` | `=B2+C2` |

`Exercise2!E37` holds `====>`, which Excel stores as a formula because it starts with an
equals sign. It is an arrow drawn in text, pointing at something on the sheet, and it is not
a calculation. Typing it back in needs a leading apostrophe or Excel rejects it.

### `11.1 Excel 11 (students) Advanced filters.xlsx`, sheet `Filtro avanzado`

| Cell | Formula | What it is |
|---|---|---|
| `D88` | `=RIGHT(B3,1)="8"` | a criteria-range formula, rows whose code ends in 8 |
| `D100` | `=J3>AVERAGE($J$3:$J$29)` | a criteria-range formula, above-average rows |
| `G99` | `=AVERAGE(J3:J29)` | the average itself, on the sheet for reference |

The first two are the interesting ones and they are why this exercise exists. A computed
criterion in an Advanced Filter criteria range must sit under a heading that is blank or that
does not match any column heading in the list, and it refers to the FIRST data row of the
list, here row 3, not to the whole column. Get either wrong and the filter silently returns
everything or nothing.

### `Hmw7_Excel(students).xlsx`, sheet `Hoja1`

| Cell | Formula |
|---|---|
| `G107` | `=SUM(G9:G105)` |
| `H107` | `=SUM(H9:H105)` |
| `I107` | `=SUM(I9:I105)` |

## The defined names these depend on

A formula that names a range cannot be rebuilt without the name. These are every defined name
in the previous years' workbooks, as the workbooks stored them.

| Workbook | Name | Refers to |
|---|---|---|
| `Comprehensive_2ndPartial_SOLVED.xlsx` | `FNAC` | `Times!$J$2` |
| | `Age` | `Times!$G$5:$G$1694` |
| | `Enrollment_date` | `Times!$B$5:$B$1694` |
| | `Equipment_description` | `Times!$D$5:$D$1694` |
| | `Machine` | `Times!$C$5:$C$1694` |
| | `Name` | `Times!$F$5:$F$1694` |
| | `Number` | `Times!$A$5:$A$1694` |
| | `Participant` | `Times!$E$5:$E$1694` |
| | `Time_of_use__minutes` | `Times!$H$5:$H$1694` |
| `8.1 Excel 8 (students) Search and filters.xlsx` | `Table1` | `Inventory!$G$4:$J$8` |
| | `Table2` | `Inventory!$Q$4:$T$8` |
| | `Table3` | `Inventory!$X$10:$AA$14` |
| `9.1 Excel 9 (inspection, properties).xlsx` | `BD` | `Personnel!$A$1:$I$115` |
| | `CRITERIOO` | `Personnel!#REF!` |
| | `CRITERIOY` | `Personnel!#REF!` |
| | `RESULTADOS` | `Personnel!#REF!` |
| `Hmw6_Excel(students).xlsx` | `Operadores` | `Ejercicio1!$A$27:$B$30` |
| `Hmw11_Excel(students)_AdvancedFilters.xlsx` | none | |

Three of the four names in `9.1 Excel 9` are broken and point at `#REF!`. They were defined
over ranges that were later deleted, and Excel keeps the name with a dead reference rather
than removing it. They are recorded here as they were found, because a student opening
`Name Manager` on that workbook would have seen exactly that, and because the current
`ex18.en.md` documents the same three names surviving into this year's version of the
exercise. Do not repair them when rebuilding: the broken state is the teaching material.

`Time_of_use__minutes` carries two underscores in the middle. That is what a defined name
looks like when it is made from the heading `Time of use (minutes)`, since a name cannot hold
a space or a bracket and Excel substitutes an underscore for each.
