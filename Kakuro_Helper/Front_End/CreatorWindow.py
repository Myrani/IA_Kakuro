import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Divided_Label_Widget import *


class CreatorWindow(QtWidgets.QWidget):
    def __init__(self, kakuro, dictionnaire_Des_Sommes):
        super(CreatorWindow, self).__init__()

        # Setup des paramêtres basique de la fenêtre principale
        self.kakuro = kakuro
        self.dictionnaire = dictionnaire_Des_Sommes
        self.title = 'Kakuro Helper'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 700
        self.initUI(self.kakuro, self.dictionnaire)

    def initUI(self, kakuro, dictionnaire_Des_Sommes):

        self.setStyleSheet("background-color: white;")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Création de la VBox Qui tiendra tout les éléments
        self.windowLayout = QtWidgets.QGridLayout()

        # Génération des VBox et de leurs layout qu'on récupéra après via un attbribut de l'objet
        self.createKakuroSolverLayout(kakuro, dictionnaire_Des_Sommes)
        self.createMenuLayout()

        # Ajout des VBoxs Crées au Layout Principal
        self.windowLayout.addWidget(self.menuGroupBox, 0, 0, 1, 0)
        self.windowLayout.addWidget(self.interfaceGroupBox, 1, 0, 6, 6)

        # Assosiation du Layout et de fenêtre
        self.setLayout(self.windowLayout)

        # Montrer le tout !
        self.show()

    def createMenuLayout(self):
        self.menuGroupBox = QtWidgets.QGroupBox(self)
        menuLayout = QtWidgets.QHBoxLayout()

        solver_To_creator_BTN = QtWidgets.QPushButton("To Solver's Side", self)

        menuLayout.addWidget(solver_To_creator_BTN)
        self.menuGroupBox.setLayout(menuLayout)

    def createKakuroSolverLayout(self, kakuro, dictionnaire_Des_Sommes):
        # grid layout + nom
        self.interfaceGroupBox = QtWidgets.QGroupBox(self)
        layout = QtWidgets.QGridLayout()

        # Aucun espace entre les cases
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        # Rajout des cases en fonction du kakuro backend fourni à l'instatiation !!
        # Double for pour parcour des cases
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[x])):

                # Changement du contenu de la case en fonction des values [0] et [1] du modèle backend

                # Cas des Cases Void
                if kakuro[x][y][0] == "#|#" or kakuro[x][y][0] == "H|#":
                    label = QtWidgets.QLabel(self)
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    layout.addWidget(label, x, y)
                    # label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Void.png);background-repeat: no-repeat;")
                    label.setStyleSheet("background-color : black;")

                # Cas des Cases jouables
                elif kakuro[x][y][0] == "   ":

                    # On passe en argument les valeurs trouvées par le mapping des values possibles stockées dans le back-end
                    label = DividedLabel(
                        kakuro[x][y][2], dictionnaire_Des_Sommes)
                    # Couleur d'arrière plan en fonction du heatmapping stocké en [1]
                    label.setStyleSheet(
                        "background-color : rgb("+str(255-int(kakuro[x][y][1]))+",0,0);")
                    layout.addWidget(label, x, y)  # Rajout à la Grid

                # Cas des cases de contraintes du Kakuro
                else:
                    label = QtWidgets.QLabel(
                        kakuro[x][y][0].replace("|", "\\").replace("H", "#"))
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    layout.addWidget(label, x, y)

        self.interfaceGroupBox.setLayout(layout)
