# Voici à quoi ressemble la table de multiplication allant jusqu'à 5 fois 5.
#   ↳
#   1  2  3  4  5
#   2  4  6  8 10
#   3  6  9 12 15
#   4  8 12 16 20
#   5 10 15 20 25
# Écrivez un programme qui affiche une table de multiplication allant jusqu'à 20 fois 20.

# Définir une variable nombre
nombre = 0
# Définir une variable quotion à 1 la première multiplication à faire
quotion = 1
# Boucle de 20 fois le nombre de ligne 
for loop in range(20):
    # Augmenter de 1 le nombre à multiplier
    nombre = nombre + 1
    # Boucle de 20 fois les multiplications dans une ligne
    for loop in range(20):
        # Afficher la multiplication à la ligne avec un espace
        print(nombre * quotion, end = " ")
        # Augmenter le quotion de 1
        quotion = quotion + 1
    # Réinitialiser le quotion
    quotion = 1
    # Retour à la ligne
    print()