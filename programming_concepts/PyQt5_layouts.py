# PyQt5 layouts

import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, 
                             QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__() 
        self.setGeometry(0,0,500,500) 
        self.initUI()
    
    # user interface
    def initUI(self):                           
        central_widget = QWidget() 
        self.setCentralWidget(central_widget) 

        label1 = QLabel("#1", self) 
        label2 = QLabel("#2", self) 
        label3 = QLabel("#3", self) 
        label4 = QLabel("#4", self) 
        label5 = QLabel("#5", self) 

        label1.setStyleSheet("background-color: #ed7c74;")
        label2.setStyleSheet("background-color: #e8aea9;")
        label3.setStyleSheet("background-color: #c4271a;")
        label4.setStyleSheet("background-color: #663f3c;")
        label5.setStyleSheet("background-color: #fcd9d7;")

        # vertical layout manager 
       
        #vbox = QVBoxLayout()

        #vbox.addWidget(label1) 
        #vbox.addWidget(label2) 
        #vbox.addWidget(label3) 
        #vbox.addWidget(label4) 
        #vbox.addWidget(label5) 

        #central_widget.setLayout(vbox) 

        # horizontal layout manager 

        #hbox = QHBoxLayout() 

        #hbox.addWidget(label1)
        #hbox.addWidget(label2)
        #hbox.addWidget(label3)
        #hbox.addWidget(label4)
        #hbox.addWidget(label5) ¨

        #central_widget.setLayout(hbox)

        # grid layout 

        grid = QGridLayout() 

        grid.addWidget(label1,0,0) 
        grid.addWidget(label2,0,1) 
        grid.addWidget(label3,1,1) 
        grid.addWidget(label4,1,2) 
        grid.addWidget(label5,3,3)

        central_widget.setLayout(grid) 


    
def main(): 
    app = QApplication(sys.argv) 
    window = MainWindow() 
    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__": 
    main() 

    