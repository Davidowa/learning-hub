Attribute VB_Name = "MacRegression"
Option Explicit
Private result As Worksheet
Private nextRow As Long
Private lastMessage As String
Private Sub Check(id As String, actual As Variant, expected As Variant)
    result.Cells(nextRow, 1).Value = id
    result.Cells(nextRow, 2).Value = 0
    result.Cells(nextRow, 3).Value = IIf(CStr(actual) = CStr(expected), "PASS", "FAIL")
    result.Cells(nextRow, 4).Value = CStr(actual)
    result.Cells(nextRow, 5).Value = CStr(expected)
    nextRow = nextRow + 1
End Sub
Public Sub RunMacRegression()
    Dim data As Worksheet
    Set result = ThisWorkbook.Worksheets.Add
    result.Name = "MacRegressionResults"
    result.Range("A1:E1").Value = Array("Test", "Week", "Status", "Actual", "Expected")
    result.Columns("D:E").NumberFormat = "@"
    nextRow = 2
    Set data = ThisWorkbook.Worksheets.Add
    data.Range("A2").Value = " ANA" & WorksheetFunction.Unichar(160) & "  LOPEZ "
    data.Range("A3").Value = "Ana" & WorksheetFunction.Unichar(160)
    LimpiarNombres
    Check "mac_es_clean_full_name", data.Range("A2").Value, "Ana Lopez"
    Check "mac_es_clean_trailing_nbsp", data.Range("A3").Value, "Ana"
    data.Range("A2").Value = " ANA" & WorksheetFunction.Unichar(160) & "  LOPEZ "
    data.Range("A3").Value = "Ana" & WorksheetFunction.Unichar(160)
    CleanNames
    Check "mac_en_clean_full_name", data.Range("A2").Value, "Ana Lopez"
    Check "mac_en_clean_trailing_nbsp", data.Range("A3").Value, "Ana"
    ThisWorkbook.Names.Add Name:="LoanAmount", RefersTo:="='" & data.Name & "'!$D$1"
    data.Range("D1").Value = "abc"
    ValidateLoan
    Check "mac_form_text_rejected", lastMessage, "Enter a numeric amount."
    data.Range("D1").Value = 0
    ValidateLoan
    Check "mac_form_zero_rejected", lastMessage, "Enter a positive amount."
    data.Range("D1").Value = -1
    ValidateLoan
    Check "mac_form_negative_rejected", lastMessage, "Enter a positive amount."
    data.Range("D1").Value = 1000
    ValidateLoan
    Check "mac_form_positive_accepted", lastMessage, "Amount accepted."
    result.Activate
    result.Columns("A:E").AutoFit
End Sub
Sub LimpiarNombres()
    Dim celda As Range

    For Each celda In Range("A2:A200")
        celda.Value = WorksheetFunction.Trim( _
            Replace(celda.Value, _
            WorksheetFunction.Unichar(160), " "))
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub

Sub CleanNames()
    Dim cell As Range

    For Each cell In Range("A2:A200")
        cell.Value = WorksheetFunction.Trim( _
            Replace(cell.Value, _
            WorksheetFunction.Unichar(160), " "))
        cell.Value = WorksheetFunction.Proper(cell.Value)
    Next cell
End Sub

Sub ValidateLoan()
    Dim amount As Variant
    amount = Range("LoanAmount").Value
    If Not IsNumeric(amount) Then
        lastMessage = "Enter a numeric amount."
        Exit Sub
    End If
    If CDbl(amount) <= 0 Then
        lastMessage = "Enter a positive amount."
        Exit Sub
    End If
    lastMessage = "Amount accepted."
End Sub
