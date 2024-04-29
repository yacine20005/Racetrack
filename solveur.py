import collections
import moteur
import affichage
import fltk
        
def solveur_profondeur(grille, pos_depart):
    fltk.cree_fenetre(888, 666)
    deque = collections.deque()
    deque.append((pos_depart, [pos_depart]))
    visite = []
    while deque != []:
        (pos, chemin) = deque.pop()
        mvt_possible = moteur.calcul_posibilite(grille, pos, chemin)
        for next_pos in mvt_possible:
            if next_pos not in visite:
                if moteur.victoire(chemin + [next_pos], grille):
                    return chemin + [next_pos]
                deque.append((next_pos, chemin + [next_pos]))
                visite.append(next_pos)
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
    return None

grille = moteur.conversion_txt("map_test.txt")
pion, pos_depart = moteur.miseenplacepion(grille)
solveur_profondeur(grille, pos_depart)

# deque = collections.deque()
# print(deque)
# deque.append((pos_depart, [pos_depart]))
# print(deque)
# (pos, chemin) = deque.pop()
# print(deque)
# deque.append(([3, 1], chemin + [[3, 1]]))
# print(deque)