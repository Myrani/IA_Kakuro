class SolverGrid():
    def __init__(self, grid):
        self.grid = grid
        self.heatmap = []
        self.objectives = []
        self.constraints = []
        self.selected = []


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


cg = CreatorGrid(7, 7)

cg.printCasesTypes()
cg.printCasesValues()


print(cg.GenerateSolverGrid().grid)
