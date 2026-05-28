' In this macro, we will learn how to create tables in Excel using VBA.

' Tables in Excel are a powerful feature that allow you to organize and analyze data more efficiently.
' They provide a structured format for your data, making it easier to sort, filter, and analyze information.

' To create a table in Excel using VBA, you can use the ListObjects.Add method.
' This method allows you to define the range of cells that you want to 
' convert into a table, as well as specify the table name and other properties.

' Let's look at an example that demonstrates how to create a table in Excel using VBA.

Sub CreateTable()
    ' Define the range of cells that you want to convert into a table.
    Dim rng As Range
    ' In this example, we first define the range of cells that we want to convert into a table using the Set statement.
    Set rng = ThisWorkbook.Sheets("Sheet1").Range("A1:C5")
    
    ' Add a new table to the worksheet using the ListObjects.Add method.
    ' The Add method takes several arguments:
    ' - SourceType: Specifies the type of data source for the table. In this case, we are using xlSrcRange to indicate that the data source is a range of cells.
    ' - Source: Specifies the range of cells that you want to convert into a table.
    ' - XlListObjectHasHeaders: Specifies whether the table has headers. In this case, we are setting it to xlYes to indicate that the first row contains headers.
    ' - TableStyleName: Specifies the style of the table. In this case, we are using the "TableStyleMedium9" style.
        ' Ask the user to input the name of the table.
    Dim tableName As String
    tableName = InputBox("Enter the name of the table:")
    If tableName = "" Then Exit Sub ' Handle empty input or cancelled input box

    Dim tbl As ListObject
    Set tbl = ThisWorkbook.Sheets("Sheet1").ListObjects.Add(xlSrcRange, rng, , xlYes, , "TableStyleMedium9")

    ' Set the name of the table.
    tbl.Name = tableName
    
    ' Display a message box to indicate that the table has been created.
    MsgBox "Table created successfully."
End Sub

' Now let's create a macro that adds a new row to the table.

Sub AddRowToTable()
    ' Ask the user to input the name of the table.
    Dim tableName As String
    tableName = InputBox("Enter the name of the table:")
    If tableName = "" Then Exit Sub ' Handle empty input or cancelled input box

    ' Assume we are working in Sheet1; adjust as necessary.
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Variable to track whether the table has been found.
    Dim found As Boolean
    found = False

    ' Loop through all tables in the worksheet to find the table by name.
    Dim tbl As ListObject
    For Each tbl In ws.ListObjects
        If tbl.Name = tableName Then
            found = True
            Exit For
        End If
    Next tbl
    
    ' If the table was not found, inform the user.
    If Not found Then
        MsgBox "Table '" & tableNameToFind & "' not found."
        Exit Sub
    End If

    Set tbl = ThisWorkbook.Sheets("Sheet1").ListObjects(tableName)
    
    ' Add a new row to the table using the ListRows.Add method.
    Dim newRow As ListRow
    Set newRow = tbl.ListRows.Add
    
    ' Display a message box to indicate that the row has been added.
    MsgBox "Row added to the table."
End Sub

' Now let's create a macro that deletes a row from the table using the index of the row.
' In VBA indexing starts from 1.

Sub DeleteRowFromTable()
    ' Ask the user to input the name of the table.
    Dim tableName As String
    tableName = InputBox("Enter the name of the table:")
    If tableName = "" Then Exit Sub ' Handle empty input or cancelled input box

    ' Assume we are working in Sheet1; adjust as necessary.
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Variable to track whether the table has been found.
    Dim found As Boolean
    found = False

    ' Loop through all tables in the worksheet to find the table by name.
    Dim tbl As ListObject
    For Each tbl In ws.ListObjects
        If tbl.Name = tableName Then
            found = True
            Exit For
        End If
    Next tbl
    
    ' If the table was not found, inform the user.
    If Not found Then
        MsgBox "Table '" & tableNameToFind & "' not found."
        Exit Sub
    End If

    Set tbl = ThisWorkbook.Sheets("Sheet1").ListObjects(tableName)
    
    ' Ask the user to input the index of the row to delete.
    Dim rowIndex As Integer
    rowIndex = Val(InputBox("Enter the index of the row to delete:"))
    If rowIndex < 1 Or rowIndex > tbl.ListRows.Count Then
        MsgBox "Invalid row index. Please enter a valid row index."
        Exit Sub
    End If
    
    ' Delete the row from the table using the ListRows property.
    tbl.ListRows(rowIndex).Delete
    
    ' Display a message box to indicate that the row has been deleted.
    MsgBox "Row deleted from the table."
End Sub


' Now let's create a macro that adds a new column to the table to the right of the last column
' or to the right of a specific column depending on the index or the name of the column.

Sub AddColumnToTable()
    ' Ask the user to input the name of the table.
    Dim tableName As String
    tableName = InputBox("Enter the name of the table:")
    If tableName = "" Then Exit Sub ' Handle empty input or cancelled input box

    ' Assume we are working in Sheet1; adjust as necessary.
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Variable to track whether the table has been found.
    Dim found As Boolean
    found = False

    ' Loop through all tables in the worksheet to find the table by name.
    Dim tbl As ListObject
    For Each tbl In ws.ListObjects
        If tbl.Name = tableName Then
            found = True
            Exit For
        End If
    Next tbl
    
    ' If the table was not found, inform the user.
    If Not found Then
        MsgBox "Table '" & tableNameToFind & "' not found."
        Exit Sub
    End If

    Set tbl = ThisWorkbook.Sheets("Sheet1").ListObjects(tableName)

    ' Ask the user to choose where to add the column.
    Dim choice As String
    choice = InputBox("Do you want to add the column to the right of the last column or to the right of a specific column? Enter 'last' or 'specific'.")

    Dim columnName As String
    Dim newColumn As ListColumn

    If choice = "last" Then
        ' Get the name for the new column.
        columnName = InputBox("Enter the name of the new column:")
        If columnName = "" Then Exit Sub ' Handle empty input

        ' Add a new column to the right of the last column.
        Set newColumn = tbl.ListColumns.Add
        newColumn.Name = columnName

        MsgBox "Column added to the table."
    ElseIf choice = "specific" Then
        ' Determine how to specify the column.
        Dim specChoice As String
        specChoice = InputBox("Do you want to add the column to the right of a column by 'index' or by 'name'? Enter 'index' or 'name'.")

        If specChoice = "index" Then
            Dim columnIndex As Integer
            columnIndex = Val(InputBox("Enter the index of the column to add the new column to the right of:"))
            If columnIndex < 1 Or columnIndex > tbl.ListColumns.Count Then
                MsgBox "Invalid index."
                Exit Sub
            End If
            Set newColumn = tbl.ListColumns.Add(columnIndex + 1)
        ElseIf specChoice = "name" Then
            Dim columnNameToFind As String
            columnNameToFind = InputBox("Enter the name of the column to add the new column to the right of:")
            Dim found As Boolean
            For Each col In tbl.ListColumns
                If col.Name = columnNameToFind Then
                    Set newColumn = tbl.ListColumns.Add(col.Index + 1)
                    found = True
                    Exit For
                End If
            Next
            If Not found Then
                MsgBox "Column name not found."
                Exit Sub
            End If
        Else
            MsgBox "Invalid choice. Please enter 'index' or 'name'."
            Exit Sub
        End If

        ' Get the name for the new column.
        columnName = InputBox("Enter the name of the new column:")
        If columnName = "" Then Exit Sub ' Handle empty input

        ' Set the name of the new column.
        newColumn.Name = columnName

        MsgBox "Column added to the table."
    Else
        MsgBox "Invalid choice. Please enter 'last' or 'specific'."
    End If
End Sub


' Now let's do a macro that deletes a column from the table using the index or the name of the column.

Sub DeleteColumnFromTable()
    ' Ask the user to input the name of the table.
    Dim tableName As String
    tableName = InputBox("Enter the name of the table:")
    If tableName = "" Then Exit Sub ' Handle empty input or cancelled input box

    ' Assume we are working in Sheet1; adjust as necessary.
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Variable to track whether the table has been found.
    Dim found As Boolean
    found = False

    ' Loop through all tables in the worksheet to find the table by name.
    Dim tbl As ListObject
    For Each tbl In ws.ListObjects
        If tbl.Name = tableName Then
            found = True
            Exit For
        End If
    Next tbl
    
    ' If the table was not found, inform the user.
    If Not found Then
        MsgBox "Table '" & tableNameToFind & "' not found."
        Exit Sub
    End If

    Set tbl = ThisWorkbook.Sheets("Sheet1").ListObjects(tableName)

    ' Ask the user to choose the method to delete the column.
    Dim choice As String
    choice = InputBox("Do you want to delete the column by index or by name? Enter 'index' or 'name'.")

    If choice = "index" Then
        ' Get the index for the column to be deleted.
        Dim columnIndex As Integer
        columnIndex = Val(InputBox("Enter the index of the column to delete:"))
        If columnIndex < 1 Or columnIndex > tbl.ListColumns.Count Then
            MsgBox "Invalid index. Please enter a valid column index."
            Exit Sub
        End If

        ' Delete the column from the table.
        tbl.ListColumns(columnIndex).Delete
        MsgBox "Column deleted from the table."
    ElseIf choice = "name" Then
        ' Get the name of the column to be deleted.
        Dim columnName As String
        columnName = InputBox("Enter the name of the column to delete:")
        If columnName = "" Then Exit Sub ' Handle empty input

        ' Attempt to find and delete the column by name.
        Dim found As Boolean
        For Each col In tbl.ListColumns
            If col.Name = columnName Then
                col.Delete
                found = True
                Exit For
            End If
        Next

        If Not found Then
            MsgBox "Column name not found. Please check the name and try again."
            Exit Sub
        End If

        MsgBox "Column deleted from the table."
    Else
        MsgBox "Invalid choice. Please enter 'index' or 'name'."
    End If
End Sub
