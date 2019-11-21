import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
from math import *
from PyQt5 import uic


# Код cicle.ui
'''
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>480</width>
    <height>435</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>170</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>480</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.x = None
        self.y = None           
        uic.loadUi('circle.ui', self)
        
        self.pushButton.clicked.connect(self.update_paint)
        
    def update_paint(self):
        self.update()
        
    def draw_crl(self, qp):
        self.x = randint(0, self.size().width())
        self.y = randint(0, self.size().height())

        color = (255, 255, 0)
        size = randint(5, 200)
        pen = QPen(Qt.yellow)
        qp.begin(self)
        qp.setPen(pen)
        qp.setBrush(Qt.yellow)
        qp.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)
        qp.end()        

    def paintEvent(self, event):
        qp = QPainter()
        self.draw_crl(qp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())