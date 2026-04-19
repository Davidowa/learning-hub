# Scope of variables

# In this example, we define a function named myFunction, which defines a variable named message
# This variable is local to the function
# That means that we can't access it outside the function or it only exists within the function
# If we try to access it outside the function, we get an error
# Example

def myFunction():
    message = "Hello World"


myFunction()
# print(message) # We will get the following error - 'message' is not defined

# These also happen with parameters
# Example


def myFunction2(phrase):
    print(phrase)


# print(phrase) # We will get the following error - 'phrase' is not defined

# These local variables exist only while the function is being executed, so they have a short lifetime

# In contrast, global variables exist throughout the program, so they have a long lifetime
# Usually, the variables that we define outside functions are global variables

# Example

message = "a"


def myFunction3():
    message = "b"


print(message)  # We will get 'a' because the global variable is printed

# The interpreter will look for the variable in the local scope first, and if it doesn't find it, it will look for it in the global scope
# Because the local variable does not exists (as the function was not called), the global variable is printed
# To change the value of a global variable inside a function, we need to use the global keyword

message = "a"


def myFunction4():
    # We use the global keyword to tell the interpreter that we want to use the global variable
    # so we can change its value and do not create a local variable
    global message
    message = "b"


myFunction4()
# We will get 'b' because the global variable was changed in the function
print(message)

# However, it is not recommended to use global variables, because they make the code harder to understand
# Moreover, you may have multiple functions that use the same global variable, and it will be hard to debug
# Or you can accidentally change the value of a global variable in a function, which can cause unexpected behavior
