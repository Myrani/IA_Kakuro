import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Widgets.Loader_Button_Widget import LoaderButton
from Back_End.Logic.Saving_Logic import get_All_Saves, load_Kakuro_From_File, dynamic_Load
from Back_End.Logic.Grid_Logic import terminalPrintFull


class LoaderWindow(QtWidgets.QWidget):

    # Initialisation Basique
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)

        self.initUI()

    def initUI(self):
        self.createSelectionMenu()

    def createSelectionMenu(self):

        # Initialisation du menu
        self.menuSelectionBox = QtWidgets.QGroupBox(self)
        self.menuLayout = QtWidgets.QVBoxLayout()
        self.menuSelectionBox.setLayout(self.menuLayout)

        # Rajoute un LoaderButton au Layout menu pour chaque fichier présent dans le dossier Save/
        saves = get_All_Saves()

        if len(saves) > 0:
            for save in saves:
                generatedButton = LoaderButton(save, parent=self)
                print(generatedButton.filename)
                self.menuLayout.addWidget(generatedButton)
        else:
            defaultButton = QtWidgets.QPushButton("Kakuro par défault", self)
            defaultButton.clicked.connect(self.loadDefaultKakuro)

        # Le rajoute au container principal
        self.layout.addWidget(self.menuSelectionBox)

    def loadDefaultKakuro(self):
        self.nativeParentWidget().solverKakuro = dynamic_Load()
        self.nativeParentWidget().startSolverWindow()