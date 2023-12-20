# Votre programme doit lire un entier nbMarchands (non nul) puis les prix des marchands entiers suivants,
#  qui indiquent le prix des galettes chez chaque marchand, de la position 1 à la position nbMarchands.
#  Votre programme devra ensuite afficher la position du plus petit de ces prix.
#  En cas d'égalité entre deux prix, on prendra la position la plus grande. Tous les prix et positions
#  sont positifs et ne dépassent pas 1 million.

# Entrer le nombre de marchands dans la rue
nbmarchands = int(input())
# Initier le prix le plus haut possible de la galette la moins chère
prix_minimum = 1000 * 1000
# Initier la position du plus petit de ces prix avec une valeur fantaisiste
position_galette = -1
# Initier la position du marchand visité à 0  
position_marchand = 0
# Utiliser une boucle pour demander le prix de la galette chez chaque marchand
for marchand in range(nbmarchands):
   # Augmenter la position du marchand
   position_marchand = position_marchand + 1
   # Demander le prix de la galette
   prix = int(input())
   # Comparer si le prix de la galette est inférieur ou égale au pris de la galette la moins chère
   if prix <= prix_minimum:
      # Si vrai, changer le prix de la galette la moins chère
      prix_minimum = prix
      # Si vrai, retenir la position du marchand à la galette la moins chère
      position_galette = position_marchand
# Afficher la position voulue
print(position_galette)
