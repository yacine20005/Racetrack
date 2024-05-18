import fltk
import moteur
import affichage
import sys


def main(map, charge, regle):
    if charge is False:
        plateau = moteur.conversion_txt(map)
        plateau_pion, posdepart = moteur.depart(plateau)
        pos_parcouru = [posdepart]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        mvtpossible = moteur.calcul_posibilite(
        plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    else:
        if len(map) > 3:
            solveur = map[3]
        else:
            solveur = False
        plateau = moteur.conversion_txt(map[1])
        pos_parcouru = map[0]
        regle = map[2]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        plateau_pion = moteur.remiseenplace(pos_actuelle, plateau)
        mvtpossible = moteur.calcul_posibilite(
            plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

    while moteur.fin_de_partie(pos_parcouru, plateau, mvtpossible, solveur): # True si solveur, False sinon ! 
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            moteur.gerer_evenement(event, plateau_pion,
                                   mvtpossible, pos_parcouru)
            pos_actuelle = moteur.posactuelle(pos_parcouru)
            mvtpossible = moteur.calcul_posibilite(
                plateau, pos_actuelle, pos_parcouru, regle)
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Touche":
            nom_touche = fltk.touche(event)
            if nom_touche == "BackSpace":
                pos_parcouru = moteur.retour_arriere(pos_parcouru)
                pos_actuelle = moteur.posactuelle(pos_parcouru)
                mvtpossible = moteur.calcul_posibilite(
                    plateau, pos_actuelle, pos_parcouru, regle)
                affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
            if nom_touche == "s":
                num = affichage.choixsauvegarde(False)
                moteur.sauvegarde_partie(pos_parcouru, map, num, regle)
            if nom_touche == "Escape":
                break
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    if moteur.victoire(pos_parcouru, plateau):
        affichage.affichevictoire()
    elif moteur.defaite(mvtpossible):
        affichage.affichedefaite()
