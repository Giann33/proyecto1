# Form implementation generated from reading ui file 'AgregarDistribuidor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DistribuidorDialog(object):
    def setupUi(self, DistribuidorDialog):
        DistribuidorDialog.setObjectName("DistribuidorDialog")
        DistribuidorDialog.resize(400, 204)
        self.pushButton_agregar = QtWidgets.QPushButton(parent=DistribuidorDialog)
        self.pushButton_agregar.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.pushButton_agregar.setObjectName("pushButton_agregar")
        self.pushButton_cancelar = QtWidgets.QPushButton(parent=DistribuidorDialog)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(240, 150, 75, 23))
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.widget = QtWidgets.QWidget(parent=DistribuidorDialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 341, 71))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.lineEdit_nombre = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_nombre.setText("")
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_nombre)
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.lineEdit_id = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_id.setText("")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_id)

        self.retranslateUi(DistribuidorDialog)
        QtCore.QMetaObject.connectSlotsByName(DistribuidorDialog)

    def retranslateUi(self, DistribuidorDialog):
        _translate = QtCore.QCoreApplication.translate
        DistribuidorDialog.setWindowTitle(_translate("DistribuidorDialog", "Dialog"))
        self.pushButton_agregar.setText(_translate("DistribuidorDialog", "Agregar"))
        self.pushButton_cancelar.setText(_translate("DistribuidorDialog", "Cancelar"))
        self.label.setText(_translate("DistribuidorDialog", "Nombre de distribuidor:"))
        self.label_2.setText(_translate("DistribuidorDialog", "ID de distribuidor:"))
