"""
Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2) signifiant que prenom1
déclare prenom2 comme étant son ami.

La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées, et la valeur
de chaque entrée est l’ensemble des amis de la personne.

Exemple
L’appel suivant de la fonction :
construction_dict_amis([('Quidam', 'Pierre'),
                        ('Thierry', 'Michelle'),
                        ('Thierry', 'Pierre')])
doit retourner :
{'Quidam' : {'Pierre'}, 'Pierre' : set(), 'Thierry' : {'Michelle', 'Pierre'}, 'Michelle' : set()}

Éditeur : Laurent REYNAUD
Date : 14-08-2020
"""

""" 
La fonction construction_dict_amis() a pour paramètre : 
-> une liste de tuples de chaînes de caractères ('prenom1' et 'prenom2') 
Le retour est un dictionnaire ayant pour clé une chaîne de caractères ('prenom1') et pour valeur un ensemble ('prenom2') 
"""

ma_liste = [('Quidam', 'Pierre'), ('Thierry', 'Michelle'), ('Thierry', 'Pierre')]


def construction_dict_amis(liste_amis):
    amis = {}
    for prenom1, prenom2 in liste_amis:
        if prenom1 not in amis:
            amis[prenom1] = {prenom2}
        else:
            amis[prenom1].add(prenom2)
        if prenom2 not in amis:
            amis[prenom2] = set()
    return amis


print(construction_dict_amis(ma_liste))
