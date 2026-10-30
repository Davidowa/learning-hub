Attribute VB_Name = "FunctionsExamples"
Option Explicit

Public Function WithTax( _
    ByVal price As Double, _
    ByVal rate As Double) As Double
    WithTax = price * (1 + rate)
End Function

Public Sub Demo()
    Dim total As Double
    total = WithTax(100, 0.08)
    Debug.Print total
End Sub

Public Sub Summarize()
    Dim ws As Worksheet
    Dim data As Range
    Dim total As Double
    Set ws = ThisWorkbook.Worksheets("Data")
    Set data = ws.Range("B2:B5")
    total = Application.WorksheetFunction _
        .Sum(data)
    ws.Range("D2").Value = total
End Sub

Public Sub StoreFormula()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Worksheets("Data")
    ws.Range("D3").Formula = "=SUM(B2:B5)"
End Sub

Public Sub FindCode()
    Dim ws As Worksheet
    Dim ids As Range
    Dim hit As Variant
    Set ws = ThisWorkbook.Worksheets("Data")
    Set ids = ws.Range("A2:A5")
    hit = Application.Match("P-02", ids, 0)
    If IsError(hit) Then
        MsgBox "Not found"
    Else
        MsgBox hit
    End If
End Sub
