# Écrivez un programme qui lit un numéro de mois algoréen, et affiche le nombre de jours de celui-ci.
#  Les Algoréens disposent de leur propre calendrier. Voici les informations dont vous avez besoin :
#
#    Numéro du mois 	Nombre de jours
#            1	               30
#            2	               30
#            3                 30
#            4	               31
#            5	               31
#            6	               31
#            7	               30
#            8	               30
#            9	               30
#           10	               31
#           11	               29

# Demander d'entrer un nombre entier à l'utilisateur
numero = int(input())
# Comparer à la possibilité unique du numéro des mois et afficher son résultat
if numero == 11:
   print(29)
#Sinon...
else:
   #...si, compararer à une autre possibilité du numéro des mois et afficher son résultat
   if ( (4 <= numero) and (numero <= 6) ) or (numero == 10):
      print(31)
    #...sinon, affacher la dernière possibilité
   else:
      print(30)
