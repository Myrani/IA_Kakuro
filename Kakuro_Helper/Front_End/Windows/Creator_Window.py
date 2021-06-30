import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Windows import Creator_Window, Main_Window, Solver_Window
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label

from Back_End.Logic.Saving_Logic import *
from Back_End.Logic.Grids import CreatorGrid


class CreatorWindow(QtWidgets.QWidget):
    def __init__(self, kakuro, datahandler, parent=None):
        super(CreatorWindow, self).__init__(parent)

        # Setup des paramêtres basique de la fenêtre principale
        self.creatorGrid = kakuro
        self.datahandler = datahandler
        self.kakuro = kakuro.types
        self.title = ''
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 700
        self.init_UI(self.kakuro)

    def init_UI(self, kakuro):

        self.setStyleSheet(
            "text-align: center; color: rgba(200, 200, 200, 255); background-color: rgba(34,34,34,255); border-style: solid; border-width: 2px; border-color: rgba(45,45,45,255); border-radius: 7px")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Création de la VBox Qui tiendra tout les éléments
        self.windowLayout = QtWidgets.QGridLayout()

        # Génération des VBox et de leurs layout qu'on récupéra après via un attbribut de l'objet
        self.create_kakuro_creator_layout(kakuro)
        self.create_menu_layout()

        # Ajout des VBoxs Crées au Layout Principal
        self.windowLayout.addWidget(self.interfaceGroupBox, 0, 0, 6, 6)
        self.windowLayout.addWidget(self.menuGroupBox, 6, 0, 6, 6)

        # Assosiation du Layout et de fenêtre
        self.setLayout(self.windowLayout)

        # Montrer le tout !
        self.show()

    def create_menu_layout(self):
        self.menuGroupBox = QtWidgets.QGroupBox(self)
        menuLayout = QtWidgets.QGridLayout()

        self.menuWidthSelection = QtWidgets.QGroupBox(self)
        menuWidthSelectionLayout = QtWidgets.QHBoxLayout()
        self.menuWidthSelection.setLayout(menuWidthSelectionLayout)

        self.dimmensions = self.nativeParentWidget().creatorKakuroDimensions

        self.x_creator_setting = QtWidgets.QLineEdit(
            str(self.dimmensions[0]), self)
        self.y_creator_setting = QtWidgets.QLineEdit(
            str(self.dimmensions[1]), self)

        self.x_creator_setting.textChanged.connect(
            lambda: self.update_creator_kakuro_dimensions(self.x_creator_setting.text(), self.y_creator_setting.text()))
        self.y_creator_setting.textChanged.connect(
            lambda: self.update_creator_kakuro_dimensions(self.x_creator_setting.text(), self.y_creator_setting.text()))

        self.x_creator_setting.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.x_creator_setting.setFixedSize(45, 15)

        self.y_creator_setting.setSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.y_creator_setting.setFixedSize(45, 15)

        menuWidthSelectionLayout.addWidget(self.x_creator_setting)
        menuWidthSelectionLayout.addWidget(self.y_creator_setting)

        saveKakuro = QtWidgets.QPushButton("Save Current Kakuro", self)
        solver_To_creator_BTN = QtWidgets.QPushButton("To Helper's Side", self)

        saveKakuro.clicked.connect(lambda: self.datahandler.pushCreator(
            self.creatorGrid.GenerateSolverGrid()))

        menuLayout.addWidget(self.menuWidthSelection, 0, 0, 2, 2)
        menuLayout.addWidget(saveKakuro, 2, 0, 3, 1)
        menuLayout.addWidget(solver_To_creator_BTN, 2, 1, 3, 1)

        self.menuGroupBox.setLayout(menuLayout)

    def update_creator_kakuro_dimensions(self, x, y):
        x = int(x)
        y = int(y)
        self.nativeParentWidget().creatorKakuroDimensions = [x, y]
        self.nativeParentWidget().creatorKakuro = CreatorGrid(x, y)
        self.nativeParentWidget().startCreatorWindow()

    def create_kakuro_creator_layout(self, kakuro):
        # grid layout + nom
        self.interfaceGroupBox = QtWidgets.QGroupBox(self)
        layout = QtWidgets.QGridLayout()

        # Aucun espace entre les cases
        layout.setHorizontalSpacing(0)
        layout.setVerticalSpacing(0)

        # Rajout des cases en fonction du kakuro backend fourni à l'instatiation !!
        # Double for pour parcour des cases
        for x in range(0, len(kakuro)):
            for y in range(0, len(kakuro[x])):

                label = Morphing_Label.Morphing_Label(
                    x, y, self.kakuro, parent=self)
                # label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet(
                    "border: solid ;"
                )
                layout.addWidget(label, x, y)

        self.interfaceGroupBox.setLayout(layout)
