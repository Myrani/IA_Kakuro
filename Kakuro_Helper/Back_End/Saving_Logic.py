import pickle
from Back_End.Heat_Mapping_Logic import *
from Back_End.Possible_Values_Mapping_Logic import *
from Back_End.Grid import *


# Fonction d'ouverte de sauvegarde intelligente
def load_Save():
    # Essaie de load un fichier de sauvegarde présent dans le dossier /Save local
    try:
        grille = []

        with open('Save/save.pkl', 'rb') as save_grille:
            grille = pickle.load(save_grille)

        # Si réussi, renvoie la grille chargée
        return grille
    except Exception as e:
        # Sinon renvoie None
        return None

# Override / Créer un ficher Save.pkl pour y stocker le kakuro passé en paramètre


def push_Save(kakuro):

    with open('Save/save.pkl', 'wb') as save_instruction:
        pickle.dump(kakuro, save_instruction)

    return None


def dynamic_Load():
    # Regarge si un ficher save est disponible
    grille = load_Save()

    # Si aucun fichier n'est trouvé Créer un kakuro par défault
    if grille == None:

        print("[Default Loading] : No save found, creating a preset Kakuro")
        kakuro_projet = grid_Maker__Default(8, 8, [[0, 2, "11|#"], [0, 3, "4|#"], [1, 1, "14|5"], [1, 4, "10|#"], [2, 0, "#|17"], [2, 5, "3|#"],
                                                   [3, 0, "#|6"], [3, 3, "3|4"], [3, 6, "H|#"], [4, 1, "#|10"], [4, 6, "H|#"], [5, 2, "#|3"], [5, 5, "H|#"], [6, 3, "H|#"], [6, 4, "H|#"]])
        kakuro_projet = set_Heat_Mapping(kakuro_projet)
        kakuro_projet = set_Objective_Propagation(kakuro_projet)

        return kakuro_projet

    # Sinon le renvoie !
    elif isinstance(grille, list):
        print("[Save Detected] : Loading saved Kakuro")
        return grille
