import fltk
import moteur
import affichage
import sys

fltk.cree_fenetre(800,800, redimension=True)
plateau = moteur.conversion_txt("map_mini.txt")
plateau_pion, posdepart = moteur.miseenplacepion(plateau)
pos_parcouru = [posdepart]
pos_actuelle = moteur.posactuelle(pos_parcouru)
mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

while moteur.victoire(pos_parcouru, plateau) is False and moteur.defaite(mvtpossible) is False:
    print(mvtpossible)
    event = fltk.attend_ev()
    tev = fltk.type_ev(event)
    if tev == "ClicGauche":
        moteur.gerer_evenement(event,plateau_pion, mvtpossible, pos_actuelle, pos_parcouru)
        pos_actuelle = moteur.posactuelle(pos_parcouru)
        mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    if tev == "Touche":
        nom_touche = fltk.touche(event)
        if nom_touche == "Left":
            pos_parcouru = moteur.retour_arriere(pos_parcouru)
            pos_actuelle = moteur.posactuelle(pos_parcouru)
            mvtpossible = moteur.calcul_posibilite(plateau, pos_actuelle, pos_parcouru)
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    if tev == "Redimension":
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    if tev == "Quitte":
        sys.exit()