from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class Morphing_Label(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Morphing_Label, self).__init__(parent)

        # Attributs pour le changement de couleures

        self.caseTypes = ["black", "white", "red"]
        self.currentState = 0
        # Box Mettant en place la grid
        self.container = QtWidgets.QGroupBox(self)
        self.container.setStyleSheet(
            "background-color: "+self.caseTypes[self.currentState]+";")
        self.container.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setLayout(self.labelLayout)

        # Rempli le minilabel avec un chiffre si c'est une solution possible , sinon le laisse vide

        self.swapMenu = QtWidgets.QGroupBox(self)
        self.swapMenuLayout = QtWidgets.QHBoxLayout()
        self.swapMenu.setLayout(self.swapMenuLayout)

        self.buttonPrecedent = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")

        self.swapMenuLayout.addWidget(self.buttonPrecedent)
        self.swapMenuLayout.addWidget(QtWidgets.QLabel("  "))
        self.swapMenuLayout.addWidget(self.buttonNext)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.swapMenu)

    def changeCaseTypes(self):
        self.currentState += 1
