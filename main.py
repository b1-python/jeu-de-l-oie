from jeuoie import *

# Création du dé qui va servir pour toute la partie
de = De(6)

# Création de trois joueurs
joueurs = [
    Joueur("toto", 5, "T"),
    Joueur("Lolo", 4, "L"),
    Joueur("Roger", 7, "R")
]

# Boucle du jeu : finDuJeu passera à True dès qu'un joueur aura gagné
finDuJeu = False
while not finDuJeu:

    # Tous les joueurs jouent chacun à leur tour
    for joueur in joueurs:
        joueur.joueSonTour(de)


    # Affiche le plateau
    for i in range(50):
        for joueur in joueurs:
            if(joueur.caseCourante() == i):
                print(joueur.pion.forme, end="")
        print(".", end=" ")
    print()

    # Vérifier si un joueur a gagne
    for joueur in joueurs:
        if joueur.aGagner(): finDuJeu = True

    # Un petit input à la fin pour stopper la boucle et éviter que tout se déroule trop vite...
    print("...")
    input()