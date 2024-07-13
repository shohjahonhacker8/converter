from PySide6.QtWidgets import QWidget, QMessageBox
from coverter2_ui import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.ayirboshlash)
        self.pushButton.clicked.connect(self.chiqish)

    def ayirboshlash(self):
        if self.lineEdit.text():
            uzs = int(self.lineEdit.text())
            usd = round(uzs / 12665, 2)
            self.lineEdit_2.setText(str(usd))

    def chiqish(self):
        response = QMessageBox.question(None, "Habar", "Chiqishni xohlaysizmi?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.close()
