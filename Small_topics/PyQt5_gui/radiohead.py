from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.radio1 = QRadioButton("Visa card",self)
        self.radio2 = QRadioButton("Master card",self)
        self.radio3 = QRadioButton("Paypal",self)
        self.radio4 = QRadioButton("In-store",self)
        self.radio5 = QRadioButton("online",self)
        self.buttongroup1 = QButtonGroup()
        self.buttongroup2 = QButtonGroup()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("QRadioButton{"
        "font-size: 10px;" 
        "padding: 10px;" 
        "font-family: Arial;"
        "}")

        self.radio1.move(10,0)
        self.radio1.adjustSize()
        self.radio2.move(10,50)
        self.radio2.adjustSize()
        self.radio3.move(10,100)
        self.radio3.adjustSize()
        self.radio4.move(10,150)
        self.radio4.adjustSize()
        self.radio5.move(10,200)
        self.radio5.adjustSize()

        self.buttongroup1.addButton(self.radio1)
        self.buttongroup1.addButton(self.radio2)
        self.buttongroup1.addButton(self.radio3)
        self.buttongroup2.addButton(self.radio4)
        self.buttongroup2.addButton(self.radio5)

        self.radio1.toggled.connect(self.button_selected)
        self.radio2.toggled.connect(self.button_selected)
        self.radio3.toggled.connect(self.button_selected)
        self.radio4.toggled.connect(self.button_selected)
        self.radio5.toggled.connect(self.button_selected)

    def button_selected(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} was clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())