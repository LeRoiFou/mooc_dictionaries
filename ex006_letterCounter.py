"""
Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres de l’alphabet
associées à leur nombre d’apparition dans texte.

Exemple
L’appel de la fonction suivant :
compteur_lettres("Dessine-moi un mouton !")
retourne :
{'a': 0, 'b': 0, 'c': 0, 'd': 1, 'e': 2,
 'f': 0, 'g': 0, 'h': 0, 'i': 2, 'j': 0,
 'k': 0, 'l': 0, 'm': 2, 'n': 3, 'o': 3,
 'p': 0, 'q': 0, 'r': 0, 's': 2, 't': 1,
 'u': 2, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
 'z': 0}

Consignes :
    -> Les clés du dictionnaire seront les lettres de l’alphabet en minuscule. Si le texte contient des
    majuscules, celles-ci seront comptabilisées comme la lettre minuscule correspondante.
    -> Le texte passé en paramètre ne comportera aucun caractère accentué.
    -> Les espaces et autres caractères de ponctuation doivent être ignorés.

Éditeur : Laurent REYNAUD
Date : 17-08-2020
"""

""" 
La fonction compteur_lettres() a pour paramètre une chaîne de caractères 
Le résultat est un dictionnaire ayant pour clé une chaîne de caractères (les lettres de l'alphabet en minuscule) et 
pour valeur un entier (le nombre de lettres dans la phrase saisie) 
"""


def compteur_lettres(texte):
    lettres = []
    recap = []
    for c in texte:
        lettres.append(c.lower())
        recap.append([c.lower(), lettres.count(c)])
        recap.sort()
    alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                'z': 0}
    ma_liste = {}
    for i in alphabet:
        for j in recap:
            if i == j[0]:
                ma_liste[i] = j[1]
    ma_liste_bis = {**alphabet, **ma_liste}  # fusion de deux dictionnaires de taille différente
    return ma_liste_bis


phrase = 'Je viens d’arriver a l’Universite Libre de Bruxelles et pour l’instant je m’y plais tres bien.'
print(compteur_lettres(phrase))
