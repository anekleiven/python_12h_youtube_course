# PyQt5 CSS styles 
# CSS = Cascading Style Sheets 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 30px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1 {
                background-color: hsl(307, 27%, 85%);
            }
            QPushButton#button2 {
                background-color: hsl(306, 47%, 77%);
            }
            QPushButton#button3 {
                background-color: hsl(307, 57%, 67%);
            }
            QPushButton#button1:hover {
                background-color: hsl(307, 27%, 65%);
            }
            QPushButton#button2:hover {
                background-color: hsl(306, 47%, 57%);
            }
            QPushButton#button3:hover {
                background-color: hsl(307, 57%, 47%);
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # ✅ Use Fusion style for hover effects
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())