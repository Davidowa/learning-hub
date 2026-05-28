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
    Call ReadInputParameters

    ' Let's leave it here for now. 
    ' You have to continue writing the rest of the code to finish the amortization table ;)

    ' Now let's create a function to do the most basic operation, a sum.
    ' As we said before, a function is used to execute a block of code and return a value.
    ' We will use the Function statement to create a function. Let's jump to (5)

    ' (6) Welcome back to the main subprocedure.
    ' Now, let's write the code to call the "Summation" function.
    ' We will use the name of the function to call the function and pass the arguments to the function.
    ' We will use the MsgBox function to display the result of the function.
    Dim resultSummation As Double
    resultSummation = Summation(5, 3)
    MsgBox "The result of the summation is " & resultSummation

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
Function Summation(number1 As Double, number2 As Double) As Double
    ' (5) Now let's write the code for the Summation function.
    ' We will use the Function statement to create a function.
    ' We will use the As statement to specify the data type of the value that the function will return.
    ' We will use the name of the function to call the function and pass the arguments to the function.
    ' We will use the Return statement to return the value of the function.

    ' Let's write the code to add two numbers and return the result.
    Summation = number1 + number2

    ' for Functions, the name of the function is used to return the value of the function.

    ' Now we will call this function from the main subprocedure. Let's move to (6) to continue reading.

End Function