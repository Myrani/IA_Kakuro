import sys

from PyQt5 import QtWidgets
from Front_End.SolverWindow import *
from Front_End.CreatorWindow import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, kakuro, dictionnaire, parent=None):
        super(MainWindow, self).__init__(parent)
        self.kakuro = kakuro
        self.dictionnaire = dictionnaire
        self.setGeometry(10, 10, 700, 800)
        self.startSolverWindow()

    def startSolverWindow(self):
        self.solverWindow = SolverWindow(self.kakuro, self.dictionnaire)
        self.setWindowTitle("Solver's Side")
        self.setCentralWidget(self.solverWindow)
        print(self.solverWindow.menuGroupBox.children())
        self.solverWindow.menuGroupBox.children()[-1].clicked.connect(
            self.startCreatorWindow)
        self.show()

    def startCreatorWindow(self):
        self.creatorWindow = CreatorWindow(self.kakuro, self.dictionnaire)
        self.setWindowTitle("Creator's Side")
        self.setCentralWidget(self.creatorWindow)
        self.creatorWindow.menuGroupBox.children()[1].clicked.connect(
            self.startSolverWindow)
        self.show()
