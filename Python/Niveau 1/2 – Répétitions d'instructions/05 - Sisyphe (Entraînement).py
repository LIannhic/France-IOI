# Programmez votre robot pour qu'il mène le rocher tout en haut des 21 marches de la pyramide
# et redescende ensuite tout en bas. Par exemple, si la pyramide ne faisait que deux marches de haut,
# votre robot devrait effectuer le trajet illustré ci-dessous :
# haut, droite, haut, droite, gauche, bas, gauche, bas.
#
#            → ←          __
#         → ↑ ← ↓      __|__|__
#        ↑   ↓        |__|__|__|
# Commandes pour cet exercice
#   Utilisez les quatre instructions ci-dessous pour déplacer le robot de case en case
#   dans les différentes directions :
#       haut()
#       bas()
#       gauche()
#       droite()
# N'oubliez pas d'inclure la ligne suivante en haut de votre programme pour utiliser ces commandes :
#   from robot import *

from robot import *

# Créer une boucle d'autant que le nombre de marches de la pyramide
for loop in range(21):
   # Ajouter les fonctions dans la boucles pour monter une marche depuis la gauche
   # D'abord la fonction monter 
   haut()
   # Puis aller à droite
   droite()
# Créer une autre boucle d'autant que le nombre de marches de la pyramide 
for loop in range(21):
   # Ajouter les fonctions dans la boucles pour descendre la pyramide vers la gauche
   # D'abord la fonction aller à gauche
   gauche()
   # Puis descendre
   bas()
