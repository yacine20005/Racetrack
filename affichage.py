import fltk
import moteur

def affiche_boutons(liste_boutons, taille_texte):
    """S'occupe d'afficher les boutons dans la fenetre fltk

    Args:
        liste_boutons (_list_): liste de liste contenant la liste
        de tous les boutons utilisés dans le jeu

        taille_boutons (_int_): Variable correspondant a la taille
        du coté des boutons en fonction de la taille de la fenetre fltk.

        epaisseur_bouton (_int_): Variable correspondant a l'épaisseur
        du coté des boutons en fonction de la taille de la fenetre fltk.
    """
    fltk.efface_tout()
    fltk.image(0,0, "fond_menu.png", fltk.largeur_fenetre(), fltk.hauteur_fenetre(),"nw",)
    for boutons in liste_boutons:
        aX, aY = boutons[0], boutons[1]
        bX, bY = boutons[2], boutons[3]
        texte = boutons[4]
        fltk.rectangle(aX, aY, bX, bY,
                        "dark grey", "white")
        fltk.texte((aX + bX) // 2, (aY + bY) // 2,
                   texte, ancrage="center", taille=taille_texte)
        
def affichage_fond_ecran():
    pass


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
                    hauteur_case * 0.75 ,"green", "green")
            elif plateau[y][x]=='A':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.75 ,"red", "red")
            elif plateau[y][x]=='D':
                fltk.cercle(coordcaseX, coordcaseY,
                    hauteur_case * 0.75 ,"gray", "gray")
                
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
    couleurs = {0: "light gray", 1: "#00BCD4", 2: "#1976D2", 3: "#0D47A1", 4: "#4CAF50",5: 
    "#8BC34A",6: "#FFEB3B",7: "#FF9800", 8: "#FF5722",9: "#F44336", 10: "#B71C1C"} 
    for i in range(len(posparcouru)-1):
        x, y = posparcouru[i][0] * largeur_case, posparcouru[i][1] * hauteur_case
        x2, y2 = posparcouru[i+1][0] * largeur_case, posparcouru[i+1][1] * hauteur_case
        variable = max(moteur.list_add2([posparcouru[i+1][0],posparcouru[i+1][1]],[posparcouru[i][0],posparcouru[i][1]]))
        if variable < 0:
            variable = -(variable)
        couleur = couleurs[variable]
        fltk.ligne(x, y, x2, y2, couleur, 3)

def affiche_tout(plateau, mvtpossible, posparcouru):
    pos_actuelle = moteur.posactuelle(posparcouru)
    fltk.efface_tout()
    affichage_plateau(plateau)
    affichage_trait(plateau)
    affiche_possibilite(plateau, mvtpossible)
    affichage_voiture(plateau, pos_actuelle)
    affiche_trace(posparcouru, plateau)

