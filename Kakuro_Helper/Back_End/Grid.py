### Ficher Relatif à la création de la grille backend


### Remplissage intelligent des espaces jouables de la gille
def grid_Smart_Filler(grid):
    # Change les characters à modifier en fonction de la case actuel au besoin 
    for line in grid:
        filler ="#|#"
        for case in line:
            if case[0] != "#|#":
                split = case[0].split("|")
                if split[0] == "H" and split[1] == "#":
                    filler = "#|#"
                
                elif split[1] == "#":
                    filler = "#|#"
                    continue
                else:
                    filler = "   "
                    continue
            else:
                case[0] = filler
    return grid

### Générateur de Grille + Instruction pour simuler le cas du projet
def grid_Maker(x,y):
    # génération de la grille
    grid = []
    for x in range(0,x):
        grid.append([["#|#",0,[]] for y in range(0,y)])

    # Instructions spécifiques 
    grid[0][2][0] = "11|#"
    grid[0][3][0] = "4|#"
    grid[1][1][0] = "14|5"
    grid[1][4][0] = "10|#"
    grid[2][0][0] = "#|17"
    grid[2][5][0] = "3|#"
    grid[3][0][0] = "#|6"
    grid[3][3][0] = "3|4"
    grid[4][1][0] = "#|10"
    grid[5][2][0] = "#|3"
    grid[5][5][0] = "H|#"
    return grid_Smart_Filler(grid)

### Fonction d'affichage lisible pour l'homme du Kakuro dans le terminal

# Affiche toutes les informations back-end de la grille
def terminalPrintFull(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[0:len(case)]).replace("[","").replace("]",""),end="")
        print("")

# Affiche toutes les informations relatives à la heatmap back-end de la grille
def terminalPrintHeatmap(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[1]).replace("[","").replace("]",""),end="")
        print("")

# Affiche toutes les informations relatives aux objectifs back-end de chaque cases de la grille
def terminalPrintObjective(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[2]),end="")
        print("")
