"""
Ce module devra par la suite etre importer dans le FReveil 
Module créé le : 2017_2_15
Nom initial du module : musique

"""
from config import *
import os
from time import *


def start(arguments):
	# Cette fonction sera la fonction qui sera lancée par le module. argument est une liste contenant les arguments passés au lancement du module
	
	# Le code qui suit jusqu'à #FIN est un code pour recuperer l'exclusivité pour utiliser l'audio au sein du FReveil.
	# Il suffit d'insérer votre code utilisant l'audio à l'endroit indiquer.
	# A chaque fois que vous souhaitez utiliser l'audio vous devriez utiliser ce code :
	if len(arguments) != 0:
		id = requestAudio()
		# Votre code utilisant l'audio
		os.system("mpg321 -q  {} && touch musique.f &".format(arguments[0]))
		continuer = True
		conf = Config()
		while continuer:
			#print("boucle")
			conf.openConfig()
			continuer = not Outils.testPresence("musique.f")
			sleep(1)
			if conf.bouton :
				continuer = False
				#print("Terminus killall")
				os.system("killall mpg321")

		#print("Sortie de la boucle")
		Outils.supprimerFichier("musique.f")

		giveRequestAudio(id)

	#FIN
			
	pass




def giveRequestAudio(id):
	# Lache l'autorisation d'utiliser l'audio pour qu'un autre module puisse l'utiliser.
	conf = Config ()
	conf.setLockAudio(False,id)

def requestAudio(): 
	# Demande l'autoristion d'utiliser l'audio. Cette méthode est bloquante jusqu'à ce que l'autorisation soit donnée.
	conf = Config ()
	id = conf.getId()
	audio =  0
	while audio != 1:
		audio = conf.setLockAudio(True,id)
	return id

		