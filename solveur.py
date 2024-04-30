import collections
import moteur


def solveur_old(grille, pos_depart, map):
    deque = collections.deque()
    deque.append((pos_depart, [pos_depart],
                  moteur.list_add2(pos_depart, pos_depart)))
    visite = []
    #set
    while deque != []:
        print(deque)
        (pos, chemin, vitesse) = deque.pop()
        mvt_possible = moteur.calcul_posibilite(grille, pos, chemin)
        if not moteur.defaite(mvt_possible):
            for next_pos in mvt_possible:
                if (next_pos, vitesse) in visite:
                    print("Lavabo")
                elif (next_pos, vitesse) not in visite:
                    if moteur.victoire(chemin + [next_pos], grille):
                        moteur.sauvegarde_partie(chemin + [next_pos], map, 9)
                        return chemin + [next_pos]
                    deque.append((next_pos, chemin + [next_pos], moteur.list_add2(next_pos, pos)))
                    visite.append((next_pos, moteur.list_add2(next_pos, pos)))
    return None

def solveur_profondeur(grille, chemin, visite, map):
    print('sku')
    if len(chemin) < 2:
        vitesse = (1, 1)
    else:
        vitesse = moteur.list_add2(chemin[-2], chemin[-1])
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin)
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) in visite:
            return None
        elif (tuple(next_pos), tuple(vitesse)) not in visite:
            if moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9)
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(moteur.list_add2(next_pos, chemin[-1]))))
            return solveur_profondeur(grille, chemin + [next_pos], visite, map)

visite = set()
map="map1.txt"
grille=moteur.conversion_txt(map)
pion, pos_depart=moteur.miseenplacepion(grille)
solveur_profondeur(grille, [pos_depart], visite, map)