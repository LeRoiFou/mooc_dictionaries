"""
Exemple de programme pour récuper les données d'un fichier .csv avec comme séparateur la ',' 

Éditeur : Laurent REYNAUD 
Date : 20-08-20 
"""


def charger(filename, sep):
    liste_donnees = []
    with open(filename, 'r', encoding='utf-8') as mon_csvfile:
        les_entetes = mon_csvfile.readline().strip().split(sep)  # lecture de la 1ère ligne sans blanc et séparateur
        for ligne in mon_csvfile:
            d_donnees = {}
            l_donnees = ligne.strip().split(sep)
            for index, donnee in enumerate(l_donnees):
                d_donnees[les_entetes[index]] = donnee
            liste_donnees.append(d_donnees)
    return liste_donnees


print("Fichier à ouvrir -> pieces/mon_fichier.csv")
mon_fichier = input()
print("Séparateur : ")
separateur = input()
print(charger(mon_fichier, separateur))
