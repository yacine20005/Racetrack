import fltk
import affichage
import sys
import grillage
import conversion
import mouvement
import jeu
import sauvegarde


def main(map, charge, regle):
    if charge is False:
        solveur = False
        plateau = conversion.conversion_txt(map)
        plateau_pion, posdepart = grillage.depart(plateau)
        pos_parcouru = [posdepart]
        pos_actuelle = grillage.posactuelle(pos_parcouru)
        mvtpossible = mouvement.calcul_posibilite(
        plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    else:
        if len(map) > 3:
            solveur = map[3]
        else:
            solveur = False
        plateau = conversion.conversion_txt(map[1])
        pos_parcouru = map[0]
        regle = map[2]
        pos_actuelle = grillage.posactuelle(pos_parcouru)
        plateau_pion = grillage.remiseenplace(pos_actuelle, plateau)
        mvtpossible = mouvement.calcul_posibilite(
            plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

    while not jeu.fin_de_partie(pos_parcouru, plateau, mvtpossible, solveur):
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            jeu.gerer_evenement(event, plateau_pion,
                                   mvtpossible, pos_parcouru)
            pos_actuelle = grillage.posactuelle(pos_parcouru)
            mvtpossible = mouvement.calcul_posibilite(
                plateau, pos_actuelle, pos_parcouru, regle)
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Touche":
            nom_touche = fltk.touche(event)
            if nom_touche == "BackSpace":
                pos_parcouru = jeu.retour_arriere(pos_parcouru)
                pos_actuelle = grillage.posactuelle(pos_parcouru)
                mvtpossible = mouvement.calcul_posibilite(
                    plateau, pos_actuelle, pos_parcouru, regle)
                affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
            if nom_touche == "s":
                num = affichage.choixsauvegarde(False)
                sauvegarde.sauvegarde_partie(pos_parcouru, map, num, regle)
            if nom_touche == "Escape":
                break
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    if jeu.victoire(pos_parcouru, plateau):
        affichage.affichevictoire()
    elif jeu.defaite(mvtpossible):
        affichage.affichedefaite()
        
def gerer_evenement(ev,plateau_pion, mvtpossible, pos_parcouru):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau_pion) 
    largeur_case = fltk.largeur_fenetre() / len(plateau_pion[0])
    Xclick, Yclick = fltk.abscisse(ev), fltk.ordonnee(ev)
    Xcaseclick = int((Xclick+largeur_case//2) // largeur_case)
    Ycaseclick = int((Yclick+hauteur_case//2) // hauteur_case)
    if [Xcaseclick, Ycaseclick] in mvtpossible:
        if len(pos_parcouru) > 1:
            poseactuelle = grillage.posactuelle(pos_parcouru)
            plateau_pion[poseactuelle[1]][poseactuelle[0]] = 0
            plateau_pion[Ycaseclick][Xcaseclick] = 1
        pos_parcouru.append([Xcaseclick, Ycaseclick])
        
def fin_de_partie(posparcouru, plateau, mvtpossible, solveur):
    if not solveur:
        return (victoire(posparcouru, plateau) or defaite(mvtpossible))
    else:
        return False

def victoire(posparcouru, plateau):
    pos = grillage.posactuelle(posparcouru)
    if plateau[pos[1]][pos[0]] == 'A':
        return True
    return False

def defaite(mvtpossible):
    if len(mvtpossible) < 1:
        return True
    return False

def veriftouche(ev, nom_sauvegarde):
    if type(ev) == "Quitte":
            sys.exit
    else:
        nom_touche = fltk.touche(ev)
        if nom_touche == "Return":
            return nom_touche, nom_sauvegarde
        if nom_touche == "BackSpace":
            nom_sauvegarde = nom_sauvegarde[:-1]
            return nom_touche, nom_sauvegarde
        if len(nom_touche) <= 1:
            return nom_touche, nom_sauvegarde + nom_touche
        else:
            return "", nom_sauvegarde