from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
import sys

icon_path = r"python_learning\Small_topics\PyQt5_gui\nanami.jpg"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.setWindowIcon(QIcon(icon_path))
        label = QLabel(self)
        x = (self.width() - label.width()) // 2
        y = (self.height() - label.height()) // 2
        label.setGeometry(x,y,label.width(),label.height())
        label.setPixmap(QPixmap(r"python_learning\Small_topics\PyQt5_gui\nanami.jpg"))
        label.setScaledContents(True)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QIcon, QFont, QPixmap
# from PyQt5.QtCore import Qt

# file_path = r"C:\Users\User\python\python_learning\Small_topics\PyQt5_gui\nanami.jpg"
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(0,0,500,500)
#         self.setWindowIcon(QIcon(file_path))
#         label = QLabel("Hello World",self)
#         label.setFont(QFont("Arial",50))
#         label.setStyleSheet("color: blue; background-color: grey; font-style: italic; font-weight: bold; text-decoration: underline")
#         label.adjustSize()
#         x = (self.width() - label.width()) // 2
#         y = (self.height() - label.height()) // 2
#         label.move(x, y)


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

# import sys 
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(0,0,500,500)
#         self.setWindowIcon(QIcon(r"python_learning\Small_topics\PyQt5_gui\nanami.jpg"))

# def main():
#     apps = QApplication(sys.argv)
#     print(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(apps.exec_())

# if __name__ == "__main__":
#     main()


# # sys - lets python interact with os
# import sys
# # QApplication - the city that manages all the restaurant, engine 
# # QApplication - controls the entire GUI application
# # QMainWindow - a ready made empty window class which you can customize, the window you see
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon

# #MainWindow - your restaurant
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # creates the real window behind the scenes
#         # sets up internal C++ objects
#         # enables features like resizing, painting, events
#         self.setGeometry(0,0,500,500)
#         self.setWindowIcon(QIcon(r"python_learning\Small_topics\PyQt5_gui\nanami.jpg"))
#         # That is equivalent to QMainWindow.__init__(self)
#         # So Python automatically supplies the current instance (self) for you.

# def main():
#     # Creates the application object.
#     apps = QApplication(sys.argv)
#     window = MainWindow()
#     # creates a new object called window

#     window.show()
#     sys.exit(apps.exec_())
#     # exec checks for events like click, exit etc continuously 
#     # when window closes apps.exec_() returns an exit code

# if __name__ == "__main__":
#     main()

# import sys 
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon 

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(0,0,500,500)
#         self.setWindowIcon(QIcon(r"python_learning\Small_topics\PyQt5_gui\nanami.jpg"))

# def main():
#     apps = QApplication(sys.argv)
#     window = QMainWindow()
#     window.show()
#     sys.exit(apps.exec_())

# if __name__ == "__main__":
#     main()