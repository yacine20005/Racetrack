import menu
import os

def sauvegarde_partie(posparcouru, map, numero, regle):
    print("sauvegarde en cours..")
    chemin = f"./sauvegardes/{numero}.txt"
    sauvegarde = str([posparcouru, map, regle])
    with open(chemin, mode = "w") as mon_fichier:
        mon_fichier.write(sauvegarde)

def charger_fichier(fichier):
    print(os.path.exists(f"./sauvegardes/{fichier}.txt"))
    if os.path.exists(f"./sauvegardes/{fichier}.txt"):
        with open(f"./sauvegardes/{fichier}.txt") as fichier:
            readlines = fichier.readlines()
            print(eval(readlines[0]))
            return eval(readlines[0])
    else:
        choix = menu.choixsauvegarde(True)
        return charger_fichier(choix)