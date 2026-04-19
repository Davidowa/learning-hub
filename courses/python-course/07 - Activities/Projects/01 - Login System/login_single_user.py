import os

def clear_console()-> None:
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main_menu() -> None:
    print("Simple Login Form")
    print("1.- Access the System")
    print("2.- Exit")


def login_menu(user: str, passw: str) -> None:
    clear_console()
    print("Login Menu")
    usern = input("Input the username: ")
    userp = input("Input the password: ")

    if usern == user and userp == passw:
        user_menu(user)
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


def login_simple() -> None:
    username = "admin"
    password = "1234"

    program_running = True

    while program_running:
        clear_console()
        main_menu()
        user_option = int(input("Option: "))
        if user_option == 1:
            login_menu(username, password)
        elif user_option == 2:
            program_running = False
            print("Closing the program... Bye!")
        else:
            input("Option not valid... Press enter to continue...")

