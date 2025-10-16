# GUI = graphical user interface 

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("My first GUI")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon("ane portrettbilde.jpg")) 

        # add photo label 
        label = QLabel(self)
        
        # size of picture 
        label.setGeometry(0,0,250,250)

        # picture file 
        pixmap = QPixmap("ane portrettbilde.jpg")


        label.setPixmap(pixmap) 
        label.setScaledContents(True)

        # place picture in center 
        label.setGeometry((self.width() - label.width()) // 2,
                        (self.height() - label.height()) // 2, 
                        label.width(), 
                        label.height())

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main() 
