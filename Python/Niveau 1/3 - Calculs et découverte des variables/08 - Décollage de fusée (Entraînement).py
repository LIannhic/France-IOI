# Votre programme devra lancer le décompte en partant de 100 puis annoncer le décollage,
# c'est-à-dire afficher une séquence d'annonces de la forme :
#   ↳
#   100
#   99
#   ...
#   2
#   1
#   0
#   Décollage ! 
# en remplaçant les « … » par toutes les valeurs intermédiaires.
# Important : votre programme ne doit pas faire plus d'une quinzaine de lignes.

# Déclarer un varible et lui attribuer la première valeur voulue
décompte = 100
# Boucle de 100 plus 1 pour arriver à la valeur 0
for loop in range(101):
   # Afficher la valeur de la variable décompte
   print(décompte)
   # Décrémenter la variable décompte de 1
   décompte = décompte - 1
# Afficher le message pour conclure le décompte
print("Décollage !")
