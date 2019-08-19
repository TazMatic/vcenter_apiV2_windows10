from GUI import basic_window
from PyQt5 import QtWidgets
import sys
import os
from PyQt5.QtWidgets import QStyleFactory

# If the current stlye is not supported by QT change it to the first supported
# style available
#supported_styles = QStyleFactory.keys()
#style = os.environ["QT_STYLE_OVERRIDE"]
#if style not in supported_styles:
#    os.environ["QT_STYLE_OVERRIDE"] = supported_styles[0]

# Create a reference to the main elements
app = QtWidgets.QApplication(sys.argv)
GUI = basic_window.main_window()
sys.exit(app.exec_())
