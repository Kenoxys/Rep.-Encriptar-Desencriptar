from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import logging

__version__ = "0.1"

logging.basicConfig(level=logging.DEBUG)

# Configuración inicial del icono (opcional)
Config.set('kivy', 'window_icon', '/home/Kenoxys/Descargas/Proyecto-Encrit/Proyect/data/icon.png')  # Método 1:cite[2]

# Clave fija para propósitos de demostración (32 bytes para AES-256)
fixed_key = b'12345678901234567890123456789012'

# Encriptar el archivo
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(file_path + '.enc', 'wb') as file:
        file.write(iv + encrypted_data)

# Desencriptar el archivo
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        iv = file.read(16)
        encrypted_data = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    with open(file_path[:-4], 'wb') as file:
        file.write(data)



    """def load_kv(self, kv_file):
        Loads the given KV file.
        with open(kv_file, 'r') as f:
            self.root = Builder.load_string(f.read()) 
        return self.root  # Return the root widget"""
    
    """def do_something(self):
        print("¡Botón presionado!")"""
    
class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_path = None  # Inicializar atributo

    def select_file(self, instance):
        logging.info("Select File button pressed")
        if len(self.ids.filechooser.selection) == 1:
            self.file_path = self.ids.filechooser.selection[0]
            self.ids.result_label.text = f"Archivo seleccionado: {self.file_path}"
            logging.info(f"Selected file: {self.file_path}")
        else:
            selected_files = ', '.join(self.ids.filechooser.selection)
            self.ids.result_label.text = f"Archivos seleccionados: {selected_files}"
            logging.info(f"Selected files: {selected_files}")

    def encrypt_file(self, instance):
        logging.info("Encrypt File button pressed")
        try:
            if self.file_path:
                if os.path.isfile(self.file_path):
                    encrypt_file(self.file_path, fixed_key)
                    self.ids.result_label.text = "Archivo encriptado correctamente"
                    logging.info("File encrypted successfully")
                else:
                    self.ids.result_label.text = "Error: El elemento seleccionado no es un archivo."
                    logging.error("Error: The selected item is not a file.")
            else:
                self.ids.result_label.text = "Por favor, selecciona un archivo primero"
                logging.warning("Please select a file first")
        except Exception as e:
            self.ids.result_label.text = f"Error al encriptar: {str(e)}"
            logging.error(f"Error encrypting file: {str(e)}")

    def decrypt_file(self, instance):
        logging.info("Decrypt File button pressed")
        try:
            if self.file_path:
                if self.file_path.endswith(".enc"):
                    decrypt_file(self.file_path, fixed_key)
                    self.ids.result_label.text = "Archivo desencriptado (si el proceso fue exitoso)"
                    logging.info("File decrypted (if the process was successful)")
                else:
                    self.ids.result_label.text = "El archivo no tiene la extensión .enc"
                    logging.warning("The file does not have the .enc extension")
            else:
                self.ids.result_label.text = "Por favor, selecciona un archivo encriptado"
                logging.warning("Please select an encrypted file")
        except Exception as e:
            self.ids.result_label.text = f"Error al desencriptar: {str(e)}"
            logging.error(f"Error decrypting file: {str(e)}")

class MyApp(App):
    title = "EncDes"  # Personaliza el título aquí:cite[9]
    def build(self):
        logging.info("Loading KV file")
        self.icon = '/home/Kenoxys/Descargas/Proyecto-Encrit/Proyect/data/icon.png'  # Método 2:cite[6]
        # Añade un tamaño inicial para la ventana
        from kivy.core.window import Window
        Window.size = (800, 600)
        
        # Carga el archivo KV y retorna MyWidget
        try:
            return MyWidget()
        except Exception as e:
            logging.error(f"Error cargando KV: {str(e)}")
            return Label(text="Error cargando la interfaz.")

if __name__ == '__main__':
    MyApp().run()
