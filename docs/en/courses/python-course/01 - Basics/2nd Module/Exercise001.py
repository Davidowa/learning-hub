# Exercises

################
# Basic
################
# Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Sum of First N Numbers
n = int(input("Enter n: "))
total = 0
for i in range(n+1):
    total += i
print(total)

# Print Numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Factorial of a Number
n = int(input("Enter n: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial)

# Check if a Number is Prime
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")

# Reverse a String
text = input("Enter text: ")
reversed_text = text[::-1]
print(reversed_text)

# Count Vowels in a String
text = input("Enter text: ").lower()
count = 0
for char in text:
    if char in 'aeiou':
        count += 1
print(count)

# Find Maximum of Three Numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# Temperature Converter (Celsius to Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}C is {fahrenheit}F")

################
# Intermediate
################
# Sum of Digits of a Number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("Sum of digits:", sum)

# Count Number of Digits in an Input Number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

# Reverse a Number
num = int(input("Enter a number: "))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print("Reversed Number:", reverse_num)

# Find the Largest and Smallest Digits in a Number
num = int(input("Enter a number: "))
min_digit = 9
max_digit = 0
while num > 0:
    digit = num % 10
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
    num //= 10
print("Smallest digit:", min_digit)
print("Largest digit:", max_digit)

# Check Whether a Number is Palindrome or Not
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
if original_num == reversed_num:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# Print Multiplication Table of a Given Number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Calculate the Sum of Natural Numbers
n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"Sum of first {n} natural numbers is: ", sum)

# Count Number of Words in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
print("Number of words:", len(words))

# Print a Triangle Pattern
n = int(input("Enter height of triangle: "))
for i in range(n):
    print(' ' * (n-i-1) + '*' * (2*i+1))


################
# Advanced
################

# Generate Fibonacci Sequence
n = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a+b

# Check for Armstrong Number (A number is called an Armstrong number if it is equal to the sum of its own digits raised to the power of the number of digits.)
num = int(input("Enter a number: "))
temp = num
sum = 0
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if num == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Perfect Number Check (A perfect number is a number that is the sum of its own positive divisors excluding itself.)
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")

# Number Pattern: Diamond Shape
n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(n - i - 1):
        print(end=" ")
    for j in range(i + 1):
        print(j + 1, end="")
    print()

for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(end=" ")
    for j in range(i + 1):
        print(j + 1, end="")
    print()

# Print the Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

# Reverse Words in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
reversed_sentence = ' '.join(reversed(words))
print(reversed_sentence)

# Check if a Year is Leap Year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Print Prime Numbers in a Range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print(num, end=" ")
