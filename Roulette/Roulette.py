# -*-coding:UTF-8 -*
import os
from random import *

party_continuing = True
total_amount = 1000
print("Ton budget s'eleve a", total_amount, " €")

while party_continuing:
	try:
		numero = int(input("Sur quel numero voulez vous miser ? (0 à 50)"))
		if 0 >= numero or numero > 50:
			raise ValueError()
	except ValueError:
		print("Ce numero n'est pas valide.")
	else:
		try:
			somme = int(input("Quelle somme voulez vous miser ?"))
			if somme > total_amount:
				raise ValueError()
		except ValueError:
			print("La somme renseigné n'est pas valide.")
		else:
			total_amount -= somme
			numberWin = randint(0,49)
			print("Le numero gagnant est", numberWin)

			if numero == numberWin:
				amount_won = somme + (somme * 3)
				total_amount += amount_won 
				print("Vous etes tombé sur le bon numero !!! Vous avez gagner ", amount_won, " €")
			elif ((numero % 2 == 0) == (numberWin % 2 == 0)):
				amount_won = somme + (somme / 2)
				total_amount += amount_won 
				print("Vous etes tombé sur la bonne couleur ! Vous avez gagner ", amount_won, " €")
			else:
				print("Vous avez perdu...")

			print("Votre cagnote s'eleve a", total_amount, " €")

			if total_amount <= 0:
				print("Vous etes ruinée, désolé...")
				party_continuing = False

os.system("pause")