import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Widgets.Loader_Button_Widget import LoaderButton
from Back_End.Saving_Logic import get_All_Saves, load_Kakuro_From_File
from Back_End.Grid import terminalPrintFull


class LoaderWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.createSelectionMenu()

    def createSelectionMenu(self):
        self.menuSelectionBox = QtWidgets.QGroupBox(self)
        self.menuLayout = QtWidgets.QGridLayout()
        self.menuSelectionBox.setLayout(self.menuLayout)

        for save in get_All_Saves():
            generatedButton = LoadeButton(save, parent=self)
            print(generatedButton.filename)
            self.menuLayout.addWidget(generatedButton)

        self.layout.addWidget(self.menuSelectionBox)

    def overrideSolverKakuro(self, grille):
        terminalPrintFull(grille)
        self.parentWidget().solverKakuro = grille
