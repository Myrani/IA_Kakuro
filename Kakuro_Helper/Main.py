# Focntion Principale du programme

import sys

from Back_End.Grid import *
from Back_End.Heat_Mapping_Logic import *
from Back_End.Possible_Values_Mapping_Logic import *
from Back_End.Dictionnaire_Des_Sommes import *
from Back_End.Saving_Logic import *

from Front_End.Main_Qt_Window import *


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

old_instructions = [[0, 2, "11|#"], [0, 3, "4|#"], [1, 1, "14|5"], [1, 4, "10|#"], [2, 0, "#|17"], [2, 5, "3|#"], [3, 0, "#|6"],
                    [3, 3, "3|4"], [3, 6, "H|#"], [4, 1, "#|10"], [4, 6, "H|#"], [5, 2, "#|3"], [5, 5, "H|#"], [6, 3, "H|#"], [6, 4, "H|#"]]

# Génération du kakuro de manière Dynamique
kakuro = dynamic_Load()

terminalPrintFull(kakuro)


# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    App = App(kakuro, dictionnaire_Des_Sommes)

    sys.exit(app.exec_())
