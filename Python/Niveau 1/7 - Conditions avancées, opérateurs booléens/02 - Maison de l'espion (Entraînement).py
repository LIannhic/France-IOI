# On vous décrit une zone de recherche rectangulaire, parallèle aux axes, puis la position
#  d'un certain nombre de maisons. Écrivez un programme qui détermine combien de maisons sont dans cette zone.
# Votre programme devra lire, dans l'ordre : l'abscisse minimale, l'abscisse maximale,
#  l'ordonnée minimale et l'ordonnée maximale du rectangle. Il lira ensuite le nombre total de maisons,
#  puis pour chaque maison, son abscisse et son ordonnée.
# Votre programme devra déterminer puis afficher le nombre de maisons qui se trouvent
#  dans la zone de recherche. Si une maison est exactement sur le bord de la zone, elle doit ête comptée.

# Demander les informations de l'énoncé
abscisse_minimale = int(input())
abscisse_maximale = int(input())
ordonnée_minimale = int(input())
ordonnée_maximale = int(input())
nombre_maison = int(input())
# Initier un compteur à 0
compteur = 0
# Dans une boucle du nombre de maison, entrer les coordonnée d'une maison
for maison in range(nombre_maison):
    abscisse = int(input())
    ordonnée = int(input())
    # Vérifier si l'abscisse est compris entre l'intervalle des abscisses minimum et maximum
    if abscisse >= abscisse_minimale and abscisse <= abscisse_maximale:
        # Puis vérifier si l'ordonnée est compris entre l'intervalle des ordonnées minimum et maximum
        if ordonnée >= ordonnée_minimale and ordonnée <= ordonnée_maximale:
            # Si vrai, augmenter le compteur de 1
            compteur = compteur + 1
# Afficher la valeur du compteur
print(compteur)
