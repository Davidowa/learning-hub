# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Cpp%20class%20notes%20-%20cpp-class%40GitHub) 

**Professor**: Dr. David Escobar Castillejos

## Contact Book Program Instructions

**Objective**: Write a program that simulates a contact book. The program must support operations to manage contact information effectively, ensuring ease of use and data integrity.

### Requirements:

1. **Data Structure**: Use a dictionary to store contact details. Each contact's name should serve as a unique key, and its value should be another dictionary or a tuple containing the phone number and email address. For example: `contacts = {"John Doe": {"phone": "123-456-7890", "email": "john.doe@example.com"}}`
2. **Ensure Uniqueness**: Ensure that each contact name is unique within the contact book. Treat the contact name as a case-sensitive identifier to simplify this requirement.
3. **Save a Contact**:
   - Prompt the user to enter the name, phone number, and email of the new contact.
   - Check if the contact name already exists in the contact book. If it does, inform the user and abort the operation; otherwise, save the new contact.
4. **Update a Contact**:
   - Ask the user for the contact name they wish to update.
   - Verify that the contact exists. If not, display a suitable message.
   - If the contact exists, prompt for the new phone number and email, and update the contact's details accordingly.
5. **Delete a Contact**:
   - Request the contact name to delete.
   - Check if the contact exists. If it does, delete the contact; otherwise, notify the user that the contact was not found.
6. **List All Contacts**:
   - Display a list of all saved contacts, along with their phone numbers and emails. Ensure the list is presented in a readable format, such as:
     ```python
     Contact Name: John Doe
     Phone Number: 123-456-7890
     Email: john.doe@example.com
     ```
   - If there are no contacts, indicate that the contact book is empty.
7. **User Interface**: Implement a simple text-based menu system that allows users to choose actions (e.g., add, update, delete, list contacts) and quit the program.

### Deliverables:

- Submit the complete source code.
- Ensure your code is well-commented and adheres to the specified features and implementation details.