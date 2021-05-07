from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

class DividedLabel(QtWidgets.QWidget):
  
    def __init__(self,specs):
        super().__init__()
        self.dictionnaire_Des_Sommes = {
            '1':[[1]],
            '2':[[2]],
            '3':[[1,2]],
            '4':[[1,3]],
            '5':[[1,4],[2,3]],
            '6':[[1,5],[1,2,3],[2,4]],
            '7':[[1,6],[1,2,4],[2,5],[3,4]],
            '8':[[1,7],[2,6],[3,5],[1,2,5],[1,3,4]],
            '9':[[1,8],[2,7],[3,6],[4,5],[1,2,6],[1,3,5],[2,3,4]],
            '10':[[1,9],[2,8],[3,7],[4,6],[1,2,7],[1,3,6],[1,4,5],[2,3,5],[1,2,3,4]],
            '11':[[2,9],[3,8],[4,7],[5,6],[1,2,8],[1,3,7],[1,4,6],[2,3,6],[2,4,5],[1,2,3,5]],
            '14':[[5,9],[6,8],[1,4,9],[1,5,8],[1,6,7],[2,3,9],[2,4,8],[2,5,7],[3,4,7],[3,5,6],[1,2,3,8],[1,2,4,7],[1,2,5,6],[1,3,4,6],[2,3,4,5]],
            '17':[[8,9],[1,7,9],[2,6,9],[2,7,8],[3,5,9],[3,6,8],[4,5,8],[4,6,7],[1,2,5,9],[1,2,6,8],[1,3,4,9],[1,3,5,8],[1,3,6,7],[1,4,5,7],[2,3,4,8],[2,3,5,7],[2,4,5,6],[1,2,3,4,7],[1,2,3,5,6]]
            }
        self.specs = specs
        self.container = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.setLayout(self.layout)
        

        self.label = QtWidgets.QLabel()
        self.labelLayout = QtWidgets.QGridLayout()
        self.labelLayout.setHorizontalSpacing(0)
        self.labelLayout.setVerticalSpacing(0)
        self.labelLayout.setContentsMargins(0, 0, 0, 0)
        self.label.setLayout(self.labelLayout)

        self.possibleSetValues = self.findCommonNumberForLength(self.specs[0][0],self.specs[0][1],self.specs[1][0],self.specs[1][1])
        print(self.possibleSetValues)

        cpt = 1
        for i in range(0,3):
            for j in range(0,3):
                if cpt in self.possibleSetValues:
                    minilabel = QtWidgets.QLabel(str(cpt))
                    minilabel.setAlignment(QtCore.Qt.AlignCenter)
                    self.labelLayout.addWidget(minilabel, i, j)
                    cpt+=1
                else:
                    minilabel = QtWidgets.QLabel("")
                    minilabel.setAlignment(QtCore.Qt.AlignCenter)
                    self.labelLayout.addWidget(minilabel, i, j)
                    cpt+=1
        
        self.layout.addWidget(self.label)

    def findCommonNumberForLength(self,firstNumber,firstLen,secondNumber,secondLen):
    
        set_One = []
        set_Two = []

        for combinaison_First in self.dictionnaire_Des_Sommes[firstNumber]:
            if len(combinaison_First) == firstLen:
                for el in combinaison_First:
                    set_One.append(el)
    
        for combinaison_Second in self.dictionnaire_Des_Sommes[secondNumber]:
            if len(combinaison_Second) == secondLen:
                for el in combinaison_Second:
                    set_Two.append(el)
    
        set_One = set(set_One)
        set_Two = set(set_Two)
        
        print(set_One,set_Two)
        return set_One & set_Two
  