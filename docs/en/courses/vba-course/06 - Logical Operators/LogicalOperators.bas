Sub LogicalOperators()
    ' In this lesson, we are going to cover the logical operators in VBA.
    ' Logical operators are used to combine two or more conditions.
    ' There are three logical operators in VBA:
    ' And
    ' Or
    ' Not
    ' The result of a logical operation is a Boolean value, which is a type of data that can be either True or False.
    ' The logical operators are used to create complex conditions that can be evaluated as True or False.

    ' Before we start, let's see a concept that is important to understand the logical operators.
    ' The concept is the truth table.
    ' A truth table is a table that shows the result of a logical operation for all possible combinations of input values.
    ' The truth table for the And operator is:
    ' True And True = True
    ' True And False = False
    ' False And True = False
    ' False And False = False

    ' The truth table for the Or operator is:
    ' True Or True = True
    ' True Or False = True
    ' False Or True = True
    ' False Or False = False

    ' The truth table for the Not operator is:
    ' Not True = False
    ' Not False = True

    ' Part 1: And Operator
    ' The And operator is used to combine two or more conditions.
    ' The result of the And operation is True only if all the conditions are True.
    ' In the following lines, we use the And operator to combine two or more conditions.
    ' The result of the And operation is assigned to a variable.
    Dim m As Integer
    Dim n As Integer
    Dim o As Boolean
    m = 5
    n = 10
    o = m > 0 And n < 20
    MsgBox "Is m greater than 0 and n less than 20? " & o

    ' Part 2: Or Operator
    ' The Or operator is used to combine two or more conditions.
    ' The result of the Or operation is True if at least one of the conditions is True.
    ' In the following lines, we use the Or operator to combine two or more conditions.
    ' The result of the Or operation is assigned to a variable.
    Dim p As Integer
    Dim q As Integer
    Dim r As Boolean
    p = 5
    q = 10
    r = p < 0 Or q > 20
    MsgBox "Is p less than 0 or q greater than 20? " & r

    ' Part 3: Not Operator
    ' The Not operator is used to negate a condition.
    ' The result of the Not operation is True if the condition is False, and False if the condition is True.
    ' In the following lines, we use the Not operator to negate a condition.
    ' The result of the Not operation is assigned to a variable.
    Dim s As Integer
    Dim t As Boolean
    s = 5
    t = Not s > 0
    MsgBox "Is s not greater than 0? " & t

    ' In each of the examples, we used the logical operators to combine two conditions.
    ' If you want to combine more than two conditions, you have to use parentheses to group the conditions.
    ' For example, if you want to combine three conditions using the And operator, you can write:
    ' result = (condition1 And condition2) And condition3
    ' This way, the conditions condition1 and condition2 are evaluated first, and then the result is combined with condition3.
    ' Depending on the complexity of the conditions, you may need to use parentheses to group the conditions in the way you want.

    ' Part 4: Combining Logical Operators
    ' You can also combine the logical operators to create complex conditions.
    ' In the following lines, we use the And and Or operators to combine multiple conditions.
    ' The result of the combined conditions is assigned to a variable.
    Dim u As Integer
    Dim v As Integer
    Dim w As Integer
    Dim x As Boolean
    u = 5
    v = 10
    w = 15
    x = (u > 0 And v < 20) Or w = 15
    MsgBox "Is u greater than 0 and v less than 20, or w equal to 15? " & x

    ' The condition is evaluated as True if either the first condition (u > 0 And v < 20) or the second condition (w = 15) is True.
    ' The parentheses are used to group the conditions in the way we want.

    ' Using both comparison and logical operators, you can create complex conditions that can be evaluated as True or False.
    ' Moreover, they are useful when you combine them with control structures (conditional statements and repetition statements) to control the flow of the program.

End Sub