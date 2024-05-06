import collections
import moteur
import affichage
import fltk
import time
import sys
import main

def solveur_profondeur(grille, chemin, visite, map):
    print('sku')
    if len(chemin) < 2:
        vitesse = (1, 1)
    else:
        vitesse = affichage.list_add2(chemin[-2], chemin[-1])
        vitesse = (abs(vitesse[0]), abs(vitesse[1]))
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, "souple")
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:
            if moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9, "souple")
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(affichage.list_add2(next_pos, chemin[-1]))))
            result = solveur_profondeur(grille, chemin + [next_pos], visite, map)
            if result is not None:
                return result
    return None

def recherche_profondeur_iteratif(grille, chemin_initial, visite, map):
    pile = [(chemin_initial, (1, 1))]
    while pile:
        chemin, vitesse = pile.pop()
        vitesse = (abs(vitesse[0]), abs(vitesse[1]))  # Modify vitesse to absolute value
        mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, "souple")
        for next_pos in mvt_possible:
            affichage.affiche_tout(grille, mvt_possible, chemin)
            if (tuple(next_pos), tuple(vitesse)) not in visite:
                if moteur.victoire(chemin + [next_pos], grille):
                    moteur.sauvegarde_partie(chemin + [next_pos], map, 9, "souple")
                    return True
                visite.add((tuple(next_pos), tuple(affichage.list_add2(next_pos, chemin[-1]))))
                pile.append((chemin + [next_pos], affichage.list_add2(next_pos, chemin[-1])))
    return False


fltk.cree_fenetre(800,800)
sys.setrecursionlimit(100000)
visite = set()
map="map_test.txt"
grille=moteur.conversion_txt(map)
pion, pos_depart=moteur.miseenplacepion(grille)
print(recherche_profondeur_iteratif(grille, [pos_depart], visite, map))