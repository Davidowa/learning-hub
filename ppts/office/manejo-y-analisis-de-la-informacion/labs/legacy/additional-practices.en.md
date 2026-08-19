# Additional practices · Five loose sheets, five topics

Five unrelated practice sheets in one workbook, `Aditional practices.xlsx`, spelling included. A computing school billing its students and grading them, a bank statement with seven questions attached, a socioeconomic survey next to a grade report, a sales log for PivotTables and a larger sales log for advanced filters. There is no instruction document anywhere in the folder for this workbook, and there never was one: the task text was typed straight into cells beside each table, which is the only reason it survived. Nothing records when these were set, whether they were homework or classwork, or what students were meant to hand back. The topics place them in the second half of the course, alongside the IF, COUNTIF, validation, PivotTable and advanced filter sessions, but that is inference and not a note from the source.

**Objectives** MO-200 2.2.5, 2.4.2, 3.3.1, 4.2.1, 4.2.2, 4.2.3, 5.1.1, MO-201 1.2.2, 2.2.2, 2.2.5, 2.3.1, 3.1.1, 4.2.1, 4.2.2, 4.2.3, 4.2.4, 4.2.5

## The data

Five sheets, named `Ej1` to `Ej5`, `Ej` being the Spanish short form of *ejercicio*. None of them holds a single formula, validation rule, conditional format, chart or PivotTable: the workbook is input data and instruction text, nothing more. Every answer column ships empty.

The CSV export drops rows and columns that are completely empty, so a line number in a CSV is not the row number in the workbook. The workbook addresses are given in the text below.

### Ej1, the computing school

Two tables and two loose questions, spread over B2:P29. The billing table sits above and the grade table below.

File: [labs/legacy/data/aditional-practices--ej1.csv](data/aditional-practices--ej1.csv), 23 rows by 8 columns.

B2 holds the title `Computing class students`. G2 holds the label `Discount` and H2 the rate, `0.25`, displayed as `25%` by a `0%` number format. The first table has its headers on B4:H4 and its data on B5:E11; columns F, G and H are the answer columns and are empty.

| Name | Course | Weekly cost | # Weeks | Subtotal | Discount | Total |
|---|---|---|---|---|---|---|
| Raúl Flores | Word | 200 | 3 | | | |
| Carlos López | Excel | 300 | 5 | | | |
| Javier Méndez | Word | 200 | 3 | | | |
| Rebeca Guzmán | Internet | 250 | 3 | | | |
| Martín Ceballos | Word | 200 | 3 | | | |
| Mónica Vázquez | Excel | 300 | 5 | | | |
| Claudia Sánchez | Excel | 300 | 5 | | | |

The second table has its headers on B14:F14 and its data on B15:D21. `Grade` and `Status`, columns E and F, are empty.

| Name | Course | Turn | Grade | Status |
|---|---|---|---|---|
| Raúl Jiménez | Word | Morning | | |
| Carlos López | Excel | Morning | | |
| Javier Méndez | Word | Evening | | |
| Rebeca Guzmán | Internet | Morning | | |
| Martín Ceballos | Word | Evening | | |
| Mónica Vázquez | Excel | Evening | | |
| Claudia Sánchez | Excel | Morning | | |

E23:E26 hold four labels down the column, `Total Approved`, `% Approved`, `Total Failed` and `% Failed`, with nothing beside them. B28 and B29 hold two questions in plain text, `How many studens attended the morning Excel course?` and `How many students attended the morning Word course?`, again with no answer cell marked.

The task text sits in J4:J6 for the first table and H14:H26 for the second.

### Ej2, the bank statement

One table of thirty transactions in C3:G33, under a title in C1 merged across C1:G1, `Transaction report Jan-Mar 2019`. The seven questions sit in I3:I18. Deposits and withdrawals are in separate columns and only one of the two is ever filled.

File: [labs/legacy/data/aditional-practices--ej2.csv](data/aditional-practices--ej2.csv), 32 rows by 6 columns.

| Month | Day | Deposit | Withdrawal | Branch |
|---|---|---|---|---|
| Jan | 1 | 5000 | | Díaz Mirón |
| Jan | 5 | | 2000 | Bolívar |
| Jan | 7 | | 1500 | Díaz Mirón |
| Jan | 15 | 4500 | | Bolívar |
| Jan | 17 | | 1200 | Díaz Mirón |
| Jan | 20 | | 1500 | Miguel Alemán |
| Jan | 25 | | 1000 | Bolívar |
| Jan | 29 | | 500 | Miguel Alemán |
| Jan | 31 | 7000 | | Díaz Mirón |
| Jan | 31 | | 1000 | Cuauhtémoc |
| Feb | 3 | | 1000 | Bolívar |
| Feb | 6 | | 1200 | Díaz Mirón |
| Feb | 10 | | 2500 | Cuauhtémoc |
| Feb | 15 | 5500 | | Miguel Alemán |
| Feb | 20 | | 3000 | Díaz Mirón |
| Feb | 25 | 2000 | | Bolívar |
| Feb | 28 | 5000 | | Miguel Alemán |
| Mar | 5 | | 1500 | Cuauhtémoc |
| Mar | 8 | | 1000 | Díaz Mirón |
| Mar | 14 | | 2000 | Bolívar |
| Mar | 16 | 5300 | | Cuauhtémoc |
| Mar | 18 | | 2000 | Cuauhtémoc |
| Mar | 21 | 1500 | | Bolívar |
| Mar | 21 | | 1000 | Díaz Mirón |
| Mar | 23 | | 1500 | Cuauhtémoc |
| Mar | 25 | 2500 | | Díaz Mirón |
| Mar | 25 | | 1000 | Miguel Alemán |
| Mar | 27 | | 1000 | Bolívar |
| Mar | 29 | | 1500 | Díaz Mirón |
| Mar | 31 | 6250 | | Díaz Mirón |

Four branches appear: `Bolívar`, `Cuauhtémoc`, `Díaz Mirón` and `Miguel Alemán`.

### Ej3, the survey and the grade report

Two tables stacked on one sheet, A2:M42.

File: [labs/legacy/data/aditional-practices--ej3.csv](data/aditional-practices--ej3.csv), 34 rows by 13 columns.

The first table sits under a title in B2 merged across B2:E2, `Personal information`, with headers on B4:E4 and data on A5:D19; the row numbers are in column A and the `Notes` column, E, is empty.

| # | Student | Father's education level | Monthly income | Notes |
|---|---|---|---|---|
| 1 | Raúl Flores | Sin estudios | 4800 | |
| 2 | Carlos López | Secundaria | 6000 | |
| 3 | Javier Méndez | Licenciatura | 12000 | |
| 4 | Rebeca Guzmán | Posgrado | 18000 | |
| 5 | Martín Ceballos | Licenciatura | 13500 | |
| 6 | Mónica Vázquez | Preparatoria | 7000 | |
| 7 | Víctor Gutiérrez | Secundaria | 6500 | |
| 8 | Andrés Morales | Primaria | 6200 | |
| 9 | Saúl Viveros | Licenciatura | 10000 | |
| 10 | Laura Flores | Sin estudios | 4000 | |
| 11 | Daniela Jimenez | Primaria | 5500 | |
| 12 | Raul Cancino | Secundaria | 6800 | |
| 13 | Miguel Carmona | Posgrado | 20000 | |
| 14 | Rebeca Torres | Preparatoria | 9000 | |
| 15 | Victoria Barrios | Preparatoria | 8200 | |

To the right, H4 holds the label `Average monthly income` and H6 the label `Percentage of education level:`, with six column labels underneath in H7:M7: `No studies`, `Primary`, `Secondary`, `High school`, `Undergraduate`, `Graduate`. No cell is marked for either answer.

The second table sits under a title in C21 merged across C21:I21, `Final Grades Report by subject`, with headers on B22:J22 and data on A23:H37. `Approved subjects` and `Result`, columns I and J, are empty.

| # | Student | Subject1 | Subject2 | Subject3 | Subject4 | Subject5 | Subject6 |
|---|---|---|---|---|---|---|---|
| 1 | Raúl Flores | 5 | 9 | 10 | 5 | 6 | 10 |
| 2 | Carlos López | 8 | 3 | 3 | 8 | 8 | 9 |
| 3 | Javier Méndez | 4 | 10 | 7 | 3 | 10 | 4 |
| 4 | Rebeca Guzmán | 9 | 10 | 9 | 5 | 4 | 4 |
| 5 | Martín Ceballos | 5 | 10 | 9 | 10 | 5 | 10 |
| 6 | Mónica Vázquez | 5 | 2 | 7 | 7 | 6 | 4 |
| 7 | Víctor Gutiérrez | 7 | 9 | 5 | 10 | 10 | 8 |
| 8 | Andrés Morales | 5 | 3 | 7 | 4 | 6 | 10 |
| 9 | Saúl Viveros | 9 | 4 | 9 | 4 | 6 | 9 |
| 10 | Laura Flores | 4 | 10 | 7 | 6 | 10 | 8 |
| 11 | Daniela Jimenez | 8 | 3 | 7 | 4 | 8 | 10 |
| 12 | Raul Cancino | 9 | 7 | 5 | 4 | 5 | 5 |
| 13 | Miguel Carmona | 10 | 10 | 10 | 3 | 10 | 10 |
| 14 | Rebeca Torres | 9 | 10 | 5 | 9 | 4 | 10 |
| 15 | Victoria Barrios | 3 | 6 | 4 | 4 | 6 | 10 |

The task text is scattered around both tables: G10 and G13 beside the survey, L28:L30 and L32:L33 beside the grades.

### Ej4, the sales log for PivotTables

One table of twenty-nine sales in B2:F31, spanning March 2017 to September 2019. The task text sits in H1:H8.

File: [labs/legacy/data/aditional-practices--ej4.csv](data/aditional-practices--ej4.csv), 31 rows by 6 columns.

Dates are real dates displayed as `mm-dd-yy` and are written below as year first for clarity. `Amount` carries an accounting currency format with a dollar sign.

| Date | Vendor | Store | Product | Amount |
|---|---|---|---|---|
| 2017-03-17 | Carlos Vasquez | Tienda A | Laptop i3 | 1000 |
| 2017-03-20 | Juan Carlos | Tienda B | Impresora | 200 |
| 2017-03-22 | Pedro Noriega | Tienda B | Laptop i5 | 3500 |
| 2017-04-20 | José Almanares | Tienda C | Impresora | 100 |
| 2017-04-17 | Carlos Vasquez | Tienda A | Pantalla 42 | 100 |
| 2017-05-22 | Juan Carlos | Tienda C | Teclado | 20 |
| 2017-05-22 | Pedro Noriega | Tienda C | Mouse | 10 |
| 2017-05-24 | José Almanares | Tienda A | Teclado | 20 |
| 2017-05-17 | José Almanares | Tienda D | Laptop i7 | 4000 |
| 2017-05-20 | Carlos Vasquez | Tienda C | Laptop i7 | 4000 |
| 2017-05-27 | Juan Carlos | Tienda C | Pantalla 17 | 180 |
| 2017-05-20 | Pedro Noriega | Tienda A | Mouse | 10 |
| 2017-05-17 | José Almanares | Tienda D | Teclado | 30 |
| 2018-05-18 | Carlos Vasquez | Tienda B | Laptop i3 | 1000 |
| 2018-06-16 | Juan Carlos | Tienda C | USB 3.0.1 | 15 |
| 2018-06-17 | Pedro Noriega | Tienda A | Laptop i7 | 4000 |
| 2018-06-20 | José Almanares | Tienda C | USB 3.0.1 | 15 |
| 2018-06-19 | Carlos Vasquez | Tienda A | Impresora | 100 |
| 2018-07-05 | Juan Carlos | Tienda D | Pantalla 42 | 100 |
| 2018-07-06 | Pedro Noriega | Tienda A | Laptop i3 | 15 |
| 2018-07-08 | José Almanares | Tienda C | Pantalla 42 | 100 |
| 2018-08-04 | Carlos Vasquez | Tienda D | USB 3.0.1 | 15 |
| 2018-08-06 | Juan Carlos | Tienda C | Pantalla 42 | 100 |
| 2018-08-07 | Pedro Noriega | Tienda A | Laptop i7 | 4000 |
| 2018-09-01 | José Almanares | Tienda A | Pantalla 42 | 100 |
| 2018-09-04 | Carlos Vasquez | Tienda B | Impresora | 100 |
| 2019-09-05 | Juan Carlos | Tienda A | Laptop i3 | 1000 |
| 2019-09-08 | Pedro Noriega | Tienda D | Laptop i5 | 3500 |
| 2019-09-20 | José Almanares | Tienda B | USB 3.0.1 | 15 |

Four vendors, four stores and nine products. The product `Impresora ` carries a trailing space in every row that holds it.

### Ej5, the sales log for advanced filters

One table of fifty-nine sales in A1:H60, weekly from 15 March 2019 to 24 April 2020. The task text sits in J1:J9. This sheet is past the forty row limit for an inline table, so it is linked rather than printed.

File: [labs/legacy/data/aditional-practices--ej5.csv](data/aditional-practices--ej5.csv), 60 rows by 9 columns, the header row and the instruction column included.

| Column | Header | What it holds |
|---|---|---|
| A | `Date` | a real date, format `d-mmm-yy`, from 2019-03-15 to 2020-04-24, mostly one per week |
| B | `Vendor` | `Carlos Vasquez`, `Juan Carlos`, `Pedro Noriega`, `José Almanares` |
| C | `Store` | `Tienda A` to `Tienda D` |
| D | `Product` | nine products, the same list as `Ej4`, with `Impresora ` again carrying a trailing space |
| E | `Quantity` | 1 to 10, format `#,##0` |
| F | `Unit Price` | ten distinct prices, 15, 80, 90, 180, 890, 950, 1800, 2900, 3500 and 9500, format `"$"#,##0.00` |
| G | `Total Sales` | quantity times unit price, typed as a static number in all 59 rows, format `"$"#,##0.00` |
| H | `Year` | the year of column A repeated as a number, 42 rows in 2019 and 17 in 2020 |

## What to do

There is no instruction document. What follows is the text found in the cells of each sheet, in the order it reads down the column, cleaned of the line breaks the narrow columns forced on it. The cell address of each instruction is given so it can be traced back.

### Ej1

1. Calculate `Subtotal` (cost times number of weeks), `Discount` and `Total` (subtotal minus discount), in F5:H11. (J4)
2. Calculate the discount taking into account that it applies only to Excel courses, using the rate in H2. (J5)
3. Format numbers as currency. (J6)
4. Insert grades between 0 and 100 in the `Grade` column, E15:E21, and validate the cells so that numbers outside that range are not allowed. (H14, H15)
5. Determine each student's status in F15:F21: `Approved` if the grade is equal to or greater than 70, `Failed` otherwise. (H16 to H18)
6. Use conditional formatting to highlight in red the students who failed, and in blue the students who passed. (H20, H21)
7. Block the cells of the `Status` column. (H23)
8. Create a 3-D column chart showing the students and their grades. (H25)
9. Create a bar chart showing `Total approved` and `Total failed`. (H26)

The four labels in E23:E26 imply four more answers, `Total Approved`, `% Approved`, `Total Failed` and `% Failed`, and the two questions in B28 and B29 imply two more, the number of students in the morning Excel course and in the morning Word course. No instruction cell mentions any of the six, and no cell is marked to hold them.

### Ej2

Seven questions, all of them answerable with one conditional count or conditional sum over C3:G33. No answer cells are marked, so the answers go beside the questions.

10. How many deposits were made during January? (I3)
11. How much was deposited in total during January? (I5)
12. How much was withdrawn at the `Díaz Mirón` branch in February? (I7)
13. How much was deposited at the `Cuauhtémoc` branch in March? (I9)
14. How much is the difference between total deposits and total withdrawals in January, February and March, one answer per month? (I11, with the three month names listed in I12, I13 and I14)
15. How many withdrawals higher than 1000 were made between March 15 and 30? (I16)
16. How many withdrawals were made at the `Miguel Alemán` branch in February and March? (I18)

### Ej3

17. Fill the `Notes` column, E5:E19: if the monthly income is 6000 or less, it should say `Scholarship candidate`. (G10)
18. Use currency format on the monthly income column. The cell repeats itself in Spanish: *Dale formato de moneda a las cantidades de la columna Ingreso mensual*. (G13)
19. Calculate the average monthly income, beside the label in H4. (H4)
20. Calculate the percentage of students at each education level, under the six labels in H7:M7. (H6)
21. Count each student's approved subjects in column I, I23:I37. (implied by the header in I22; no instruction cell says it)
22. Fill the `Result` column, J23:J37: if the number of failed subjects is greater than 2 the result is `Take general exam`, otherwise the result is the average of the six subjects. (L28 to L30)
23. Use conditional formatting with a red font and a yellow fill on the cells showing `Take general exam`. (L32, L33)

### Ej4

24. Create a PivotTable for each of the five reports below, from the table in B2:F31. (H2)
25. Show the sum of the amount per vendor, grouped by store. (H4)
26. Show the sum of the amount per store, grouped by date, year and month. (H5)
27. Show the sum of the amount by store, grouped by date, year and month, and add a slicer by vendor. (H6)
28. Show the average sales per vendor, grouped by store, and insert a timeline. (H7)
29. Show the sum of sales per vendor, grouped by store, and insert a calculated field that works out a 10 per cent discount on the amount of sales. (H8)

### Ej5

30. Starting on cell J15, present the six filters below, over the table in A1:H60. (J3)
31. Show all data for the years 2019 and 2020. (J4)
32. Show the data from March to May 2019, showing only date, product and total sales. (J5)
33. Show the data from stores A and B for the products `Impresora` and `Laptop i7`, showing only the vendor, store and total sales columns. (J6)
34. Show vendors starting with `C`, showing only the store, vendor and total sales columns. (J7)
35. Show only prices between 8000 and 10 000, showing only product and price. (J8)
36. Show vendors whose names start with `C` and `J`. (J9)

## Checks

Nothing in the source states the answers, so the figures below were recalculated from the data in the sheets. They hold for the rules as written and change if a threshold is read differently, which is flagged where it happens.

**Ej1.** The billing table, with a 25 per cent discount on Excel courses only:

| Name | Course | Subtotal | Discount | Total |
|---|---|---|---|---|
| Raúl Flores | Word | 600 | 0 | 600 |
| Carlos López | Excel | 1500 | 375 | 1125 |
| Javier Méndez | Word | 600 | 0 | 600 |
| Rebeca Guzmán | Internet | 750 | 0 | 750 |
| Martín Ceballos | Word | 600 | 0 | 600 |
| Mónica Vázquez | Excel | 1500 | 375 | 1125 |
| Claudia Sánchez | Excel | 1500 | 375 | 1125 |

The seven totals add up to 5,925. The two questions at the foot of the sheet answer 2 for the morning Excel course, Carlos López and Claudia Sánchez, and 1 for the morning Word course, Raúl Jiménez. Everything downstream of the `Grade` column depends on grades the student invents, so only the rules can be checked there: the validation must reject 101 and accept 100, the status column must flip at exactly 70, and the two colours must follow the status and not the grade.

**Ej2.** The seven questions, answered, with the fifth split into its three months:

| Question | Answer |
|---|---|
| Deposits made during January | 3 |
| Total deposited during January | 16,500 |
| Withdrawn at Díaz Mirón in February | 4,200 |
| Deposited at Cuauhtémoc in March | 5,300 |
| Deposits minus withdrawals, January | 16,500 less 8,700, so 7,800 |
| Deposits minus withdrawals, February | 12,500 less 7,700, so 4,800 |
| Deposits minus withdrawals, March | 15,550 less 12,500, so 3,050 |
| Withdrawals over 1000 between March 15 and 30 | 3 |
| Withdrawals at Miguel Alemán in February and March | 1 |

Question 6 says between March 15 and 30, which leaves out the withdrawal of 31 March; there is none that day, so the reading does not change the answer. The whole sheet totals 44,550 deposited and 28,900 withdrawn.

**Ej3.** The average monthly income is 9,166.67 over the fifteen students, from a total of 137,500. The education levels count 2 `Sin estudios`, 2 `Primaria`, 3 `Secundaria`, 3 `Preparatoria`, 3 `Licenciatura` and 2 `Posgrado`, which is 13.33, 13.33, 20, 20, 20 and 13.33 per cent in the order of the labels in H7:M7. Four students carry `Scholarship candidate` on an income of 6000 or less: Raúl Flores, Carlos López, Laura Flores and Daniela Jimenez.

For the grade report, the average of the six subjects per student is:

| Student | Average | Subjects below 6 |
|---|---|---|
| Raúl Flores | 7.50 | 2 |
| Carlos López | 6.50 | 2 |
| Javier Méndez | 6.33 | 3 |
| Rebeca Guzmán | 6.83 | 3 |
| Martín Ceballos | 8.17 | 2 |
| Mónica Vázquez | 5.17 | 3 |
| Víctor Gutiérrez | 8.17 | 1 |
| Andrés Morales | 5.83 | 3 |
| Saúl Viveros | 6.83 | 2 |
| Laura Flores | 7.50 | 1 |
| Daniela Jimenez | 6.67 | 2 |
| Raul Cancino | 5.83 | 4 |
| Miguel Carmona | 8.83 | 1 |
| Rebeca Torres | 7.83 | 2 |
| Victoria Barrios | 5.50 | 3 |

The second column counts subjects below 6, which is the usual pass mark on a ten point scale, and the sheet never says so. On that reading six students take the general exam: Javier Méndez, Rebeca Guzmán, Mónica Vázquez, Andrés Morales, Raul Cancino and Victoria Barrios. Move the pass mark to 7 and the count changes for almost everyone, so grade the formula rather than the list.

**Ej4.** The twenty-nine sales total 27,345. By vendor: Carlos Vasquez 6,315, Juan Carlos 1,615, Pedro Noriega 15,035, José Almanares 4,380. By store: Tienda A 10,345, Tienda B 4,815, Tienda C 4,540, Tienda D 7,645. Every PivotTable that sums the amount must reach 27,345 in its grand total, whatever it is grouped by.

**Ej5.** The row counts each filter should extract:

| Filter | Rows |
|---|---|
| Years 2019 and 2020 | 59, which is the whole table |
| March to May 2019 | 12 |
| Stores A and B, products Impresora and Laptop i7 | 10 |
| Vendors starting with C | 15 |
| Unit price between 8000 and 10000 | 6, all of them at 9500 |
| Vendors starting with C or J | 45 |

The fifth filter reads `prices`, and on total sales rather than unit price the answer is 4 instead of 6.

## Notes on the source

- The workbook is called `Aditional practices.xlsx`, one `d` short of additional. The sheet names `Ej1` to `Ej5` are the Spanish abbreviation of *ejercicio*, and they are the only ordering the file gives.
- There is no instruction document for this workbook, and no evidence one ever existed. Every other exercise in the folder has a `.docx` beside it; this one has the task text typed into cells to the right of the data instead. What is written above is therefore the whole of it: no objectives, no due date, no hand-in format, no marking scheme, and no statement of which of the five sheets belong together.
- The instruction cells are ordinary cells, not text boxes, so they sit in the print range and in the used range of every sheet. They are also part of the data as far as any filter or PivotTable is concerned, which matters on `Ej5`, where the instructions occupy column J and the results are told to start at J15.
- The English is the instructor's own and carries a steady run of typos: `amout` for amount on `Ej4`, `alumn` for student, `grater` for greater, `formating`, `highligh` and `studens` on `Ej1`, and `Insert grades` where `enter grades` is meant.
- `Ej3` cell G13 gives the same instruction twice, once in English and once in Spanish, in one cell: `Use currency format in the monthly income Dale formato de moneda a las cantidades de la columna Ingreso mensual.`
- Also on `Ej3`, the education levels in column C are in Spanish, `Sin estudios`, `Primaria`, `Secundaria`, `Preparatoria`, `Licenciatura` and `Posgrado`, while the six labels waiting for the percentages in H7:M7 are in English. A COUNTIF has to match the Spanish strings, not the headings above it.
- `Ej3` never states the pass mark for a subject, although the whole `Result` column turns on the count of failed subjects. It also never says what should happen to the `Approved subjects` column in I; only the header names it.
- `Ej1` never states the pass mark for the summary block either, although the status rule two instructions earlier gives 70, and the block asks for counts and percentages that no instruction mentions.
- `Ej2` stores the month as text in one column and the day as a number in another, so there are no real dates on that sheet. The question about withdrawals between March 15 and 30 has to be answered with a compound criterion on two columns, not with a date filter.
- `Ej2` marks no answer cells at all. The questions sit in column I with blank rows between them, which is where the answers were presumably meant to go.
- `Ej4` and `Ej5` share four vendor names and nine product names, but they are two different tables: `Ej4` runs 2017 to 2019 with an `Amount` column, `Ej5` runs 2019 to 2020 with quantity, unit price and total sales.
- The product `Impresora ` carries a trailing space on both sheets, seven rows of it on `Ej5`. Advanced Filter matches text criteria by prefix, so a criterion of `Impresora` still catches it, while an exact-match formula such as `=D2="Impresora"` does not.
- `Ej5` column H repeats the year of column A as a static number, and column G repeats quantity times unit price as a static number. Both agree with their sources in all 59 rows, and neither is a formula, so editing a price leaves the total behind.
- `Ej5` filter 1 asks for the years 2019 and 2020, which is every row in the table. As a filter it teaches the criteria range and returns the whole list.
- `Ej5` filter 6 asks for vendors starting with `C` and `J`. Read as `C` or `J` it catches Carlos Vasquez, Juan Carlos and José Almanares, 45 of the 59 rows; read as `C` and `J` at once it catches nothing. The first reading is the only one that returns rows.
- `Ej5` says the results start at cell J15, but the instruction text itself occupies J1 to J9, and nowhere on the sheet is a criteria range marked out. Six filters copied to one column starting at J15 will run into each other unless the student spaces them, and the source gives no spacing.
