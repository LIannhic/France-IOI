# Vous devez écrire un programme qui détermine si deux soldats ont été de garde en même temps.
# Votre programme doit lire quatre entiers : la date du début et la date de fin (incluse)
#  du service du premier soldat puis celles du second soldat.
# Si les deux soldats ont, à un moment (même une seule seconde), été de garde en même temps
#  le programme devra écrire "Amis" et sinon "Pas amis".

# Entrer les informations demandés dans l'énoncé
date_début_garde1 = int(input())
date_fin_garde1 = int(input())
date_début_garde2 = int(input())
date_fin_garde2 = int(input())
# Comparer si la fin de la garde d'un soldat se termine avant le début de la garde de l'autre soldat ou inversement
if date_fin_garde2 < date_début_garde1 or date_fin_garde1 < date_début_garde2:
    # ...pour afficher Amis
    print("Pas amis")
#Sinon...
else:
    # ...afficher Pas amis
    print("Amis")
