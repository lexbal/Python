# -*-coding:UTF-8 -*
import os
from multiply import *

# Is a function
"""f = lambda x: x * x
f(5)

table(7,10)"""

annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
    if annee == 0:
        raise ValueError("L'année saisie est nulle")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

os.system("pause")