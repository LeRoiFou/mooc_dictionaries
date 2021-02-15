"""
Introduction aux ensembles et aux dictionnaires

Éditeur : Laurent REYNAUD
Date : 11-08-2020
"""

"""  
Pour créer un ensemble on utilise des '{}'  
Dans un ensemble, il n'y a pas d'ordre d'affichage tout comme le dictionnaire HashMap dans Java  
"""
personnages = {"rose", "serpent", "renard", "renard", "rose"}
print(personnages)  # {'rose', 'renard', 'serpent'} -> n'affichera qu'une seule fois les mots "rose" et "renard"

print(len(personnages))  # 3 : les contenus "rose" et "renard" ne sont pris en compte qu'une seule fois

personnages = {"serpent", "renard", "rose"}
print("rose" in personnages)  # True : la fonction "in" fonctionne pour les ensembles
print("lion" in personnages)  # False

for p in personnages:  # la fonction "for" fonctionne pour les ensembles
    print(p)
    """  
    Résultat :  
    serpent  
    renard  
    rose  
    """

"""  
La fonction prédéfinie 'set' va prendre une séquence et la transformer en ensemble  
"""
s = set("abracadabra")
t = set("alakazam")

print(s - t)  # {'b', 'd', 'c', 'r'} : donne les lettres qui sont dans la variable 's' mais pas dans 't'

print(s | t)  # {'c', 'l', 'r', 'm', 'a', 'd', 'b', 'z', 'k'} : donne l'union des lettres de 's' et de 't'

print(s & t)  # {a} : donne les lettres communes de 's' et de 't'

print(s ^ t)  # {'k', 'z', 'c', 'd', 'r', 'l', 'b', 'm'} : donne les lettres qui ne sont pas communes entre 's' et 't'

s.add("x")  # ajoute un élément dans 's'
print(s)  # {'d', 'r', 'c', 'a', 'b', 'x'}

s.discard("w")  # supprime un élément même s'il n'existe pas dans l'ensemble 's'
print(s)  # {'r', 'x', 'b', 'c', 'd'}

s.pop()  # supprime au hasard un élément de l'ensemble 's' (ici l'élémént 'd' a été supprimé)
print(s)  # dans le désordre affiche : {'t', 'r'}

s.clear()  # supprime tous les éléments de l'ensemble 's'
print(s)  # set()

vide = set()  # déclaration d'un ensemble vide
print(vide)  # set()

a = {1, 2, 3}
b = {1, 2, 3, 5}

print(a < b)  # True

print(a <= b)  # True

print(a >= b)  # False

t = {"k", "m", "a", "l", "z"}
print(t[0])  # Dans un ensemble on ne peut pas sélectionner un élémént, il n'y a pas d'indice
