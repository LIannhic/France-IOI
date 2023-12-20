# Il existe 4 types d'arbres :
#   le "Tinuviel" fait moins de 5 mètres de haut et ses feuilles sont composées de plus de 8 folioles
#   le "Calaelen" fait plus de 10 mètres de haut et ses feuilles sont composées de plus 10 folioles
#   le "Falarion" fait moins de 8 mètres de haut et ses feuilles sont composées de moins de 5 folioles
#   le "Dorthonion" fait plus de 12 mètres de haut et ses feuilles sont composées de moins de 7 folioles
# Votre programme lira deux entiers, la hauteur et le nombre de folioles de l'arbre,
#  et affichera le nom de l'arbre correspondant.
# Toutes les inégalités sont à prendre au sens large, c'est-à-dire que "moins" signifie "moins ou égal"
#  ou et "plus" signifie "plus ou égal".

# Entrer les valeurs de la hauteur et le nombre de folioles des arbres
hauteur = int(input())
folioles = int(input())
# Vérifier la hauteur puis le nombre de folioles avant s'afficher le nom de l'arbre
if (hauteur) <= 5:
    if(folioles) >= 8:
        print ("Tinuviel")
if (hauteur) >= 10:
    if (folioles) >= 10:
        print ("Calaelen")
if (hauteur) <= 8:
    if (folioles) <= 5:
        print ("Falarion")
if (hauteur) >= 12:
    if(folioles) <= 7:
        print ("Dorthonion")
