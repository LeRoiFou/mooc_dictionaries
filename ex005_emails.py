"""
Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie un
dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs
correspondantes, triées par ordre croissant (UTF-8).

Exemple
L’appel de la fonction suivant :
store_email(["ludo@prof.ur", "andre.colon@stud.ulb",
             "thierry@profs.ulb", "sébastien@prof.ur",
             "eric.ramzi@stud.ur", "bernard@profs.ulb",
             "jean@profs.ulb" ])
retourne le dictionnaire :
{ 'prof.ur' : ['ludo', 'sébastien'],
  'stud.ulb' : ['andre.colon'],
  'profs.ulb' : ['bernard', 'jean', 'thierry'],
  'stud.ur' : ['eric.ramzi'] }

Éditeur : Laurent REYNAUD
Date : 15-08-2020
"""

""" 
La fonction store_email() a pour paramètre une liste de chaînes de caractères 
Le résultat est un dictionnaire ayant pour clé une chaîne de caractères et pour valeur une liste de chaînes de  
caractères triée 
"""

adresses = ["ludo@prof.ur", "andre.colon@stud.ulb",
            "thierry@profs.ulb", "sébastien@prof.ur",
            "eric.ramzi@stud.ur", "bernard@profs.ulb",
            "jean@profs.ulb"]


def store_email(liste_mails):
    mon_dico = {}
    recap_liste1 = []
    recap_liste2 = []
    for i in liste_mails:
        recap_liste1.append(i.split("@"))
    for elt1, elt2 in recap_liste1:
        recap_liste2.append([elt2, elt1])
    recap_liste2.sort()

    ma_liste = set()
    for i in liste_mails:
        recap_liste1 = i.split("@")
        ma_liste.add(recap_liste1[1])

    for domaine in ma_liste:
        for adresse in recap_liste2:
            if domaine == adresse[0]:
                if domaine not in mon_dico:
                    mon_dico[domaine] = [adresse[1]]
                else:
                    mon_dico[domaine].append(adresse[1])
    return mon_dico


print(store_email(adresses))
