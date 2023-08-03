import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui import Ui_MainWindow
from utils import encryption

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.crypt_obj = encryption.RSACrypt()
        
        self.ui.encrypt_start.clicked.connect(self.encrypt_start)
        self.ui.decrypt_start.clicked.connect(self.decrypt_start)
        
    def encrypt_start(self) -> None:
        self.crypt_obj.encrypt(self.ui.encrypt_text_box.toPlainText())

    def decrypt_start(self) -> None:
        private_key = QFileDialog.getOpenFileName(caption="Open Private Key")
        encrypted_file = QFileDialog.getOpenFileName(caption="Select Encrypted File")
        text_out = self.crypt_obj.decrypt(private_key = os.path.normpath(private_key[0]),
                                          encrypted_file = os.path.normpath(encrypted_file[0]))
        self.ui.decrypted_text.setPlainText(text_out)
        self.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())