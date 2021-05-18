from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Widgets.Content_Button_Widget import ContentButton


class DividedLabel(QtWidgets.QWidget):

    def __init__(self, specs, dictionnaire_Des_Sommes):
        super().__init__()

        # Contraintes d'analyses importées du back-end
        self.specs = specs

        print(self.specs)
        # Box Mettant en place la grid
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.labelLayout.setHorizontalSpacing(-5)
        self.labelLayout.setVerticalSpacing(-5)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)

        self.label.setLayout(self.labelLayout)

        self.possibleSetValues = self.findCommonNumberForLength(
            dictionnaire_Des_Sommes, self.specs)

        # Rempli le minilabel avec un chiffre si c'est une solution possible , sinon le laisse vide
        cpt = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if cpt in self.possibleSetValues:
                    minibutton = ContentButton(str(cpt))
                    self.labelLayout.addWidget(minibutton, i, j)
                    cpt += 1
                else:
                    minilabel = QtWidgets.QLabel("   ")
                    minilabel.setAlignment(QtCore.Qt.AlignCenter)
                    self.labelLayout.addWidget(minilabel, i, j)
                    cpt += 1

        self.layout.addWidget(self.label)

    def findCommonNumberForLength(self, dictionnaire_Des_Sommes, specs):

        set_One = []  # Futur set des solutions pour la contrainte de Ligne
        set_Two = []  # Futur set des solutions pour la contrainte de Colonnes

        # Tri des solutions possibles en fonction des de cases à remplir : Ligne
        for combinaison_First in dictionnaire_Des_Sommes[int(specs[0][0])]:
            if len(combinaison_First) == specs[0][1]:
                for el in combinaison_First:
                    set_One.append(el)

        # Tri des solutions possibles en fonction des de cases à remplir : Colonne
        if len(specs) > 1:
            for combinaison_Second in dictionnaire_Des_Sommes[int(specs[1][0])]:
                if len(combinaison_Second) == int(specs[1][1]):
                    for el in combinaison_Second:
                        set_Two.append(el)
        # Transformation en Set
        set_One = set(set_One)
        set_Two = set(set_Two)

        # Retourne la jointure des 2 Sets, Donc les éléments communs au 2 ensembles de solutions !
        if len(specs) > 1:
            return set_One & set_Two
        else:
            return set_One
