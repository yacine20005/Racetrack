import affichage
import fltk
import jeu
import sys

def creer_grille(x, y):
    grille = []
    for _ in range(y):
        ligne = []
        for _ in range(x):
            ligne.append(0)
        grille.append(ligne)
    return grille

def afficher_grille(grille):
    for ligne in grille:
        print(ligne)
        
def posdepart(plateau):
    zonedepart = []
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            if plateau[y][x]=="D":
                zonedepart.append([x,y])
    return zonedepart

def miseenplacepion(plateau):
        len_y = len(plateau)
        len_x = len(plateau[0])
        listeposX = []
        listeposY = []
        posfinalX, posfinalY = 0,0
        grille = creer_grille(len_x, len_y)
        for y in range(len(plateau)):
            for x in range(len(plateau[0])):
                if plateau[y][x] == "D":
                    listeposX.append(x)
                    listeposY.append(y)
        posfinalX = (max(listeposX) + min(listeposX)) // 2
        posfinalY = (max(listeposY) + min(listeposY)) // 2
        grille[posfinalY][posfinalX] = 1
        posdepart = [posfinalX,posfinalY]
        return grille, posdepart

def depart(plateau):
    mvtpossible = posdepart(plateau)
    affichage.affiche_depart(plateau, mvtpossible)
    pos_parcouru = []
    plateau_pion = creer_grille(len(plateau), len(plateau[1]))
    while pos_parcouru == []:
        ev = fltk.attend_ev()
        tev = fltk.type_ev(ev)
        if tev == "ClicGauche":
            jeu.gerer_evenement(ev, plateau_pion,
                                   mvtpossible, pos_parcouru)
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    return plateau_pion, pos_parcouru[-1]


def remiseenplace(pos_actuelle, plateau):
    len_y = len(plateau)
    len_x = len(plateau[0])
    grille = creer_grille(len_y, len_x)
    grille[pos_actuelle[1]][pos_actuelle[0]] = 1
    return grille

def posactuelle(pos_parcouru):
    return pos_parcouru[-1]

def trouver_arrivee(plateau):
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            if plateau[y][x]=="A":
                return [x,y]
            
def list_addition(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def list_soustraction(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result
