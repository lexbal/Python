import os;
import pickle;

score = {
   "joueur 1":    5,
   "joueur 2":   35,
   "joueur 3":   20,
   "joueur 4":    2,
}

with open("file.txt", "w") as mon_fichier:
	mon_fichier.write("That's my text !")
 
with open("file.txt", "r") as mon_fichier:
	contenu = mon_fichier.read()
	print(contenu)


with open('file_binary', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open('file_binary', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
    print(score_recupere)

# is closed ? => filename.closed
# closed : true 
# open : false
os.system("pause")