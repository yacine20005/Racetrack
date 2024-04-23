def creer_grille(n):
    grille = []
    for x in range(n):
        ligne = []
        for y in range(n):
            ligne.append(0)
        grille.append(ligne)
    return grille
