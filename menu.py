import fltk
import sys
import utilitaire
import affichage as af
import boutons
import solveur as sv
import jeu
import affichage
import sauvegarde

def evenement_clic_menu(event, liste_boutons, phase, map, choix, regle, solveur, affichage):
    Xclick, Yclick = fltk.abscisse(event), fltk.ordonnee(event)
    for boutons in liste_boutons:
        if Xclick in range(boutons[0],boutons[2]) and Yclick in range(boutons[1], boutons[3]):
            return actionboutonsmenu(boutons[4], phase, map, choix, regle, solveur, affichage)
    return choix, phase
          
def actionboutonsmenu(action, phase, map, choix, regle, solveur, affichage):
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
        sv.solveur(solveur[0], map[0], regle[0], affichage, choix)
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
        jeu.main(map[0], False, regle[0])
        menu()
    elif action == "Options":
        phase = "Options"
        return choix, phase
    elif action == "Règle":
        map = utilitaire.decalagegauche(regle)
        return choix, phase
    elif action == "Choix de la map":
        map = utilitaire.decalagegauche(map)
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
    map = ["map_mini.txt","map_test.txt","map1.txt","map2.txt", "map3.txt"]
    solveur = ["Profondeur","Largeur","random","Bidirectionnel"]
    affichage = [True, False]
    phase = "Accueil"
    choix = ""
    regle = ["souple", "strict"]
    liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle, solveur, affichage)
    af.affiche_boutons(liste_boutons, 20)

    while True:
            event = fltk.attend_ev()
            tev = fltk.type_ev(event)
            if tev == "ClicGauche":
                choix, phase = evenement_clic_menu(event, liste_boutons, phase, map, choix, regle, solveur, affichage)
                liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle, solveur, affichage)
                af.affiche_boutons(liste_boutons, 20)
            if tev == "Redimension":
                liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle, solveur, affichage)
                af.affiche_boutons(liste_boutons, 20)
            if tev == "Quitte":
                sys.exit()

def choixsauvegarde(Relance): 
    nom_sauvegarde = ""
    affichage.affiche_fenetre_sauvegarde(nom_sauvegarde, Relance)
    ev = fltk.attend_ev()
    nom_touche, nom_sauvegarde = jeu.veriftouche(ev, nom_sauvegarde)
    while nom_touche != "Return":
        affichage.affiche_fenetre_sauvegarde(nom_sauvegarde, Relance)
        ev = fltk.attend_ev()
        nom_touche, nom_sauvegarde = jeu.veriftouche(ev, nom_sauvegarde)
    fltk.efface("sauvegarde")
    return nom_sauvegarde
