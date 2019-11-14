# -*-coding:UTF-8 -*
import os

def tri_list(my_list):
	inventaire_inverse = [(quantity, fruit) for fruit,quantity in my_list]
	print([(fruit, quantity) for quantity,fruit in sorted(inventaire_inverse, \
    reverse=True)])

inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

tri_list(inventaire)


os.system("pause")