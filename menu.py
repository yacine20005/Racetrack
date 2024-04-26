import fltk
import sys
import main
import moteur
import affichage
import boutons

def evenement_clic_menu(event, liste_boutons, phase, map, choix):
    Xclick, Yclick = fltk.abscisse(event), fltk.ordonnee(event)
    for boutons in liste_boutons:
        if Xclick in range(boutons[0],boutons[2]) and Yclick in range(boutons[1], boutons[3]):
            return actionboutonsmenu(boutons[4], phase, map, choix)
    return phase
          
def actionboutonsmenu(action, phase, map, choix):
    if action == "Jouer":
        phase = "Jouer"
        return phase
    elif action == "Regles":
        phase = "Regles"
        return phase
    elif action == "Quitter":
        sys.exit()
    elif action == "Nouvelle Partie":
        phase = "Choix"
        return phase
    elif action == "Charger":
        phase = "Charger"
        return phase
    elif action == "Retour":
        phase = "Accueil"
        return phase
    elif action =="‎Jouer‎":
        main.main(map[0], charge=False)
        menu()
    elif action == "Choix de la map":
        map = moteur.decalagegauche(map)
        return phase
    elif action == "‎Retour‎":
        phase = "Jouer"
        return phase
    elif action == "‎Charger‎":
        main.main(moteur.charger_fichier(choix),True)
    elif action == f"Choix de la sauvegarde : {choix}":
        choix = moteur.choixsauvegarde()
        main.main(moteur.charger_fichier(choix),True)
    else:
        return phase
    

def menu():
    map = ["map_mini.txt","map_test.txt","map1.txt","map2.txt",]
    phase = "Accueil"
    choix = 1
    liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix)
    affichage.affiche_boutons(liste_boutons, 20)

    while True:
            event = fltk.attend_ev()
            tev = fltk.type_ev(event)
            if tev == "ClicGauche":
                phase = evenement_clic_menu(event, liste_boutons, phase, map, choix)
                liste_boutons = boutons.initialiseboutonsmenu(phase, map, choix)
                affichage.affiche_boutons(liste_boutons, 20)
            if tev == "Quitte":
                sys.exit()

fltk.cree_fenetre(800,800, redimension=True)
menu()