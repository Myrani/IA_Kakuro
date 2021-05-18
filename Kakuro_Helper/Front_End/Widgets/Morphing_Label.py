from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class Morphing_Label(QtWidgets.QWidget):

    def __init__(self, x, y, kakuro, parent=None):
        super(Morphing_Label, self).__init__(parent)

        # Attributs pour le changement de couleures
        self.caseColors = ["black", "white", "red"]
        self.caseTypes = ["#|#", "  | ", "X|X"]
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

        # Box Permettant l'entrée de contraintes par l'utilisateur

        if self.nativeParentWidget().creatorKakuro[self.x][self.y][0] == 'X|X':

            self.inputMenu = QtWidgets.QGroupBox(self)
            self.inputMenuLayout = QtWidgets.QHBoxLayout()
            self.inputMenu.adjustSize()
            self.inputMenu.setLayout(self.inputMenuLayout)

            # Recupère les values qui vont rempir les palces holder des QLineEdits qui récupère les inputs
            try:
                displaySplit = self.nativeParentWidget(
                ).creatorKakuro[self.x][self.y][1].split("|")
                print(displaySplit)
            except Exception as e:
                print(e)
                pass
            # Les remplis
            self.valueFormLeft = QtWidgets.QLineEdit(displaySplit[0])
            self.valueFormRight = QtWidgets.QLineEdit(displaySplit[1])
            # Fixe la Taille ....
            self.valueFormLeft.setSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.valueFormLeft.setFixedSize(15, 15)
            # Modifie dans le Back-end les valeures + Refresh la page
            self.valueFormLeft.textChanged.connect(
                lambda: self.updateCaseValue(self.valueFormLeft.text()+"|"+self.valueFormRight.text()))

            # Fixe la Taille ....
            self.valueFormRight.setSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            self.valueFormRight.setFixedSize(15, 15)
            # Modifie dans le Back-end les valeures + Refresh la page
            self.valueFormRight.textChanged.connect(
                lambda: self.updateCaseValue(self.valueFormLeft.text()+"|"+self.valueFormRight.text()))

            # Ajoute le tout au Layout du menu
            self.inputMenuLayout.addWidget(self.valueFormLeft)
            self.inputMenuLayout.addWidget(QtWidgets.QLabel(" \\"))
            self.inputMenuLayout.addWidget(self.valueFormRight)

            self.inputMenu.adjustSize()
            # Ajoute le tout au container !
            self.layout.addWidget(self.inputMenu)

        # Cas sans inputs
        else:

            self.label = QtWidgets.QLabel()
            self.labelLayout = QtWidgets.QGridLayout()
            self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setStyleSheet("background-color: transparent;")
            self.label.setLayout(self.labelLayout)
            self.layout.addWidget(self.label)

        # Création d'un Menu pour swap le type de case

        # Juste une HBox avec 2 boutons et 1 label entre les 2
        self.swapMenu = QtWidgets.QGroupBox(self)
        self.swapMenuLayout = QtWidgets.QHBoxLayout()
        self.swapMenu.setLayout(self.swapMenuLayout)

        self.buttonPrecedent = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")

        # Reliage à une fonction mettant à jour le contenu de currentState +changement du kakuro back-end+ Refresh de la page
        self.buttonPrecedent.clicked.connect(
            lambda: self.updateCaseType(-1, self.caseTypes[self.currentState]))

        self.buttonNext.clicked.connect(
            lambda: self.updateCaseType(1, self.caseTypes[self.currentState]))

        # Rajout a Layout du menu
        self.swapMenuLayout.addWidget(self.buttonPrecedent)
        self.swapMenuLayout.addWidget(QtWidgets.QLabel("  "))
        self.swapMenuLayout.addWidget(self.buttonNext)

        # Rajout du Label Ligne 28 et du menu dans le layout du container

        self.layout.addWidget(self.swapMenu)

    def updateCaseType(self, value, userInput):
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
        self.updateCaseValue(userInput)
        self.nativeParentWidget().startCreatorWindow()

    def updateCaseValue(self, value):
        self.nativeParentWidget().creatorKakuro[self.x][self.y][1] = value

    def onLineEdit(self, value):
        print(value)
