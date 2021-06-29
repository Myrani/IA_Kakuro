import pickle
import os

from Back_End.Logic.Heat_Mapping_Logic import *
from Back_End.Logic.Grid_Logic import *
from Back_End.Logic.Grids import *

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
        creator = CreatorGrid(7, 7)

        return creator.GenerateSolverGrid()

    # Sinon le renvoie !
    elif isinstance(grille, list):
        print("[Save Detected] : Loading saved Kakuro")
        return grille

# Partie de logique de la fenêtre de création


def push_Creator(kakuro):
    kakuro.printAll()
    with open(os.getcwd()+'/Save_Creator_Result/save.pkl', 'wb') as file:
        pickle.dump(kakuro, file)

    print("Saved !")

    return None


# Partie logique de la fenêtre de Load du kakuro


def get_All_Saves():
    list_of_files = []

    for root, dirs, files in os.walk("Save/"):
        for file in files:
            list_of_files.append(file)

    return list_of_files
