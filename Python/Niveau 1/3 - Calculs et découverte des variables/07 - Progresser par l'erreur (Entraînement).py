# Vous devez lire attentivement les programmes donnés ci-dessous pour déterminer s'ils sont valides ou non,
#  et ce sans essayer de les exécuter. Pour chacun des 7 programmes, vous devez afficher sur une ligne
#  soit la lettre « V » pour indiquer que le programme est valide, soit la lettre « I » pour indiquer
#  qu'il est invalide. Par exemple, si vous pensez que les 4 premiers programmes s'exécuteront sans erreur
#  et que les 3 suivants entraîneront des erreurs, faites afficher à votre programme :
#   ↳
#   V
#   V
#   V
#   V
#   I
#   I
#   I
# Voici les sept programmes.
# 1.  nbBillesRouges = 4
#     nbBillesBleues = 6
#     print(nbBillesRouges + nbBillesBleues)
# 2.  taille = 4
#     taille = 6
#     print(taille)
# 3.  nbBillesBleues = 3
#     print(nbBillesRouges)
# 4.  2 = 2
#     print(2)
# 5.  âge1 = 6
#     âge2 = 4
#     âge2 = âge1
#     print(âge2)
# 6.  prix = 10
#     prix - 2 = prix
#     print(prix)
# 7.  prix = âge - 7
#     âge = 12
#     print(prix)

# Le programme 1. est valide
print("V")
# Le programme 2. est valide
print("V")
# Le programme 3. n'est pas valide, la variable nbBillesRouges n'existe pas 
print("I")
# Le programme 4. n'est pas valide, un nombre ne peut pas être une variable
print("I")
# Le programme 5. est valide
print("V")
# Le programme 6. n'est pas valide, la modification d'une variable se fait à droite de signe égale
print("I")
# Le programme 7. n'est pas valide, la variable âge est déclarer après la variable prix 
print("I")
