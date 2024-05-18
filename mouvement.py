import fltk
import math
import grillage

def calcul_posibilite(plateau, pospion, posparcouru, regle):
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

    longueursegmentcarre = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if longueursegmentcarre == 0:
        return math.sqrt((xc - x1)**2 + (yc - y1)**2)

    
    t = max(0, min(1, ((xc - x1) * (x2 - x1) + (yc - y1) * (y2 - y1)) / longueursegmentcarre))

    x_proche = x1 + t * (x2 - x1)
    y_proche = y1 + t * (y2 - y1)
    
    return math.sqrt((x_proche - xc) ** 2 + (y_proche - yc) ** 2)

def intersection_cercle(x1, y1, x2, y2, xc, yc, r):
    distance = distance_centre(x1, y1, x2, y2, xc, yc)
    return distance <= r

def retour_arriere(posparcouru):
    posparcouru.pop()
    return posparcouru