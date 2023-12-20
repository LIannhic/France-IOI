# Votre programme doit d'abord lire un entier décrivant votre position actuelle sur la route,
#  sous la forme d'un nombre de kilomètres par rapport au début de la route. Ensuite, il doit lire
#  un entier donnant le nombre de villages. Pour chaque village, il doit lire un entier décrivant
#  la position de ce village le long de cette même route. Votre programme doit alors afficher
#  le nombre de villages qui se trouvent à une distance inférieure ou égale à 50 km de votre position actuelle.

# Lire la position actuelle sur la route
position = int(input())
# Lire le nombre de village
nombre_village = int(input())
# Initialiser le compteur de village proche
proche = 0
# Parcourir chaque village
for village in range(nombre_village):
    # Lire la position du village sur la route
    position_village = int(input())
    # calculer la distance entre la position actuel et la position du village
    distance = position - position_village
    # Vérifier si le résutat est négative
    if distance < 0:
        # Si vrai, inverser le résultat car distance est toujours positive 
        distance = -distance # moins par moins égale plus
    # Vérifier si la distance est inférieur ou égale à 50 
    if distance <= 50:
        # Augmenter le compteur de village proche de 1
        proche = proche + 1
# Afficher le nombre de village à une distance de 50 km ou moins de la position actuelle
print(proche)