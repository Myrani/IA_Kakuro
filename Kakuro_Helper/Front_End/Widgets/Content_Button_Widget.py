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

    # Logique Pricipale du bouton
    def change_Content(self):

        self.kakuro_solver_ref = self.nativeParentWidget().solverKakuro

        # Si le boutton n'est pas sélectionné , alors rajoute une contrainte en haut,bas,droite et à gauche de la case actuelle
        if not self.selected:

            # rajoute le bouton à la liste des values préssées sur cette case
            self.kakuro_solver_ref.selectedsMap[self.x][self.y].append(
                int(self.content))

            # Propage la contrainte sur les cases voisines concernées
            self.start_add_constraint_propagation(
                self.kakuro_solver_ref, self.x, self.y, int(self.content))
        # Si il l'est , alors propage la libération de la contrainte en haut,bas,droite et à gauche de la case actuelle
        if self.selected:

            # enlève le bouton de la liste des cases préssée sur cette case
            self.kakuro_solver_ref.selectedsMap[self.x][self.y].remove(
                int(self.content))
            # Propage la libération sur les case voisines concernées
            self.start_remove_constraint_propagation(
                self.kakuro_solver_ref, self.x, self.y, int(self.content))

    # Exemple détaillé
    # Propage en haut
    def propagate_add_constraint_up(self, kakuro, x, y, constraint):
        # Permet d'handle les sorties de grille si une case jouable se trouve sur un bord du Kakuro
        try:
            # Vérifie le la case actuelle est une case jouable sinon fini la récursivité
            if kakuro.grid[x][y] == " | ":
                # le rajoute une contrainte dans la liste de contrainte de la case actuelle
                kakuro.constraintsMap[x][y].append(constraint)
                # Poursuit la récursivité
                self.propagate_add_constraint_up(kakuro, x-1, y, constraint)
            # La récursivité de ce côté est donc terminée, on trigger la fin de récursivité
            else:
                return None
        # La récursivité de ce côté est donc terminée, on trigger la fin de récursivité
        except:
            return None
    # Propage en bas

    def propagate_add_constraint_down(self, kakuro, x, y, constraint):
        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].append(constraint)
                self.propagate_add_constraint_down(kakuro, x+1, y, constraint)
            else:
                return None
        except:
            return None
    # Propage à droite

    def propagate_add_constraint_rigth(self, kakuro, x, y, constraint):
        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].append(constraint)
                self.propagate_add_constraint_rigth(kakuro, x, y+1, constraint)
            else:
                return None
        except:
            return None
    # Propage à gauche

    def propagate_add_constraint_left(self, kakuro, x, y, constraint):

        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].append(constraint)
                self.propagate_add_constraint_left(kakuro, x, y-1, constraint)
            else:
                return None
        except:
            return None

    # Démarre toutes les propagations et call un refresh de la fenêtre
    def start_add_constraint_propagation(self, kakuro, x, y, constraint):
        self.propagate_add_constraint_down(kakuro, x+1, y, constraint)
        self.propagate_add_constraint_up(kakuro, x-1, y, constraint)
        self.propagate_add_constraint_rigth(kakuro, x, y+1, constraint)
        self.propagate_add_constraint_left(kakuro, x, y-1, constraint)

        self.nativeParentWidget().startSolverWindow()
        return None

# Remove Constraint

    # Propage en haut
    def propagate_remove_constraint_up(self, kakuro,  x, y, constraint):
        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].remove(constraint)
                self.propagate_remove_constraint_up(kakuro, x-1, y, constraint)
            else:
                return None
        except:
            return None
    # Propage en bas

    def propagate_remove_constraint_down(self, kakuro, x, y, constraint):
        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].remove(constraint)
                self.propagate_remove_constraint_down(
                    kakuro, x+1, y, constraint)
            else:
                return None
        except:
            return None

    # Propage à droite
    def propagate_remove_constraint_rigth(self, kakuro, x, y, constraint):
        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].remove(constraint)
                self.propagate_remove_constraint_rigth(
                    kakuro, x, y+1, constraint)
            else:
                return None
        except:
            return None
    # Propage à gauche

    def propagate_remove_constraint_left(self, kakuro, x, y, constraint):

        try:
            if kakuro.grid[x][y] == " | ":
                kakuro.constraintsMap[x][y].remove(constraint)
                self.propagate_remove_constraint_left(
                    kakuro, x, y-1, constraint)
            else:
                return None
        except:
            return None
    # démarre la propagation et call un refresh de la page

    def start_remove_constraint_propagation(self, kakuro, x, y, constraint):
        self.propagate_remove_constraint_down(kakuro, x+1, y, constraint)
        self.propagate_remove_constraint_up(kakuro, x-1, y, constraint)
        self.propagate_remove_constraint_rigth(kakuro, x, y+1, constraint)
        self.propagate_remove_constraint_left(kakuro, x, y-1, constraint)

        self.nativeParentWidget().startSolverWindow()

        return None
