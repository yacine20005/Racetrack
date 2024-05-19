import os

def sauvegarde_partie(posparcouru, carte, numero, regle):
    """Sauvegarde les informations de la partie dans un fichier texte.

    Args:
        posparcouru (list): Liste des positions parcourues.
        map (str): Chaîne de caractères représentant la carte.
        numero (int): Numéro de la sauvegarde.
        regle (str): Chaîne de caractères représentant les règles du jeu.
    """
    print("sauvegarde en cours..")
    chemin = f"./sauvegardes/{numero}.txt"
    sauvegarde = str([posparcouru, carte, regle])
    with open(chemin, mode="w", encoding="utf-8") as mon_fichier:
        mon_fichier.write(sauvegarde)

def charger_fichier(fichier):
    """
    Charge les données à partir d'un fichier de sauvegarde.

    Args:
        fichier (str): Le nom du fichier de sauvegarde.

    Returns:
        tab: Les données chargées à partir du fichier de sauvegarde.
    """
    import menu
    print(os.path.exists(f"./sauvegardes/{fichier}.txt"))
    if os.path.exists(f"./sauvegardes/{fichier}.txt"):
        with open(f"./sauvegardes/{fichier}.txt", encoding="utf-8") as fichier:
            readlines = fichier.readlines()
            print(eval(readlines[0]))
            return eval(readlines[0])
    else:
        choix = menu.choixsauvegarde(True)
        return charger_fichier(choix)
