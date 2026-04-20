# In this code we will create a simple login system using Python
# First let us import the os modules
# This modules is used to interact with the operating system
import os
from login_single_user import login_simple
from login_multiple_users import login_multiple

def clear_console()-> None:
    # Using these modules we can get the OS name
    os_name = os.name
    # We can perform an if to clear the console based on the OS
    # If the OS is Windows, we use the command "cls"
    # If the OS is Linux or Mac, we use the command "clear"

    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear_console()

# Let's use a ternary operator to check if we want to use the multiple user login system
multiple_users = True if input("Do you want to use the multiple user login system? (y/n) ").lower() == "y" else False

if multiple_users:
    login_multiple()
else:
    login_simple()

input("\nPress Enter to exit the program...")

clear_console()