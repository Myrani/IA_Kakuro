import sys

from PyQt5 import QtWidgets

from Front_End.Windows import CreatorWindow, MainWindow, SolverWindow
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, kakuro, dictionnaire, parent=None):
        super(MainWindow, self).__init__(parent)
        self.kakuro = kakuro
        self.filterSettings = []
        self.dictionnaire = dictionnaire
        self.setGeometry(10, 10, 700, 800)
        self.startSolverWindow()

    def startSolverWindow(self):
        self.solverWindow = SolverWindow.SolverWindow(
            self.kakuro, self.dictionnaire, self.filterSettings, parent=self)
        self.setWindowTitle("Helper's Side")
        self.setCentralWidget(self.solverWindow)
        # print(self.solverWindow.menuGroupBox.children())
        self.solverWindow.menuGroupBox.children()[-1].clicked.connect(
            self.startCreatorWindow)
        self.show()

    def startCreatorWindow(self):
        self.creatorWindow = CreatorWindow.CreatorWindow(
            self.kakuro, self.dictionnaire)
        self.setWindowTitle("Creator's Side")
        self.setCentralWidget(self.creatorWindow)
        self.creatorWindow.menuGroupBox.children()[1].clicked.connect(
            self.startSolverWindow)
        self.show()
