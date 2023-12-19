# Votre programme doit lire 20 entiers puis afficher la somme de tous ces entiers.

# Initialiser la variable nombre_cumulé à 0 pour stocker le nombre cumulatif total de karvas dans le village.
nombre_cumulé = 0
# Constante représentant le nombre de cheptels dans le village
CHEPTEL_VILLLAGE = 20
# Utiliser une boucle pour accumuler le nombre Karvas à travers chaque cheptel
for cheptel in range(CHEPTEL_VILLLAGE):
    # Demander à l'utilisateur d'entrer le nombre de karvas pour le cheptel actuel
    nombre_karvas = int(input())    
    # Ajouter le nombre de karvas au nombre cumulatif
    nombre_cumulé = nombre_cumulé + nombre_karvas
# Afficher le nombre cumulatif total de karvas dans le village
print(nombre_cumulé)
