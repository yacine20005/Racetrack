import fltk
import grillage as gr

def conversion_txt(fichier):
    """
    Convertit un fichier texte en une grille de jeu.

    Args:
        fichier (str): Le chemin du fichier texte à convertir.

    Returns:
        list: Une grille de jeu représentée sous forme de liste.
              Chaque élément de la liste représente une ligne de la grille.
              Les caractères "#" sont convertis en "H",
              les caractères "*" sont convertis en "A",
              les caractères ">" sont convertis en "D",
              les autres caractères sont convertis en "R".
              Si le fichier n'est pas valide, None est retourné.
    """
    with open(f"maps-texte/{fichier}", encoding="utf-8") as fichier:
        readlines = [ligne.rstrip() for ligne in fichier.readlines()]
        len_y = len(readlines)
        len_x = len(readlines[0])
        grille=gr.creer_grille(len_x, len_y)
        for y in range(len(readlines)):
            for x in range(len(readlines[0])):
                if len(readlines[y]) != len_x:
                    return None
                if readlines[y][x] not in ["#", "*", ">", "."]:
                    return None
                if readlines[y][x] == "#":
                    grille[y][x]="H"
                elif readlines[y][x] == "*":
                    grille[y][x]="A"
                elif readlines[y][x] == ">":
                    grille[y][x]="D"
                else:
                    grille[y][x]="R"
    return grille

def conversion_img(fichier, maillage):
    """Convertit un fichier image en une grille de jeu.

    Args:
        fichier (str) : Le chemin du fichier image à convertir.
        maillage (int): Taille du maillage.

    Returns:
        None
    """
    image = fltk.PhotoImage(file = f"maps-image/{fichier}")
    grille = gr.creer_grille(maillage, maillage)
    largeur = image.width()
    hauteur = image.height()
    pas_x = largeur // maillage
    pas_y = hauteur // maillage
    x = -1
    y = -1
    for coord_y in range(0, hauteur, pas_y):
        y += 1
        x = -1
        for coord_x in range(0, largeur, pas_x):
            x += 1
            if y >= maillage or x >= maillage:
                break
            if image.get(coord_x, coord_y) == (0, 128, 128):
                grille[y][x] = "D"
            elif image.get(coord_x, coord_y) == (128, 128, 128):
                grille[y][x] = "A"
            elif image.get(coord_x, coord_y) not in [(0, 128, 128),
                                                     (128, 128, 128), (255, 255, 255)]:
                grille[y][x] = "H"
            else:
                grille[y][x] = "R"
    gr.afficher_grille(grille)
    return grille
