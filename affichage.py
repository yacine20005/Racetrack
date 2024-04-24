import fltk
import sys
import cropta

def affichage_voiture(plateau, pos_actuelle):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    coordcaseX = pos_actuelle[0] * largeur_case
    coordcaseY = pos_actuelle[1] * hauteur_case
    fltk.cercle(coordcaseX, coordcaseY,
        hauteur_case * 0.5 ,"orange", "orange")


def affichage_plateau(plateau):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coordcaseX = x * largeur_case
            coordcaseY = y * hauteur_case
            if plateau[y][x]=='H':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.75 ,"green", "green") #anciennement 1,2
            elif plateau[y][x]=='A':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.71 ,"red", "red")
            elif plateau[y][x]=='D':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.71 ,"gray", "gray")
                
def affichage_trait(plateau):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coordcaseX = x * largeur_case
            coordcaseY = y * hauteur_case
            fltk.ligne(coordcaseX,coordcaseY,
                coordcaseX + largeur_case, 
                coordcaseY,"Black")
            fltk.ligne(coordcaseX,coordcaseY,
                coordcaseX, 
                coordcaseY + hauteur_case,"Black")
                

def affiche_possibilite(plateau, mvtpossible):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for pos in mvtpossible:
        x, y = pos[0], pos[1]
        coordcaseX = x * largeur_case
        coordcaseY = y * hauteur_case
        fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.25 ,"black", "black")

def affiche_trace(posparcouru, plateau):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for i in range(len(posparcouru)-1):
        x, y = posparcouru[i][0] * largeur_case, posparcouru[i][1] * hauteur_case
        x2, y2 = posparcouru[i+1][0] * largeur_case, posparcouru[i+1][1] * hauteur_case
        fltk.ligne(x, y, x2, y2, "pink", 5)

def affiche_tout(plateau, plateaupion, mvtpossible, pos_actuelle, posparcouru):
    fltk.efface_tout()
    affichage_plateau(plateau)
    affichage_trait(plateau)
    affichage_voiture(plateaupion, pos_actuelle)
    affiche_possibilite(plateau, mvtpossible)
    affiche_trace(posparcouru, plateau)

fltk.cree_fenetre(800,800, redimension=True)
plateau = cropta.conversion_txt("map2.txt")
plateau_pion = cropta.miseenplacepion(plateau)
pos_actuelle, mvtpossible = cropta.calcul_posibilite(plateau, plateau_pion)
pos_parcouru = [pos_actuelle]
affiche_tout(plateau, plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)

while True:
    event = fltk.attend_ev()
    tev = fltk.type_ev(event)
    if tev == "ClicGauche":
        pos_actuelle, mvtpossible = cropta.calcul_posibilite(plateau, plateau_pion)
        cropta.gerer_evenement(event,plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)
        affiche_tout(plateau, plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)
        print(pos_parcouru)
    if tev == "Redimension":
        affiche_tout(plateau, plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)
    if tev == "Quitte":
        sys.exit()
