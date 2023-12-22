# Sur une table est placée une feuille de papier rectangulaire de 90 cm de large et 70 cm de haut,
#  composée de zones de différentes couleurs, comme le décrit la figure ci-dessous. Un certain nombre
#  de personnes placent l'une après l'autre un jeton où elles le souhaitent sur la table, à l'exception
#  des frontières entre les différentes zones.
#
# JJJJJJJJJJJJJJJJJJ 
# JJJJJJJJJJJJJJJJJJ
# JJBBBBBBBBBBBBBBBJ
# JJBBBBBBBBBBBBBBBJ
# JJBBBJJJJJBBBBBBBJ
# JJBBBJJJJJBBBBBBBJ
# JJBBBJJJJJBBBBBBBJ
# JJBBBJJJJJBBBBBBBJ
# JJBBBJJJJJBBBBBBBJ
# JJBBBBBBBBBBBBBBBJ
# JJBBBBBBBBBBBBBBBJ
# JJJJJJJJJJJJJJJJJJ
# JJJRRRRRRJJJRRRRRJ
# JJJRRRRRRJJJRRRRRJ
#
# On vous donne en entrée le nombre de jetons qui ont été déposés, puis, pour chaque jeton,
#  ses coordonnées sur la feuille par rapport à l'origine en haut à gauche, sous la forme d'une abscisse et
#  d'une ordonnée entre −1 000 et 1 000.
# Votre programme devra qualifier chaque jeton avec l'un des textes suivants, en fonction de la couleur
#  sur laquelle il se trouve :
#     « En dehors de la feuille »
#     « Dans une zone jaune »
#     « Dans une zone bleue »
#     « Dans une zone rouge »
# Essayez d'écrire votre programme de sorte qu'il y ait au maximum une condition par possibilité de
#  texte affiché.

# Répertorier les coordonnées des différentes zones: 
#coordonnée premier rectangle rouge
xMinRouge1 = 15
xMaxRouge1 = 45
yMinRouge1 = 60
yMaxRouge1 = 70
#coordonnée deuxième rectangle rouge
xMinRouge2 = 60
xMaxRouge2 = 85
yMinRouge2 = 60
yMaxRouge2 = 70
#coordonnée petit rectangle jaune
xMinPetitJaune = 25
xMaxPetitJaune = 50
yMinPetitJaune = 20
yMaxPetitJaune = 45
#coordonnée rectangle bleu et petit jaune
xMinBleuJaune = 10
xMaxBleuJaune = 85
yMinBleuJaune = 10
yMaxBleuJaune = 55
#coordonnée feuille
xMinFeuille = 0
xMaxFeuille = 90
yMinFeuille = 0
yMaxFeuille = 70
# Itérer les coordonnées à vérifier par nombre de cas
nbcas = int(input())
for loop in range(nbcas):
    x = int(input())
    y = int(input())
    # Décrire les cas possibles
    dansRouge1 = (x > xMinRouge1 and x < xMaxRouge1) and (y > yMinRouge1 and y < yMaxRouge1)
    dansRouge2 = (x > xMinRouge2 and x < xMaxRouge2) and (y > yMinRouge2 and y < yMaxRouge2)
    dansRouge = dansRouge1 or dansRouge2
    dansPetitJaune = (x > xMinPetitJaune and x < xMaxPetitJaune) and (y > yMinPetitJaune and y < yMaxPetitJaune)
    dansBleuJaune =  (x > xMinBleuJaune and x < xMaxBleuJaune) and (y > yMinBleuJaune and y < yMaxBleuJaune)
    dansBleu = dansBleuJaune and not dansPetitJaune
    dansFeuille = (x > xMinFeuille and x < xMaxFeuille) and (y > yMinFeuille and y < yMaxFeuille)
    horsFeuille = not dansFeuille
    # Vérifier les cas possibles
    if dansRouge:
        print("Dans une zone rouge")
    elif dansBleu:
        print("Dans une zone bleue")
    elif horsFeuille:
        print("En dehors de la feuille")
    else:
        print("Dans une zone jaune")
