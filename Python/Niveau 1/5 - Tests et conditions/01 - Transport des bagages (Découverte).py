# Votre programme lira deux entiers : le nombre de paquets et le poids d'un paquet.
#  Si le poids total est strictement supérieur à 105 kg, votre programme devra alors
#  afficher le texte « Surcharge ! ».

# Initialiser une variable pour le poids total à 0
total = 0
# Demander à l'utilisateur d'entrer le poids moyen de chaque paquets
charge = int(input())
# Demander à l'utilisateur d'entrer le nombre de paquets
paquet = int(input())
# calculer le poids total des paquets
total = charge * paquet
# Vérifier si le poids total dépasse la limite de 105 kg
if total > 105:
    # Afficher le message demandé
    print("Surcharge !")
