import sys
import affichage
import fltk

def creer_grille(x, y):
    """Crée une grille de dimensions x par y remplie de zéros.

    Args:
        x (int): Le nombre de colonnes de la grille.
        y (int): Le nombre de lignes de la grille.

    Returns:
        list: Une liste de listes représentant la grille remplie de zéros.
    """
    grille = []
    for _ in range(y):
        ligne = []
        for _ in range(x):
            ligne.append(0)
        grille.append(ligne)
    return grille

def afficher_grille(grille):
    """
    Affiche la grille passée en paramètre.

    Args:
        grille (list): Une liste de listes représentant la grille à afficher.
    """
    for ligne in grille:
        print(ligne)

def posdepart(plateau):
    """
    Renvoie les coordonnées des cases contenant la lettre "D" dans le plateau.

    Args:
        plateau (list): Le plateau de jeu représenté par une liste de listes.

    Returns:
        list: Une liste contenant les coordonnées des cases contenant la lettre "D".
    """
    zonedepart = []
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            if plateau[y][x]=="D":
                zonedepart.append([x,y])
    return zonedepart

def miseenplacepion(plateau):
    """Place le pion au centre de la zone de départ et renvoie la grille et la position de départ.

    Args:
        plateau (list): Le plateau de jeu.

    Returns:
        tuple: Un tuple contenant la grille mise à jour et la position de départ du pion.
    """
    len_y = len(plateau)
    len_x = len(plateau[0])
    liste_pos_x = []
    liste_pos_y = []
    pos_final_x, pos_final_y = 0,0
    grille = creer_grille(len_x, len_y)
    for y in range(len(plateau)):
        for x in range(len(plateau[0])):
            if plateau[y][x] == "D":
                liste_pos_x.append(x)
                liste_pos_y.append(y)
    pos_final_x = (max(liste_pos_x) + min(liste_pos_x)) // 2
    pos_final_y = (max(liste_pos_y) + min(liste_pos_y)) // 2
    grille[pos_final_y][pos_final_x] = 1
    pos_depart = [pos_final_x,pos_final_y]
    return grille, pos_depart

def depart(plateau):
    """Démarre le jeu en affichant le plateau initial et en permettant aux joueurs de jouer.

    Args:
        plateau (list): Le plateau de jeu.

    Returns:
        tuple: Un tuple contenant le plateau avec les pions déplacés et 
        la dernière position parcourue.
    """
    mvtpossible = posdepart(plateau)
    affichage.affiche_depart(plateau, mvtpossible)
    pos_parcouru = []
    plateau_pion = creer_grille(len(plateau), len(plateau[1]))
    while not pos_parcouru:
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if tev == "ClicGauche":
            gerer_evenement(ev, plateau_pion,
                                   mvtpossible, pos_parcouru)
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    return plateau_pion, pos_parcouru[-1]


def remiseenplace(pos_actuelle, plateau):
    """Place la position actuelle sur une nouvelle grille.

    Cette fonction prend en paramètre la position actuelle et le plateau de jeu.
    Elle crée une grille vide de même taille que le plateau, place la position 
    actuelle sur la grille
    et renvoie la grille mise à jour.

    Args:
        pos_actuelle (tuple): La position actuelle sur le plateau de jeu.
        plateau (list): Le plateau de jeu.

    Returns:
        list: Une grille mise à jour avec la position actuelle.
    """
    len_y = len(plateau)
    len_x = len(plateau[0])
    grille = creer_grille(len_y, len_x)
    grille[pos_actuelle[1]][pos_actuelle[0]] = 1
    return grille

def posactuelle(pos_parcouru):
    """Retourne la position actuelle du parcours.

    Args:
        pos_parcouru (list): Une liste contenant les positions parcourues.

    Returns:
        int: La position actuelle du parcours.
    """
    return pos_parcouru[-1]

def trouver_arrivee(plateau):
    """
    Cette fonction permet de trouver la position de l'arrivée sur le plateau.

    Args:
        plateau (list): Le plateau de jeu représenté par une liste de listes.

    Returns:
        list: Les coordonnées [x, y] de l'arrivée sur le plateau.
    """
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            if plateau[y][x] == "A":
                return [x, y]

def list_addition(a, b):
    """
    Cette fonction prend deux listes, `a` et `b`, et renvoie une nouvelle liste
    contenant l'addition élément par élément des éléments correspondants de `a` et `b`.

    Args:
        a (list): La première liste.
        b (list): La deuxième liste.

    Returns:
        list: Une nouvelle liste contenant l'addition élément par élément de `a` et `b`.
    """
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def list_soustraction(a, b):
    """
    Cette fonction prend deux listes, `a` et `b`, et renvoie une nouvelle liste
    contenant la soustraction élément par élément des éléments correspondants de `a` et `b`.

    Args:
        a (list): La première liste.
        b (list): La deuxième liste.

    Returns:
        list: Une nouvelle liste contenant la soustraction élément par élément de `a` et `b`.
    """
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result

def gerer_evenement(ev, plateau_pion, mvtpossible, pos_parcouru):
    """
    Gère un événement de clic sur le plateau de jeu.

    Args:
        ev (fltk.Event): L'événement de clic.
        plateau_pion (list): Le plateau de jeu contenant les pions.
        mvtpossible (list): Les mouvements possibles.
        pos_parcouru (list): Les positions parcourues.

    Returns:
        None
    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau_pion)
    largeur_case = fltk.largeur_fenetre() / len(plateau_pion[0])
    x_click, y_click = fltk.abscisse(ev), fltk.ordonnee(ev)
    x_case_click = int((x_click+largeur_case//2) // largeur_case)
    y_case_click = int((y_click+hauteur_case//2) // hauteur_case)
    if [x_case_click, y_case_click] in mvtpossible:
        if len(pos_parcouru) > 1:
            poseactuelle = posactuelle(pos_parcouru)
            plateau_pion[poseactuelle[1]][poseactuelle[0]] = 0
            plateau_pion[y_case_click][x_case_click] = 1
        pos_parcouru.append([x_case_click, y_case_click])
