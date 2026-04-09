from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget

from ui_duedate import DueDateForm  # import your compiled UI


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Load the UI
        self.ui = DueDateForm()
        self.ui.setupUi(self)

        # Enable dropdown calendar
        self.ui.dateEdit.setCalendarPopup(True)

        # set default date to today
        self.ui.dateEdit.setDate(QDate.currentDate())

        # connect the buttons
        self.ui.btnFind.clicked.connect(self.caclulate_due_date)
        self.ui.btnReset.clicked.connect(self.reset_fields)

    def caclulate_due_date(self):
        # Get LMP date from the date edit widget
        lmp = self.ui.dateEdit.date()

        # Validate: LMP must be at least 28 days ago
        days_sime_lmp = lmp.daysTo(QDate.currentDate())
        if days_sime_lmp < 28:
            QMessageBox.warning(
                self, "Invalid LMP Date", "LMP date must be at least 28 days ago."
            )
            return

        # due date calculation: LMP + 280 days
        due_date = lmp.addDays(280)
        self.ui.lnDueDate.setText(due_date.toString("dd/MM/yyyy"))

        # find pregnancy age in weeks
        days_since_lmp = lmp.daysTo(QDate.currentDate())
        weeks = days_since_lmp // 7
        days = days_since_lmp % 7
        self.ui.lnEditAge.setText(f"{weeks} weeks and {days} days")

    def reset_fields(self):
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.lnEditAge.clear()
        self.ui.lnDueDate.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
