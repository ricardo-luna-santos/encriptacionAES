# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 262)
        MainWindow.setMinimumSize(QtCore.QSize(551, 262))
        MainWindow.setMaximumSize(QtCore.QSize(551, 262))
        MainWindow.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgLogo = QtWidgets.QLabel(self.centralwidget)
        self.imgLogo.setGeometry(QtCore.QRect(10, 40, 141, 151))
        self.imgLogo.setText("")
        self.imgLogo.setPixmap(QtGui.QPixmap("login.png"))
        self.imgLogo.setScaledContents(True)
        self.imgLogo.setWordWrap(True)
        self.imgLogo.setObjectName("imgLogo")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(170, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(300, 39, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtUsuario.setFont(font)
        self.txtUsuario.setObjectName("txtUsuario")
        self.lblContrasena = QtWidgets.QLabel(self.centralwidget)
        self.lblContrasena.setGeometry(QtCore.QRect(170, 111, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblContrasena.setFont(font)
        self.lblContrasena.setObjectName("lblContrasena")
        self.txtContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.txtContrasena.setGeometry(QtCore.QRect(300, 110, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txtContrasena.setFont(font)
        self.txtContrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtContrasena.setObjectName("txtContrasena")
        self.btnEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(360, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnEntrar.setFont(font)
        self.btnEntrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("aceptar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEntrar.setIcon(icon1)
        self.btnEntrar.setIconSize(QtCore.QSize(16, 16))
        self.btnEntrar.setObjectName("btnEntrar")
        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(170, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("cancelar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancelar.setIcon(icon2)
        self.btnCancelar.setCheckable(False)
        self.btnCancelar.setObjectName("btnCancelar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bienvenido al Sistema de Encriptación de Datos"))
        self.lblUsuario.setText(_translate("MainWindow", "Usuario: "))
        self.lblContrasena.setText(_translate("MainWindow", "Contraseña"))
        self.btnEntrar.setToolTip(_translate("MainWindow", "Enviar usuario y contraseña"))
        self.btnEntrar.setText(_translate("MainWindow", "Aceptar"))
        self.btnCancelar.setToolTip(_translate("MainWindow", "Cancelar, salir de la aplicación"))
        self.btnCancelar.setText(_translate("MainWindow", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())