# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Cpp%20class%20notes%20-%20cpp-class%40GitHub) 

**Professor**: Dr. David Escobar Castillejos

## Student Score Analysis Program Instructions

**Objective**: Develop a program that analyzes two lists of students from two different classes, where each student is associated with a score. The program should calculate the average score for each class, identify students present in both classes and calculate their combined average score, and also calculate the average score for students unique to their respective classes.

## Overview

This exercise involves working with dictionaries to store and process student data, including names and scores. It requires parsing raw data, performing arithmetic operations to calculate averages, and identifying common and unique students between two classes.

### Requirements

### Data Structure

- Each student's information should be stored in a dictionary, with keys for the student's name and score.
- Having these two lists, each containing 30 dictionaries for the students in each class. Ensure there are overlapping students between the two lists to simulate common students.

- Class 1 Raw Data
  ```python
  '''
  John Doe, 85
  Jane Smith, 78
  Michael Brown, 92
  Emily Johnson, 88
  Daniel Wilson, 74
  Olivia Jones, 95
  William Garcia, 81
  Ava Martinez, 87
  Isabella Rodriguez, 90
  Sophia Anderson, 77
  Mason Lee, 83
  Ella Young, 79
  James Hernandez, 84
  Charlotte Gonzalez, 91
  Benjamin Perez, 75
  Amelia Lopez, 89
  Ethan White, 93
  Mia Thompson, 80
  Alexander Harris, 85
  Aria Clark, 82
  Henry Lewis, 76
  Evelyn Walker, 94
  Sebastian Hall, 72
  Abigail Allen, 86
  Liam Scott, 78
  Sophie Adams, 73
  Oscar Nelson, 88
  Luna King, 91
  Jack Wright, 79
  Lucas Green, 84
  '''
  ```
- Class 2 Raw Data
  ```python
  '''
  Isaac Moore, 89
  Eva Turner, 88
  Nathan Martin, 76
  Grace Hill, 92
  Samuel Adams, 85
  Zoe Davis, 81
  Aiden Robinson, 87
  Chloe Campbell, 90
  Gabriel Mitchell, 77
  Lily Anderson, 83
  Jane Smith, 82
  Emily Johnson, 90
  Daniel Wilson, 78
  Olivia Jones, 97
  Ella Young, 81
  Charlotte Gonzalez, 89
  Amelia Lopez, 91
  Mia Thompson, 82
  Alexander Harris, 88
  Sophia Anderson, 79
  Lucas Green, 86
  Jack Wright, 82
  Luna King, 93
  Oscar Nelson, 90
  Sophie Adams, 75
  Liam Scott, 80
  Henry Lewis, 88
  Aria Clark, 84
  Ethan White, 95
  Benjamin Perez, 77
  '''
  ```

### Core Functionality

- **Parse Raw Data**: Convert the provided raw data into structured dictionaries within two separate lists.
- **Calculate Average Scores**:
  - Calculate and display the average score for each class.
  - Identify students who are present in both classes and calculate their average score.
  - For students unique to each class, calculate and display the average score for each class.
  - Identify students across both classes (those who are only in one class and not the other), calculate and display the average score for this combined group.

#### Additional Guidelines

- **Comments and Documentation**: Include comments throughout your code explaining your logic and decisions. This is especially important for parts of the code that handle text normalization and frequency calculation.
- **Modular Design**: Structure your program with functions to improve readability and maintainability. For example, separate functions for normalization, splitting text into words, and counting word frequencies can make your code more organized.

### Deliverables

- Submit the complete source code.
- Ensure your code is well-commented and adheres to the specified features and implementation details.