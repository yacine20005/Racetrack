#R = route
#H = herbe
#A = arrivée
#D = départ

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


def convertion(fichier):
    with open(f"maps-texte/{fichier}") as fichier:
        readlines = [ligne.rstrip() for ligne in fichier.readlines()]
        x = len(readlines)
        y = len(readlines[0])
        grille = creer_grille(y, x)
        afficher_grille(grille)
        for y in range(y):
            for x in range(x):
                if readlines[y][x] == "#":
                    grille[y][x] = "H"
                if readlines[y][x] == ">":
                    grille[y][x] = "A"
                if readlines[y][x] == "*":
                    grille[y][x] = "D"


convertion("map_mini.txt")
