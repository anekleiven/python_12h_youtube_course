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

        # add text label 
        label = QLabel("Hei din luring", self) 
        label.setFont(QFont("Arial", 25)) 
        label.setGeometry(0,0, 500, 100)
        label.setStyleSheet("color: #d4778e;"
                            "background-color: #f2d1b8;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        #label.setAlignment(Qt.AlignTop)                        # Vertically top 
        #label.setAlignment(Qt.AlignBottom)                     # Vertically bottom 
        #label.setAlignment(Qt.AlignVCenter)                    # Vertifally center 
        #label.setAlignment(Qt.AlignRight)                      # Horizontally right 
        #label.setAlignment(Qt.AlignHCenter)                    # Horizontally center 
        #label.setAlignment(Qt.AlignLeft)                       # Horizontally left 
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)      # Center and top 
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)   # Center and bottom 
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # Center vertically and horizontally
        label.setAlignment(Qt.AlignCenter)

def main(): 
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main() 
