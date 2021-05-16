# Focntion Principale du programme

import sys

from Back_End.Grid import *
from Back_End.Heat_Mapping_Logic import *
from Back_End.Possible_Values_Mapping_Logic import *
from Back_End.Dictionnaire_Des_Sommes import *
from Back_End.Saving_Logic import *


from Front_End.MainWindow import *
from Front_End.SolverWindow import *
from Front_End.CreatorWindow import *

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


# Génération du kakuro de manière Dynamique
kakuro = dynamic_Load()

terminalPrintFull(kakuro)


# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainWindow(kakuro, dictionnaire_Des_Sommes)

    sys.exit(app.exec_())
