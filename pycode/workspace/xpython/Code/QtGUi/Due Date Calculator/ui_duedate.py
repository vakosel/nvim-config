# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'due_date_calculatorSDPAzg.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDateEdit,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class DueDateForm(object):
    def setupUi(self, MainForm):
        if not MainForm.objectName():
            MainForm.setObjectName("MainForm")
        MainForm.resize(406, 204)
        self.groupBox = QGroupBox(MainForm)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 411, 201))
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.lblLMP = QLabel(self.groupBox)
        self.lblLMP.setObjectName("lblLMP")
        font1 = QFont()
        font1.setPointSize(10)
        self.lblLMP.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblLMP)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName("dateEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dateEdit)

        self.lblAge = QLabel(self.groupBox)
        self.lblAge.setObjectName("lblAge")
        self.lblAge.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblAge)

        self.lnEditAge = QLineEdit(self.groupBox)
        self.lnEditAge.setObjectName("lnEditAge")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lnEditAge)

        self.lblDueDate = QLabel(self.groupBox)
        self.lblDueDate.setObjectName("lblDueDate")
        self.lblDueDate.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDueDate)

        self.lnDueDate = QLineEdit(self.groupBox)
        self.lnDueDate.setObjectName("lineDueDate")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lnDueDate)

        self.btnReset = QPushButton(self.groupBox)
        self.btnReset.setObjectName("btnReset")
        self.btnReset.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.btnReset)

        self.btnFind = QPushButton(self.groupBox)
        self.btnFind.setObjectName("btnFind")
        self.btnFind.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.btnFind)

        self.retranslateUi(MainForm)

        QMetaObject.connectSlotsByName(MainForm)

    # setupUi

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(
            QCoreApplication.translate("MainForm", "Due Date Calulator", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainForm", "Due Date Calculator", None)
        )
        self.lblLMP.setText(QCoreApplication.translate("MainForm", "Enter LMP", None))
        self.lblAge.setText(
            QCoreApplication.translate("MainForm", "Age (weeks + days)    ", None)
        )
        self.lblDueDate.setText(
            QCoreApplication.translate("MainForm", "Due Date ", None)
        )
        self.btnReset.setText(
            QCoreApplication.translate("MainForm", "Reset Date ", None)
        )
        self.btnFind.setText(
            QCoreApplication.translate("MainForm", "Find Age - Due date", None)
        )

    # retranslateUi
