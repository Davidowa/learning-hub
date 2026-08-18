# Solutions · Information Analysis and Processing · TIA503

The instructor's copy. It carries the run solution to every exercise, the expected output, a ten-point rubric and the mistake that turns up most often when marking. The numbering matches the exercises file. Amounts use the decimal point and the thousands comma, the way Excel types them. Everything below was measured on Excel 16.0 with an English interface, and where the result depends on the machine, on the interface language or on an iteration, the solution says so instead of inventing an exact figure.

---

## Week 01 · Course framing and the first recorded macro

### 01.1 · Recognise

**Solution**

When it finishes, column D is hidden and column E is visible. The two lines touching E cancel each other: the second hides it and the third brings it back.

For the third statement line:

| Piece | What it is |
|---|---|
| Object | `Columns("E:E")`, and of that object its `EntireColumn` |
| Property | `Hidden` |
| Value | `False` |

Three statement lines run. Only one of them, the first, changes the final state of the sheet.

**Output**

```text
Column D: hidden
Column E: visible
Lines that run:            3
Lines that leave a mark:   1
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Says D ends hidden and E visible | 4 |
| Separates object, property and value correctly | 3 |
| Tells the three lines that run from the single one that leaves a mark | 3 |

**Most common mistake**

Answering that both end up hidden, because the macro is called `HideCosts`. It gives itself away by never mentioning the third line.

### 01.2 · Apply

**Solution**

```vba
Sub PrepareCatalogue()
    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

Four lines get deleted. The original version finished in the same state because the last line put D back to `True` and E had been left at `False` two lines earlier: the result matched by accident, not by design.

**Output**

```text
Column D: hidden
Column E: visible
Lines deleted: 4
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| One statement line is left and it is the right one | 5 |
| The procedure name did not change and it compiles | 2 |
| Explains why the original reached the same state | 3 |

**Most common mistake**

Leaving two lines, D at `True` and E at `False`, believing the code has to say that E is shown. It gives itself away by writing a statement to leave something exactly as it already was.

### 01.3 · Integrate

**Solution**

What the recorder writes, blank comments and all:

```vba
Sub PrepareCatalogue()
'
' PrepareCatalogue Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = False
    Columns("B:B").EntireColumn.Hidden = True
End Sub
```

Edited, without the lines from the undone click:

```vba
Sub PrepareCatalogue()
    Columns("D:D").EntireColumn.Hidden = True
    Columns("B:B").EntireColumn.Hidden = True
End Sub
```

If the workbook is saved as `.xlsx`, Excel warns that the format holds no code and, if the user accepts, the file is left without the macro. Depending on how the clicks fell, the recorder may also write lines of `Select` and `Selection`; they come out the same way, and week 6 explains why they were spare.

**Output**

```text
Before running:  B visible, C visible, D visible, E visible
After running:   B hidden,  C visible, D hidden,  E visible
Second run:      the same state, nothing changed
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The workbook is an `.xlsm` and the macro runs from the macro dialog | 2 |
| Hands in the recorded code and the edited code, and the difference shows | 4 |
| The edited version leaves B and D hidden and is idempotent | 2 |
| Explains what happens on saving as `.xlsx` | 2 |

**Most common mistake**

Handing in only the edited version. Without the original code there is no way to mark what was cut, and the exercise asked for both.

---

## Week 02 · Unit 1 · The VBA editor

### 02.1 · Recognise

**Solution**

Only `LoadTargets` turns up in the macro dialog. The dialog lists the procedures of the standard modules; `AnnounceTargets` lives in the sheet module and is not offered from there.

After running `LoadTargets` with F5 the three values are written.

With the yellow highlight on `Range("B3").Value = 95000`, that line has not run yet: B2 is already 120000 and B3 is still empty. The yellow marks what is pending, not what is done.

**Output**

```text
Macro dialog:  LoadTargets

After F5:      B2 = 120000   B3 = 95000   B4 = 143000
Yellow on B3:  B2 = 120000   B3 = (empty)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Only `LoadTargets` shows, and it explains why | 4 |
| The three values of B2, B3 and B4 | 3 |
| B3 empty while the yellow sits on its line | 3 |

**Most common mistake**

Saying B3 is already 95000 because the line is highlighted. It is the first-class confusion in the editor, and it gives itself away by running the rest of the trace one line ahead as well.

### 02.2 · Apply

**Solution**

```vba
Sub ShowSegment()
    MsgBox "Premium segment: 3 campaigns"
End Sub

Sub WriteTotals()
    Range("B2").Value = 3350
    Range("B3").Value = 50250
End Sub

Sub PrepareSummary()
    Call ShowSegment
    Call WriteTotals
End Sub
```

**Output**

```text
Message box:  Premium segment: 3 campaigns

B2 = 3350
B3 = 50250
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `ShowSegment` shows the exact text | 3 |
| `WriteTotals` writes both numbers into the cells asked for | 3 |
| `PrepareSummary` calls both with `Call` and does not repeat their code | 3 |
| The module is named `Campaigns` and is exported as `.bas` | 1 |

**Most common mistake**

Copying the contents of the other two inside `PrepareSummary` instead of calling them. It gives itself away by three identical `MsgBox` lines in the module.

### 02.3 · Integrate

**Solution**

```vba
Sub HideUnitCost()
    Columns("D:D").EntireColumn.Hidden = True
    MsgBox "Cost column hidden"
End Sub

Sub ShowUnitCost()
    Columns("D:D").EntireColumn.Hidden = False
    MsgBox "Cost column visible"
End Sub

Sub ReviewCatalogue()
    Call HideUnitCost
    Range("F1").Value = "Reviewed"
End Sub
```

The trace, starting with column D visible and F1 empty:

| F8 | Highlighted line | Column D | F1 |
|---|---|---|---|
| step 1 | `Sub ReviewCatalogue()` | visible | empty |
| step 2 | `Call HideUnitCost` | visible | empty |
| step 3 | `Sub HideUnitCost()` | visible | empty |
| step 4 | `Columns("D:D")… = True` | visible | empty |
| step 5 | `MsgBox "Cost column hidden"` | hidden | empty |
| step 6 | `End Sub` of `HideUnitCost` | hidden | empty |
| step 7 | `Range("F1").Value = "Reviewed"` | hidden | empty |
| step 8 | `End Sub` of `ReviewCatalogue` | hidden | Reviewed |

**Output**

```text
When it finishes:  column D hidden, F1 = Reviewed
Message boxes in total: one, the one from HideUnitCost
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three procedures run and do what their names say | 3 |
| `ReviewCatalogue` uses `Call` and writes into F1 | 2 |
| The trace respects that the highlight is the pending line | 3 |
| The trace shows F8 stepping into the called procedure | 2 |

**Most common mistake**

Tracing as though `Call` were a single step and F8 did not step into the called procedure. It gives itself away in four-line traces that jump straight from the `Call` to the `End Sub`.

---

## Week 03 · Unit 1 · Types, variables and cells

### 03.1 · Recognise

**Solution**

In (a), C2 ends up at 14. VBA rounds to the nearest even number when a decimal is stored in an `Integer`, so 14.5 comes down to 14 and 15.5 would go up to 16.

In (b), `lastRef = 41020` is the one that stops, with error 6, `Overflow`. `Dim firstRef, lastRef As Integer` declares only the last one `As Integer`: `firstRef` was left a `Variant` and that is why it takes the same number without complaining.

In (c), the message shows 420. Without `Option Explicit`, VBA creates `unts` on the spot, puts 75 in it and leaves `units` at 420. With `Option Explicit` on the first line of the module the project no longer compiles and the editor points at `unts` as an undefined variable.

**Output**

```text
(a)  C2 = 14
(b)  firstRef = 41020
     lastRef    -> Run-time error '6': Overflow
(c)  Message box: 420
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) answers 14 and names the rounding to even | 3 |
| (b) points at `lastRef` and error 6, and explains the `Variant` | 4 |
| (c) answers 420 and says what changes with `Option Explicit` | 3 |

**Most common mistake**

Answering 15 in (a) with the rounding taught at school. It gives itself away when the same student answers 4 for 3.5, which does happen to agree, and does not notice that the rule is a different one.

### 03.2 · Apply

**Solution**

```vba
Option Explicit

Sub SupplierRecord()
    Dim code As String
    Dim supplier As String
    Dim taxId As String
    Dim stock As Long
    Dim unitCost As Double
    Dim active As Boolean
    Dim inventoryValue As Double

    code = "P-101"
    supplier = "Empaques Lira"
    taxId = "ELI980312QX4"
    stock = 180
    unitCost = 64.5
    active = True
    inventoryValue = stock * unitCost

    Range("A1").Value = code
    Range("A1").Offset(0, 1).Value = supplier
    Range("A1").Offset(0, 2).Value = taxId
    Range("A1").Offset(0, 3).Value = stock
    Range("A1").Offset(0, 4).Value = unitCost
    Range("A1").Offset(0, 5).Value = active
    Range("A1").Offset(0, 6).Value = inventoryValue
End Sub
```

**Output**

```text
A1 = P-101
B1 = Empaques Lira
C1 = ELI980312QX4
D1 = 180
E1 = 64.5
F1 = TRUE
G1 = 11610
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Every field with the right type and no `Variant` | 4 |
| The tax ID declared as `String` | 2 |
| Uses `Offset` from A1 for the six following fields | 2 |
| G1 with the inventory value, 11,610 | 2 |

**Most common mistake**

Declaring the tax ID as `Long` because it carries digits. It blows up on assignment, and whoever declares it `Double` gets a number that can no longer be compared against the one in the system.

Grading note: F1 shows `TRUE` because the interface is in English. On a Spanish installation the same `Boolean` shows `VERDADERO`. The cell holds the same value either way, and the wording of that one cell is not marked.

### 03.3 · Integrate

**Solution**

```vba
Option Explicit

Sub InventoryValue()
    Dim stock As Long
    Dim unitCost As Double
    Dim value As Double

    stock = Range("C2").Value
    unitCost = Range("D2").Value
    value = stock * unitCost

    Range("E2").Value = value
    MsgBox value

    Columns("D:D").EntireColumn.Hidden = True
End Sub
```

**Output**

```text
E2 = 77700
Message box: 77700
Column D: hidden
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `Option Explicit` on the first line of the module | 1 |
| Reads C2 and D2 into variables with their type | 3 |
| E2 ends at 77,700 | 3 |
| Shows the message and hides column D | 2 |
| Runs from the macro dialog | 1 |

**Most common mistake**

Writing `Range("E2").Value = Range("C2").Value * Range("D2").Value` and skipping the variables. It runs and gives the right number, but the exercise was marking the declarations and there is nothing there to mark.

---

## Week 04 · Unit 1 · Operations and range names

### 04.1 · Recognise

**Solution**

| Cell | Expression | Ends at |
|---|---|---|
| D2 | `250000 - 180000 / 12` | 235000 |
| D3 | `(250000 - 180000) / 12` | 5833.33333333333 |
| D4 | `100 \ 7` | 14 |
| D5 | `100 Mod 7` | 2 |
| D6 | `-3 ^ 2` | -9 |
| D7 | `7.5 \ 2` | 4 |

The one that changes result depending on where it is written is `-3 ^ 2`. In VBA it gives -9, because the sign applies after the power; as a cell formula, `=-3^2` gives 9.

In the packing problem, D4 is the number of full boxes that come out and D5 is the pieces left loose.

**Output**

```text
D2 = 235000
D3 = 5833.33333333333
D4 = 14
D5 = 2
D6 = -9
D7 = 4

typed into a cell:  =-3^2  ->  9
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The six cells right, one point each | 6 |
| Identifies `-3 ^ 2` and gives the 9 of the cell | 2 |
| Reads D4 and D5 as full boxes and loose pieces | 2 |

**Most common mistake**

Answering 3.75 in D7. The backslash rounds both operands to whole numbers before dividing, so the sum it actually does is 8 divided by 2.

### 04.2 · Apply

**Solution**

```vba
Option Explicit

Sub EquivalentMonthlyRate()
    Dim annual As Double
    Dim monthly As Double

    ThisWorkbook.Names.Add _
        Name:="AnnualInflation", RefersTo:="=Sheet1!$B$1"
    ThisWorkbook.Names.Add _
        Name:="MonthlyInflation", RefersTo:="=Sheet1!$B$2"

    Range("AnnualInflation").Value = 0.065
    annual = Range("AnnualInflation").Value

    monthly = ((1 + annual) ^ (1 / 12)) - 1

    ' B2 keeps the whole number and only how it looks changes.
    ' B3 keeps what Format left of it, and nothing past two decimals survived.
    Range("MonthlyInflation").Value = monthly
    Range("MonthlyInflation").NumberFormat = "0.00%"

    Range("B3").Value = Format(monthly, "0.00%")
    Range("B4").Value = Round(monthly, 6)
End Sub
```

**Output**

```text
B1  0.065
B2  value 0.00526169427684775,  shows 0.53%
B3  value 0.0053,               shows 0.53%
B4  0.005262

Range("B2").Value = Range("B3").Value  ->  False
```

`Format` returns the string `0.53%`. Writing that string into a cell with `.Value` hands it straight back to Excel, which parses it as a percentage and stores 0.0053 with the format `0.00%`. So the two cells read identically on screen and hold different numbers: B2 still carries the whole calculation and B3 carries only what fitted into two decimals.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The two names created with `Names.Add` and used afterwards | 3 |
| The power formula with the right parentheses | 3 |
| B2 with `NumberFormat`, B3 with `Format` and B4 with `Round` | 3 |
| The comment separates what B2 keeps from what B3 lost | 1 |

**Most common mistake**

Writing `1 + annual ^ 1 / 12`. It runs, returns a number and is not the rate: the power resolves before the addition and the division, so both pairs of parentheses are missing.

Grading note one: `RefersTo` carries the real sheet name. On a Spanish Excel the first sheet is called `Hoja1`, not `Sheet1`, and `Names.Add` with the wrong name leaves the name pointing at a broken reference. A submission using the name its own copy of Excel gave the sheet is correct.

Grading note two: `Format` does return a `String`, and students often report B3 as text. What the measurement shows is that the conversion back happens on the write, not in `Format`. Accept either answer as long as the student says what they measured in their own workbook and can show it.

### 04.3 · Integrate

**Solution**

```vba
Option Explicit

Sub ComputeVariance()
    Dim budgeted As Double
    Dim actual As Double
    Dim variance As Double
    Dim proportion As Double

    ThisWorkbook.Names.Add Name:="BudgetTotal", RefersTo:="=Budget!$B$6"
    ThisWorkbook.Names.Add Name:="ActualTotal", RefersTo:="=Budget!$C$6"
    ThisWorkbook.Names.Add Name:="VarianceTotal", RefersTo:="=Budget!$D$6"
    ThisWorkbook.Names.Add Name:="VariancePct", RefersTo:="=Budget!$E$6"

    budgeted = Range("BudgetTotal").Value
    actual = Range("ActualTotal").Value

    variance = actual - budgeted
    proportion = variance / budgeted

    Range("VarianceTotal").Value = variance
    Range("VarianceTotal").NumberFormat = "$#,##0.00"

    Range("VariancePct").Value = proportion
    Range("VariancePct").NumberFormat = "0.00%"
End Sub
```

**Output**

```text
D6  value 64600.5,              shows $64,600.50
E6  value 0.0206062200956938,   shows 2.06%
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four names created and pointing at the right cells | 3 |
| The variance in pesos, 64,600.50 | 2 |
| The proportion over the budget, 2.06 % | 2 |
| Both formats applied | 2 |
| After the names are created no coordinate is left written | 1 |

**Most common mistake**

Dividing the variance by the actual instead of by the budget. It gives 2.02 %, which sounds close enough, and that is what makes it hard to spot in review.

---

## Week 05 · Unit 1 · Data entry and messages

### 05.1 · Recognise

**Solution**

| What they type | IsNumeric | CDbl |
|---|---|---|
| 15 | True | 15 |
| 1,000 | True | 1000 |
| $780.50 | depends on the region, see the note | depends on the region, see the note |
| fifteen | False | error 13 |
| nothing, they pressed Cancel | False | error 13 |

With `fifteen`, the macro stops on the `If` line, with error 13, `Type mismatch`. `And` does not cut out at the first false: VBA evaluates both sides before applying the operator, so `CDbl("fifteen")` runs even though `IsNumeric` has already returned False.

**Output**

```text
Run-time error '13':

Type mismatch
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five rows of the table, one point each | 5 |
| Says it stops on the `If` line | 2 |
| Names error 13 | 1 |
| Explains that `And` evaluates both sides | 2 |

**Most common mistake**

Marking `False` for `1,000`. The thousands comma does get through `IsNumeric` and `CDbl` turns it into 1000, and the student who rejects it is usually validating more than the problem asked for.

Grading note: the currency symbol row depends on the machine's regional setting, so its point is awarded for either answer as long as the student says which region they tested on. `IsNumeric` accepts the currency symbol of the active region and rejects any other. The week 5 slide says `False` and error 13 because it was measured on an Excel set to the United Kingdom, where the symbol is the pound and the dollar sign does not count as currency. Measured on the classroom machine, region United States: `IsNumeric("$780.50")` returns `True` and `CDbl("$780.50")` returns 780.5, while the same string with a pound sign returns `False`. What is not accepted is claiming that no currency symbol ever gets through.

### 05.2 · Apply

**Solution**

```vba
Option Explicit

Sub CaptureDays()
    Dim text As String
    Dim days As Double
    Dim valid As Boolean
    Dim answer As Long

    valid = False
    Do While Not valid
        text = InputBox("Days worked by Ana Robles", "Payroll")

        ' Two nested Ifs and not one with And: in VBA both sides of And
        ' are always evaluated, so CDbl would run over text and blow up.
        If IsNumeric(text) Then
            If CDbl(text) > 0 Then
                days = CDbl(text)
                valid = True
            End If
        End If

        If Not valid Then
            MsgBox "That is not a valid number of days.", vbExclamation
        End If
    Loop

    answer = MsgBox("Save " & days & " days for Ana Robles?", _
                    vbYesNo + vbQuestion, "Confirm")

    If answer = vbYes Then
        Range("C2").Value = days
    End If
End Sub
```

**Output**

```text
Types "fifteen"  ->  box: That is not a valid number of days.  and asks again
Types "-3"       ->  box: That is not a valid number of days.  and asks again
Types "15"       ->  box: Save 15 days for Ana Robles?
   Yes  ->  C2 = 15
   No   ->  C2 stays as it was
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The loop insists until the value is usable | 3 |
| The validation sits in two nested `If` statements | 2 |
| Rejects zero and negatives, not only text | 2 |
| The confirmation compares against `vbYes` and only then writes | 2 |
| The comment explains why `And` is not used | 1 |

**Most common mistake**

Comparing the answer against the button text, something like `If answer = "Yes"`. It never enters the `If`, the macro raises no error and C2 is left empty.

### 05.3 · Integrate

**Solution**

```vba
Option Explicit

Sub CapturePayslip()
    Dim text As String
    Dim valid As Boolean
    Dim wage As Double
    Dim days As Double
    Dim gross As Double
    Dim bonus As Double
    Dim total As Double

    ThisWorkbook.Names.Add Name:="DailyWage", RefersTo:="=Payroll!$B$2"
    ThisWorkbook.Names.Add Name:="DaysWorked", RefersTo:="=Payroll!$B$3"
    ThisWorkbook.Names.Add Name:="GrossPay", RefersTo:="=Payroll!$B$4"
    ThisWorkbook.Names.Add Name:="Bonus", RefersTo:="=Payroll!$B$5"
    ThisWorkbook.Names.Add Name:="TotalPay", RefersTo:="=Payroll!$B$6"

    valid = False
    Do While Not valid
        text = InputBox("Daily wage", "Payslip")
        If IsNumeric(text) Then
            If CDbl(text) > 0 Then
                wage = CDbl(text)
                valid = True
            End If
        End If
        If Not valid Then
            MsgBox "The daily wage has to be greater than zero.", vbExclamation
        End If
    Loop

    valid = False
    Do While Not valid
        text = InputBox("Days worked", "Payslip")
        If IsNumeric(text) Then
            If CDbl(text) > 0 Then
                days = CDbl(text)
                valid = True
            End If
        End If
        If Not valid Then
            MsgBox "The days worked have to be greater than zero.", vbExclamation
        End If
    Loop

    gross = wage * days
    bonus = gross * 0.08
    total = gross + bonus

    Range("DailyWage").Value = wage
    Range("DaysWorked").Value = days
    Range("GrossPay").Value = gross
    Range("Bonus").Value = bonus
    Range("TotalPay").Value = total

    Range("GrossPay").NumberFormat = "$#,##0.00"
    Range("Bonus").NumberFormat = "$#,##0.00"
    Range("TotalPay").NumberFormat = "$#,##0.00"

    MsgBox "Gross: " & Format(gross, "$#,##0.00") & vbNewLine & _
           "Bonus: " & Format(bonus, "$#,##0.00") & vbNewLine & _
           "Total: " & Format(total, "$#,##0.00"), _
           vbInformation, "Payslip"
End Sub
```

**Output**

With a daily wage of 780.50 and 15 days:

```text
B2 = 780.5
B3 = 15
B4 = 11707.5     shows $11,707.50
B5 = 936.6       shows $936.60
B6 = 12644.1     shows $12,644.10

Message box, title Payslip:
Gross: $11,707.50
Bonus: $936.60
Total: $12,644.10
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five names created and used for writing | 2 |
| The two validated entries, each with its own loop | 3 |
| The three amounts right: 11,707.50, 936.60 and 12,644.10 | 3 |
| Currency format on the three amount cells | 1 |
| The closing message with three lines split by `vbNewLine` | 1 |

**Most common mistake**

Working the total out as `gross * 1.08` and never writing the bonus separately. It gives the same total and leaves B5 empty, which is the cell the payroll office checks.

Grading note: `"$#,##0.00"` leaves the dollar sign unquoted, so Excel treats it as the currency placeholder and uses the symbol from the machine's regional setting. On the classroom machine it comes out as `$`. A workbook run in another region showing another symbol is not the student's error.

---

## Week 06 · Unit 2 · Editing what you recorded

### 06.1 · Recognise

**Solution**

Eight rows end up formatted, from D2 to D9. The other 32 are untouched and the macro raises no error at all: the range it recorded exists, it just fell short.

`Cells(Rows.Count, 1).End(xlUp).Row` returns 41, because it starts from row 1,048,576 and comes up until it hits data. `Range("A1").CurrentRegion` returns `$A$1:$D$41`.

**Output**

```text
Rows formatted:      8 of 40
Error:               none
End(xlUp).Row:       41
CurrentRegion:       $A$1:$D$41
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Answers 8 rows formatted | 3 |
| Says there is no error | 2 |
| `End(xlUp).Row` returns 41 | 3 |
| `CurrentRegion` returns `$A$1:$D$41` | 2 |

**Most common mistake**

Answering 40 for `End(xlUp).Row`, forgetting that row 1 is the headers and that the property returns a row number, not a count of data.

### 06.2 · Apply

**Solution**

```vba
Option Explicit

Sub FormatAmounts()
    Dim lastRow As Long
    Dim amounts As Range

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    Set amounts = Range(Cells(2, 4), Cells(lastRow, 4))

    amounts.NumberFormat = "$#,##0.00"
    Range("F1").Value = lastRow - 1
End Sub
```

**Output**

With the eight-row database:

```text
lastRow = 9
Range built: $D$2:$D$9
F1 = 8
```

With the forty-row database the same code builds `$D$2:$D$41` and leaves F1 at 40.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Not one `Select` or `Selection` is left | 2 |
| The last row is worked out with `End(xlUp)` into a `Long` variable | 3 |
| The range is built with `Range(Cells, Cells)` and assigned with `Set` | 3 |
| F1 ends at 8, the count without the header | 2 |

**Most common mistake**

Writing `Set amounts = Range(Cells(2, 4), Cells(lastRow, 4))` without the `Set`. It stops with error 91 and the student goes looking for the problem in `Cells`.

### 06.3 · Integrate

**Solution**

```vba
Option Explicit

Sub PrepareCatalogue()
    Dim lastRow As Long
    Dim costs As Range

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    Set costs = Range(Cells(2, 4), Cells(lastRow, 4))
    costs.NumberFormat = "$#,##0.00"

    ThisWorkbook.Names.Add Name:="TotalRows", RefersTo:="=Suppliers!$G$1"
    Range("TotalRows").Value = lastRow - 1

    If Columns("E:E").EntireColumn.Hidden Then
        Columns("E:E").EntireColumn.Hidden = False
    Else
        Columns("E:E").EntireColumn.Hidden = True
    End If

    MsgBox "Cost range: " & costs.Address
End Sub
```

**Output**

```text
lastRow = 6
G1 = 5
D2 shows $185.00
Message box: Cost range: $D$2:$D$6

First run:   column E hidden
Second run:  column E visible
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cost range is built with `Cells` and gets the format | 3 |
| The name `TotalRows` is created and ends at 5 | 2 |
| Column E toggles by reading `Hidden`, and is never deleted | 3 |
| The message shows `$D$2:$D$6` through `Address` | 2 |

**Most common mistake**

Using `Delete` instead of `Hidden` for the helper column. In the demonstration it looks identical, and by the second run it has taken away a column of data nobody is going to get back.

---

## Week 07 · Unit 2 · Goal Seek and chaining

### 07.1 · Recognise

**Solution**

The cell that cannot carry a formula is `UnitPrice`, the one in `ChangingCell`. Goal Seek writes trial values there, and it cannot write over a formula.

The search arrives at a unit price of 136.50. Worked out by hand: for the margin to be 250,000 the expression `(price - 84) * 12000` has to come to 630,000, that is a unit margin of 52.50 over a variable cost of 84.00.

Whether B6 lands exactly on 250,000 is not something to count on. Goal Seek gropes: it tries a value, measures how far off it landed and corrects. It stops when the gap fits inside `Application.MaxChange`, which defaults to 0.001, or when it uses up `Application.MaxIterations`, which defaults to 100 tries. Measured on this model, which is linear, the first correction landed on the answer and the difference came out as exactly zero.

If `ChangingCell` points at `TotalMargin`, the macro stops with error 1004, because that cell holds a formula.

**Output**

```text
Before:   UnitPrice 120.00     TotalMargin 52,000.00
After:    UnitPrice 136.50     TotalMargin 250,000.00

TotalMargin - 250000  ->  0
UnitPrice = 136.5 exactly ?  True

MaxChange      0.001
MaxIterations  100
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Points at `UnitPrice` and explains why it cannot hold a formula | 3 |
| Arrives at 136.50 | 3 |
| Says whether a residue is left and names `MaxChange` and `MaxIterations` | 2 |
| Recognises the 1004 of the last case | 2 |

**Most common mistake**

Concluding from this run that Goal Seek always lands exactly. It does here because the margin is a straight line in the price. On the module 00 amortization model, measured, the same method leaves the closing balance at -5.56E-10, and a student who writes a comparison against exact zero finds it never fires.

### 07.2 · Apply

**Solution**

```vba
Option Explicit

Sub LoadParameters()
    Range("UnitPrice").Value = 120
    Range("Units").Value = 12000
    Range("VariableCost").Value = 84
    Range("FixedCosts").Value = 380000
End Sub

Sub FormatModel()
    Range("UnitPrice").NumberFormat = "$#,##0.00"
    Range("VariableCost").NumberFormat = "$#,##0.00"
    Range("FixedCosts").NumberFormat = "$#,##0.00"
    Range("TotalMargin").NumberFormat = "$#,##0.00"
End Sub

Sub SeekPrice()
    Range("TotalMargin").GoalSeek _
        Goal:=250000, _
        ChangingCell:=Range("UnitPrice")
End Sub

Sub ClosePrice()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call LoadParameters
    Call FormatModel

    Application.Calculation = xlCalculationAutomatic

    Call SeekPrice

    Application.ScreenUpdating = True
End Sub
```

**Output**

```text
When ClosePrice finishes:
  UnitPrice        $136.50
  TotalMargin      $250,000.00
  Calculation      xlCalculationAutomatic (-4105)
  ScreenUpdating   True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The three procedures run on their own from the macro dialog | 3 |
| The master only calls and touches no cell | 2 |
| Switches screen and calculation off and back on | 2 |
| Calculation is on automatic while the search runs | 3 |

**Most common mistake**

Leaving calculation on manual during the goal seek. The macro raises no error, but the margin formula is not re-evaluated between one try and the next, so the search finishes with the starting price or with any old one.

### 07.3 · Integrate

**Solution**

```vba
Option Explicit

Function ComputedTotalMargin(price As Double, units As Double, _
                             varCost As Double, fixed As Double) As Double
    ComputedTotalMargin = (price - varCost) * units - fixed
End Function

Sub CompareMargin()
    Dim computed As Double

    computed = ComputedTotalMargin(Range("UnitPrice").Value, _
                                   Range("Units").Value, _
                                   Range("VariableCost").Value, _
                                   Range("FixedCosts").Value)

    Range("B8").Value = computed

    If computed = Range("TotalMargin").Value Then
        Range("B9").Value = "Matches"
    Else
        Range("B9").Value = "Check"
    End If
End Sub
```

**Output**

```text
With the starting price at 120:
  B6 = 52000     B8 = 52000     B9 = Matches

After ClosePrice:
  UnitPrice   136.5
  B6          250000
  B8          250000
  B9          Matches
  B6 - 250000 0
```

The residue depends on the run. This model is linear, so the search converges in a single correction and on the machine these solutions were measured on the difference came out as exactly zero. What is marked is that the student reports the number their own run produced, not that it matches a fixed one. A student who reports a residue in the order of a billionth on a model of theirs is equally right.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function declares the type it returns and assigns its own name | 3 |
| With 120, 12000, 84 and 380000 it returns 52,000 | 2 |
| `CompareMargin` writes B8 and decides between Matches and Check | 2 |
| Reports the price found and the value left in B6 | 2 |
| Reports the difference it measured rather than the one it expected | 1 |

**Most common mistake**

Writing the function without ever assigning its own name. It raises no error, returns zero, and B9 says Check while the model is fine. The student goes looking for the problem in the sheet.

---

## Week 08 · Unit 3 · Decisions and the first midterm

### 08.1 · Recognise

**Solution**

| Comparison | Returns | Why |
|---|---|---|
| `"Norte" = "norte"` | False | VBA compares text respecting case |
| `"10" < "9"` | True | As text, the 1 sorts before the 9 |
| `10 < 9` | False | As numbers, nine is the smaller |
| `CInt(True)` | -1 | True is worth minus one, not one |
| `Range("A1").Value = 0` | True | An empty cell equals zero |
| `Range("A1").Value = ""` | True | And it equals the empty string as well |
| `Range("A1").Value > 0` | False | Empty is not greater than zero |

Grouping by the text exactly as it was typed, Excel reports three separate regions for the north: Norte, norte and NORTE.

To tell a sale with no amount from a sale of zero pesos, the comparison that is no use is `= 0`, because the empty cell returns True as well. None of the three tells the case apart: what is needed is `IsEmpty`, which arrives next week.

**Output**

```text
"Norte" = "norte"      False
"10" < "9"             True
10 < 9                 False
CInt(True)             -1
A1 empty = 0           True
A1 empty = ""          True
A1 empty > 0           False
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The seven comparisons, one point each | 7 |
| Answers three regions for the north | 1 |
| Points out that `= 0` does not tell the empty cell apart | 2 |

**Most common mistake**

Answering 1 for `CInt(True)`. It leads to writing sums of flags that come out negative, and the student checks the addition instead of the conversion.

### 08.2 · Apply

**Solution**

```vba
Option Explicit

Sub ClassifyWithIf()
    Dim amount As Double
    Dim tier As String

    amount = Range("D2").Value

    If amount >= 150000 Then
        tier = "A"
    ElseIf amount >= 100000 Then
        tier = "B"
    ElseIf amount >= 50000 Then
        tier = "C"
    Else
        tier = "D"
    End If

    Range("E2").Value = tier
End Sub

Sub ClassifyWithCase()
    Dim amount As Double
    Dim tier As String

    amount = Range("D2").Value

    ' With Is, every case is a floor and everything above it was caught already.
    ' With To you would have to write the ceiling of each band, and an amount
    ' between two ceilings, say 149,999.50, would fall to the Else with no tier.
    Select Case amount
        Case Is >= 150000
            tier = "A"
        Case Is >= 100000
            tier = "B"
        Case Is >= 50000
            tier = "C"
        Case Else
            tier = "D"
    End Select

    Range("E2").Value = tier
End Sub
```

**Output**

```text
D2 = 210500   ->  E2 = A
D2 = 128400   ->  E2 = B
D2 =  65900   ->  E2 = C
D2 =  41200   ->  E2 = D
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `If` chain runs from the strictest condition to the loosest | 3 |
| The `Select Case` gives the same for the four amounts | 3 |
| No amount is left without a tier | 2 |
| The comment explains why `Is` and not `To` | 2 |

**Most common mistake**

Writing the chain the other way round, starting at `>= 50000`. It runs without error and tiers everything as C, because the first true condition is the one that wins.

### 08.3 · Integrate

**Solution**

```vba
Option Explicit

Sub ReviewAccount()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call CaptureAmount
    Call MeasureData
    Call ClassifyAmount

    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
End Sub

Sub CaptureAmount()
    Dim text As String
    Dim valid As Boolean

    ThisWorkbook.Names.Add Name:="ReviewedAmount", RefersTo:="=Sales!$G$2"

    valid = False
    Do While Not valid
        text = InputBox("Amount to review", "Sales")
        If IsNumeric(text) Then
            If CDbl(text) > 0 Then
                Range("ReviewedAmount").Value = CDbl(text)
                valid = True
            End If
        End If
        If Not valid Then
            MsgBox "That is not a valid amount.", vbExclamation
        End If
    Loop
End Sub

Sub MeasureData()
    Dim lastRow As Long
    Dim amounts As Range

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    Set amounts = Range(Cells(2, 4), Cells(lastRow, 4))
    amounts.NumberFormat = "$#,##0.00"

    ThisWorkbook.Names.Add Name:="TotalRows", RefersTo:="=Sales!$G$1"
    Range("TotalRows").Value = lastRow - 1
End Sub

Sub ClassifyAmount()
    Dim amount As Double
    Dim tier As String

    ThisWorkbook.Names.Add Name:="ReviewedTier", RefersTo:="=Sales!$G$3"

    amount = Range("ReviewedAmount").Value

    Select Case amount
        Case Is >= 150000
            tier = "A"
        Case Is >= 100000
            tier = "B"
        Case Is >= 50000
            tier = "C"
        Case Else
            tier = "D"
    End Select

    Range("ReviewedTier").Value = tier
    Range("ReviewedAmount").NumberFormat = "$#,##0.00"
End Sub
```

Which week each piece comes from:

| Procedure | Week | What is marked from there |
|---|---|---|
| `CaptureAmount` | 5 | `InputBox`, `IsNumeric` and the loop that insists |
| `MeasureData` | 6 | Variable range with `End(xlUp)` and `Cells` |
| `ClassifyAmount` | 8 | `Select Case` over the tier table |
| `ReviewAccount` | 7 | Bounded automation and chaining with `Call` |

**Output**

Entering 128400 over the eight-row database:

```text
G1 = 8
G2 = 128400      shows $128,400.00
G3 = B
Column D with currency format from D2 to D9
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The master bounds and restores screen and calculation | 2 |
| The entry validates and lets neither text nor zero through | 2 |
| The range is worked out rather than typed, and G1 ends at 8 | 2 |
| The tiering uses `Select Case` and G3 ends at B | 2 |
| The three range names created and used | 1 |
| The table assigns each procedure to its week | 1 |

**Most common mistake**

Writing `Range("G3").Value = tier` inside `ClassifyAmount` instead of using the name. It works, and it is exactly the constraint the brief was testing.

---

## Week 09 · Unit 3 · Repetition

### 09.1 · Recognise

**Solution**

In (a) the message reads `Periods: 10 7 4 1 `, with a trailing space. `Step -3` comes down in threes and stops at 1, because the next value would be -2 and that is past the limit.

In (b) the walk hands over `$A$1 $B$1 $A$2 $B$2 `. `For Each` over a range goes across and then down: it finishes each row before moving down.

In (c) three of the six campaigns are left. Deleting row 2 pulls row 3 up into position 2 while the counter is already at 3, so it skips every other one. With `For r = 7 To 2 Step -1` none are left: deleting backwards moves rows the loop has already passed.

**Output**

```text
(a)  Periods: 10 7 4 1
(b)  $A$1 $B$1 $A$2 $B$2
(c)  forwards:   3 of 6 left
     backwards:  0 of 6 left
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The text of (a), including the descending order | 3 |
| The order of (b), across and then down | 3 |
| (c) answers 3 of 6 and explains the shift | 2 |
| (c) answers 0 of 6 when walking backwards | 2 |

**Most common mistake**

Answering the column order in (b), `$A$1 $A$2 $B$1 $B$2`. It gives itself away when the student uses `For Each` to read a database and builds the rows crossed over each other.

### 09.2 · Apply

**Solution**

```vba
Option Explicit

Sub FlagOverdue()
    Dim lastRow As Long
    Dim r As Long
    Dim flagged As Long
    Dim overdueAmount As Double

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        If Cells(r, 4).Value > 30 Then
            Cells(r, 5).Value = "Overdue"
            flagged = flagged + 1
            overdueAmount = overdueAmount + Cells(r, 3).Value
        End If
    Next r

    Range("G1").Value = flagged
    Range("G2").Value = overdueAmount
    Range("G2").NumberFormat = "$#,##0.00"
End Sub
```

**Output**

```text
E3 = Overdue      (F-2202, 45 days)
E5 = Overdue      (F-2204, 61 days)
E7 = Overdue      (F-2206, 38 days)

G1 = 3
G2 = 69730        shows $69,730.00
```

Invoice F-2205, at exactly 30 days, is not flagged.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The last row is worked out and the loop starts at 2 | 3 |
| The three invoices flagged are the right ones | 3 |
| G1 ends at 3 | 2 |
| G2 ends at 69,730.00 with currency format | 2 |

**Most common mistake**

Using `>= 30` and flagging four invoices. The brief said exactly 30 is not flagged, and F-2205 puts 21,930.00 of overdue book into a total that is not overdue.

### 09.3 · Integrate

**Solution**

```vba
Option Explicit

Sub CleanCampaigns()
    Application.ScreenUpdating = False

    Call ClassifyCampaigns
    Call DropNoData

    Application.ScreenUpdating = True
End Sub

Sub ClassifyCampaigns()
    Dim lastRow As Long
    Dim r As Long
    Dim mass As Long
    Dim targeted As Long
    Dim noData As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        If IsEmpty(Cells(r, 3).Value) Then
            Cells(r, 5).Value = "No data"
            noData = noData + 1
        ElseIf Cells(r, 3).Value >= 3000 Then
            Cells(r, 5).Value = "Mass"
            mass = mass + 1
        Else
            Cells(r, 5).Value = "Targeted"
            targeted = targeted + 1
        End If
    Next r

    Range("G1").Value = mass
    Range("G2").Value = targeted
    Range("G3").Value = noData
End Sub

Sub DropNoData()
    Dim lastRow As Long
    Dim r As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = lastRow To 2 Step -1
        If Cells(r, 5).Value = "No data" Then
            Rows(r).Delete
        End If
    Next r
End Sub
```

**Output**

```text
After ClassifyCampaigns:
  E2 Targeted   E3 Mass      E4 No data
  E5 Mass       E6 No data   E7 Mass

  G1 = 3    mass
  G2 = 1    targeted
  G3 = 2    no data

After DropNoData:
  4 rows of data left: C-01, C-02, C-04 and C-06
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `IsEmpty` tells the empty cell apart, and it comes before the comparison | 3 |
| The six classifications right | 2 |
| The three counters at 3, 1 and 2 | 2 |
| The delete walks from the bottom up | 2 |
| Four rows of data are left | 1 |

**Most common mistake**

Asking `If Cells(r, 3).Value = 0` instead of `IsEmpty`. The two campaigns with no data get classified as targeted, the counters come out 3, 3 and 0, and nothing gets deleted.

---

## Week 10 · Units 1 and 3 · Procedures and functions

### 10.1 · Recognise

**Solution**

B2 ends at 12644.1. The parameter of `ApplyBonus` was declared `amount As Double`, without writing `ByVal`, and in VBA whatever is not declared goes by reference: the procedure multiplied the caller's own variable by 1.08.

B3 ends at 0. `PayslipTotal` never assigns anything to its own name, so it returns the default value of a `Double`. It raises no error, and the calculation carries on with that zero.

The word that fixes the first one is `ByVal`, in `Sub ApplyBonus(ByVal amount As Double)`. The line missing for the second one is `PayslipTotal = gross + bonus`.

**Output**

```text
B2 = 12644.1
B3 = 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| B2 at 12,644.10 and names the pass by reference | 3 |
| B3 at zero and explains that the function never assigns its name | 3 |
| Proposes `ByVal` as the missing word | 2 |
| Writes the missing assignment line | 2 |

**Most common mistake**

Answering that B3 raises an error. That is what you would expect, and it is exactly what does not happen: the silence is what makes the case expensive.

### 10.2 · Apply

**Solution**

```vba
Option Explicit

Function SaleCommission(ByVal amount As Double) As Double
    If amount >= 150000 Then
        SaleCommission = amount * 0.06
    ElseIf amount >= 100000 Then
        SaleCommission = amount * 0.04
    ElseIf amount >= 50000 Then
        SaleCommission = amount * 0.025
    Else
        SaleCommission = 0
    End If
End Function
```

On the sheet, E2 carries `=SaleCommission(D2)` and is copied down to E9. E10 carries `=SUM(E2:E9)`.

**Output**

```text
V-1001   128,400.00   4.0 %    5,136.00
V-1002    96,750.00   2.5 %    2,418.75
V-1003   143,200.00   4.0 %    5,728.00
V-1004    87,300.00   2.5 %    2,182.50
V-1005   210,500.00   6.0 %   12,630.00
V-1006    65,900.00   2.5 %    1,647.50
V-1007    54,120.00   2.5 %    1,353.00
V-1008   181,045.00   6.0 %   10,862.70

Commission total               41,958.45
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function declares `As Double` on the way out and assigns its name in all four branches | 3 |
| The parameter goes `ByVal` | 1 |
| The eight commissions right | 4 |
| The total at 41,958.45 | 1 |
| The function is used from the cell, not from a macro | 1 |

**Most common mistake**

Writing the function as a `Sub`. No error turns up until it is typed into the cell, and there Excel returns `#NAME?`, which the student reads as having misspelled the name.

### 10.3 · Integrate

**Solution**

```vba
Option Explicit

Function TotalPay(ByVal days As Double, ByVal wage As Double, _
                  ByVal bonusPct As Double) As Double
    Dim gross As Double

    gross = days * wage
    TotalPay = gross + gross * bonusPct
End Function

Sub ComputePay()
    Dim lastRow As Long
    Dim r As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        Cells(r, 6).Value = TotalPay(Cells(r, 3).Value, _
                                     Cells(r, 4).Value, _
                                     Cells(r, 5).Value)
        Cells(r, 6).NumberFormat = "$#,##0.00"
    Next r
End Sub

Sub FlagIncomplete()
    Dim lastRow As Long
    Dim r As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        If Cells(r, 3).Value < 15 Then
            Cells(r, 7).Value = "Check"
        End If
    Next r
End Sub

Sub TotalPayroll()
    Dim lastRow As Long
    Dim r As Long
    Dim total As Double

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        total = total + Cells(r, 6).Value
    Next r

    Cells(lastRow + 1, 6).Value = total
    Cells(lastRow + 1, 6).NumberFormat = "$#,##0.00"
End Sub

Sub ProcessPayroll()
    Application.ScreenUpdating = False

    Call ComputePay
    Call FlagIncomplete
    Call TotalPayroll

    Application.ScreenUpdating = True
End Sub
```

**Output**

```text
F2 = 12644.1     $12,644.10    Ana Robles
F3 =  9639       $9,639.00     Beto Lira
F4 = 13513.5     $13,513.50    Carla Méndez
F5 =  7926       $7,926.00     Darío Sáenz
F6 = 43722.6     $43,722.60    total

G4 = Check       (Carla Méndez, 13 days)
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The function takes the three parameters `ByVal` and returns `Double` | 2 |
| `ComputePay` computes nothing itself, it only calls the function | 2 |
| The four payments right | 2 |
| The total at 43,722.60, on the row after the last data row | 2 |
| Only Carla Méndez is flagged with Check | 1 |
| Each procedure runs on its own from the macro dialog | 1 |

**Most common mistake**

Putting the bonus calculation inside `ComputePay` and leaving the function unused. The submission runs and gives the same numbers, and there is nothing that can be tested on its own, which was the point of the session.

---

## Week 11 · Units 2 and 3 · Events

### 11.1 · Recognise

**Solution**

In (a) nothing happens. The code compiles, the name is right, and Excel looks for sheet handlers only in that sheet's own module. In a standard module it is left as a procedure nobody calls. There is no message, no error and no warning that it was orphaned. It is `Private` as well, so it does not turn up in the macro dialog either.

In (b), writing 15 into B2 fires the handler, which writes into C2. Writing into C2 is also a change, so Excel calls the handler again, which writes into D2, and so on. Nothing stops it: Excel stops responding and the process dies on its own.

In (c), with the guard on B2 and `IsNumeric` deciding what to write:

| What gets typed into B2 | `IsNumeric` on that text | `IsNumeric(Target.Value)` | What gets written into C2 |
|---|---|---|---|
| 15 | True | True | Number |
| 12.5 | True | True | Number |
| $780.50 | True in the United States region | True | Number |
| 15% | False | True | Number |
| fifteen | False | False | Not a number |

The rows where the columns differ are `15%` and, depending on the region, `$780.50`. The reason is the same for both: by the time the handler fires, Excel has already interpreted what was typed and stored it as a number. `15%` sits in the cell as 0.15 with a percentage format, and `$780.50` as 780.5 with a currency format. `Target.Value` hands over those numbers, not the text, so `IsNumeric` says True even though the original string was not numeric. Only `fifteen` stays as text and is the one that reaches `Not a number`.

**Output**

```text
(a)  nothing happens, and Excel gives no warning
(b)  Excel stops responding and the process dies
(c)  four times Number and one single Not a number

measured, what the cell holds after each entry:
  15        ->  15      format General
  12.5      ->  12.5    format General
  $780.50   ->  780.5   format $#,##0.00_);[Red]($#,##0.00)
  15%       ->  0.15    format 0%
  fifteen   ->  fifteen format General
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) says nothing happens and explains where Excel looks for the handler | 3 |
| (b) describes the chain of writes that refire | 2 |
| The `IsNumeric(Target.Value)` column and the C2 column | 3 |
| Points out `15%` as the row where the two columns differ | 2 |

**Most common mistake**

Answering `Not a number` for `15%`, copying the week 11 slide table without noticing that there `IsNumeric` is measured over a string and here over `Target.Value`. It gives itself away when the student hands in the text column filled in twice.

Grading note: the week 11 slide lists `$5`, `5%` and `2026-01-01` as `False`, and that is true of `IsNumeric` applied to those strings, not of the cell once it has been entered. Measured on Excel 16.0 in the United States region, typing those three values into a cell leaves `Target.Value` at 5, 0.15 and 46023, all three numeric. The `$780.50` row also depends on the region in the text column: `IsNumeric` accepts the currency symbol of the active region, so it returns `True` here and `False` on a machine set to the United Kingdom, where the symbol is the pound. The slide answer is accepted if the student explains which of the two questions they are answering.

### 11.2 · Apply

**Solution**

In the module of the `Payroll` sheet:

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    ' The guard is enough because the handler writes into H2 and never into C2.
    ' If it also wrote into C2, that write would come back through the guard
    ' and call the handler again: there is where EnableEvents would be needed.
    If Target.Address <> "$C$2" Then Exit Sub

    If IsNumeric(Target.Value) Then
        Range("H2").Value = "Valid days"
        Target.NumberFormat = "0"
    Else
        Range("H2").Value = "Check entry"
        Target.Interior.Color = RGB(255, 235, 156)
    End If
End Sub
```

**Output**

```text
15 typed into C2        ->  H2 = Valid days,   C2 with format 0
fifteen typed into C2   ->  H2 = Check entry,  C2 in yellow
something typed in D2   ->  nothing happens
Twenty entries in a row ->  Excel keeps responding
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The handler is in the sheet module, not a standard one | 2 |
| The guard lets only the C2 change through | 3 |
| The two H2 texts according to `IsNumeric` | 2 |
| The format and the yellow fill applied to C2 | 2 |
| The comment explains the limit of the guard | 1 |

**Most common mistake**

Putting the handler in a standard module. It compiles, it shows up in the tree, and it never fires. It gives itself away when the student reports that their code does nothing and has no error to show.

### 11.3 · Integrate

**Solution**

In `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    ThisWorkbook.Worksheets("Payroll").Activate
    ThisWorkbook.Worksheets("Payroll").Range("C2").Select
    MsgBox "Enter the days worked in C2"
End Sub
```

In the module of the `Payroll` sheet:

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    If Target.Address <> "$C$2" Then Exit Sub

    Application.EnableEvents = False

    If IsNumeric(Target.Value) Then
        If CDbl(Target.Value) > 0 Then
            Range("F2").Value = TotalPay(CDbl(Target.Value), _
                                         Range("D2").Value, _
                                         Range("E2").Value)
            Range("F2").NumberFormat = "$#,##0.00"
            Range("G2").ClearContents
        Else
            Range("F2").ClearContents
            Range("G2").Value = "Check entry"
        End If
    Else
        Range("F2").ClearContents
        Range("G2").Value = "Check entry"
    End If

    Application.EnableEvents = True
End Sub
```

**Output**

```text
On opening the workbook:
  Payroll sheet active, C2 selected
  box: Enter the days worked in C2

15 entered into C2:
  F2 = 12644.1    shows $12,644.10
  G2 empty

fifteen entered into C2:
  F2 empty
  G2 = Check entry
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| `Workbook_Open` lives in `ThisWorkbook` and leaves C2 selected | 2 |
| The sheet handler reacts only to C2 | 2 |
| Reuses the `TotalPay` function from week 10 instead of recalculating | 2 |
| F2 ends at 12,644.10 when 15 is entered | 2 |
| Switches events off and back on around the writes | 2 |

**Most common mistake**

Switching events off and never switching them back on because the procedure exits through the error branch. Excel is left with no events until it is closed, and the student reports that the handler stopped working for no reason.

---

## Week 12 · Unit 3 · Custom classes

### 12.1 · Recognise

**Solution**

In (a) it prints 13875. There was only one `New`, so only one object exists: `Set b = a` copies nothing, it leaves two names pointing at the same place. The last stock assignment is `b`'s, which put 75, and the cost stayed at 185. For them to be independent a second `New` is needed, that is `Set b = New Supplier`.

In (b) it stops with error 91, `Object variable or With block variable not set`. `Dim` reserves the name and creates nothing; without `Set s = New Supplier`, the first line that uses the object blows up.

In (c) it prints 0. The validation lives in `Property Let UnitCost`, so the -185 never gets in: the field stays at zero and so does the inventory value.

**Output**

```text
(a)  13875        objects created: 1
(b)  Error 91     Object variable or With block variable not set
(c)  0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) answers 13875 and explains that there is only one object | 4 |
| (a) proposes the second `New` to separate them | 1 |
| (b) names error 91 and the difference between `Dim` and `Set` | 3 |
| (c) answers zero and places the validation in `Let` | 2 |

**Most common mistake**

Answering 77700 in (a), reading the assignments as though `a` and `b` were separate boxes. It is the same reasoning that works for numbers and stops working for objects.

### 12.2 · Apply

**Solution**

Class module, named `Supplier` from the Properties window:

```vba
Option Explicit

Private pCode As String
Private pStock As Long
Private pUnitCost As Double

Private Sub Class_Initialize()
    pCode = "no code"
    pStock = 0
    pUnitCost = 0
End Sub

Public Property Get Code() As String
    Code = pCode
End Property

Public Property Let Code(value As String)
    pCode = value
End Property

Public Property Get Stock() As Long
    Stock = pStock
End Property

Public Property Let Stock(value As Long)
    If value < 0 Then
        pStock = 0
    Else
        pStock = value
    End If
End Property

Public Property Get UnitCost() As Double
    UnitCost = pUnitCost
End Property

Public Property Let UnitCost(value As Double)
    If value < 0 Then
        pUnitCost = 0
    Else
        pUnitCost = value
    End If
End Property

Public Function Value() As Double
    Value = pStock * pUnitCost
End Function
```

Standard module:

```vba
Option Explicit

Sub TestSupplier()
    Dim s As Supplier
    Set s = New Supplier

    Debug.Print s.Code & " | " & s.Stock & " | " & _
                s.UnitCost & " | " & s.Value

    s.Code = "P-100"
    s.Stock = 420
    s.UnitCost = 185
    Debug.Print s.Code & " | " & s.Stock & " | " & _
                s.UnitCost & " | " & s.Value

    s.UnitCost = -50
    Debug.Print s.Code & " | " & s.Stock & " | " & _
                s.UnitCost & " | " & s.Value
End Sub
```

**Output**

Immediate window:

```text
no code | 0 | 0 | 0
P-100 | 420 | 185 | 77700
P-100 | 420 | 0 | 0
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The class module is named `Supplier`, not Class1 | 1 |
| Three private fields and their three pairs of `Get` and `Let` | 3 |
| The negative validation lives inside `Let` | 2 |
| `Value` returns stock times unit cost | 2 |
| `Class_Initialize` leaves the object usable without anything assigned | 2 |

**Most common mistake**

Naming the private field the same as the property. The property calls itself, goes into recursion and the program runs out of stack. It gives itself away because the error turns up on the first read and not on the write.

### 12.3 · Integrate

**Solution**

```vba
Option Explicit

Sub ValueCatalogue()
    Dim lastRow As Long
    Dim r As Long
    Dim total As Double
    Dim item As Supplier

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    ThisWorkbook.Names.Add Name:="TotalValue", RefersTo:="=Suppliers!$G$1"

    For r = 2 To lastRow
        Set item = New Supplier

        item.Code = Cells(r, 1).Value

        If IsEmpty(Cells(r, 3).Value) Then
            Cells(r, 6).Value = "Check"
        Else
            item.Stock = Cells(r, 3).Value
        End If

        item.UnitCost = Cells(r, 4).Value

        Cells(r, 5).Value = item.Value
        Cells(r, 5).NumberFormat = "$#,##0.00"
        total = total + item.Value
    Next r

    Range("TotalValue").Value = total
    Range("TotalValue").NumberFormat = "$#,##0.00"
End Sub
```

**Output**

```text
E2 =  77700     $77,700.00     P-100
E3 =  11610     $11,610.00     P-101
E4 =  18000     $18,000.00     P-102
E5 =  16000     $16,000.00     P-103
E6 =  21930     $21,930.00     P-104

G1 = 145240     $145,240.00
```

With C4 emptied, that row comes out at zero, F4 says Check and the total drops to 127,240.00.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The `New` goes inside the loop, one per row | 3 |
| Each row's value comes out of the object, not out of a sum in the macro | 3 |
| The total at 145,240.00, in the named cell | 2 |
| A row with empty stock comes out at zero and flagged | 2 |

**Most common mistake**

Putting `Set item = New Supplier` before the loop. It runs and gives the right total, because the object is reused and all three values are overwritten every turn, but there stops being one object per row and the first property that is not reassigned drags the previous row's value along.

---

## Week 13 · Unit 4 · Cleaning and sorting

### 13.1 · Recognise

**Solution**

In (a) the VBA `Trim` strips the spaces at the edges and leaves the ones in the middle alone. The sheet one, called through `WorksheetFunction`, also collapses the middle ones to a single space.

In (b), `Len(s)` and `Len(Trim(s))` are both 5, and the comparison returns `False`. `Chr(160)` is a hard space and `Trim` does not recognise it as a space, so it survives and makes two cells that look identical compare as different.

In (c), the one that is not what the user wanted is `Aceros Del Bajío`: `Proper` capitalises every word, articles and prepositions included.

In (d) all four rows are left, the header and the three data rows. `Columns:=2` counts inside the range, so it points at column C, the codes, and all three are different. To strip the repeated suppliers you have to pass `Columns:=1`.

**Output**

```text
(a)  [Aceros del Bajío]
     [Aceros    del Bajío]
     [Aceros del Bajío]

(b)  5    5
     False

(c)  Empaques Lira
     Aceros Del Bajío
     Papelera Central

(d)  4 rows, nothing removed
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) tells the VBA `Trim` from the sheet one | 3 |
| (b) answers 5 and 5, and False, and names the hard space | 3 |
| (c) points at `Aceros Del Bajío` | 2 |
| (d) answers four rows and proposes `Columns:=1` | 2 |

**Most common mistake**

Answering 5 and 4 in (b), assuming `Trim` strips the hard space because on screen it looks like an ordinary one. That is exactly the assumption that leaves the database dirty.

### 13.2 · Apply

**Solution**

```vba
Option Explicit

Sub CleanSuppliers()
    Dim lastRow As Long
    Dim cell As Range

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For Each cell In Range(Cells(2, 1), Cells(lastRow, 1))
        ' The order matters: if Trim goes first, the hard space is still
        ' there and neither it nor Proper touches it. First translate it
        ' into an ordinary space, then collapse, then even out the case.
        cell.Value = Replace(cell.Value, Chr(160), " ")
        cell.Value = WorksheetFunction.Trim(cell.Value)
        cell.Value = WorksheetFunction.Proper(cell.Value)
    Next cell
End Sub
```

**Output**

```text
A2 = Aceros Del Bajío
A3 = Empaques Lira
A4 = Papelera Central
A5 = Comercial Sáenz
```

`Proper` leaves `Del` capitalised. That is the correct result of the function and not the one the business wants: if the catalogue requires it in lower case, it has to be fixed afterwards with `Replace`.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The last row is worked out and the range is built with `Cells` | 2 |
| The hard space is replaced before trimming | 3 |
| Uses the sheet `Trim`, not the VBA one | 2 |
| `Proper` evens out the case of all four | 2 |
| The comment explains the order | 1 |

**Most common mistake**

Using the VBA `Trim`. Row 3 keeps its four middle spaces, the database looks clean, and the PivotTable goes on reporting two suppliers where there is one.

### 13.3 · Integrate

**Solution**

```vba
Option Explicit

Sub PrepareSales()
    Dim lastRow As Long
    Dim r As Long
    Dim total As Double

    Application.ScreenUpdating = False

    Call EvenOutRegion
    Call DeleteBlanks
    Call RemoveRepeats
    Call SortSales

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row
    For r = 2 To lastRow
        total = total + Cells(r, 4).Value
    Next r

    Range("F1").Value = lastRow - 1
    Range("F2").Value = total
    Range("F2").NumberFormat = "$#,##0.00"

    Application.ScreenUpdating = True
End Sub

Sub EvenOutRegion()
    Dim lastRow As Long
    Dim cell As Range

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For Each cell In Range(Cells(2, 2), Cells(lastRow, 2))
        If Not IsEmpty(cell.Value) Then
            cell.Value = WorksheetFunction.Proper( _
                WorksheetFunction.Trim(cell.Value))
        End If
    Next cell
End Sub

Sub DeleteBlanks()
    Dim lastRow As Long
    Dim r As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = lastRow To 2 Step -1
        If WorksheetFunction.CountA(Rows(r)) = 0 Then
            Rows(r).Delete
        End If
    Next r
End Sub

Sub RemoveRepeats()
    Dim lastRow As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(lastRow, 4)).RemoveDuplicates _
        Columns:=1, Header:=xlYes
End Sub

Sub SortSales()
    Dim lastRow As Long

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(lastRow, 4)).Sort _
        Key1:=Range("B1"), Order1:=xlAscending, _
        Key2:=Range("D1"), Order2:=xlDescending, _
        Header:=xlYes
End Sub
```

**Output**

```text
Database when it finishes:

  A         B        C               D
2 V-1004    Centro   Darío Sáenz      87,300.00
3 V-1003    Norte    Carla Méndez    143,200.00
4 V-1001    Norte    Ana Robles      128,400.00
5 V-1005    Sur      Ana Robles      210,500.00
6 V-1002    Sur      Beto Lira        96,750.00

F1 = 5
F2 = 666150      shows $666,150.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The regions come out even: sur and NORTE become Sur and Norte | 2 |
| The blank row is deleted walking from the bottom up | 2 |
| The repeated ref is stripped and the first one survives | 2 |
| The sort runs on two criteria over the whole database, header declared | 2 |
| F1 at 5 and F2 at 666,150.00 | 1 |
| Every row keeps its salesperson and its amount after sorting | 1 |

**Most common mistake**

Sorting with only the amount column passed as the range. The amounts come out ordered, the names do not move, no error turns up and every row says something false.

---

## Week 14 · Unit 4 · Filters, subtotals and tables

### 14.1 · Recognise

**Solution**

| How it is added up | Returns |
|---|---|
| `For Each` over `D2:D9` | 967,215.00 |
| `For Each` over that same range with `SpecialCells(xlCellTypeVisible)` | 325,720.00 |
| `SUBTOTAL(9,D2:D9)` | 325,720.00 |
| `SUM(D2:D9)` | 967,215.00 |

The two returning 967,215 are the plain loop and `SUM`. Filtering is a decision about the view: the hidden rows are still in place with their contents intact, and neither the loop nor `SUM` asks whether they are visible.

With the criterion headed `Department` and the database headed `Region`, the advanced filter does not find the column, matches nothing and hides all eight. Zero rows are left visible and no error message appears.

**Output**

```text
For Each loop ........  967,215.00
visible only .........  325,720.00
SUBTOTAL(9) ..........  325,720.00
SUM ..................  967,215.00

rows visible on screen:  3

advanced filter, header Department:  0 of 8 visible, Err 0
advanced filter, header Region:      3 of 8 visible
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four totals, two points each | 8 |
| Answers zero visible rows and no error at all for the advanced filter | 2 |

**Most common mistake**

Assuming `SUM` respects the filter because on screen the range looks filtered. The one that respects it is `SUBTOTAL`, and that is why Excel uses it when the user presses AutoSum over a filtered list.

### 14.2 · Apply

**Solution**

```vba
Option Explicit

Sub VisibleRegionTotal()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim cell As Range
    Dim total As Double
    Dim visible As Long

    Set ws = ThisWorkbook.Worksheets("Sales")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, 4)).AutoFilter _
        Field:=2, Criteria1:=ws.Range("H1").Value

    For Each cell In ws.Range(ws.Cells(2, 4), ws.Cells(lastRow, 4)) _
            .SpecialCells(xlCellTypeVisible)
        total = total + cell.Value
        visible = visible + 1
    Next cell

    ws.Range("H2").Value = visible
    ws.Range("H3").Value = total
    ws.Range("H3").NumberFormat = "$#,##0.00"
    ws.Range("H4").Formula = "=SUBTOTAL(9,D2:D" & lastRow & ")"
End Sub
```

**Output**

```text
H1 = Norte    ->  H2 = 3   H3 = $325,720.00   H4 = 325720
H1 = Sur      ->  H2 = 2   H3 = $307,250.00   H4 = 307250
H1 = Bajío    ->  H2 = 1   H3 = $181,045.00   H4 = 181045
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The criterion is read from H1 and is not written into the code | 2 |
| The filter is applied over the region column with a variable range | 2 |
| The total comes out of `SpecialCells(xlCellTypeVisible)` | 3 |
| The three pairs of numbers agree with `SUBTOTAL` | 3 |

**Most common mistake**

Walking `D2:D9` without asking for the visible cells and reporting 967,215 for all three regions. The number looks reasonable, and it gives itself away by not changing when the criterion changes.

Grading note: if the filter leaves no rows visible, `SpecialCells` stops with error 1004 instead of returning an empty range. Handling it comes in week 16; this week it is enough for the student to point it out.

### 14.3 · Integrate

**Solution**

```vba
Option Explicit

Sub BuildSummary()
    Application.ScreenUpdating = False

    Call ConvertToTable
    If TableHasRows Then Call SummariseByRegion

    Application.ScreenUpdating = True
End Sub

Sub ConvertToTable()
    Dim ws As Worksheet
    Dim tbl As ListObject

    Set ws = ThisWorkbook.Worksheets("Sales")
    If ws.ListObjects.Count > 0 Then Exit Sub

    Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1").CurrentRegion, , xlYes)
    tbl.Name = "Sales2026"
End Sub

Function TableHasRows() As Boolean
    Dim tbl As ListObject

    Set tbl = ThisWorkbook.Worksheets("Sales").ListObjects("Sales2026")

    If tbl.DataBodyRange Is Nothing Then
        MsgBox "The table has no rows"
        TableHasRows = False
    Else
        TableHasRows = True
    End If
End Function

Sub SummariseByRegion()
    Dim tbl As ListObject
    Dim wr As Worksheet
    Dim bodyRow As Range
    Dim r As Long
    Dim count As Long
    Dim sum As Double

    Set tbl = ThisWorkbook.Worksheets("Sales").ListObjects("Sales2026")
    Set wr = ThisWorkbook.Worksheets("Summary")

    wr.Range("A1").Value = "Region"
    wr.Range("B1").Value = "Sales"
    wr.Range("C1").Value = "Amount"
    wr.Range("A2").Value = "Bajío"
    wr.Range("A3").Value = "Centro"
    wr.Range("A4").Value = "Norte"
    wr.Range("A5").Value = "Sur"

    For r = 2 To 5
        count = 0
        sum = 0

        For Each bodyRow In tbl.DataBodyRange.Rows
            If bodyRow.Cells(1, 2).Value = wr.Cells(r, 1).Value Then
                count = count + 1
                sum = sum + bodyRow.Cells(1, 4).Value
            End If
        Next bodyRow

        wr.Cells(r, 2).Value = count
        wr.Cells(r, 3).Value = sum
        wr.Cells(r, 3).NumberFormat = "$#,##0.00"
    Next r
End Sub
```

**Output**

```text
Summary sheet:

  Region    Sales    Amount
  Bajío       1      $181,045.00
  Centro      2      $153,200.00
  Norte       3      $325,720.00
  Sur         2      $307,250.00

DataBodyRange rows = 8
```

Adding two sales at the end of the table, the table grows on its own, `DataBodyRange` hands back ten rows instead of eight and the summary picks them up without a single address in the code having been touched:

```text
after two new rows, DataBodyRange rows = 10

  Bajío       1      $181,045.00
  Centro      2      $153,200.00
  Norte       4      $355,720.00
  Sur         3      $327,250.00
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The table is created with the name asked for and running twice does not blow up | 2 |
| `TableHasRows` checks `DataBodyRange Is Nothing` and returns `Boolean` | 3 |
| The summary walks the table body, not a written address | 2 |
| The four summary rows right | 2 |
| Adding rows brings them into the summary without touching the code | 1 |

**Most common mistake**

Checking the empty table with `If tbl.DataBodyRange.Rows.Count = 0`. The check itself stops with error 91, because to ask `Nothing` how many rows it has you first need something there.

---

## Week 15 · Units 4 and 5 · Reports and R1C1

### 15.1 · Recognise

**Solution**

In (a), the first line stops with error 438, `Object doesn't support this property or method`: `Left` belongs to VBA and does not turn up under `WorksheetFunction`. The second returns `Aceros`.

In (b), `WorksheetFunction.VLookup` stops with error 1004 when the code is not there. `Application.VLookup` does not stop: it returns the error value `#N/A` as a value, and that is why `IsError(v)` prints `True`. The one that lets you carry on is the `Application` one.

In (c), both cells show 30 when they are written. After A1 changes to 100, C1 goes to 120 because the formula is still live in the cell, and D1 stays at 30 because all that was left there was the number the calculation gave at the moment the macro ran.

In (d) it prints `=RC[-2]*RC[-1]`.

**Output**

```text
(a)  Error 438  /  Aceros
(b)  Error 1004 /  True
(c)  when written:      C1 = 30    D1 = 30
     after A1 = 100:    C1 = 120   D1 = 30
(d)  =RC[-2]*RC[-1]
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| (a) names the 438 and returns `Aceros` | 2 |
| (b) names the 1004 and says `Application` returns the error as a value | 3 |
| (c) the four values, before and after | 3 |
| (d) the exact R1C1 string | 2 |

**Most common mistake**

Writing that `Application.VLookup` returns an empty string. It returns an error value, and that is why it has to be received in a `Variant` and asked with `IsError`.

### 15.2 · Apply

**Solution**

```vba
Option Explicit

Sub CompleteMovements()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim r As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Movements")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For r = 2 To lastRow
        ' v has to be a Variant: a String cannot receive an error value,
        ' and the assignment blows up before it can be checked.
        v = Application.VLookup(ws.Cells(r, 1).Value, _
                                Range("Catalogue"), 2, False)

        If IsError(v) Then
            ws.Cells(r, 3).Value = "not in catalogue"
            ws.Range(ws.Cells(r, 1), ws.Cells(r, 3)) _
                .Interior.Color = RGB(255, 235, 156)
        Else
            ws.Cells(r, 3).Value = v
        End If
    Next r

    ws.Range("E1").Value = WorksheetFunction.SumIfs( _
        ws.Range(ws.Cells(2, 2), ws.Cells(lastRow, 2)), _
        ws.Range(ws.Cells(2, 3), ws.Cells(lastRow, 3)), _
        "Aceros del Bajío")
    ws.Range("E1").NumberFormat = "$#,##0.00"

    ws.Range("E2").Value = WorksheetFunction.CountIf( _
        ws.Range(ws.Cells(2, 3), ws.Cells(lastRow, 3)), _
        "Aceros del Bajío")
End Sub
```

**Output**

```text
C2 = Aceros del Bajío
C3 = Empaques Lira
C4 = Aceros del Bajío
C5 = Papelera Central
C6 = not in catalogue      row 6 in yellow
C7 = Empaques Lira
C8 = Aceros del Bajío
C9 = Papelera Central

E1 = 65650      shows $65,650.00
E2 = 3
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Uses `Application.VLookup` and not `WorksheetFunction.VLookup` | 3 |
| The variable receiving the lookup is a `Variant` and is checked with `IsError` | 2 |
| Row 6 is flagged and the macro reaches row 9 | 2 |
| E1 at 65,650.00 and E2 at 3 | 2 |
| The comment explains why a `String` is no use | 1 |

**Most common mistake**

Declaring the variable `As String`. The assignment of the error value blows up with a 13 before `IsError` gets a chance to look at it, so the net falls down on the very line it was there to protect.

### 15.3 · Integrate

**Solution**

```vba
Option Explicit

Sub CatalogueReport()
    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    Call CleanNames
    Call ComputeValue

    ' The column E formulas have to be evaluated before SumIfs reads them,
    ' so automatic calculation goes back on here.
    Application.Calculation = xlCalculationAutomatic

    Call SummariseBySupplier
    Call ChartSummary

    Application.ScreenUpdating = True
End Sub

Sub CleanNames()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim cell As Range

    Set ws = ThisWorkbook.Worksheets("Suppliers")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For Each cell In ws.Range(ws.Cells(2, 2), ws.Cells(lastRow, 2))
        cell.Value = Replace(cell.Value, Chr(160), " ")
        cell.Value = WorksheetFunction.Trim(cell.Value)
        cell.Value = WorksheetFunction.Proper(cell.Value)
    Next cell
End Sub

Sub ComputeValue()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim values As Range

    Set ws = ThisWorkbook.Worksheets("Suppliers")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    Set values = ws.Range(ws.Cells(2, 5), ws.Cells(lastRow, 5))

    values.FormulaR1C1 = "=RC[-2]*RC[-1]"
    values.NumberFormat = "$#,##0.00"
End Sub

Sub SummariseBySupplier()
    Dim ws As Worksheet
    Dim wr As Worksheet
    Dim lastRow As Long
    Dim r As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Suppliers")
    Set wr = ThisWorkbook.Worksheets("Summary")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    wr.Range("A1").Value = "Supplier"
    wr.Range("B1").Value = "Value"
    wr.Range("C1").Value = "Sector"
    wr.Range("A2").Value = "Aceros Del Bajío"
    wr.Range("A3").Value = "Empaques Lira"
    wr.Range("A4").Value = "Papelera Central"

    For r = 2 To 4
        wr.Cells(r, 2).Value = WorksheetFunction.SumIfs( _
            ws.Range(ws.Cells(2, 5), ws.Cells(lastRow, 5)), _
            ws.Range(ws.Cells(2, 2), ws.Cells(lastRow, 2)), _
            wr.Cells(r, 1).Value)
        wr.Cells(r, 2).NumberFormat = "$#,##0.00"

        v = Application.VLookup(wr.Cells(r, 1).Value, _
                                Range("Catalogue"), 2, False)
        If IsError(v) Then
            wr.Cells(r, 3).Value = "not in catalogue"
        Else
            wr.Cells(r, 3).Value = v
        End If
    Next r
End Sub

Sub ChartSummary()
    Dim wr As Worksheet
    Dim ch As ChartObject

    Set wr = ThisWorkbook.Worksheets("Summary")

    Do While wr.ChartObjects.Count > 0
        wr.ChartObjects(1).Delete
    Loop

    Set ch = wr.ChartObjects.Add(250, 20, 320, 200)
    ch.Chart.SetSourceData wr.Range("A1:B4")
    ch.Chart.ChartType = xlColumnClustered
    ch.Chart.HasTitle = True
    ch.Chart.ChartTitle.Text = "Value by supplier"
End Sub
```

**Output**

```text
Column E of Suppliers, written with a single statement:
  E2  =C2*D2  ->   $77,700.00
  E3  =C3*D3  ->   $11,610.00
  E4  =C4*D4  ->   $18,000.00
  E5  =C5*D5  ->   $16,000.00
  E6  =C6*D6  ->   $21,930.00

Summary sheet:
  Aceros Del Bajío    $95,700.00    Metals
  Empaques Lira       $33,540.00    Packaging
  Papelera Central    $16,000.00    not in catalogue

  Grand total        $145,240.00
  One column chart on the sheet, title Value by supplier
```

Column E is left as a live formula because the report is reopened every month with new stock. If the deliverable were the closed cut of one month, freezing the value would be the right call.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cleaning leaves column B even before anything is grouped | 2 |
| Column E is written with a single statement in R1C1 | 3 |
| The summary uses `SumIfs` and gives the three right totals | 2 |
| The sector lookup does not stop the macro and flags Papelera Central | 2 |
| The chart is created and does not stack up when run twice | 1 |

**Most common mistake**

Building the column E formula by gluing the row number in, with something like `"=C" & r & "*D" & r` inside a loop. It works and it is the route R1C1 was there to avoid, so it does not earn the criterion.

Grading note: if the student leaves calculation on manual for the whole procedure, `SumIfs` reads zeros and the three totals come out at zero, with no error at all. It is worth asking about in the review even when the result is right.

---

## Week 16 · Units 4 and 6 · Pivots, errors and protection

### 16.1 · Recognise

**Solution**

| Moment | Grand total |
|---|---|
| Freshly created | 967215 |
| After changing the row 2 amount to 200,000 | 967215 |
| After `pt.RefreshTable` | 1038815 |
| After adding row 10 and refreshing again | 1038815 |

The pivot writes the data field with the `General` format, so the grand total shows as a bare number until somebody gives that field a format of its own.

They are two different failures. The first is the cache: the pivot reads a copy of the data, not the sheet, and refreshing fills it again. The second is not fixed by refreshing, because the cache was built over `A1:D9` and row 10 falls outside that range. For new rows to get in, the source has to be a table.

In the `Err` block, the message does come up: it says `The sum failed` even though the sum ran perfectly. `Err.Number` is 0 before the `Open`, 1004 the moment the file is not there, and still 1004 after `total = 2 + 2`, because `Resume Next` does not handle the error, it just carries on and clears nothing.

The two missing statements are checking `Err.Number` on the line immediately after the `Open` and clearing with `Err.Clear` before carrying on. Switching the stretch off with `On Error GoTo 0` as soon as the risky part is past is the third, and it is the one that stops the rest of the procedure from staying covered.

**Output**

```text
freshly created .... 967215
amount changed ..... 967215
after RefreshTable . 1038815
new row ............ 1038815

Err before the Open ........ 0
Err after the Open ......... 1004
Err after 2 + 2 ............ 1004
Message box: The sum failed
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The four grand totals | 4 |
| Tells the cache failure from the fixed range failure | 2 |
| Says the message comes up and that `Err` is still 1004 | 2 |
| Proposes checking immediately and clearing with `Err.Clear` | 2 |

**Most common mistake**

Answering that after the second refresh the total does include the new sale. It is what the word refresh leads you to expect, and it is the reason the fixed range charges for itself three weeks running.

### 16.2 · Apply

**Solution**

```vba
Option Explicit

Sub RegionalBreakdown()
    Dim ws As Worksheet
    Dim wd As Worksheet
    Dim pc As PivotCache
    Dim pt As PivotTable

    On Error GoTo Failed

    Application.ScreenUpdating = False

    Set ws = ThisWorkbook.Worksheets("Sales")
    Set wd = ThisWorkbook.Worksheets("Summary")

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create( _
        xlDatabase, ws.Range("A1").CurrentRegion)
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Breakdown")

    pt.PivotFields("Region").Orientation = xlRowField
    pt.PivotFields("Amount").Orientation = xlDataField
    pt.RefreshTable

    Application.ScreenUpdating = True
    Exit Sub

Failed:
    MsgBox "Stopped with error " & Err.Number & ": " & Err.Description
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
End Sub
```

**Output**

```text
Summary sheet:

  Row Labels    Sum of Amount
  Bajío                181045
  Centro               153200
  Norte                325720
  Sur                  307250
  Grand Total          967215
```

Two things about that block. The header of the data field is written by Excel in the language of its interface: on an English installation it says `Sum of Amount` and on a Spanish one, `Suma de Amount`. That string is not marked. And the numbers arrive with the `General` format, which is why they show without a thousands separator; giving the field a format of its own is a separate step nobody asked for here.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The cache is built with `CurrentRegion` and not a written range | 2 |
| The two fields with the right orientation | 2 |
| Running twice does not blow up because the previous pivot is deleted | 2 |
| `On Error GoTo` with a label, and `Exit Sub` before it | 3 |
| The handler reports number and description, and restores what it switched off | 1 |

**Most common mistake**

Forgetting the `Exit Sub` before the label. The normal flow walks into the handler and out comes a box reporting error 0 with an empty description, on a run that went perfectly.

### 16.3 · Integrate

**Solution**

In `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    Dim ws As Worksheet

    For Each ws In ThisWorkbook.Worksheets
        ws.Protect Password:="tia503", UserInterfaceOnly:=True
    Next ws
End Sub
```

In a standard module:

```vba
Option Explicit

Sub CloseProject()
    Dim ws As Worksheet
    Dim wd As Worksheet
    Dim tbl As ListObject
    Dim pc As PivotCache
    Dim pt As PivotTable

    On Error GoTo Failed

    Application.ScreenUpdating = False
    Application.EnableEvents = False

    Set ws = ThisWorkbook.Worksheets("Sales")
    Set wd = ThisWorkbook.Worksheets("Summary")

    If ws.ListObjects.Count = 0 Then
        Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1").CurrentRegion, , xlYes)
        tbl.Name = "Sales2026"
    End If

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, "Sales2026")
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Breakdown")

    pt.PivotFields("Region").Orientation = xlRowField
    pt.PivotFields("Amount").Orientation = xlDataField
    pt.RefreshTable

    Application.EnableEvents = True
    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
    Exit Sub

Failed:
    MsgBox "Stopped with error " & Err.Number & ": " & Err.Description
    Application.EnableEvents = True
    Application.Calculation = xlCalculationAutomatic
    Application.ScreenUpdating = True
End Sub
```

`UserInterfaceOnly` has to be reapplied every time the workbook opens because it is a flag of the session, not of the file: saving keeps the protection, but not the permission for code to write. Measured, on reopening a workbook protected that way the first write from a macro comes back with error 1004 while `ProtectContents` still reads `True`.

If the macro stopped just after switching events off, Excel would be left with no events until somebody closed it. The sheet and workbook handlers would stop firing and there would be no warning at all. That is why the error handler switches them back on before it ends.

**Output**

```text
Pivot over the table Sales2026:
  Row Labels    Sum of Amount
  Bajío                181045
  Centro               153200
  Norte                325720
  Sur                  307250
  Grand Total          967215

Two sales added at the end of the table, 30,000 in Norte and 20,000 in Sur,
and refreshed:
  Bajío                181045
  Centro               153200
  Norte                355720
  Sur                  327250
  Grand Total         1017215
  the breakdown picks them up without touching a single range in the code

Protection, measured:
  just applied, macro writes into the cell   ->  Err 0, the value goes in
  after saving and reopening, macro writes   ->  Err 1004
  ProtectContents after reopening            ->  True
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The pivot is built over the table and grows with it | 3 |
| The protection is reapplied in `Workbook_Open` with `UserInterfaceOnly` | 3 |
| The handler restores events, calculation and screen whatever happens | 2 |
| Explains why the flag does not survive the save | 1 |
| Explains what would happen if it died with events switched off | 1 |

**Most common mistake**

Protecting without `UserInterfaceOnly` and unprotecting at the start of every macro to reprotect at the end. It works until the first macro that blows up halfway and leaves the workbook wide open.

---

## Week 17 · Closing · Final exam

### 17.1 · Recognise

**Solution**

| Scenario | Err | Why |
|---|---|---|
| Dividing by an empty cell | 11 | The empty cell is read as zero and VBA does not divide by zero |
| `CDbl` over `fifteen` | 13 | Type mismatch: there is no number to convert |
| An object declared without `New` | 91 | `Dim` reserves the name, it does not create the object |
| `WorksheetFunction.Left` | 438 | `Left` belongs to VBA and does not live in `WorksheetFunction` |
| `WorksheetFunction.VLookup` with no match | 1004 | It raises the error instead of returning `#N/A` |

The six that give no warning:

| Operation | What it produces |
|---|---|
| Sorting only the amounts column | The amounts get ordered and the names stay put: every row says something false |
| Walking a filtered range with `For Each` | It adds up the hidden rows too and the total comes from the whole range |
| A misspelled criteria header in the advanced filter | It hides every row and the report comes out empty |
| Subtotals without sorting first | A break every time the value changes, so no break closes a whole group |
| Reading a pivot without refreshing | The total of the previous run, with yesterday's data |
| Checking `Err.Number` three lines later | It blames a statement that ran perfectly |

None of the six raises an error. That is what makes them expensive: the file looks normal and the number reaches the report.

**Output**

```text
Err  11, 13, 91, 438, 1004
Silent failures: six, and not one of them raises anything
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The five error numbers, one point each | 5 |
| The six silent failures with the wrong result each one produces | 3 |
| Says that none of the six raises an error | 2 |

**Most common mistake**

Assigning the 1004 to the division by an empty cell. The 1004 is Excel saying it cannot do something with an object; dividing by zero is VBA's and it is the 11.

### 17.2 · Apply

**Solution**

```vba
Option Explicit

Sub FixedReport()
    Dim lastRow As Long
    Dim r As Long
    Dim v As Variant

    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    For r = lastRow To 2 Step -1
        If Cells(r, 4).Value < 50000 Then
            Rows(r).Delete
        End If
    Next r

    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    Range(Cells(1, 1), Cells(lastRow, 4)).Sort _
        Key1:=Range("D1"), Order1:=xlAscending, Header:=xlYes

    Application.Calculation = xlCalculationAutomatic

    For r = 2 To lastRow
        v = Application.VLookup(Cells(r, 1).Value, Range("Catalogue"), 2, False)
        If IsError(v) Then
            Cells(r, 5).Value = "not in catalogue"
        Else
            Cells(r, 5).Value = v
        End If
    Next r

    Application.ScreenUpdating = True
End Sub
```

| Defect | What it does wrong | What it produces | Week |
|---|---|---|---|
| Calculation is left on manual | It never goes back to automatic | Excel stops updating formulas and the user concludes their data is wrong | 7 |
| The delete loop walks forwards | Delete a row and the one below climbs into a spot the loop has already passed | It skips half the rows it was meant to delete | 9 |
| Both loops run 2 to 9 | The limit is typed, not worked out | On a bigger database it leaves rows unprocessed, and on a smaller one it writes past the data | 6 |
| The `Sort` gets only `D2:D9` | It sorts a single column | The amounts get ordered and the names stay put: every row says something false | 13 |
| `WorksheetFunction.VLookup` | It raises the error instead of returning it | It stops at the first missing code and leaves the report split | 15 |

**Output**

Run over the eight-row sales database, where every amount is above 50,000 so nothing gets deleted:

```text
8 rows of data left, sorted ascending by amount, each row with its own salesperson

  V-1007   Norte    Carla Méndez     54,120.00   not in catalogue
  V-1006   Centro   Beto Lira        65,900.00   not in catalogue
  V-1004   Centro   Darío Sáenz      87,300.00   not in catalogue
  V-1002   Sur      Beto Lira        96,750.00   not in catalogue
  V-1001   Norte    Ana Robles      128,400.00   North quarterly
  V-1003   Norte    Carla Méndez    143,200.00   North annual
  V-1008   Bajío    Darío Sáenz     181,045.00   Bajío annual
  V-1005   Sur      Ana Robles      210,500.00   South annual

Before: the macro runs, raises no error, and the report is wrong in five ways
After:  it runs on a database of any size, every row keeps its own data,
        and the missing codes are flagged as not in catalogue
```

Worth pointing out in the review even though it is not one of the five: an empty amount cell compares as zero, so the condition `< 50000` deletes it. If the business does not want that, the condition needs an `IsEmpty` in front of it.

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| Calculation goes back to automatic before it ends | 2 |
| The delete walks from the bottom up | 2 |
| The last row is worked out, and worked out again after the delete | 2 |
| The `Sort` covers the four columns and declares the header | 2 |
| The lookup uses `Application` and `IsError` | 1 |
| The table names the five defects with their week | 1 |

**Most common mistake**

Fixing the `Sort` range and leaving `Header:=xlNo`. The header joins the pile and ends up in the middle of the database, sorted as though it were one more sale.

### 17.3 · Integrate

**Solution**

In `ThisWorkbook`:

```vba
Private Sub Workbook_Open()
    Dim ws As Worksheet

    For Each ws In ThisWorkbook.Worksheets
        ws.Protect Password:="tia503", UserInterfaceOnly:=True
    Next ws
End Sub
```

In a standard module:

```vba
Option Explicit

Function SaleTier(ByVal amount As Double) As String
    Select Case amount
        Case Is >= 150000
            SaleTier = "A"
        Case Is >= 100000
            SaleTier = "B"
        Case Is >= 50000
            SaleTier = "C"
        Case Else
            SaleTier = "D"
    End Select
End Function

Sub ProcessSales()
    On Error GoTo Failed

    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Application.Calculation = xlCalculationManual

    Call EvenOutRegion
    Call DeleteBlanks
    Call RemoveRepeats
    Call SortSales

    Application.Calculation = xlCalculationAutomatic

    Call ClassifySales
    Call FetchManager
    Call ConvertToTable
    Call BuildBreakdown
    Call ChartSummary

    Application.EnableEvents = True
    Application.ScreenUpdating = True
    Exit Sub

Failed:
    MsgBox "Stopped with error " & Err.Number & ": " & Err.Description
    Application.Calculation = xlCalculationAutomatic
    Application.EnableEvents = True
    Application.ScreenUpdating = True
End Sub

Sub ClassifySales()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim r As Long

    Set ws = ThisWorkbook.Worksheets("Sales")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    ws.Cells(1, 5).Value = "Tier"

    For r = 2 To lastRow
        If IsEmpty(ws.Cells(r, 4).Value) Then
            ws.Cells(r, 5).Value = "no amount"
        Else
            ws.Cells(r, 5).Value = SaleTier(ws.Cells(r, 4).Value)
        End If
    Next r
End Sub

Sub FetchManager()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim r As Long
    Dim v As Variant

    Set ws = ThisWorkbook.Worksheets("Sales")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    ws.Cells(1, 6).Value = "Manager"

    For r = 2 To lastRow
        v = Application.VLookup(ws.Cells(r, 3).Value, _
                                Range("Catalogue"), 2, False)
        If IsError(v) Then
            ws.Cells(r, 6).Value = "not in catalogue"
        Else
            ws.Cells(r, 6).Value = v
        End If
    Next r
End Sub

Sub BuildBreakdown()
    Dim wd As Worksheet
    Dim pc As PivotCache
    Dim pt As PivotTable

    Set wd = ThisWorkbook.Worksheets("Summary")

    Do While wd.PivotTables.Count > 0
        wd.PivotTables(1).TableRange2.Clear
    Loop

    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, "Sales2026")
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Breakdown")

    pt.PivotFields("Region").Orientation = xlRowField
    pt.PivotFields("Amount").Orientation = xlDataField
    pt.RefreshTable
End Sub
```

`EvenOutRegion`, `DeleteBlanks`, `RemoveRepeats` and `SortSales` are the ones from 13.3 unchanged. `ConvertToTable` is the one from 14.3 and `ChartSummary` the one from 15.3, pointed at the `Summary` sheet.

The procedure that fails in silence if you take away the last-row line is any of the ones that walk, but the most expensive is `ClassifySales`: without that line you have to type a limit, and on a database longer than the test one it leaves rows with no tier, flagging nothing and stopping nowhere.

**Output**

```text
Database when it finishes:
  even regions, no blank rows, no repeated refs
  sorted by region ascending and by amount descending
  Tier column written by SaleTier, usable from a cell as well
  Manager column with the missing salesperson flagged as not in catalogue

Summary sheet:
  pivot over the table Sales2026, region down the rows and amount in the data
  column chart of the same breakdown

On opening the workbook:
  every sheet protected, and the macros still writing
```

**Rubric** (totals 10)

| Criterion | Points |
|---|---|
| The database comes out clean, no blanks, no repeats and sorted correctly | 2 |
| The tier comes from a function of the student's that also runs in a cell | 2 |
| The manager lookup does not stop the macro and flags the missing one | 1 |
| The pivot and the chart are built over the table and grow with it | 2 |
| The handler restores calculation, events and screen whatever happens | 1 |
| The protection with `UserInterfaceOnly` is reapplied on open | 1 |
| No loop carries a hand-typed address | 1 |

**Most common mistake**

Handing in the workbook without running it again from scratch over fresh data. A macro tested in pieces leaves the database half cleaned, and the breakdown comes out of a cache that no longer matches. A workbook that does not run is capped at 30 %.
