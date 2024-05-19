import fltk

def initialiseboutonsmenu(phase, carte, choix, regle, solveur, affichage):
        """Initialise les boutons du menu ainsi que leurs fonctions associées.

        Args:
            phase (_type_): _description_
            carte (_type_): _description_
            choix (_type_): _description_
            regle (_type_): _description_
            solveur (_type_): _description_
            affichage (_type_): _description_

        Returns:
            _type_: _description_
        """
        milieu_fenetre_x = fltk.largeur_fenetre()//2
        milieu_fenetre_y = fltk.hauteur_fenetre()//2
        liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Solveur"],
                        [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Jouer"],
                        [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), "Quitter"]]
        if phase == "Jouer":
                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Charger"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Nouvelle Partie"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), "Retour"]]
        elif phase == "Choix":
                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Options"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Lancer"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), " Retour "]]
        elif phase == "Solveur":
                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), "Retour"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "  Options  "],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Résoudre"]]
        elif phase == "  Options  ":
                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), "      Retour      "],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x - fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Choix de la map"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x - fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//8, carte[0]],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x - fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Règle"],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x - fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y - int(1.5*(fltk.hauteur_fenetre()//12)), regle[0]],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Affichage"],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - int(1.5*(fltk.hauteur_fenetre()//12)), affichage[0]],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Choix du solveur"],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y + fltk.largeur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//12,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//8, solveur[0]]]
        elif phase == "Charger":

                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), " Charger "],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Choix de la sauvegarde"],

                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), " Retour "]]
        elif phase == "Options":
                liste_boutons = [[milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), "Règle"],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - 4*(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y - 2 * (fltk.hauteur_fenetre()//12), regle[0]],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, "Choix de la map"],
                                [milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y - fltk.hauteur_fenetre()//12,
                                        milieu_fenetre_x + fltk.largeur_fenetre()//3,
                                        milieu_fenetre_y + fltk.hauteur_fenetre()//12, carte[0]],
                                [milieu_fenetre_x - fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 2 *(fltk.hauteur_fenetre()//12),
                                        milieu_fenetre_x + fltk.largeur_fenetre()//6,
                                        milieu_fenetre_y + 4 *(fltk.hauteur_fenetre()//12), "  Retour  "]]
        return liste_boutons
