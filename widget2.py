from PySide6.QtWidgets import QWidget, QMessageBox
from vazifa_ui import Ui_Dialog


class Widget(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Hisoblagich")

        self.b1.clicked.connect(self.button_clicked)
        self.b2.clicked.connect(self.button_clicked)
        self.b3.clicked.connect(self.button_clicked)
        self.b4.clicked.connect(self.button_clicked)
        self.b5.clicked.connect(self.button_clicked)
        self.b6.clicked.connect(self.button_clicked)
        self.b7.clicked.connect(self.button_clicked)
        self.b8.clicked.connect(self.button_clicked)
        self.b9.clicked.connect(self.button_clicked)
        self.b0.clicked.connect(self.button_clicked)
        self.bb1.clicked.connect(self.button_clicked)
        self.bb2.clicked.connect(self.button_clicked)
        self.bb3.clicked.connect(self.button_clicked)
        self.bb4.clicked.connect(self.button_clicked)
        self.b10.clicked.connect(self.button_clicked)
        self.bbb.clicked.connect(self.button_clicked)
        self.bc.clicked.connect(self.button_clicked)

    def button_clicked(self):
        btn = self.sender()
        text = self.label.text()

        if text == "0":
            text = ""

        if btn.text() == "=":
            result = eval(text)
            self.label_2.setText(text)
            self.label.setText(str(result))
        else:
            self.label_2.setText(text + btn.text())
            self.label.setText(text + btn.text())
        if btn.text() == "C":
            self.label_2.setText("")
            self.label.setText("0")
