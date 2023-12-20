# Votre programme devra lire un premier entier : le nombre de membres nbMembres qui constituent une équipe.
#  Ensuite, il devra lire les poids (en kilogrammes), au total nbMembres × 2, sachant que le premier poids
#  est celui d'un joueur de la 1re équipe, le deuxième poids celui d'un joueur de la 2e équipe,
#  le troisième la 1re équipe, le quatrième la 2e équipe, etc.
# Après avoir calculé le poids total de chaque équipe, vous devrez afficher le texte
#  « L'équipe X a un avantage » (en remplaçant X par la valeur 1 ou 2), en considérant qu'une équipe
#  est avantagée si elle a un poids total supérieur à celui de l'autre.
# Vous afficherez ensuite le texte « Poids total pour l'équipe 1 : » suivi du poids de l'équipe 1,
#  puis « Poids total pour l'équipe 2 : » suivi du poids de l'équipe 2.

# Demander le nombre de membres qui constituent une équipe
nbMembres = int(input())
# Initier le poids total des membres de l'équipe 1
total_équipe1 = 0
# Initier le poids total des membres de l'équipe 2
total_équipe2 = 0
# Utiliser une boucle du nombre de membres par équipe pour demander le poids des membres et les additionner
for loop in range(nbMembres):
   # Demander le poids d'un membre de l'équipe 1
   poids1 = int(input())
   # Demander le poids d'un membre de l'équipe 2
   poids2 = int(input())
   # Additionner le poids donné au total des poids de l'équipe 1
   total_équipe1 = total_équipe1 + poids1
   # Additionner le poids donné au total des poids de l'équipe 2
   total_équipe2 = total_équipe2 + poids2
# Vérifier si le poids de l'équipe 1 est strictement supérieur au poids de l'équipe 2
if total_équipe1 > total_équipe2:
   # Afficher le message demandé
   print("L'équipe 1 a un avantage")
# Sinon et même si il y a une égalité
else:
   # Afficher l'autre message demandé
   print("L'équipe 2 a un avantage")
# Afficher le poids de l'équipe 1
print("Poids total pour l'équipe 1 :", total_équipe1)
# Afficher le poids de l'équipe 2
print("Poids total pour l'équipe 2 :", total_équipe2)
