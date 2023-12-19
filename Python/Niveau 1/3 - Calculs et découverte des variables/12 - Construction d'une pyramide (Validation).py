# L'objectif est de construire une tour à l'aide de petits cubes en bois, sachant que la forme de cette tour
#  consiste en un ensemble de grands cubes placés les uns au-dessus des autres. La base de la tour
#  est un cube de taille 17×17×17, c'est-à-dire composé de 17×17×17 = 4 913 petits cubes. Sur ce cube est posé
#  un autre cube de taille 15×15×15. Au-dessus de ce dernier se trouve un cube de 13×13×13. La tour continue
#  ainsi jusqu'à atteindre le sommet, qui consiste en un cube de taille 1×1×1.
# Dessin de la tour
#                              __ __   __
#                            /  /__ /|   /|     
#                           /   |__|/   / |  __
#                          /__  __  __ /  |    /|
#                         /|          |  /    / |
#                        / |          | /    /  |
#                       /  |__  __  __|/    /   |
#                      /__  __  __  __  __ /    |
#                      |                  |    /
#                      |                  |   /
#                      |                  |  /
#                      |                  | /
#                      |__  __  __  __  __|/

# Exemple d'une tour allant de 1×1×1 cubes à 5×5×5 cubes
# Votre programme doit calculer et afficher le nombre total de petits cubes nécessaires pour construire
# la pyramide. Effectuez les calculs dans le programme en y intégrant une boucle.

# Nombre de cudes utilisés par étage précédent
cumule_cubes = 0
# La longueur d'un étage en cube
longueur_étage = 1
# Boucle 9 fois, le total de nombre impair jusqu'à 17
for loop in range(9):
   # Total des cubes étage par étage plus le volume du nouvel étage
   cumule_cubes = cumule_cubes + longueur_étage * longueur_étage * longueur_étage
   # Augmentation au nombre impair suivant
   longueur_étage = longueur_étage + 2
# Afficher les cubes utilisés totals
print(cumule_cubes)