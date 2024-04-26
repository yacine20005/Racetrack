import fltk
import moteur
import affichage
import sys

def main(map, charge):
    if charge is False:
        plateau = moteur.conversion_txt(map)
        plateau_pion, posdepart = moteur.miseenplacepion(plateau)
        pos_parcouru = [posdepart]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    else:
        plateau = moteur.conversion_txt(map[1])
        pos_parcouru = map[0]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        plateau_pion = moteur.remiseenplace(pos_actuelle, plateau)
        mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

    while moteur.victoire(pos_parcouru, plateau) is False and moteur.defaite(mvtpossible) is False:
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            moteur.gerer_evenement(event,plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)
            pos_actuelle = moteur.posactuelle(pos_parcouru)
            mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Touche":
            nom_touche = fltk.touche(event)
            if nom_touche == "BackSpace":
                pos_parcouru = moteur.retour_arriere(pos_parcouru)
                pos_actuelle = moteur.posactuelle(pos_parcouru)
                mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
                affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
            if nom_touche == "S":
                pass
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
