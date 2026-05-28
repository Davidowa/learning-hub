Sub RepetitionStatements()
    
    ' In this lesson, we will learn about repetition statements in VBA
    ' Repetition statements, also known as loops, are used to repeat a block of code until a condition is met
    ' There are different types of loops in VBA
    ' For...Next loop
    ' Do...Loop
    ' While...Wend loop

    ' Part 1: For...Next Loop
    ' The For...Next loop is used to repeat a block of code a specific number of times
    ' The loop starts with the For keyword and ends with the Next keyword
    ' In this loop, we need to define a counter.
    ' A counter variable in programming is a variable that is used to count something.
    ' Let's see an example of a For...Next loop
    ' We will use the For...Next loop to print the numbers from 1 to 5
    Dim i As Integer
    Dim message As String
    message = "The numbers from 1 to 5 are: "
    For i = 1 To 5
        message = message & i & " "
    Next i
    MsgBox message

    ' In this example, we used the For...Next loop to concatenate the numbers from 1 to 5 to a message
    ' The loop starts with the For keyword and ends with the Next keyword
    ' The counter variable i is used to keep track of the current number
    ' The loop runs from 1 to 5, and for each iteration, the value of i is incremented by 1 when the Next keyword is reached

    ' Let's see another example of a For...Next loop
    
    ' Let's fill a Row with Consecutive Numbers
    ' This loop places the numbers 1 to 120 horizontally starting from cell B3.
    ' We use Offset to change the value of the next cell in the row.
    Dim counter As Integer
    Range("B3").Select
    For counter = 1 To 120
        ActiveCell.Offset(0, counter - 1).Value = counter
    Next counter

    ' Another Approach to Fill a Row with Consecutive Numbers
    ' This loop achieves the same result as the first loop but uses Select to move the active cell.
    ' In this case, every time we use the Select method, the selected cell becomes the ActiveCell.
    Range("B4").Select
    For counter = 1 To 120
        ActiveCell.Value = counter
        ActiveCell.Offset(0, 1).Select
    Next counter

    ' Part 2: Do...Loop
    ' The Do...Loop is used to repeat a block of code while a condition is True
    ' The loop starts with the Do keyword and ends with the Loop keyword
    ' There are different types of Do...Loop
    ' Do While...Loop
    ' Do Until...Loop
    ' Let's see an example of a Do While...Loop
    ' We will use the Do While...Loop to print the numbers from 1 to 5
    Dim j As Integer
    Dim message2 As String
    message2 = "The numbers from 1 to 5 are: "
    j = 1
    Do While j <= 5
        message2 = message2 & j & " "
        j = j + 1
    Loop

    MsgBox message2

    ' In this example, we used the Do While...Loop to concatenate the numbers from 1 to 5 to a message
    ' The loop starts with the Do keyword and ends with the Loop keyword
    ' The condition j <= 5 is checked at the beginning of the loop
    ' If the condition is True, the block of code inside the loop is executed.
    ' It's like saying "Do this while this condition is True"
    ' The value of j is incremented by 1 inside the loop
    ' The loop continues until the condition j <= 5 is False

    ' Let's see another example of a Do Until...Loop
    ' We will use the Do Until...Loop to print the numbers from 1 to 5
    Dim k As Integer
    Dim message3 As String
    message3 = "The numbers from 1 to 5 are: "
    k = 1
    Do Until k > 5
        message3 = message3 & k & " "
        k = k + 1
    Loop

    MsgBox message3

    ' In this example, we used the Do Until...Loop to concatenate the numbers from 1 to 5 to a message
    ' The loop starts with the Do keyword and ends with the Loop keyword
    ' The condition k > 5 is checked at the beginning of the loop
    ' If the condition is False, the block of code inside the loop is executed.
    ' It's like saying "Do this until this condition is True"
    ' The value of k is incremented by 1 inside the loop
    ' The loop continues until the condition k > 5 is True (in this case, when k = 6)

    ' Part 3: While...Wend Loop
    ' The While...Wend loop is used to repeat a block of code while a condition is True
    ' The loop starts with the While keyword and ends with the Wend keyword
    ' Let's see an example of a While...Wend loop
    ' We will use the While...Wend loop to print the numbers from 1 to 5
    Dim l As Integer
    Dim message4 As String
    message4 = "The numbers from 1 to 5 are: "
    l = 1
    While l <= 5
        message4 = message4 & l & " "
        l = l + 1
    Wend

    MsgBox message4

    ' In this example, we used the While...Wend loop to concatenate the numbers from 1 to 5 to a message
    ' The loop starts with the While keyword and ends with the Wend keyword
    ' The condition l <= 5 is checked at the beginning of the loop
    ' If the condition is True, the block of code inside the loop is executed.
    ' It's like saying "While this condition is True, do this"
    ' The value of l is incremented by 1 inside the loop
    ' The loop continues until the condition l <= 5 is False
    ' The difference between the While...Wend loop and the Do While...Loop is the position of the condition
    ' In the While...Wend loop, the condition is checked at the beginning of the loop
    ' On the other hand, in the Do While...Loop, the condition is checked at the end of the loop
    ' So in the Do While...Loop, the block of code inside the loop is executed at least once, even if the condition is False at the beginning.
    
End Sub