import moteur
import affichage
import fltk
import sys
import collections

def solveur_profondeur(grille, chemin, visite, map):
    if len(chemin) < 2:
        vitesse = (0, 0)
    else:
        vitesse = affichage.list_add2(chemin[-2], chemin[-1])
        vitesse = (vitesse[0], vitesse[1])
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, "strict")
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:      
            affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
            if moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9, "strict")
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))         
            result = solveur_profondeur(grille, chemin + [next_pos], visite, map)
            if result is not None:
                return result
    return None

def solveur_largeur(grille, map):
    visite = set()
    pile = collections.deque()
    pion, pos_depart=moteur.miseenplacepion(grille)
    pile.append(([pos_depart], (0, 0)))
    while len(pile) != 0:
        chemin, vitesse = pile.popleft()
        mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, "strict")
        for next_pos in mvt_possible:
            if (tuple(next_pos), tuple(vitesse)) not in visite:  
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])    
                if moteur.victoire(chemin + [next_pos], grille):
                    moteur.sauvegarde_partie(chemin + [next_pos], map, 9, "strict")
                    return chemin + [next_pos]
                visite.add((tuple(next_pos), tuple(vitesse)))
                pile.append((chemin + [next_pos], affichage.list_add2(chemin[-1], next_pos)))
    return None


fltk.cree_fenetre(800,800)
sys.setrecursionlimit(10000)
visite = set()
map="map2.txt"
grille=moteur.conversion_txt(map)
print(solveur_largeur(grille, map))