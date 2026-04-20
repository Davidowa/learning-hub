import os

def clear_console()-> None:
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_move(n: int, from_rod: str, to_rod: str) -> None:
    """
    Prints the movement of disks during the Tower of Hanoi puzzle solution.
    It visually represents disks as strings of asterisks.

    Parameters:
    - n: The number of the disk being moved.
    - from_rod: The rod from which the disk is moved.
    - to_rod: The rod to which the disk is moved.
    """
    # Create a string of asterisks (*) to represent the disk being moved
    disk = str('*' * n)
    # Print the action of moving the disk from one rod to another
    print(f"Move disk: {disk} from rod {from_rod} to rod {to_rod}")


def solve_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str) -> None:
    """
    Solves the Tower of Hanoi puzzle for a given number of disks.

    Parameters:
    - n: The total number of disks to be moved.
    - from_rod: The rod to move disks from.
    - to_rod: The rod to move disks to.
    - aux_rod: The auxiliary (helper) rod used in the process.
    """
    # Base case: if there are no disks to move, do nothing
    if n == 0:
        return
    # Move n-1 disks from the starting rod to the auxiliary rod, using the destination rod as a temporary placeholder
    solve_hanoi(n - 1, from_rod, aux_rod, to_rod)
    # Visualize the movement of the nth disk from the starting rod to the destination rod
    print_move(n, from_rod, to_rod)
    # Move the n-1 disks that were placed on the auxiliary rod to the destination rod, using the starting rod as a temporary placeholder
    solve_hanoi(n - 1, aux_rod, to_rod, from_rod)


clear_console()

# Prompt the user to enter the number of disks for the puzzle
n = int(input("Enter the number of disks: "))

# Solve the Tower of Hanoi puzzle for the given number of disks
# 'A', 'B', and 'C' are the names of the three towers
solve_hanoi(n, 'A', 'C', 'B')

input("\nPress Enter to exit the program...")

clear_console()