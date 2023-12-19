# Il y a trois entiers à lire : la position de départ positionDepart,
#  la largeur d'un emplacement largeurEmplacement et le nombre de vendeurs nbVendeurs.
# Vous devez afficher une suite de nombres, partant de positionDepart et augmentant de largeurEmplacement
#  à chaque fois. Il y a au total nbVendeurs augmentations à faire. Vous devez afficher 
#  la valeur de chacun des nombres de la suite.

# Demander à l'utilisateur d'entrer la position de départ des stands
positionDépart = int(input())
# Demander à l'utilisateur d'entrer la largeur d'un emplacement
largeurEmplacement = int(input())
# Demander à l'utilisateur d'entrer le nombre de vendeurs
nbVendeurs = int(input())
# Initialiser la variable position de commencement d'un stan à la position de départ des stands
position = positionDépart
# Utiliser une boucle pour générer les positions de départ du stand de chaque vendeur
for loop in range(nbVendeurs + 1):
    # Afficher la position de départ du stand d'un vendeur
    print(position)
    # Augmenter la valeur de la position en fonction de la largeur de l'emplacement
    position = position + largeurEmplacement
