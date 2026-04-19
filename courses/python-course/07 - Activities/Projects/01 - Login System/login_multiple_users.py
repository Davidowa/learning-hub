import os

def clear_console()-> None:
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main_menu() -> None:
    print("Simple Login Form")
    print("0.- Add user to the System")
    print("1.- Edit user to the System")
    print("2.- Remove user to the System")
    print("3.- Access the System")
    print("4.- Exit")


def add_user_menu(usernames: list, passws: list) -> tuple:
    clear_console()
    print("Add User Menu")
    usern = input("Input the new username: ")
    userp = input("Input the new password: ")

    # Using the in statement, Python checks an iterable element
    # in this case a list, and if the value is in the iterable
    # return True, else returns False
    user_in_list = usern in usernames

    if user_in_list != True:
        usernames.append(usern)
        passws.append(userp)
    else:
        input("Username is already in the system. Press enter to continue...")

    return usernames, passws
    # (usernames, passws)


def edit_user_by_name_menu(usernames: list, passws: list) -> tuple:
    print()
    usern = input("Input the username to edit: ")

    # Obtain the index of the user IF it is inside the list
    # In this case, we are going to use the index method
    # The index method returns the index of the first occurrence
    # However, if the value is not in the list, the method raises an error
    # Therefore, we are going to use a new concetp called exception handling
    # The exception handling is a way to handle errors in Python
    # The syntax is the following:
    # try:
    #     # Code that may raise an error
    # except:
    #     # Code to handle the error

    # Let us use the exception handling to handle the error
    # The ValueError is raised when a value is not found in a list
    # There are different types of errors in Python, and each one has a different
    # name and message, so we can handle them in different ways.
    # You can find the list of errors in the official documentation of Python
    # Link: https://docs.python.org/3/library/exceptions.html
    try:
        userp = input("Input the new password: ")
        index = usernames.index(usern)
        passws[index] = userp
        input("User edited. Press enter to continue...")
    except ValueError:
        input("Username not found. Press enter to continue...")

    return usernames, passws
    # (usernames, passws)


def edit_user_by_index_menu(usernames: list, passws: list) -> tuple:
    print()
    print("Users in the system:")
    for i in range(0, len(usernames), 1):
        print(f"{i+1}.- {usernames[i]}")
    index = int(input("Input the user to edit: "))
    index -= 1
    # Let use the exception handling to handle the error again
    # This time we are going to use the IndexError, which is raised
    # when an index to access a element of a numbered collection is out of range
    try:
        userp = input("Input the new password: ")
        passws[index] = userp
        input("User edited. Press enter to continue...")
    except IndexError:
        input("Index not found. Press enter to continue...")
    return usernames, passws
    # (usernames, passws)


def edit_user_menu(usernames: list, passws: list) -> tuple:
    
    user_menu_running = True
    while user_menu_running:
        clear_console()
        print("Edit User Menu")
        print("1.- Edit user by name")
        print("2.- Edit user by index")
        print("3.- Return to the main menu")
        user_option = int(input("Option: "))
        if user_option == 1:
            usernames, passws = edit_user_by_name_menu(usernames, passws)
        elif user_option == 2:
            usernames, passws = edit_user_by_index_menu(usernames, passws)
        elif user_option == 3:
            user_menu_running = False
            input("Returning to the main menu... Press enter to continue...")
        else:
            input("Option not valid... Press enter to continue...")
    return usernames, passws
    # (usernames, passws)
    

def remove_user_menu(usernames: list, passws: list) -> tuple:
    clear_console()
    print("Remove User Menu")
    usern = input("Input the username to remove: ")
    user_in_list = usern in usernames
    if user_in_list == True:
        index = usernames.index(usern)
        usernames.pop(index)
        passws.pop(index)
        input("User removed. Press enter to continue...")
    else:
        input("Username not found. Press enter to continue...")
    return usernames, passws
    # (usernames, passws)


def login_menu(user: list, passw: list) -> None:
    clear_console()
    print("Login Menu")
    usern = input("Input the username: ")
    userp = input("Input the password: ")

    # Obtain the index of the user IF it is inside the list
    index = -1
    for i in range(0, len(user), 1):
        if user[i] == usern:
            index = i
            break
    
    if index != -1:
        if usern == user[index] and userp == passw[index]:
            user_menu(user[index])
        else:
            input("Wrong user or password. Press enter to continue...")
    else:
        input("Wrong user or password. Press enter to continue...")


def user_menu(user: str) -> None:
    user_login = True

    while user_login:
        clear_console()
        print("User Menu")
        print(f"Welcome {user}!")
        print("1.- Log off")
        user_option = int(input("Option: "))
        if user_option == 1:
            user_login = False
            input("Login off... Press enter to continue...")
        else:
            input("Option not valid... Press enter to continue...")


def login_multiple() -> None:
    username_list = []
    password_list = []
    program_running = True

    while program_running:
        clear_console()
        main_menu()
        user_option = int(input("Option: "))
        if user_option == 0:
            username_list, password_list = add_user_menu(username_list, password_list)
        elif user_option == 1:
            username_list, password_list = edit_user_menu(username_list, password_list)
        elif user_option == 2:
            username_list, password_list = remove_user_menu(username_list, password_list)
        elif user_option == 3:
            login_menu(username_list, password_list)
        elif user_option == 4:
            program_running = False
            print("Closing the program... Bye!")
        else:
            input("Option not valid... Press enter to continue...")
