def absolue(a):
    """Calcule la valeur absolue de chaque élément d'une liste.

    Args:
        a (list): Une liste d'éléments numériques.

    Returns:
        list: Une nouvelle liste contenant les valeurs absolues des éléments de la liste d'entrée.
    """
    result = []
    for i in range(len(a)):
        result.append(abs(a[i]))
    return result

def decalagegauche(lst):
    """Décale les éléments d'une liste vers la gauche.

    Args:
        lst (list): La liste à décaler.

    Returns:
        list: La liste décalée.
    """
    premier = lst.pop(0)
    lst.append(premier)
    return lst
