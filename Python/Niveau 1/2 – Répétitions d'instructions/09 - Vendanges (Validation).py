# Le champ est représenté ci-dessous :
#      1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
#    | R | . | . | . | . | . | . | . | . | . | . | . | . | . | . | C |
# Le robot est initialement tout à gauche, là où se trouve un grand tas de raisins. Il devra, 20 fois :
#     ramasser des raisins pour remplir la hotte de ramassage ;
#     se rendre à la charrette ;
#     déposer le contenu de la hotte ;
#     revenir au point de départ.
# Commandes pour cet exercice
#    Ici, vous allez :
#       Aller à gauche
#       Aller à droite
#       Ramasser les raisins
#       Déposer les raisins
# Ce qui correspond aux quatre instructions :
#   gauche()
#   droite()
#   ramasser()
#   deposer()

from robot import *

# Boucle fois 20
for loop in range(20):
   # ajout de la fonction ramasser les raisins
   ramasser()
   # Création d'une boucle fois 15 (départ à 1 et non 0)
   for loop in range(15):
      # Pour aller à droite vers la charette C
      droite()
    # Déposer les raisins
   deposer()
   # Création d'une boucle fois 15 
   for loop in range(15):
      #Pour aller à gauche vers le point de départ où se trouver les raisins
      gauche()
