from pathlib import Path
import json,re
B=Path('ppts/audit/evidencia-vba-runtime-2026-10-13')
S=json.loads(Path('/tmp/vba-sources.json').read_text()); sources={(int(Path(x['file']).name[1:3]),x['slide']):x['source'] for x in S}
# The original procedure bodies are retained. Renaming isolates repeated teaching names.
selected=[(1,18),(2,21),(3,10),(3,16),(3,19),(4,8),(4,13),(4,16),(4,19),(6,6),(6,12),(6,16),(7,7),(8,7),(8,11),(9,6),(9,8),(9,11),(9,14),(10,15),(10,18),(13,9),(13,16),(14,8),(14,15),(14,17),(15,9),(15,19),(16,6)]
procedures=[]
for week,slide in selected:
 code=sources[week,slide]
 # Message dialogs are logged rather than displayed in the automatic pass.
 code=re.sub(r'(?m)^([ \t]*)MsgBox (.+)$',r'\1LastMessage = \2',code)
 names=re.findall(r'(?im)^Sub\s+(\w+)',code)
 for old in names: code=re.sub(r'\b'+old+r'\b',f'P{week:02}_{slide:02}_{old}',code)
 procedures.append(code)
for week,slide in [(10,11)]:procedures.append(sources[week,slide])
cls=sources[12,9]
(B/'Empleado.cls').write_text('VERSION 1.0 CLASS\nBEGIN\n  MultiUse = -1\nEND\nAttribute VB_Name = "Empleado"\nAttribute VB_GlobalNameSpace = False\nAttribute VB_Creatable = False\nAttribute VB_PredeclaredId = False\nAttribute VB_Exposed = False\n'+cls)
head='''Attribute VB_Name = "RuntimeSuite"
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

Private Function Fresh(Optional n As String = "Hoja1") As Worksheet
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

Public Sub RunAutoTests()
    Dim ws As Worksheet
    oldEvents = Application.EnableEvents
    oldScreen = Application.ScreenUpdating
    oldCalc = Application.Calculation
    oldAlerts = Application.DisplayAlerts
    On Error GoTo Fatal
    Application.EnableEvents = False
    Application.DisplayAlerts = False
    Set Report = Sheet("VBAResults")
    Report.Cells.Clear
    Report.Range("A1:E1").Value = Array("Test", "Week", "Status", "Actual", "Expected")
    rr = 2
    Report.Range("G1").Value = "Excel VBA native runtime"
    Report.Range("G2").Value = Application.Version
    Report.Range("G3").Value = Application.OperatingSystem
    Report.Range("G4").Value = Now
    Case01: Case02: Case03: Case04: Case05: Case06
    Case07: Case08: Case09: Case10: Case12: Case13
    Case14Filter: Case14Advanced: Case14Subtotal: Case14Table
    Case15Functions: Case15Lookup: Case15Formula: Case15Chart
    Case16Pivot: Case16Errors: Case16Protection: Case17
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
'''
cases=[]
def case(name,w,body):
 cases.append(f'Private Sub {name}()\n    On Error GoTo Failed\n    Dim ws As Worksheet, i As Long, n As Long, v As Variant, x As Double\n'+body+'\n    Exit Sub\nFailed:\n    Unexpected "'+name+'", '+str(w)+', Err.Number, Err.Description\nEnd Sub\n')
case('Case01',1,'''
    Set ws = Fresh()
    P01_18_HideColumn
    Check "hide_column_final", 1, ws.Columns("D:D").Hidden, False''')
case('Case02',2,'''
    Set ws = Fresh()
    P02_21_Ejemplo
    Check "range_assignment_1", 2, ws.Range("A1").Value, 10
    Check "range_assignment_2", 2, ws.Range("A2").Value, 20''')
case('Case03',3,'''
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
    Check "date_isnumeric", 3, IsNumeric(DateSerial(2026, 10, 13)), False''')
case('Case04',4,'''
    Set ws = Fresh()
    P04_08_Precedencia
    Check "precedence", 4, ws.Range("A1").Value, 11
    Check "parentheses", 4, ws.Range("A2").Value, 16
    P04_13_TasaLegible
    Check "monthly_rate", 4, ws.Range("B1").Value, 0.00948879293458305
    Check "monthly_format", 4, ws.Range("B2").Value, "0.95%"
    Check "monthly_round", 4, ws.Range("B3").Value, 0.009489
    P04_16_DefinirNombres
    Check "named_range_amount", 4, ws.Range("MontoPrestamo").Value, 500000
    Check "named_range_rate", 4, ws.Range("TasaAnual").Value, 0.12
    P04_19_Cuentas
    Check "negative_power", 4, ws.Range("A1").Value, -9
    Check "integer_division", 4, ws.Range("A2").Value, 4''')
case('Case05',5,'''
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
    Check "percent_input_005", 5, CDbl("0.05"), 0.05''')
case('Case06',6,'''
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
    Check "toggle_off", 6, ws.Columns("D:D").Hidden, False''')
case('Case07',7,'''
    Set ws = Fresh()
    ws.Range("B1").Value = 500000
    ws.Range("B2").Value = TasaMensual(0.12)
    ws.Range("B3").Value = 120: ws.Range("B4").Value = 1000
    ws.Range("B5").Formula = "=B1*(1+B2)^B3-B4*((1+B2)^B3-1)/B2"
    ThisWorkbook.Names.Add "SaldoFinal", "=Hoja1!$B$5"
    ThisWorkbook.Names.Add "PagoMensual", "=Hoja1!$B$4"
    ws.Calculate
    Check "balance_before_goal_seek", 7, ws.Range("B5").Value, 1330994.06, 0.01
    P07_07_BuscarPagoMensual
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
    Application.Calculation = oldCalc''')
case('Case08',8,'''
    Set ws = Fresh()
    P08_07_Comparar
    Check "comparison_message", 8, LastMessage, "\u00bfa es igual a b? True"
    P08_11_Clasificar
    Check "elseif_classification", 8, LastMessage, "C"
    If ws.Range("A1").Value = 0 Then ws.Range("B1").Value = "Sin venta" Else ws.Range("B1").Value = "Con venta"
    Check "empty_cell_compares_to_zero", 8, ws.Range("B1").Value, "Sin venta"''')
case('Case09',9,'''
    Set ws = Fresh()
    P09_06_Contar
    Check "loop_message", 9, LastMessage, "Los n\u00fameros del 1 al 5 son: 1 2 3 4 5 "
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
    Check "forward_delete_skips_rows", 9, WorksheetFunction.CountA(ws.Columns(1)), 3''')
case('Case10',10,'''
    Set ws = Fresh()
    Check "summation_function", 10, Summation(5, 3), 8
    Check "rate_function", 10, TasaMensual(0.12), 0.00948879293458305
    P10_15_Facturar
    Check "byref_iva", 10, ws.Range("A1").Value, 1160
    P10_18_Probar
    Check "byref_double", 10, ws.Range("A1").Value, 14
    ws.Range("A1").Value = 0.12
    ws.Range("B1").Formula = "=TasaMensual(A1)"
    ws.Calculate
    Check "udf_in_worksheet", 10, ws.Range("B1").Value, 0.00948879293458305''')
case('Case12',12,'''
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
    Check "class_alias", 12, a.Anual, 240000''')
case('Case13',13,'''
    Dim s As String
    Set ws = Fresh()
    Check "vba_trim_preserves_middle", 13, Trim("Ana    Lopez"), "Ana    Lopez"
    Check "excel_trim_collapses_middle", 13, WorksheetFunction.Trim("Ana    Lopez"), "Ana Lopez"
    s = "Ana" & Chr(160)
    Check "trim_keeps_chr160", 13, Len(Trim(s)), 4
    Check "replace_chr160", 13, Trim(Replace(s, Chr(160), " ")), "Ana"
    Check "chr160_is_nbsp_on_mac", 13, AscW(Chr(160)), 160
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
    Set ws = Fresh("Datos")
    ws.Range("A1:C1").Value = Array("Nombre", "Depto", "Sueldo")
    ws.Range("A2:C2").Value = Array("Ana", "Ventas", 15000)
    ws.Range("A3:C3").Value = Array("Beto", "Compras", 22000)
    ws.Range("A4:C4").Value = Array("Carla", "Ventas", 18000)
    P13_16_OrdenarBase
    Check "sort_department", 13, ws.Range("A2").Value, "Beto"
    Check "sort_secondary_desc", 13, ws.Range("A3").Value, "Carla"''')
case('Case14Filter',14,'''
    Set ws = Fresh("Datos")
    SeedSales ws
    P14_08_SumarSoloVisible
    Check "visible_filter_total", 14, LastMessage, "400"
    Check "filtered_sum_all", 14, WorksheetFunction.Sum(ws.Range("B2:B5")), 1000
    Check "filtered_subtotal", 14, WorksheetFunction.Subtotal(9, ws.Range("B2:B5")), 400''')
case('Case14Advanced',14,'''
    Set ws = Fresh("Datos"): SeedSales ws
    ws.Range("D1").Value = "Depto": ws.Range("D2").Value = "Ventas"
    ws.Range("A1:B5").AdvancedFilter xlFilterInPlace, ws.Range("D1:D2")
    Check "advanced_matching_header", 14, ws.Range("A2:A5").SpecialCells(xlCellTypeVisible).Count, 2
    ws.ShowAllData
    ws.Range("D1").Value = "Departamento"
    ws.Range("A1:B5").AdvancedFilter xlFilterInPlace, ws.Range("D1:D2")
    Check "advanced_wrong_header", 14, ws.Range("A2:A5").SpecialCells(xlCellTypeVisible).Count, 0''')
case('Case14Subtotal',14,'''
    Set ws = Fresh("Datos"): SeedSales ws
    ws.Range("A1:B5").Subtotal GroupBy:=1, Function:=xlSum, TotalList:=Array(2)
    Check "subtotal_unsorted_rows", 14, ws.Range("A1").CurrentRegion.Rows.Count, 10
    Set ws = Fresh("Datos"): SeedSales ws
    P14_15_SubtotalesPorDepto
    Check "subtotal_sorted_rows", 14, ws.Range("A1").CurrentRegion.Rows.Count, 8''')
case('Case14Table',14,'''
    Dim tbl As ListObject
    Set ws = Fresh("Datos")
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
    Set ws = Fresh("Datos")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    Set tbl = ws.ListObjects.Add(xlSrcRange, ws.Range("A1:B1"), , xlYes)
    Check "empty_table_rows", 14, tbl.ListRows.Count, 0
    Check "empty_table_body", 14, tbl.DataBodyRange Is Nothing, True
    On Error Resume Next
    Err.Clear
    i = tbl.DataBodyRange.Rows.Count
    n = Err.Number
    On Error GoTo Failed
    Check "empty_table_body_error", 14, n, 91''')
case('Case15Functions',15,'''
    Check "vba_left", 15, Left("Hola mundo", 4), "Hola"
    Check "worksheet_trim", 15, WorksheetFunction.Trim("a    b"), "a b"''')
case('Case15Lookup',15,'''
    Set ws = Fresh()
    ws.Range("D1:E3").Value = Array(Array("Ana", 100), Array("Beto", 200), Array("Carla", 300))
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
    Check "application_lookup_found", 15, Application.VLookup("Ana", ws.Range("D1:E3"), 2, False), 100''')
case('Case15Formula',15,'''
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
    Check "r1c1_value", 15, ws.Range("C4").Value, 40''')
case('Case15Chart',15,'''
    Set ws = Fresh("Datos")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    ws.Range("A2:B2").Value = Array("Ventas", 100)
    ws.Range("A3:B3").Value = Array("Compras", 200)
    P15_19_GraficaPorDepto
    Check "chart_count", 15, ws.ChartObjects.Count, 1
    Check "chart_series_count", 15, ws.ChartObjects(1).Chart.SeriesCollection.Count, 1
    Check "chart_title", 15, ws.ChartObjects(1).Chart.ChartTitle.Text, "Monto por depto"''')
case('Case16Pivot',16,'''
    Dim pt As PivotTable
    Set ws = Fresh("Datos"): SeedSales ws
    Set ws = Fresh("Resumen")
    P16_06_CorteMensual
    Set pt = ThisWorkbook.Sheets("Resumen").PivotTables("Corte")
    Set ws = ThisWorkbook.Sheets("Datos")
    Check "pivot_initial", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1000
    ws.Range("B2").Value = 999
    Check "pivot_before_refresh", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1000
    pt.RefreshTable
    Check "pivot_after_refresh", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1899
    ws.Range("A6").Value = "Ventas": ws.Range("B6").Value = 1000
    pt.RefreshTable
    Check "pivot_fixed_cache_excludes_new_row", 16, pt.GetPivotData(pt.DataFields(1).Name).Value, 1899''')
case('Case16Errors',16,'''
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
    Check "err_persists_after_valid_addition", 16, n, 11''')
case('Case16Protection',16,'''
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
    ws.Unprotect "abc"''')
case('Case17',17,'''
    Dim pt As PivotTable, pc As PivotCache, ch As ChartObject, wd As Worksheet
    Set ws = Fresh("Datos17")
    ws.Range("A1:B1").Value = Array("Depto", "Monto")
    For i = 2 To 100: ws.Cells(i, 1).Value = "Ventas": ws.Cells(i, 2).Value = 1: Next i
    Set wd = Fresh("Resumen17")
    Set pc = ThisWorkbook.PivotCaches.Create(xlDatabase, ws.Range("A1:B100"))
    Set pt = pc.CreatePivotTable(wd.Range("A1"), "Corte17")
    pt.PivotFields("Depto").Orientation = xlRowField
    pt.PivotFields("Monto").Orientation = xlDataField
    Set ch = ws.ChartObjects.Add(200, 20, 300, 200)
    ch.Chart.SetSourceData ws.Range("A1:B100")
    For i = 101 To 120: ws.Cells(i, 1).Value = "Ventas": ws.Cells(i, 2).Value = 10: Next i
    pt.RefreshTable
    Check "final_fixed_pivot", 17, pt.GetPivotData(pt.DataFields(1).Name).Value, 99
    Check "final_fixed_chart", 17, UBound(ch.Chart.SeriesCollection(1).Values), 99''')
code=head+'\n'.join(cases)+'\n'+ '\n'.join(procedures)
# VBA exported modules on Mac import UTF-8 reliably only for ASCII. Replace
# test literal accents in both original messages and assertions, not the logic.
import unicodedata
code=code.replace('\u00bf','').replace('\u00a1','')
code=unicodedata.normalize('NFKD',code).encode('ascii','ignore').decode()
(B/'RuntimeSuite.bas').write_text(code)
(B/'suite-provenance.json').write_text(json.dumps({'source':'Lesson YAML Spanish canonical code; English/Mac core parity checked separately','selected_exact_procedure_bodies':selected,'automatic_instrumentation':['Procedure names prefixed to avoid duplicate declarations','MsgBox output captured in LastMessage for unattended assertions','Message accents normalized consistently for ASCII module import','Fixtures supply sheet names, rows, catalog and amortization formula; not original workbooks'],'not_in_auto_pass':['Interactive InputBox/MsgBox paths','Sheet event modules','Intentional compile errors','UserInterfaceOnly save/reopen']},indent=2)+'\n')
print(len(code),len(cases),'case groups',code.count('Check "'),'assertions')
