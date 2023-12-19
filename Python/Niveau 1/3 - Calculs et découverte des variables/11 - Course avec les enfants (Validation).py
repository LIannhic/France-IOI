# Votre robot R doit partir de la case de gauche, aller chercher les anneaux O dans l'ordre
#  (de gauche à droite) et les ramener un par un à la case de départ.
# Schéma avec les anneaux
#
#   ROOOOOOOOOO
#
# Commandes pour cet exercice
#   Ici encore, vous devrez faire :
#       Aller à gauche
#       Aller à droite
#       Ramasser l'anneau
#       Déposer l'anneau
# ce qui correspond aux instructions suivantes :
#   gauche()
#   droite()
#   ramasser()
#   deposer()

from robot import *

# Déclarer la variable de la distance de l'anneau le plus proche
distance = 1
# Boucle du nombre de fois où l'action devra se répéter, 10 
for loop in range(10):
   # Boucle de la distance à parcourir pour atteindre l'anneau le plus proche
   for loop in range(distance):
      # Aller à droite
      droite()
    # Ramasser l'anneau
   ramasser()
   # Boucle de la distance à parcourir pour revenir au point de départ
   for loop in range(distance):
      # Aller à gauche
      gauche()
    # Déposer l'anneau
   deposer()
   # Augmenter la distance jusqu'au prochain anneau
   distance = distance + 1
