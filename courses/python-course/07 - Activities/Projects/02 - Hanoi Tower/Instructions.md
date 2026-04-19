# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Cpp%20class%20notes%20-%20cpp-class%40GitHub) 

**Professor**: Dr. David Escobar Castillejos

## Tower of Hanoi Solver Program Instructions

**Objective**: Implement a program that solves the Tower of Hanoi puzzle for three disks. The program should visually represent each move in the solution process.

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

### Requirements:

- **`clear_console`**: Clears the console screen. This function should check the operating system for compatibility (`nt` for Windows, otherwise assume Unix/Linux).

- **`print_move`**:
  - Parameters: `n = 3` (disk number), `from_rod`, `to_rod`
  - Purpose: Print the action of moving a disk from one rod to another. Represent disks as strings of asterisks (`*`). For instance, disk 1 as `*`, disk 2 as `**`, and so on.

- **`solve_hanoi`**:
  - Parameters: `n` (total number of disks), `from_rod`, `to_rod`, `aux_rod` (auxiliary or helper rod)
  - Purpose: Recursively solve the Tower of Hanoi puzzle. Use the base case of `n == 0` (no disks to move) to stop the recursion. Follow the puzzle rules to move disks between rods.

- **Comments**: Include comments explaining the logic behind each function, especially the recursive solution in `solve_hanoi`.

### User Interaction

- At the start, prompt the user that the program will solve the puzzle using three disks.
- Use the `solve_hanoi` function to display each move required to solve the puzzle.
- After completing the puzzle, prompt the user to press Enter to exit the program.

### Deliverables:

- Submit the complete source code.
- Ensure your code is well-commented and adheres to the specified features and implementation details.