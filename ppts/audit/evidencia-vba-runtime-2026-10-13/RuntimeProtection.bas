Attribute VB_Name = "RuntimeProtection"
Option Explicit
Private out As Worksheet
Private row As Long
Private Sub Record(id As String, w As Long, got As Variant, want As Variant)
    out.Cells(row, 1).Value = id
    out.Cells(row, 2).Value = w
    out.Cells(row, 3).Value = IIf(CStr(got) = CStr(want), "PASS", "FAIL")
    out.Cells(row, 4).Value = CStr(got)
    out.Cells(row, 5).Value = CStr(want)
    row = row + 1
End Sub
Public Sub RunProtectionRoundtrip()
    Dim ws As Worksheet, wb As Workbook, p As String
    Dim old As Boolean, oldAlerts As Boolean, n As Long
    old = Application.EnableEvents
    oldAlerts = Application.DisplayAlerts
    Set out = ThisWorkbook.Worksheets.Add
    out.Name = "VBAProtection"
    out.Range("A1:E1").Value = Array("Test", "Week", "Status", "Actual", "Expected")
    out.Columns("D:E").NumberFormat = "@"
    row = 2
    On Error GoTo Failed
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
