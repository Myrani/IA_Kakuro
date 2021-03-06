import pickle
# Fichier concernant la partie logique de recommendation de coup à jouer

#from Back_End.Logic.Saving_Logic import load_Sums

# Propagation des objectifs par ligne sur chaque cases concernées


def load_Sums():
    with open('Back_End/Ressources/sums.pkl', 'rb') as sums:
        return pickle.load(sums)


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


# Refactor


def objective_Propagation_Row__Refactored(kakuro, objectives):
    # Double for de parcours de la grille

    current_Objective = None  # Objectif à propager

    final_List = []  # Liste de tout les espaces jouables liés
    current_List = []  # Liste de l'espace jouable actuellement traité

    for i in range(0, len(kakuro)):

        for j in range(0, len(kakuro)):

            # S'assure que nous sommes bien dans le cas d'une colonne de contrainte
            if kakuro[i][j] != "#|#" and kakuro[i][j] != "H|#" and kakuro[i][j] != " | ":
                # Extrait l'objectif et le met dans la variable de propagation
                current_Objective = kakuro[i][j].split("|")[1]
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []
            # Cas d'une case jouable -> stockage de l'objectif en cour de propagation si il est Set
            elif kakuro[i][j] == " | " and current_Objective != None:

                current_List.append([i, j, current_Objective])

            # Cas de colisition aved un bord neutre, reset de l'objectif
            elif kakuro[i][j] == "#|#" or kakuro[i][j] == "H|#":
                current_Objective = None
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []

    # Attribution des valeures dans le Kakuro
    for space in final_List:
        for case in space:
            objectives[case[0]][case[1]].append([case[2], len(space)])

    return objectives

# Propagation des objectifs par colonne sur chaque cases concernées


def objective_Propagation_Column__Refactored(kakuro, objectives):
    # Double for de parcours de la grille

    current_Objective = None  # Objectif à propager

    final_List = []  # Liste de tout les espaces jouables liés
    current_List = []  # Liste de l'espace jouable actuellement traité

    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro)):

            # S'assure que nous sommes bien dans le cas d'une colonne de contrainte
            if kakuro[j][i] != "#|#" and kakuro[j][i] != "H|#" and kakuro[j][i] != " | ":
                print(kakuro[j][i])

                # Extrait l'objectif et le met dans la variable de propagation
                current_Objective = kakuro[j][i].split("|")[0]
                print("Current objective :", current_Objective)
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []
            # Cas d'une case jouable -> stockage de l'objectif en cour de propagation si il est Set
            elif kakuro[j][i] == " | " and current_Objective != None:

                current_List.append([j, i, current_Objective])

            # Cas de colisition aved un bord neutre, reset de l'objectif
            elif kakuro[j][i] == "#|#" or kakuro[j][i] == "H|#":
                current_Objective = None
                if current_List != []:
                    final_List.append(current_List)
                    current_List = []

    # Attribution des valeures dans le Kakuro : Objectif de la cases , contrainte de longueur
    for space in final_List:
        for case in space:
            objectives[case[0]][case[1]].append([case[2], len(space)])

    return objectives


# Execute la double propagation des objectifs sur le kakuro
def set_Objective_Propagation__Refactored(kakuro):

    objectives_map = [[[] for x in range(0, len(kakuro))]
                      for y in range(0, len(kakuro))]

    return objective_Propagation_Row__Refactored(kakuro, objective_Propagation_Column__Refactored(kakuro, objectives_map))


def findCommonNumberForLength__Refactored(dictionnaire_Des_Sommes, specs):

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


def set_Possible_Values_Mapping__Refactored(kakuro, objectives_map):
    sums = load_Sums()

    values_map = [[[] for x in range(0, len(kakuro))]
                  for y in range(0, len(kakuro))]

    for i in range(0, len(kakuro)):
        for j in range(0, len(kakuro[i])):
            if kakuro[i][j] == " | ":
                values_map[i][j] = findCommonNumberForLength(
                    sums, objectives_map[i][j])
    return values_map
