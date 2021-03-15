# Commentaire avant de coder:
# 1. mettre les bouts de code dans les parties correspondantes..
# .. Modules importés, Constantes, Variable globale, Fonction principale, Placement des widgets
# 2. Tout le code les algorithmes, les if, else, les conditions, etc... doivent être mis.. 
# ..dans les fonctions
# 3. nommer les constantes en majuscule, mettez une docstring au debut de chaque fonction ..
# et utiliser de bon noms, exemple creer_balle, LONGUEUR, etc...


######################################
##### Projet : incendie
##### Participants:
# Nour cherif
# Salah-Eddine Harnoufi
# Karim Maurel
# Léon
# issouf
# sissokho abdoulah
##### Groupe:
# td: 5
# Cm: 1
######################################

#####################################
# Modules importés: tkinter
import tkinter as tk

#####################################
# Constantes
LARGEUR = 700
HAUTEUR = 700

# Constantes correspondant a une durée
#DUREE_FEU = 
#DUREE_CENDRE = 


#####################################
# Variables globales (si besoin)

#####################################
# Fonctions principales

def clique_utilisateur():
    pass


#####################################
# Placement des widgets

canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid(column=0, row=0)


canvas.bind('<1>', clique_utilisateur)