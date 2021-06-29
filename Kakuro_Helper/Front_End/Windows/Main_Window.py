import sys

from PyQt5 import QtWidgets

from Back_End.Logic.Grid_Logic import grid_Maker__Creator, terminalPrintFullRaw
from Back_End.Logic.Saving_Logic import get_All_Saves
from Back_End.Logic.Grids import CreatorGrid

from Front_End.Windows import Creator_Window, Main_Window, Solver_Window, Loader_Window
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, dictionnaire, parent=None):
        super(MainWindow, self).__init__(parent)

        self.solverKakuro = []
        self.creatorKakuroDimensions = [7, 7]
        self.creatorKakuro = CreatorGrid(
            self.creatorKakuroDimensions[0], self.creatorKakuroDimensions[1])
        self.filterSettings = []
        self.dictionnaire = dictionnaire
        self.setGeometry(10, 10, 700, 800)
        self.setStyleSheet(
            "color: rgba(200, 200, 200, 255); background-color: rgba(34,34,34,255); border-style: none;")
        self.startLoaderWindow()

    def startSolverWindow(self):
        self.solverWindow = Solver_Window.SolverWindow(
            self.solverKakuro, self.dictionnaire, self.filterSettings, parent=self)
        self.setWindowTitle("Helper's Side")
        self.setCentralWidget(self.solverWindow)
        self.setStyleSheet(
            "color: rgba(200, 200, 200, 255); background-color : rgba(30,30,30,210);border-style: solid; border-width: 1px; border-color: rgba(34,34,34,255);")
        self.solverWindow.menuGroupBox.children()[-2].clicked.connect(
            self.startLoaderWindow)
        self.solverWindow.menuGroupBox.children()[-1].clicked.connect(
            self.startCreatorWindow)
        self.show()

    def startCreatorWindow(self):
        self.creatorWindow = Creator_Window.CreatorWindow(
            self.creatorKakuro, parent=self)
        self.setWindowTitle("Creator's Side")
        self.setCentralWidget(self.creatorWindow)
        self.creatorWindow.menuGroupBox.children()[-1].clicked.connect(
            self.startSolverWindow)
        self.show()

    def startLoaderWindow(self):
        self.loaderWindow = Loader_Window.LoaderWindow(parent=self)
        self.setWindowTitle("Kakuro Loader")
        self.setCentralWidget(self.loaderWindow)

        print(self.loaderWindow.menuSelectionBox.children()[1:])
        for loaderButton in self.loaderWindow.menuSelectionBox.children()[1:]:
            loaderButton.button.clicked.connect(self.startSolverWindow)

        self.show()
