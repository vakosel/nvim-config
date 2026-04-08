import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QLineEdit, QPushButton, QWidget


class Example(QWidget):
    
    def __init__(self):
        super().__init__()


        self.btn = QPushButton("Write")
        self.qtbn = QPushButton("Exit")
        self.qtbn.clicked.connect(self.close)
        self.btn.clicked.connect(self.write)        
        self.qle= QLineEdit()

        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.qle, 1, 0, )
        self.grid.addWidget(self.btn, 2, 0)
        self.grid.addWidget(self.qtbn, 3, 0)

        self.setLayout(self.grid)
        self.show()
        self.setWindowTitle("Quit Button")

    def write(self):
        self.qle.setText("Hello World")
        

        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec())

if __name__ == '__main__':
    main()
