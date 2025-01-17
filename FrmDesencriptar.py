# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmDesencriptar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_FrmDesencriptar(object):
    def setupUi(self, FrmDesencriptar):
        FrmDesencriptar.setObjectName("FrmDesencriptar")
        FrmDesencriptar.resize(800, 600)
        FrmDesencriptar.setMinimumSize(QtCore.QSize(800, 600))
        FrmDesencriptar.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(FrmDesencriptar)
        self.centralwidget.setObjectName("centralwidget")
        self.btnDesencriptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDesencriptar.setGeometry(QtCore.QRect(550, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnDesencriptar.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("encriptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDesencriptar.setIcon(icon)
        self.btnDesencriptar.setIconSize(QtCore.QSize(32, 32))
        self.btnDesencriptar.setObjectName("btnDesencriptar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(550, 140, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLimpiar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiar.setIcon(icon1)
        self.btnLimpiar.setIconSize(QtCore.QSize(32, 32))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnCargar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCargar.setGeometry(QtCore.QRect(550, 200, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCargar.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCargar.setIcon(icon2)
        self.btnCargar.setIconSize(QtCore.QSize(32, 32))
        self.btnCargar.setObjectName("btnCargar")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 50, 471, 511))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.Texto = QtWidgets.QWidget()
        self.Texto.setObjectName("Texto")
        self.lblMensaje = QtWidgets.QLabel(self.Texto)
        self.lblMensaje.setGeometry(QtCore.QRect(10, 0, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblMensaje.setFont(font)
        self.lblMensaje.setObjectName("lblMensaje")
        self.lblMensaje_3 = QtWidgets.QLabel(self.Texto)
        self.lblMensaje_3.setGeometry(QtCore.QRect(10, 240, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblMensaje_3.setFont(font)
        self.lblMensaje_3.setObjectName("lblMensaje_3")
        self.lblMensajeEncriptado = QtWidgets.QLabel(self.Texto)
        self.lblMensajeEncriptado.setGeometry(QtCore.QRect(0, 40, 451, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblMensajeEncriptado.setFont(font)
        self.lblMensajeEncriptado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblMensajeEncriptado.setText("")
        self.lblMensajeEncriptado.setTextFormat(QtCore.Qt.PlainText)
        self.lblMensajeEncriptado.setScaledContents(False)
        self.lblMensajeEncriptado.setWordWrap(True)
        self.lblMensajeEncriptado.setObjectName("lblMensajeEncriptado")
        self.lblMensajeDesencriptado = QtWidgets.QLabel(self.Texto)
        self.lblMensajeDesencriptado.setGeometry(QtCore.QRect(0, 280, 451, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblMensajeDesencriptado.setFont(font)
        self.lblMensajeDesencriptado.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblMensajeDesencriptado.setText("")
        self.lblMensajeDesencriptado.setTextFormat(QtCore.Qt.PlainText)
        self.lblMensajeDesencriptado.setScaledContents(False)
        self.lblMensajeDesencriptado.setWordWrap(True)
        self.lblMensajeDesencriptado.setObjectName("lblMensajeDesencriptado")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../.designer/backup/text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Texto, icon3, "")
        self.Imagen = QtWidgets.QWidget()
        self.Imagen.setObjectName("Imagen")
        self.label = QtWidgets.QLabel(self.Imagen)
        self.label.setGeometry(QtCore.QRect(10, 60, 431, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../.designer/backup/picture.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lblMensaje_2 = QtWidgets.QLabel(self.Imagen)
        self.lblMensaje_2.setGeometry(QtCore.QRect(10, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblMensaje_2.setFont(font)
        self.lblMensaje_2.setObjectName("lblMensaje_2")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../../../.designer/backup/picture.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.Imagen, icon4, "")
        self.btnDescargar = QtWidgets.QPushButton(self.centralwidget)
        self.btnDescargar.setGeometry(QtCore.QRect(550, 260, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnDescargar.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDescargar.setIcon(icon5)
        self.btnDescargar.setIconSize(QtCore.QSize(32, 32))
        self.btnDescargar.setObjectName("btnDescargar")
        self.btnEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnviar.setGeometry(QtCore.QRect(550, 320, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEnviar.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEnviar.setIcon(icon6)
        self.btnEnviar.setIconSize(QtCore.QSize(32, 32))
        self.btnEnviar.setObjectName("btnEnviar")
        FrmDesencriptar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FrmDesencriptar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuDesencriptar = QtWidgets.QMenu(self.menubar)
        self.menuDesencriptar.setObjectName("menuDesencriptar")
        self.menuLimpiar = QtWidgets.QMenu(self.menubar)
        self.menuLimpiar.setObjectName("menuLimpiar")
        self.menuCargar = QtWidgets.QMenu(self.menubar)
        self.menuCargar.setObjectName("menuCargar")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        FrmDesencriptar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FrmDesencriptar)
        self.statusbar.setObjectName("statusbar")
        FrmDesencriptar.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDesencriptar.menuAction())
        self.menubar.addAction(self.menuLimpiar.menuAction())
        self.menubar.addAction(self.menuCargar.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(FrmDesencriptar)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FrmDesencriptar)

    def retranslateUi(self, FrmDesencriptar):
        _translate = QtCore.QCoreApplication.translate
        FrmDesencriptar.setWindowTitle(_translate("FrmDesencriptar", "Desencriptar archivo o mensaje"))
        self.btnDesencriptar.setText(_translate("FrmDesencriptar", "Desencriptar"))
        self.btnLimpiar.setText(_translate("FrmDesencriptar", "Limpiar"))
        self.btnCargar.setText(_translate("FrmDesencriptar", "Cargar"))
        self.lblMensaje.setText(_translate("FrmDesencriptar", "Mensaje encriptado"))
        self.lblMensaje_3.setText(_translate("FrmDesencriptar", "Mensaje desencriptado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Texto), _translate("FrmDesencriptar", "Texto"))
        self.lblMensaje_2.setText(_translate("FrmEncriptar", "Imagen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Imagen), _translate("FrmDesencriptar", "Imagen"))
        self.btnDescargar.setText(_translate("FrmDesencriptar", "Descargar"))
        self.btnEnviar.setText(_translate("FrmDesencriptar", "Enviar"))
        self.menuDesencriptar.setTitle(_translate("FrmDesencriptar", "Desencriptar"))
        self.menuLimpiar.setTitle(_translate("FrmDesencriptar", "Limpiar"))
        self.menuCargar.setTitle(_translate("FrmDesencriptar", "Cargar"))
        self.menuSalir.setTitle(_translate("FrmDesencriptar", "Salir"))
        self.menuAyuda.setTitle(_translate("FrmDesencriptar", "Ayuda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDesencriptar = QtWidgets.QMainWindow()
    ui = Ui_FrmDesencriptar()
    ui.setupUi(FrmDesencriptar)
    FrmDesencriptar.show()
    sys.exit(app.exec_())
