def absolue(a):
    result = []
    for i in range(len(a)):
        result.append(abs(a[i]))
    return result

def decalagegauche(lst):
        premier = lst.pop(0)
        lst.append(premier)
        return lst