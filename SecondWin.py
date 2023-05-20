from PyQt5.QtCore import Qt,QTimer,QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from FinalWindow import *

time=QTime(0,0,15)
class SecondWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    
  def set_appear(self):
    self.setWindowTitle('Second Window')
    self.resize(600,400)

  def initUI(self):
    self.main_layout=QHBoxLayout()
    self.layout1=QVBoxLayout()
    self.layout2=QVBoxLayout()

    self.main_layout.addLayout(self.layout1)
    self.main_layout.addLayout(self.layout2)


    self.fio=QLabel('текст1')
    self.otdih=QLabel('текст2')
    self.let=QLabel('текст3')
    self.prised=QLabel('текст4')
    self.total_otdih=QLabel('текст5')

    self.fiole=QLineEdit()
    self.otdihle=QLineEdit()
    self.letle=QLineEdit()
    self.total=QLineEdit()
    self.final=QLineEdit()

    self.otdihbut=QPushButton('кнопка1')
    self.prisedbut=QPushButton('кнопка2')
    self.total_otdihbut=QPushButton('кнопка3')
    self.result=QPushButton('кнопка4')

    self.text_timer=QLabel(time.toString('hh:mm:ss'))
    
    self.layout1.addWidget(self.fio,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.fiole,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.let,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.letle,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.otdih,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.otdihbut,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.otdihle,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.prised,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.prisedbut,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.total_otdih,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.total_otdihbut,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.total,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.final,alignment=Qt.AlignLeft)
    self.layout1.addWidget(self.result,alignment=Qt.AlignCenter)
    self.layout2.addWidget(self.text_timer,alignment=Qt.AlignRight)

    self.setLayout(self.main_layout)

  def timer1(self):
    global time 
    time=QTime(0,0,15)
    self.timer=QTimer()
    self.timer.timeout.connect(self.timer1Event)
    self.timer.start(1000)

  def timer1Event(self):
    global time
    time=time.addSecs(-1)
    self.text_timer.setText(time.toString("hh:mm:ss"))
    self.text_timer.setFont(QFont("Times",36,QFont.Bold))
    self.text_timer.setStyleSheet("color: rgb (0,0,0")
    if time.toString("hh:mm:ss")=="00:00:00":
      self.timer.stop()

  def connects(self):
    self.otdihbut.clicked.connect(self.timer1)
    #self.prisedbut.clicked.connect(self.timer2)
    #self.total_otdihbut.clicked.connect(self.timer3)
    self.result.clicked.connect(self.next_click)

  def next_click(self):
    self.hide()
    self.third_screen=FinalWin()
    self.third_screen.show()

  def timer_test(self):
    pass
