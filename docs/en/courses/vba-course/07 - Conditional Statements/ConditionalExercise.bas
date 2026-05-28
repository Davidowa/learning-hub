Sub LeapYear()
    ' Let's use the Select Case statement to check if a year is a leap year
    ' A leap year is a year that is divisible by 4, except for years that are divisible by 100, unless they are also divisible by 400
    ' For example, the year 2000 is a leap year, but the year 1900 is not
    ' Let's calculate if a year is a leap year using Nested If...Then...Else statements
    ' In this case we will have three nested If...Then...Else statements
    Dim year As Integer
    year = 2020
    If year Mod 4 = 0 Then
        If year Mod 100 = 0 Then
            If year Mod 400 = 0 Then
                MsgBox "The year is a leap year"
            Else
                MsgBox "The year is not a leap year"
            End If
        Else
            MsgBox "The year is a leap year"
        End If
    Else
        MsgBox "The year is not a leap year"
    End If

    ' Another approach, we will use the Select Case statement and a nested If...Then...Else statement to check if a year is a leap year
    ' In this case we will have a Select Case statement and two nested If...Then...Else statements
    Dim year As Integer
    year = 2020
    Select Case year Mod 4
        Case 0
            If year Mod 100 = 0 Then
                If year Mod 400 = 0 Then
                    MsgBox "The year is a leap year"
                Else
                    MsgBox "The year is not a leap year"
                End If
            Else
                MsgBox "The year is a leap year"
            End If
        Case Else
            MsgBox "The year is not a leap year"
    End Select

    ' Lastly is to form a one line conditional statement, meaning that we can compose a comparisson operation in just one line
    ' As we stated before, a leap year is a year that is divisible by 4, except for years that are divisible by 100, unless they are also divisible by 400
    Dim isLeapYear As Boolean
    year = 2020
    ' The following line of code will check if the year is a leap year and store the result in the isLeapYear variable
    isLeapYear = (year Mod 4 = 0 And year Mod 100 <> 0) Or (year Mod 400 = 0)

    ' Now we will display the result
    If isLeapYear Then
        MsgBox "The year is a leap year"
    Else
        MsgBox "The year is not a leap year"
    End If

    ' This approach requires less lines of code and is easier to read. However, you need a lot of practice in conditions to be able to write this kind of code
End Sub
```