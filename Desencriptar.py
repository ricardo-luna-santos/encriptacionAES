from FrmDesencriptar  import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import ctypes

from datetime import *
import smtplib 
from email.message import EmailMessage 

class Desencriptar(QtWidgets.QMainWindow, Ui_FrmDesencriptar):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btnDesencriptar.clicked.connect(self.desencrypt_data_AES)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnDescargar.clicked.connect(self.crearFichero)
        self.btnCargar.clicked.connect(self.uploadFichero)
        self.btnEnviar.clicked.connect(self.eviarCorreo)
    
    def desencrypt_data_AES(self):
        data = self.lblMensajeEncriptado.text()
        key = b"123456789101112131415161718_UTXJ"
        iv = b"TI_UTXJ2024ENCRI"
        cadena_bytes = eval(data)
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        # Desencriptar los datos
        mensaje_desencriptado = decryptor.update(cadena_bytes) + decryptor.finalize()
        # El mensaje desencriptado puede contener padding, así que lo eliminamos
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        mensaje_desencriptado = unpadder.update(mensaje_desencriptado) + unpadder.finalize()
        self.lblMensajeDesencriptado.setText(mensaje_desencriptado.decode('utf-8'))
   
    def limpiar(self):
        self.lblMensajeEncriptado.clear()
        self.lblMensajeDesencriptado.clear()
    
    def crearFichero(self):
        cadena=self.lblMensajeDesencriptado.text()
        cadenaencriptada = self.lblMensaje.text()
        if cadena!="" and cadenaencriptada!="":
            fecha = datetime.now()
            d = fecha.strftime("%m-%d-%Y%H-%M-%S")
            with open(f'archivosDes/MensajeDes-{d}.txt', 'w') as fichero:
                fichero.write(cadena)
            QMessageBox.about(self, "Archivo", "Datos guardados correctamente")
        else:
            QMessageBox.about(self, "Error", "No hay texto encriptado que almacenar")
    
    def uploadFichero(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*.txt);;Python Files (*.py)", options=options)
        #fileName, _ =QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        if fileName:
            with open(fileName, 'r') as fichero:
                mensaje = fichero.read()
            self.lblMensajeEncriptado.setText(mensaje)
    
    def eviarCorreo(self):
        email_subject = "Datos encriptados" 
        sender_email_address = "ricardo_luna_santos@hotmail.com" 
        receiver_email_address = "ricardo.luna@utxicotepec.edu.mx\Ó" 
        email_smtp = "smtp-mail.outlook.com" 
        email_password = "Radio1245" 

        # Create an email message object 
        message = EmailMessage() 

        # Configure email headers 
        message['Subject'] = email_subject 
        message['From'] = sender_email_address 
        message['To'] = receiver_email_address 

        # Set email body text 
        message.set_content(self.lblMensajeEncriptado.text()) 

        # Set smtp server and port 
        server = smtplib.SMTP(email_smtp, '587') 

        # Identify this client to the SMTP server 
        server.ehlo() 

        # Secure the SMTP connection 
        server.starttls() 

        # Login to email account 
        server.login(sender_email_address, email_password) 

        # Send email 
        server.send_message(message) 

        # Close connection to server 
        server.quit()