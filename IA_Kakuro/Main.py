### Focntion Principale du programme
from Back_End.Grid import *
from Front_End.Main_Qt_Window import *


kakuro_projet = gridMaker(6,6)

terminalPrint(kakuro_projet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = App(kakuro_projet)
    sys.exit(app.exec_())

