# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Cpp%20class%20notes%20-%20cpp-class%40GitHub) 

**Professor**: Dr. David Escobar Castillejos

## Login System Program Instructions

### Project 1: Single User Login System

**Objective**: Create a simpler version of the login system that supports a single set of credentials. The program should authenticate the user and provide access to a basic user menu.

#### Core Features:

1. **Login**: Prompt the user for a username and password. If the credentials match the pre-set values, grant access to the user menu.
2. **User Menu**: After login, display a simple menu welcoming the user and offering the option to log off.

#### Implementation Details:

- Store the single set of user credentials (username and password) directly in the code.
- Ensure the program handles incorrect login attempts gracefully.
- Provide a clear, concise menu for logging in and navigating the user menu.

### Project 2: Multiple User Login System

**Objective**: Implement a program that manages multiple user logins, allowing the addition, modification, and deletion of user credentials, as well as authenticating users.

#### Core Features:

1. **Add User**: Prompt for a username and password, then store these credentials. Ensure no duplicate usernames are allowed.
2. **Edit User**: Allow modifying the password of an existing user. Provide options to edit by username or by selecting from a list.
3. **Remove User**: Enable the deletion of a user's credentials based on the username.
4. **Login**: Authenticate a user based on the provided username and password.
5. **List Users**: Display a list of all usernames currently stored in the system.

#### Implementation Details:

- Store usernames and passwords as collections.
- Implement a simple, text-based menu system that guides the user through the various operations (add, edit, delete, login).
  
### General Requirements for Both Projects:

- **Clear Console**: Before displaying any menu or prompt, clear the console screen to keep the output clean and readable.
- **Comments**: Include comments throughout your code to explain the functionality of each section and any important variables.
  
### Deliverables:

- Submit the complete source code for both the multiple user and single user login systems.
- Ensure your code is well-commented and adheres to the specified features and implementation details.