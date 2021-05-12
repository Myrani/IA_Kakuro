# Ficher Relatif à la création de la grille backend


# Remplissage intelligent des espaces jouables de la gille
def grid_Smart_Filler(grid):
    # Change les characters à modifier en fonction de la case actuel au besoin
    for line in grid:
        filler = "#|#"
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


# Génération d'une grille vide et la remplie avec une liste d'instructions précises


def grid_Maker__Default(x, y, liste_Instructions):
    # Génération de la grille
    grid = []
    for x in range(0, x):
        grid.append([["#|#", 0, []] for y in range(0, y)])

    # Application des instructions
    for instruction in liste_Instructions:
        grid[instruction[0]][instruction[1]][0] = instruction[2]

    # Renvoit du tout
    return grid_Smart_Filler(grid)

# Renvoie Simplement le résultat de la save chargée


def grid_Maker__Save(save=None):
    return save

# Fonction d'affichage lisible pour l'homme du Kakuro dans le terminal

# Affiche toutes les informations back-end de la grille


def terminalPrintFull(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[0:len(case)]
                          ).replace("[", "").replace("]", ""), end="")
        print("")

# Affiche toutes les informations relatives à la heatmap back-end de la grille


def terminalPrintHeatmap(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[1]).replace("[", "").replace("]", ""), end="")
        print("")

# Affiche toutes les informations relatives aux objectifs back-end de chaque cases de la grille


def terminalPrintObjective(kakuro):
    for line in kakuro:
        for case in line:
            print("|"+str(case[2]), end="")
        print("")
