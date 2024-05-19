import sys
import utilitaire
import fltk
import affichage as af
import boutons
import solveur as sv
import jeu
import sauvegarde

def evenement_clic_menu(event, liste_boutons, phase, carte, choix, regle, solveur, affichage):
    """
    Gère l'événement de clic sur le menu.

    Args:
        event (type): L'événement de clic.
        liste_boutons (type): La liste des boutons du menu.
        phase (type): La phase actuelle du jeu.
        map (type): La carte du jeu.
        choix (type): Le choix actuel du joueur.
        regle (type): Les règles du jeu.
        solveur (type): Le solveur du jeu.
        affichage (type): L'affichage du jeu.

    Returns:
        type: Le choix et la phase mis à jour.
    """
    xclick, yclick = fltk.abscisse(event), fltk.ordonnee(event)
    for btn in liste_boutons:
        if xclick in range(btn[0],btn[2]) and yclick in range(btn[1], btn[3]):
            return actionboutonsmenu(btn[4], phase, carte, choix, regle, solveur, affichage)
    return choix, phase

def actionboutonsmenu(action, phase, carte, choix, regle, solveur, affichage):
    """
    Cette fonction gère les actions des boutons dans le menu du jeu.

    Args:
        action (str): L'action du bouton sélectionné.
        phase (str): La phase actuelle du jeu.
        map (list): La liste des cartes disponibles.
        choix (str): Le choix actuel du joueur.
        regle (str): La règle actuelle du jeu.
        solveur (str): Le solveur actuel du jeu.
        affichage (str): L'affichage actuel du jeu.

    Returns:
        tuple: Un tuple contenant le choix et la phase mis à jour.
    """
    if action == "Jouer":
        phase = "Jouer"
        return choix, phase
    elif action == "Solveur":
        phase = "Solveur"
        return choix, phase
    elif action == "Quitter":
        sys.exit()
    elif action == "Résoudre":
        choix = choixsauvegarde(False)
        sv.solveur(solveur[0], carte[0], regle[0], affichage, choix)
        return choix, phase
    elif action == "  Options  ":
        phase = "  Options  "
        return choix, phase
    elif action == "Choix du solveur":
        solveur = utilitaire.decalagegauche(solveur)
        return choix, phase
    elif action == "Affichage":
        affichage = utilitaire.decalagegauche(affichage)
        return choix, phase
    elif action == "      Retour      ":
        phase = "Solveur"
        return choix, phase
    elif action == "Nouvelle Partie":
        phase = "Choix"
        return choix, phase
    elif action == "Charger":
        phase = "Charger"
        return choix, phase
    elif action == "Retour":
        phase = "Accueil"
        return choix, phase
    elif action =="Lancer":
        jeu.main(carte[0], False, regle[0])
        menu()
    elif action == "Options":
        phase = "Options"
        return choix, phase
    elif action == "Règle":
        carte = utilitaire.decalagegauche(regle)
        return choix, phase
    elif action == "Choix de la map":
        carte = utilitaire.decalagegauche(carte)
        return choix, phase
    elif action == "  Retour  ":
        phase = "Choix"
        return choix, phase
    elif action == " Retour ":
        phase = "Jouer"
        return choix, phase
    elif action == " Charger ":
        jeu.main(sauvegarde.charger_fichier(choix),True, regle[0])
        return "", "Accueil"
    elif action == "Choix de la sauvegarde":
        choix = choixsauvegarde(False)
        return choix, phase
    else:
        return choix, phase

def menu():
    """
    Fonction qui affiche le menu du jeu et gère les interactions avec l'utilisateur.

    return: None
    """
    carte = ["map_mini.txt","map_test.txt","map1.txt","map2.txt", "map3.txt"]
    solveur = ["Profondeur","Largeur","random","Bidirectionnel"]
    affichage = [True, False]
    phase = "Accueil"
    choix = ""
    regle = ["souple", "strict"]
    liste_boutons = boutons.initialiseboutonsmenu(phase, carte, choix, regle, solveur, affichage)
    af.affiche_boutons(liste_boutons, 20)
    while True:
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            choix, phase = evenement_clic_menu(event, liste_boutons, phase, carte, choix, regle, solveur, affichage)
            liste_boutons = boutons.initialiseboutonsmenu(phase, carte, choix, regle, solveur, affichage)
            af.affiche_boutons(liste_boutons, 20)
        if tev == "Redimension":
            liste_boutons = boutons.initialiseboutonsmenu(phase, carte, choix, regle, solveur, affichage)
            af.affiche_boutons(liste_boutons, 20)
        if tev == "Quitte":
            sys.exit()

def choixsauvegarde(relance):
    """Permet à l'utilisateur de choisir un nom de sauvegarde.

    Args:
        relance (bool): Indique si le jeu a été relancé ou non.

    Returns:
        str: Le nom de la sauvegarde choisie par l'utilisateur.
    """
    nom_sauvegarde = ""
    af.affiche_fenetre_sauvegarde(nom_sauvegarde, relance)
    ev = fltk.attend_ev()
    nom_touche, nom_sauvegarde = jeu.veriftouche(ev, nom_sauvegarde)
    while nom_touche != "Return":
        af.affiche_fenetre_sauvegarde(nom_sauvegarde, relance)
        ev = fltk.attend_ev()
        nom_touche, nom_sauvegarde = jeu.veriftouche(ev, nom_sauvegarde)
    fltk.efface("sauvegarde")
    return nom_sauvegarde
