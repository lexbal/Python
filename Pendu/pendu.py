import function as function
import donnee as donnee
import os

function.resume()
player = function.player_info()
word   = function.get_random_word(donnee.words)

while True:
	char = function.input_letter()
	if not char in donnee.letters_pick:
		donnee.letters_pick.append(char)

	print("Letter always said : ", ", ".join(map(str, donnee.letters_pick)))

	word_list = function.crypt_word(donnee.letters_pick, word)
	print(word_list)
	if "*" in word_list:
		if word.find(char) == -1:
			donnee.chance = function.health_point(donnee.chance)
			if donnee.chance == 0:
				print("No more chance ! The word was => ", word)
				break
			print("You lost 1 health point (", donnee.chance, " left)")
	else:
		function.set_score(player, donnee.chance)
		print("You won !!!")
		break

os.system("pause")