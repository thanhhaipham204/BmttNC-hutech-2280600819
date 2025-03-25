import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow  # Đổi tên file giao diện phù hợp với Rail Fence
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/encrypt"
        try:
            payload = {
                "plain_text": self.ui.txt_plaintext.toPlainText(),
                "key": int(self.ui.txt_key.toPlainText())  # Chuyển key sang số nguyên
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setText(data["encrypted_text"])
                self.show_message("Encrypted Successfully")
            else:
                self.show_message("Error while calling API")
        except ValueError:
            self.show_message("Key must be an integer")
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {e}")
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/railfence/decrypt"
        try:
            payload = {
                "cipher_text": self.ui.txt_cipher.toPlainText(),
                "key": int(self.ui.txt_key.toPlainText())  # Chuyển key sang số nguyên
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setText(data["decrypted_text"])
                self.show_message("Decrypted Successfully")
            else:
                self.show_message("Error while calling API")
        except ValueError:
            self.show_message("Key must be an integer")
        except requests.exceptions.RequestException as e:
            self.show_message(f"Error: {e}")

    def show_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
