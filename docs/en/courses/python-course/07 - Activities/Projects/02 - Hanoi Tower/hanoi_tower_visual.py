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

    Parameters:
    - n: The number of the disk being moved.
    - from_rod: The rod from which the disk is moved.
    - to_rod: The rod to which the disk is moved.
    """
    print(f"Move disk: {'*' * n} from rod {from_rod} to rod {to_rod}")


def print_towers(towers: list[list[str]]) -> None:
    """
    Prints the current state of the towers.

    Parameters:
    - towers: A list of lists representing the towers and their disks.
    """
    maxHeight = max(len(tower) for tower in towers)
    for i in range(maxHeight - 1, -1, -1):
        for tower in towers:
            if i < len(tower):
                print(f"{tower[i]}\t", end="")
            else:
                print("|\t", end="")
        print()
    print("-----------------")


def solve_hanoi(n: int, from_rod: str, to_rod: str, aux_rod: str, towers: list[list[str]]) -> None:
    """
    Solves the Tower of Hanoi puzzle.

    Parameters:
    - n: The total number of disks to move.
    - from_rod: The starting rod.
    - to_rod: The destination rod.
    - aux_rod: The auxiliary rod.
    - towers: The current state of the towers.
    """
    if n == 0:
        return
    solve_hanoi(n - 1, from_rod, aux_rod, to_rod, towers)

    # Perform the actual move
    disk = towers[ord(from_rod) - ord('A')].pop()
    towers[ord(to_rod) - ord('A')].append(disk)
    print_move(n, from_rod, to_rod)
    print_towers(towers)

    solve_hanoi(n - 1, aux_rod, to_rod, from_rod, towers)


clear_console()

n = int(input("Enter the number of disks: "))
towers = [[str('*' * i) for i in range(n, 0, -1)], [], []]

print("Initial state:")
print_towers(towers)

print("\nSteps:\n")
solve_hanoi(n, 'A', 'C', 'B', towers)

input("\nPress Enter to exit the program...")

clear_console()
