from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class Morphing_Label(QtWidgets.QWidget):

    def __init__(self, x, y, kakuro, parent=None):
        super(Morphing_Label, self).__init__(parent)

        # Attributs pour le changement de couleures
        self.caseColors = ["black", "white", "red"]
        self.caseTypes = ["#|#", "   ", "4\\4"]
        self.currentState = self.caseTypes.index(kakuro[x][y][0])
        self.x = x
        self.y = y
        # Box Mettant en place la grid
        self.container = QtWidgets.QGroupBox(self)
        self.container.setStyleSheet(
            "background-color: "+self.caseColors[self.caseTypes.index(kakuro[x][y][0])]+";")
        self.container.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setLayout(self.labelLayout)

        # Rempli le minilabel

        self.swapMenu = QtWidgets.QGroupBox(self)
        self.swapMenuLayout = QtWidgets.QHBoxLayout()
        self.swapMenu.setLayout(self.swapMenuLayout)

        self.buttonPrecedent = QtWidgets.QPushButton("<")
        self.buttonNext = QtWidgets.QPushButton(">")

        self.buttonPrecedent.clicked.connect(
            lambda: self.changeCaseTypes(-1))

        self.buttonNext.clicked.connect(
            lambda: self.changeCaseTypes(1))

        self.swapMenuLayout.addWidget(self.buttonPrecedent)
        self.swapMenuLayout.addWidget(QtWidgets.QLabel("  "))
        self.swapMenuLayout.addWidget(self.buttonNext)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.swapMenu)

    def changeCaseTypes(self, value):
        print(self.currentState)
        self.currentState += value
        print(self.currentState)

        if self.currentState == 3:
            self.currentState = 0
        elif self.currentState == -1:
            self.currentState = 2
        else:
            pass

        print(self.currentState)
        self.nativeParentWidget(
        ).creatorKakuro[self.x][self.y][0] = self.caseTypes[self.currentState]

        print(self.nativeParentWidget().creatorKakuro)
        self.nativeParentWidget().startCreatorWindow()
