# Le palais est un grand carré de taille 10×10, et le robot se trouve au départ
#  dans le coin en bas à gauche, comme représenté ci-dessous :
# Grille du palais
# ___ __ __ __ __ __ __ __ __ __
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |__|__|__|__|__|__|__|__|__|__|
# |R_|__|__|__|__|__|__|__|__|__|
#
# Votre robot doit passer une et une seule fois dans chacune des pièces,
#  puis se retrouver dans sa case de départ.
# Commandes pour cet exercice
#   Les quatre instructions ci-dessous permettent de déplacer le robot d'une case dans une direction.
#       haut()
#       bas()
#       gauche()
#       droite()

from robot import *

# Aller à droite d'une case pour se positionner afin de pouvoir répéter un motif
droite()
# Créer une boucle fois 4 et non fois 5 qui ferait sortir le robot du palais 
for loop in range(4):
   # indenter une boucle du reste de la distance à parcourir
   for loop in range(8):
      # Aller à droite
      droite()
    # Aller en haut d'une case
   haut()
   # indenter une autre boucle pour le retour
   for loop in range(8):
      # Aller à gauche
      gauche()
    # Aller encore en haut d'une case
   haut()
# Répéter le processus de la boucle fois 4 sans aller en haut
for loop in range(8):
   droite()
haut()
# Augmenter d'une case 
for loop in range(8 + 1):
   gauche()
# Dernière boucle pour parcourir la dernière distance de 9 cases vers le point de départ
for loop in range(9):
   # Aller en bas
   bas()