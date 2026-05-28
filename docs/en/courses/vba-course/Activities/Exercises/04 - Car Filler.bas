Sub AddDetails()
    ' Fill the form with details
    ' C4 is the cell for the name
    ' C5 is the cell for the birthdate
    ' C6 is the cell for the budget
    ' C7 is the cell for the car brand

    ' Declare variables to store the details
    Dim name As String
    Dim birthdate As Date
    Dim budget As String
    Dim carBrand As String

    ' Prompt the user to enter their name
    name = InputBox("What is your name?")

    ' Prompt the user to enter their birthdate
    birthdate = InputBox("What is your birthdate? (MM/DD/YYYY)")
    ' Set the number format for the cell to display the date correctly  
    Range("C5").NumberFormat = "MM/DD/YYYY"

    ' Prompt the user to enter their budget
    budget = InputBox("What is your budget?")
    ' Set the number format for the cell to display the budget correctly
    Range("C6").NumberFormat = "$#,##0.00"

    ' Prompt the user to enter their car brand
    carBrand = InputBox("What is your favorite car brand?")

    ' Fill the form with the details
    Range("C4").Value = name
    Range("C5").Value = birthdate
    Range("C6").Value = budget
    Range("C7").Value = carBrand
End Sub
Sub EditDetails()
    ' Edit the details in the form
    ' C4 is the cell for the name
    ' C5 is the cell for the birthdate
    ' C6 is the cell for the budget
    ' C7 is the cell for the car brand

    ' Declare variables to store the edited details
    Dim name As String
    Dim birthdate As Date
    Dim budget As String
    Dim carBrand As String

    ' Get the current details from the form
    name = Range("C4").Value
    birthdate = Range("C5").Value
    budget = Range("C6").Value
    carBrand = Range("C7").Value

    ' Prompt the user to edit their name
    name = InputBox("Edit your name: " & name)

    ' Prompt the user to edit their birthdate
    birthdate = InputBox("Edit your birthdate: " & birthdate & " (MM/DD/YYYY)")
    ' Set the number format for the cell to display the date correctly  
    Range("C5").NumberFormat = "MM/DD/YYYY"

    ' Prompt the user to edit their budget
    budget = InputBox("Edit your budget: " & budget)
    ' Set the number format for the cell to display the budget correctly
    Range("C6").NumberFormat = "$#,##0.00"

    ' Prompt the user to edit their car brand
    carBrand = InputBox("Edit your favorite car brand: " & carBrand)

    ' Fill the form with the edited details
    Range("C4").Value = name
    Range("C5").Value = birthdate
    Range("C6").Value = budget
    Range("C7").Value = carBrand
End Sub