Sub AddDetails()
    ' Fill the form with details
    ' C4 is the cell for the name
    ' C5 is the cell for the birthdate
    ' C6 is the cell for the budget
    ' C7 is the cell for the car brand

    ' Declare variables to store the details
    Dim name As String
    Dim birthdate As Date
    Dim budget As String
    Dim carBrand As String

    ' Prompt the user to enter their name
    name = InputBox("What is your name?")

    ' Prompt the user to enter their birthdate
    birthdate = InputBox("What is your birthdate? (MM/DD/YYYY)")
    ' Set the number format for the cell to display the date correctly  
    Range("C5").NumberFormat = "MM/DD/YYYY"

    ' Prompt the user to enter their budget
    budget = InputBox("What is your budget?")
    ' Set the number format for the cell to display the budget correctly
    Range("C6").NumberFormat = "$#,##0.00"

    ' Prompt the user to enter their car brand
    carBrand = InputBox("What is your favorite car brand?")

    ' Fill the form with the details
    Range("C4").Value = name
    Range("C5").Value = birthdate
    Range("C6").Value = budget
    Range("C7").Value = carBrand
End Sub
Sub EditDetails()
    ' Edit the details in the form
    ' C4 is the cell for the name
    ' C5 is the cell for the birthdate
    ' C6 is the cell for the budget
    ' C7 is the cell for the car brand

    ' Declare variables to store the edited details
    Dim name As String
    Dim birthdate As Date
    Dim budget As String
    Dim carBrand As String

    ' Get the current details from the form
    name = Range("C4").Value
    birthdate = Range("C5").Value
    budget = Range("C6").Value
    carBrand = Range("C7").Value

    ' Prompt the user to edit their name
    name = InputBox("Edit your name: " & name)

    ' Prompt the user to edit their birthdate
    birthdate = InputBox("Edit your birthdate: " & birthdate & " (MM/DD/YYYY)")
    ' Set the number format for the cell to display the date correctly  
    Range("C5").NumberFormat = "MM/DD/YYYY"

    ' Prompt the user to edit their budget
    budget = InputBox("Edit your budget: " & budget)
    ' Set the number format for the cell to display the budget correctly
    Range("C6").NumberFormat = "$#,##0.00"

    ' Prompt the user to edit their car brand
    carBrand = InputBox("Edit your favorite car brand: " & carBrand)

    ' Fill the form with the edited details
    Range("C4").Value = name
    Range("C5").Value = birthdate
    Range("C6").Value = budget
    Range("C7").Value = carBrand
End Sub
Sub AddRecordToDatabase()
    Dim wsDatabase As Worksheet
    Dim lastRow As Long

    ' Set references to the worksheets
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    ' Find the last used row in the Database sheet, starting from column 'A' which is the first piece of data
    lastRow = wsDatabase.Cells(wsDatabase.Rows.Count, "A").End(xlUp).Row

    ' If the lastRow is just the header, we'll need to start on the next row
    If lastRow = 1 And IsEmpty(wsDatabase.Cells(lastRow, "A").Value) Then lastRow = 2

    ' Copy the data from the Car Application form to the next available row in the Database
    ' Assuming that your form data is contiguous from C4 to C7, you can copy it all at once
    Range("C4:C7").Copy

    ' Paste the data into the Database sheet starting at the next available row
    ' Transpose:=True will paste the data in a row instead of a column
    wsDatabase.Range("A" & lastRow + 1).PasteSpecial Paste:=xlPasteValues, Transpose:=True
    Application.CutCopyMode = False ' Clear the clipboard and cancel cut/copy mode

    ' Set the number format for the birthdate and budget columns
    wsDatabase.Range("B" & lastRow + 1).NumberFormat = "MM/DD/YYYY"
    wsDatabase.Range("D" & lastRow + 1).NumberFormat = "$#,##0.00"

    MsgBox "Record added to Database successfully!"
End Sub
Sub DeleteDuplicateRecords()
    Dim wsDatabase As Worksheet
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    Dim lastRow As Long
    lastRow = wsDatabase.Cells(wsDatabase.Rows.Count, "A").End(xlUp).Row

    ' We consider also A1 as it is the header row
    wsDatabase.Range("$A$1:$D$" & lastRow).RemoveDuplicates Columns:=Array(1, 2, 3, 4), Header:=xlYes

    MsgBox "Duplicates have been removed."
End Sub
Sub DeleteEmptyRows()
    Dim wsDatabase As Worksheet
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    Dim lastRow As Long
    lastRow = wsDatabase.Cells(wsDatabase.Rows.Count, "A").End(xlUp).Row

    wsDatabase.Range("$A$1:$D$" & lastRow).SpecialCells(xlCellTypeBlanks).EntireRow.Delete

    MsgBox "Empty rows have been removed."
End Sub
Sub DeleteEmptyColumns()
    Dim wsDatabase As Worksheet
    Set wsDatabase = ThisWorkbook.Sheets("Database")

    Dim lastColumn As Long
    lastColumn = wsDatabase.Cells(1, wsDatabase.Columns.Count).End(xlToLeft).Column

    ' Now we can loop through the columns from right to left
    Dim i As Long
    For i = lastColumn To 1 Step -1
        ' Check if the column is empty
        ' Application.WorksheetFunction.CountA returns the number of non-empty cells in a range
        ' If the column is empty, delete it
        If Application.WorksheetFunction.CountA(wsDatabase.Columns(i)) = 0 Then
            wsDatabase.Columns(i).Delete
        End If
    Next i
    MsgBox "Empty columns have been removed."
End Sub

