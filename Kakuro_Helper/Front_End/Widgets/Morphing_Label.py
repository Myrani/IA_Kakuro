from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class Morphing_Label(QtWidgets.QWidget):

    def __init__(self, x, y, kakuro, parent=None):
        super(Morphing_Label, self).__init__(parent)

        # Attributs pour le changement de couleures
        self.caseColors = ["black", "white", "red"]
        self.caseTypes = ["#|#", "   ", "4|4"]
        # Changement de l'index en fonction de la valeur trouvé dans le kakuro back-end
        self.currentState = self.caseTypes.index(kakuro[x][y][0])
        # + Stockage des indices de la case actuelle
        self.x = x
        self.y = y
        # Container mettant en place la VBox + cutsomisation de la VBox
        # en fonction du contenu du kakuro backend
        self.container = QtWidgets.QGroupBox(self)
        self.container.setStyleSheet(
            "background-color: "+self.caseColors[self.caseTypes.index(kakuro[x][y][0])]+";")
        self.container.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        # Label Permettant L'écart du haut // à remplacé dasn certain futurs cas
        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setLayout(self.labelLayout)

        # Création d'un Menu pour swap le type de case

        # Juste une HBox avec 2 boutons et 1 label entre les 2
        self.swapMenu = QtWidgets.QGroupBox(self)
        self.swapMenuLayout = QtWidgets.QHBoxLayout()
        self.swapMenu.setLayout(self.swapMenuLayout)

        self.buttonPrecedent = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")

        # Reliage à une fonction mettant à jour le contenu de currentState +changement du kakuro back-end+ Refresh de la page
        self.buttonPrecedent.clicked.connect(
            lambda: self.changeCaseTypes(-1))

        self.buttonNext.clicked.connect(
            lambda: self.changeCaseTypes(1))

        # Rajout a Layout du menu
        self.swapMenuLayout.addWidget(self.buttonPrecedent)
        self.swapMenuLayout.addWidget(QtWidgets.QLabel("  "))
        self.swapMenuLayout.addWidget(self.buttonNext)

        # Rajout du Label Ligne 28 et du menu dans le layout du container
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.swapMenu)

    def changeCaseTypes(self, value):
        # En fonction du bouton +1 ou -1 au currentState (Index)
        self.currentState += value

        # Handle les cas ou l'index se barre pour le mettre à l'autre bout de la liste
        if self.currentState == 3:
            self.currentState = 0
        elif self.currentState == -1:
            self.currentState = 2
        else:
            pass

        # Stockage de la nouvelle valeure en fonction de l'index dans le kakuro back-end
        # se trouvant dans la MainWindow
        self.nativeParentWidget(
        ).creatorKakuro[self.x][self.y][0] = self.caseTypes[self.currentState]

        # Refresh la page et activant la fonction de création de PageCreateur de MainWindow !
        self.nativeParentWidget().startCreatorWindow()
