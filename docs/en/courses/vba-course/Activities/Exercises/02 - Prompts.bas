Sub PromptTwoQuestions()
    ' Prompt the user to answer two questions
    ' The answers will be stored in variables
    
    ' Declare variables to store the answers
    ' To declare a variable, use the Dim statement followed by the variable name and the data type
    ' In this case, the answers will be stored as strings
    Dim answer1 As String
    Dim answer2 As String
    
    ' To prompt the user to answer a question, use the InputBox function
    ' The InputBox function takes a string argument with the question to be displayed
    ' The user's answer will be stored in the variable using the assignment operator (=)

    ' Prompt the user to answer the first question
    answer1 = InputBox("What is your name?")
    
    ' Prompt the user to answer the second question
    answer2 = InputBox("What is your hobby")

    ' Let's display the answers in their corresponding cells
    ' The Range method takes a string argument with the cell address
    ' The Value property of the Range object is used to set the cell value
    Range("B1").Value = answer1
    Range("B2").Value = answer2
    
    ' You can display the answers in a cell
    Range("A4").Value = "Hi " & answer1 & ", it's nice to know that your hobby is " & answer2

    ' To display a message box to the user, use the MsgBox function
    ' The MsgBox function takes a string argument with the message to be displayed
    ' You can concatenate (join) strings and variables using the & operator

    ' Display the answers in a message box
    MsgBox "Hi " & answer1 & ", it's nice to know that your hobby is " & answer2
End Sub