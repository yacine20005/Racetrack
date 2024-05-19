import collections
import random
import sys
import affichage
import conversion
import mouvement
import grillage
import sauvegarde as save

def victoire(posparcouru, plateau):
    """Vérifie si la position actuelle du joueur correspond à une victoire.

    Args:
        posparcouru (tuple): Les coordonnées de la position actuelle du joueur.
        plateau (list): Le plateau de jeu.

    Returns:
        bool: True si la position actuelle du joueur correspond à une victoire, False sinon.
    """
    pos = grillage.posactuelle(posparcouru)
    if plateau[pos[1]][pos[0]] == 'A':
        return True
    return False

def solveur_profondeur(grille, chemin, visite, carte, regle, affiche, sauvegarde):
    """
    Fonction qui résout le jeu en utilisant une recherche en profondeur.

    Args:
        grille (list): La grille du problème.
        chemin (list): Le chemin actuel dans la grille.
        visite (set): L'ensemble des positions visitées.
        map (str): La carte des mouvements possibles.
        regle (list): Les règles du problème.
        affiche (bool): Indique si l'affichage doit être activé ou non.
        sauvegarde (str): Nom de la sauvegarde.

    Returns:
        list: Le chemin solution ou None si aucune solution n'est trouvée.
    """
    if len(chemin) < 2:
        vitesse = (0, 0)
    else:
        vitesse = grillage.list_soustraction(chemin[-2], chemin[-1])
        vitesse = (vitesse[0], vitesse[1])
    mvt_possible = mouvement.calcul_posibilite(grille, chemin[-1], chemin, regle)
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:
            if affiche:
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
            elif victoire(chemin + [next_pos], grille):
                save.sauvegarde_partie(chemin + [next_pos], carte, sauvegarde, regle)
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))
            result = solveur_profondeur(grille, chemin + [next_pos], visite, carte, regle, affiche, sauvegarde)
            if result is not None:
                return result
    return None

def solveur_largeur(grille, visite, carte, regle, affiche, sauvegarde):
    """
    Fonction qui résout le jeu en utilisant la méthode de recherche en largeur.

    Args:
        grille (list): La grille du jeu.
        visite (set): Ensemble des positions visitées.
        map (str): La carte du jeu.
        regle (list): Les règles du jeu.
        affiche (bool): Indique si l'affichage doit être activé ou non.
        sauvegarde (str): Le nom de sauvegarde du jeu.

    Returns:
        list: Le chemin solution ou None si aucune solution n'est trouvée
    """
    pile = collections.deque()
    _, pos_depart=grillage.miseenplacepion(grille)
    pile.append(([pos_depart], (0, 0)))
    while len(pile) != 0:
        chemin, vitesse = pile.popleft()
        mvt_possible = mouvement.calcul_posibilite(grille, chemin[-1], chemin, regle)
        for next_pos in mvt_possible:
            if (tuple(next_pos), tuple(vitesse)) not in visite:
                if affiche:
                    affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
                elif victoire(chemin + [next_pos], grille):
                    save.sauvegarde_partie(chemin + [next_pos], carte, sauvegarde, regle)
                    return chemin + [next_pos]
                visite.add((tuple(next_pos), tuple(vitesse)))
                pile.append((chemin + [next_pos], grillage.list_soustraction(chemin[-1], next_pos)))
    return None

def solveur_random(grille, chemin, visite, carte, regle, affiche, sauvegarde):
    """
    Fonction qui résout le jeu en utilisant une approche aléatoire.

    Args:
        grille (list): La grille du problème.
        chemin (list): Le chemin actuel dans la grille.
        visite (set): L'ensemble des positions visitées.
        map (str): La carte du problème.
        regle (str): La règle du problème.
        affiche (list): Indique si l'affichage est activé ou non.
        sauvegarde (bool): Indique le nom de la sauvegarde.

    Returns:
        list: Le chemin solution ou None si aucune solution n'est trouvée.
    """
    if len(chemin) < 2:
        vitesse = (0, 0)
    else:
        vitesse = grillage.list_soustraction(chemin[-2], chemin[-1])
        vitesse = (vitesse[0], vitesse[1])
    mvt_possible = mouvement.calcul_posibilite(grille, chemin[-1], chemin, regle)
    random.shuffle(mvt_possible)
    for next_pos in mvt_possible:
        if (tuple(next_pos), tuple(vitesse)) not in visite:
            if affiche:
                affichage.affiche_tout(grille, mvt_possible, chemin + [next_pos])
            elif victoire(chemin + [next_pos], grille):
                save.sauvegarde_partie(chemin + [next_pos], carte, sauvegarde, regle)
                return chemin + [next_pos]
            visite.add((tuple(next_pos), tuple(vitesse)))
            result = solveur_random(grille, chemin + [next_pos], visite, carte, regle, affiche, sauvegarde)
            if result is not None:
                return result
    return None

def solveur_bidirectionnel(grille, depart, arrivee, carte, regle, affiche, sauvegarde):
    """
    Non fonctionnel pour le moment.
    """
    pile_depart = collections.deque()
    pile_arrivee = collections.deque()

    pile_depart.append(([depart], (0, 0)))
    pile_arrivee.append(([arrivee], (0, 0)))

    visite_depart = set()
    visite_arrivee = set()

    while pile_depart and pile_arrivee:
        chemin_depart, vitesse_depart = pile_depart.popleft()
        chemin_arrivee, vitesse_arrivee = pile_arrivee.popleft()

        mvt_possible_depart = mouvement.calcul_posibilite(grille, chemin_depart[-1], chemin_depart, regle)
        mvt_possible_arrivee = mouvement.calcul_posibilite(grille, chemin_arrivee[-1], chemin_arrivee, regle)

        for next_pos in mvt_possible_depart:
            if (tuple(next_pos), tuple(vitesse_depart)) not in visite_depart:
                if affiche:
                    affichage.affiche_tout(grille, mvt_possible_depart, chemin_depart + [next_pos])
                if tuple(next_pos) in visite_arrivee:
                    save.sauvegarde_partie(chemin_depart + chemin_arrivee[::-1], carte, sauvegarde, regle)
                    return chemin_depart + chemin_arrivee[::-1]
                visite_depart.add((tuple(next_pos), tuple(vitesse_depart)))
                pile_depart.append((chemin_depart + [next_pos], grillage.list_soustraction(chemin_depart[-1], next_pos)))

        for next_pos in mvt_possible_arrivee:
            if (tuple(next_pos), tuple(vitesse_arrivee)) not in visite_arrivee:
                if affiche:
                    affichage.affiche_tout(grille, mvt_possible_arrivee, chemin_arrivee + [next_pos])
                if tuple(next_pos) in visite_depart:
                    save.sauvegarde_partie(chemin_arrivee + chemin_depart[::-1], carte, sauvegarde, regle)
                    return chemin_arrivee + chemin_depart[::-1]
                visite_arrivee.add((tuple(next_pos), tuple(vitesse_arrivee)))
                pile_arrivee.append((chemin_arrivee + [next_pos], grillage.list_soustraction(chemin_arrivee[-1], next_pos)))
    return None

def solveur(choix, carte, regle, affiche, sauvegarde):
    """
    Résout le problème du jeu en fonction des paramètres donnés.

    Args:
        choix (str): Le choix de l'algorithme de résolution ("Profondeur", 
        "Largeur", "Random", "Bidirectionnel").
        map (str): Le chemin vers le fichier contenant la carte du jeu.
        regle (str): La règle de jeu choisi.
        affiche (bool): Indique si l'affichage du jeu est activé ou non.
        sauvegarde (bool): Indique le nom de la sauvegarde du jeu.

    Returns:
        str: Le résultat de la résolution du jeu.
    """
    grille = conversion.conversion_txt(carte)
    _, pos_depart = grillage.miseenplacepion(grille)
    pos_arrivee = grillage.trouver_arrivee(grille)
    visite = set()
    if choix == "Profondeur":
        return solveur_profondeur(grille, [pos_depart], visite, carte, regle, affiche[0], sauvegarde)
    elif choix == "Largeur":
        return solveur_largeur(grille, visite, carte, regle, affiche[0], sauvegarde)
    elif choix == "Random":
        return solveur_random(grille, [pos_depart], visite, carte, regle, affiche[0], sauvegarde)
    elif choix == "Bidirectionnel":
        return solveur_bidirectionnel(grille, pos_depart, pos_arrivee, carte, regle, affiche[0], sauvegarde)
    else:
        return None

sys.setrecursionlimit(10000)
