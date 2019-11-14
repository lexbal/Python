import pickle
import traceback
import os.path as path
from random import *

def player_info():
	alreadyExist = False
	try:
		player_name = input("Please tell us your name :")

		player = {
		   player_name:    0,
		}

		if not path.exists('player_info') and not path.isfile('player_info'):
			with open('player_info', 'wb') as player_info:
				file = pickle.Pickler(player_info)
				file.dump(player)
		else:
			with open('player_info', 'rb') as player_info:
				file = pickle.Unpickler(player_info)
				data = file.load()
				if player_name in data:
					print('Welcome back, ', player_name)
					alreadyExist = True
			
			if not alreadyExist:
				with open('player_info', 'wb') as player_info:
					file = pickle.Pickler(player_info)
					data.update(player)
					file.dump(data)
		return player_name
	except Exception: 
		print(traceback.format_exc())

def resume():
	try:
		if not path.exists('player_info') and not path.isfile('player_info'):
			print("No users found")
		else:
			with open('player_info', 'rb') as player_info:
				file_read = pickle.Unpickler(player_info)
				data = file_read.load()
				print(data)
	except Exception:
		print(traceback.format_exc())

def get_random_word(words):
	try:
		word = choice(words)
	except Exception:
		print(traceback.format_exc())

	return word

def input_letter():
	try:
		while True:
		    character = input("\nWhich letter do you pick ?")
		    if len(character) != 1:
		        print('Enter only ONE character !')
		    else:
		        break

		return character
	except Exception:
		print(traceback.format_exc())

def crypt_word(letters, word):
	try:
		word_crypt = list(word)
		word_list  = list(word_crypt)

		for key, char in enumerate(word_crypt):
		    word_crypt[key] = "*"

		for letter in letters:
			for key, char in enumerate(word_list):
			    if char == letter:
			        word_crypt[key] = letter

		return word_crypt
	except Exception:
		print(traceback.format_exc())

def health_point(health):
	health -= 1

	return health

def set_score(player, score):
	try:
		if path.exists('player_info') and path.isfile('player_info'):
			with open('player_info', 'rb') as player_info:
				file = pickle.Unpickler(player_info)
				data = file.load()
			with open('player_info', 'wb') as player_info:
				file = pickle.Pickler(player_info)
				data[player] += score
				file.dump(data)
	except Exception:
		print(traceback.format_exc())