import time
import fltk
import grillage

def affiche_fenetre_sauvegarde(nom_sauvegarde, relance):
    """Affiche une fenêtre de sauvegarde avec des éléments graphiques.

    Cette fonction affiche une fenêtre de sauvegarde avec des éléments graphiques.
    Elle prend en paramètre le nom de la sauvegarde et un booléen indiquant si la fonction doit être relancée.

    Args:
        nom_sauvegarde (str): Le nom de la sauvegarde.
        Relance (bool): Indique si la fonction doit être relancée.

    """
    milieu_fenetre_x = fltk.largeur_fenetre() //2
    milieu_fenetre_y = fltk.hauteur_fenetre() //2
    taille_fenetre_x = fltk.largeur_fenetre() //2
    taille_fenetre_y = fltk.hauteur_fenetre() //3
    fltk.rectangle(milieu_fenetre_x - taille_fenetre_x //2,
                                     milieu_fenetre_y - taille_fenetre_y//2,
                                     milieu_fenetre_x + taille_fenetre_x //2,
                                     milieu_fenetre_y + taille_fenetre_y//2, "Black", "#f3f6f4", tag = "sauvegarde")
    fltk.rectangle(milieu_fenetre_x - taille_fenetre_x //2,
                                     milieu_fenetre_y - taille_fenetre_y//2,
                                     milieu_fenetre_x + taille_fenetre_x //2,
                                     milieu_fenetre_y - taille_fenetre_y // 3, "Black", "White", tag = "sauvegarde")
    fltk.texte(milieu_fenetre_x,
                                milieu_fenetre_y - ((taille_fenetre_y // 2 + taille_fenetre_y // 3)//2),
                                    "Choix de la Sauvegarde", "Black", "center", taille = 18, tag = "sauvegarde")
    fltk.texte(milieu_fenetre_x,
                                milieu_fenetre_y - taille_fenetre_y//4,
                                    "Entrez le nom du fichier que vous souhaitez charger", 
                                    "Black", "center", taille = 13, tag = "sauvegarde")
    fltk.texte(milieu_fenetre_x, milieu_fenetre_y - taille_fenetre_y // 10,
                                " ou dans lequel vous souhaitez sauvegarder", 
                                "Black", "center", taille = 13, tag = "sauvegarde")
    fltk.rectangle(milieu_fenetre_x - taille_fenetre_x //2 + 20,
                                     milieu_fenetre_y,
                                     milieu_fenetre_x + taille_fenetre_x //2 -20,
                                     milieu_fenetre_y + taille_fenetre_y // 4, "Black", "White", tag = "sauvegarde")
    fltk.texte(milieu_fenetre_x, milieu_fenetre_y + taille_fenetre_y // 8,
                                nom_sauvegarde,
                                "Black", "center", taille = 13, tag = "sauvegarde")
    if relance is True:
        fltk.texte(milieu_fenetre_x, milieu_fenetre_y + taille_fenetre_y // 3,
                                "Le fichier que vous souhaitez charger n'existe pas", 
                                "Red", "center", taille = 13, tag = "sauvegarde")

def affiche_boutons(liste_boutons, taille_texte):
    """Affiche une liste de boutons avec du texte.

    Cette fonction affiche une liste de boutons à l'écran, en utilisant les coordonnées
    spécifiées dans la liste_boutons. Chaque bouton est représenté par un rectangle
    avec du texte à l'intérieur.

    Args:
        liste_boutons (list): Une liste contenant les coordonnées et le texte de chaque bouton.
            Chaque élément de la liste doit être une liste de la forme [aX, aY, bX, bY, texte],
            où aX et aY sont les coordonnées du coin supérieur gauche du rectangle,
            bX et bY sont les coordonnées du coin inférieur droit du rectangle,
            et texte est le texte à afficher à l'intérieur du rectangle.
        taille_texte (int): La taille du texte à afficher.

    Returns:
        None
    """
    fltk.efface_tout()
    fltk.image(0,0, "images/fond_menu.png", fltk.largeur_fenetre(), fltk.hauteur_fenetre(),"nw",)
    for boutons in liste_boutons:
        a_x, a_y = boutons[0], boutons[1]
        b_x, b_y = boutons[2], boutons[3]
        texte = boutons[4]
        fltk.rectangle(a_x, a_y, b_x, b_y,
                        "dark grey", "white")
        fltk.texte((a_x + b_x) // 2, (a_y + b_y) // 2,
                   texte, ancrage="center", taille=taille_texte)

def affichage_fond_ecran():
    """_summary_
    """
    pass

def affichage_voiture(plateau, pos_actuelle):
    """Affiche la "voiture" sur le plateau de jeu.

    Args:
        plateau (list): Le plateau de jeu représenté par une liste de listes.
        pos_actuelle (tuple): La position actuelle de la voiture sur le plateau.

    Returns:
        None
    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau)
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    coord_case_x = pos_actuelle[0] * largeur_case
    coord_case_y = pos_actuelle[1] * hauteur_case
    fltk.cercle(coord_case_x, coord_case_y,
        hauteur_case * 0.5 ,"orange", "orange")

def affichage_plateau(plateau):
    """Affiche le plateau de jeu.

    Args:
        plateau (list): Le plateau de jeu représenté par une liste de listes.

    Returns:
        None
    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau)
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coord_case_x = x * largeur_case
            coord_case_y = y * hauteur_case
            if plateau[y][x]=='H':
                fltk.cercle(coord_case_x, coord_case_y,
                    hauteur_case * 0.75 ,"green", "green")
            elif plateau[y][x]=='A':
                fltk.cercle(coord_case_x, coord_case_y,
                    hauteur_case * 0.75 ,"red", "red")
            elif plateau[y][x]=='D':
                fltk.cercle(coord_case_x, coord_case_y,
                    hauteur_case * 0.75 ,"gray", "gray")

def affichage_trait(plateau):
    """
    Affiche les traits du plateau de jeu.

    Args:
        plateau (list): Le plateau de jeu représenté par une liste de listes.

    Returns:
        None
    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau)
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for y in range(len(plateau)):
        for x in range(len(plateau[y])):
            coord_case_x = x * largeur_case
            coord_case_y = y * hauteur_case
            fltk.ligne(coord_case_x,coord_case_y,
                coord_case_x + largeur_case,
                coord_case_y,"Black")
            fltk.ligne(coord_case_x,coord_case_y,
                coord_case_x,
                coord_case_y + hauteur_case,"Black")

def affiche_possibilite(plateau, mvtpossible):
    """Affiche les possibilités de déplacement sur le plateau.

    Args:
        plateau (list): Le plateau de jeu.
        mvtpossible (list): La liste des positions de déplacement possibles.

    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau)
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    for pos in mvtpossible:
        x, y = pos[0], pos[1]
        coord_case_x = x * largeur_case
        coord_case_y = y * hauteur_case
        fltk.cercle(coord_case_x, coord_case_y,
                    hauteur_case * 0.25 ,"black", "black")

def affiche_trace(posparcouru, plateau):
    """Affiche la trace du parcours sur le plateau.

    Args:
        posparcouru (list): Liste des positions parcourues.
        plateau (list): Plateau de jeu.

    """
    hauteur_case = fltk.hauteur_fenetre() / len(plateau)
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    couleurs = {0: "#000000", 1: "#330a00", 2: "#661400", 3: "#991f00", 4: "#cc2900",5:
    "#ff3300",6: "#ff5c33",7: "#ff8566", 8: "#ffad99",9: "#ffd6cc", 10: "#ffffff"}
    for i in range(len(posparcouru)-1):
        x, y = posparcouru[i][0] * largeur_case, posparcouru[i][1] * hauteur_case
        x2, y2 = posparcouru[i+1][0] * largeur_case, posparcouru[i+1][1] * hauteur_case
        variable = max(grillage.list_soustraction([posparcouru[i+1][0],posparcouru[i+1][1]],[posparcouru[i][0],posparcouru[i][1]]))
        if variable < 0:
            variable = -(variable)
        couleur = couleurs[variable]
        fltk.ligne(x, y, x2, y2, couleur, 3)

def affiche_tout(plateau, mvtpossible, posparcouru):
    """Affiche tous les éléments du jeu sur l'interface graphique.

    Args:
        plateau (list): Le plateau de jeu.
        mvtpossible (list): Les mouvements possibles.
        posparcouru (list): Les positions parcourues.
    """
    pos_actuelle = grillage.posactuelle(posparcouru)
    fltk.efface_tout()
    affichage_plateau(plateau)
    affichage_trait(plateau)
    affiche_possibilite(plateau, mvtpossible)
    affichage_voiture(plateau, pos_actuelle)
    affiche_trace(posparcouru, plateau)
    fltk.mise_a_jour()

def affiche_depart(plateau, mvtpossible):
    """Affiche le départ du jeu.

    Cette fonction efface tout le contenu de la fenêtre graphique, puis affiche le plateau de jeu,
    les traits de séparation, et les mouvements possibles.

    Args:
        plateau (list): Le plateau de jeu.
        mvtpossible (list): Les mouvements possibles.

    Returns:
        None
    """
    fltk.efface_tout()
    affichage_plateau(plateau)
    affichage_trait(plateau)
    affiche_possibilite(plateau, mvtpossible)
    fltk.mise_a_jour()

def affichevictoire():
    """Affiche l'écran de victoire.

    Cette fonction affiche un écran de victoire avec une image et un texte.
    La fonction attend 2 secondes avant d'effacer tout le contenu de l'écran.
    Ensuite, elle affiche l'image de victoire en plein écran et le texte "Victoire"
    centré sur l'écran. Enfin, elle met à jour l'affichage et attend 3 secondes
    avant de terminer.

    Args:
        Aucun.

    Returns:
        Aucun.
    """
    time.sleep(2)
    fltk.efface_tout()
    fltk.image(0,0, "images/victoire.png", fltk.largeur_fenetre(), fltk.hauteur_fenetre(), ancrage = 'nw')
    fltk.texte(fltk.largeur_fenetre()//2, fltk.hauteur_fenetre()//2,"Victoire", "Black", "c")
    fltk.mise_a_jour()
    time.sleep(3)

def affichedefaite():
    """Affiche l'écran de défaite.

    Cette fonction affiche un écran de défaite avec une image et un texte.
    
    Args:
        Aucun.

    Returns:
        Aucun.

    Raises:
        Aucun.
    """
    time.sleep(2)
    fltk.efface_tout()
    fltk.image(0,0, "images/defaite.png", fltk.largeur_fenetre(), fltk.hauteur_fenetre(), ancrage = 'nw')
    fltk.texte(fltk.largeur_fenetre(), fltk.hauteur_fenetre(),"Défaite", "Black", "c")
    fltk.mise_a_jour()
    time.sleep(3)
