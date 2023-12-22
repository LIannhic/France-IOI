# On vous donne un intervalle de temps pendant lequel on sait qu'un espion est arrivé,
#  puis la date d'arrivée d'un certain nombre de personnes. Déterminez combien de ces personnes
#  peuvent être cet espion.
# Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de l'intervalle
#  pendant lequel on sait que l'espion est arrivé en ville. Il doit ensuite lire un entier nbEntrées,
#  le nombre total de personnes entrées dans la ville, puis les nbEntrées nombres suivants qui
#  représentent les dates d'entrée (non triées) des différentes personnes.
# Votre programme doit afficher le nombre de personnes entrées entre les deux dates données, incluses.

# Entrer la date de début et la date de fin de l'intervalle puis le nombre total de personnes entrées
début_intervalle = int(input())
fin_intervalle = int(input())
nbEntrées = int(input())
# Initier la variable compteur à 0
compteur = 0
# Dans une boucle du nombre d'entrées saisir la date d'entrée des personnes
for personnes in range(nbEntrées):
    entrée_personnes = int(input())
    # Vérifier si la date d'entrée est entre les dates de début et de fin de l'intervalle
    if entrée_personnes >= début_intervalle and entrée_personnes <= fin_intervalle:
        # Si vrai, augmenter le compteur de 1
        compteur = compteur + 1
# Afficher la valeur du compteur
print(compteur)
