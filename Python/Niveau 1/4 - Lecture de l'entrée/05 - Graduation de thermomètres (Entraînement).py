# Étant données deux températures entières tempMin et tempMax, votre programme doit afficher
# toutes les températures comprises entre les deux, bornes incluses.

# Demander à l'utilisateur d'entrer la température minimale
tempMin = int(input())
# Demander à l'utilisateur d'entrer la température maximale
tempMax = int(input())
# Calculer la différence entre la température maximale et minimale, ajouté 1 pour inclure tempMax
différence = tempMax - tempMin + 1
# Utiliser une variable temporaire pour afficher les températures
tempAffichée = tempMin
# Utiliser une boucle pour afficher toutes les températures entre tempMin et tempMax
for loop in range(différence):
    # Afficher la température
    print(tempAffichée)
    # Augmenter la température affichée pour la prochaine itération
    tempAffichée = tempAffichée + 1
