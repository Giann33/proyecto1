from PyQt6 import QtCore, QtGui, QtWidgets
from UI.uiMainWindow import Ui_MainWindow
from Application.Articulos.moduloArticulos import FrmAgregarArticulos
from Application.Bodegas.moduloBodegas import *
from Application.Distribuidores import *


class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setup(self)
        self.ui.actionAgregar_distribuidor.triggered.connect(self.clickAgregarDistribuidor)
        self.ui.actionAgregar_bodegas.triggered.connect(self.clickAgregarBodegas)
        self.ui.actionAgregar_articulos.triggered.connect(self.clickAgregarArticulos)
        self.ui.actionVer_distribuidor.triggered.connect(self.clickVerDistribuidor)
        self.ui.actionVer_bodegas.triggered.connect(self.clickVerBodegas)
        self.pantalla1 = None
        self.pantalla2 = None
        self.pantalla3 = None
        self.pantalla4 = None
        self.pantalla5 = None

    def clickAgregarDistribuidor(self):
        self.pantalla1 = FrmAgregarDistribuidores()
        self.pantalla1.show()

    def clickAgregarBodegas(self):
        self.pantalla2 = FrmAgregarBodegas()
        self.pantalla2.show()

    def clickAgregarArticulos(self):
        self.pantalla3 = FrmAgregarArticulos()
        self.pantalla3.show()

    def clickVerDistribuidor(self):
        self.pantalla1 = FrmVerDistribuidor()
        self.pantalla1.show()

    def clickVerBodegas(self):
        self.pantalla1 = FrmVerBodegas()
        self.pantalla1.show()





