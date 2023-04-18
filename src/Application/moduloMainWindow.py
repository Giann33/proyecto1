from PyQt6 import QtCore, QtGui, QtWidgets
from UI.uiMainWindow import Ui_MainWindow

class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setup(self)
        self.ui
