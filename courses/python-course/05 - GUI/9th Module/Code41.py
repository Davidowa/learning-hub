# Lets continue with the Grid Layout:
# To use a grid layout we need to import the QGridLayout
import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QGridLayout
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

        # Create a grid layout
        grid_layout = QGridLayout(central_widget)

        # Add the label and button to the layout at specific positions
        # The addWidget() method takes the following arguments:
        # 1. The widget to add
        # 2. The row position
        # 3. The column position
        grid_layout.addWidget(label, 0, 1)  # Row 0, Column 1
        grid_layout.addWidget(button, 1, 0)  # Row 1, Column 1

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
