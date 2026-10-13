Attribute VB_Name = "RuntimeSuiteV2"
Option Explicit
Private Report As Worksheet
Private rr As Long
Private LastMessage As String
Private oldEvents As Boolean, oldScreen As Boolean, oldAlerts As Boolean
Private oldCalc As XlCalculation

Private Sub Check(id As String, w As Long, got As Variant, want As Variant, Optional tolerance As Double = 0.00000001)
    Dim ok As Boolean
    If IsNumeric(got) And IsNumeric(want) Then
        ok = Abs(CDbl(got) - CDbl(want)) <= tolerance
    Else
        ok = CStr(got) = CStr(want)
    End If
    Report.Cells(rr, 1).Value = id
    Report.Cells(rr, 2).Value = w
    Report.Cells(rr, 3).Value = IIf(ok, "PASS", "FAIL")
    Report.Cells(rr, 4).Value = CStr(got)
    Report.Cells(rr, 5).Value = CStr(want)
    rr = rr + 1
End Sub

Private Sub Unexpected(id As String, w As Long, n As Long, message As String)
    Check id & ".runtime", w, "ERROR " & n & ": " & message, "No unexpected error"
End Sub

Private Function Sheet(n As String) As Worksheet
    On Error Resume Next
    Set Sheet = ThisWorkbook.Worksheets(n)
    On Error GoTo 0
    If Sheet Is Nothing Then
        Set Sheet = ThisWorkbook.Worksheets.Add
        Sheet.Name = n
    End If
End Function

Private Function Fresh(Optional n As String = "Hoja1V2") As Worksheet
    Dim ws As Worksheet, t As ListObject
    Set ws = Sheet(n)
    ws.Unprotect "abc"
    On Error Resume Next
    If ws.FilterMode Then ws.ShowAllData
    ws.AutoFilterMode = False
    For Each t In ws.ListObjects
        t.Unlist
    Next t
    ws.ChartObjects.Delete
    On Error GoTo 0
    ws.Cells.Clear
    ws.Rows.Hidden = False
    ws.Columns.Hidden = False
    ThisWorkbook.Activate
    ws.Activate
    Set Fresh = ws
End Function

Private Sub SeedSales(ws As Worksheet)
    ws.Range("A1").Value = "Depto"
    ws.Range("B1").Value = "Monto"
    ws.Range("A2").Value = "Ventas": ws.Range("B2").Value = 100
    ws.Range("A3").Value = "Compras": ws.Range("B3").Value = 200
    ws.Range("A4").Value = "Ventas": ws.Range("B4").Value = 300
    ws.Range("A5").Value = "Compras": ws.Range("B5").Value = 400
End Sub

Public Sub RunAutoTestsV2()
    Dim ws As Worksheet
    oldEvents = Application.EnableEvents
    oldScreen = Application.ScreenUpdating
    oldCalc = Application.Calculation
    oldAlerts = Application.DisplayAlerts
    On Error GoTo Fatal
    Application.EnableEvents = False
    Application.DisplayAlerts = False
    Set Report = Sheet("VBAResultsV2")
    Report.Cells.Clear
    Report.Range("A1:E1").Value = Array("Test", "Week", "Status", "Actual", "Expected")
    Report.Columns("D:E").NumberFormat = "@"
    rr = 2
    Report.Range("G1").Value = "Excel VBA native runtime"
    Report.Range("G2").Value = Application.Version
    Report.Range("G3").Value = Application.OperatingSystem
    Report.Range("G4").Value = Now
    Call Case01: Call Case02: Call Case03: Call Case04: Call Case05: Call Case06
    Call Case07: Call Case08: Call Case09: Call Case10: Call Case12: Call Case13
    Call Case14Filter: Call Case14Advanced: Call Case14Subtotal: Call Case14Table
    Call Case15Functions: Call Case15Lookup: Call Case15Formula: Call Case15Chart
    Call Case16Pivot: Call Case16Errors: Call Case16Protection: Call Case17
Finished:
    Application.EnableEvents = oldEvents
    Application.ScreenUpdating = oldScreen
    Application.Calculation = oldCalc
    Application.DisplayAlerts = oldAlerts
    Report.Activate
    Report.Range("G6").Value = "PASS"
    Report.Range("H6").Formula = "=COUNTIF(C:C,""PASS"")"
    Report.Range("G7").Value = "FAIL"
    Report.Range("H7").Formula = "=COUNTIF(C:C,""FAIL"")"
    Report.Columns("A:E").AutoFit
    Exit Sub
Fatal:
    Unexpected "suite", 0, Err.Number, Err.Description
    Resume Finished
End Sub
Private Sub Case01()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    P01_18_HideColumn
    Check "hide_column_final", 1, ws.Columns("D:D").Hidden, False
    Exit Sub
Failed:
    Unexpected "Case01", 1, Err.Number, Err.Description
End Sub

Private Sub Case02()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    P02_21_Ejemplo
    Check "range_assignment_1", 2, ws.Range("A1").Value, 10
    Check "range_assignment_2", 2, ws.Range("A2").Value, 20
    Exit Sub
Failed:
    Unexpected "Case02", 2, Err.Number, Err.Description
End Sub

Private Sub Case03()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    On Error Resume Next
    Err.Clear
    P03_10_ContarRenglones
    n = Err.Number
    On Error GoTo Failed
    Check "integer_overflow_rows", 3, n, 6
    P03_16_AccessCells
    Check "range_offset", 3, ws.Range("B3").Value, 6
    P03_19_Redondeo
    Check "integer_bankers_rounding", 3, ws.Range("A1").Value, 2
    Check "date_isnumeric", 3, IsNumeric(DateSerial(2026, 10, 13)), False
    Exit Sub
Failed:
    Unexpected "Case03", 3, Err.Number, Err.Description
End Sub

Private Sub Case04()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    P04_08_Precedencia
    Check "precedence", 4, ws.Range("A1").Value, 11
    Check "parentheses", 4, ws.Range("A2").Value, 16
    P04_13_TasaLegible
    Check "monthly_rate", 4, ws.Range("B1").Value, 0.00948879293458305
    Check "monthly_format_function", 4, Format(ws.Range("B1").Value, "0.00%"), "0.95%"
    Check "monthly_format_cell_value", 4, ws.Range("B2").Value, 0.0095
    Check "monthly_format_cell_text", 4, ws.Range("B2").Text, "0.95%"
    Check "monthly_round", 4, ws.Range("B3").Value, 0.009489
    P04_16_DefinirNombres
    Check "named_range_amount", 4, ws.Range("MontoPrestamoV2").Value, 500000
    Check "named_range_rate", 4, ws.Range("TasaAnualV2").Value, 0.12
    ws.Range("C1").Formula = "=-3^2"
    Check "worksheet_negative_power", 4, ws.Range("C1").Value, 9
    Check "vba_text_plus", 4, "5" + "3", "53"
    Check "vba_mod_negative", 4, -5 Mod 3, -2
    Check "worksheet_mod_negative", 4, Application.Evaluate("MOD(-5,3)"), 1
    Check "vba_power_chain", 4, 2 ^ 3 ^ 2, 64
    P04_19_Cuentas
    Check "negative_power", 4, ws.Range("A1").Value, -9
    Check "integer_division", 4, ws.Range("A2").Value, 4
    Exit Sub
Failed:
    Unexpected "Case04", 4, Err.Number, Err.Description
End Sub

Private Sub Case05()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim t As String
    Set ws = Fresh()
    t = "abc"
    On Error Resume Next
    Err.Clear
    If IsNumeric(t) And CDbl(t) > 0 Then ws.Range("A1").Value = CDbl(t)
    n = Err.Number
    On Error GoTo Failed
    Check "and_is_not_short_circuit", 5, n, 13
    Check "numeric_positive", 5, IsNumeric("500000"), True
    Check "blank_not_numeric", 5, IsNumeric(""), False
    Check "percent_input_005", 5, CDbl("0.05"), 0.05
    Exit Sub
Failed:
    Unexpected "Case05", 5, Err.Number, Err.Description
End Sub

Private Sub Case06()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    ws.Range("A1").Value = "ID"
    For i = 2 To 41: ws.Cells(i, 1).Value = i - 1: ws.Cells(i, 3).Value = i: Next i
    P06_06_FormatearVentas
    Check "fixed_range_stops_at_13", 6, ws.Range("C14").NumberFormat, "General"
    P06_12_FormatearVentas
    Check "dynamic_range_reaches_41", 6, ws.Range("C41").NumberFormat, "$#,##0.00"
    P06_16_AlternarColumnaAuxiliar
    Check "toggle_on", 6, ws.Columns("D:D").Hidden, True
    P06_16_AlternarColumnaAuxiliar
    Check "toggle_off", 6, ws.Columns("D:D").Hidden, False
    Exit Sub
Failed:
    Unexpected "Case06", 6, Err.Number, Err.Description
End Sub

Private Sub Case07()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    ws.Range("B1").Value = 500000
    ws.Range("B2").Value = V2_TasaMensual(0.12)
    ws.Range("B3").Value = 120: ws.Range("B4").Value = 1000
    ws.Range("B5").Formula = "=B1*(1+B2)^B3-B4*((1+B2)^B3-1)/B2"
    ThisWorkbook.Names.Add "SaldoFinalV2", "=Hoja1V2!$B$5"
    ThisWorkbook.Names.Add "PagoMensualV2", "=Hoja1V2!$B$4"
    ws.Calculate
    Check "balance_before_goal_seek", 7, ws.Range("B5").Value, 1330994.06, 0.01
    P07_07_BuscarPagoMensualV2
    Check "payment_after_goal_seek", 7, ws.Range("B4").Value, 6997.36, 0.01
    Check "balance_after_goal_seek", 7, ws.Range("B5").Value, 0, 0.001
    Application.ScreenUpdating = False
    Check "screen_updating_during_execution", 7, Application.ScreenUpdating, False
    Application.ScreenUpdating = oldScreen
    Application.Calculation = xlCalculationManual
    On Error Resume Next
    Err.Raise 5
    n = Err.Number
    On Error GoTo Failed
    Check "calculation_manual_after_error", 7, Application.Calculation, xlCalculationManual
    Application.Calculation = oldCalc
    Exit Sub
Failed:
    Unexpected "Case07", 7, Err.Number, Err.Description
End Sub

Private Sub Case08()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    P08_07_Comparar
    Check "comparison_message", 8, LastMessage, "a es igual a b? True"
    P08_11_Clasificar
    Check "elseif_classification", 8, LastMessage, "C"
    If ws.Range("A1").Value = 0 Then ws.Range("B1").Value = "Sin venta" Else ws.Range("B1").Value = "Con venta"
    Check "empty_cell_compares_to_zero", 8, ws.Range("B1").Value, "Sin venta"
    Exit Sub
Failed:
    Unexpected "Case08", 8, Err.Number, Err.Description
End Sub

Private Sub Case09()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    P09_06_Contar
    Check "loop_message", 9, LastMessage, "Los numeros del 1 al 5 son: 1 2 3 4 5 "
    P09_08_NumerarPeriodos
    Check "period_first", 9, ws.Range("B3").Value, 1
    Check "period_last", 9, ws.Cells(3, 121).Value, 120
    P09_11_MarcarVacias
    Check "empty_cell_fill", 9, ws.Range("A1").Interior.Color, RGB(255, 235, 156)
    Set ws = Fresh()
    ws.Range("A1").Value = "Customer"
    ws.Range("A2").Value = "A": ws.Range("C2").Value = 31
    ws.Range("A3").Value = "B": ws.Range("C3").Value = 30
    P09_14_MarcarMorosos
    Check "past_due_above_30", 9, ws.Range("D2").Value, "Vencido"
    Check "past_due_at_30", 9, ws.Range("D3").Value, ""
    Set ws = Fresh()
    ws.Range("A1:A6").Value = "X"
    For i = 1 To 6
        If ws.Cells(i, 1).Value = "X" Then ws.Rows(i).Delete
    Next i
    Check "forward_delete_skips_rows", 9, WorksheetFunction.CountA(ws.Columns(1)), 3
    Exit Sub
Failed:
    Unexpected "Case09", 9, Err.Number, Err.Description
End Sub

Private Sub Case10()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    Check "summation_function", 10, V2_Summation(5, 3), 8
    Check "rate_function", 10, V2_TasaMensual(0.12), 0.00948879293458305
    P10_15_Facturar
    Check "byref_iva", 10, ws.Range("A1").Value, 1160
    P10_18_Probar
    Check "byref_double", 10, ws.Range("A1").Value, 14
    ws.Range("A1").Value = 0.12
    ws.Range("B1").Formula = "=V2_TasaMensual(A1)"
    ws.Calculate
    Check "udf_in_worksheet", 10, ws.Range("B1").Value, 0.00948879293458305
    Exit Sub
Failed:
    Unexpected "Case10", 10, Err.Number, Err.Description
End Sub

Private Sub Case12()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim e As Empleado, a As Empleado, b As Empleado
    Set e = New Empleado: e.Sueldo = 15000
    Check "class_annual", 12, e.Anual, 180000
    e.Sueldo = -500
    Check "class_negative_salary", 12, e.Sueldo, 0
    Set e = Nothing
    On Error Resume Next
    Err.Clear
    e.Nombre = "Luis"
    n = Err.Number
    On Error GoTo Failed
    Check "class_not_instantiated", 12, n, 91
    Set a = New Empleado: Set b = a
    a.Sueldo = 10000: b.Sueldo = 20000
    Check "class_alias", 12, a.Anual, 240000
    Exit Sub
Failed:
    Unexpected "Case12", 12, Err.Number, Err.Description
End Sub

Private Sub Case13()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim s As String
    Set ws = Fresh()
    Check "vba_trim_preserves_middle", 13, Trim("Ana    Lopez"), "Ana    Lopez"
    Check "excel_trim_collapses_middle", 13, WorksheetFunction.Trim("Ana    Lopez"), "Ana Lopez"
    s = "Ana" & Chr(160)
    Check "trim_keeps_chr160", 13, Len(Trim(s)), 4
    Check "replace_chr160", 13, Trim(Replace(s, Chr(160), " ")), "Ana"
    Check "chr160_is_nbsp_on_mac", 13, AscW(Chr(160)), 160
    Check "chrw160_is_nbsp_on_mac", 13, AscW(ChrW(160)), 160
    Check "unichar160_is_nbsp_on_mac", 13, AscW(WorksheetFunction.Unichar(160)), 160
    ws.Range("A1:B1").Value = Array("Depto", "Nombre")
    ws.Range("A2:B2").Value = Array("Ventas", "primero")
    ws.Range("A3:B3").Value = Array("Compras", "segundo")
    ws.Range("A4:B4").Value = Array("Ventas", "tercero")
    ws.Range("A1:B4").RemoveDuplicates Columns:=1, Header:=xlYes
    Check "duplicates_first_wins", 13, ws.Range("B2").Value, "primero"
    Check "duplicates_count", 13, WorksheetFunction.CountA(ws.Range("A2:A4")), 2
    Set ws = Fresh()
    ws.Range("B1:C1").Value = Array("Depto", "Nombre")
    ws.Range("B2:C2").Value = Array("Ventas", "primero")
    ws.Range("B3:C3").Value = Array("Compras", "segundo")
    ws.Range("B4:C4").Value = Array("Ventas", "tercero")
    ws.Range("B1:C4").RemoveDuplicates Columns:=2, Header:=xlYes
    Check "relative_duplicate_column", 13, WorksheetFunction.CountA(ws.Range("B2:B4")), 3
    Set ws = Fresh("DatosV2")
    ws.Range("A1:C1").Value = Array("Nombre", "Depto", "Sueldo")
    ws.Range("A2:C2").Value = Array("Ana", "Ventas", 15000)
    ws.Range("A3:C3").Value = Array("Beto", "Compras", 22000)
    ws.Range("A4:C4").Value = Array("Carla", "Ventas", 18000)
    P13_16_OrdenarBase
    Check "sort_department", 13, ws.Range("A2").Value, "Beto"
    Check "sort_secondary_desc", 13, ws.Range("A3").Value, "Carla"
    Exit Sub
Failed:
    Unexpected "Case13", 13, Err.Number, Err.Description
End Sub

Private Sub Case14Filter()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh("DatosV2")
    SeedSales ws
    P14_08_SumarSoloVisible
    Check "visible_filter_total", 14, LastMessage, "400"
    Check "filtered_sum_all", 14, WorksheetFunction.Sum(ws.Range("B2:B5")), 1000
    Check "filtered_subtotal", 14, WorksheetFunction.Subtotal(9, ws.Range("B2:B5")), 400
    Exit Sub
Failed:
    Unexpected "Case14Filter", 14, Err.Number, Err.Description
End Sub

Private Sub Case14Advanced()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh("DatosV2"): SeedSales ws
    ws.Range("D1").Value = "Depto": ws.Range("D2").Value = "Ventas"
    ws.Range("A1:B5").AdvancedFilter xlFilterInPlace, ws.Range("D1:D2")
    Check "advanced_matching_header", 14, ws.Range("A2:A5").SpecialCells(xlCellTypeVisible).Count, 2
    ws.ShowAllData
    ws.Range("D1").Value = "Departamento"
    ws.Range("A1:B5").AdvancedFilter xlFilterInPlace, ws.Range("D1:D2")
    n = 0
    For i = 2 To 5
        If Not ws.Rows(i).Hidden Then n = n + 1
    Next i
    Check "advanced_wrong_header", 14, n, 0
    Exit Sub
Failed:
    Unexpected "Case14Advanced", 14, Err.Number, Err.Description
End Sub

Private Sub Case14Subtotal()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh("DatosV2"): SeedSales ws
    ws.Range("A1:B5").Subtotal GroupBy:=1, Function:=xlSum, TotalList:=Array(2)
    Check "subtotal_unsorted_rows", 14, ws.Range("A1").CurrentRegion.Rows.Count, 10
    Set ws = Fresh("DatosV2"): SeedSales ws
    P14_15_SubtotalesPorDepto
    Check "subtotal_sorted_rows", 14, ws.Range("A1").CurrentRegion.Rows.Count, 8
    Exit Sub
Failed:
    Unexpected "Case14Subtotal", 14, Err.Number, Err.Description
End Sub

Private Sub Case14Table()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim tbl As ListObject
    Set ws = Fresh("DatosV2")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    ws.Range("A2:B2").Value = Array("Ventas", 100)
    ws.Range("A3:B3").Value = Array("Compras", 200)
    P14_17_CrearTabla
    Set tbl = ws.ListObjects("Ventas2026")
    ws.Range("D1").Formula = "=SUM(Ventas2026[Monto])"
    ws.Calculate
    Check "table_initial_sum", 14, ws.Range("D1").Value, 300
    tbl.ListRows.Add.Range.Cells(1, 2).Value = 300
    ws.Calculate
    Check "table_expanded_sum", 14, ws.Range("D1").Value, 600
    Set ws = Fresh("DatosV2")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1:B1"), , xlYes)
    Check "empty_table_rows", 14, tbl.ListRows.Count, 0
    Check "empty_table_body", 14, tbl.DataBodyRange Is Nothing, True
    On Error Resume Next
    Err.Clear
    i = tbl.DataBodyRange.Rows.Count
    n = Err.Number
    On Error GoTo Failed
    Check "empty_table_body_error", 14, n, 91
    Exit Sub
Failed:
    Unexpected "Case14Table", 14, Err.Number, Err.Description
End Sub

Private Sub Case15Functions()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Check "vba_left", 15, Left("Hola mundo", 4), "Hola"
    Check "worksheet_trim", 15, WorksheetFunction.Trim("a    b"), "a b"
    Exit Sub
Failed:
    Unexpected "Case15Functions", 15, Err.Number, Err.Description
End Sub

Private Sub Case15Lookup()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    ws.Range("D1").Value = "Ana": ws.Range("E1").Value = 100
    ws.Range("D2").Value = "Beto": ws.Range("E2").Value = 200
    ws.Range("D3").Value = "Carla": ws.Range("E3").Value = 300
    On Error Resume Next
    Err.Clear
    v = WorksheetFunction.VLookup("Zoe", ws.Range("D1:E3"), 2, False)
    n = Err.Number
    On Error GoTo Failed
    Check "worksheet_lookup_missing", 15, n, 1004
    v = Application.VLookup("Zoe", ws.Range("D1:E3"), 2, False)
    Check "application_lookup_missing_iserror", 15, IsError(v), True
    Check "application_lookup_found", 15, Application.VLookup("Ana", ws.Range("D1:E3"), 2, False), 100
    Exit Sub
Failed:
    Unexpected "Case15Lookup", 15, Err.Number, Err.Description
End Sub

Private Sub Case15Formula()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    ws.Range("A1").Value = 10: ws.Range("A2").Value = 20
    ws.Range("C1").Formula = "=SUM(A1:A2)"
    ws.Range("D1").Value = WorksheetFunction.Sum(ws.Range("A1:A2"))
    ws.Range("A1").Value = 100: ws.Calculate
    Check "formula_recalculates", 15, ws.Range("C1").Value, 120
    Check "value_is_snapshot", 15, ws.Range("D1").Value, 30
    ws.Range("A2:A4").Value = 2
    ws.Range("B2:B4").Value = 20
    ws.Range("C2:C4").FormulaR1C1 = "=RC[-2]*RC[-1]"
    ws.Calculate
    Check "r1c1_formula", 15, ws.Range("C2").Formula, "=A2*B2"
    Check "r1c1_value", 15, ws.Range("C4").Value, 40
    Exit Sub
Failed:
    Unexpected "Case15Formula", 15, Err.Number, Err.Description
End Sub

Private Sub Case15Chart()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh("DatosV2")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    ws.Range("A2:B2").Value = Array("Ventas", 100)
    ws.Range("A3:B3").Value = Array("Compras", 200)
    P15_19_GraficaPorDepto
    Check "chart_count", 15, ws.ChartObjects.Count, 1
    Check "chart_series_count", 15, ws.ChartObjects(1).Chart.SeriesCollection.Count, 1
    Check "chart_title", 15, ws.ChartObjects(1).Chart.ChartTitle.Text, "Monto por depto"
    Exit Sub
Failed:
    Unexpected "Case15Chart", 15, Err.Number, Err.Description
End Sub

Private Sub Case16Pivot()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim pt As PivotTable
    Set ws = Fresh("DatosV2"): SeedSales ws
    Set ws = Fresh("ResumenV2")
    P16_06_CorteMensual
    Set pt = ThisWorkbook.Sheets("ResumenV2").PivotTables("Corte")
    Set ws = ThisWorkbook.Sheets("DatosV2")
    Check "pivot_initial", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1000
    ws.Range("B2").Value = 999
    Check "pivot_before_refresh", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1000
    pt.RefreshTable
    Check "pivot_after_refresh", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1899
    ws.Range("A6").Value = "Ventas": ws.Range("B6").Value = 1000
    pt.RefreshTable
    Check "pivot_fixed_cache_excludes_new_row", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1899
    Exit Sub
Failed:
    Unexpected "Case16Pivot", 16, Err.Number, Err.Description
End Sub

Private Sub Case16Errors()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    On Error Resume Next
    Err.Clear
    x = 1 / 0
    n = Err.Number
    Check "division_error", 16, n, 11
    v = CDbl("no soy numero")
    n = Err.Number
    Check "conversion_error", 16, n, 13
    Err.Clear
    Check "err_clear", 16, Err.Number, 0
    x = 1 / 0
    x = 2 + 2
    n = Err.Number
    On Error GoTo Failed
    Check "err_persists_after_valid_addition", 16, n, 11
    Exit Sub
Failed:
    Unexpected "Case16Errors", 16, Err.Number, Err.Description
End Sub

Private Sub Case16Protection()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Set ws = Fresh()
    ws.Protect Password:="abc"
    On Error Resume Next
    Err.Clear
    ws.Range("A1").Value = "la macro escribio"
    n = Err.Number
    On Error GoTo Failed
    Check "protected_write", 16, n, 1004
    ws.Unprotect "abc"
    ws.Protect Password:="abc", UserInterfaceOnly:=True
    ws.Range("A1").Value = "la macro escribio"
    Check "user_interface_only_allows_macro", 16, ws.Range("A1").Value, "la macro escribio"
    Check "user_interface_only_still_protected", 16, ws.ProtectContents, True
    ws.Unprotect "abc"
    Exit Sub
Failed:
    Unexpected "Case16Protection", 16, Err.Number, Err.Description
End Sub

Private Sub Case17()
    On Error GoTo Failed
    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double

    Dim pt As PivotTable, pc As PivotCache, ch As ChartObject, wd As Worksheet
    Set ws = Fresh("DatosV217")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    For i = 2 To 100: ws.Cells(i, 1).Value = "Ventas": ws.Cells(i, 2).Value = 1: Next i
    Set wd = Fresh("ResumenV217")
    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, ws.Range("A1:B100"))
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte17")
    pt.PivotFields("Depto").Orientation = xlRowField
    pt.PivotFields("Monto").Orientation = xlDataField
    Set ch = ws.ChartObjects.Add(200, 20, 300, 200)
    ch.Chart.SetSourceData ws.Range("A1:B100")
    For i = 101 To 120: ws.Cells(i, 1).Value = "Ventas": ws.Cells(i, 2).Value = 10: Next i
    pt.RefreshTable
    Check "final_fixed_pivot", 17, pt.GetPivotData(pt.DataFields(1).Name).Value, 99
    Check "final_fixed_chart", 17, UBound(ch.Chart.SeriesCollection(1).Values), 99
    Exit Sub
Failed:
    Unexpected "Case17", 17, Err.Number, Err.Description
End Sub

Sub P01_18_HideColumn()
'
' P01_18_HideColumn Macro
'

'
    Columns("D:D").EntireColumn.Hidden = True
    Columns("D:D").EntireColumn.Hidden = False
End Sub

Sub P02_21_Ejemplo()
    Range("A1").Value = 10
    Range("A2").Value = 20
End Sub

Sub P03_10_ContarRenglones()
    Dim fila As Integer
    fila = Rows.Count
End Sub

Sub P03_16_AccessCells()
    Range("A1").Value = 1
    Range("A2").Value = 2
    Range("A3").Value = 3

    Range("B1").Value = 2
    Range("B1").Offset(1, 0).Value = 4
    Range("B1").Offset(2, 0).Value = 6
End Sub

Sub P03_19_Redondeo()
    Dim piezas As Integer
    piezas = 2.5
    Range("A1").Value = piezas
End Sub

Sub P04_08_Precedencia()
    ' 1. Parentesis  2. ^  3. * /  4. \  5. Mod  6. + -
    Dim sinParentesis As Double
    Dim conParentesis As Double

    sinParentesis = 5 + 3 * 2
    conParentesis = (5 + 3) * 2

    Range("A1").Value = sinParentesis
    Range("A2").Value = conParentesis
End Sub

Sub P04_13_TasaLegible()
    Dim tasaMensual As Double
    tasaMensual = ((1 + 0.12) ^ (1 / 12)) - 1

    Range("B1").Value = tasaMensual
    Range("B1").NumberFormat = "0.00%"

    Range("B2").Value = Format(tasaMensual, "0.00%")
    Range("B3").Value = Round(tasaMensual, 6)
End Sub

Sub P04_16_DefinirNombres()
    ThisWorkbook.Names.Add _
        Name:="MontoPrestamoV2", RefersTo:="=Hoja1V2!$B$1"
    ThisWorkbook.Names.Add _
        Name:="TasaAnualV2", RefersTo:="=Hoja1V2!$B$2"

    Range("MontoPrestamoV2").Value = 500000
    Range("TasaAnualV2").Value = 0.12
End Sub

Sub P04_19_Cuentas()
    Range("A1").Value = -3 ^ 2
    Range("A2").Value = 7.5 \ 2
End Sub

Sub P06_06_FormatearVentas()
'
' P06_06_FormatearVentas Macro
'
    Range("C2:C13").Select
    Selection.NumberFormat = "$#,##0.00"
    Range("A1").Select
End Sub

Sub P06_12_FormatearVentas()
    Dim ultimaFila As Long
    Dim datos As Range

    ultimaFila = Cells(Rows.Count, 1).End(xlUp).Row
    Set datos = Range(Cells(2, 3), Cells(ultimaFila, 3))

    datos.NumberFormat = "$#,##0.00"
End Sub

Sub P06_16_AlternarColumnaAuxiliar()
    Dim col As Range
    Set col = Columns("D:D")

    If col.EntireColumn.Hidden Then
        col.EntireColumn.Hidden = False
    Else
        col.EntireColumn.Hidden = True
    End If
End Sub

Sub P07_07_BuscarPagoMensualV2()
    Range("SaldoFinalV2").GoalSeek _
        Goal:=0, _
        ChangingCell:=Range("PagoMensualV2")
End Sub

Sub P08_07_Comparar()
    Dim a As Integer
    Dim b As Integer
    Dim sonIguales As Boolean

    a = 5
    b = 5
    sonIguales = a = b

    LastMessage = "a es igual a b? " & sonIguales
End Sub

Sub P08_11_Clasificar()
    Dim calificacion As Double
    calificacion = 7.5

    If calificacion >= 9 Then
        LastMessage = "A"
    ElseIf calificacion >= 8 Then
        LastMessage = "B"
    ElseIf calificacion >= 7 Then
        LastMessage = "C"
    Else
        LastMessage = "Reprobado"
    End If
End Sub

Sub P09_06_Contar()
    Dim i As Integer
    Dim mensaje As String

    mensaje = "Los numeros del 1 al 5 son: "
    For i = 1 To 5
        mensaje = mensaje & i & " "
    Next i

    LastMessage = mensaje
End Sub

Sub P09_08_NumerarPeriodos()
    Dim periodo As Long

    Range("B3").Select
    For periodo = 1 To 120
        ActiveCell.Offset(0, periodo - 1).Value = periodo
    Next periodo
End Sub

Sub P09_11_MarcarVacias()
    Dim celda As Range

    For Each celda In Range("A1:C500")
        If IsEmpty(celda.Value) Then
            celda.Interior.Color = RGB(255, 235, 156)
        End If
    Next celda
End Sub

Sub P09_14_MarcarMorosos()
    Dim ultima As Long
    Dim fila As Long

    ultima = Cells(Rows.Count, 1).End(xlUp).Row

    For fila = 2 To ultima
        If Cells(fila, 3).Value > 30 Then
            Cells(fila, 4).Value = "Vencido"
        End If
    Next fila
End Sub

Sub P10_15_AplicarIVA(monto As Double)
    monto = monto * 1.16
End Sub

Sub P10_15_Facturar()
    Dim subtotal As Double
    subtotal = 1000

    P10_15_AplicarIVA subtotal
    Range("A1").Value = subtotal
End Sub

Sub P10_18_Duplicar(n As Long)
    n = n * 2
End Sub

Sub P10_18_Probar()
    Dim x As Long
    x = 7
    P10_18_Duplicar x
    Range("A1").Value = x
End Sub

Sub P13_09_LimpiarNombres()
    Dim celda As Range

    For Each celda In Range("A2:A200")
        celda.Value = WorksheetFunction.Trim( _
            Replace(celda.Value, Chr(160), " "))
        celda.Value = WorksheetFunction.Proper(celda.Value)
    Next celda
End Sub

Sub P13_16_OrdenarBase()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("DatosV2")

    ws.Range("A1:C200").Sort _
        Key1:=ws.Range("B1"), Order1:=xlAscending, _
        Key2:=ws.Range("C1"), Order2:=xlDescending, _
        Header:=xlYes
End Sub

Sub P14_08_SumarSoloVisible()
    Dim ws As Worksheet, c As Range, total As Double
    Set ws = ThisWorkbook.Sheets("DatosV2")

    ws.Range("A1:B5").AutoFilter 1, "Ventas"

    For Each c In ws.Range("B2:B5") _
            .SpecialCells(xlCellTypeVisible)
        total = total + c.Value
    Next c
    LastMessage = total
End Sub

Sub P14_15_SubtotalesPorDepto()
    Dim ws As Worksheet, base As Range
    Set ws = ThisWorkbook.Sheets("DatosV2")
    Set base = ws.Range("A1").CurrentRegion

    base.RemoveSubtotal
    base.Sort Key1:=ws.Range("A1"), _
              Order1:=xlAscending, Header:=xlYes
    base.Subtotal GroupBy:=1, Function:=xlSum, _
                  TotalList:=Array(2)
End Sub

Sub P14_17_CrearTabla()
    Dim ws As Worksheet, tbl As ListObject
    Set ws = ThisWorkbook.Sheets("DatosV2")

    Set tbl = ws.ListObjects.Add( _
        xlSrcRange, ws.Range("A1").CurrentRegion, , xlYes)
    tbl.Name = "Ventas2026"
End Sub

Sub P15_09_BuscarSeguro()
    Dim i As Long, v As Variant

    For i = 2 To 500
        v = Application.VLookup(Cells(i, 1).Value, _
                Range("Catalogo"), 2, False)

        If IsError(v) Then
            Cells(i, 2).Value = "sin catalogo"
        Else
            Cells(i, 2).Value = v
        End If
    Next i
End Sub

Sub P15_19_GraficaPorDepto()
    Dim ws As Worksheet, ch As ChartObject
    Set ws = ThisWorkbook.Sheets("DatosV2")

    Set ch = ws.ChartObjects.Add(200, 20, 300, 200)
    ch.Chart.SetSourceData ws.Range("A1:B3")
    ch.Chart.ChartType = xlColumnClustered
    ch.Chart.HasTitle = True
    ch.Chart.ChartTitle.Text = "Monto por depto"
End Sub

Sub P16_06_CorteMensual()
    Dim pc As PivotCache, pt As PivotTable
    Dim ws As Worksheet, wd As Worksheet
    Set ws = ThisWorkbook.Sheets("DatosV2")
    Set wd = ThisWorkbook.Sheets("ResumenV2")

    Set pc = ThisWorkbook.PivotCaches.Create( _
        xlDatabase, ws.Range("A1").CurrentRegion)
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte")

    pt.PivotFields("Depto").Orientation = xlRowField
    pt.PivotFields("Monto").Orientation = xlDataField
End Sub

Function V2_TasaMensual(anual As Double) As Double
    V2_TasaMensual = ((1 + anual) ^ (1 / 12)) - 1
End Function

Function V2_Summation(n1 As Double, n2 As Double) As Double
    V2_Summation = n1 + n2
End Function
