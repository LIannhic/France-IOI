# Votre programme doit d'abord lire le nombre de Karvas en compétition. Ensuite, pour chaque Karva, il doit :
#     lire 4 entiers : son poids, son âge, la longueur de ses cornes et la hauteur au garrot ;
#     afficher sa note, sachant qu'elle s'obtient en multipliant la longueur des cornes par
#     la hauteur au garrot, valeur à laquelle on ajoute le poids.

# Demander à l'utilisateur d'entrer le nombre de kravas
nombre_kravas = int(input())
# Utiliser une boucle pour chaque kravas
for kravas in range(nombre_kravas):
    # Demander à l'utilisateur d'entrer le poids, l'âge, la longueur des cornes et la hauteur du garrot
    poids = int(input())
    âge = int(input())
    longueur_cornes = int(input())
    hauteur_garrot = int(input())
    # Calculer la note en utilisant la formule donnée
    note = longueur_cornes * hauteur_garrot + poids
    # Afficher la note pour chaque kravas
    print(note)
