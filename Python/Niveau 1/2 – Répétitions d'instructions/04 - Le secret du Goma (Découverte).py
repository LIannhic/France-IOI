# L'allée centrale du village peut être représentée comme une série de 17 cases _ ,
# dont la plupart contiennent une bouse de Borlok . :
# R...............-
# Le robot R se trouve initialement dans la case de gauche. Il doit se déplacer case par case en allant
# vers la droite, et ramasser sur chaque case la bouse qui s'y trouve. Enfin, votre robot doit déposer
# tout ce qu'il a ramassé dans la boîte située sur la 17e case _ , tout à droite.
# Votre programme ne doit pas faire plus d'une dizaine de lignes.
# Commandes pour cet exercice
#   Pour résoudre ce problème, vous allez devoir :
#       Aller à gauche
#       Aller à droite
#       Ramasser une bouse
#       Déposer les bouses
#   Il s'agit donc à nouveau de :
#       gauche()
#       droite()
#       ramasser()
#       deposer()

from robot import *

# Créer une Boucle qui se répète 15 fois
for loop in range(15):
   # Ajouter les fonctions à répéter, aller à droite
   droite()
   # puis ramasser une bouse
   ramasser()
# Ajouter la fonction aller à droite en dehors de la boucle
droite()
# Ajouter la fonction déposer toutes les bouses
deposer()