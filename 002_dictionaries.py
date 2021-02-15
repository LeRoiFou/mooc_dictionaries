"""
Les dictionnaires : comprennent une clé et une valeur (comme le Hashmap dans Java)

Éditeur : Laurent REYNAUD
Date : 12-08-2020
"""

ang2fr = {"one": "un", "two": "deux", "three": "trois"}  # dictionnaire {clé1 : valeur1, clé2 : valeur2...}

print(type(ang2fr))  # <class 'dict'>

ang2fr["four"] = "quatre"  # Rajout d'une entrée dans le dictionnaire 'ang2fr' : [clé] = valeur
print(ang2fr)  # {'one': 'un', 'two': 'deux', 'three': 'trois', 'four': 'quatre'}

print(ang2fr["two"])  # deux : affichage de la valeur associée à la clé 'two'

d = {}  # dictionnaire vide
d = {"ent": 1, "list": [1, 2, 3], (1, 2): 3.141, "dic": ang2fr}  # les valeurs peuvent-être de n'importe quel type

print(d["dic"])  # {'one': 'un', 'two': 'deux', 'three': 'trois', 'four': 'quatre'}

print(d["dic"]["two"])  # deux : affichage de la valeur 'deux' de la clé 'two' du dictionnaire 'ang2fr'

print(d["list"][-1])  # 3 : affichage du dernier composant de la valeur [liste] de la clé 'list'

d = {'joe': 26, 'bob': 33, 'joe': 36}  # chaque clé d'un dictionnaire est unique...

print(d)  # {'joe': 36, 'bob': 33} : ...pour la clé 'joe' seule la dernière valeur du dictionnaire est affichée

print('one' in ang2fr)  # True : tout comme la fonction prédéfinie 'len', 'in' marche également dans un dictionnaire

print('deux' in ang2fr)  # False

for cle in ang2fr:  # La boucle for peut-être également utilisée dans un dictionnaire
    print(cle)
    """ 
    Résultat affiché: 
    one 
    two 
    three 
    four 
    """

del (ang2fr["four"])  # Possibilité d'utiliser la fonction prédéfinie 'del' dans un dictionnaire
print(ang2fr)  # {'one': 'un', 'two': 'deux', 'three': 'trois'}

""" 
Dans le dictionnaire 'tel' ci-dessous, la clé est un tuple de chaîne de caractères et la valeur est également une 
chaîne de caractères 
"""
tel = {('Baroud', 'Bill'): '065-37-07-56', ('II', 'Albert'): '02-256-89-14', ('Poelvoorde', 'Benoit'): '081-23-89-65'}

print(tel)
# {('Baroud', 'Bill'): '065-37-07-56', ('II', 'Albert'): '02-256-89-14', ('Poelvoorde', 'Benoit'): '081-23-89-65'}

for nom, prenom in tel:
    print(prenom, nom, tel[nom, prenom])
    """ 
    Résultat affiché: 
    Bill Baroud 065-37-07-56 
    Albert II 02-256-89-14 
    Benoit Poelvoorde 081-23-89-65 
    """

""" 
La fonction ci-après permet de compter la fréquence d'une lettre dans un mot 
"""


def histogram(mot):
    dico = {}  # initialisation du dictionnaire 'dico'
    for lettres in mot:  # pour chaque lettre du mot...
        if lettres in dico:  # si la lettre est déjà dans le dictionnaire
            dico[lettres] += 1  # alors la fréquence de cette lettre est augmentée de 1
        else:
            dico[lettres] = 1  # sinon la fréquence de cette lettre est de 1
    return dico


h = histogram('anticonstitutionnellement')  # la fonction histogram() est initialisée en une variable 'h'
print(h)  # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2} : clé = lettre / valeur = fréquence
