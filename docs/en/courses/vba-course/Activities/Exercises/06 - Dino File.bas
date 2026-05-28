Sub SearchDinoName()
    ' Get the dino name to search
    Dim dinoName As String
    dinoName = Range("B2").Value

    ' Search for the dino name in the Database worksheet
    Dim wsDatabase As Worksheet

    ' Set references to the worksheets
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    ' Create the variables to store the dino information
    Dim meaningName As String
    Dim pronunciationName As String
    Dim period As String
    Dim diet As String
    Dim length As String
    Dim weight As String
    Dim mass As String
    Dim noWalkingLegs As String
    Dim hipType As String
    Dim group As String

    ' Find the dino information using the VLOOKUP function
    ' The VLOOKUP function takes four arguments:
    ' The value to search for (dinoName)
    ' The range of cells to search in (the database range)
    ' The column index number of the value to return (2 for the meaning)
    ' Whether to find an exact match or an approximate match (FALSE for exact match)

    ' Get the last row in the database
    Dim lastRow As Long
    lastRow = wsDatabase.Cells(wsDatabase.Rows.Count, "A").End(xlUp).Row

    ' Get the last column in the database
    Dim lastColumn As Long
    lastColumn = wsDatabase.Cells(1, wsDatabase.Columns.Count).End(xlToLeft).Column

    ' Start searching using VLOOKUP and the last row and column
    meaningName = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 2, False)
    pronunciationName = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 3, False)
    period = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 4, False)
    diet = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 5, False)
    length = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 6, False)
    weight = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 7, False)
    mass = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 8, False)
    noWalkingLegs = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 9, False)
    hipType = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 10, False)
    group = Application.WorksheetFunction.VLookup(dinoName, wsDatabase.Range(wsDatabase.Cells(2, 1), wsDatabase.Cells(lastRow, lastColumn)), 11, False)

    ' Display the dino information in the form
    Range("B3").Value = meaningName
    Range("B4").Value = pronunciationName
    Range("B5").Value = period
    Range("B6").Value = diet
    Range("B7").Value = length
    Range("B8").Value = weight
    Range("B9").Value = mass
    Range("B10").Value = noWalkingLegs
    Range("B11").Value = hipType
    Range("B12").Value = group
End Sub
Sub MarbledPattern()
    ' Create a marbled pattern in the Database worksheet
    Dim wsDatabase As Worksheet
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    ' Get the last row in the database
    Dim lastRow As Long
    lastRow = wsDatabase.Cells(wsDatabase.Rows.Count, "A").End(xlUp).Row

    ' Get the last column in the database
    Dim lastColumn As Long
    lastColumn = wsDatabase.Cells(1, wsDatabase.Columns.Count).End(xlToLeft).Column

    ' Start from the second row
    Dim row As Long
    Dim column As Long
    For row = 2 To lastRow
        For column = 1 To lastColumn
            ' If the row number is even, color the cells with a light blue 
            If row Mod 2 = 0 Then
                wsDatabase.Cells(row, column).Interior.Color = RGB(173, 216, 230)
            End If
        Next column
    Next row
End Sub