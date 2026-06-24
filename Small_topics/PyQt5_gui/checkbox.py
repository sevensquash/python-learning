from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.checkbox = QCheckBox("Do you like pizza",self)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Pizza! 🍕", self.widget)
        self.label.setStyleSheet("font-size: 40px; font-family: Arial;")

        self.checkbox.setStyleSheet("font-family: Arial; font-size: 40px;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checked_box)

        layout.addWidget(self.label)
        layout.addWidget(self.checkbox)

        self.widget.setLayout(layout)
        

    def checked_box(self, state):
        if state == Qt.Checked:
            self.label = QLabel("Pizza! 🍕", self.widget)
            print("Yay")
        else:
            print("Noooo")
            self.label.setText("Noo Pizza! eat apple 🍎")

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()