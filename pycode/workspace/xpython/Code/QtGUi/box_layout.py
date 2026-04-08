import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUI()


    def setupUI(self):
        okButton = QPushButton("OK")
        caneclButton = QPushButton("Cancel")

        hBox = QHBoxLayout()
        hBox.addStretch(-1)
        hBox.addWidget(okButton)
        hBox.addWidget(caneclButton)
        
        vBox = QVBoxLayout()
        # vBox.addStretch(2)
        vBox.addLayout(hBox)

        self.setLayout(vBox)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle("Buttons")

        self.show()



def main():
    app =  QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
