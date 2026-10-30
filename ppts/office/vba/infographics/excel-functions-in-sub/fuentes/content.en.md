# Use Excel functions inside a Sub

A macro can call SUM, AVERAGE, and MAX, then write their results to cells.

## Start with the data

Create a worksheet named Data in the workbook that contains the macro. Enter these numbers:

| Cell | Value |
| --- | --- |
| B2 | 10 |
| B3 | 20 |
| B4 | 30 |
| B5 | 40 |

## Run one complete macro

Paste this code into a standard module. Option Explicit belongs at the top of the module.

```vb
Option Explicit

Sub BuildSummary()
    Dim ws As Worksheet
    Dim data As Range
    Set ws = ThisWorkbook.Worksheets("Data")
    Set data = ws.Range("B2:B5")
    With Application.WorksheetFunction
        ws.Range("E2").Value = .Sum(data)
        ws.Range("E3").Value = .Average(data)
        ws.Range("E4").Value = .Max(data)
    End With
    ws.Range("E6").Formula = "=SUM(B2:B5)"
End Sub
```

## Read the macro

Set assigns the worksheet and range objects. Inside With, .Sum(data) means Application.WorksheetFunction.Sum(data). The range data supplies the numbers. Each .Value assignment writes a calculated number. The .Formula assignment writes an Excel formula as text beginning with =.

## Check the results

| Cell | What the macro writes | Initial result |
| --- | --- | --- |
| E2 | SUM result stored as a value | 100 |
| E3 | AVERAGE result stored as a value | 25 |
| E4 | MAX result stored as a value | 40 |
| E6 | =SUM(B2:B5) stored as a formula | 100 |

Change B5 from 40 to 80. E2, E3, and E4 keep their stored values until the macro runs again. E6 becomes 140 when Excel recalculates. After rerunning the macro, E2 is 140, E3 is 35, and E4 is 80.

## Run it in Excel

Save the workbook as .xlsm and allow macros for this trusted file. Select Developer > Macros > BuildSummary > Run in desktop Excel. The macro writes E2:E4 and E6 on Data. Use numeric input cells without Excel error values.

## Remember

Use WorksheetFunction to calculate now. Use .Formula to leave a formula that recalculates. A Sub performs these actions without returning a value through its name. Use English function names in VBA and in .Formula, even when Excel displays another language.
