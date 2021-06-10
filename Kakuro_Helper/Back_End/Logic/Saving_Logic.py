import pickle
import os

from Back_End.Logic.Heat_Mapping_Logic import *
from Back_End.Logic.Possible_Values_Mapping_Logic import set_Objective_Propagation, set_Possible_Values_Mapping
from Back_End.Logic.Grid_Logic import *


# Fonction pour load le dictionnaire de sommes

def load_Sums():
    with open('Back_End/Ressources/sums.pkl', 'rb') as sums:
        return pickle.load(sums)


# Fonction d'ouverte de sauvegarde intelligente
def load_Default_Save():
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


def load_Kakuro_From_File(filename):
    with open('Save/'+filename, 'rb') as save_grille:
        grille = pickle.load(save_grille)

    return grille


# Permet d'écrire le kakuro en paramètre dans un fichier pkl
def push_Save(kakuro):

    with open('Save/save.pkl', 'wb') as save_instruction:
        pickle.dump(kakuro, save_instruction)

    return None


def dynamic_Load():
    # Regarge si un ficher save est disponible
    grille = load_Default_Save()

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

# Partie de logique de la fenêtre de création


def push_Creator(kakuro):
    # print(os.getcwd())
    modifiedKakuro = extract_user_kakuro(kakuro)
    # terminalPrintFullRaw(modifiedKakuro)
    mofifiedKakuro = set_Heat_Mapping(modifiedKakuro)
    # terminalPrintFullRaw(modifiedKakuro)
    modifiedKakuro = set_Objective_Propagation(modifiedKakuro)
    # terminalPrintFullRaw(modifiedKakuro)
    mofifiedKakuro = set_Possible_Values_Mapping(modifiedKakuro)
    # terminalPrintFullRaw(modifiedKakuro)
    with open(os.getcwd()+'/Save_Creator_Result/save.pkl', 'wb') as save_instruction:
        pickle.dump(modifiedKakuro, save_instruction)

    return None


def extract_user_kakuro(kakuro):
    kakuroToSave = []
    for x in range(0, len(kakuro)):
        # 0              1       2                                3                                    4                                5
        # Type de case , Heat , Liste des objectifs de la case , valeurs possible pour les objectifs , Liste des valeures Contraintes , Cases étant selectionnées
        kakuroToSave.append([[kakuro[x][y][1], 0, [], [], [], []]
                            for y in range(0, len(kakuro[x]))])

    return kakuroToSave


# Partie logique de la fenêtre de Load du kakuro


def get_All_Saves():
    list_of_files = []

    for root, dirs, files in os.walk("Save/"):
        for file in files:
            list_of_files.append(file)

    return list_of_files
