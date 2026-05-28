Sub ArithmeticOperators()
    ' In this lesson, we are going to cover the basic arithmetic operators in VBA.
    ' These operators are used to perform mathematical operations.
    
    ' Part 1: Addition
    ' The addition operator (+) is used to add two numbers together.
    ' In this example, we add 5 and 3 together and display the result in a message box.
    MsgBox 5 + 3
    
    ' Part 2: Subtraction
    ' The subtraction operator (-) is used to subtract one number from another.
    ' In this example, we subtract 5 from 3 and display the result in a message box.
    MsgBox 5 - 3
    
    ' Part 3: Multiplication
    ' The multiplication operator (*) is used to multiply two numbers together.
    ' In this example, we multiply 5 by 3 and display the result in a message box.
    MsgBox 5 * 3
    
    ' Part 4: Division
    ' The division operator (/) is used to divide one number by another.
    ' In this example, we divide 5 by 3 and display the result in a message box.
    MsgBox 5 / 3
    
    ' Part 5: Exponentiation
    ' The exponentiation operator (^) is used to raise a number to a power.
    ' In this example, we raise 5 to the power of 3 and display the result in a message box.
    MsgBox 5 ^ 3
    
    ' Part 6: Integer Division
    ' The integer division operator (\) is used to divide one number by another and return the integer part of the result.
    ' In this example, we divide 5 by 3 and display the integer part of the result in a message box.
    MsgBox 5 \ 3
    
    ' Part 7: Modulus
    ' The modulus operator (Mod) is used to divide one number by another and return the remainder.
    ' In this example, we divide 5 by 3 and display the remainder in a message box.
    MsgBox 5 Mod 3
    
    ' Part 8: Order of Operations
    ' When performing multiple operations in a single expression, VBA follows the order of operations.
    ' The order of operations is as follows:
    ' 1. Parentheses
    ' 2. Exponents
    ' 3. Multiplication and Division (from left to right)
    ' 4. Addition and Subtraction (from left to right)

    ' In this example, we use parentheses to change the order of operations and display the result in a message box.
    MsgBox (5 + 3) * 2
    ' The result of this expression is 16, not 26, because the addition inside the parentheses is performed first.
    ' Then, the result is multiplied by 2.

    ' In the examples above, we used the operators directly in the MsgBox function to display the results.
    ' However, in programming, we often use operators to perform calculations between variables and store the results in other variables.
    ' The main reason we store the results in variables is to use them later in the code, as we usually do not want to display the results immediately.

End Sub