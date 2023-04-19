import traceback
from  PyQt6 import QtCore,QtGui,QtWidgets
from UI.uiAgregarDistribuidor import Ui_DistribuidorDialog
from UI.uiVerDistribuidores import Ui_VerDistribuidorDialog
from Dominio.entities import distribuidor
from Dominio.Persistencia import Persistencia

class FrmAgregarDistribuidor(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_DistribuidorDialog()
        self.ui.setupUi(self)
        self.oDistribuidor = None
        self.ui.pushButton_agregar.clicked.connect(self.clickAgregar)
        self.ui.pushButton_cancelar.clicked.connect(self.clickCancelar)

    def clickAgregar(self):
        self.oDistribuidor = distribuidor()
        self.oDistribuidor.nombredistribuidor = self.ui.lineEdit_nombre.text()
        self.oDistribuidor.iddistribuidor = self.ui.lineEdit_id.text()
        Persistencia.agregarDistribuidor(self.oDistribuidor)
        self.close()

    def clickCancelar(self):
        self.close()






class FrmVerDistribuidores():
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_VerDistribuidorDialog()
        self.ui.setupUi(self)
        