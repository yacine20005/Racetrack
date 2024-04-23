import fltk
import sys

def affichage_plateau(plateau):
    hauteur_case = fltk.hauteur_fenetre() // len(plateau) 
    largeur_case = fltk.largeur_fenetre() // len(plateau[0])
    print(fltk.hauteur_fenetre())
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coordcaseX = x * largeur_case
            coordcaseY = y * hauteur_case
            if plateau[y][x]=='H':
                fltk.cercle(coordcaseX, coordcaseY,
                    60 ,"green", "green")
            if plateau[y][x]=='A':
                fltk.cercle(coordcaseX, coordcaseY,
                    50 ,"gray", "gray")
            #elif plateau[y][x]=='R':
                #fltk.rectangle(coordcaseX, coordcaseY,
                    #coordcaseX + largeur_case,
                    #coordcaseY + hauteur_case, "white", "white")
    fltk.mise_a_jour

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
plateau = [['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
            ['H', 'A', 'R', 'R', 'R', 'R', 'R', 'H', 'H', 'R'],
            ['H', 'A', 'R', 'R', 'R', 'R', 'R', 'H', 'R', 'R'],
            ['H', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'H', 'H', 'H', 'H', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'H', 'H', 'H', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'H', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'D', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'D', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['H', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
            ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']]

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
