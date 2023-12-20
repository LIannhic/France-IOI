# Votre programme doit d'abord lire un entier strictement positif, le nombre de jours de marche effectués
#  jusqu'à présent. Il doit ensuite lire, pour chaque jour, la distance parcourue ce jour-là.
#  Il doit alors afficher la distance maximale parcourue en une journée.

# Initier la distance maximum parcourue en un jour à 0
distance_max = 0
# Demander le nombre de jour marche
nombre_jours_marche = int(input())
# Utiliser une boucle pour demander la distance parcourue chaque jour
for jour in range(nombre_jours_marche):
    distance_parcourue = int(input())
    # Vérifier si la distance parcourue est stricement plus grande que la distance maximum
    if distance_parcourue > distance_max:
        # Si vrai, attribuer à la distance maximum la valeur de la distance du jour 
        distance_max = distance_parcourue
# Afficher la distance maximum parcourue durant ces jours de marche
print(distance_max)
