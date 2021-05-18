def heat_Mapping_Row(kakuro, weigth):
    # Parcours de toutes les cases avec un double for ; version ligne  : [i][j]
    for i in range(0, len(kakuro)):

        free_spots = []  # Stockage des cases libres à chaque ligne

        for j in range(0, len(kakuro[i])):
            if kakuro[i][j][0] == " | ":
                free_spots.append([i, j])  # si case libre -> alors ajout

        # Attribution des poids en fonction du nombres de cases libres dans chaque ligne ; dans le [1] de les cases correspondantes du kakuro
        for spot in free_spots:
            kakuro[spot[0]][spot[1]][1] += weigth/len(free_spots)  # à opti

    return kakuro


def heat_Mapping_Column(kakuro, weigth):

    # Parcours de toutes les cases avec un double for version colonne  : [j][i]
    for i in range(0, len(kakuro)):

        free_spots = []  # Stockage des cases libres à chaque colonne

        for j in range(0, len(kakuro[i])):
            if kakuro[j][i][0] == " | ":  # si case libre -> alors ajout
                free_spots.append([j, i])

        # Attribution des poids en fonction du nombres de cases libres dans chaque colonne ; dans le [1] de les cases correspondantes du kakuro
        for spot in free_spots:
            kakuro[spot[0]][spot[1]][1] += weigth/len(free_spots)  # à opti

    return kakuro


def set_Heat_Mapping(kakuro):

    # Poid à partager entre les cases
    default_Weigth = 100

    # Mapping des lignes
    mapped_kakuro = heat_Mapping_Row(kakuro, default_Weigth)
    # Mapping des colonnes
    mapped_kakuro = heat_Mapping_Column(kakuro, default_Weigth)

    return mapped_kakuro
