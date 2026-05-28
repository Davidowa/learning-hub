Sub ComparissonOperators()
' In this lesson, we are going to cover the comparison operators in VBA.
' Comparison operators are used to compare two values.
' The result of a comparison is a Boolean value, which is a type of data that can be either True or False.
' The comparison operators are:
' - Equal to: =
' - Not equal to: <>
' - Greater than: >
' - Less than: <
' - Greater than or equal to: >=
' - Less than or equal to: <=

' Part 1: Equal to
' The equal to operator is used to compare if two values are equal.
' If the values are equal, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, a and b.
' The result of the comparison is assigned to the variable c.
Dim a As Integer
Dim b As Integer
Dim c As Boolean
a = 5
b = 5
c = a = b
MsgBox "Is a equal to b? " & c

' Part 2: Not equal to
' The not equal to operator is used to compare if two values are different.
' If the values are different, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, d and e.
' The result of the comparison is assigned to the variable f.
Dim d As Integer
Dim e As Integer
Dim f As Boolean
d = 5
e = 10
f = d <> e
MsgBox "Is d different from e? " & f

' Part 3: Greater than
' The greater than operator is used to compare if a value is greater than another value.
' If the first value is greater than the second value, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, g and h.
' The result of the comparison is assigned to the variable i.
Dim g As Integer
Dim h As Integer
Dim i As Boolean
g = 5
h = 10
i = g > h
MsgBox "Is g greater than h? " & i

' Part 4: Less than
' The less than operator is used to compare if a value is less than another value.
' If the first value is less than the second value, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, j and k.
' The result of the comparison is assigned to the variable l.
Dim j As Integer
Dim k As Integer
Dim l As Boolean
j = 5
k = 10
l = j < k
MsgBox "Is j less than k? " & l

' Part 5: Greater than or equal to
' The greater than or equal to operator is used to compare if a value is greater than or equal to another value.
' If the first value is greater than or equal to the second value, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, m and n.
' The result of the comparison is assigned to the variable o.
Dim m As Integer
Dim n As Integer
Dim o As Boolean
m = 5
n = 5
o = m >= n
MsgBox "Is m greater than or equal to n? " & o

' Part 6: Less than or equal to
' The less than or equal to operator is used to compare if a value is less than or equal to another value.
' If the first value is less than or equal to the second value, the result is True. Otherwise, the result is False.
' In the following lines, we compare the values of two variables, p and q.
' The result of the comparison is assigned to the variable r.
Dim p As Integer
Dim q As Integer
Dim r As Boolean
p = 5
q = 10
r = p <= q
MsgBox "Is p less than or equal to q? " & r

' Comparrison operators can be used to compare different types of data, such as numbers, strings, and dates. 
' These are useful to create conditions in VBA, which are used to control the flow of the program.
' In the next lesson, we will cover the logical operators, which are used to combine multiple conditions.
End Sub