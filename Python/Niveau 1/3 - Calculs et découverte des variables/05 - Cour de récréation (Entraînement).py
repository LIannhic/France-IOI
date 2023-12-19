# La cour carrée a été mesurée avec quatre bâtons de longueurs respectives 17 m, 7 m, 5 m et 2 m.
#  La longueur du côté de la cour est égale à 5 fois le premier bâton plus 2 fois le second plus
#  1 fois le troisième plus 2 fois le quatrième.
# Votre programme doit afficher deux lignes : la première doit contenir la surface de la cour,
#  et la seconde ligne doit contenir son périmètre. Les résultats doivent être exprimés en mètres carrés
#  et en mètres, respectivement, mais vous ne devez pas afficher l'unité après la valeur numérique.
# Important : dans votre programme, commencez par calculer la longueur du côté de la cour 
#  et l'enregistrer dans une variable.

# Attribuer des valeurs aux variables des bâtons
premier_bâton = 17
deuxième_bâton = 7
troisième_bâton = 5
quatrième_bâton = 2

# Attribuer une valeur à la longueur de la cours d'après l'énoncé
longueur_cours = premier_bâton * 5 + deuxième_bâton * 2 + troisième_bâton * 1 + quatrième_bâton * 2

# Afficher l'aire de la cours, aire d'un carré est côté fois côté
print(longueur_cours * longueur_cours)

# Afficher le périmètre de la cours, périmètre d'un est côté fois quatre
print(longueur_cours * 4)
