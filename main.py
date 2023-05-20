from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtWidgets import *
from SecondWin import *
from FinalWindow import *
 
app = QApplication([])
 
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.look()
        self.initUI()
        self.connect()
 
    def look(self):
        self.setWindowTitle('1st screen')
        self.resize(600,400)
 
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.hello_text = QLabel('Hello\nhello\nhello')
        self.instruction_text = QLabel('Long text')
        self.button = QPushButton('Start')
        self.main_layout.addWidget(self.hello_text)
        self.main_layout.addWidget(self.instruction_text)
        self.main_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)
 
    def connect(self):
 
        self.button.clicked.connect(self.next_screen)
 
    def next_screen(self):
        self.hide()
        self.second_screen = SecondWin()
        self.second_screen.show()
 
main_win = MainWin()
main_win.show()
app.exec_()