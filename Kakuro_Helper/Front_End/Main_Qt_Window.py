
import sys
import os

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


from Front_End.Divided_Label_Widget import DividedLabel



class App(QtWidgets.QWidget):

    # init des infos basiques de la window
    def __init__(self,kakuro):
        super().__init__()
        self.kakuro = kakuro
        self.title = 'Kakuro Helper'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 600
        self.initUI(self.kakuro)

        
        
    def initUI(self,kakuro):

        self.setStyleSheet("background-color: white;")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground) <-- background transparent sympa
        self.createGridLayout(kakuro)

        # Setup du design en grid 
        windowLayout = QtWidgets.QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox) 
        self.setLayout(windowLayout)
        
        
        # Montrer le tout !
        self.show()
    
    # Coeur du setup du design en grid 
    def createGridLayout(self,kakuro):
        # grid layout + nom
        self.horizontalGroupBox = QtWidgets.QGroupBox(self)
        layout = QtWidgets.QGridLayout()
        
        # Aucun espace entre les cases
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)
        
        # Rajout des cases en fonction du kakuro backend fourni à l'instatiation !!
        # Double for pour parcour des cases
        for x in range(0,len(kakuro)):        
            for y in range(0,len(kakuro[x])):

                # Changement du contenu de la case en fonction des values [0] et [1] du modèle backend 
                
                # Cas des Cases Void 
                if kakuro[x][y][0] == "#|#" or kakuro[x][y][0] == "H|#" :
                    label = QtWidgets.QLabel(self)
                    layout.addWidget(label,x,y)
                    #label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Void.png);background-repeat: no-repeat;")
                    label.setStyleSheet("background-color : black;")
                
                # Cas des Cases jouables
                elif kakuro[x][y][0] == "   ":
                    ###Version avec poid en description
                    #label = QLabel(str(kakuro[x][y][1]),self)
                    
                    #Version case vide
                    label = DividedLabel(self)
                    label.setStyleSheet("background-color : rgb("+str(255-int(kakuro[x][y][1]))+",0,0);") # Couleur d'arrière plan en fonction du heatmapping stocké en [1]
                    layout.addWidget(label,x,y)
                
                # Cas des cases de contraintes du Kakuro
                else:
                    layout.addWidget(QtWidgets.QLabel(kakuro[x][y][0].replace("|","\\").replace("H","#")),x,y)

        
        self.horizontalGroupBox.setLayout(layout)
