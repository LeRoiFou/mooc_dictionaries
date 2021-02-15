"""
Après avoir longuement réfléchi et un peu visité notre monde, le Petit Prince décide de ne pas rentrer sur sa planète
mais de s’installer dans les Cévennes pour profiter de la belle nature qu’on y trouve. Il y trouve une petite demeure
pour y habiter, et plusieurs de ses amis veulent l’aider en lui proposant des meubles, des denrées, des livres ou
d’autres choses qui pourraient l’intéresser pour aménager son nouveau domicile.

Nous vous proposons de l'aider.
Écrire une fonction inventaire(offres, objets) où :
-> offres est un dictionnaire contenant, comme clés, les objets proposés par les amis du Petit Prince, et comme valeurs
associées, le nom de l'ami proposant cet objet,
-> objets est une liste contenant tous les objets dont a besoin le Petit Prince.
La fonction retourne l'ensemble des amis chez qui il lui faut se rendre pour sa récolte.


Exemple
L’appel suivant de la fonction :
inventaire({'lit': 'Antoine', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle', 'livre "le vieil homme et la mer"':
            'Ernest', 'sac de bonbons': 'Thierry', 'smartphone': 'Ted', 'table': 'Sophie'}, ['sac de bonbons', 'table',
            'chaise', 'lit', 'livre "le vieil homme et la mer"'])
doit retourner (à l'ordre près) :
{'Thierry', 'Sophie', 'Isabelle', 'Antoine', 'Ernest'}

Consignes
-> Dans cet exercice, il vous est demandé d’écrire seulement la fonction inventaire. Le code que vous soumettez à UpyLaB
doit donc comporter uniquement la définition de cette fonction, et ne fait en particulier aucun appel à input ou à
print.
-> Vous pourrez supposer que les arguments passés à la fonction sont du bon type, et que les objets  dont a besoin le
Petit Prince  figurent bien parmi ceux offerts par ses amis.

Éditeur : Laurent REYNAUD
Date : 12-08-2020
"""

""" 
-> Le paramètre 'offres' est un dictionnaire avec pour clé et valeur une chaîne de caractères : 
{'lit': 'Antoine', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle', 'livre "le vieil homme et la mer"': 'Ernest',  
    'sac de bonbons': 'Thierry', 'smartphone': 'Ted', 'table': 'Sophie'} 
-> Le paramètre 'objets' est une liste : 
['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"'] 
Le but est de recouper les composants de la liste 'objets' avec les clés du dictionnaire 'offres' 
-> Le résultat attendu est un ensemble 
"""


def inventaire(offres, objets):
    res = set()  # déclaration vide d'un ensemble
    for cle in offres:  # pour chaque clé du dictionnaire 'offres'
        for composant in objets:  # pour chaque composant de la liste 'objets'
            if composant in cle:  # si le composant de la liste 'objets' se trouve dans la clé du dictionnaire 'offres'
                res.add(offres[cle])
    return res


souhait = ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']

propositions = {'lit': 'Antoine', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle',
                'livre "le vieil homme et la mer"': 'Ernest', 'sac de bonbons': 'Thierry', 'smartphone': 'Ted',
                'table': 'Sophie'}

print(inventaire(souhait, propositions))
