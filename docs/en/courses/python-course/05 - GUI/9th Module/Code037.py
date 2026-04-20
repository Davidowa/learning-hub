# Graphic User Interface (GUI) with PyQt6
# Graphic user insterfaces are used to make the interaction between the user and the computer easier.

# Qt is a cross-platform application framework that is widely used for developing application software 
# that can be run on various software and hardware platforms with little or no change in the underlying codebase,
# while still being a native application with native capabilities and speed.

# PyQt6 is a python module that allows us to create GUIs using Qt.

# To install PyQt6, run the following command in the terminal:
# pip install PyQt6

# Now, let's create a simple GUI with PyQt6.

# Importing the necessary libraries.

import sys
import platform
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

# QApplication: This class manages the GUI application's control flow and main settings.
# QWidget: This class is the base class of all user interface objects.

# Creating the application object.
# You need one and only one QApplication object per application.
# When you create the QApplication object, it reads the command line arguments passed to the script,
# so you have to pass the sys.argv to it.
# sys.argv is a list of command line arguments that enables the user to control the startup of the application.
app = QApplication(sys.argv)

# Now let's create a window.
window = QWidget()

# Let's set the title of the window.
window.setWindowTitle("PyQt6 GUI")

# (x, y, width, height)
# the first two parameters are the coordinates of the window according to the screen
# the last two parameters are the width and height of the window that we are going to create.
window.setGeometry(100, 100, 280, 80) 

# You can also add an icon to the window.
# To do that, you need to create a QIcon object and pass it to the setWindowIcon method of the window.
# Let's set the icon of the window according to the operating system.
os_name = platform.system()
if os_name == 'Darwin':  # macOS uses the Darwin kernel
    icon_path =  Path() / "05 - GUI/9th Module/Assets" / "apple.png"
elif os_name == 'Windows':
    icon_path =  Path() / "05 - GUI/9th Module/Assets" / "windows.png"
else:
    icon_path = Path() / "05 - GUI/9th Module/Assets" / "linux.png"

window.setWindowIcon(QIcon(str(icon_path)))

# Now let's show the window.
window.show()

# Finally, we run the application's event loop.

# the sys.exit() method ensures a clean exit.
# the app.exec() method starts the event loop.
sys.exit(app.exec())