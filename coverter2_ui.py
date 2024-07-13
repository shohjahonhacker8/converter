# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter2kFNSbk.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(556, 249)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 173))
        self.widget.setMaximumSize(QSize(16777215, 173))
        self.widget.setStyleSheet(u"QWidget {\n"
"background-color: grey;\n"
"border-radius:5px;\n"
"}\n"
"QLineEdit {\n"
"background-color:white;\n"
"border-radius:5px;\n"
"padding:5px 10px;\n"
"font-size:20px;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(50, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 20px;\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setDragEnabled(False)

        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(500, 25, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: grey;\n"
"color:white;\n"
"font: 16pt \"Segoe UI\";\n"
"border-raduis:5px;\n"
"padding:5px;")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"UZS", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"USD", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Chiqish", None))
    # retranslateUi

