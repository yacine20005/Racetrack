import collections
import moteur
import affichage
import fltk
import time
import sys
import main

def solveur_profondeur(grille, chemin, visite, map):
    if len(chemin) < 2:
        vitesse = (1, 1)
    else:
        vitesse = affichage.list_add2(chemin[-2], chemin[-1])
        vitesse = (abs(vitesse[0]), abs(vitesse[1]))
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, "souple")
    for next_pos in mvt_possible:
        print((tuple(next_pos), tuple(vitesse)) not in visite)
        if (tuple(next_pos), tuple(vitesse)) not in visite:                      
            if moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9, "souple")
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))         
            result = solveur_profondeur(grille, chemin + [next_pos], visite, map)
            if result is not None:
                return result
    return None

fltk.cree_fenetre(700,700)
sys.setrecursionlimit(100000)
visite = set()
map="map2.txt"
grille=moteur.conversion_txt(map)
pion, pos_depart=moteur.miseenplacepion(grille)
print(solveur_profondeur(grille, [pos_depart], visite, map))