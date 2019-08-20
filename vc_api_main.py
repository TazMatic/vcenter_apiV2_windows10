from GUI import basic_window
from PySide2 import QtWidgets
import sys
import os


# Create a reference to the main elements
app = QtWidgets.QApplication(sys.argv)
basic_window.main_window(app)
sys.exit(app.exec_())
