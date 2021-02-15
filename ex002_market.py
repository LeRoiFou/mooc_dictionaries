"""
Monsieur Germain est une personne très âgée. Il aimerait préparer une liste de courses à faire à l’avance. Ayant un
budget assez serré, il voudrait que sa liste de courses soit dans ses capacités. Son seul petit souci est qu’il a une
très mauvaise vue et n’arrive donc pas à voir le prix associé à chaque produit contenu dans le catalogue de courses.

Écrire une fonction calcul_prix(produits, catalogue) où :
-> produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs
associées, la quantité désirée de chacun d’entre eux,
-> catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.

La fonction retourne le montant total des achats de Monsieur Germain.

Exemple
L’appel suivant de la fonction :
calcul_prix({"brocoli":2, "mouchoirs":5, "bouteilles d'eau":6},
            {"brocoli":1.50, "bouteilles d'eau":1, "bière":2,
             "savon":2.50, "mouchoirs":0.80})
doit retourner :
13.0

Éditeur : Laurent REYNAUD
Date : 13-08-2020
"""

""" 
-> Le paramètre 'produits' est un dictionnaire ayant pour clé une chaîne de caractères (produit souhaité) et pour valeur 
 un réel (quantité de produit souhaitée) 
-> Le paramètre 'catalogues' est un dictionnaire ayant pour clé une chaîne de caractères (produit recoupé) et pour  
valeur un réel (prix du produit concerné) 
-> Le résultat attendu est de type réel qui donne le prix total des produits souhaités 
"""


def calcul_prix(produits, catalogues):
    res = 0.0
    for cle in produits:
        for cle_bis in catalogues:
            if cle_bis in cle:
                res += produits[cle] * catalogues[cle_bis]
    return res


client = {"brocoli": 2, "mouchoirs": 5, "bouteilles d'eau": 6}
magasin = {"brocoli": 1.50, "bouteilles d'eau": 1, "bière": 2, "savon": 2.50, "mouchoirs": 0.80}
print(calcul_prix(client, magasin))
