# Votre programme doit lire un entier : le code fourni par l'utilisateur. Si ce code correspond au code secret,
#  qui est 64 741, alors le programme devra afficher le texte « Bon festin ! ».
#  Sinon, il devra afficher « Allez-vous en ! ». 

# Demander à l'utilisateur d'écrire un nombre
proposition = int(input())
# Vérifier si le nombre proposé est différent du code secret
if proposition != 64741:
   # Afficher le refus
   print("Allez-vous en !")
# Sinon afficher l'accord
else:
   print("Bon festin !")
