import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.uiAgregarBodega import Ui_BodegaDialog
from UI.uiVerBodegas import Ui_VerBodegaDialog
from Dominio.entities import bodega
from Dominio.Persistencia import Persistencia

class FrmAgregarBodega():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_BodegaDialog()
        self.ui.setupUi(self)
        self.oBodega = None



class FrmVerBodegas():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_VerBodegaDialog()
        self.ui.setupUi(self)
        