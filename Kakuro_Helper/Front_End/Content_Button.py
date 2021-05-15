from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class ContentButton(QtWidgets.QWidget):

    def __init__(self, content, parent):
        super().__init__()

        self.content = content
        self.button = QtWidgets.QPushButton(self.content, parent)
        self.button.pressed.connect(self.change_Content)

    def change_Content(self):
        if self.button.text() == self.content:
            self.button.setText("")
        else:
            self.button.setText(self.content)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # creating a push button
        self.button = ContentButton("9", self)

        # setting geometry of button
        self.button.setGeometry(100, 100, 100, 100)

        # self.addWidget(self.button)


# create pyqt5 app
App = QtWidgets.QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
