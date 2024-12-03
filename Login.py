from FrmLogin  import *
from Menu import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.btnEntrar.clicked.connect(self.validar)
        self.btnCancelar.clicked.connect(self.salir)

    def validar(self):
        usuario = self.txtUsuario.text()
        contrasena = self.txtContrasena.text()
        if usuario == "rlunas" and contrasena == "1234":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("Bienvenido al Sistema")
            msgBox.setWindowTitle("Autorizado")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.openMenu()
                self.hide()
            else:
                self.close()
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Error usuario o contraseña incorrectos")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(QMessageBox.Ok )
            returnValue = msgBox.exec()

    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Deseas salir de la aplicación")
        msgBox.setWindowTitle("Cancelar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.close()

    def openMenu(self):
        opennewwindow = Menu(self)
        opennewwindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()