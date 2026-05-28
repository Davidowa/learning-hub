Sub CircleAreaInMessage()
    ' Let's start with a simple example to calculate the area of a circle and display the result in a message box.
    Const pi As Double = 3.14159   ' Declare 'pi' as a constant Double to store the value of pi (π).
    Dim radius As Double            ' Declare 'radius' as a Double to store the radius of the circle.
    Dim area As Double              ' Declare 'area' as a Double to store the calculated area of the circle.
    Dim resultMessage As String     ' Declare 'resultMessage' as a String to store and display the final message.
    
    ' Let's assign the value of 5 to 'radius'.
    ' Variables can be assigned values using the assignment operator (=).
    radius = 5  ' The value of 'radius' is now 5.
    
    ' Let's start building the 'resultMessage' string with the radius information.
    ' A string is a sequence of characters, such as letters, numbers, and symbols.
    ' "&" is used to concatenate (join) strings and variables in VBA.
    ' In this case, we are concatenating the text "The area of a circle with R: " with the value of 'radius' and then concatenating again the text " is ".
    resultMessage = "The area of a circle with R: " & radius & " is "
    ' This will result in a string like "The area of a circle with R: 5 is ".
    
    ' Calculate the area of the circle
    ' The formula to calculate the area of a circle is:
    ' Area = π * (radius ^ 2)
    ' By using arithmetic operators, we can perform the formula.
    area = pi * (radius ^ 2)
    
    ' Now that we have the calculated 'area', let's complete the 'resultMessage' by appending the calculated 'area' and the unit of measurement.
    ' Currently, 'resultMessage' contains "The area of a circle with R: 5 is ".
    ' We will concatenate the value of 'area' and the unit of measurement " m^2" to 'resultMessage'.
    ' The sintax of 'variable = variable & value' for string or 'variable = variable + value' (where + can be any operator) is very common in programming.
    ' This means that we are going to update the value of the variable by using the current value and adding (& or +) the new value.
    ' Remember that & can only be used to concatenate (sum) strings, and arithmetic operators (+, -, *, /, ^) can only be used with numerical values.
    resultMessage = resultMessage & area & " m^2"

    ' The final value of 'resultMessage' will be "The area of a circle with R: 5 is 78.53975 m^2".
    
    ' Display the final result in a message box to the user.
    MsgBox resultMessage

End Sub
Sub CircleAreaInMessageWithInputs()
    ' Now let's improve this code.
    ' So far the value of radius is provided inside the code.
    ' Sometimes we would like the user to input the information to perform the action.
    
    ' Let's start by defining our variables
    Const pi As Double = 3.14159
    Dim radius As Double
    Dim area As Double
    Dim resultMessage As String
    
    ' Introducing a new method: 'InputBox'.
    ' 'InputBox' displays a dialog box that prompts the user for input.
    ' It's a simple way to gather input from a user, which is returned as a String.
    
    ' Since our variable 'radius' needs to be a Double,
    ' we must convert the input from the 'InputBox' (which is a String) to a Double.
    ' This process is known as 'type conversion'.

    ' There are various methods for type conversion in VBA, each suited for different data types.
    ' For more information on these methods, visit:
    ' https://learn.microsoft.com/en-us/office/vba/language/concepts/getting-started/type-conversion-functions

    ' We will use the 'CDbl' function here. 'CDbl' is used to convert a String to a Double.
    ' This is necessary because mathematical operations in VBA require numerical values, not Strings.
    radius = CDbl(InputBox("Please enter the value of the radius"))

    
    resultMessage = "The area of a circle with R: " & radius & " is "
    area = pi * (radius ^ 2)
    resultMessage = resultMessage & area & " m^2"
    MsgBox resultMessage
    
    ' Note: If you don't input a number into the InputBox and attempt to convert the input to a Double using CDbl,
    ' VBA will throw a runtime error.
    ' This happens because CDbl expects a string that can be converted into a numerical value,
    ' and if it encounters a non-numeric string, it can't perform the conversion.
    ' We will learn how to validate read information in future sessions.
    
End Sub
Sub CircleAreaInExcelSheet()
    ' Now let's start working with information provided in an Excel worksheet.
    ' Let's assume that the cell A1 contains the text 'Radius' and the user will input the radius value in B1.
    Const pi As Double = 3.14159
    Dim radius As Double
    Dim area As Double
    Dim resultMessage As String
    
    ' Retrieve the radius value from cell B1.
    radius = Range("B1").Value
    ' Alternatively, if we have assigned a name to cell B1 in the Excel worksheet, such as 'Radius',
    ' we can directly reference the named range.
    ' radius = Range("Radius").Value
    
    area = pi * (radius ^ 2)
    resultMessage = "Area"
    
    ' Output the resultMessage value in cell A2
    Range("A2").Value = resultMessage
    
    ' Output the radius value in cell B2
    Range("B2").Value = area
    
End Sub