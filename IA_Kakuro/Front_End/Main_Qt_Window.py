
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self,kakuro):
        super().__init__()
        self.kakuro = kakuro
        self.title = 'Kakuro Helper'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 250
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
        self.horizontalGroupBox = QGroupBox("Kakuro")
        layout = QGridLayout()
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)
        for x in range(0,len(kakuro)):        
            for y in range(0,len(kakuro[x])):
                if kakuro[x][y][0] == "#|#":
                    label = QLabel(self)
                    layout.addWidget(label,x,y)
                    label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Void.png)")

                elif kakuro[x][y][0] == "   ":
                    label = QLabel(self)
                    layout.addWidget(label,x,y)
                    label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Playable.png)")
                else:
                    layout.addWidget(QLabel(kakuro[x][y][0].replace("|","\\").replace("H","#")),x,y)

        
        self.horizontalGroupBox.setLayout(layout)
