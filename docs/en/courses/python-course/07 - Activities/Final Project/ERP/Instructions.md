# Python Programming Course

![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:descobarc@up.edu.mx?subject=Python%20class%20Final%20Project)

**Professor**: Dr. David Escobar Castillejos

## ERP - Sales System Program

**Objective**: 
Develop an Python-based application using PyQt for the graphical user interface and SQLite3 for database management. The program will function as a basic ERP system tailored specifically for managing sales, products, and user roles.

### Overview & Requirements
The project involves creating an ERP system that handles various sales-related activities. The system should be designed with usability and functional clarity in mind, allowing users with different roles to perform specific tasks according to their permissions.

#### Data Structure
You will design and implement the following data classes:

- Users: This class should capture user details. Each user will have the following attributes:
  - id (int): A unique identifier.
  - username (str): The user's login name.
  - password (str): The user's password for system access.
  - role (str): The user's role within the system (e.g., Admin, Salesman).
  - name (str): The user's first name.
  - lastname (str): The user's last name.
  - date_joined (date): The date the user was added to the system.

- Clients: Information about clients who purchase products.
  - id (int): Unique client identifier.
  - name (str): Client's full name.
  - RFC (str): Tax identification number.
  - fiscal_regimen_id (int): Associated tax regimen ID.
  - address (str): Full address.
  - city (str): City of residence.
  - state (str): State of residence.
  - zip_code (str): Postal code of the client's address.
  
- FiscalRegimen 
  - id (int): Unique tax regimen identifier.
  - code (int): tax regime's code. 
  - name (str): tax regime's name.

- Product: Basic information about the products.
  - id (int): Unique product identifier.
  - UPC (str): Universal Product Code.
  - name (str): Product name.
  - id_presentation (int): Associated presentation ID.
  - price (float): Price of the product.
  - cost (float): Cost per unit.
  - has_iva (bool): Whether the product price includes VAT (Value Added Tax).
  - stock (int): Quantity available.

- Presentation: Describes the type of product presentation.
  - id (int): Unique identifier.
  - name (str): Name of the presentation (e.g., bottle, box).

- Sale: Records details of sales transactions.
  - id (int): A unique identifier for each sale transaction. 
  - date_of_sale (datetime): The date and time when the sale was completed.
  - user_id (int): The identifier of the seller who processed the sale. 
  - client_id (int): The identifier of the client who made the purchase. 
  - total_amount (float): The total monetary amount of the sale. 
  
- ProductSold:
  - id (int): A unique identifier for each product sold record.
  - id_sale (int): The identifier of the sale this product is associated with.
  - id_product (int): The identifier of the product that has been sold. 
  - quantity (int): The number of units of the product sold in this particular transaction.
  - sale_price_per_unit (float): The price at which each unit of the product was sold.

### Core Functionality

The core functionality of your ERP - Sales System Program will include features that allow users to manage sales, products, clients, and user roles efficiently. Here's a breakdown of the essential functions your system will provide:

#### Default Administrator Account
Upon first launch, the system will automatically create a default user account with administrative privileges. This default account can be used to access the system initially and set up additional user accounts and configurations. The details for the default administrator account are as follows:

- Username: admin
- Password: admin

#### User Management

- **Add User**: Allows administrators to create new user accounts by entering details such as username, password, role, name, and lastname. The system will automatically assign a unique identifier and capture the date the user was added.
- **Edit User**: Enables modifications to existing user details. Administrators can update any information related to a user except for the unique identifier.
- **View Users**: Display a list of all users in the system with their relevant details. This view can be filtered by role, username, or name.
- **Delete User**: Remove a user from the system. This function should include a confirmation step to prevent accidental deletions.

#### Client Management

- **Add Client**: Input new client information including name, RFC, fiscal regimen, address, city, state, and zip code. Each client will receive a unique identifier automatically.
- **Edit Client**: Update existing client details. Users can change any information except for the unique identifier.
- **View Clients**: Show a comprehensive list of all clients with complete details. This feature might include search and filter capabilities based on name, city, or state.
- **Delete Client**: Safely remove a client's record from the database, with a confirmation prompt to ensure the action is intentional.

#### Product Management

- **Add Product**: Enter new product details like UPC, name, presentation type, price, cost, VAT inclusion, and stock quantity.
- **Edit Product**: Modify existing product information. All aspects, except the unique product identifier, can be adjusted.
- **View Products**: Display all products, providing a clear view of stock levels, pricing, and other relevant details. Include sorting and filtering options to ease product searches.
- **Delete Product**: Enable deletion of products from the inventory, including a verification step to avoid errors.

#### Sales Management

- **Record Sale**: Create a record for a new sale, capturing the sale date, seller ID, client ID, total amount, and details of products sold (quantity, sale price per unit).
- **View Sales**: Provide a detailed list of all sales transactions. This should include filtering options by date, client, or seller to help users quickly find specific transactions.

#### Reporting

- **Sales Reports**: Generate reports based on sales data, which can be customized by client or product.
- **Inventory Reports**: Produce detailed reports on inventory levels, product movement, and restock needs.
- **User Activity Reports**: Track and report on user activities.

#### Additional Functionalities

- **User Permissions**: Implement a permissions system where users can access only the features relevant to their roles. For example, salesmen might only access sales-related functions.
- **Secure Login System**: Ensure that all user logins are secure and that passwords are encrypted in the database.

#### Additional Guidelines
- **Modular Design**: Organize your program using functions. This approach not only makes your code cleaner and easier to read but also easier to update or fix later. Think of each function as a building block that performs a specific task.

### Deliverables
- **Complete Source Code and Database Files**: You need to submit all the code files you wrote for this project, along with any SQLite database files you used. Ensure all files are included so that your program can be run as intended.
- **User Manual**: Create a manual that serves as a guide to using your application. This document should also explain what each part of your program does, essentially documenting your code. 
- **Well-Commented Code**: Make sure your code includes detailed comments that explain what each section does and how it contributes to the functionality of the program. Your comments should follow the coding standards and guidelines.

### Grading Criteria

To evaluate the effectiveness and quality of the ERP - Sales System Program, the following grading criteria will be applied. Each aspect of the project will be assessed based on its adherence to the specified requirements, quality of implementation, and overall functionality.

#### Functionality (40%)
- **System Initialization**: Includes correct creation of the default admin account and proper initialization of the database.
- **User Operations**: Effectiveness in handling user management functions such as adding, editing, viewing, and deleting users.
- **Client Operations**: Accuracy and functionality in managing client information including additions, updates, and deletions.
- **Product Operations**: System's capability to handle product management tasks, including inventory management and product details adjustments.
- **Sales Management**: Efficiency and accuracy in recording, viewing, and managing sales transactions.

#### User Interface (20%)
- **Intuitiveness**: How easy it is for a new user to navigate the system without requiring extensive training.
- **Responsiveness**: Adaptability of the interface across different devices and screen sizes.
- **Aesthetics**: Visual appeal of the GUI, including layout consistency and color scheme.

#### Code Quality (20%)
- **Readability**: The code should be well-organized and easy to follow, with logical structuring and naming conventions.
- **Modularity**: Usage of functions and modules to ensure that the code is not only reusable but also scalable.
- **Commenting**: Comprehensive comments that explain the purpose of code blocks and major functions, aiding future maintenance and updates.

#### Documentation (10%)
- **Completeness**: All aspects of the system should be thoroughly documented, including setup instructions, user guide, and a detailed description of the system functionalities.
- **Clarity**: The documentation should be clear and straightforward, making it accessible to users of varying technical backgrounds.

#### Robustness and Error Handling (10%)
- **System Stability**: The application should run smoothly without crashes or freezes.
- **Error Handling**: The system should be able to handle common errors gracefully, providing informative error messages to the user instead of technical jargon.