# -*-coding:UTF-8 -*
import os

def afficher_flottant(flottant):

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")

    return ",".join([partie_entiere, partie_flottante[:3]])

print(afficher_flottant(3.255))

os.system("pause")