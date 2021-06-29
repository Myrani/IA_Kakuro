

from Back_End.Logic.Possible_Values_Mapping_Logic import set_Objective_Propagation__Refactored, set_Possible_Values_Mapping__Refactored
from Back_End.Logic.Heat_Mapping_Logic import *


class SolverGrid():
    def __init__(self, grid):
        self.grid = grid
        self.heatMap = set_Heat_Mapping__Refactored(self.grid)
        self.objectivesMap = set_Objective_Propagation__Refactored(self.grid)
        self.possibleValuesMap = set_Possible_Values_Mapping__Refactored(
            self.grid, self.objectivesMap)
        self.constraintsMap = [[[] for x in range(0, len(self.grid))]
                               for y in range(0, len(self.grid[0]))]
        self.selectedsMap = [[[] for x in range(0, len(self.grid))]
                             for y in range(0, len(self.grid[0]))]

    def printKakuro(self):
        print("|| Current kakuro")
        for line in self.grid:
            for case in line:
                print("|"+str(case[0:len(case)]), end="|")
            print("")
        print("\n")

    def printHeatMap(self):
        print("|| Current HeatMap")
        for line in self.heatMap:
            for case in line:
                print("|"+str(case), end="|")
            print("")
        print("\n")

    def printObjectivesMap(self):
        print("|| Current Objectives")
        for line in self.objectivesMap:
            for case in line:
                print("|"+str(case), end="|")
            print("")
        print("\n")

    def printPossibleValuesMap(self):
        print("|| Current Possible Values")
        for line in self.possibleValuesMap:
            for case in line:
                print("|"+str(case), end="|")
            print("")
        print("\n")

    def printConstraintsMap(self):
        print("|| Current Constraints")
        for line in self.constraintsMap:
            for case in line:
                print("|"+str(case), end="|")
            print("")
        print("\n")

    def printSelectedsMap(self):
        print("|| Current Selected Values")
        for line in self.selectedsMap:
            for case in line:
                print("|"+str(case), end="|")
            print("")
        print("\n")

    def printAll(self):
        self.printKakuro()
        self.printHeatMap()
        self.printObjectivesMap()
        self.printPossibleValuesMap()
        self.printConstraintsMap()
        self.printSelectedsMap()


class CreatorGrid():

    def __init__(self, x, y):
        self.types = []
        self.values = []
        self.createSolverGrid(x, y)

    def createSolverGrid(self, x, y):
        # Génération de la grille
        for x in range(0, x):
            self.types.append(["#|#" for y in range(0, y)])
            self.values.append(["#|#" for y in range(0, y)])

    def printCasesTypes(self):
        for line in self.types:
            for case in line:
                print("|"+str(case[0:len(case)]), end="|")
            print("")
        print("\n")

    def printCasesValues(self):
        for line in self.values:
            for case in line:
                print("|"+str(case[0:len(case)]), end="|")
            print("")
        print("\n")

    def GenerateSolverGrid(self):
        return SolverGrid(self.values)
