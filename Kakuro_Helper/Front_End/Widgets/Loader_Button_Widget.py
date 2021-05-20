from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys

from Back_End.Saving_Logic import load_Kakuro_From_File


class LoaderButton(QtWidgets.QPushButton):

    def __init__(self, filename, parent=None):
        super().__init__(parent)

        self.filename = filename
        self.button = QtWidgets.QPushButton(self.filename, self)
        self.button.pressed.connect(self.loadKakuro)
        self.button.setStyleSheet(
            "border-style: solid; background-color: rgba(34,34,34,255); border-color:black ;background: transparent;")

    def loadKakuro(self):
        self.nativeParentWidget().solverKakuro = load_Kakuro_From_File(self.filename)
