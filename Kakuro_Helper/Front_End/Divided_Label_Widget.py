from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Content_Button import ContentButton


class DividedLabel(QtWidgets.QWidget):

    def __init__(self, specs, dictionnaire_Des_Sommes):
        super().__init__()

        # Contraintes d'analyses importées du back-end
        self.specs = specs

        # Box Mettant en place la grid
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.labelLayout.setHorizontalSpacing(8)
        self.labelLayout.setVerticalSpacing(0)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)

        self.label.setLayout(self.labelLayout)

        self.possibleSetValues = self.findCommonNumberForLength(
            self.specs[0][0], self.specs[0][1], self.specs[1][0], self.specs[1][1], dictionnaire_Des_Sommes)

        # Rempli le minilabel avec un chiffre si c'est une solution possible , sinon le laisse vide
        cpt = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if cpt in self.possibleSetValues:
                    minibutton = ContentButton(str(cpt))
                    self.labelLayout.addWidget(minibutton, i, j)
                    cpt += 1
                else:
                    minilabel = QtWidgets.QLabel("")
                    minilabel.setAlignment(QtCore.Qt.AlignCenter)
                    self.labelLayout.addWidget(minilabel, i, j)
                    cpt += 1

        self.layout.addWidget(self.label)

    def findCommonNumberForLength(self, firstNumber, firstLen, secondNumber, secondLen, dictionnaire_Des_Sommes):

        set_One = []  # Futur set des solutions pour la contrainte de Ligne
        set_Two = []  # Futur set des solutions pour la contrainte de Colonnes

        # Tri des solutions possibles en fonction des de cases à remplir : Ligne
        for combinaison_First in dictionnaire_Des_Sommes[int(firstNumber)]:
            if len(combinaison_First) == firstLen:
                for el in combinaison_First:
                    set_One.append(el)

        # Tri des solutions possibles en fonction des de cases à remplir : Colonne
        for combinaison_Second in dictionnaire_Des_Sommes[int(secondNumber)]:
            if len(combinaison_Second) == secondLen:
                for el in combinaison_Second:
                    set_Two.append(el)
        # Transformation en Set
        set_One = set(set_One)
        set_Two = set(set_Two)

        # Retourne la jointure des 2 Sets, Donc les éléments communs au 2 ensembles de solutions !
        return set_One & set_Two
