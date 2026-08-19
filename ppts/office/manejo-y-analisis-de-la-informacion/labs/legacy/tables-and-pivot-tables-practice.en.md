# Tables and PivotTables · additional practice

A bookshop inventory of thirty-seven titles with four months of sales against each one. The missing pieces get filled in first, including a format column that has to be generated at random and then translated through a small lookup table and coloured by its value. Then the range becomes a real Excel table, and the Quick Analysis button does the rest: totals, averages, two PivotTables, sparklines, a stacked bar chart and a colour scale, followed by slicers. It is extra practice rather than a graded homework, and it is the one file in the legacy set that walks the whole Quick Analysis menu.

**Objectives** MO-200 3.1.1, MO-200 3.1.2, MO-200 2.1.1, MO-200 3.2.3, MO-200 2.2.5, MO-200 2.2.2, MO-200 2.4.1, MO-200 2.4.2, MO-200 3.3.2, MO-200 5.1.1, MO-201 3.2.1, MO-201 4.2.1, MO-201 4.2.3

## The data

One sheet, `Hoja1`, in `Tables and pivot tables additional practice.xlsx`. The used range is `A1:P39`: header on row 1, thirty-seven books on rows 2 to 38, and a leftover totals row on 39.

File: [labs/legacy/data/tables-and-pivot-tables-additional-pra--hoja1.csv](data/tables-and-pivot-tables-additional-pra--hoja1.csv), 39 rows by 16 columns.

Two of the sixteen columns arrive empty and are the ones to fill: `G`, `Format`, and `N`, `Sparkline`. Everything else is populated. The book metadata is in Spanish, titles, genres and publishers alike, in an otherwise English sheet.

| Book code | Author's surname | Author's name | Book title | Gender | Editorial | Format | Cost | Sale price | Units sold January | Units sold February | Units sold March | Units sold April | Sparkline | Initial Inventory | Final Inventory |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 111 | Ruiz Zafón | Carlos | Marina | Novela negra | Planeta |  | 150 | 300 | 41 | 31 | 82 | 34 |  | 759 | 571 |
| 112 | Falcones | Ildefonso | La Catedral del Mar | Histórica | Del Bolsillo |  | 25 | 75 | 35 | 55 | 57 | 20 |  | 602 | 435 |
| 113 | Foenkinos | David | Hacia la belleza | Romance | Alfaguara |  | 25 | 100 | 11 | 48 | 54 | 86 |  | 893 | 694 |
| 114 | Luiselli | Valeria | Los Ingrávidos | Novela corta | Sexto Piso |  | 25 | 150 | 9 | 38 | 72 | 44 |  | 781 | 618 |
| 115 | Melchor | Fernanda | Temporada de huracanes | Novela corta | Random House |  | 100 | 250 | 41 | 6 | 89 | 54 |  | 642 | 452 |
| 116 | García Márquez | Gabriel | Cien años de Soledad | Novela | Diana |  | 25 | 150 | 83 | 30 | 57 | 88 |  | 888 | 630 |
| 117 | Follett | Ken | Los Pilares de la Tierra | Histórica | Random House |  | 300 | 400 | 61 | 28 | 19 | 62 |  | 674 | 504 |
| 118 | Ruiz Zafón | Carlos | El Juego del Ángel | Misterio | Planeta |  | 25 | 50 | 7 | 37 | 74 | 68 |  | 648 | 462 |
| 119 | Rand | Ayn | El Manantial | Novela Filosófica | Ediciones Orbis |  | 25 | 50 | 35 | 65 | 21 | 80 |  | 724 | 523 |
| 120 | Hernández | Miguel | Poesía | Poesía | Seix Barral |  | 85 | 100 | 54 | 60 | 1 | 58 |  | 811 | 638 |
| 121 | Follett | Ken | La Boca del Dragón | Suspenso | Grijalvo |  | 20 | 30 | 79 | 78 | 5 | 11 |  | 572 | 399 |
| 122 | Salcido | Iván | El Terremoto de 2017 | Histórica | Casa de las campanas editores |  | 20 | 30 | 59 | 41 | 27 | 30 |  | 742 | 585 |
| 123 | Varios | autores | Cuentos rusos clasicos | Cuentos | Servicios pedagógicos |  | 75 | 100 | 39 | 15 | 89 | 48 |  | 740 | 549 |
| 124 | Beevor | Anthony | La Batalla por los puentes | Histórica | Paidós |  | 25 | 50 | 0 | 41 | 8 | 6 |  | 897 | 842 |
| 125 | Sánchez Pardós | Daniel | Una Ciudad convulsa | Histórica | Planeta |  | 90 | 130 | 16 | 35 | 61 | 77 |  | 531 | 342 |
| 126 | Jones | Sherry | La Joya de Medina | Histórica | Quebecor World |  | 25 | 50 | 68 | 71 | 90 | 27 |  | 879 | 623 |
| 127 | Wallace | Irwing | La Palabra | Misterio | Grijalvo |  | 15 | 30 | 31 | 2 | 35 | 47 |  | 548 | 433 |
| 128 | Waltari | Mika | El Etrusco | Histórica | Liberduplex |  | 100 | 150 | 3 | 86 | 22 | 5 |  | 692 | 576 |
| 129 | González Olivo | Marisol | Leyendas Mexicanas de todos los tiempos | Cuentos | Editores Mexicanos Unidos |  | 50 | 75 | 84 | 49 | 39 | 26 |  | 535 | 337 |
| 130 | Anónimo |  | Las mil y una noches | Cuentos | Editores Mexicanos Unidos |  | 50 | 70 | 66 | 87 | 38 | 86 |  | 600 | 323 |
| 131 | Stevenson | Robert Louis | La Isla del Tesoro | Aventura | Forum SA |  | 25 | 50 | 5 | 11 | 89 | 11 |  | 636 | 520 |
| 132 | Twain | Mark | Un Yankee en la Corte del Rey Arturo | Aventura | Forum SA |  | 20 | 30 | 11 | 7 | 46 | 79 |  | 742 | 599 |
| 133 | Eurípides |  | Tragedias | Tragedia | Secretaría de Eduación Pública |  | 90 | 135 | 64 | 86 | 14 | 23 |  | 516 | 329 |
| 134 | Varios | Autores | Cartografías de las Islas Mexicanas | Geografía | Comunicación y ediciones Tracuilo  |  | 250 | 350 | 79 | 19 | 72 | 38 |  | 577 | 369 |
| 135 | Azar | Héctor | Entre las horas detenido | Novela | Porrúa |  | 200 | 400 | 5 | 79 | 85 | 67 |  | 858 | 622 |
| 136 | Varios | Autores | México, esplendores de 30 siglos | Histórica | Friends of the arts of Mexico |  | 400 | 550 | 81 | 54 | 30 | 51 |  | 752 | 536 |
| 137 | De Saint- Exupéry | Antoine | El Principito | Infantil | Del Bolsillo |  | 25 | 60 | 61 | 78 | 65 | 69 |  | 723 | 450 |
| 138 | Vargas Llosa | Mario | La ciudad y los perros | Aventura | Del Bolsillo |  | 20 | 50 | 67 | 6 | 59 | 17 |  | 818 | 669 |
| 139 | Marías | Javier | Los enamoramientos | Romance | Del Bolsillo |  | 150 | 300 | 48 | 86 | 43 | 77 |  | 862 | 608 |
| 140 | Amkie | Lorena | El club de los perdedores | Juvenil | Rústico |  | 25 | 85 | 23 | 24 | 80 | 10 |  | 797 | 660 |
| 141 | Padura | Leonardo | El hombre que amaba a los perros | Histórica | Tusquets |  | 180 | 300 | 4 | 43 | 48 | 46 |  | 823 | 682 |
| 142 | Dumas | Alejandro | La dama de las camelias | Romance | Del Bolsillo |  | 20 | 55 | 53 | 62 | 46 | 39 |  | 644 | 444 |
| 143 | Kundera | Milan | La insoportable levedad del ser | Novela Filosófica | Tusquets |  | 150 | 300 | 67 | 1 | 13 | 5 |  | 863 | 777 |
| 144 | Hesse | Hermann | El lobo estepario | Novela | Rústico |  | 20 | 75 | 77 | 47 | 65 | 30 |  | 750 | 531 |
| 145 | Allende | Isabel | El amante japonés | Romance | Plaza Janés |  | 25 | 90 | 11 | 22 | 17 | 18 |  | 562 | 494 |
| 146 | Arreola | Juan José | Bestiario | Cuentos | Booket |  | 50 | 180 | 70 | 82 | 44 | 55 |  | 866 | 615 |
| 147 | Miller | Madeline | Circe | Histórica | Alianza |  | 25 | 70 | 41 | 70 | 18 | 8 |  | 614 | 477 |

**Row 39** is not a book. It holds `1589`, `1680`, `1774` and `1600` under the four month columns, `717.8648648648649` under `Initial Inventory`, and `37` under `Final Inventory`. See the notes at the end for what those are.

**The format lookup table**, given in the instruction document rather than in the workbook. It has to be typed onto the sheet before the format column can be filled.

| No. | Format | Colour |
|---|---|---|
| 1 | PDF | Blue |
| 2 | Pocket | Green |
| 3 | Hardcover | Red |
| 4 | Audiobook | Grey |

## What to do

Complete the table and analyse the sales behaviour.

1. Fill in the missing table information.
   - Format the `Sales` and `Cost` columns as currency. Route MO-200 2.2.5. On this sheet those are `I`, `Sale price`, and `H`, `Cost`.
   - Centre the units sold per month, columns `J` to `M`. Route MO-200 2.2.2.
   - Fill the `Format` column, `G2:G38`, from the four-row table above, using RANDBETWEEN to draw a number from 1 to 4 and LOOKUP to turn it into the format name. Route MO-201 3.2.1 for the lookup.
   - Colour each format cell according to its value, using conditional formatting: PDF blue, Pocket green, Hardcover red, Audiobook grey. Route MO-200 2.4.2, **Highlight Cells Rules**, **Equal To...**, four times, with **Custom Format...** for the fills.
2. Final inventory is the initial inventory minus the sales of the four months, that is `O` minus the sum of `J` to `M`.
3. Sort the information by book code. Route MO-200 3.3.2.
4. Convert the range of cells holding the inventory information into a Table, with a style. **Home**, **Styles**, **Format as Table**. Routes MO-200 3.1.1 and MO-200 3.1.2.
5. Use the Quick Analysis button, the small icon that appears at the bottom right corner of a selection, to:
   - get the sum of sales per month, from the **Totals** tab;
   - get the average cost and the average sales, also from **Totals**;
   - generate two PivotTables, from the **Tables** tab. Route MO-201 4.2.1;
   - get the sparkline of sales by month for each product, from the **Sparklines** tab. Route MO-200 2.4.1. The sparklines belong in column `N`, the empty column left for them between April and the initial inventory;
   - generate a stacked bar chart of sales by month, from the **Charts** tab. Route MO-200 5.1.1;
   - include a colour scale for price, from the **Formatting** tab.
6. Add slicers and see that they work the same way filters do. Route MO-201 4.2.3.

## Checks

The four month columns total 1,589 in January, 1,680 in February, 1,774 in March and 1,600 in April, and 6,643 across the four. Those four figures are already sitting on row 39 of the shipped file, so they are a check on the totals row rather than a discovery.

The initial inventory column totals 26,561 across the 37 books, giving an average of 717.8648648648649. The final inventory column totals 19,918. The difference between the two, 6,643, is the total units sold, which is the arithmetic check that task 2 was applied to every row and only to the book rows.

Task 2 is already satisfied by the shipped file. All 37 rows already hold a final inventory equal to the initial inventory minus the four months, so recalculating the column must change nothing. If a value moves, the formula picked up row 39 or missed a month.

Task 3 is also already satisfied. The book codes run 111 to 147 in order with no gaps, so a correct sort leaves the sheet exactly as it was. That makes the sort a poor check on its own; the way to see it worked is to sort by a different column first and then sort back.

The format column cannot be checked against a fixed answer, because RANDBETWEEN redraws on every recalculation. What can be checked is that all 37 cells hold one of exactly four strings, that each string carries the colour the lookup table assigns it, and that pressing `F9` reshuffles both the words and the colours together. If the words change and the colours do not follow, the fills were painted by hand instead of by a rule. If the exercise is to be handed in with a fixed set of formats, copy `G2:G38` and paste back over itself as values first, route MO-200 2.1.1.

Cost runs from 15 to 400 and sale price from 30 to 550, so the colour scale on price has a real spread to work with. Sale price is above cost on every one of the 37 rows.

## Notes on the source

- The workbook lives in the Tareas folder alongside the numbered homework sets, but it is not numbered and the instruction document does not give it a homework number. It is titled `TABLES AND PIVOT TABLES ADDITIONAL PRACTICE`. The folder holds no homework 10; the numbered set runs 1 to 9 and then jumps to 11, and nothing has been renumbered here to close the gap.
- Row 39 holds five numbers that are typed values, not formulas. Four of them are the column sums of the month columns and are correct. The fifth, `717.8648648648649` under `Initial Inventory`, is the average of that column rather than its sum. The sixth, `37` under `Final Inventory`, is the count of books, sitting in the column where a sum would be expected. It looks like the residue of somebody else's pass through the Quick Analysis **Totals** tab, where **Sum**, **Average** and **Count** sit next to each other and are easy to apply to the wrong column. It is worth clearing row 39 before handing the file out, because task 4 turns the range into a table and a stray row of literals directly under the data will be swallowed as a thirty-eighth record.
- The `Format` column and the `Sparkline` column are empty and the instruction document never says where the format lookup table should be typed. Anywhere off to the right of column `P` works and keeps it out of the table range.
- `Gender` in `E1` means genre. It is a literal rendering of the Spanish `género`, which carries both meanings. `Editorial` in `F1` means publisher, likewise. Neither is corrected here, because a task that names a column has to name the column the sheet actually has.
- The instruction document says to use RANDBETWEEN and LOOKUP for the format column but never says to freeze the result. A workbook handed in with live RANDBETWEEN shows a different set of formats every time it is opened, and the conditional formatting colours move with it. Whether that is acceptable is not addressed by the source.
- The four colours in the format table, blue, green, red and grey, are given as words with no hex values and no reference to a theme, so any reasonable fill of each colour satisfies the task.
- Task 5 lists six things to do through Quick Analysis, and two of them are not on the Quick Analysis menu in the form the task describes. Quick Analysis offers PivotTable recommendations rather than a way to specify what two PivotTables should contain, and the task does not say what either one should summarise. The stacked bar chart is offered under **Charts** only when the selection has a shape Excel can read that way, and a selection of the whole 16-column table generally will not. Both are easier to reach from the **Insert** tab, and the source does not say the Quick Analysis route is required.
- Title 136 is `México, esplendores de 30 siglos`, whose comma inside the value is why that field is quoted in the CSV. Row 130 has an author's surname of `Anónimo` and no first name, and rows 123, 134 and 136 have `Varios` as the surname with `autores` or `Autores` as the first name, in two different capitalisations. Row 133, `Eurípides`, likewise has no first name.
