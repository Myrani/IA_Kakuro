from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class ContentButton(QtWidgets.QPushButton):

    def __init__(self, content):
        super().__init__()

        self.content = content
        self.button = QtWidgets.QPushButton(self.content, self)
        self.button.pressed.connect(self.change_Content)
        self.button.setStyleSheet(
            "border-style: solid; background-color: rgba(34,34,34,255); border-color:black ;background: transparent;")
        self.button.setGeometry(QtCore.QRect(0, 0, 10, 15))

    def change_Content(self):
        if self.button.text() == self.content:
            self.button.setText("")
        else:
            self.button.setText(self.content)
