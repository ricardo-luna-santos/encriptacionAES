from FrmMenu  import *
from Encriptar import *
from Desencriptar import *
from Login import *
class Menu(QtWidgets.QMainWindow, Ui_FrmMenu):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.menuEncriptar.addAction("Encriptar Archivo", self.openencriptar)
        self.menuDesencriptar.addAction("Desencriptar Archivo", self.opendesencriptar)
        self.menuOpciones.addAction("Salir", self.salir)

    def openencriptar(self):
        opennewwindow = Encriptar(self)
        opennewwindow.show()
    def opendesencriptar(self):
        opennewwindow = Desencriptar(self)
        opennewwindow.show()
    def ocultar(self):
        opennewwindow = MainWindow(self)
        opennewwindow.show()
    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Deseas salir de la aplicación")
        msgBox.setWindowTitle("Cancelar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.hide()
            self.ocultar()


