Sub AccessCells()
    ' In this lesso, we are going to cover different methods to access and manipulate cells in Excel using VBA.

    ' Part 1: Direct Cell Access
    ' By using the Range method, we can access cells in a worksheet.
    ' The way to access a cell is to specify its row and column number.
    ' Then by using the Value property, we can assign a value to the cell.
    ' In this case, let's assign consecutive numbers (1 to 5) to cells in column A (A1 to A5).
    ' This approach is straightforward but can be inefficient for large datasets.
    Range("A1").Value = 1
    Range("A2").Value = 2
    Range("A3").Value = 3
    Range("A4").Value = 4
    Range("A5").Value = 5

    ' Part 2: Using Offset for Cell Access
    ' Instead of referencing each cell directly, we can use the Offset method.
    ' The offset values (rows, columns) determine the direction and distance of the movement.
    ' You can also use negative values to move up (rows) or left (columns).
    ' In the following lines, we assign even numbers (2, 4, 6, 8, 10) to cells in column B (B1 to B5).
    ' We start from cell B1 and move down by 1 row for each value.
    Range("B1").Value = 2
    Range("B1").Offset(1, 0).Value = 4
    Range("B1").Offset(2, 0).Value = 6
    Range("B1").Offset(3, 0).Value = 8
    Range("B1").Offset(4, 0).Value = 10

    ' Part 3: Combining Select and Offset
    ' Another way to work with cells is to use the Select method to focus on a specific cell.
    ' In this approach, we add a new term, which is the ActiveCell.
    ' When you apply the Select method, the selected cell becomes the ActiveCell.
    ' In a visual approach, the ActiveCell is the cell that is currently selected in the worksheet (green border).
    ' In the next lines, we assign multiples of 3 (3, 6, 9) to cells in column C (C1 to C3).
    ' First, we select cell C1 and assign the value 3. 
    ' Then, we use Offset to move down by 1 row and assign the value 6.
    ' Then, we use Offset again to move down by 1 and select this new cell as the ActiveCell.
    ' Finally, we assign the value 9 to the ActiveCell, which is now C3.
    Range("C1").Select
    ActiveCell.Value = 3
    ActiveCell.Offset(1, 0).Value = 6
    ActiveCell.Offset(2, 0).Select
    ActiveCell.Value = 9
    
End Sub