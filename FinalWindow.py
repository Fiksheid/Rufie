from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtWidgets import *

class FinalWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    
  def set_appear(self):
    self.setWindowTitle('Final Window')
    self.resize(600,400)
  def initUI(self):
    self.main_layout=QVBoxLayout()

    self.text1=QLabel('текст1')
    self.text2=QLabel('текст2')
    self.main_layout.addWidget(self.text1,alignment=Qt.AlignCenter)
    self.main_layout.addWidget(self.text2,alignment=Qt.AlignCenter)

    self.setLayout(self.main_layout)

