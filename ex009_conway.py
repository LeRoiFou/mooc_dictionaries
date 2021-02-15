"""
Voici le début d’une suite logique inventée par John Horton Conway (et connue donc sous le nom de suite de Conway).
1
1 1
2 1
1 2 1 1
1 1 1 2 2 1
3 1 2 2 1 1
...
Chaque ligne, à partir de la deuxième, décrit la précédente :
la première ligne, 1, est formée de un “1”, d’où la deuxième ligne : 1 1 ;
la troisième ligne décrit la deuxième ligne, où l’on voit deux “1”, d’où 2 1 ;
la quatrième ligne décrit la troisième ligne, où l’on voit un “2” et un “1”, d’où 1 2 1 1 ;
et ainsi de suite.


Écrire une fonction next_line(line) qui reçoit une liste d’entiers décrivant une ligne de cette suite,
et qui retourne la liste correspondant à la ligne suivante.

Exemple 1
L’appel suivant de la fonction :
next_line([1, 2, 1, 1])
doit retourner :
[1, 1, 1, 2, 2, 1]

Exemple 2
L’appel suivant de la fonction :
next_line([1])
doit retourner :
[1, 1]

Exemple 3
L’appel suivant de la fonction :
next_line([])
doit retourner :
[1]

Consignes :
Notez que l’appel next_line([]) sur la liste vide retourne par convention la liste [1].

Éditeur : Laurent REYNAUD
Date : 18-08-2020
"""

""" 
La fonction next_line() a pour paramètre une liste d'entier 
Le résultat est une liste d'entier (ou de chaîne de caractères ?) 
"""


def next_line(numbers):
    if not numbers:
        res = [1]
    else:
        count = 0
        res = []
        val = numbers[0]
        for n in numbers:
            if n == val:
                count += 1

            else:
                res.extend([count, val])
                val = n
                count = 1
        res.extend([count, val])
    return res


print("Chiffres svp :")
chiffres = input()
print(next_line(chiffres))
