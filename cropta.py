import fltk

# R = route
# H = herbe
# A = arrivée
# D = départ

def creer_grille(x, y):
    grille = []
    for _ in range(y):
        ligne = []
        for _ in range(x):
            ligne.append("R")
        grille.append(ligne)
    return grille


def afficher_grille(grille):
    for ligne in grille:
        print(ligne)


def conversion_txt(fichier):
    with open(f"maps-texte/{fichier}") as fichier:
        readlines = [ligne.rstrip() for ligne in fichier.readlines()]
        len_y = len(readlines)
        len_x = len(readlines[0])
        grille=creer_grille(len_y, len_x)
        for y in range(len(readlines)):
            for x in range(len(readlines[0])):
                if readlines[y][x] == "#":
                    grille[y][x]="H"
                elif readlines[y][x] == ">":
                    grille[y][x]="A"
                elif readlines[y][x] == "*":
                    grille[y][x]="D"
    return grille 

def conversion_img(fichier, maillage):
    fltk.cree_fenetre(800,800, redimension=True)
    image = fltk.PhotoImage(file = f"maps-image/{fichier}")
    grille = creer_grille(maillage, maillage)
    largeur = image.width()
    hauteur = image.height()
    pas_x = largeur // maillage
    pas_y = hauteur // maillage
    x = -1
    y = -1
    for coord_y in range(0, hauteur, pas_y):
        y += 1
        for coord_x in range(0, largeur, pas_x):
            x += 1
            if image.get(coord_x, coord_y) == (0, 128, 128):
                grille[y][x] = "D"
            elif image.get(coord_x, coord_y) == (128, 128, 128):
                grille[y][x] = "A"
            elif image.get(coord_x, coord_y) not in [(0, 128, 128), (128, 128, 128), (255, 255, 255)]:
                grille[y][x] = "H"

conversion_img("map_test.png", 40)

#Bug map3.txt