import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.uiAgregarDistribuidor import Ui_ArticuloDialog
from UI.uiVerDistribuidores import Ui_VerDistribuidorDialog
from Dominio.entities import distribuidor
from Dominio.Persistencia import Persistencia

class FrmAgregarDistribuidor():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_ArticuloDialog
        self.ui.setupUi(self)
        self.oDistribuidor = None



class FrmVerDistribuidores():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_VerDistribuidorDialog
        self.ui.setupUi(self)
        