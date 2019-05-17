import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
 
class Figure(QGraphicsPixmapItem):
    def __init__(self, parent = None, color = None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.color = color
 
    def __str__(self):
        return 'figure'
 
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.oldRect = 0
        self.x = 0
        self.y = 0 
        self.oldx = 0
        self.oldy = 0   
        self.oldFigures = None
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView()
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setSceneRect(0, 0, 800, 800)
        self.setCentralWidget(self.graphics_view) 
        self.DrawMap()        
 
    def initUI(self):    
        self.setGeometry(300, 100, 802, 802)
        self.setWindowTitle('chess')
        self.show()      

    def DrawMap(self):
        for i in range(8): 
            for j in range(8):   
                if (8 - i + 1 + j) % 2 == 0:
                    Rect = QGraphicsRectItem(i*100, j*100, 100, 100)
                    Rect.setBrush(QColor(101, 67, 33))
                else:
                    Rect = QGraphicsRectItem(i*100, j*100, 100, 100)
                    Rect.setBrush(QColor(255, 255, 255)) 
                self.scene.addItem(Rect)   

        pawnW1 = Figure(QPixmap('/git/chess/figures/bP.png').scaled(99, 99), 'black')
        pawnW1.setOffset(300, 300)
        self.scene.addItem(pawnW1)  

    def paintEvent(self, e):                   
        if self.oldRect != 0:
            self.scene.removeItem(self.oldRect)
        Rect = QGraphicsRectItem(self.x, self.y, 100, 100)
        Rect.setPen(QPen(Qt.red,  2,))
        self.scene.addItem(Rect)
        self.flag = False
        self.oldRect = Rect

    def mousePressEvent(self, event):     
        self.x = int(event.pos().x() / 100) * 100
        self.y = int(event.pos().y() / 100) * 100
  
        serh = True
        it = self.graphics_view.items(self.x + 50, self.y + 50)
        for k in it:
            if str(k) == 'figure':
                self.oldFigures = k
                serh = False
        if serh and self.oldFigures != None:
            self.oldFigures.setOffset(self.x, self.y)
            self.oldFigures = None           
        
        self.oldx = self.x
        self.oldy = self.y 
        self.update() 
 
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())