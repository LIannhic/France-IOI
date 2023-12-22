# On vous décrit les arrivées et départs des participants d'une fête, et votre programme doit afficher
#  le nombre maximum de personnes qui ont été présentes au même moment. Chacun des invités est identifié
#  par un numéro.
# Le premier entier à lire est nbPersonnes : le nombre total de personnes qui se sont rendues à la fête.
#  Ensuite, il y a 2 × nbPersonnes entiers à lire, dans l'ordre chronologique des arrivées et départs.
#  Si l'entier est positif, c'est que la personne de numéro correspondant vient d'arriver,
#  s'il est négatif, elle vient de partir. Une fois qu'une personne est partie, elle ne revient pas.
# Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient là simultanément.

# Entrer le nombre total de personnes qui se sont rendues à la fête
nbPersonnes = int(input())
# Initier des compteurs de personnes à 0
compteur = 0
compteurMax = 0
# Faire une boucle pour entrer le numéro des personnes en entrées ou en sortie du double d'invités
for entrée_sortie in range(nbPersonnes * 2):
    numéro_personne = int(input())
    # Vérifier si le numéro de l'invité est positif et augmenter le compteur
    if numéro_personne > 0:
        compteur = compteur + 1
        # Vérifier si le compteur est plus grande que le compteur maximum.
        if compteur > compteurMax:
            # Si c'est le cas, remplacer la valeur du compteur maximum par celle du compteur
            compteurMax = compteur
    # Sinon diminuer le compteur
    else:
        compteur = compteur - 1
# Après la boucle afficher le compteur maximum
print(compteurMax)
