# Votre programme doit lire deux entiers, compris entre 1 et 6, la valeur de chaque dé.
#  Si la somme est supérieure ou égale à 10, alors vous devez payer une taxe spéciale (36 pièces).
#  Sinon, vous payez deux fois la somme des valeurs des deux dés. Votre programme devra afficher
#  selon le cas le texte « Taxe spéciale ! » ou bien « Taxe régulière »,
#  puis la somme à payer (sans indiquer l'unité).

# Demender à l'utilisateur la valeur sur la face un dé
face_dé_1 = int(input())
# Demender à l'utilisateur la valeur sur la face l'autre dé
face_dé_2 = int(input())
# Vérifier si la somme des dé est strictement inférieur à 9
if face_dé_1 + face_dé_2 > 9:
    # Afficher le message demandé
    print("Taxe spéciale !")
    # Et afficher le prix de passage
    print(36)
# Sinon...    
else:
    # ...afficher l'autre message demandé
    print("Taxe régulière")
    # Et Afficher le résultat du calcul du prix de passage
    print((face_dé_1 + face_dé_2) * 2)
