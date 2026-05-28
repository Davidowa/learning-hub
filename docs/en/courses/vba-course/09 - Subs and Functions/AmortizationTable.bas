Sub SubFunctions()
    ' In this lesson we will learn about Subs and Functions
    ' So far, we have been using Subs to execute a block of code
    ' Subs are used to execute a block of code, but they do not return a value
    ' This that the code inside a Sub will be executed, and once it finishes, it will stop executing.

    ' However, in programming, we usually need to execute multiple Subs and Functions to perform a task.
    ' In the beginning and in the previous line, we use the term Function.
    ' Functions are used to execute a block of code and return a value. 
    ' This means that the code inside a Function will be executed, and once it finishes, it will return a value.

    ' But don't panic, in this lesson we will learn how to create and use Subs and Functions in VBA.
    ' In our classes and previous codes, you have seen that I divided the code into Subs, and we have used play and stop buttons to execute of an specific Sub.

    ' Let's consider this SubFuction subprocedure as the main subprocedure of the program.
    ' This means that this subprocedure will be the first subprocedure to be executed when the program starts.
    ' and it will call the other subprocedures to perform the task.

    ' Let's create a Sub called "SetupFieldsInWorksheet" to write the names of the fields in the worksheet.
    ' I will start using a notation of the order of how to read this lesson.
    ' I will write (1) to indicate you where you have to continue reading after this line. 


    ' (2) Welcome back to the main subprocedure.
    ' Now, let's write the code to call the "SetupFieldsInWorksheet" subprocedure.
    ' To execute a subprocedure, we use the Call statement followed by the name of the subprocedure.
    ' We will use the Call statement to call the "SetupFieldsInWorksheet" subprocedure.
    Call SetupFieldsInWorksheet

    ' Now, let's write another function to use the InputBox function to get the values of each field from the user.
    ' Let us jump to (3) to continue reading.

    ' (4) Welcome back to the main subprocedure.
    ' Now, let's write the code to call the "ReadInputParameters" subprocedure.
    Call ReadInputParametersValidation

    ' Let's leave it here for now. 
    ' You have to continue writing the rest of the code to finish the amortization table ;)
    ' I think I have given you enough time to solve this problem.
    ' Now, let's finish together the code to create the amortization table.
    ' Let's move to the next subprocedure to continue writing the code.
    ' Let's move to (5) to continue reading.

    ' (6) Welcome back to the main subprocedure.
    ' Now, let's write the code to call the "AmortizationTable" subprocedure.
    Call AmortizationTable

    ' And that's all folks! We have finished the main subprocedure; consequently, we have finished making our amortization table!

End Sub
Sub SetupFieldsInWorksheet()
    ' (1) see, now you have to continue reading from here.
    ' Let's start writing the code for the "SetupFieldsInWorksheet" subprocedure.
    ' Remember the amortization table we created in the first lesson?
    ' Let's write the necessary fields and define the necessary cell names in the worksheet.

    ' Let's start applying all the knowledge we have learned so far.
    ' We will use the Range object to write the names of the fields in the worksheet.
    ' We will use the Name property to define the names of the cells.

    ' First, we will write the names of the fields in the worksheet.
    Range("A1").Value = "Amortization Table Parameters"
    Range("A2").Value = "Loan Amount"
    Range("A3").Value = "Annual Interest Rate"
    Range("A4").Value = "Monthly Interest Rate"
    Range("A5").Value = "Number of Payments"
    Range("A6").Value = "Monthly Payment"
    Range("A7").Value = "Total Payment"

    ' Now, we will define the names of the cells.
    ' We will use the Name property to define the names of the cells.
    
    ThisWorkbook.Names.Add Name:="LoanAmount", RefersTo:="=Sheet1!$B$2"
    ThisWorkbook.Names.Add Name:="AnnualInterestRate", RefersTo:="=Sheet1!$B$3"
    ThisWorkbook.Names.Add Name:="MonthlyInterestRate", RefersTo:="=Sheet1!$B$4"
    ThisWorkbook.Names.Add Name:="NumberOfPayments", RefersTo:="=Sheet1!$B$5"
    ThisWorkbook.Names.Add Name:="MonthlyPayment", RefersTo:="=Sheet1!$B$6"
    ThisWorkbook.Names.Add Name:="TotalPayment", RefersTo:="=Sheet1!$B$7"

    ' Also, let's apply some number formatting to the cells
    ' We will use the NumberFormat property to apply the number formatting to the cells
    Range("LoanAmount").NumberFormat = "$#,##0.00"
    Range("AnnualInterestRate").NumberFormat = "0.00%"
    Range("MonthlyInterestRate").NumberFormat = "0.00%"
    Range("NumberOfPayments").NumberFormat = "0"
    Range("MonthlyPayment").NumberFormat = "$#,##0.00"
    Range("TotalPayment").NumberFormat = "$#,##0.00"

    ' Now we will call this subprocedure from the main subprocedure.
    ' Let's move to (2) to continue reading.

End Sub
Sub ReadInputParameters()
    ' (3) So, now let's use the InputBox function to get the values of each field from the user.
    ' In total we need to input 3 values: the loan amount, the annual interest rate and the number of payments.
    Dim loanAmount As Double
    Dim annualInterestRate As Double
    Dim numberOfPayments As Integer

    loanAmount = CDbl(InputBox("Please enter the loan amount", "Input Loan Amount"))
    annualInterestRate = CDbl(InputBox("Please enter the annual interest rate", "Input Annual Interest Rate"))
    numberOfPayments = CInt(InputBox("Please enter the number of payments", "Input Number of Payments"))

    ' Now let's write those values in the worksheet.
    Range("LoanAmount").Value = loanAmount
    Range("AnnualInterestRate").Value = annualInterestRate
    ' For the Monthly Interest Rate, we will assign it a formula instead of a value
    ' As we mentioned before, the monthly interest rate is the twelve squared root of the annual interest rate plus 1 and then minus 1
    ' We will use the Formula property to assign the formula to the cell
    ' As you can see, using cell names is easier to write the formula
    Range("MonthlyInterestRate").Formula = "=((1+AnnualInterestRate)^(1/12))-1"
    Range("NumberOfPayments").Value = numberOfPayments

    ' Now we will call this subprocedure from the main subprocedure. Let's move to (4) to continue reading.

End Sub
Sub ReadInputParametersValidation()
    ' This is an extra to show you how to validate the input of the user.
    ' We will use the IsNumeric function to check if the value entered by the user is a number.
    ' However, we also require a loop to keep asking the user to enter a number if the value entered is not a number.
    
    Dim loanAmount As Double
    Dim annualInterestRate As Double
    Dim numberOfPayments As Integer
    Dim inputValid As Boolean
    Dim userInput As String
    
    inputValid = False ' Initialize the flag to indicate input is not yet valid
    
    Do While Not inputValid
        userInput = InputBox("Please enter the loan amount", "Input Loan Amount")
        
        If IsNumeric(userInput) And userInput <> "" Then ' Check if input is numeric and not empty
            loanAmount = CDbl(userInput) ' Safely convert to Double for numeric operations
            inputValid = True ' Set the flag to true to exit the loop
        Else
            MsgBox "The value entered is not a number. Please enter a numeric value.", vbExclamation, "Input Invalid"
        End If
    Loop

    inputValid = False ' Reset the flag to indicate input is not yet valid

    Do While Not inputValid
        userInput = InputBox("Please enter the annual interest rate", "Input Annual Interest Rate")
        
        If IsNumeric(userInput) And userInput <> "" Then ' Check if input is numeric and not empty
            annualInterestRate = CDbl(userInput) ' Safely convert to Double for numeric operations
            inputValid = True ' Set the flag to true to exit the loop
        Else
            MsgBox "The value entered is not a number. Please enter a numeric value.", vbExclamation, "Input Invalid"
        End If
    Loop

    inputValid = False ' Reset the flag to indicate input is not yet valid

    Do While Not inputValid
        userInput = InputBox("Please enter the number of payments", "Input Number of Payments")
        
        If IsNumeric(userInput) And userInput <> "" Then ' Check if input is numeric and not empty
            numberOfPayments = CInt(userInput) ' Safely convert to Integer for numeric operations
            inputValid = True ' Set the flag to true to exit the loop
        Else
            MsgBox "The value entered is not a number. Please enter a numeric value.", vbExclamation, "Input Invalid"
        End If
    Loop

    ' Now let's write those values in the worksheet.
    Range("LoanAmount").Value = loanAmount
    Range("AnnualInterestRate").Value = annualInterestRate
    Range("MonthlyInterestRate").Formula = "=((1+AnnualInterestRate)^(1/12))-1"
    Range("NumberOfPayments").Value = numberOfPayments

End Sub
Sub AmortizationTable()
    ' (5) Now, let's write the code to create the amortization table.
    ' First, we will write the names of the fields in the worksheet.
    Range("A9").Value = "Amortization Table"
    Range("A10").Value = "Payment Number"

    ' Let's write the numbers from 1 to 120 in the worksheet.
    ' 120 is the maximum number of periods this model can support.
    Dim i As Integer
    Range("B10").Select
    For i = 1 To 120
        ActiveCell.Value = i
        ActiveCell.Offset(0, 1).Select
    Next i

    ' Now, let's write the names of the fields in the worksheet.
    Range("A11").Select
    Range("A11").Value = "Initial Loan Amount"
    Range("A12").Value = "Interest Payment"
    Range("A13").Value = "Principal Payment"
    Range("A14").Value = "Remaining Loan Amount"

    ' Now, let's write the formulas to calculate the values of the fields in each period.
    ' For the first period:
    Range("B11").Formula = "=LoanAmount"
    Range("B11").NumberFormat = "$#,##0.00"
    Range("B12").Formula = "=LoanAmount*MonthlyInterestRate"
    Range("B12").NumberFormat = "$#,##0.00"
    Range("B13").Formula = "=MonthlyPayment"
    Range("B13").NumberFormat = "$#,##0.00"
    Range("B14").Formula = "=LoanAmount+B12-B13"
    Range("B14").NumberFormat = "$#,##0.00"

    ' Now for the second and consecutive periods we will use a combination of a loop, the with statement, the offset property and the formula property, and the formulaR1C1 property.
    ' Let's start describing the With statement.
    ' The With statement allows you to perform a series of statements on a specified object without requalifying the name of the object.
    ' This means that you can perform a series of statements on a specified object without having to specify the name of the object each time.

    ' Now let's describe the formulaR1C1 property.
    ' The FormulaR1C1 property is used to set the formula of a cell using the R1C1 notation.
    ' The R1C1 notation is a notation used to refer to cells in a worksheet.
    ' In this notation, R1C1 refers to the cell in the first row and the first column of the worksheet.
    ' The R1C1 notation is useful when you want to set the formula of a cell using the offset property.

    For i = 1 To 120
        With Range("C11").Offset(0, i - 1) ' Start from C11 and move down each iteration
            .FormulaR1C1 = "=R[3]C[-1]" ' This will set the formula to cell B14
            .NumberFormat = "$#,##0.00"
            .Offset(1, 0).FormulaR1C1 = "=R[-1]C*MonthlyInterestRate" ' This will set the formula to cell the row above in the same column multiplied by the monthly interest rate
            .Offset(1, 0).NumberFormat = "$#,##0.00"
            ' Now let's use an If statement to set the formula to evaluate if the current period is less than or equal to the number of payments we want to calculate
            ' If it's true, then we will set the formula to calculate the monthly payment
            ' If it's false, then we will set the formula to calculate 0, as there are no more payments to calculate
            If i<=Range("NumberOfPayments").Value Then
                .Offset(2, 0).Formula = "=MonthlyPayment" 
            Else
                .Offset(2, 0).Formula = "=0" 
            End If
            .Offset(2, 0).NumberFormat = "$#,##0.00"
            .Offset(3, 0).FormulaR1C1 = "=R[-3]C+R[-2]C-R[-1]C" ' This will set the formula to cell above three rows (initial loan amount) plus the cell above two rows (interest payment) minus the cell above one row (principal payment) of the same column
            .Offset(3, 0).NumberFormat = "$#,##0.00"
            If i = 120 Then
                .Offset(3, 0).Select
            End If
        End With
    Next i

    ' Now let's name the current ActiveCell as "RemainingLoanAmount"
    ' We will use the Name property and the Address property to define the name of the cell.
    ' ActiveSheet.Name will return the name of the active sheet 
    ' ActiveCell.Address will return the address of the active cell
    ' For instance, if the active sheet is "Sheet1" and the active cell is "B14", then the name of the cell will be "Sheet1!$B$14"
    ' You can also noticed that we are using single quotes to refer to the active sheet.
    ' This is useful when the name of the sheet has spaces.
    ThisWorkbook.Names.Add Name:="RemainingLoanAmount", RefersTo:="='" & ActiveSheet.Name & "'!" & ActiveCell.Address
    Range("TotalPayment").Formula = "=RemainingLoanAmount" 

    ' Lastly, lets apply the Goal Seek tool to calculate the monthly payment.
    Range("TotalPayment").GoalSeek Goal:=0, ChangingCell:=Range("MonthlyPayment")
    Range("A1").Select

    ' Let's move to the main subprocedure to continue writing the code (6).
End Sub