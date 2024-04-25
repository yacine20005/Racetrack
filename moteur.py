import fltk

# R = route
# H = herbe
# A = arrivée
# D = départ


list_add = lambda a, b: [a[i]+b[i] for i in range(len(a))]
list_add2 = lambda a, b: [a[i]-b[i] for i in range(len(a))]

def creer_grille(x, y):
    grille = []
    for _ in range(y):
        ligne = []
        for _ in range(x):
            ligne.append(0)
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
                elif readlines[y][x] == "*":
                    grille[y][x]="A"
                elif readlines[y][x] == ">":
                    grille[y][x]="D"
                else:
                    grille[y][x]="R"


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
            else:
                grille[y][x] = "H"

def miseenplacepion(plateau):
        len_y = len(plateau)
        len_x = len(plateau[0])
        listeposX = []
        listeposY = []
        posfinalX, posfinalY = 0,0
        grille = creer_grille(len_y, len_x)
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

def posactuelle(pos_parcouru):
    return pos_parcouru[-1]

def calcul_posibilite(plateau, pospion, posparcouru):
    voisinpossibilite = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
    mvtpossible = []
    if len(posparcouru) <= 1:
        pospotentielle = pospion
    else:
        distanceprecedent = list_add2(pospion, posparcouru[-2])
        pospotentielle = list_add(pospion, distanceprecedent)
        if pospotentielle[1] < len(plateau) and pospotentielle[0] < len(plateau) and plateau[pospotentielle[1]][pospotentielle[0]] != "H" :
            mvtpossible.append(pospotentielle)
    for pos in voisinpossibilite:
        posacheck = list_add(pospotentielle, pos)
        if posacheck[1] < len(plateau) and posacheck[0] < len(plateau) and plateau[posacheck[1]][posacheck[0]] != "H" :
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
        print("perdu")
        return True
    return False
