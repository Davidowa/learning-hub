' In this macros we will see how to use Excel functions in VBA
' Excel functions can be used in VBA code to perform calculations, manipulate data, and automate tasks.
' They are useful as these are built-in functionalities that can be leveraged within VBA to enhance the capabilities of your macros.

' To use Excel functions in VBA, you can call them directly within your code using the Application.WorksheetFunction object.
' This object provides access to a wide range of Excel functions that can be used in VBA.

' Let's look at an example that demonstrates how to use the SUM function in VBA to calculate the sum of a range of cells.

Sub CalculateSum()
    ' Define the range of cells that you want to calculate the sum of.
    Dim rng As Range
    ' In this example, we first define the range of cells that we want to calculate the sum of using the Set statement.
    Set rng = ThisWorkbook.Sheets("Sheet1").Range("A1:A5")
    
    ' Declare a variable to store the result of the sum calculation.
    Dim sumResult As Double

    ' The Application.WorksheetFunction object allows us to call Excel functions in VBA.
    ' The Sum function calculates the sum of a range of cells.
    ' We pass the range 'rng' as an argument to the Sum function to calculate the sum of the specified range.
    ' The result is stored in the 'sumResult' variable.
    sumResult = Application.WorksheetFunction.Sum(rng)
    
    ' Display the result in a message box.
    MsgBox "The sum of the range is: " & sumResult
End Sub

