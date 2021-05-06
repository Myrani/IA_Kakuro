
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self,kakuro):
        super().__init__()
        self.kakuro = kakuro
        self.title = 'Kakuro Helper'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI(self.kakuro)

        
        
    def initUI(self,kakuro):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout(kakuro)

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
    

    def createGridLayout(self,kakuro):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()

        for x in range(0,len(kakuro)):        
            for y in range(0,len(kakuro[x])):
                layout.addWidget(QLabel(kakuro[x][y][0]),x,y)

        
        self.horizontalGroupBox.setLayout(layout)