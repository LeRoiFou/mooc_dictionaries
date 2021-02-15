"""
Écrire une fonction belongs_to_file(word, filename) qui reçoit deux chaînes de caractères en paramètre. La première
correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne. La
fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon.

Exemple :
L’appel de la fonction suivant, où words.txt est le fichier indiqué dans les consignes ci-dessous et en supposant
qu'il se trouve dans le même répertoire que le programme :
belongs_to_file("renard", "words.txt")
retourne :
False

Consignes :
-> Vous pourrez supposer que le fichier passé en paramètre contient bien une liste de mots, chacun sur sa propre ligne.
-> N’oubliez pas d’ouvrir le fichier dans le code de la fonction.

Éditeur : Laurent REYNAUD
Date : 17-08-2020
"""

""" 
La fonction belongs_to_file() a pour paramètre : 
    -> une chaîne de caractères ('word' : mot recherché dans le fichier) 
    -> une autre chaîne de caractères ('filename' : fichier à récupérer pour rechercher le mot souhaité) 
Le résultat est un booléen (retourne 'True' si le mot recherché se trouve dans le fichier concerné et inversement) 
"""


def belongs_to_file(word, filename):
    with open(filename, encoding="utf-8") as f:
        filedata = f.readlines()
        trouve = False
        while not trouve:
            for ligne in filedata:
                if ligne.strip() == word:
                    trouve = True
            return trouve


print("Mot recherché :")
mot = input()
print("Fichier concerné : pieces/words.txt")
fichier = input()
print(belongs_to_file(mot, fichier))
