

def heat_Mapping_Row__Refactored(kakuro, heat_map, weigth):
    # Parcours de toutes les cases avec un double for ; version ligne  : [i][j]
    for i in range(0, len(kakuro)):

        free_spots = []  # Stockage des cases libres à chaque ligne

        for j in range(0, len(kakuro[i])):
            if kakuro[i][j][0] == " | ":
                free_spots.append([i, j])  # si case libre -> alors ajout

        # Attribution des poids en fonction du nombres de cases libres dans chaque ligne ; dans le [1] de les cases correspondantes du kakuro
        for spot in free_spots:
            heat_map[spot[0]][spot[1]] += weigth/len(free_spots)

    return heat_map


def heat_Mapping_Column__Refactored(kakuro, heat_map, weigth):
    # Parcours de toutes les cases avec un double for version colonne  : [j][i]
    for i in range(0, len(kakuro)):

        free_spots = []  # Stockage des cases libres à chaque colonne

        for j in range(0, len(kakuro[i])):
            if kakuro[j][i] == " | ":  # si case libre -> alors ajout
                free_spots.append([j, i])

            else:
                # Attribution des poids en fonction du nombres de cases libres dans chaque colonne ; dans le [1] de les cases correspondantes du kakuro
                for spot in free_spots:
                    heat_map[spot[0]][spot[1]] += weigth / len(free_spots)

                free_spots = []

        if len(free_spots) != 0:
            for spot in free_spots:
                heat_map[spot[0]][spot[1]] += weigth / len(free_spots)

            free_spots = []

    return heat_map


def set_Heat_Mapping__Refactored(kakuro):

    # Poid à partager entre les cases
    default_Weigth = 100

    # HeatMap
    heat_map = [[0 for x in range(0, len(kakuro))]
                for y in range(0, len(kakuro))]
    # Mapping des lignes
    heat_map = heat_Mapping_Row__Refactored(
        kakuro, heat_map, default_Weigth)
    # Mapping des colonnes
    heat_map = heat_Mapping_Column__Refactored(
        kakuro, heat_map, default_Weigth)

    return heat_map
