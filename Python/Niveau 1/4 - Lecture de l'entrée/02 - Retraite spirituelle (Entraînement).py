# Votre programme devra lire un entier : le nombre de jours que dure la randonnée. Ensuite, il devra afficher
# le nombre de fois que l'incantation est répétée, sachant qu'elle est prononcée une fois par seconde
# pendant 16 heures par jour (les 8 autres heures, on dort !).

# Demander à l'utilisateur d'entrer le nombre de jours
nombre_jour = int(input())
# Calculer le total d'incantations sur la période de jours donnée
# (60 secondes/minute) * (60 minutes/heure) * (16 incantations/heure) * (nombre de jours)
total_incantation = 60 * 60 * 16 * nombre_jour
# Afficher le total d'incantations
print(total_incantation)
