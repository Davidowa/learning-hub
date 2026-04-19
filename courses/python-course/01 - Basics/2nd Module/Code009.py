# Repetition Statements: for loop

# Lets imagine that we want to print "Send message" 4 times
# We can do it like this
print("Send message")
print("Send message")
print("Send message")
print("Send message")

# However, this is not efficient
# Imagine that we want to print "Send message" 100 times

# We can use repetition statements to do this
# Repetition statements are used to execute a piece of code multiple times
# There are two types of repetition statements
# for loop
# while loop

# for loop
# The for loop is used to iterate a block of code a specific number of times
# Lets see an example
for number in range(10):
    print("Attempt", number, number * ".")

# When we use range(10), the sequence will be from 0 to 9
# The variable number will take the value of each element in the sequence
# In the first iteration, number will be 0
# In the second iteration, number will be 1
# And so on
# The code inside the for loop will be executed each time the variable number takes a new value until the sequence ends
# In this case, the code inside the for loop will be executed 9 times
# The output will be:
# Attempt 0
# Attempt 1 .
# Attempt 2 ..
# ...
# Attempt 8 ........
# Attempt 9 .........

# When we use the range function, we can specify the start, stop and step arguments
# Lets see an example
for number in range(5, 10, 2):
    print("Attempt", number, number * ".")
# In this case, the sequence will start at 5, and it will end at 9
# The step argument is 2, so the sequence will be 5, 7, 9
# The output will be:
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........

# We can also use the for loop to iterate over a string
# Lets see an example

for character in "Python":
    print(character)  # P y t h o n

# In this case, the code inside the for loop will be executed 6 times
# The first time, the variable character will be equal to P
# The second time, the variable character will be equal to y
# And so on

# Special case: For else loop
# We can use the else keyword with the for loop
# The code inside the else block will be executed after the for loop ends
# Lets see an example

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# In this case, the code inside the for loop will be executed 1 time because the break statement is executed as successful is True

# Lets change the value of successful to False
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# In this case, the code inside the for loop will be executed 3 times because the break statement is not executed as successful is False
# And because the break statement is not executed, the code inside the else block will be executed

# while loop
# The while loop is used to iterate a block of code while a condition is True
# Lets see an example
number = 100
while number > 0:
    print(number)
    number //= 2

# In this case, the code inside the while loop will be executed 7 times because the number variable will be divided by 2 each time the code inside the while loop is executed
# The output will be:
# 100
# 50
# 25
# 12
# 6
# 3
# 1

# The while is used when we don't know how many times we want to execute a piece of code, but we know the condition that will stop the execution

# Special case: While else loop
# We can also use the else keyword with the while loop
# The code inside the else block will be executed after the while loop ends
# Lets see an example
number = 100
while number > 0:
    print(number)
    number //= 2
else:
    print("Loop ended")

# In this case, the code inside the while loop will be executed 7 times because the number variable will be divided by 2 each time the code inside the while loop is executed
# The output will be:
# 100
# 50
# 25
# 12
# 6
# 3
# 1
# Loop ended


# Nested loops
# We can use loops inside other loops
# Lets see an example
for x in range(2):
    for y in range(3):
        print(f"({x}, {y})")

# In this case, the code inside the inner loop will be executed 3 times for each iteration of the outer loop, which is executed 2 times
# The output will be:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)

# We have seen the break statement, but also we have the continue statement and the pass statement
# break statement
# The break statement is used to stop the execution of a loop
# Lets see an example
for number in range(5):
    if number == 3:
        break
    print(number)

# In this case, the code inside the for loop will be executed 3 times
# The output will be:
# 0
# 1
# 2

# continue statement
# The continue statement is used to skip the current iteration of a loop
# Lets see an example
for number in range(5):
    if number == 3:
        continue
    print(number)

# In this case, the code inside the for loop will be executed 4 times
# The output will be:
# 0
# 1
# 2
# 4

# pass statement
# The pass statement is used to do nothing
# Lets see an example
for number in range(5):
    if number == 3:
        pass
    print(number)

# In this case, the code inside the for loop will be executed 5 times
# The output will be:
# 0
# 1
# 2
# 3
# 4

# We have something that is called iterable
# An iterable is an object that can be iterated over
# The first iterable that we have seen is the range function
# Lets see an example
for number in range(5):
    print(number)  # 0 1 2 3 4

# In this case, the range function is an iterable
# We can also iterate over a string
# Lets see an example
for character in "Python":
    print(character)  # P y t h o n

# In this case, the string is an iterable

# Iterable are objects that can be iterated over

# Last thing: infinite loops
# An infinite loop is a loop that never ends
# Lets see an example
# while True:
#    print("Hello")

# In this case, the code inside the while loop will be executed forever

# To stop the execution, we can use the break statement
# Lets see an example
while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# Or we can write
command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
