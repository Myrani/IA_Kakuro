import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

from Front_End.Windows import Creator_Window, Main_Window, Solver_Window
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label


class SolverWindow(QtWidgets.QWidget):
    def __init__(self, kakuro, dictionnaire_Des_Sommes, filterSettings, parent=None):
        super(SolverWindow, self).__init__(parent)

        print(self.parentWidget().filterSettings)
        # Setup des paramêtres basique de la fenêtre principale
        self.grid = kakuro
        self.kakuro = kakuro.grid
        self.dictionnaire = dictionnaire_Des_Sommes
        self.filterSettings = filterSettings
        self.title = 'Kakuro Helper'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 700
        self.initUI(self.kakuro, self.dictionnaire, self.filterSettings)

    def initUI(self, kakuro, dictionnaire_Des_Sommes, filterSettings):

        self.setStyleSheet("background-color: rgba(34,34,34,255);")
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Création de la VBox Qui tiendra tout les éléments
        self.windowLayout = QtWidgets.QGridLayout()

        # Génération des VBox et de leurs layout qu'on récupéra après via un attbribut de l'objet
        self.createKakuroSolverLayout(kakuro, dictionnaire_Des_Sommes)
        self.createMenuLayout()

        # Ajout des VBoxs Crées au Layout Principal
        self.windowLayout.addWidget(self.menuGroupBox, 0, 0, 1, 0)
        self.windowLayout.addWidget(self.interfaceGroupBox, 1, 0, 6, 6)

        # Assosiation du Layout et de fenêtre
        self.setLayout(self.windowLayout)

        # Montrer le tout !
        self.show()

    def createMenuLayout(self):
        self.menuGroupBox = QtWidgets.QGroupBox(self)
        menuLayout = QtWidgets.QGridLayout()

        solver_To_loader_BTN = QtWidgets.QPushButton(
            "Reload an other Kakuro", self)
        solver_To_creator_BTN = QtWidgets.QPushButton(
            "To Creator's Side", self)

        self.filter_Heat_CHK = QtWidgets.QCheckBox("Heat Map")
        self.filter_PossibleValues_CHK = QtWidgets.QCheckBox(
            "Valeures Possibles")
        # self.filter_X_CHK = QtWidgets.QCheckBox("Possible Filtre")
        # self.filter_Y_CHK = QtWidgets.QCheckBox("Possible Filtre")

        for filter in self.parentWidget().filterSettings:
            if filter == "Heat Map":
                self.filter_Heat_CHK.setChecked(True)
            elif filter == "Possible Values":
                self.filter_PossibleValues_CHK.setChecked(True)

        self.filter_Heat_CHK.toggled.connect(
            lambda: self.onChecked(self.filter_Heat_CHK, "Heat Map"))

        self.filter_PossibleValues_CHK.toggled.connect(
            lambda: self.onChecked(self.filter_PossibleValues_CHK, "Possible Values"))

        menuLayout.addWidget(self.filter_Heat_CHK, 0, 0)
        menuLayout.addWidget(self.filter_PossibleValues_CHK, 1, 0)
        # menuLayout.addWidget(self.filter_X_CHK, 0, 1)
        # menuLayout.addWidget(self.filter_Y_CHK, 1, 1)

        menuLayout.addWidget(solver_To_loader_BTN, 0, 2)
        menuLayout.addWidget(solver_To_creator_BTN, 1, 2)
        self.menuGroupBox.setLayout(menuLayout)

    def onChecked(self, box, filter):
        if box.isChecked():
            self.parentWidget().filterSettings.append(filter)
        else:
            self.parentWidget().filterSettings.remove(filter)

        self.parentWidget().startSolverWindow()

    def createKakuroSolverLayout(self, kakuro, dictionnaire_Des_Sommes):
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

                # Changement du contenu de la case en fonction des values [0] et [1] du modèle backend

                # Cas des Cases Void
                if kakuro[x][y] == "#|#" or kakuro[x][y] == "H|#":
                    label = QtWidgets.QLabel(self)
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    layout.addWidget(label, x, y)
                    # label.setStyleSheet("background-image : url("+os.getcwd()+"/Front_End/Ressources/Void.png);background-repeat: no-repeat;")
                    label.setStyleSheet(
                        "background-color : rgba(20,20,20,210);border-style: solid; border-width: 1px; border-color: rgba(34,34,34,255); border-radius: 7px;")

                # Cas des Cases jouables
                elif kakuro[x][y] == " | ":

                    # On passe en argument les valeurs trouvées par le mapping des values possibles stockées dans le back-end
                    if "Possible Values" in self.filterSettings:
                        label = Divided_Label_Widget.DividedLabel(
                            self.grid.possibleValuesMap[x][y], self.grid.constraintsMap[x][y], self.grid.selectedsMap[x][y], x, y)
                    else:
                        label = QtWidgets.QLabel("")

                    # Couleur d'arrière plan en fonction du heatmapping stocké en [1]
                    if "Heat Map" in self.filterSettings:
                        label.setStyleSheet(
                            "background-color : rgba(255,80,0,"+str(int(self.grid.heatMap[x][y]))+"); border-radius: 7px;")
                        layout.addWidget(label, x, y)  # Rajout à la Grid
                    else:
                        label.setStyleSheet(
                            "background-color :rgba(34,34,34,255);")
                        layout.addWidget(label, x, y)  # Rajout à la Grid
                # Cas des cases de contraintes du Kakuro
                else:
                    label = QtWidgets.QLabel(
                        kakuro[x][y].replace("|", "\\").replace("H", "#"))
                    label.setAlignment(QtCore.Qt.AlignCenter)
                    layout.addWidget(label, x, y)

        self.interfaceGroupBox.setLayout(layout)
