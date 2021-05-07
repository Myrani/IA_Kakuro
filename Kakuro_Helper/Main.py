### Focntion Principale du programme
from Back_End.Grid import *
from Back_End.Heat_Mapping_Logic import *

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


from Front_End.Main_Qt_Window import *


# Génération du kakuro
kakuro_projet = grid_Maker(6,6)
kakuro_projet = set_Heat_Mapping(kakuro_projet)
terminalPrint(kakuro_projet)

#Instantiation du Front_End
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #print(os.getcwd()+"/Front_End/Ressources/Void.png")

    App = App(kakuro_projet)

    sys.exit(app.exec_())

