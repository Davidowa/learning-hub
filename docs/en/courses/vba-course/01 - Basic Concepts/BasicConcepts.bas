Attribute VB_Name = "BasicMacros"
Sub MessageAndSubs()

    ' Let's start with the most basic programming task: displaying a message.
    ' In VBA, you can use the MsgBox function to display a message in a dialog box.
    ' The basic syntax of the MsgBox function is:
    ' MsgBox Prompt
    ' Where Prompt is the message you want to display.

    ' In this macro, we create a message word (MsgBox) with the text "Hello, World!"
    MsgBox "Hello, World!"

    ' The message can be a string, a number, a variable, or an expression.
    ' More details about variables and expressions will be covered in the above sections.

    ' An addittional concept to be aware of is the Sub procedure.
    ' You can notices that the code is inside a Sub word and an End Sub word.
    ' Sub is short for Subroutine, which is a block of code that performs a specific task.
    ' The code inside the Sub and End Sub is the body of the Subroutine, in other words, the code that will be executed.
    ' We usually refer to the Subroutine as a macro, which is a sequence of instructions that automates a task.
    ' A Macro is a set of instructions that can be executed by a user or by another macro.
    ' This could also mean that a macro can call a subroutine, which executes a specific task and/or call other subroutines and functions.

End Sub
Sub Variables()
    
    ' Variables
    ' Now let's move to the next fundamental concept in VBA programming: Variables.
    ' Variables are fundamental elements in any programming language.
    ' They are used for storing data.

    ' To declare a variable in VBA, use the 'Dim' keyword followed by the variable's name.
    ' This name, known as an identifier, is a unique label used to reference specific data in your code.
    Dim number1
    Dim positionX
    
    ' VBA is not case-sensitive.
    ' This means that 'myvariable' and 'MyVariable' are treated as the same identifier.
    ' Using the same name with different cases will lead to an error.
    Dim myvariable
    'Dim MyVariable  ' Uncommenting this will cause an error due to duplicate names.
    
    ' There are specific rules for naming variables in VBA.
    ' For more details, please refer to page 16 of Excel_01.pdf on Moodle.
    
    ' Typically, you define a variable by specifying both its name and type:
    ' Dim VariableName As DataType
    
    ' The most commonly used variable types in VBA include:
    Dim age As Integer       ' Integer: Stores whole numbers without decimals.
    Dim price As Double      ' Double: Stores large decimal numbers.
    Dim name As String       ' String: Stores text.
    Dim isVisible As Boolean ' Boolean: Stores TRUE or FALSE values.
    
    ' For a comprehensive list of variable types, refer to page 17 of Excel_01.pdf on Moodle.

    ' In the first lines, you can notice that I did not specify a type for the variables.
    ' When a type is not specified in VBA, Excel considers these variables as 'Variant'.
    ' A 'Variant' type can take any form of data.
    ' However, it is recommended to avoid using 'Variant' when possible as it can impact
    ' performance due to its flexibility and memory usage.
    
    'Dim number2 ' As mentioned, try to avoid using this notation
    Dim number2 As Long ' Long: Stores larger whole numbers without decimals.
    
End Sub
Sub Constants()
    ' Constants
    ' Constants are similar to variables, but their values remain unchanged throughout the macro.
    ' We declare a constant using the 'Const' keyword instead of 'Dim'.

    Const pi As Double = 3.14159

    ' Here, we're declaring a constant named 'pi' and assigning it the value of 3.14159.
    ' The type of this constant is 'Double', which is used for decimal numbers.
    ' Constants are useful for values that we know will not change, such as mathematical constants like pi.
    ' Constants are declared and assigned a value in the same line.
    ' Using constants helps prevent accidental modification of these values in the code.
    
    ' If you try to change the value of a constant, you will receive an error.
    'pi = 3.14 ' Uncommenting this line will cause an error.
    
End Sub