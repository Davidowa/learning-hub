# Lets talk a little bit more about the QGridLayout
# for the addWidget() method, we have some more arguments:
# row span: The number of rows the widget will span
# column span: The number of columns the widget will span

import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 480, 180)
        self.setWindowIcon(QIcon(str(self.icon_path())))

        # Central widget
        central_widget = QWidget(self)

        # Create a label and a button
        label = QLabel("This is a label")
        button = QPushButton("Press Me!")
        
        # Lets make the button expand to fill the available space
        # This is done by setting the size policy of the button
        # If we don't do this, the button will be the minimum size
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Create a grid layout
        grid_layout = QGridLayout(central_widget)

        # Lets add the label at position 0, 0
        grid_layout.addWidget(label, 0, 0)

        # For the button, lets say we want it to span two columns
        # and two rows
        grid_layout.addWidget(button, 0, 1, 2, 2)

        # Set the central widget with the layout
        self.setCentralWidget(central_widget)
    
    def icon_path(self):
        os_name = platform.system()
        if os_name == 'Darwin':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "apple.png"
        elif os_name == 'Windows':
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "windows.png"
        else:
            icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.png"
        return icon_path

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
