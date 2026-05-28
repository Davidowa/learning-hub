Sub ConditionalStatements()
    ' In this lesson, we are going to cover the conditional statements in VBA.
    ' Conditional statements are used to execute a block of code based on a condition.
    ' There are four conditional statements in VBA:
    ' If...Then
    ' If...Then...Else
    ' If...Then...ElseIf...Then...Else
    ' Select Case

    ' Part 1: If...Then
    ' The If...Then statement is used to execute a block of code if a condition is True
    ' The condition is checked after the If keyword
    ' If the condition is True, the block of code is executed
    ' Let's see an example of an If...Then statement
    ' We will use the If...Then statement to check if a number is positive
    Dim a As Integer
    a = 5
    If a > 0 Then
        MsgBox "The number is positive"
    End If

    ' In this example, we used the If...Then statement to check if the number a is positive
    ' The condition a > 0 is checked after the If keyword
    ' If the condition is True, in this a is greater than 0. Therefore, the block of code is executed.
    ' The block of code is indented to make it clear that it is inside the If...Then statement.
    ' Lastly, the block of code ends with the End If keyword.

    ' Part 2: If...Then...Else
    ' The If...Then...Else statement is used to execute a block of code if a condition is True, and another block of code if the condition is False
    ' The condition is checked after the If keyword
    ' If the condition is True, the first block of code is executed
    ' If the condition is False, the second block of code is executed
    ' Let's see an example of an If...Then...Else statement
    ' We will use the If...Then...Else statement to check if a number is positive or negative
    Dim b As Integer
    b = -5
    If b > 0 Then
        MsgBox "The number is positive"
    Else
        MsgBox "The number is negative"
    End If

    ' In this example, we used the If...Then...Else statement to check if the number b is positive or negative  
    ' The condition b > 0 is checked after the If keyword
    ' If the condition is True, in this b is less than 0. Therefore, the first block of code is not executed
    ' The second block of code, which is after the Else keyword, is executed instead
    ' Lastly, the block of code ends with the End If keyword.

    ' Part 3: If...Then...ElseIf...Then...Else
    ' The If...Then...ElseIf...Then...Else statement is used to execute an specific block of code if one of its conditions is True, and another block of code if all the conditions are False
    ' The conditions are checked after the If and ElseIf keywords
    ' The conditions are checked in order, from top to bottom
    ' When a condition is True, the block of code of that condition is executed. After that, it exits the If...Then...ElseIf...Then...Else statement
    ' However, if all the conditions are False, the block of code after the Else keyword is executed.
    ' Let's see an example of an If...Then...ElseIf...Then...Else statement
    ' We will use the If...Then...ElseIf...Then...Else statement to check if a number is positive, negative or zero
    Dim c As Integer
    c = 0
    If c > 0 Then
        MsgBox "The number is positive"
    ElseIf c < 0 Then
        MsgBox "The number is negative"
    Else
        MsgBox "The number is zero"
    End If

    ' In this example, we used the If...Then...ElseIf...Then...Else statement to check if the number c is positive, negative or zero
    ' Firt, the condition c > 0 is checked after the If keyword. In this case, c is not greater than 0. Therefore, the block of code is not executed
    ' Then, the condition c < 0 is checked after the ElseIf keyword. In this case, c is not less than 0. Therefore, the block of code is not executed
    ' Lastly, the block of code after the Else keyword is executed instead, as all the conditions are False.
    ' In this form, the Else is usually called the default condition, as it is executed when all the other conditions are False.

    ' Let's see another example of an If...Then...ElseIf...Then...Else statement
    ' Let's use the If...Then...ElseIf...Then...Else statement to classify a student based on his grade
    Dim score As Double
    score = 7.5
    If score >= 9 Then
        MsgBox "The student has an A"
    ElseIf score >= 8 Then
        MsgBox "The student has a B"
    ElseIf score >= 7 Then
        MsgBox "The student has a C"
    ElseIf score >= 6 Then
        MsgBox "The student has a D"
    Else
        MsgBox "The student has an F"
    End If

    ' Part 4: Select Case
    ' The Select Case statement is used to execute a block of code based on the value of a variable
    ' checked after the Select Case keyword
    ' compared to the values of the Case clauses
    ' When equal to the value of a Case clause, the block of code of that Case clause is executed
    ' If not equal to any of the values of the Case clauses, the block of code after the Case Else keyword is executed
    ' Let's see an example of a Select Case statement
    ' We will use the Select Case statement to check the value of a variable
    Dim d As Integer
    d = 3
    Select Case d
        Case 1
            MsgBox "1"
        Case 2
            MsgBox "2"
        Case 3
            MsgBox "3"
        Case Else
            MsgBox "not 1, 2 or 3"
    End Select

    ' In this example, we used the Select Case statement to check the value of the variable d
    ' Same as the If...Then...ElseIf...Then...Else statement, compared in order, from top to bottom
    ' When equal to the value of a Case clause, the block of code of that Case clause is executed
    ' The Select Case statement ends with the End Select keyword
    ' The Select Case statement is useful when you have to compare if the value of a variable is equal to a list of values.
    ' If you require to compare if the value of a variable is greater than, less than or equal to a value, you should use the If...Then...ElseIf...Then...Else statement instead.
End Sub
Sub NestedConditionalStatements()
    ' In this lesson, we are going to cover the nested conditional statements in VBA.
    ' Nested conditional statements are used to execute a block of code based on a condition, and inside that block of code, execute another block of code based on another condition.

    ' Part 1: Nested If...Then...Else
    ' We will use the Nested If...Then...Else statement to check if a number is positive, negative or zero
    Dim a As Integer
    a = 0
    If a > 0 Then
        MsgBox "The number is positive"
    Else
        If a < 0 Then
            MsgBox "The number is negative"
        Else
            MsgBox "The number is zero"
        End If
    End If

    ' Lets see another example of a Nested If...Then...Else statement
    ' Let's use the Nested If...Then...Else statement to classify a student based on his grade
    ' But now, We will have A+, A, B+, B, C+, C, D and F
    Dim score As Double
    score = 7.5
    If score >= 9 Then
        If score >= 9.5 Then
            MsgBox "The student has an A+"
        Else
            MsgBox "The student has an A"
        End If
    ElseIf score >= 8 Then
        If score >= 8.5 Then
            MsgBox "The student has a B+"
        Else
            MsgBox "The student has a B"
        End If
    ElseIf score >= 7 Then
        If score >= 7.5 Then
            MsgBox "The student has a C+"
        Else
            MsgBox "The student has a C"
        End If
    ElseIf score >= 6 Then
        MsgBox "The student has a D"
    Else
        MsgBox "The student has an F"
    End If

    ' We can have a Nested Select Case statement as well
    ' Let's use the Nested Select Case statement to check if the value of a variable is positive, and according to that, check display the name of the month
    Dim month As Integer
    month = 3
    If month > 0 Then
        Select Case month
            Case 1
                MsgBox "January"
            Case 2
                MsgBox "February"
            Case 3
                MsgBox "March"
            Case 4
                MsgBox "April"
            Case 5
                MsgBox "May"
            Case 6
                MsgBox "June"
            Case 7
                MsgBox "July"
            Case 8
                MsgBox "August"
            Case 9
                MsgBox "September"
            Case 10
                MsgBox "October"
            Case 11
                MsgBox "November"
            Case 12
                MsgBox "December"
            Case Else
                MsgBox "Not a valid month"
        End Select
    Else
        MsgBox "The number is not positive"
    End If

    ' In this case, instead of using a nested If...ElseIf...Else statement, we used a nested Select Case statement
    

End Sub