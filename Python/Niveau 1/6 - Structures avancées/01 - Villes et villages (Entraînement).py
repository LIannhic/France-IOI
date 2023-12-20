# On vous donne le nombre d'habitants d'un certain nombre de lieux que vous visitez. Une ville étant
#  un lieu dont la population est strictement supérieure à 10 000 habitants, déterminez combien de lieux
#  sont des villes.
# Votre programme doit lire un entier : le nombre de lieux. Il doit ensuite lire, pour chaque lieu,
#  un entier donnant le nombre de gens qui y habitent. Votre programme doit alors afficher le nombre de villes.

# Entrer le nombre de lieu visité
nombre_lieux = int(input())
# Initier le nombre de ville à 0
ville = 0
# Utiliser une boucle pour entrer le nombre d'habitant par lieu visité
for visite in range(nombre_lieux):
    nombre_habitants = int(input())
    # Vérifier si le nombre d'habitant est strictement supérieur à 10000
    if nombre_habitants > 10000:
        # Si vrai, alors ajouter 1 au nombre de ville
        ville = ville + 1
    print(visite)
# Afficher le nombre de ville
print(ville)
