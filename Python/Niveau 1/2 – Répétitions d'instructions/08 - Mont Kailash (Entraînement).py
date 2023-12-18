# Votre robot doit faire 108 fois le tour du chemin vert représenté ci-dessous,
# en tournant dans le sens des aiguilles d'une montre.
#   ################
#   #              #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   # ############ #
#   #D             #
#   ################
# Le robot D se trouve initialement en bas à gauche.
#  Chaque case représente 1 km, donc pour faire un tour, le robot doit se déplacer
#  successivement de 13 km dans chacune des 4 directions.
# Commandes pour cet exercice
#   Utilisez les quatre instructions ci-dessous pour déplacer le robot d'une case dans une direction :
#       haut()
#       bas()
#       gauche()
#       droite()
# N'oubliez pas d'écrire en début de programme la ligne :
#    from robot import *.

from robot import *

# Créer un boucle fois 108 pour chaque tour demandé
for loop in range(108):
   # Indenter une première boucle fois 13 pour parcourir la première distance
   for loop in range(13):
      # Ajouter la aller en haut pour suivre le sens des aiguilles
      haut()
    # Répéter processus trois fois pour les trois distances droite, bas et gauche dans l'ordre 
   for loop in range(13):
      droite()
   for loop in range(13):
      bas()
   for loop in range(13):
      gauche()