import fltk
import math

# R = route
# H = herbe
# A = arrivée
# D = départ

def list_add(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

def list_add2(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] - b[i])
    return result

def absolue(a):
    result = []
    for i in range(len(a)):
        result.append(abs(a[i]))
    return result

def creer_grille(x, y):
    grille = []
    for _ in range(y):
        ligne = []
        for _ in range(x):
            ligne.append(0)
        grille.append(ligne)
    return grille

def decalagegauche(lst):
        premier = lst.pop(0)  # Retire le premier élément et le sauvegarde
        lst.append(premier)   # Ajoute cet élément à la fin de la liste
        return lst

def afficher_grille(grille):
    for ligne in grille:
        print(ligne)

def conversion_txt(fichier):
    with open(f"maps-texte/{fichier}") as fichier:
        readlines = [ligne.rstrip() for ligne in fichier.readlines()]
        len_y = len(readlines)
        len_x = len(readlines[0])
        grille=creer_grille(len_x, len_y)
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
        x = -1 
        for coord_x in range(0, largeur, pas_x):
            x += 1
            if y >= maillage or x >= maillage:
                break
            if image.get(coord_x, coord_y) == (0, 128, 128):
                grille[y][x] = "D"
            elif image.get(coord_x, coord_y) == (128, 128, 128):
                grille[y][x] = "A"
            elif image.get(coord_x, coord_y) not in [(0, 128, 128), (128, 128, 128), (255, 255, 255)]:
                grille[y][x] = "H"
            else:
                grille[y][x] = "R"
    afficher_grille(grille)

def miseenplacepion(plateau):
        len_y = len(plateau)
        len_x = len(plateau[0])
        listeposX = []
        listeposY = []
        posfinalX, posfinalY = 0,0
        grille = creer_grille(len_x, len_y)
        for y in range(len(plateau)):
            for x in range(len(plateau[0])):
                if plateau[y][x] == "D":
                    listeposX.append(x)
                    listeposY.append(y)
        posfinalX = (max(listeposX) + min(listeposX)) // 2
        posfinalY = (max(listeposY) + min(listeposY)) // 2
        grille[posfinalY][posfinalX] = 1
        posdepart = [posfinalX,posfinalY]
        return grille, posdepart

def remiseenplace(pos_actuelle, plateau):
    len_y = len(plateau)
    len_x = len(plateau[0])
    grille = creer_grille(len_y, len_x)
    grille[pos_actuelle[1]][pos_actuelle[0]] = 1
    return grille

def posactuelle(pos_parcouru):
    return pos_parcouru[-1]

def calcul_posibilite(plateau, pospion, posparcouru, regle):
    voisinpossibilite = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    mvtpossible = []
    if len(posparcouru) <= 1:
        pospotentielle = pospion
    else:
        distanceprecedent = list_add2(pospion, posparcouru[-2])
        pospotentielle = list_add(pospion, distanceprecedent)
        if coup_possible(plateau, pospion, pospotentielle, regle):
            mvtpossible.append(pospotentielle)
    for pos in voisinpossibilite:
        posacheck = list_add(pospotentielle, pos)
        if coup_possible(plateau, pospion, posacheck, regle):
            mvtpossible.append(posacheck)
    return mvtpossible

def gerer_evenement(ev,plateau_pion, mvtpossible, poseactuelle, pos_parcouru):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau_pion) 
    largeur_case = fltk.largeur_fenetre() / len(plateau_pion[0])
    Xclick, Yclick = fltk.abscisse(ev), fltk.ordonnee(ev)
    Xcaseclick = int((Xclick+largeur_case//2) // largeur_case)
    Ycaseclick = int((Yclick+hauteur_case//2) // hauteur_case)
    if [Xcaseclick, Ycaseclick] in mvtpossible:
        plateau_pion[poseactuelle[1]][poseactuelle[0]] = 0
        plateau_pion[Ycaseclick][Xcaseclick] = 1
        pos_parcouru.append([Xcaseclick, Ycaseclick])

def coup_possible(plateau, pospion, posacheck, regle):
    hauteur_case = fltk.hauteur_fenetre() / len(plateau) 
    largeur_case = fltk.largeur_fenetre() / len(plateau[0])
    if (0 <= posacheck[1] < len(plateau) and 0 <= posacheck[0] < len(plateau[0]) 
                and plateau[posacheck[1]][posacheck[0]] != "H"):
            if regle == "souple":
                return True
            for y in range(len(plateau)):
                for x in range(len(plateau[y])):
                    if plateau[y][x] == "H":
                        if intersection_cercle(pospion[0] * largeur_case, pospion[1] * hauteur_case,
                                            posacheck[0] * largeur_case, posacheck[1] * hauteur_case,
                                            x * largeur_case, y * hauteur_case, hauteur_case * 0.75):
                            return False
            return True
    return False

def distance_centre(x1, y1, x2, y2, xc, yc):

    longueursegmentcarre = (x2 - x1) ** 2 + (y2 - y1) ** 2

    if longueursegmentcarre == 0:
        return math.sqrt((xc - x1)**2 + (yc - y1)**2)

    
    t = max(0, min(1, ((xc - x1) * (x2 - x1) + (yc - y1) * (y2 - y1)) / longueursegmentcarre))

    x_proche = x1 + t * (x2 - x1)
    y_proche = y1 + t * (y2 - y1)
    
    return math.sqrt((x_proche - xc) ** 2 + (y_proche - yc) ** 2)

def intersection_cercle(x1, y1, x2, y2, xc, yc, r):
    distance = distance_centre(x1, y1, x2, y2, xc, yc)
    return distance <= r


def retour_arriere(posparcouru):
    posparcouru.pop()
    return posparcouru

def victoire(posparcouru, plateau):
    pos = posactuelle(posparcouru)
    if plateau[pos[1]][pos[0]] == 'A':
        return True
    return False

def defaite(mvtpossible):
    if len(mvtpossible) < 1:
        return True
    return False

def sauvegarde_partie(posparcouru, map, numero, regle):
    print("sauvegarde en cours..")
    chemin = f"./sauvegardes/{numero}.txt"
    sauvegarde = str([posparcouru,map, regle])
    with open(chemin, mode = "w") as mon_fichier:
        mon_fichier.write(sauvegarde)

def charger_fichier(fichier):
    with open(f"./sauvegardes/{fichier}.txt") as fichier:
        readlines = fichier.readlines()
        return eval(readlines[0])