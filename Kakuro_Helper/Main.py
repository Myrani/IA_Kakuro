# Focntion Principale du programme
from Back_End.Grid import *
from Back_End.Heat_Mapping_Logic import *
from Back_End.Possible_Values_Mapping_Logic import *
from Back_End.Dictionnaire_Des_Sommes import *

from Front_End.Main_Qt_Window import *

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


# Génération du kakuro
kakuro_projet = grid_Maker(8, 8)
kakuro_projet = set_Heat_Mapping(kakuro_projet)
kakuro_projet = set_Objective_Propagation(kakuro_projet)

terminalPrintFull(kakuro_projet)


# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    App = App(kakuro_projet, dictionnaire_Des_Sommes)

    sys.exit(app.exec_())
