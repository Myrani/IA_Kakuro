
import sys
import os
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
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

        self.setStyleSheet("background-color: white;")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.opacity_effect = QGraphicsOpacityEffect()
  
        # setting opacity level
        self.opacity_effect.setOpacity(0.1)
  
 
        
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
                if kakuro[x][y][0] == "#|#" or kakuro[x][y][0] == "H|#" :
                    label = QLabel(self)
                    layout.addWidget(label,x,y)
                    label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Void.png);background-repeat: no-repeat;")

                elif kakuro[x][y][0] == "   ":
                    label = QLabel(str(kakuro[x][y][1]),self)
                    label.setStyleSheet("background-color : rgb("+str(255-int(kakuro[x][y][1]))+",0,0);")
                    layout.addWidget(label,x,y)
                    
                else:
                    layout.addWidget(QLabel(kakuro[x][y][0].replace("|","\\").replace("H","#")),x,y)

        
        self.horizontalGroupBox.setLayout(layout)
