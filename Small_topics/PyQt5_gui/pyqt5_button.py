from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys 

class MainWindow(QMainWindow):
    # After the constructor ends all the things inside it are deleted so inorder to protect button object 
    # we do self.button which makes it exist even after the constructor end 
    # so does doing self.smt make it a class attribute or method 
    # btw you also said that that self.button is an attribute but its an object how can an object be attribute
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.button = QPushButton("click me",self)
        self.label = QLabel("Hello",self)
        # self is telling this button belongs to this window
        self.initUI()
        # so is it calling the initUI method on this window or we are accessing the initUI method form this window

    def initUI(self):
        self.button.setGeometry(50,50,200,200)
        self.button.setStyleSheet("font-size: 30px;")
        # is this saying we are connecting the method of this window or that we are accessing the button click method from this window because you know . is access operaotr
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        print("Button was clicked")
        self.label.setText("Goodbye")
        self.button.setText("Clicked")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()