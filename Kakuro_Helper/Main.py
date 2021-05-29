# Fonction Principale du programme

import sys

from Back_End.Logic.Grid_Logic import *
from Back_End.Logic.Heat_Mapping_Logic import *
from Back_End.Logic.Possible_Values_Mapping_Logic import *
from Back_End.Logic.Saving_Logic import *


from Front_End.Windows import Creator_Window, Main_Window, Solver_Window
from Front_End.Widgets import Content_Button_Widget, Divided_Label_Widget, Morphing_Label


from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


# Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Main_Window.MainWindow(load_Sums())

    sys.exit(app.exec_())
