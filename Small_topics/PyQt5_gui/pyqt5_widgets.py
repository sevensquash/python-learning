import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout)
# QVBoxLayout does NOT mean widgets become vertical in shape it means widgets are stacked vertically on eachother 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("apple",self)
        label2 = QLabel("dog",self)
        label3 = QLabel("polonium",self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: green")

        grid = QGridLayout()

        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)

        central_widget.setLayout(grid)
    
def main():
    apps = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(apps.exec_())

if __name__ == "__main__":
    main()