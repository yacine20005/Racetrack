import moteur
import affichage
import fltk
import sys
import collections
import random

def solveur_profondeur(grille, chemin, visite, map, regle, affiche):
    if len(chemin) < 2:
        vitesse = (0, 0)
    else:
        vitesse = affichage.list_add2(chemin[-2], chemin[-1])
        vitesse = (vitesse[0], vitesse[1])
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, regle)
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:
            if affiche:
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
            elif moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9, regle)
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))         
            result = solveur_profondeur(grille, chemin + [next_pos], visite, map, regle, affiche)
            if result is not None:
                return result
    return None

def solveur_largeur(grille, visite, map, regle, affiche):
    pile = collections.deque()
    pion, pos_depart=moteur.miseenplacepion(grille)
    pile.append(([pos_depart], (0, 0)))
    while len(pile) != 0:
        chemin, vitesse = pile.popleft()
        mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, regle)
        for next_pos in mvt_possible:
            if (tuple(next_pos), tuple(vitesse)) not in visite:  
                if affiche:
                    affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
                elif moteur.victoire(chemin + [next_pos], grille):
                    moteur.sauvegarde_partie(chemin + [next_pos], map, 9, regle)
                    return chemin + [next_pos]
                visite.add((tuple(next_pos), tuple(vitesse)))
                pile.append((chemin + [next_pos], affichage.list_add2(chemin[-1], next_pos)))
    return None

def solveur_random(grille, chemin, visite, map, regle, affiche):
    if len(chemin) < 2:
        vitesse = (0, 0)
    else:
        vitesse = affichage.list_add2(chemin[-2], chemin[-1])
        vitesse = (vitesse[0], vitesse[1])
    mvt_possible = moteur.calcul_posibilite(grille, chemin[-1], chemin, regle)
    random.shuffle(mvt_possible)
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:
            if affiche:
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
            elif moteur.victoire(chemin + [next_pos], grille):
                moteur.sauvegarde_partie(chemin + [next_pos], map, 9, regle)
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))         
            result = solveur_random(grille, chemin + [next_pos], visite, map, regle, affiche)
            if result is not None:
                return result
    return None

def solveur_bidirectionnel(grille, depart, arrivee, map, regle, affiche):
    pile_depart = collections.deque()
    pile_arrivee = collections.deque()
    
    pile_depart.append(([depart], (0, 0)))
    pile_arrivee.append(([arrivee], (0, 0)))
    
    visite_depart = set()
    visite_arrivee = set()
    
    while pile_depart and pile_arrivee:
        chemin_depart, vitesse_depart = pile_depart.popleft()
        chemin_arrivee, vitesse_arrivee = pile_arrivee.popleft()
        
        mvt_possible_depart = moteur.calcul_posibilite(grille, chemin_depart[-1], chemin_depart, regle)
        mvt_possible_arrivee = moteur.calcul_posibilite(grille, chemin_arrivee[-1], chemin_arrivee, regle)
        
        for next_pos in mvt_possible_depart:
            if (tuple(next_pos), tuple(vitesse_depart)) not in visite_depart:
                if tuple(next_pos) in visite_arrivee:
                    moteur.sauvegarde_partie(chemin_depart + chemin_arrivee[::-1], map, 9, regle)
                    return chemin_depart + chemin_arrivee[::-1]
                visite_depart.add((tuple(next_pos), tuple(vitesse_depart)))
                pile_depart.append((chemin_depart + [next_pos], affichage.list_add2(chemin_depart[-1], next_pos)))
                
        for next_pos in mvt_possible_arrivee:
            if (tuple(next_pos), tuple(vitesse_arrivee)) not in visite_arrivee:
                if tuple(next_pos) in visite_depart:
                    moteur.sauvegarde_partie(chemin_arrivee + chemin_depart[::-1], map, 9, regle)
                    return chemin_arrivee + chemin_depart[::-1]
                visite_arrivee.add((tuple(next_pos), tuple(vitesse_arrivee)))
                pile_arrivee.append((chemin_arrivee + [next_pos], affichage.list_add2(chemin_arrivee[-1], next_pos)))
    return None

def solveur(choix, map, regle, affiche, sauvegarde):
    grille=moteur.conversion_txt(map)
    pion, pos_depart = moteur.miseenplacepion(grille)
    pos_arrivee = moteur.trouver_arrivee(grille)
    visite = set()
    if choix == "Profondeur":
        return solveur_profondeur(grille, [pos_depart], visite, map, regle, affiche[0])
    elif choix == "Largeur":
        return solveur_largeur(grille, visite, map, regle, affiche[0])
    elif choix == "Random":
        return solveur_random(grille, [pos_depart], visite, map, regle, affiche[0])
    elif choix == "Bidirectionnel":
        return solveur_bidirectionnel(grille, pos_depart, pos_arrivee, map, regle, affiche[0])
    else:
        return None
    
"""fltk.cree_fenetre(800,800)
sys.setrecursionlimit(10000)
solveur("Bidirectionnel", "map2.txt", "souple", False)"""