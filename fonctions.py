# -*- coding: utf-8 -*-
import os 

import pickle
import operator
from random import choice

from donnees import *



def recup_scores():
	if os.path.exists(nom_fichier_scores):
		with open(nom_fichier_scores,"rb") as fichier_scores:
			mon_depickler = pickle.Unpickler(fichier_scores)
			sauvegarde = mon_depickler.load()
	else:
		scores= {}
		sauvegarde = {}
		sauvegarde["scores"] = scores

	if os.path.exists("mot"):		
		with open("mot","rb") as fichier_mot:
			mon_depickler = pickle.Unpickler(fichier_mot)
			dic_mot = mon_depickler.load()
	else:
		dic_mot = {}
		dic_mot["theme"] = ["maison", "jardin", "ecole", "sport"]
		mot = {}
		dic_mot["mot"] = mot
		dic_mot["mot"]["maison"] = ["fourchette", "cuisine", "maison", "porte", "armoire", "jeux", "ordinateur", "telephone"]
		dic_mot["mot"]["jardin"] = ["feuille", "jardin", "herbe", "neige"," piscine", "froid", "chaud", "pluie", "tempete"]
		dic_mot["mot"]["ecole"] = ["ecole", "trousse", "crayon", "tableau","bureau","copain","classe","colle","recreation"]
		dic_mot["mot"]["sport"] = ["football", "tennis", "basket", "pingpong"]
	return sauvegarde, dic_mot		

def enregistrer_scores(sauvegarde, dic_mot):
	with open(nom_fichier_scores, "wb") as fichier_scores:
		mon_pickler = pickle.Pickler(fichier_scores)
		mon_pickler.dump(sauvegarde)
	with open("mot", "wb") as fichier_mot:
		mon_pickler_mot = pickle.Pickler(fichier_mot)
		mon_pickler_mot.dump(dic_mot)	

def recup_nom_utilisateur():
	nom_utilisateur = input("Tapez votre nom : ")
	nom_utilisateur = nom_utilisateur.capitalize()
	if not nom_utilisateur.isalpha() or len(nom_utilisateur) < 4:
		print("Nom invalide")
		return recup_nom_utilisateur()
	else:
		return nom_utilisateur

def recup_lettre(lettres_trouvees, lettres_saisie):
	"""La fonction recupère la lettre entrer par l'utilisateur
	"""
	lettre = input("Tapez une lettre : ")
	lettre = lettre.lower()
	if len(lettre)>1 or not lettre.isalpha():
		print("Choix invalide ! ")
		return recup_lettre(lettres_trouvees, lettres_saisie)
	elif lettre in lettres_trouvees or lettre in lettres_saisie:
		print("Vous avez déjà choisi cette lettre.")
		return recup_lettre(lettres_trouvees, lettres_saisie)
	else:
		lettres_saisie.append(lettre)
		return lettre	

def liste_tout(dic_mot):
	dic_mot["mot"]["tout"][:]= []
	liste_tout = list()
	for i in dic_mot["mot"].values():
		liste_tout.extend(i)
	dic_mot["mot"]["tout"] = liste_tout
def choisir_mot(choix, dic_mot):
	"""Cette fonction choisie un mot dans la liste : liste_mot
	"""
	if choix == "tout":  
		return choice(dic_mot["mot"]["tout"])
	else:
		return choice(dic_mot["mot"][choix])


def recup_mot_masque(mot_complet, lettres_trouvees):
    """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
    - du mot d'origine (type str)
    - des lettres déjà trouvées (type list)

    On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
    n'a pas encore trouvées."""
    
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque

					

def afficher_personne(chance):
	"""Cette fonction est chargée d'afficher notre pendu au fur et à mesure"""
	if chance == 9:
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("\n")
		print("_____________\n")
	elif chance ==8:
		print("\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 7:
		print("_____________\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance ==6:
		print("_____________\n")
		print(" | /\n")
		print(" |/\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 5:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 4:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/       O\n")
		print(" |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 3:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/       O\n")
		print(" |        |\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 2:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/       O\n")
		print(" |       -|-\n")
		print(" |\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 1:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/       O\n")
		print(" |       -|-\n")
		print(" |        /\\\n")
		print(" |\n")
		print("_|____________\n")
	elif chance == 0:
		print("_____________\n")
		print(" | /      |\n")
		print(" |/       O\n")
		print(" |       -|-\n")
		print(" |        /\\\n")
		print(" |\n")
		print("_|____________\n")
		print("Trop tard je suis mort !\n")
				

def def_classement(scores):
	nb_joueur = len(scores)
	if nb_joueur > 3:
		nb_joueur = 3
	joueur_liste = [None] *nb_joueur
	score_l = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
	score_l = score_l[:nb_joueur]
	i = 0
	while i !=nb_joueur:
		joueur_liste[i] = score_l[i][0]
		i += 1
	return joueur_liste, nb_joueur
	
			
				
def afficher_classement(joueur_liste, scores, nb_joueur):
	print("Classement :\n")
	i = 0
	while i !=nb_joueur:
		print("Joueur ",i+1," :",joueur_liste[i],"avec",scores[joueur_liste[i]],"points")
		i += 1


def choix_liste(dic_mot):
	liste_tout(dic_mot)
	print("Quelles listes de mots voulez vous ? : \n")
	i= 1
	for mot in dic_mot["theme"]:
		print(i,"",mot.capitalize(),"(",len(dic_mot["mot"][mot]),"mots)")
		i +=1	
	print(i," Pas de catégorie","(",len(dic_mot["mot"]["tout"]),")\n")

	i = 0
	while i !=1:
		choix= input("Quelles est votre choix ? : ")
		try:
			choix = int(choix)
		except ValueError:
			print("Choix invalide ! ")
			continue
		if choix < 1 or choix >len(dic_mot["theme"]) +1:
			print("Choix invalide ! ")
			continue
		else:
			i = 1
			if choix == len(dic_mot["theme"])+1:
				choix = "tout"
				return choix	
			else:	
				return dic_mot["theme"][choix-1]


def ajouter_mot_liste(dic_mot):
	autre_liste = 1
	while autre_liste == 1:
		choix_autre_liste = input("Voulez vous modifier une liste ? (o/n) : ")
		choix_autre_liste = choix_autre_liste.lower()
		if not choix_autre_liste.isalpha() or len(choix_autre_liste) !=1 :
			print("Choix invalide ! ")
			ajouter_mot_liste(dic_mot)
		if choix_autre_liste == "o":
			autre_liste = 0
		elif choix_autre_liste == "n":
			return	
	mot_juste = 1
	while mot_juste == 1:
		print("\nVoici la liste des thème : ")
		i = 1
		for mot in dic_mot["theme"]:
			print(i,"",mot.capitalize(),"(",len(dic_mot["mot"][mot]),"mots)")
			i += 1
		print("\n")	
		theme_choisie = input("Quelle est le nom de votre thème \nSi il n'existe pas elle sera crée : ")
		theme_choisie = theme_choisie.lower()
		if theme_choisie.isdigit() and int(theme_choisie) > 0 and int(theme_choisie) < 1+len(dic_mot["theme"]):
			theme_choisie = dic_mot["theme"][int(theme_choisie)-1]
		elif not theme_choisie.isalpha() or len(theme_choisie) < 4:
			print("Choix invalide ! ")
			continue
		elif theme_choisie in dic_mot["theme"]:
			print("Le thème ",theme_choisie," est déja existant.\n")
		else:
			dic_mot["theme"].append(theme_choisie)
			print("Le thème",theme_choisie," est ajoutée.\n")
		mot_juste = 0
	stop = 1
	while stop == 1:
		continuer = True
		print("Tapez STOP pour quitter l'édition")
		mot_ajouter = input("Entrez le mot à ajouter dans la liste "+theme_choisie+" : ")
		mot_ajouter = mot_ajouter.lower()
		if not mot_ajouter.isalpha():
			print("Choix invalide ! ")
			continue
		if mot_ajouter == "stop":
			continuer = False
			stop = 0
		if continuer == True:		
			if theme_choisie in dic_mot["mot"]:
				theme_existant = True
			else:
				theme_existant = False		
			if theme_existant:
				if mot_ajouter in dic_mot["mot"][theme_choisie]:
					print("Le mot ",mot_ajouter," est déja dans la liste.")
					continue 
				else:		
					dic_mot["mot"][theme_choisie].append(mot_ajouter)
					print("Le mot ",mot_ajouter," est maintenant dans la liste ",theme_choisie)
					print("\n\n")
			else:
				dic_mot["mot"][theme_choisie] =	list()	
				dic_mot["mot"][theme_choisie].append(mot_ajouter)
				print("Le mot ",mot_ajouter," est maintenant dans la liste ",theme_choisie)
				print("\n\n")
	return ajouter_mot_liste(dic_mot)			

def supprimer_mot_liste(dic_mot):
	autre_liste = 1
	while autre_liste == 1:
		choix_autre_liste = input("Voulez vous supprimer un mot d'une liste ? (o/n) : ")
		choix_autre_liste = choix_autre_liste.lower()
		if not choix_autre_liste.isalpha() or len(choix_autre_liste) !=1 :
			print("Choix invalide ! ")
			supprimer_mot_liste(dic_mot)
		if choix_autre_liste == "o":
			autre_liste = 0
		elif choix_autre_liste == "n":
			return	
	mot_juste = 1
	while mot_juste == 1:
		print("\nVoici la liste des thème : ")
		i = 1
		for mot in dic_mot["theme"]:
			print(i,"",mot.capitalize(),"(",len(dic_mot["mot"][mot]),"mots)")
			i += 1
		print("\n")	
		theme_choisie = input("Quelle est le nom de votre thème : ")
		theme_choisie = theme_choisie.lower()
		if theme_choisie.isdigit() and int(theme_choisie) > 0 and int(theme_choisie) < 1+len(dic_mot["theme"]):
			theme_choisie = dic_mot["theme"][int(theme_choisie)-1]
		elif not theme_choisie.isalpha() or len(theme_choisie) < 4 or not theme_choisie in dic_mot["mot"]:
			print("Choix invalide ! ")
			continue
		mot_juste = 0
	stop = 1
	continuer = True
	while stop == 1:
		print("Tapez STOP pour quitter l'édition")
		mot_ajouter = input("Entrez le mot à supprimer dans la liste "+theme_choisie+" : ")
		mot_ajouter = mot_ajouter.lower()
		if not mot_ajouter.isalpha():
			print("Choix invalide ! ")
			continue
		if mot_ajouter == "stop":
			continuer = False
			stop = 0
		if continuer == True:		
			if mot_ajouter in dic_mot["mot"][theme_choisie]:
				print("Le mot ",mot_ajouter," est supprimé de la liste",theme_choisie)
				dic_mot["mot"][theme_choisie].remove(mot_ajouter)
				if len(dic_mot["mot"][theme_choisie]) == 0:
					del dic_mot["mot"][theme_choisie]
					dic_mot["theme"].remove(theme_choisie)
					print("La liste est vide et a donc été supprimé")
					continuer = False
					stop = 0
					continue
				continue 
			else:		
				print("Le mot ",mot_ajouter," n'est pas dans la liste ",theme_choisie)
				print("\n\n")
	return supprimer_mot_liste(dic_mot)				



			






    	



    




		



			

			
			


