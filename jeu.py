import sys
import fltk
import affichage
import grillage
import conversion
import mouvement
import sauvegarde
import menu


def main(carte, charge, regle):
    """Fonction principale du jeu.

    Cette fonction gère le déroulement du jeu en fonction des paramètres donnés.

    Args:
        map (str): Le chemin vers le fichier contenant la carte du jeu.
        charge (bool): Indique si une partie est chargée ou non.
        regle (str): Les règles du jeu.

    """
    if charge is False:
        solveur = False
        plateau = conversion.conversion_txt(carte)
        plateau_pion, posdepart = grillage.depart(plateau)
        pos_parcouru = [posdepart]
        pos_actuelle = grillage.posactuelle(pos_parcouru)
        mvtpossible = mouvement.calcul_posibilite(
        plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
    else:
        if len(carte) > 3:
            solveur = carte[3]
        else:
            solveur = False
        plateau = conversion.conversion_txt(carte[1])
        pos_parcouru = carte[0]
        regle = carte[2]
        pos_actuelle = grillage.posactuelle(pos_parcouru)
        plateau_pion = grillage.remiseenplace(pos_actuelle, plateau)
        mvtpossible = mouvement.calcul_posibilite(
            plateau, pos_actuelle, pos_parcouru, regle)
        affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)

    while not fin_de_partie(pos_parcouru, plateau, mvtpossible, solveur):
        event = fltk.attend_ev()
        tev = fltk.type_ev(event)
        if tev == "ClicGauche":
            gerer_evenement(event, plateau_pion,
                                   mvtpossible, pos_parcouru)
            pos_actuelle = grillage.posactuelle(pos_parcouru)
            mvtpossible = mouvement.calcul_posibilite(
                plateau, pos_actuelle, pos_parcouru, regle)
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Touche":
            nom_touche = fltk.touche(event)
            if nom_touche == "BackSpace":
                pos_parcouru = mouvement.retour_arriere(pos_parcouru)
                pos_actuelle = grillage.posactuelle(pos_parcouru)
                mvtpossible = mouvement.calcul_posibilite(
                    plateau, pos_actuelle, pos_parcouru, regle)
                affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
            if nom_touche == "s":
                num = menu.choixsauvegarde(False)
                sauvegarde.sauvegarde_partie(pos_parcouru, carte, num, regle)
            if nom_touche == "Escape":
                break
        if tev == "Redimension":
            affichage.affiche_tout(plateau, mvtpossible, pos_parcouru)
        if tev == "Quitte":
            sys.exit()
    if victoire(pos_parcouru, plateau):
        affichage.affichevictoire()
    elif defaite(mvtpossible):
        affichage.affichedefaite()

def gerer_evenement(ev,plateau_pion, mvtpossible, pos_parcouru):
    """
    Gère un événement de clic sur le plateau de jeu.

    Args:
        ev (fltk.Event): L'événement de clic.
        plateau_pion (list): Le plateau de jeu contenant les pions.
        mvtpossible (list): Les mouvements possibles.
        pos_parcouru (list): Les positions parcourues.

    Returns:
        None
    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau_pion)
    largeur_case = fltk.largeur_fenetre() / len(plateau_pion[0])
    xclick, yclick = fltk.abscisse(ev), fltk.ordonnee(ev)
    xcaseclick = int((xclick+largeur_case//2) // largeur_case)
    ycaseclick = int((yclick+hauteur_case//2) // hauteur_case)
    if [xcaseclick, ycaseclick] in mvtpossible:
        if len(pos_parcouru) > 1:
            poseactuelle = grillage.posactuelle(pos_parcouru)
            plateau_pion[poseactuelle[1]][poseactuelle[0]] = 0
            plateau_pion[ycaseclick][xcaseclick] = 1
        pos_parcouru.append([xcaseclick, ycaseclick])

def fin_de_partie(posparcouru, plateau, mvtpossible, solveur):
    """Vérifie si la partie est terminée.

    Cette fonction vérifie si la partie est terminée en fonction des paramètres donnés.
    Si le solveur est désactivé, la partie est terminée si le joueur a gagné ou 
    s'il n'a plus de mouvements possibles.
    Si le solveur est activé, la partie n'est jamais terminée.

    Args:
        posparcouru (list): La liste des positions parcourues par le joueur.
        plateau (list): Le plateau de jeu.
        mvtpossible (bool): Indique si le joueur a encore des mouvements possibles.
        solveur (bool): Indique si le solveur est activé.

    Returns:
        bool: True si la partie est terminée, False sinon.
    """
    if not solveur:
        return (victoire(posparcouru, plateau) or defaite(mvtpossible))
    else:
        return False

def victoire(posparcouru, plateau):
    """Vérifie si la position actuelle du joueur correspond à une victoire.

    Args:
        posparcouru (tuple): Les coordonnées de la position actuelle du joueur.
        plateau (list): Le plateau de jeu.

    Returns:
        bool: True si la position actuelle du joueur correspond à une victoire, False sinon.
    """
    pos = grillage.posactuelle(posparcouru)
    if plateau[pos[1]][pos[0]] == 'A':
        return True
    return False

def defaite(mvtpossible):
    """Vérifie si la partie est perdue.

    Args:
        mvtpossible (list): La liste des mouvements possibles.

    Returns:
        bool: True si la partie est perdue, False sinon.
    """
    if len(mvtpossible) < 1:
        return True
    return False

def veriftouche(ev, nom_sauvegarde):
    """
    Vérifie la touche entrée par l'utilisateur et effectue les actions correspondantes.

    Args:
        ev (str): L'événement de la touche entrée par l'utilisateur.
        nom_sauvegarde (str): Le nom de sauvegarde actuel.

    Returns:
        tuple: Un tuple contenant la touche entrée par l'utilisateur et le nom 
        de sauvegarde mis à jour.
    """
    if isinstance(ev, str) and ev == "Quitte":
        sys.exit()
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
