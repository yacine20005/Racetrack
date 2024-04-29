import moteur

def solveur_profondeur(grille, vecteur, deque):
    while len(deque) != 0:
        i,j = deque.pop()
        if plateau[i][j] != "white":
            continue
        plateau[i][j] = "red"
        affiche_plateau(plateau)
        for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            deque.append((a,b))

grille = moteur.conversion_txt("map_test.txt")
pion, pos_depart = moteur.miseenplacepion(grille)
print(moteur.calcul_posibilite(grille, pos_depart, [pos_depart]))