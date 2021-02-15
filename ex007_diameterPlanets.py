"""
Le Petit Prince a peur des baobabs qui, en poussant, pourraient abîmer sa minuscule planète. Par contre, il adore les
arbres à fleurs que Monsieur Jardinier lui montre. Touché par son enthousiasme, Monsieur Jardinier lui offre 1 000
graines de ces arbres à fleurs, mais maintenant, le Petit Prince doit trouver une planète suffisamment grande pour
les accueillir, sachant que chacun de ces arbres nécessite une surface de 50 m2 pour se développer sereinement.

Écrire une fonction booléenne bonne_planete(diametre) qui reçoit en paramètre un nombre représentant le diamètre,
en mètres, d'une planète candidate. La fonction retourne la valeur True ou False selon que la planète convient ou
non.

Écrire ensuite un programme qui lit un diamètre depuis l'entrée et affiche la chaîne de caractères "Bonne
planète" si le résultat de l'appel à la fonction bonne_planete est True la chaîne de caractères "Trop petite" sinon

Exemple 1
L’exécution du programme avec le nombre suivant en entrée  :
500
affiche :
"Bonne planète"

Exemple 2
L’exécution du programme avec le nombre suivant en entrée  :
10
affiche :
"Trop petite"

Consignes :
Nous rappelons que l'aire d'une sphère, solide auquel est assimilée une planète pour les besoins de
l'exercice, s'obtient par le calcul π * d2 où d désigne le diamètre de la sphère.

Éditeur : Laurent REYNAUD
Date : 17-08-2020
"""

""" 
La fonction bonne_planete() a pour paramètre un entier (diamètre de la planète) 
Le résultat est un boléen ("Bonne planète" ou "Trop petite") 
"""

import math


def bonne_planete(diametre):
    sphere = math.pi * diametre * diametre
    if sphere < 50000:
        res = False
    else:
        res = True
    return res


chiffre = int(input())
resultat = bonne_planete(chiffre)
if not resultat:
    print("Trop petite")
else:
    print("Bonne planète")
