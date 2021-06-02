import pickle
# Fichier concernant la partie logique de recommendation de coup à jouer

from Back_End.Logic.Saving_Logic import load_Sums

# Propagation des objectifs par ligne sur chaque cases concernées


def load_Sums():
    with open('Back_End/Ressources/sums.pkl', 'rb') as sums:
        return pickle.load(sums)


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
                print(kakuro[i][j][0].split("|"))
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

    # Attribution des valeures dans le Kakuro : Objectif de la cases , contrainte de longueur
    for space in final_List:
        for case in space:
            kakuro[case[0]][case[1]][2].append([case[2], len(space)])

    return kakuro


# Execute la double propagation des objectifs sur le kakuro
def set_Objective_Propagation(kakuro):
    return objective_Propagation_Row(objective_Propagation_Column(kakuro))


def findCommonNumberForLength(dictionnaire_Des_Sommes, specs):

    set_One = []  # Futur set des solutions pour la contrainte de Ligne
    set_Two = []  # Futur set des solutions pour la contrainte de Colonnes
    print(set_One == [])
    # Tri des solutions possibles en fonction des de cases à remplir : ligne OU colonne
    if len(specs) == 1:
        for combinaison_First in dictionnaire_Des_Sommes[int(specs[0][0])]:
            if len(combinaison_First) == specs[0][1]:
                for el in combinaison_First:
                    set_One.append(el)

    # Tri des solutions possibles en fonction des de cases à remplir : ligne ET colonne
    elif len(specs) > 1:

        for combinaison_First in dictionnaire_Des_Sommes[int(specs[0][0])]:
            if len(combinaison_First) == specs[0][1]:
                for el in combinaison_First:
                    set_One.append(el)

        for combinaison_Second in dictionnaire_Des_Sommes[int(specs[1][0])]:
            if len(combinaison_Second) == int(specs[1][1]):
                for el in combinaison_Second:
                    set_Two.append(el)

        # Transformation en Set
    set_One = set(set_One)
    set_Two = set(set_Two)

    # Retourne la jointure des 2 Sets, Donc les éléments communs au 2 ensembles de solutions !
    # ligne et colonne
    if set_One != set([]) and set_Two != set([]):
        # print(set_One)
        # print(set_Two)
        #print("Case Double specs", set_One & set_Two)
        return set_One & set_Two
    # ligne
    elif set_One != [] and set_Two == set([]):
        #print("Case solo specs", set_One)
        return set_One
    # possible traitement d'un failstate ...
    else:
        return []

# Démarre la propagation dans le kakuro


def set_Possible_Values_Mapping(kakuro):
    sums = load_Sums()
    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro[i])):
            if kakuro[i][j][0] == " | ":
                kakuro[i][j][3] = findCommonNumberForLength(
                    sums, kakuro[i][j][2])
    return kakuro
