import math
import fltk
import grillage

def calcul_posibilite(plateau, pospion, posparcouru, regle):
    """Calcule les positions possibles pour un pion sur un plateau de jeu.

    Args:
        plateau (list): Le plateau de jeu.
        pospion (list): La position actuelle du pion.
        posparcouru (list): Les positions déjà parcourues par le pion.
        regle (int): La règle du jeu.

    Returns:
        list: Une liste contenant les positions possibles pour le pion.
    """
    voisinpossibilite = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    mvtpossible = []
    if len(posparcouru) <= 1:
        pospotentielle = pospion
    else:
        distanceprecedent = grillage.list_soustraction(pospion, posparcouru[-2])
        pospotentielle = grillage.list_addition(pospion, distanceprecedent)
        if coup_possible(plateau, pospion, pospotentielle, regle):
            mvtpossible.append(pospotentielle)
    for pos in voisinpossibilite:
        posacheck = grillage.list_addition(pospotentielle, pos)
        if coup_possible(plateau, pospion, posacheck, regle):
            mvtpossible.append(posacheck)
    return mvtpossible

def coup_possible(plateau, pospion, posacheck, regle):
    """Vérifie si un coup est possible selon les règles spécifiées.

    Args:
        plateau (list): Le plateau de jeu.
        pospion (tuple): La position du pion.
        posacheck (tuple): La position à vérifier.
        regle (str): La règle à appliquer.

    Returns:
        bool: True si le coup est possible, False sinon.
    """
    if (0 <= posacheck[1] < len(plateau) and 0 <= posacheck[0] < len(plateau[0])
                and plateau[posacheck[1]][posacheck[0]] != "H"):
        if regle == "souple":
            return True
        hauteur_case = fltk.hauteur_fenetre() / len(plateau)
        largeur_case = fltk.largeur_fenetre() / len(plateau[0])
        for y in range(len(plateau)):
            for x in range(len(plateau[y])):
                if plateau[y][x] == "H":
                    if intersection_cercle(pospion[0] * largeur_case, pospion[1] * hauteur_case,
                        posacheck[0] * largeur_case, posacheck[1] * hauteur_case,
                        x * largeur_case, y * hauteur_case, hauteur_case * 0.75):
                        return False
            return True
    return False


def distance_centre(x1, y1, x2, y2, xc, yc):
    """Cette fonction calcule la distance entre un point (xc, yc) et 
    un segment de droite défini par les points (x1, y1) et (x2, y2).
    Elle utilise la formule de la distance entre un point et un segment de droite.
    
    Args:
        x1 (float): Coordonnée x du premier point du segment de droite.
        y1 (float): Coordonnée y du premier point du segment de droite.
        x2 (float): Coordonnée x du deuxième point du segment de droite.
        y2 (float): Coordonnée y du deuxième point du segment de droite.
        xc (float): Coordonnée x du point pour lequel la distance doit être calculée.
        yc (float): Coordonnée y du point pour lequel la distance doit être calculée.
    
    Returns:
        float: La distance entre le point (xc, yc) et le segment de droite défini par 
        les points (x1, y1) et (x2, y2).
    """
    # Calculer la longueur au carré du segment de droite
    longueursegmentcarre = (x2 - x1) ** 2 + (y2 - y1) ** 2
    # Si la longueur du segment de droite est nulle, retourner la distance
    # entre le point et le premier point du segment
    if longueursegmentcarre == 0:
        return math.sqrt((xc - x1)**2 + (yc - y1)**2)
    # Calculer le paramètre t, qui représente la position du point le plus
    # proche sur le segment de droite par rapport au point (xc, yc)
    t = max(0, min(1, ((xc - x1) * (x2 - x1) + (yc - y1) * (y2 - y1)) / longueursegmentcarre))
    # Calculer les coordonnées du point le plus proche sur le segment de droite
    x_proche = x1 + t * (x2 - x1)
    y_proche = y1 + t * (y2 - y1)
    # Calculer la distance entre le point (xc, yc) et le point le plus proche
    # sur le segment de droite
    return math.sqrt((x_proche - xc) ** 2 + (y_proche - yc) ** 2)

def intersection_cercle(x1, y1, x2, y2, xc, yc, r):
    """Vérifie si un cercle d'un rayon donné intersecte un segment de droite.

    Args:
        x1 (float): Coordonnée x du premier point du segment.
        y1 (float): Coordonnée y du premier point du segment.
        x2 (float): Coordonnée x du deuxième point du segment.
        y2 (float): Coordonnée y du deuxième point du segment.
        xc (float): Coordonnée x du centre du cercle.
        yc (float): Coordonnée y du centre du cercle.
        r (float): Rayon du cercle.

    Returns:
        bool: True si le cercle intersecte le segment, False sinon.
    """
    distance = distance_centre(x1, y1, x2, y2, xc, yc)
    return distance <= r

def retour_arriere(posparcouru):
    """Retourne en arrière dans le parcours.

    Cette fonction prend en paramètre une liste représentant le parcours effectué jusqu'à présent.
    Elle supprime le dernier élément de la liste et retourne la liste modifiée.

    Args:
        posparcouru (list): La liste représentant le parcours effectué jusqu'à présent.

    Returns:
        list: La liste modifiée après avoir supprimé le dernier élément.
    """
    posparcouru.pop()
    return posparcouru
