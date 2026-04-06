from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Calculator")

v_layout = QVBoxLayout(window)

# Display
display = QLineEdit()
display.setReadOnly(True)
display.setAlignment(Qt.AlignmentFlag.AlignRight)
display.setFixedHeight(50)
v_layout.addWidget(display)

# Grid layout for buttons
grid = QGridLayout()

# Buttons: (text, row, col, type)
buttons = [
    ("7", 0, 0, "num"),
    ("8", 0, 1, "num"),
    ("9", 0, 2, "num"),
    ("/", 0, 3, "op"),
    ("4", 1, 0, "num"),
    ("5", 1, 1, "num"),
    ("6", 1, 2, "num"),
    ("*", 1, 3, "op"),
    ("1", 2, 0, "num"),
    ("2", 2, 1, "num"),
    ("3", 2, 2, "num"),
    ("-", 2, 3, "op"),
    ("0", 3, 0, "num"),
    (".", 3, 1, "num"),
    ("=", 3, 2, "op"),
    ("+", 3, 3, "op"),
]

for text, row, col, typ in buttons:
    btn = QPushButton(text)
    btn.setMinimumSize(60, 60)
    if typ == "op":
        btn.setStyleSheet("background-color: orange; color: white; font-weight: bold;")
    else:
        btn.setStyleSheet("background-color: lightgray;")
    grid.addWidget(btn, row, col)

v_layout.addLayout(grid)

window.show()
app.exec()
