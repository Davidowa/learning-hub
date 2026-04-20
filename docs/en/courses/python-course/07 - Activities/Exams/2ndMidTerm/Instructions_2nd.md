# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Cpp%20class%20notes%20-%20cpp-class%40GitHub)

**Professor**: Dr. David Escobar Castillejos

## Second Midterm Exam

### Exam Norms

1. **Read Each Question Carefully**: Before answering, ensure you fully understand what is being asked.
2. **No Clarifications During the Exam**: Questions about the exam content will not be addressed once the exam has started.
3. **The Exam Must Be Completed Individually**: Communicating with fellow students during the exam is strictly forbidden and will be considered academic misconduct.
4. The use of cell phones, smartwatches, tablets, or any other electronic devices not explicitly allowed by the instructor is prohibited. Using any of these devices will lead to the invalidation of your exam.
5. If the exam requires the use of computers or specific applications, only those relevant to the exam are permitted. Accessing other applications or files will invalidate your exam.
6. If you use procedures or instructions not covered in class, your answer(s) may be nullified at the instructor's discretion. Discuss any concerns during the exam review session.
7. The exam is valued at 100 points.
8. You have 80 minutes to complete the exam.
9. The exam starts at the scheduled class time, with a grace period for late arrivals not exceeding 10 minutes. Arriving later than this grace period will result in being unable to take the exam.
10. Only files with a ‘.py’ extension named after you (e.g., “JohnDoe.py”) are accepted for evaluation. Files must be created at the start of the exam period and submitted via Moodle.
11. Taking photos or screenshots of the exam is strictly prohibited.
12. Any prohibited behavior will be reported for disciplinary action.
13. If the code provided in the answers does not run correctly in each program due to compilation errors, unexpected results, or if it does not reach the required solution, the program will be graded with 0 points. It is your responsibility to ensure that your code is functional and error-free to meet the question's requirements.

### Additional Guidelines

- **Comments and Documentation**: Include comments throughout your code to explain your logic and decisions. This is especially important for parts of the code that handle text normalization and frequency calculation.
- **Modular Design**: Structure your program with functions to improve readability and maintainability. For example, using separate functions for normalization, splitting text into words, and counting word frequencies can make your code more organized.

### Code of Professional Ethics

Any cases of disciplinary misconduct will be referred to the appropriate Committee in accordance with the General Regulations of Universidad Panamericana (Articles 206 and 207) and the Regulations of the Faculty of Engineering (Articles 86, 206, 207, and 209).

By submitting this file/document with your implementations/answers/development, you affirm that the work carried out is your own. Should it be confirmed otherwise, your work will be nullified; you will be referred to the academic council for review, and the maximum penalty may result in permanent dismissal from the University.

## Programs

You will work with file operations in Python to read and work with the contents from different files.

### Script 1 (25 pts)
1. Read the contents of the text file named `menu.txt`. This file contains the menu items that you will process.
2. Store the contents of the file in a variable. Ensure that the entire content is captured in this variable as a single string or a list of strings, depending on how you choose to read the file.
3. Define a function named `print_menu` that accepts one argument. This argument will be the variable where you stored the file's contents.
4. Inside the `print_menu` function, write code that prints the contents of the menu to the console. 
5. Call the `print_menu` function to display the menu. 

### Script 2 (25 pts)
1. Define a function named `read_numbers` that opens and reads the contents of a file named `values.txt`. This file contains two numbers separated by a dash (-). The function should split these numbers, convert them to integers, and return them as two separate values.
2. Call the `read_numbers` function and store the returned values in two variables, `num1` and `num2`.
3. Define another function named `perform_operations` that takes two parameters. These parameters will be the variables where you stored the numbers from the file.
4. Within the `perform_operations` function, implement code to print the results of the following arithmetic operations:
   1. Addition (`num1` + `num2`).
   2. Subtraction (`num1` - `num2`).
   3. Multiplication (`num1` * `num2`).
   4. Division (`num1` / `num2`).
   5. Modulus (`num1` % `num2`).
5. Call `perform_operations` using `num1` and `num2` as arguments to display the results of the arithmetic operations.

### Script 3 (50 pts)
1. Define a `Videogame` Class:
   - **Attributes:** Include attributes for title, year, genre, and platform.
   - **Methods:**
     - `print_info()`: Prints the complete information of the video game in a readable format.
2. Open and read the contents of `videogames.csv`, where each line contains details such as title, year, genre, and platform.
3. Make a function name `print_list_of_videogames` that takes one argument. This argument is the list of `Videogame` objects and prints each video game's details using the `print_info` method.
4. Make a function name `amount_of_games_per_platform` that takes one argument. This argument is the list of `Videogame` objects and prints the count of video games per platform.
5. Make a function called `add_videogame` that takes one argument. This argument is the list of `Videogame` objects.
   - This function prompts the user for details of a new video game, creates a `Videogame` object, and appends it to the list.
6. Make a function called `update_file` that takes one argument. This argument is the list of `Videogame` objects and writes the updated list of video games back to the `videogames.csv` file.
7. Execute Functions:
   - Call `print_list_of_videogames` to display all video games.
   - Call `amount_of_games_per_platform` to see how many games each platform has.
   - Call `add_videogame` to add a new game to the collection.
   - Call `update_file` to save the updated list to the CSV file.