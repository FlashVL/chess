import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QImage
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.x = 0
        self.y = 0    
    def initUI(self):    
        self.setGeometry(300, 100, 800, 800)
        self.setWindowTitle('chess')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        if self.flag:
            self.paint = QPainter()
            self.paint.begin(self)
            self.paint.setPen(QPen(Qt.red,  2,))
            self.paint.drawRect(self.x, self.y, 100, 100)
            self.paint.end()
            self.flag = False

        painter = QPainter(self)
        painter.drawImage(0, 100, QImage('/git/chess/figures/bP.png').scaled(100, 100))
        painter.end()

    def drawRectangles(self, qp):

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        k = 0
        for i in range(8): 
            for j in range(8):   
                if (8 - i + 1 + j) % 2 == 0:
                    qp.setBrush(QColor(101, 67, 33))
                    qp.drawRect(i*100, j*100, 100, 100)
                    k = 1
                else:
                    qp.setBrush(QColor(255, 255, 255))
                    qp.drawRect(i*100, j*100, 100, 100)               
                    k = 0

    def mousePressEvent(self, event):      
        self.x = int(event.pos().x() / 100) * 100
        self.y = int(event.pos().y() / 100) * 100
        self.flag = True
        self.update()   

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())