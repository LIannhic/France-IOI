# Votre programme doit lire deux entiers, correspondant à deux numéros de bornes kilométriques,
#  et il doit afficher la distance séparant ces deux bornes. Notez que le résultat doit être
#  un nombre positif ou nul.

# Initialiser la variable pour stocker la différence
difference = 0
# Prendre l'entrée de l'utilisateur pour la valeur de la première borne
borne1 = int(input())
# Prendre l'entrée de l'utilisateur pour la valeur de la deuxième borne
borne2 = int(input())
# Calculer la différence entre les deux bornes
difference = borne1 - borne2
# Vérifier si la différence est possitive
if difference >= 0:
    # Si vrai, imprimer la différence
    print(difference)
# Vérifier si la différence est négative
if difference < 0:
    # Si vrai, calculer la différence absolue dans l'autre sens
    difference = borne2 - borne1
    # Imprimer la différence absolue
    print(difference)
