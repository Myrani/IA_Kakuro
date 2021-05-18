# Fichier concernant la partie logique de recommendation de coup à jouer

# Propagation des objectifs par ligne sur chaque cases concernées

def objective_Propagation_Row(kakuro):
    # Double for de parcours de la grille

    current_Objective = None  # Objectif à propager

    final_List = []  # Liste de tout les espaces jouables liés
    current_List = []  # Liste de l'espace jouable actuellement traité

    for i in range(0, len(kakuro)):

        for j in range(0, len(kakuro)):

            # S'assure que nous sommes bien dans le cas d'une colonne de contrainte
            if kakuro[i][j][0] != "#|#" and kakuro[i][j][0] != "H|#" and kakuro[i][j][0] != " | ":
                # Extrait l'objectif et le met dans la variable de propagation
                current_Objective = kakuro[i][j][0].split("|")[1]
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []
            # Cas d'une case jouable -> stockage de l'objectif en cour de propagation si il est Set
            elif kakuro[i][j][0] == " | " and current_Objective != None:

                current_List.append([i, j, current_Objective])

            # Cas de colisition aved un bord neutre, reset de l'objectif
            elif kakuro[i][j][0] == "#|#" or kakuro[i][j][0] == "H|#":
                current_Objective = None
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []

    # Attribution des valeures dans le Kakuro
    for space in final_List:
        for case in space:
            kakuro[case[0]][case[1]][2].append([case[2], len(space)])

    return kakuro

# Propagation des objectifs par colonne sur chaque cases concernées


def objective_Propagation_Column(kakuro):
    # Double for de parcours de la grille

    current_Objective = None  # Objectif à propager

    final_List = []  # Liste de tout les espaces jouables liés
    current_List = []  # Liste de l'espace jouable actuellement traité

    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro)):

            # S'assure que nous sommes bien dans le cas d'une colonne de contrainte
            if kakuro[j][i][0] != "#|#" and kakuro[j][i][0] != "H|#" and kakuro[j][i][0] != " | ":
                # Extrait l'objectif et le met dans la variable de propagation
                current_Objective = kakuro[j][i][0].split("|")[0]
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []
            # Cas d'une case jouable -> stockage de l'objectif en cour de propagation si il est Set
            elif kakuro[j][i][0] == " | " and current_Objective != None:

                current_List.append([j, i, current_Objective])

            # Cas de colisition aved un bord neutre, reset de l'objectif
            elif kakuro[j][i][0] == "#|#" or kakuro[j][i][0] == "H|#":
                current_Objective = None
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []

    # Attribution des valeures dans le Kakuro
    for space in final_List:
        for case in space:
            kakuro[case[0]][case[1]][2].append([case[2], len(space)])

    return kakuro


# Execute la double propagation des objectif sur le kakuro
def set_Objective_Propagation(kakuro):
    return objective_Propagation_Row(objective_Propagation_Column(kakuro))
