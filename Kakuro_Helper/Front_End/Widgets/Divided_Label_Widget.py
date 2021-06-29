from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Widgets.Content_Button_Widget import ContentButton
from Back_End.Logic.Grid_Logic import terminalPrintFull


class DividedLabel(QtWidgets.QWidget):

    def __init__(self, possibleValues, constraints, selected, x, y):
        super().__init__()

        # Contraintes d'analyses importées du back-end

        # Box Mettant en place la grid
        self.x = x
        self.y = y
        self.selected = selected

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
        print(possibleValues)
        self.possibleSetValues = [
            value for value in possibleValues if value not in constraints]
        # Rempli le minilabel avec un chiffre si c'est une solution possible , sinon le laisse vide
        cpt = 1
        for i in range(0, 3):
            for j in range(0, 3):
                if cpt in self.possibleSetValues:
                    if cpt in self.selected:
                        minibutton = ContentButton(
                            str(cpt), self.x, self.y, True)
                    else:
                        minibutton = ContentButton(
                            str(cpt), self.x, self.y, False)
                    self.labelLayout.addWidget(minibutton, i, j)
                    cpt += 1
                else:
                    minilabel = QtWidgets.QLabel("   ")
                    minilabel.setAlignment(QtCore.Qt.AlignCenter)
                    self.labelLayout.addWidget(minilabel, i, j)
                    cpt += 1

        self.layout.addWidget(self.label)
