# Lets finish with the Form Layout:
# To use a form layout we need to import the QFormLayout
# The form layout is used to create a form with labels and fields.
# This is useful when we want to capture user input.

import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QFormLayout
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 280, 80)
        self.setWindowIcon(QIcon(str(self.icon_path())))

        # Central widget
        central_widget = QWidget(self)

        # Create a label and a button
        label = QLabel("This is a label")
        button = QPushButton("Press Me!")

        # Create a form layout
        form_layout = QFormLayout(central_widget)

        # Add the label and button to the layout
        # The addRow() method is used to add widgets in the form layout
        # It takes the label (or string for the label) and the corresponding field widget
        form_layout.addRow("Label:", label)  # Adds a row with a string label and the QLabel widget
        form_layout.addRow("Button:", button)  # Adds a row with a string label and the QPushButton widget

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
