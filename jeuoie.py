import random
# Dé => se lancer

# Pion :
#  - forme
#  - position

# Joueur :
##  -> à un pion
##  -> jouer
##  -> avancer son pion

class De:
    """
    Représente un dé, permet de tirer un nombre aléatoire.
    Attributs :
      - nbFaces : le nombre de faces du dé
    Méthodes :
      - lancer() : renvoie un nombre aléatoire entre 1 et le nombre de faces
    """

    def __init__(self, nbFaces):
        """ Constructeur : initialise le nombre de faces"""
        self.nbFaces = nbFaces

    def lancer(self):
        """ Lance le dé : renvoie un nombre aléatoire entre 1 et le nombre de faces"""
        return random.randint(1, self.nbFaces)


class Pion:
    """
    Représente un point du jeu de l'oie : un point de couleur (une forme ascii ici) qui a une position pour sa case en case.
    Deux attributs :
      - forme : le caractère ascii qui représente le pion
      - position : un nombre qui indique sur quelle case se situe le pion
    """

    def __init__(self, forme):
        """ Constructeur de la classe : initialise la forme et le pose à la case 0"""
        self.forme = forme
        self.position = 0


class Joueur:
    """
    Représente un joueur du jeu de l'oie. Un joueur :
        -> à un pion
        -> peut jouer : lancer le dé et avancer son pion
        -> avancer son pion (lorsqu'il joue)

    Attributs :
      - pion : un objet de type Pion, le pion du joueur
      - nom : le nom du joueur
      - age : l'age du joueur

    Méthodes :
      - joueSonTour(de) : lance le dé passé en paramètre et avance le pion du nombre de cases fait par le dé
      - avancer(combien) : avance le pion de "combien" cases
      - aGagner() : renvoie un boolean, True si le joueur
      - caseCourante() : renvoie le numéro de la case courante sur laquelle est le pion du joueur
    """

    def __init__(self, nom, age, formePion):
        self.pion = Pion(formePion)
        self.nom = "Joueur "+nom
        self.age = age

    def joueSonTour(self, de):
        """ Joue son tour de jeu en lançant le dé passé en paramètre """
        resultatDe = de.lancer()
        self.avancer(resultatDe)

    def avancer(self, combien):
        """ Avance son pion du nombre de case passées en paramètre """
        self.pion.position += combien

    def aGagner(self):
        """ Vérifie si le joueur a gagné, c'est à dire à son pion au dela de la dernière case -> Hardcodé à 50 """
        return self.pion.position >= 50

    def caseCourante(self):
        """ Renvoie la case sur laquelle est le pion du joueur """
        return self.pion.position



