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


def conversion(fichier):
    with open(f"maps-texte/{fichier}") as fichier:
        readlines = [ligne.rstrip() for ligne in fichier.readlines()]
        len_y = len(readlines)
        len_x = len(readlines[0])
        grille=creer_grille(len_y, len_x)
        for y in range(len(readlines)):
            for x in range(len(readlines[0])):
                if readlines[y][x] == "#":
                    grille[y][x]="H"
                if readlines[y][x] == ">":
                    grille[y][x]="A"
                if readlines[y][x] == "*":
                    grille[y][x]="D"
    return grille 

afficher_grille(conversion("map_mini.txt"))