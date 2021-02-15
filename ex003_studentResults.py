"""
Un jury doit attribuer le prix du « Codeur de l’année ».

Afin de récompenser les trois candidats ayant obtenu la meilleure moyenne, nous vous demandons d’écrire une fonction
top_3_candidats(moyennes) qui reçoit un dictionnaire contenant comme clés les noms des candidats et comme valeurs la
moyenne que chacun a obtenue.

Cette fonction doit retourner un tuple contenant les noms des trois meilleurs candidats, par ordre décroissant de
leurs moyennes.

Exemple
L’appel suivant de la fonction :
top_3_candidats({'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85,
                 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
                 'Candidat 4': 33})
doit retourner :
('Candidat 6', 'Candidat 5', 'Candidat 2')

Éditeur : Laurent REYNAUD
Date : 13-08-2020
"""

"""  
La fonction top_3_candidats() a pour paramètre :  
-> 'moyennes' qui est un dictionnaire ayant pour clé une chaîne de caractères (nom du candidat) et pour valeur un entier  
(moyenne obtenue du candidat)  
-> le résultat attendu est un tuple de chaîne de caractères (nom des 3 candidats ayant obtenus la meilleure moyenne par  
ordre décroissant)  
"""

concours_A = {'Candidat 7': 2, 'Candidat 2': 38, 'Candidat 6': 85, 'Candidat 1': 8, 'Candidat 3': 17, 'Candidat 5': 83,
              'Candidat 4': 33}


def top_3_candidats(moyennes):
    cumul = []
    cumul = list(moyennes.values())
    cumul.sort()
    top = (cumul[-1], cumul[-2], cumul[-3])
    res = []
    for composants in top:
        for valeurs in moyennes:
            if composants == moyennes[valeurs]:
                res.append(valeurs)
                test = tuple(res)
    return test


print(top_3_candidats(concours_A))
