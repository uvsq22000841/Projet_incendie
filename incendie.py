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
# Modules importés: tkinter, random
import tkinter as tk
import random
from tkinter.constants import N

#####################################
# Constantes
LARGEUR = 700
HAUTEUR = 700

# Constantes correspondant a une durée
#DUREE_FEU = 
#DUREE_CENDRE = 

#####################################
# Variables globales (si besoin)

# types possible pour une passaerelle
type_passerelle = ['Eau', 'Forêt', 'Feu', 'Prairie', 'Cendres tièdes', 'Cendres éteintes']

# couleur possible

couleurs = ['blue', 'green', 'red', 'yellow', 'gray', 'black']

#variable qui enregistre les elements a changer a la fin du traitement de chaque simulation

liste_a_changer = []

#####################################
# Fonctions principales

def to_change(i, a, type_pas, couleur):
    '''enregistre toutes les elements a changer a la fin, dans une liste'''
    global liste_a_changer

    liste_a_changer.append([i, a, type_pas, couleur])

    print(liste_a_changer)

def change_tout():
    '''change tout les elements qui doivent être changer une fois toutes les passerelles vérifiés'''
    global liste_a_changer

    for element in liste_a_changer:
        tableau[ element[0] ][ element[1] ][1] = element[2]
        canvas.itemconfigure(tableau[ element[0] ][ element[1] ][0], fill=element[3])
        


def verifier_case_autour(i, a):
    '''verifier toutes les cases autour de prairiee'''
    global n, m
    # 8 cases autour à vérifier,  (i-1, a); (i-1,  a-1); (i-1, a+1); (i, a-1), (i, a+1)
    # (i+1, a); (i+1, a-1); (i+1, a+1)

    # pour ne pas être en dehors de la range du tableau
    z_n =  n-1
    z_m = m-1

    cpt = 0

    # quand on est pas au bord inferieur
    if a != z_m:
        if tableau[i][a+1][1] == "Feu":
            cpt += 1
        if i != 0:
            if tableau[i-1][a+1][1] == "Feu":
                cpt += 1
        if i != z_n:
            if tableau[i+1][a+1][1] == "Feu":
                cpt += 1

    # quand on est pas au bord supérieur
    if a != 0:
        if tableau[i][a-1][1] == "Feu":
            cpt += 1
        if i != 0:
            if tableau[i-1][a-1][1] == "Feu":
                cpt += 1
        if i != z_n:
            if tableau[i+1][a-1][1] == "Feu":
                cpt += 1

    #quand on est pas au bord lateral gauche
    if i != 0:
        if tableau[i-1][a][1] == "Feu":
            cpt += 1
    
    # bord lateral droit
    if i != z_n:
        if tableau[i+1][a][1] == "Feu":
            cpt += 1

    # si prairie a plus de 4 voisins feu
    if cpt >= 4:
        to_change(i, a, "Feu", "red")


def simulation():
    '''lance la simulation de l'incendie'''
    global n, m
    for i in range(0, n):
        for a in range(0, m):
            if tableau[i][a][1] == "Prairie":
                verifier_case_autour(i, a)


    # simulation finie on modifie les valeurs de chaque element
    change_tout()


def clique_utilisateur(event):
    '''recupere le clique de l'utilisateur et modifie la passerelle correspondant au clique'''
    global largeur_rec, hauteur_rec

    colonne = event.x // hauteur_rec
    ligne = event.y // largeur_rec

    if tableau[ligne][colonne][1] == "Forêt" or tableau[ligne][colonne][1] == "Prairie":

        canvas.itemconfigure(tableau[ligne][colonne][0], fill="red")

        tableau[ligne][colonne][1] = "Feu"


def type_aleatoire():
    '''renvoie un type aleatoire de passerelle'''
    global type_passerelle, couleurs

    nombre_aleatoire = random.randint(0, 5)



    return type_passerelle[nombre_aleatoire], couleurs[nombre_aleatoire]


def division_du_canvas(n, m):
    '''subdivise le canvas en partie égales'''
    global LARGEUR, HAUTEUR

    largeur_rec = LARGEUR//n
    hauteur_rec = HAUTEUR//m

    return largeur_rec, hauteur_rec


def quadrillage(n, m):
    '''creer le quadrillage contenant les pacerelles'''

    largeur_rec, hauteur_rec = division_du_canvas(n, m)

    tableau = []
    for i in range(0, n):
        tableau.append([])
        for a in range(0, m):
            type_pas, couleur_pas = type_aleatoire()

            tableau[i].append([canvas.create_rectangle((a*hauteur_rec, i*largeur_rec), ((a+1)*hauteur_rec, (i+1)*largeur_rec), fill=couleur_pas, outline="white"), type_pas])

    return tableau, largeur_rec, hauteur_rec, n, m
#####################################
# Placement des widgets

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid(column=0, row=0)

bouton = tk.Button(racine, text="Lancer simulation", command= lambda:simulation())
bouton.grid(column = 0, row =1)


tableau, largeur_rec, hauteur_rec, n, m = quadrillage(10, 20)




canvas.bind('<1>', clique_utilisateur)

racine.mainloop()
