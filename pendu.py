# -*- coding: utf-8 -*-
from donnees import *
from fonctions import *
import os
sauvegarde, dic_mot = recup_scores()
utilisateur = recup_nom_utilisateur()
if utilisateur not in sauvegarde["scores"].keys():
	sauvegarde["scores"][utilisateur] = 0

ajouter_mot_liste(dic_mot)
supprimer_mot_liste(dic_mot)
choix_liste = choix_liste(dic_mot)

continuer_partie = "o"
while continuer_partie != "n":
	lettres_saisie = []
	lettres_trouvees = []
	print("Joueur {0}: {1} point(s) \n".format(utilisateur, sauvegarde["scores"][utilisateur]))
	joueur_liste, nb_joueur = def_classement(sauvegarde["scores"])
	afficher_classement(joueur_liste ,sauvegarde["scores"], nb_joueur)
	print("\n\n")	
	mot_a_trouver = choisir_mot(choix_liste, dic_mot)	
	mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
	nb_chances = nb_coups
	while mot_a_trouver!=mot_trouve and nb_chances>0:
		print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
		lettre = recup_lettre(lettres_trouvees, lettres_saisie)
		if lettre in mot_a_trouver:
			lettres_trouvees.append(lettre)
			print("Bien joué.")
		else:
			nb_chances -=1
			print("... non, cette lettre ne se trouve pas dans le mot...")
			afficher_personne(nb_chances)
		mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
		print("\n \n") 	
	if mot_trouve == mot_a_trouver:
		print("Félicitation ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
	else:
		print("PENDU !!! Vous avez perdu.")
	sauvegarde["scores"][utilisateur] += nb_chances
	continuer_partie = input("Souhaitez vous continuer la partie (O/N) ?")
	continuer_partie = continuer_partie.lower()
	os.system("cls")
	enregistrer_scores(sauvegarde,dic_mot)



joueur_liste, nb_joueur = def_classement(sauvegarde["scores"])
print("Vous finissez la partie avec {0} points.".format(sauvegarde["scores"][utilisateur]))
afficher_classement(joueur_liste ,sauvegarde["scores"], nb_joueur)

os.system("pause")
		 