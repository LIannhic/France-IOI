# On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un certain nombre
#  d'invités d'une fête. Écrivez un programme qui détermine combien d'invités ont été présents à un moment
#  de la période étudiée.
# Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de la période étudiée.
#  L'entier suivant, nbInvites, est le nombre total d'invités. Pour chaque invité, votre programme doit
#  ensuite lire deux entiers : sa date d'arrivée et de départ. Un invité est suspect si la période
#  à laquelle il a été présent intersecte la période étudiée. Votre programme doit afficher 
#  le nombre d'invités suspects.

# On demande à l'utilisateur d'entrer la date de début de la période étudiée
début_fête = int(input())
# On demande à l'utilisateur d'entrer la date de fin de la période étudiée
fin_fête = int(input())
# On demande à l'utilisateur d'entrer le nombre total d'invités
nbInvites = int(input())
# Compteur pour le nombre d'invités suspects
compteur = 0
# On parcourt la liste des invités
for période in range(nbInvites):
    # On demande à l'utilisateur d'entrer la date d'arrivée de l'invité
    arrivé_suspect = int(input())
    # On demande à l'utilisateur d'entrer la date de départ de l'invité
    départ_suspect = int(input())
    # On vérifie si l'invité est parti avant le début de la période étudiée
    parti_avant_fête = départ_suspect < début_fête
    # On vérifie si l'invité est arrivé après la fin de la période étudiée
    arrivé_après_fête = fin_fête < arrivé_suspect
    # On vérifie si l'invité est suspect (sa période de présence intersecte la période étudiée)
    if not ( parti_avant_fête or arrivé_après_fête ):
        # On augmente le compteur de 1
        compteur = compteur + 1
# On affiche le nombre d'invités suspects
print(compteur)
