# Votre programme doit lire entier : un nombre de personnes à considérer. Ensuite, pour chaque personne,
#  il doit lire son signalement sous la forme de cinq entiers : sa taille en centimètres, son âge en années,
#  son poids en kilogrammes, un entier valant 1 si la personne possède un cheval et 0 sinon,
#  et un entier valant 1 si la personne à les cheveux bruns et 0 sinon.
# On veut déterminer pour chaque personne à quel point elle correspond aux 5 critères suivants :
#     il aurait une taille supérieure ou égale à 178 cm et inférieure ou égale à 182 cm ;
#     il aurait au moins 34 ans ;
#     il pèserait strictement moins de 70 kg ;
#     il n'a pas de cheval ;
#     il a les cheveux bruns.
# Lorsque cela n'est pas précisé explicitement, les inégalités sont au sens large.
# Pour chaque personne, vous devez tester tous les critères. S'ils sont vérifiés tous les 5,
#  vous devez afficher « Très probable ». Si seulement 3 ou 4 sont vérifiés, vous devez afficher « Probable ».
#  Si aucun n'est vérifié, vous devez afficher « Impossible », et dans les autres cas,
#  vous devez afficher « Peu probable ».


# Entrer le nombre de supect à controller et entrer autant de fois les 5 critères demandés 
nbsuspect = int(input())
for loop in range(nbsuspect):
    tailleSuspect = int(input())
    ageSuspect = int(input())
    poidsSuspect = int(input())
    cavalier = int(input())
    chevelure = int(input())
    # Initialisation à 0 du compteur de critères vérifiés à chaque boucle
    criteres = 0
    # Vérification de chaque critère et incrémentation du compteur si le critère est vérifié.
    if 178 <= tailleSuspect <= 182:
        criteres = criteres + 1
    if ageSuspect >= 34:
        criteres = criteres + 1
    if poidsSuspect < 70:
        criteres = criteres + 1
    if cavalier == 0:
        criteres = criteres + 1
    if chevelure == 1:
        criteres = criteres + 1
    # Affichage du résultat en fonction du nombre de critères vérifiés.
    if criteres == 5:
        print("Très probable")
    elif criteres >= 3:
        print("Probable")
    elif criteres == 0:
        print("Impossible")
    else:
        print("Peu probable")
