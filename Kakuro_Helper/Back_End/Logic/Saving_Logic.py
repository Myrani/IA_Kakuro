import pickle
import os

from Back_End.Logic.Heat_Mapping_Logic import *
from Back_End.Logic.Grids import *

# Fonction pour load le dictionnaire de sommes


class Datahandler():
    def __init__(self):
        pass

    def loadSums(self):
        with open('Back_End/Ressources/sums.pkl', 'rb') as sums:
            return pickle.load(sums)

    def loadDefaultSave(self):
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

    def loadKakuroFromFile(self, filename):
        with open('Save/'+filename, 'rb') as save_grille:
            grille = pickle.load(save_grille)

        return grille

    def pushSaveWithName(self, kakuro, name):

        with open('Save/'+name+'.pkl', 'wb') as file:
            pickle.dump(kakuro, file)

        return None

    def pushCreator(self, kakuro):
        kakuro.printAll()
        with open(os.getcwd()+'/Save_Creator_Result/save.pkl', 'wb') as file:
            pickle.dump(kakuro, file)

        print("Saved !")

        return None

    def getAllSaves(self):
        list_of_files = []

        for root, dirs, files in os.walk("Save/"):
            for file in files:
                list_of_files.append(file)

        return list_of_files

    def dynamicLoad(self):
        # Regarge si un ficher save est disponible
        grille = self.loadDefaultSave()

        # Si aucun fichier n'est trouvé Créer un kakuro par défault
        if grille == None:

            print("[Default Loading] : No save found, creating a preset Kakuro")
            creator = CreatorGrid(7, 7)

            return creator.GenerateSolverGrid()

    # Sinon le renvoie !
        elif isinstance(grille, list):
            print("[Save Detected] : Loading saved Kakuro")
            return grille
