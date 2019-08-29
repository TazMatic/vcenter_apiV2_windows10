""""Provides the main_window"""
from PySide2 import QtCore, QtWidgets

import GUI.vc_connect


class main_window(QtWidgets.QMainWindow):

    def __init__(self, instance):
        super(main_window, self).__init__()
        self.setGeometry(400, 200, 300, 0)
        self.setAccessibleName("VCenter_API")
        self.setWindowTitle("VCenter ACDC GUI")
        self.setWindowFlags(
                            QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowMinimizeButtonHint
        )
        self.show()

        # Create main frame
        self.main_frame = QtWidgets.QFrame(accessibleName='main_frame')
        self.main_frame.setStyleSheet("background-color: #3a3d42;")
        self.setCentralWidget(self.main_frame)

        # Variable creation
        self.host_text = None
        self.log = None
        self.scroll_frame = None
        self.last_rendered = None
        self.vms = list()
        self.app = instance
        GUI.vc_connect.render_login(self)
