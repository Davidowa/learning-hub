Sub MoveRight()
    ' Set the inicial cell as the ActiveCell
    ActiveCell.Select
    ' Move the ActiveCell to the right

    ' The Offset method takes two arguments
    ' The number of rows (1) and the number of columns (1) to move
    ActiveCell.Offset(0, 1).Select
End Sub
Sub MoveLeft()
    ' Set the inicial cell as the ActiveCell
    ActiveCell.Select
    ' Move the ActiveCell to the left

    ' The Offset method takes two arguments
    ' The number of rows (0) and the number of columns (-1) to move
    ActiveCell.Offset(0, -1).Select
End Sub
Sub MoveUp()
    ' Set the inicial cell as the ActiveCell
    ActiveCell.Select
    ' Move the ActiveCell up

    ' The Offset method takes two arguments
    ' The number of rows (-1) and the number of columns (0) to move
    ActiveCell.Offset(-1, 0).Select
End Sub
Sub MoveDown()
    ' Set the inicial cell as the ActiveCell
    ActiveCell.Select
    ' Move the ActiveCell down

    ' The Offset method takes two arguments
    ' The number of rows (1) and the number of columns (0) to move
    ActiveCell.Offset(1, 0).Select
End Sub
Sub MoveToGoal()
    ' Move the ActiveCell to the goal of the maze
    ' The goal is the cell F3

    ' The Range method takes a string argument with the cell address
    Range("F3").Select

    ' You can also create a Range object and use the Select method
    Dim goal As Range
    Set goal = Range("F3")
    goal.Select

    ' Or you can create a string variable with the cell address
    Dim goalAddress As String
    goalAddress = "F3"
    Range(goalAddress).Select
End Sub
Sub RestartMaze()
    ' Move the ActiveCell to the start of the maze
    ' The start is the cell A1

    ' The Range method takes a string argument with the cell address
    Range("B2").Select
End Sub