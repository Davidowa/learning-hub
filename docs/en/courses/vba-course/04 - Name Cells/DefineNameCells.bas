Sub DefineNameCells()

    ' Definition of cell names using VBA
    ' In this lesson, we will learn how to define cell names using VBA.
    ' In previous Excel Courses, we learned how to define cell names manually.
    ' We have to go to the 'Formulas' tab, click on 'Define Name', and then assign a name to a cell or range of cells.
    ' This will change the way we reference these cells in our formulas.
    ' The normal way to reference a cell is by using its address, such as A1, B2, C3, etc.
    ' Where, A is the column and 1 is the row for instance.

    ' Using the A1 notation, we usually call it relative cell reference.
    ' This means that the reference is relative to the cell that contains the formula.

    ' It's contrast is absolute cell reference, which is a reference that does not change when copied or moved to another cell.
    ' For example, if you copy a formula from cell A1 to cell B1, the relative reference will change from A1 to B1.
    ' However, the absolute reference will remain the same.
    ' The absolute reference is indicated by the dollar sign ($).
    ' For example, $A$1 is an absolute reference.

    ' In VBA, the relative reference and absolute reference does not apply in the same way as in Excel.
    

End Sub

Sub DefineNameCells()
    ' References and Names in Excel vs VBA
    ' In this lesson, we will explore how to define names for cells and ranges using VBA.
    ' However, before we dive into the VBA code, let's review some background information about cell names in Excel.
    
    ' Background: Cell Names in Excel
    ' Normally, cells in Excel are referenced by their positions, such as "A1" for the cell at column A and row 1. 
    ' Naming cells or ranges allows us to refer to them by meaningful names instead of just their cell addresses. 
    ' This is particularly useful in complex formulas, making them easier to understand.
    
    ' Defining Names Manually in Excel
    ' In Excel, you can name a cell or range manually by going to the 'Formulas' tab, selecting 'Define Name', and then specifying a name. 
    ' Named cells can simplify formula creation by replacing cell references with descriptive names.
    
    ' Relative vs. Absolute References
    ' - Relative References change when a formula is copied to another cell. They are the default reference type in Excel (e.g., A1).
    ' - Absolute References remain constant, no matter where they are copied. They are denoted by dollar signs (e.g., $A$1).
    
    ' However, when programming with VBA, the concept of relative and absolute references is not applied in the same manner. 
    ' In VBA, we directly manipulate cells and ranges using their names or addresses without worrying about how formulas adapt.
    ' When we are working with VBA, we're constantly setting values or properties directly, so the concept of relative and absolute references is not as relevant.
    ' However, defining names for cells and ranges can still be useful for making code more readable and maintainable.

    ' Defining a Name for a Cell
    ' The following code demonstrates how to define a name for the cell A1 as "StartingCell" using VBA. 

    ' This allows us to refer to cell A1 by this name in our VBA code and Excel formulas.
    ' To define a name cell in VBA we use
    ' ThisWorkbook.Names.Add Name:="NameOfTheCell", RefersTo:="=Sheet1!$A$1"
    ThisWorkbook.Names.Add Name:="StartingCell", RefersTo:="=Sheet1!$A$1"
    
    ' Here, 'ThisWorkbook.Names.Add' is used to create a new named reference. The ThisWorkbook object refers to the workbook where the VBA code is running.
    ' 'Name:="NameOfTheCell"' specifies the name to be assigned. In this case, "StartingCell" is the name.
    ' 'RefersTo:="=Sheet1!$A$1"' defines the cell or range the name refers to.

    ' Defining a Name for a Range
    ' The following code demonstrates how to define a name for a range of cells using VBA.
    ' This allows us to refer to the range by this name in our VBA code and Excel formulas.
    ' To define a name range in VBA we use
    ' ThisWorkbook.Names.Add Name:="NameOfTheRange", RefersTo:="=Sheet1!$A$1:$B$5"
    ThisWorkbook.Names.Add Name:="DataRange", RefersTo:="=Sheet1!$A$1:$B$5"

    ' Here, 'ThisWorkbook.Names.Add' is used to create a new named reference.
    ' 'Name:="NameOfTheRange"' specifies the name to be assigned. In this case, "DataRange" is the name.
    ' 'RefersTo:="=Sheet1!$A$1:$B$5"' defines the cell or range the name refers to.

    ' Naming of ranges is going to be useful in later lessons when we start working with data analysis and manipulation.

End Sub
