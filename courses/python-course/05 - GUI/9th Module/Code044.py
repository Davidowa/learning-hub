# Now lets see a functional example of a simple GUI application using PyQt6
# A login form that takes a username and password and then refreshes the window to show a welcome message.
# We will use also a database to store the username and password.

# Lets start by importing the necessary modules:
import sys
import os
import platform
import sqlite3
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QFormLayout, QLineEdit, QMessageBox, QSystemTrayIcon
from PyQt6.QtGui import QIcon

# Lets start by creating a database:
database_file = Path() / "05 - GUI/9th Module" / "user.db"
if database_file.exists():
    # If it exists, delete the file
    os.remove(database_file)

# Create a connection to the database
with sqlite3.connect(str(database_file)) as conn:
    # Create command
    create_command = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)"
    # Execute the command
    conn.execute(create_command)

    # Lets insert some data
    # Create a list of tuples
    users = [
        {"name": "David", "password": "123"}, 
        {"name": "Lorena", "password": "456"}, 
        {"name": "Octavio", "password": "789"}
    ]

    ## Insert user data command
    insert_command = "INSERT INTO Users (username, password) VALUES (?, ?)"
    # Insert user data using a for loop
    for user in users:
        conn.execute(insert_command, (user['name'], user['password']))
    conn.commit()


# Now lets create a class that inherits from QMainWindow:

def icon_ico_path() -> Path:
        os_name = platform.system()
        if os_name == 'Darwin':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "apple.ico"
        elif os_name == 'Windows':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "windows.ico"
        else:
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.ico"
        return icon_path    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 280, 120)
        self.setWindowIcon(QIcon(str(self.icon_path())))

        # Initialize views
        self.current_username = None
        self.setCentralWidget(self.create_login_view())

    def create_login_view(self):
        central_widget = QWidget()
        form_layout = QFormLayout(central_widget)

        self.username_label = QLabel("Username:")
        self.password_label = QLabel("Password:")
        self.login_button = QPushButton("Access")
        self.exit_button = QPushButton("Exit")
        self.username_line_edit = QLineEdit()
        self.password_line_edit = QLineEdit()

        form_layout.addRow(self.username_label, self.username_line_edit)
        form_layout.addRow(self.password_label, self.password_line_edit)
        form_layout.addRow(self.login_button)
        form_layout.addRow(self.exit_button)


        self.login_button.clicked.connect(self.access_button)
        self.exit_button.clicked.connect(self.close)
        return central_widget

    def create_post_login_view(self):
        central_widget = QWidget()
        grid_layout = QGridLayout(central_widget)

        welcome_label = QLabel(f"Hello {self.current_username}")
        exit_button = QPushButton("Sign Out")

        grid_layout.addWidget(welcome_label, 0, 0)
        grid_layout.addWidget(exit_button, 1, 1)

        exit_button.clicked.connect(self.show_login_view)
        return central_widget

    def access_button(self):
        username = self.username_line_edit.text()
        password = self.password_line_edit.text()

        with sqlite3.connect(str(database_file)) as conn:
            select_command = "SELECT * FROM Users WHERE username = ? AND password = ?"
            cursor = conn.execute(select_command, (username, password))
            results = cursor.fetchall()

            if len(results) == 0:
                QMessageBox.critical(self, "Error", "The user does not exist")
                self.refresh()
            else:
                QMessageBox.information(self, "Welcome", f"Welcome to the system, {username}")
                self.current_username = username
                self.setCentralWidget(self.create_post_login_view())

    def close(self):
        super().close()

    def show_login_view(self):
        self.setCentralWidget(self.create_login_view())
        self.username_line_edit.clear()
        self.password_line_edit.clear()

    def refresh(self):
        self.username_line_edit.clear()
        self.password_line_edit.clear()
    
    def icon_path(self) -> Path:
        os_name = platform.system()
        if os_name == 'Darwin':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "apple.ico"
        elif os_name == 'Windows':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "windows.ico"
        else:
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.ico"
        return icon_path

       

    
# Create the application instance
app = QApplication(sys.argv)

# Create the window instance
window = MainWindow()

# Show the window
window.show()

# Execute the app
sys.exit(app.exec())