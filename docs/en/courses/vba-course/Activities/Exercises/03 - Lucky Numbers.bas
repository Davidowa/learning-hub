Sub CreateRandomNumbersInCells()
    ' Generate random numbers and place them in cells
    ' Declare a variable to store the random number
    Dim randomNumber As Integer
    
    ' Let's clear the previous random numbers and the sum
    ' The ClearContents method clears the cell contents
    Range("B3:H3").ClearContents

    ' Set the starting position to generate random numbers
    Range("B3").Select
    
    ' Loop through the cells and generate random numbers
    ' Let's use a For loop to generate random numbers for the 6 cells
    ' The For loop lets you repeat a block of code a specific number of times
    ' The loop variable (i) will start at 1 and end at 6

    Dim i As Integer
    For i = 1 To 6
        ' Generate a random number between 1 and 59
        ' To access Excel functions, use the WorksheetFunction object
        ' It provides access to Excel functions like RandBetween
        ' The RandBetween function takes two arguments: the minimum and maximum values
        randomNumber = WorksheetFunction.RandBetween(1, 59)
        
        ' Place the random number in the current cell
        ActiveCell.Value = randomNumber
        
        ' Move to the next cell
        ActiveCell.Offset(0, 1).Select
    ' The Next statement is used to increment the loop variable (i) and continue the loop until the end value (6)
    Next i

    ' Now let's do the sum of the random numbers
    ' First, we need to go back to the first cell
    Range("B3").Select

    ' Declare a variable to store the sum of the random numbers
    Dim sum As Integer
    sum = 0 ' Initialize the sum variable to 0

    ' Now let's loop through the cells and calculate the sum using a Do While loop
    ' The Do While loop repeats a block of code while a condition is true
    ' In this case, we want to continue the loop while the current cell is not empty
    Do While ActiveCell.Value <> "" ' The current active cell is B3
        ' Add the value of the current cell to the sum
        sum = sum + ActiveCell.Value
        
        ' Move to the next cell
        ActiveCell.Offset(0, 1).Select
    ' The Loop statement is used to go back to the Do While statement and check the condition again
    Loop

    ' Place the sum in the last cell
    ' As the last selected cell is H3, which is empty and where we want to place the sum, we set the value directly
    ActiveCell.Value = sum
End Sub