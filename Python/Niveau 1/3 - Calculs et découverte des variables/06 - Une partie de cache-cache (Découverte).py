# Le robot devra compter jusqu'à 100, c'est à dire afficher les entiers de 1 à 100, un par ligne,
#  et ensuite afficher « J'arrive ! ». Ainsi, s'il ne devait compter que jusqu'à 3 au lieu de 100,
#  votre robot devrait afficher :
#   ↳
#   1
#   2
#   3
#   J'arrive !
# Important : votre programme ne doit pas faire plus d'une quinzaine de lignes.

# Créer une variable compte et lui attribuer la première valeur
compte = 1
# Boucle fois 100
for loop in range(100):
   # Afficher la valeur de la variable compte
   print(compte)
   # Incrémenter la valeur de la variable compte de un
   compte = compte + 1
# Afficher le message concluant le compte
print("J'arrive !")