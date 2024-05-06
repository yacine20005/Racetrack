import fltk
import moteur
import affichage
import sys


def main(map, charge, regle):
    if charge is False:
        plateau = moteur.conversion_txt(map)
        plateau_pion, posdepart = moteur.miseenplacepion(plateau)
        pos_parcouru = [posdepart]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        mvtpossible = moteur.calcul_posibilite(
            plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    else:
        plateau = moteur.conversion_txt(map[1])
        pos_parcouru = map[0]
        regle = map[2]
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        plateau_pion = moteur.remiseenplace(pos_actuelle, plateau)
        mvtpossible = moteur.calcul_posibilite(
            plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

    #while moteur.victoire(pos_parcouru, plateau) is False and moteur.defaite(mvtpossible) is False:
    while moteur.defaite(mvtpossible) is False:

        # neuille
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            moteur.gerer_evenement(event, plateau_pion,
                                   mvtpossible, pos_actuelle, pos_parcouru)
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
            if nom_touche == "Echap":
                break
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    if moteur.victoire(pos_parcouru, plateau) is True:
        print("Victoire")
    if moteur.defaite(mvtpossible) is True:
        print("Perdu")
