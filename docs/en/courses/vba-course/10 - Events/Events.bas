' An event in VBA Excel is a procedure that automatically executes when a specific action occurs.
' For instance, changing the selection of cells in a worksheet can trigger an event. 
' Events are useful for automating tasks, validating data, or interacting with users through the interface.

' This example demonstrates an event handler that displays a message box whenever a user selects a cell in a worksheet.
' Event handlers like this one can enhance user interaction by providing immediate feedback or guiding their actions within a spreadsheet.

' To implement this event handler, the following code needs to be added to the code window of the worksheet you wish to monitor.
' You can access this by right-clicking the worksheet's tab at the bottom of Excel and selecting "View Code".

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
    ' The 'ByVal' keyword passes an argument by value.
    ' This method copies the actual value of an argument into the procedure's parameter.
    ' Here, 'Target' is passed by value, meaning we work with a copy of the range reference.
    ' Changes to 'Target' inside this subroutine will not affect the original range on the worksheet.

    ' 'Target' is a Range object that represents the cell or range of cells that has just been selected by the user.

    ' The MsgBox function displays a message box with a specified message.
    ' Here, we concatenate the text "You selected cell " with the address of 'Target'.
    ' Target.Address provides the address of the selected range in A1 notation.
    
    MsgBox "You selected cell " & Target.Address
End Sub

' Now let's create another event handler that triggers when you input a value into a cell.
' This event will call a subroutine that checks if the input value is a number and writes 
' in the cell to the right of the input cell whether the input is a number or not.

Private Sub Worksheet_Change(ByVal Target As Range)
    ' The 'Worksheet_Change' event is triggered whenever a cell or range of cells on the worksheet is changed.
    ' The 'Target' parameter represents the range that has been changed.

    ' We will call a subroutine named 'CheckIfNumber' to check if the input value is a number.
    ' This subroutine will take the 'Target' range as an argument.
    ' If the input value is a number, it will write "Number" in the cell to the right of the input cell.
    ' If the input value is not a number, it will write "Not a Number" in the cell to the right of the input cell.

    ' If the 'Target' addres is A1, we will perform the check.
    ' You can modify this condition to target specific cells or ranges based on your requirements.
    If Target.Address = "$A$1" Then
        CheckIfNumber Target
    End If
End Sub

Sub CheckIfNumber(Target As Range)
    ' This subroutine checks if the input value in the 'Target' range is a number.
    ' If the input value is a number, it writes "Number" in the cell to the right of the input cell.
    ' If the input value is not a number, it writes "Not a Number" in the cell to the right of the input cell.

    ' We use the IsNumeric function to check if the value in the 'Target' range is a number.
    ' IsNumeric returns True if the expression is a number, and False otherwise.

    If IsNumeric(Target.Value) Then
        ' If the input value is a number, we write "Number" in the cell to the right of the input cell.
        Target.Offset(0, 1).Value = "Number"
    Else
        ' If the input value is not a number, we write "Not a Number" in the cell to the right of the input cell.
        Target.Offset(0, 1).Value = "Not a Number"
    End If
End Sub



