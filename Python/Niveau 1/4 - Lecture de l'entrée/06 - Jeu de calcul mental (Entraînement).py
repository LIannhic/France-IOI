# Un nombre de départ va être donné par le chef du village. La personne qui suit doit le multiplier par 2,
#  puis la suivante doit multiplier le nombre obtenu par 3, celle d'encore après doit multiplier le résultat
#  par 4… jusqu'à ce que les nbNombres calculs aient été effectués.
# Le chef a choisi le nombre 66 pour démarrer le jeu. Votre programme lira l'entier nbNombres,
#  la quantité de nombres attendue par le jeu (nombre de départ inclus). Il devra ensuite afficher
#  tous les nombres de la partie afin de vous rendre imbattable !

# Demander à l'utilisateur d'entrer sa position
position = int(input())
# Constante représentant le nombre choisi du chef
CHOIXCHEF = 66
# Initialiser la variable tour à 1
tour = 1
# Calculer le résultat du premier tour
résultat = CHOIXCHEF * tour
# Utiliser une boucle pour générer les réponses jusqu'à la participation de l'utilisateur
for loop in range(position):
    # Afficher le résultat
    print(résultat)
    # Augmenter la valeur du tour pour la prochaine itération
    tour = tour + 1
    # Mettre à jour le résultat en fonction du tour dans la boucle
    résultat = résultat + (résultat * tour)
