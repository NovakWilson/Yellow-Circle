import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import *
from math import *
from PyQt5 import uic


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