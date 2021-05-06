### Focntion Principale du programme
from Back_End.Grid import *
from Front_End.Main_Qt_Window import *

# Génération du kakuro
kakuro_projet = gridMaker(6,6)
#terminalPrint(kakuro_projet)

#Instantiation du Front_End
if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(os.getcwd()+"/Front_End/Ressources/Void.png")

    App = App(kakuro_projet)



    sys.exit(app.exec_())

