import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.uiAgregarArticulo import Ui_ArticuloDialog
from Dominio.entities import articulo
from Dominio.Persistencia import Persistencia

class FrmAgregarArticulos():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_ArticuloDialog
        self.ui.setupUi(self)
        self.oArticulo = None