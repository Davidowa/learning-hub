Attribute VB_Name = "RuntimeEvents"
Option Explicit
Private out As Worksheet
Private row As Long
Public WrongModuleCount As Long
Public EventCount As Long
Public SelectionCount As Long
Public LastSelection As String
Public SafeWriteMode As Boolean
Public RecursiveProbe As Boolean
Private Sub Record(id As String, w As Long, got As Variant, want As Variant)
    out.Cells(row, 1).Value = id
    out.Cells(row, 2).Value = w
    out.Cells(row, 3).Value = IIf(CStr(got) = CStr(want), "PASS", "FAIL")
    out.Cells(row, 4).Value = CStr(got)
    out.Cells(row, 5).Value = CStr(want)
    row = row + 1
End Sub
Private Sub Prepare()
    On Error Resume Next
    Set out = ThisWorkbook.Worksheets("VBAExtension")
    On Error GoTo 0
    If out Is Nothing Then
        Set out = ThisWorkbook.Worksheets.Add
        out.Name = "VBAExtension"
    End If
    If row = 0 Then
        out.Cells.Clear
        out.Range("A1:E1").Value = Array("Test", "Week", "Status", "Actual", "Expected")
        out.Columns("D:E").NumberFormat = "@"
        row = 2
    End If
End Sub
Public Sub RunExtensionTests()
    Dim ws As Worksheet, wb As Workbook, p As String
    Dim old As Boolean, oldAlerts As Boolean, n As Long
    old = Application.EnableEvents
    oldAlerts = Application.DisplayAlerts
    Prepare
    On Error GoTo Failed
    Set ws = ThisWorkbook.Worksheets.Add
    ws.Name = "NameCleaningTest"
    ws.Range("A2").Value = "  ANA" & WorksheetFunction.Unichar(160) & "  LOPEZ "
    ws.Range("A3").Value = "Ana" & WorksheetFunction.Unichar(160)
    CleanNamesOriginal
    Record "original_mac_cleaner_keeps_nbsp", 13, InStr(ws.Range("A3").Value, WorksheetFunction.Unichar(160)) > 0, True
    CleanNamesMac
    Record "mac_cleaner_full_name", 13, ws.Range("A2").Value, "Ana Lopez"
    Record "mac_cleaner_trailing_nbsp", 13, ws.Range("A3").Value, "Ana"
    Application.EnableEvents = False
    ThisWorkbook.Worksheets("Sheet1").Cells.Clear
    SafeWriteMode = False
    RecursiveProbe = False
    EventCount = 0
    Application.EnableEvents = True
    ThisWorkbook.Worksheets("Sheet1").Range("A1").Value = 12
    Record "worksheet_change_numeric", 11, ThisWorkbook.Worksheets("Sheet1").Range("B1").Value, "Numero"
    Record "guard_allows_one_nested_b1_event", 11, EventCount, 2
    ThisWorkbook.Worksheets("Sheet1").Range("A1").Value = "abc"
    Record "worksheet_change_text", 11, ThisWorkbook.Worksheets("Sheet1").Range("B1").Value, "No es numero"
    SafeWriteMode = True
    EventCount = 0
    ThisWorkbook.Worksheets("Sheet1").Range("A1").Value = 50
    Record "disabled_events_prevent_recursion", 11, EventCount, 1
    Record "events_restored", 11, Application.EnableEvents, True
    RecursiveProbe = True
    EventCount = 0
    ThisWorkbook.Worksheets("Sheet1").Range("D1").Value = "start"
    Record "unguarded_write_repeats_bounded_at_five", 11, EventCount, 5
    RecursiveProbe = False
    ThisWorkbook.Worksheets("Sheet1").Activate
    SelectionCount = 0
    ThisWorkbook.Worksheets("Sheet1").Range("D7").Select
    Record "selection_change_address", 11, LastSelection, "$D$7"
    Record "selection_change_fired", 11, SelectionCount, 1
    Set ws = ThisWorkbook.Worksheets.Add
    ws.Name = "NoEventHandler"
    WrongModuleCount = 0
    ws.Range("A1").Value = 100
    Record "standard_module_event_never_fires", 11, WrongModuleCount, 0
    Application.EnableEvents = False
    Set wb = Workbooks.Add
    Set ws = wb.Worksheets(1)
    ws.Protect Password:="abc", UserInterfaceOnly:=True
    ws.Range("A1").Value = "before save"
    Record "ui_only_before_save", 16, ws.ProtectionMode, True
    p = ThisWorkbook.Path & "/protection-roundtrip.xlsx"
    Application.DisplayAlerts = False
    wb.SaveAs Filename:=p, FileFormat:=xlOpenXMLWorkbook
    wb.Close SaveChanges:=False
    Set wb = Workbooks.Open(p)
    Set ws = wb.Worksheets(1)
    Record "protected_after_reopen", 16, ws.ProtectContents, True
    Record "ui_only_not_persisted", 16, ws.ProtectionMode, False
    On Error Resume Next
    Err.Clear
    ws.Range("A1").Value = "after reopen"
    n = Err.Number
    On Error GoTo Failed
    Record "write_after_reopen_error", 16, n, 1004
    ws.Protect Password:="abc", UserInterfaceOnly:=True
    ws.Range("A1").Value = "after restored ui only"
    Record "restore_ui_only_after_open", 16, ws.Range("A1").Value, "after restored ui only"
    wb.Close SaveChanges:=False
Finished:
    Application.DisplayAlerts = oldAlerts
    Application.EnableEvents = old
    out.Activate
    out.Columns("A:E").AutoFit
    Exit Sub
Failed:
    Record "extension_runtime_error", 0, Err.Number & ": " & Err.Description, "No unexpected error"
    Resume Finished
End Sub
Private Sub CleanNamesOriginal()
    Dim celda As Range
    For Each celda In Range("A2:A200")
        celda.Value = WorksheetFunction.Trim( _
            Replace(celda.Value, Chr(160), " "))
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub
Private Sub CleanNamesMac()
    Dim celda As Range
    For Each celda In Range("A2:A200")
        celda.Value = WorksheetFunction.Trim( _
            Replace(celda.Value, _
            WorksheetFunction.Unichar(160), " "))
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub
Private Sub Worksheet_Change(ByVal Target As Range)
    WrongModuleCount = WrongModuleCount + 1
End Sub
Public Sub RunInputBoxes()
    Dim monto As Double, tasa As Double
    Prepare
    ThisWorkbook.Worksheets("Sheet1").Activate
    monto = CDbl(InputBox("Monto del prestamo", "Captura"))
    tasa = CDbl(InputBox("Tasa anual", "Captura"))
    Range("B1").Value = monto
    Range("B2").Value = tasa
    Record "input_amount", 5, Range("B1").Value, 500000
    Record "input_annual_rate", 5, Range("B2").Value, 0.12
    out.Activate
End Sub
Public Sub RunNumericInputLoop()
    Dim monto As Double, texto As String, valido As Boolean
    Prepare
    valido = False
    Do While Not valido
        texto = InputBox("Monto del prestamo", "Captura")
        If IsNumeric(texto) Then
            monto = CDbl(texto)
            valido = True
        Else
            MsgBox "Eso no es un numero.", vbExclamation
        End If
    Loop
    Record "numeric_loop_recovers_after_abc", 5, monto, 1000
    out.Activate
End Sub
Public Sub RunHelloWorld()
    Prepare
    MsgBox "Hello, World!"
    Record "hello_world_dialog_dismissed", 2, True, True
    out.Activate
End Sub
