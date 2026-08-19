# Comprehensive exercise, second partial · The gym usage log

A gym hands over four sheets of raw data, 1,689 machine sessions logged between August and November 2021, ten machines with their prices, seventy members with their dates of birth split across three columns, and a price list nobody is meant to touch. The exercise turns that into one workbook where a receptionist types a member number into a single cell and reads back the member's name, age, first recorded date and a month by month breakdown of time spent on every machine, with five charts beside it and every other cell locked. It is the integrating exercise for the second period of an earlier run of the course, so it reaches back over the whole term: lookups, conditional sums, named ranges, custom date formats, conditional formatting, sheet protection and charts, in one file. Hand in `Comprehensive_2ndPartial.xlsx` worked through.

**Objectives** MO-200 1.3.1, 1.5.1, 1.5.3, 2.1.3, 2.2.2, 2.2.5, 2.2.7, 2.3.1, 2.4.2, 3.3.2, 4.1.2, 4.2.1, 4.2.2, 4.3.3, 5.1.1, 5.2.3, MO-201 1.2.2, 2.2.1, 2.3.1, 3.1.1, 3.2.1

## The data

Two workbooks survive: `Comprehensive_2ndPartial.xlsx`, the file the students start from, and `Comprehensive_2ndPartial_SOLVED.xlsx`, the instructor's worked copy. Both are described below, because the worked copy is the only record of what the finished file was supposed to look like.

The starting workbook holds four sheets, named `Hoja2`, `Hoja3`, `Hoja4` and `Hoja5`. There is no `Hoja1`. The instruction sheet calls them Sheet 2, Sheet 3, Sheet 4 and Sheet 5, which matches the names rather than the positions, so Sheet 2 is the first sheet in the file.

One warning about the CSV files below. The export drops rows and columns that are completely empty, so a line number in a CSV is not always the row number in the workbook. Where that matters the workbook row is given in the text. The solved CSV files also hold results, not formulas, because the export reads the calculated values.

### The starting workbook

**Sheet `Hoja2`, the usage log.** One row per session: which member used which machine, on what day, for how many minutes. The header sits on row 2 and the records run from row 3 to row 1691, 1,689 of them, in columns A to D. Row 1 is empty.

File: [labs/legacy/data/comprehensive-2ndpartial--hoja2.csv](data/comprehensive-2ndpartial--hoja2.csv), 1,690 rows by 4 columns, the header included.

| Column | Header | What it holds |
|---|---|---|
| A | `Enrollment date` | The date of the session, formatted `mm-dd-yy`, from 1 August to 30 November 2021 |
| B | `Machine` | `Machine 1` to `Machine 10` |
| C | `Participant` | `Participant 1` to `Participant 70` |
| D | `Time of use (minutes)` | Whole minutes, in an accounting number format |

The sessions split 437 in August, 465 in September, 412 in October and 375 in November, and they add up to 240,167 minutes.

**Sheet `Hoja3`, the machines.** Ten machines in A2:C11, unsorted, with only one header in place: C1 reads `Price` while A1 and B1 are empty. Task 9 is what fixes that.

File: [labs/legacy/data/comprehensive-2ndpartial--hoja3.csv](data/comprehensive-2ndpartial--hoja3.csv), 11 rows by 3 columns.

| (no header) | (no header) | Price |
|---|---|---|
| Machine 9 | Nordick Track Comercial 9.9 Eliptica | 29995 |
| Machine 1 | Nordick Track Comercial 9.9 Eliptica | 29995 |
| Machine 7 | Nordick Track Caminadora Comercial 1750 | 42995 |
| Machine 3 | Nordick Track RW700 Remadora | 29995 |
| Machine 10 | Multigimnasio sportline | 9999 |
| Machine 2 | Nordick Track Caminadora Comercial 1750 | 42995 |
| Machine 4 | Escalera sin fin unifitness | 50736 |
| Machine 6 | Escalera sin fin unifitness | 50736 |
| Machine 5 | Nordick Track VR25 Bicicleta Reclinada | 29995 |
| Machine 8 | Nordick Track Comercial 9.9 Eliptica | 29995 |

**Sheet `Hoja4`, the participants.** Seventy members in A3:E72, with no header row at all. Column A holds the member code, column B the full name as `Surnames,Given names`, and columns C, D and E hold the day, the month and the year of birth as three separate numbers. Column F is empty and is where task 14 builds the date.

File: [labs/legacy/data/comprehensive-2ndpartial--hoja4.csv](data/comprehensive-2ndpartial--hoja4.csv), 70 rows by 5 columns.

**Sheet `Hoja5`, the price list.** A small reference sheet the exercise never calculates with. It is only protected and hidden, in task 23. Two blocks, and the annual column is deliberately empty.

File: [labs/legacy/data/comprehensive-2ndpartial--hoja5.csv](data/comprehensive-2ndpartial--hoja5.csv), 18 rows by 6 columns.

| Cell | Contents |
|---|---|
| A1:D1 | `Plan`, `Description`, `Monthly`, `Annual` |
| A2:C2 | `A`, `Only Gym`, `1528` |
| A3:C3 | `B`, `Only Pool`, `2345` |
| A4:C4 | `C`, `Gym and Pool`, `Sum of the previous with 20% discount` |
| A6 | `Annual payment, 7% discount` |
| A8 | `Payment frequency` |
| A9, A10 | `Monthly`, `Annual` |
| E8 | `Months of the year` |
| E9:F20 | `1` to `12` against `January` to `December` |

### The worked workbook

The solved file renames the sheets and adds one. `Hoja2` becomes `Times`, `Hoja3` becomes `Machines`, `Hoja4` becomes `Participants`, `Hoja5` keeps its name, and the new sheet is called `Report`. Tab colours are set on four of the five: `Times` in accent 1 darkened, `#4472C4`, blue; `Machines` in accent 2 darkened, `#ED7D31`, orange; `Participants` in accent 4 darkened, `#FFC000`, amber; `Report` in `#FF0000`, red. `Hoja5` keeps the default tab.

**Sheet `Times`.** The usage log with six columns added. Row 1 holds the title `Gym HT Information` in A1, styled with the built-in Heading 1 cell style, Calibri 15 bold, and aligned Center Across Selection. J2 holds the cut-off date `30/11/2021` in the format `d-mmm-yy` and carries the defined name `FNAC`. Row 3 is empty. The header row is row 4, bold and centred both horizontally and vertically. Records run from row 5 to row 1693. Row 1694 holds the record count and the total minutes, row 1695 the same total in hours.

File: [labs/legacy/data/comprehensive-2ndpartial-solved--times.csv](data/comprehensive-2ndpartial-solved--times.csv), 1,694 rows by 10 columns.

| Column | Header | Contents in row 5 | Number format |
|---|---|---|---|
| A | `Number` | `1`, then `=+A5+1` filled down | General |
| B | `Enrollment date` | the session date | `dddd\ dd/mm/yyyy` |
| C | `Machine` | the machine code | General |
| D | `Equipment description` | `=VLOOKUP(C5,Machines!$A$2:$C$11,2,FALSE)` | General |
| E | `Participant` | the member code | General |
| F | `Name` | `=VLOOKUP(E5,Participants!$A$3:$B$72,2,FALSE)` | General |
| G | `Age` | `=ROUND((FNAC-VLOOKUP(F5,Participants!$B$3:$F$72,5,FALSE))/365,0)` | `#,##0_);(#,##0)` |
| H | `Time of use (minutes)` | the minutes | accounting, `_(* #,##0.00_);_(* \(#,##0.00\);_(* "-"??_);_(@_)` |
| I | none | `=B5`, a second copy of the date | `dddd\ dd/mm/yyyy` |
| J | none | `=MONTH(I5)`, the month number | General |

Columns I and J are helper columns the instruction sheet never asks for. The report on the new sheet depends on both.

Row 1694 holds `=COUNT(A5:A1693)` in A1694 and `=SUM(H5:H1693)` in H1694, with the word `minutes` in I1694. Row 1695 holds `=H1694/60` in H1695 with the word `hours` in I1695.

Nine defined names live on this sheet, all scoped to the workbook:

| Name | Refers to |
|---|---|
| `Number` | `Times!$A$5:$A$1694` |
| `Enrollment_date` | `Times!$B$5:$B$1694` |
| `Machine` | `Times!$C$5:$C$1694` |
| `Equipment_description` | `Times!$D$5:$D$1694` |
| `Participant` | `Times!$E$5:$E$1694` |
| `Name` | `Times!$F$5:$F$1694` |
| `Age` | `Times!$G$5:$G$1694` |
| `Time_of_use__minutes` | `Times!$H$5:$H$1694` |
| `FNAC` | `Times!$J$2` |

One conditional formatting rule sits on this sheet, and it is the only one in the workbook:

- Range `G5:G1695`, rule type Cell Value, operator greater than, value `45`, priority 1.
- Format: bold on, italic off, font colour theme 0, which is `#FFFFFF`, white, and a solid fill in theme 9, accent 6, which is `#70AD47`, green.

**Sheet `Machines`.** Headers on row 1, ten machines sorted by column A on rows 2 to 11, the investment total in C12. Column D is the column task 13 adds.

File: [labs/legacy/data/comprehensive-2ndpartial-solved--machines.csv](data/comprehensive-2ndpartial-solved--machines.csv), 12 rows by 4 columns.

| Machine | Equipment Description | Price | Total time used |
|---|---|---|---|
| Machine 1 | Nordick Track Comercial 9.9 Eliptica | 29995 | 22748 |
| Machine 10 | Multigimnasio sportline | 9999 | 22881 |
| Machine 2 | Nordick Track Caminadora Comercial 1750 | 42995 | 23193 |
| Machine 3 | Nordick Track RW700 Remadora | 29995 | 24996 |
| Machine 4 | Escalera sin fin unifitness | 50736 | 25581 |
| Machine 5 | Nordick Track VR25 Bicicleta Reclinada | 29995 | 23617 |
| Machine 6 | Escalera sin fin unifitness | 50736 | 30443 |
| Machine 7 | Nordick Track Caminadora Comercial 1750 | 42995 | 23950 |
| Machine 8 | Nordick Track Comercial 9.9 Eliptica | 29995 | 20555 |
| Machine 9 | Nordick Track Comercial 9.9 Eliptica | 29995 | 22203 |
| | | 347436 | |

C12 holds `=SUM(C2:C11)`. D2 holds `=SUMIF(Times!$C$4:$C$1693,Machines!A2,Times!$H$4:$H$1693)`, filled down to D11.

**Sheet `Participants`.** The member list with the date of birth built in column F. Row 1 is empty, F2 holds the single header `Date of birth`, and the members sit on rows 3 to 72. F3 holds `=DATE(E3,D3,C3)` filled down, formatted `dd/mmmm/yyyy`. Columns A to E are untouched from the starting file, headers included, which is to say there are none.

File: [labs/legacy/data/comprehensive-2ndpartial-solved--participants.csv](data/comprehensive-2ndpartial-solved--participants.csv), 71 rows by 6 columns.

**Sheet `Report`, the new sheet.** The only sheet a user of the finished workbook may type on, and then only in B1. Row 5 is empty.

File: [labs/legacy/data/comprehensive-2ndpartial-solved--report.csv](data/comprehensive-2ndpartial-solved--report.csv), 15 rows by 5 columns. The values below are the ones the file was saved with, for `Participant 6`.

| Cell | Contents | Value as saved |
|---|---|---|
| A1, B1 | `Participant Number`, the number typed by the user | 6 |
| A2, B2 | `Participant Name`, `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,2,FALSE)` | Gutiérrez Ramírez,Juan Carlos |
| A3, B3 | `Age`, `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,3,FALSE)` | 51 |
| A4, B4 | `Date of enrollment`, `=VLOOKUP(_xlfn.CONCAT("Participant ",$B$1),Times!$E$4:$I$1693,5,FALSE)`, formatted `dd/mmm/yy` | 09/nov/21 |

B1:D1, B2:D2, B3:D3 and B4:D4 are merged. The grid below starts on row 6:

| | August | September | October | November |
|---|---|---|---|---|
| Machine 1 | 0 | 144 | 120 | 0 |
| Machine 2 | 130 | 0 | 131 | 309 |
| Machine 3 | 0 | 242 | 0 | 291 |
| Machine 4 | 243 | 0 | 0 | 0 |
| Machine 5 | 139 | 0 | 0 | 142 |
| Machine 6 | 0 | 121 | 0 | 0 |
| Machine 7 | 0 | 0 | 155 | 0 |
| Machine 8 | 0 | 120 | 0 | 0 |
| Machine 9 | 301 | 0 | 132 | 0 |
| Machine 10 | 0 | 128 | 0 | 0 |

A6 reads `Total time spent:`, and B6:E6 hold the four month names. Every cell in B7:E16 holds a SUMIFS over the log, matching the member by name, the machine by the label in column A and the month by the number in the helper column. B7 is `=SUMIFS(Times!$H$4:$H$1693,Times!$F$4:$F$1693,Report!$B$2,Times!$C$4:$C$1693,Report!A7,Times!$J$4:$J$1693,8)`, with 9, 10 and 11 as the last argument in columns C, D and E.

The sheet is protected with a password. Every permission in the **Allow all users of this worksheet to** list is denied, including formatting, inserting and deleting rows and columns, sorting, AutoFilter, PivotTables, editing objects and editing scenarios. Only **Select locked cells** and **Select unlocked cells** are allowed, so a user can click anywhere but type nowhere. B1 is the single unlocked cell on the sheet; every other cell is locked. The password itself is stored as a SHA-512 hash and cannot be read back from the file.

Print setup on this sheet: print area `Report!$A$1:$R$33`, landscape, A4, scaled to 61 per cent, with fit to page on.

Five charts float over the sheet, all of them reading from the grid above:

| Chart | Type | Title | Categories | Values |
|---|---|---|---|---|
| 1 | Line, standard grouping, no smoothing | `Machine usage in August` | `Report!$A$7:$A$16` | `Report!$B$7:$B$16` |
| 2 | Line | `Machine usage in September` | `Report!$A$7:$A$16` | `Report!$C$7:$C$16` |
| 3 | Line | `Machine usage in October` | `Report!$A$7:$A$16` | `Report!$D$7:$D$16` |
| 4 | Line | `Machine usage in November` | `Report!$A$7:$A$16` | `Report!$E$7:$E$16` |
| 5 | Column, clustered | `Total time spent per Machine` | `Report!$B$6:$E$6` | ten series, `Report!$B$7:$E$7` down to `Report!$B$16:$E$16`, each named from its own cell in `Report!$A$7` to `Report!$A$16` |

The four line charts carry data labels and no legend. The column chart carries both. Roughly, chart 1 sits over F4:L16, chart 2 over M4:R16, chart 3 over F17:L30, chart 4 over M18:R30 and chart 5 over A18:F32.

**Sheet `Hoja5`.** Unchanged in content, hidden, and protected with a password under the same settings as `Report`: everything denied except selecting cells.

File: [labs/legacy/data/comprehensive-2ndpartial-solved--hoja5.csv](data/comprehensive-2ndpartial-solved--hoja5.csv), 18 rows by 6 columns.

## What to do

The instruction sheet is a two column table, the task on the left and the sheet it belongs to on the right. It moves from sheet to sheet and back again; the thirty tasks are regrouped by sheet below, with the table's own sheet number given first and the workbook name beside it. Nothing is added and nothing is dropped.

**On Sheet 2, `Hoja2`.**

1. Insert a column on the left, so it becomes the first column.
2. In the inserted column, number the data. The solved file writes `1` in A5 and `=+A5+1` down the rest.
3. In column E, include a formula at the end of the data that counts the records in that column. The solved file puts `=COUNT(A5:A1693)` in A1694 instead, in the numbering column rather than column E.
4. Insert a column after `Participant` entitled `Name`.
5. In the `Name` column, enter a formula that looks up the participant on Sheet 4 and places the name in the correct cell: `=VLOOKUP(E5,Participants!$A$3:$B$72,2,FALSE)`.
6. Insert a column after `Machine` entitled `Equipment Description`.
7. In the `Equipment Description` column, enter a formula that looks up the machine on Sheet 3 and places the description in the correct cell: `=VLOOKUP(C5,Machines!$A$2:$C$11,2,FALSE)`.
8. Change the date cell format to one that includes the day of the week. The solved file uses the custom format `dddd\ dd/mm/yyyy`.
9. At the end of the `Time of Use` column, include a formula that gives how long the equipment has been used in total: `=SUM(H5:H1693)`, with `=H1694/60` underneath it for the same figure in hours.
10. Insert a column next to the participant's name and calculate the age as of 30 November 2021. The solved file puts the cut-off date in J2 and writes `=ROUND((FNAC-VLOOKUP(F5,Participants!$B$3:$F$72,5,FALSE))/365,0)` in column G, next to the `Name` column.
11. Name the cell holding the 30 November date `FNAC`, and protect it so that it cannot be modified.
12. For participants over 45 years of age, highlight the age cell with a green fill and white letters. The rule in the solved file is Cell Value greater than `45` over `G5:G1695`, formatted bold, white text `#FFFFFF`, green fill `#70AD47`.
13. Insert two rows at the beginning of the sheet.
14. Write the title `Gym HT Information` in row 1.
15. Create an attractive style for the title and apply it to row 1. The solved file uses the built-in Heading 1 cell style with Center Across Selection.
16. Name each column with the column title. The solved file defines eight names over the data, `Number`, `Enrollment_date`, `Machine`, `Equipment_description`, `Participant`, `Name`, `Age` and `Time_of_use__minutes`, each pointing at rows 5 to 1694 of its own column.
17. Center the titles vertically and horizontally in the cell.

**On Sheet 3, `Hoja3`.**

18. Include a header for each column. The solved file writes `Machine`, `Equipment Description`, `Price` and `Total time used` across A1:D1.
19. Sort the data by column A.
20. At the end of the `Price` column, include a formula that calculates the total investment in machines: `=SUM(C2:C11)` in C12.
21. To the right of each machine's price, include a formula giving the total time that machine was used between August and November 2021: `=SUMIF(Times!$C$4:$C$1693,Machines!A2,Times!$H$4:$H$1693)`, filled down.

**On Sheet 4, `Hoja4`.**

22. In column F, join the data in columns C, D and E, which hold each participant's day, month and year of birth, to form the date of birth. The date must carry the format `dd/mmmm/yyyy`. The solved file uses `=DATE(E3,D3,C3)`.

**On Sheet 5, `Hoja5`.**

23. Protect Sheet 5 with the password `1234` and hide it.

**On a new sheet.**

24. Insert a new sheet.
25. On that sheet the user types only the participant number, in cell B1, and gets back: the participant name in B2, the age in B3, the date of enrollment in B4, and the total time spent per machine per month, one row for each machine with the months in the columns starting at B5. The instruction sheet adds that extra columns of information may be added if required.
26. The user of this file may only modify the participant number on the new sheet, and must not be able to modify anything on any other sheet.
27. Generate a line chart showing usage per machine in each month, one chart for August, another for September, and so on.
28. Generate a column chart giving the total time of use of each machine over the period.
29. Apply an attractive format and print settings to this data, the charts included.

**On every sheet.**

30. Name each sheet with a label that refers to its content, and format it attractively.

## Checks

Against the log itself:

| What | Where | Value |
|---|---|---|
| Records counted | `Times!A1694` | 1689 |
| Total minutes | `Times!H1694` | 240,167 |
| The same in hours | `Times!H1695` | 4002.783333 |
| Distinct machines | column C | 10 |
| Distinct participants | column E | 70 |
| Sessions by month | column J | 437 in August, 465 in September, 412 in October, 375 in November |

Against the machine sheet: `Machines!C12` is 347,436, and the ten values in D2:D11 add up to 240,167, the same figure as `Times!H1694`. If those two totals disagree, a SUMIF range is off or a machine label is misspelt somewhere in the log.

Conditional formatting: 756 of the 1,689 age cells go green and white, which is the 31 participants of the 70 who are over 45 by the rounding the formula uses. A rule that colours nothing is pointed at the wrong column, and one that colours everything has the operator inverted.

The report, with `6` typed into `Report!B1`, must return `Gutiérrez Ramírez,Juan Carlos` in B2, `51` in B3 and `09/nov/21` in B4, and the grid must match the table given above under `Report`. The forty cells of the grid total 2,848 minutes, which is the whole of that member's 21 sessions.

Protection: with the workbook open, typing into any cell of `Report` other than B1 must be refused, and so must typing anywhere on `Hoja5`, which should not be visible in the tab bar at all. Both sheets ask for a password to unprotect.

The five charts must redraw when `Report!B1` changes, because they read the grid and the grid reads the member name.

## Notes on the source

- The instruction sheet numbers the sheets `Sheet 2` to `Sheet 5`, which are the names `Hoja2` to `Hoja5`, not positions. There is no `Hoja1` in the file, so Sheet 2 is the first tab.
- Instruction 3 asks for the record count in column E, at the end of the data. The solved file puts `=COUNT(A5:A1693)` at the foot of column A instead. Column E holds the participant codes, which COUNT would report as zero because they are text, so the solved file is the sensible reading and the instruction is probably a leftover from an earlier column layout.
- Instruction 10 says the age column goes next to the participant's name, and pairs the task with Sheet 2 rather than Sheet 4. The solved file follows the sheet label: the age is calculated on `Times`, in column G, next to the looked-up `Name` in column F, once per session rather than once per member. That is 1,689 copies of seventy ages, and it is what the conditional formatting rule and the report both read.
- The age formula divides the day difference by 365 and rounds to the nearest whole number, so it rounds up from six months and can report an age up to half a year early. It also ignores leap days. `DATEDIF` or `YEARFRAC` would give the exact figure. The count of participants over 45 changes if the formula is corrected, so grade the method rather than the number.
- `FNAC` is Spanish shorthand for *fecha de nacimiento*, date of birth, and the cell it names holds the cut-off date, 30 November 2021, which is nobody's birth date. The name is misleading and the formula still works.
- Instruction 11 says to protect the `FNAC` cell so that it cannot be modified. In the solved file J2 is locked, but the `Times` sheet itself was never protected, and a lock does nothing until the sheet is. The same gap swallows instruction 26: only `Report` and `Hoja5` are protected, so `Times`, `Machines` and `Participants` stay fully editable in the finished file.
- The password on `Report` and on `Hoja5` is stored as a SHA-512 hash with a salt, so the file cannot confirm that it is the `1234` the instruction sheet asks for.
- The defined names all end at row 1694, one row past the last record, so `Age`, `Time_of_use__minutes` and the rest include the totals row. `Number` picks up the record count of 1689 as though it were a record number.
- The lookup and conditional sum ranges all start at row 4, the header row, one row above the data. It changes no result here, since the headers are text and the criteria never match them, and it is still a range chosen by dragging rather than by counting.
- The conditional formatting range `G5:G1695` runs two rows past the last age and covers the totals rows, which hold no age and so never colour.
- `Report!B4` is labelled `Date of enrollment` but VLOOKUP returns the first row in sheet order where the member appears, which is not the earliest date. For `Participant 6` it returns 9 November 2021, while the earliest session logged for that member is 1 August 2021. Nothing in the data records an actual enrollment date, so the label promises more than the source can give.
- The header on the log reads `Enrollment date` as well, although every row is one session on one machine, not an enrollment.
- The report matches members by name, not by code: the SUMIFS in B7:E16 compares `Times` column F against `Report!B2`. Two pairs of members share a name, `Chávez Hernández,Kenia Naydelin` as Participants 26 and 52 and `Ambriz Balmori,Emilio` as Participants 20 and 50. They stay apart only because the strings differ in whitespace, one with a space after the comma and a trailing space, the other without. Tidy that whitespace and both the ages and the report start mixing two people together. Matching on the participant code would have been safe.
- Instruction 25 asks for the months in the columns starting at B5. The solved file starts them at B6, leaving row 5 empty, and the charts are anchored to rows 7 to 16 accordingly.
- Instruction 28 asks for a column chart of the total time of use per machine over the period, one number per machine. The chart in the file plots four bars per machine, one for each month, so it repeats the four line charts in a different shape rather than summing them.
- The instruction sheet gives no chart titles. The five in the solved file are `Machine usage in August`, `Machine usage in September`, `Machine usage in October`, `Machine usage in November` and `Total time spent per Machine`.
- Helper columns I and J on `Times` are not asked for anywhere. I is a plain copy of the date in B and J is the month number taken from I. The report cannot work without J, and the instruction sheet does allow extra columns, so they are the intended answer even though nothing names them.
- Hiding a worksheet has no objective code of its own in MO-200 or MO-201; it appears in `procedures.en.md` only as the ungraded short route under MO-201 1.2.3.
- Equipment names are misspelt and mixed in language: `Nordick Track` for NordicTrack throughout, and Spanish product names such as `Caminadora`, `Remadora` and `Escalera sin fin` beside the English column headers. Ten machines carry seven distinct descriptions, so the lookup on the description is many to one, which is fine in this direction and would break if reversed.
- The starting `Hoja3` has one header, `Price` in C1, and `Hoja4` has none at all. Only `Hoja3` gets a header row from the instructions, in task 18, so `Participants` ends the exercise with a single header, `Date of birth` in F2, floating over five unlabelled columns.
