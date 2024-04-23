import fltk
import sys
import cropta

def affichage_plateau(plateau):
    hauteur_case = fltk.hauteur_fenetre() // len(plateau) 
    largeur_case = fltk.largeur_fenetre() // len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coordcaseX = x * largeur_case
            coordcaseY = y * hauteur_case
            if plateau[y][x]=='H':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.75 ,"green", "green")
            if plateau[y][x]=='D':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.7 ,"red", "red")
            if plateau[y][x]=='A':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.625 ,"gray", "gray")
    fltk.mise_a_jour()

def affichage(plateau):
    hauteur_case = fltk.hauteur_fenetre() // len(plateau) 
    largeur_case = fltk.largeur_fenetre() // len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coordcaseX = x * largeur_case
            coordcaseY = y * hauteur_case
            fltk.ligne(coordcaseX,coordcaseY,
                coordcaseX + largeur_case, 
                coordcaseY,"Black")
            fltk.ligne(coordcaseX,coordcaseY,
                coordcaseX , 
                coordcaseY + hauteur_case,"Black")

fltk.cree_fenetre(800,800, redimension=True)
plateau = cropta.conversion("map1.txt")

while True:
    event = fltk.attend_ev()
    tev = fltk.type_ev(event)
    if tev == "ClicGauche":
        affichage_plateau(plateau)
        affichage(plateau)
    if tev == "Redimension":
        pass
    if tev == "Quitte":
        sys.exit()
