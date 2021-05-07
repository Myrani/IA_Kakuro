from Grid import * 

kakuro = grid_Maker(6,6)


def objective_Propagation_Row(kakuro):

    for i in range(0,len(kakuro)):
        curent_Objective = None
        for j in range(0,len(kakuro)):
            if kakuro[i][j][0] != "#|#" and kakuro[i][j][0] != "H|#" and kakuro[i][j][0] != "   ":
                curent_Objective = kakuro[i][j][0].split("|")[1]
            elif kakuro[i][j][0] == "   " and curent_Objective != None:
                kakuro[i][j][2].append(curent_Objective)
            elif kakuro[i][j][0] != "#|#" or kakuro[i][j][0] != "H|#":
                curent_Objective = None

    return kakuro




def objective_Propagation_Column(kakuro):
    
    for i in range(0,len(kakuro)):
        curent_Objective = None
        for j in range(0,len(kakuro)):
            if kakuro[j][i][0] != "#|#" and kakuro[j][i][0] != "H|#" and kakuro[j][i][0] != "   ":
                curent_Objective = kakuro[j][i][0].split("|")[0]
            elif kakuro[j][i][0] == "   " and curent_Objective != None:
                kakuro[j][i][2].append(curent_Objective)
            elif kakuro[j][i][0] != "#|#" or kakuro[j][i][0] != "H|#":
                curent_Objective = None

    return kakuro



def objective_Propagation(kakuro):
    return objective_Propagation_Row(objective_Propagation_Column(kakuro))


terminalPrintObjective(objective_Propagation(kakuro))




