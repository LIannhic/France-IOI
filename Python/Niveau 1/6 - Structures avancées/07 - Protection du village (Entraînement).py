# Le programme doit d'abord lire un entier strictement positif correspondant au nombre de maisons.
#  Ensuite, pour chaque maison, il doit lire la position horizontale (l'abscisse, le "x")
#  et sa position verticale (l'ordonnée, le "y") de cette maison. Toutes les abscisses et ordonnées
#  sont des entiers compris entre zéro et 1 million.
# Le programme doit alors afficher le périmètre de la plus petite clôture rectangulaire englobant
#  toutes les maisons. Ce rectangle doit avoir ses côtés parallèles aux axes du repère.

# Demander le nombre de maison à protéger
nombre_maison = int(input())
# Initialisez les valeurs minimales et maximales avec des valeurs extrêmes pour garantir
# la mise à jour correcte lors de la première itération.
abscisse_max = -1
abscisse_min = 1000001
ordonnee_max = -1
ordonnee_min = 1000001
# Utiliser une boucle pour demander la position d'une des maisons dans le repère
for loop in range(nombre_maison):
    abscisse = int(input())
    ordonnee = int(input())
    # Mettez à jour les valeurs minimales et maximales pour les abscisses et les ordonnées.
    if abscisse > abscisse_max:
        abscisse_max = abscisse
    if abscisse < abscisse_min:
        abscisse_min = abscisse
    if ordonnee > ordonnee_max:
        ordonnee_max = ordonnee
    if ordonnee < ordonnee_min:
        ordonnee_min = ordonnee
# Calculer les longueurs des côtés du rectangle englobant.
longueur_abscisse = abscisse_max - abscisse_min
longueur_ordonnee = ordonnee_max - ordonnee_min
# Calculer et affichez le périmètre du rectangle englobant.
perimetre = 2 * (longueur_abscisse + longueur_ordonnee)
print(perimetre)
