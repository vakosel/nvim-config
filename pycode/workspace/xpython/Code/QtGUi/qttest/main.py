from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        text = self.lineEdit.text()
        msgBox = QMessageBox()
        msgBox.setText(f"You entered: {text}")
        msgBox.exec()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
