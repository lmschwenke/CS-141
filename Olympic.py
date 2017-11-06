import sys
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Olympic(QWidget):

  def __init__(self):
    super().__init__()           
    self.setGeometry(300, 300, 550, 600)
    self.setWindowTitle('Olympic Rings')
    self.show()
  
  def mousePressEvent(self, event):
    
    self.x = event.x()
    self.y = event.y()
    
    x = self.x
    y = self.y 
    
    #Blue
    center_x = 153
    center_y = 148
    if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
      self.event = 1
      center_x = 208
      center_y = 206
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 6 #BlueYellow
    else:
      self.event = 10 #Anything outside of a ring, print nothing.
        
    #Yellow
    center_x = 206
    center_y = 208
    if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
      self.event = 2
      center_x = 263
      center_y = 148
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 7
      center_x = 153
      center_y = 148
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 6 #YellowBlack
        
    #Black
    center_x = 263
    center_y = 148
    if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
      self.event = 3
      center_x = 318
      center_y = 206
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 8
      center_x = 206
      center_y = 208
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 7 #BlackGreen
    
    #Green
    center_x = 318
    center_y = 209
    if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
      self.event = 4
      center_x = 373
      center_y = 148
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 9
      center_x = 263
      center_y = 148
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 8 #GreenRed
        
    #RedRing
    center_x = 373
    center_y = 148
    if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
      self.event = 5
      center_x = 318  
      center_y = 209
      if((x-center_x)**2 + (y-center_y)**2) <= 47.5**2:
        self.event = 9 #RedGreen
      
    self.update()
  def paintEvent(self, event):
    qp = QPainter()
    qp.begin(self)
    #Draw things here
    pen1 = QPen(QBrush(Qt.blue), 6)
    pen2 = QPen(QBrush(Qt.yellow), 6)
    pen3 = QPen(QBrush(Qt.black), 6)
    pen4 = QPen(QBrush(Qt.green), 6)
    pen5 = QPen(QBrush(Qt.red), 6)
    qp.setPen (pen1)  
    qp.drawEllipse (105, 100, 95, 95)
    qp.setPen (pen2)  
    qp.drawEllipse (160, 160, 95, 95)
    qp.setPen (pen3)    
    qp.drawEllipse (215, 100, 95, 95)
    qp.setPen (pen4)  
    qp.drawEllipse (270, 160, 95, 95)
    qp.setPen (pen5)  
    qp.drawEllipse (325, 100, 95, 95)
    
    ring = self.event
    
    if ring == 1:
        qp.setPen (pen1) #Draw in this color
        qp.setBrush(QBrush(Qt.blue)) #Fill the rectangle in this color
        qp.drawRect (100, 300, 350, 80)

    elif ring == 6:
        qp.setPen (pen1)
        qp.setBrush(QBrush(Qt.blue))
        qp.drawRect (100, 300, 175, 80)
        qp.setPen (pen2)
        qp.setBrush(QBrush(Qt.yellow))
        qp.drawRect (250, 300, 175, 80)

    elif ring == 2:
        qp.setPen (pen2)
        qp.setBrush(QBrush(Qt.yellow))
        qp.drawRect (100, 300, 350, 80)

    elif ring == 7:
        qp.setPen (pen2)
        qp.setBrush(QBrush(Qt.yellow))
        qp.drawRect (100, 300, 175, 80)
        qp.setPen (pen3)
        qp.setBrush(QBrush(Qt.black))
        qp.drawRect (250, 300, 175, 80)
  
    elif ring == 3:
        qp.setPen (pen3)
        qp.setBrush(QBrush(Qt.black))
        qp.drawRect (100, 300, 350, 80)

    elif ring == 8:
        qp.setPen (pen3)
        qp.setBrush(QBrush(Qt.black))
        qp.drawRect (100, 300, 175, 80)
        qp.setPen (pen4)
        qp.setBrush(QBrush(Qt.green))
        qp.drawRect (250, 300, 175, 80)

    elif ring == 4:
        qp.setPen (pen4)
        qp.setBrush(QBrush(Qt.green))
        qp.drawRect (100, 300, 350, 80)

    elif ring == 9:
        qp.setPen (pen4)
        qp.setBrush(QBrush(Qt.green))
        qp.drawRect (100, 300, 175, 80)
        qp.setPen (pen5)
        qp.setBrush(QBrush(Qt.red))
        qp.drawRect (250, 300, 175, 80)

    elif ring == 5:
        qp.setPen (pen5)
        qp.setBrush(QBrush(Qt.red))
        qp.drawRect (100, 300, 350, 80)
        
    qp.end()
    
if __name__ == '__main__':  
  app = QApplication(sys.argv)
  ex = Olympic()
  sys.exit(app.exec_())
  
self.show()  
  