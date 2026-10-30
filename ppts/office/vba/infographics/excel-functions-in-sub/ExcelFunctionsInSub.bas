Attribute VB_Name = "ExcelFunctionsInSub"
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
