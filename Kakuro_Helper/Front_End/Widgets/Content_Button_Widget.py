from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import sys


class ContentButton(QtWidgets.QPushButton):

    def __init__(self, content, x, y, selected):
        super().__init__()
        self.content = content
        self.x = x
        self.y = y
        self.selected = selected
        self.button = QtWidgets.QPushButton(self.content, self)
        self.button.pressed.connect(self.change_Content)
        self.button.setStyleSheet(
            "border-style: solid; background-color: rgba(34,34,34,255); border-color:black ;background: transparent;")
        self.button.setGeometry(QtCore.QRect(0, 0, 10, 15))
        if self.selected:
            self.button.setStyleSheet("color:red;")

    def change_Content(self):
        if not self.selected:

            # Add Constraint
            self.nativeParentWidget().solverKakuro[self.x][self.y][5].append(
                int(self.content))
            self.start_add_constraint_propagation(
                self.x, self.y, int(self.content))
        if self.selected:
            self.nativeParentWidget().solverKakuro[self.x][self.y][5].remove(
                int(self.content))
            self.start_remove_constraint_propagation(
                self.x, self.y, int(self.content))

    def propagate_add_constraint_up(self,  x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].append(constraint)
                self.propagate_add_constraint_up(x-1, y, constraint)
            else:
                return None
        except:
            return None

    def propagate_add_constraint_down(self, x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].append(constraint)
                self.propagate_add_constraint_down(x+1, y, constraint)
            else:
                return None
        except:
            return None

    def propagate_add_constraint_rigth(self, x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].append(constraint)
                self.propagate_add_constraint_rigth(x, y+1, constraint)
            else:
                return None
        except:
            return None

    def propagate_add_constraint_left(self, x, y, constraint):

        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].append(constraint)
                self.propagate_add_constraint_left(x, y-1, constraint)
            else:
                return None
        except:
            return None

    def start_add_constraint_propagation(self, x, y, constraint):
        self.propagate_add_constraint_down(x+1, y, constraint)
        self.propagate_add_constraint_up(x-1, y, constraint)
        self.propagate_add_constraint_rigth(x, y+1, constraint)
        self.propagate_add_constraint_left(x, y-1, constraint)

        self.nativeParentWidget().startSolverWindow()
        return None

# Remove Constraint

    def propagate_remove_constraint_up(self,  x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].remove(constraint)
                self.propagate_add_constraint_up(x-1, y, constraint)
            else:
                return None
        except:
            return None

    def propagate_remove_constraint_down(self, x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].remove(constraint)
                self.propagate_add_constraint_down(x+1, y, constraint)
            else:
                return None
        except:
            return None

    def propagate_remove_constraint_rigth(self, x, y, constraint):
        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].remove(constraint)
                self.propagate_remove_constraint_rigth(x, y+1, constraint)
            else:
                return None
        except:
            return None

    def propagate_remove_constraint_left(self, x, y, constraint):

        try:
            if self.nativeParentWidget().solverKakuro[x][y][0] == " | ":
                self.nativeParentWidget(
                ).solverKakuro[x][y][4].remove(constraint)
                self.propagate_add_constraint_left(x, y-1, constraint)
            else:
                return None
        except:
            return None

    def start_remove_constraint_propagation(self, x, y, constraint):
        self.propagate_remove_constraint_down(x+1, y, constraint)
        self.propagate_remove_constraint_up(x-1, y, constraint)
        self.propagate_remove_constraint_rigth(x, y+1, constraint)
        self.propagate_remove_constraint_left(x, y-1, constraint)

        self.nativeParentWidget().startSolverWindow()

        return None
