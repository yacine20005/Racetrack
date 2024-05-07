import fltk
import sys
import main
import moteur
import affichage
import boutons

def evenement_clic_menu(event, liste_boutons, phase, map, choix, regle):
    Xclick, Yclick = fltk.abscisse(event), fltk.ordonnee(event)
    for boutons in liste_boutons:
        if Xclick in range(boutons[0],boutons[2]) and Yclick in range(boutons[1], boutons[3]):
            return actionboutonsmenu(boutons[4], phase, map, choix, regle)
    return choix, phase
          
def actionboutonsmenu(action, phase, map, choix, regle):
    if action == "Jouer":
        phase = "Jouer"
        return choix, phase
    elif action == "Regles":
        phase = "Regles"
        return choix, phase
    elif action == "Quitter":
        #alt + 060
        #espaces insécables
        sys.exit()
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
        main.main(map[0], False, regle[0])
        menu()
    elif action == "Options":
        phase = "Options"
        return choix, phase
    elif action == "Règle":
        map = moteur.decalagegauche(regle)
        return choix, phase
    elif action == "Choix de la map":
        map = moteur.decalagegauche(map)
        return choix, phase
    elif action == "‎‎Retour‎‎":
        phase = "Choix"
        return choix, phase
    elif action == "‎Retour‎":
        phase = "Jouer"
        return choix, phase
    elif action == "‎Charger‎":
        main.main(moteur.charger_fichier(choix),True, regle[0])
        return "", "Accueil"
    elif action == "Choix de la sauvegarde":
        choix = affichage.choixsauvegarde(False)
        phase = "Charger"
        return choix, phase
    else:
        return choix, phase
    
def menu():
    map = ["map_mini.txt","map_test.txt","map1.txt","map2.txt", "map3.txt"]
    phase = "Accueil"
    choix = ""
    regle = ["souple", "strict"]
    liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle)
    affichage.affiche_boutons(liste_boutons, 20)

    while True:
            event = fltk.attend_ev()
            tev = fltk.type_ev(event)
            if tev == "ClicGauche":
                choix, phase = evenement_clic_menu(event, liste_boutons, phase, map, choix, regle)
                liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle)
                affichage.affiche_boutons(liste_boutons, 20)
            if tev == "Redimension":
                liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix, regle)
                affichage.affiche_boutons(liste_boutons, 20)
            if tev == "Quitte":
                sys.exit()

fltk.cree_fenetre(800,800, redimension=True)
menu()