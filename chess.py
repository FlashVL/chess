import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.oldRect = 0
        self.flag = False
        self.x = 0
        self.y = 0  
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView()
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setSceneRect(0, 0, 800, 800)
        self.setCentralWidget(self.graphics_view)        

    def initUI(self):    
        self.setGeometry(300, 100, 802, 802)
        self.setWindowTitle('chess')
        self.show()

    def paintEvent(self, e):
        for i in range(8): 
            for j in range(8):   
                if (8 - i + 1 + j) % 2 == 0:
                    Rect = QGraphicsRectItem(i*100, j*100, 100, 100)
                    Rect.setBrush(QColor(101, 67, 33))

                else:
                    Rect = QGraphicsRectItem(i*100, j*100, 100, 100)
                    Rect.setBrush(QColor(255, 255, 255)) 
                self.scene.addItem(Rect)                             
        if self.flag:
            if self.oldRect != 0:
                del self.oldRect 
            Rect = QGraphicsRectItem(self.x, self.y, 100, 100)
            Rect.setPen(QPen(Qt.red,  2,))
            self.scene.addItem(Rect)
            self.flag = False
            oldRect = Rect 



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
                self.scene.addItem(qp)

    def mousePressEvent(self, event):     
        self.x = int(event.pos().x() / 100) * 100
        self.y = int(event.pos().y() / 100) * 100
        self.flag = True
        self.update()   
    
    def pawn(self):
        painter = QPainter(self)
        painter.drawImage(0, 100, QImage('/git/chess/figures/bP.png').scaled(100, 100))
        painter.end()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())