# QMainWindow
# In the previous code, we used QWidget to create a window.
# In Qt, any widget can be a window (QWidget, QPushButton, QCheckBox, etc.).
# However, its better to use the appropriate widget for each task, and thats why you should use QMainWindow.
# The QMainWindow is a pre-made widget which provides a lot of standard windows features, such as a menu bar, a status bar, a toolbar, etc.

# Let's create a window with QMainWindow.

import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

# app = QApplication(sys.argv)
# window = QMainWindow()
# window.setWindowTitle("PyQt6 GUI")
# window.setGeometry(100, 100, 280, 80) 

# os_name = platform.system()
# if os_name == 'Darwin':  # macOS uses the Darwin kernel
#     icon_path =  Path() / "05 - GUI/9th Module/Assets" / "apple.png"
# elif os_name == 'Windows':
#     icon_path =  Path() / "05 - GUI/9th Module/Assets" / "windows.png"
# else:
#     icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.png"

# window.setWindowIcon(QIcon(str(icon_path)))

# window.show()

# sys.exit(app.exec())

# However, once we start working with GUIs is better to create a class for each window.

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 280, 80)
        self.setWindowIcon(QIcon(str(self.icon_path())))

        # In this case, we will create a button (QPushButton)
        # A QPushButton is a button that can be clicked.
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        # The central widget is the widget that occupies the central area of the window
        self.setCentralWidget(button)
    
    def icon_path(self) -> Path:
        os_name = platform.system()
        if os_name == 'Darwin':  # macOS uses the Darwin kernel
            icon_path =  Path() / "05 - GUI/9th Module/Assets" / "apple.png"
        elif os_name == 'Windows':
            icon_path =  Path() / "05 - GUI/9th Module/Assets" / "windows.png"
        else:
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.png"
        return icon_path

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())