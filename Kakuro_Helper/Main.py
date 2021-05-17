# Fonction Principale du programme

import sys

from Back_End.Grid import *
from Back_End.Heat_Mapping_Logic import *
from Back_End.Possible_Values_Mapping_Logic import *
from Back_End.Dictionnaire_Des_Sommes import *
from Back_End.Saving_Logic import *


from Front_End.Windows import CreatorWindow, MainWindow, SolverWindow
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


# Génération du kakuro de manière Dynamique
kakuro = dynamic_Load()


# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainWindow.MainWindow(kakuro, dictionnaire_Des_Sommes)

    sys.exit(app.exec_())
