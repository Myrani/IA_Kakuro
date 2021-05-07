from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


class DividedLabel(QtWidgets.QWidget):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)
        

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setHorizontalSpacing(0)
        self.labelLayout.setVerticalSpacing(0)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)
        self.label.setLayout(self.labelLayout)

        cpt = 1
        for i in range(0,3):
            for j in range(0,3):
                self.labelLayout.addWidget(QtWidgets.QLabel(str(cpt)), i, j)
                cpt+=1

        self.layout.addWidget(self.label)

    
  