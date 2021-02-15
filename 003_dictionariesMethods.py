"""
Les méthodes des dictionnaires

Éditeur : Laurent REYNAUD
Date : 14-08-2020
"""

""" 
Création, ajout et recherche d'éléments dans un dictionnaire 
"""

d = {'yes': 'oui', 'no': 'non'}

d2 = d.copy()  # copie du dictionnaire 'd'
print(d2)  # {'yes': 'oui', 'no': 'non'}

from copy import deepcopy  # recour à la copie profonde 'deepcopy' possible (voir Module5-17_Listes&Comprehension&Copie)

d2 = deepcopy(d)

d2.clear()  # suppression des données du dictionnaire 'd2'
print(d2)  # {}

d2 = {}.fromkeys('abcde', 0)  # la méthode fromkeys() permet d'affecter une même valeur à une séquence de clés
print(d2)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

# la fonction get() permet de récupérer la valeur d'une clé si la valeur existe sinon affichage d'une valeur par défaut
print(d.get("yes", "mot inconnu"))  # oui : valeur de la clé 'yes' existante dans le dictionnaire 'd'
print(d.get('a', 'mot inconnu'))
""" 
"mot inconnu" : il n'y a pas de clé 'a' dans le dictionnaire 'd' -> affichage de la valeur par défaut qui est 'mot  
inconnu'  
"""

d.setdefault('tree', 'arbre')  # fonctionne de la même façon que get, mais si la clé n'existe pas, celle-ci est rajoutée
print(d)  # {'yes': 'oui', 'no': 'non', 'tree': 'arbre'}

print('yes' in d)  # True : permet de savoir si une clé fait partie des clés du dictionnaire

""" 
Les méthodes keys(), values() et items() permettent d'obtenir des clés / des valeurs du dictionnaire 
"""

d = {'a': 1, 'b': 2}

print(d.keys())  # dict_keys(['a', 'b']) : permet d'obtenir les clés du dictionnaire

print(d.values())  # dict_values([1, 2]) : permet d'obtenir les valeurs du dictionnaire

print(d.items())  # dict_items([('a', 1), ('b', 2)]) : permet d'obtenir les clés et les valeurs du dictionnaire

for cle, valeur in d.items():  # recours à la méthode items() en association avec la boucle for
    print(cle, valeur)
    """ 
    Résulat affiché : 
    a 1 
    b 2 
    """

""" 
La méthode pop() permet de retirer des clés du dictionnaire 
"""

eng2fr = {'one': 'un', 'two': 'deux', 'three': 'trois'}

print(eng2fr.pop('three'))  # trois : la méthode pop() retire une clé du dictionnaire avec la valeur associée
print(eng2fr.pop("four", "clé inconnue"))
""" 
"clé inconnue" : avec ce deuxième paramètre, la clé "four" n'existant pas, le programme affiche donc "clé inconnue".  
À défaut de ce deuxième paramètre, il y aurait eu un message d'erreur  
"""
print(eng2fr)  # {'one': 'un', 'two': 'deux'}

""" 
La méthode update() permet de rajouter plusieurs clés avec des valeurs associées     
"""

d = {'a': 0}

d.update(zip('bcd', range(1, 4)))
print(d)  # {'a': 0, 'b': 1, 'c': 2, 'd': 3}

""" 
Changement de type avec la méthode dict() pour convertir un type qui doit être obligatoirement une séquence de couples  
en un dictionnaire (clé, valeur) 
"""

l = [('a', 1), ('b', 2)]  # déclaration d'une liste de couples

print(dict(l))  # {'a': 1, 'b': 2} : conversion de la liste de couples en un dictionnaire
print(dict(zip('abc', range(3))))  # {'a': 0, 'b': 1, 'c': 2} : idem avec le recours de la fonction zip()
