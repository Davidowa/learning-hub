# Lets continue with the Vertical Box Layout:

import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 280, 80)
        self.setWindowIcon(QIcon(str(self.icon_path())))

        # Central widget
        central_widget = QWidget(self)

        # Lets create a label and a button:
        label = QLabel("This is a label")
        button = QPushButton("Press Me!")

        # Create a vertical box layout:
        horizontal_layout = QVBoxLayout(central_widget)

        # Add the label to the horizontal layout:
        horizontal_layout.addWidget(label)

        # Add the button to the horizontal layout:
        horizontal_layout.addWidget(button)

        # Set the central widget with the layout
        self.setCentralWidget(central_widget)
    
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