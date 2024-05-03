import fltk

def initialiseboutonsmenu(phase, map, Choix, regle):
        MillieufenetreX = fltk.largeur_fenetre()//2
        MillieufenetreY = fltk.hauteur_fenetre()//2
        liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                MillieufenetreY - fltk.hauteur_fenetre()//12,
                                MillieufenetreX + fltk.largeur_fenetre()//6, 
                                MillieufenetreY + fltk.hauteur_fenetre()//12, "Regles"], 
                        [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                MillieufenetreX + fltk.largeur_fenetre()//6, 
                                MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), "Jouer"],
                        [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                MillieufenetreX + fltk.largeur_fenetre()//6, 
                                MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "Quitter"]]
        if phase == "Jouer":
                liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - fltk.hauteur_fenetre()//12,
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + fltk.hauteur_fenetre()//12, "Charger"], 
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), "Nouvelle Partie"],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "Retour"]]
        elif phase == "Choix":
                liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - fltk.hauteur_fenetre()//12,
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + fltk.hauteur_fenetre()//12, "Options"],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), "‎Jouer‎"],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "‎Retour‎"]]
        elif phase == "Regles":
                liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "Retour"]]
        elif phase == "Charger":

                liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), "‎Charger‎"],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - fltk.hauteur_fenetre()//12,
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + fltk.hauteur_fenetre()//12, "Choix de la sauvegarde"],

                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "‎Retour‎"]]
        elif phase == "Options":
                print("boutons")
                liste_boutons = [[MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), "Règle"],
                                [MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - 4*(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//3, 
                                        MillieufenetreY - 2 * (fltk.hauteur_fenetre()//12), regle[0]],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - fltk.hauteur_fenetre()//12,
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + fltk.hauteur_fenetre()//12, "Choix de la map"],
                                [MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY - fltk.hauteur_fenetre()//12,
                                        MillieufenetreX + fltk.largeur_fenetre()//3, 
                                        MillieufenetreY + fltk.hauteur_fenetre()//12, map[0]],
                                [MillieufenetreX - fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 2 *(fltk.hauteur_fenetre()//12),
                                        MillieufenetreX + fltk.largeur_fenetre()//6, 
                                        MillieufenetreY + 4 *(fltk.hauteur_fenetre()//12), "‎‎Retour‎‎"]]
        return liste_boutons

