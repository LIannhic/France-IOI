# Voici un exemple de socle :
#
#                                __  __  __  __  __  
#                              /                   /|__ 
#                             /                   //  /|__
#                            /                   //  //  /|
#                           /                   //  //  //
#                          /__  __  __  __  __ //  //  //   
#                         /|__  __  __  __  __|/  //  //
#                        /__  __  __  __  __  __ //  //  
#                       /|__  __  __  __  __  __|/  //
#                      /__  __  __  __  __  __  __ //    
#                      |__  __  __  __  __  __  __|/
#
# Pyramide formée de 3 marches carrées de tailles décroissantes
#
# Un socle est ainsi constitué d'étages, chaque étage ayant une hauteur égale à une unité et une base carrée.
#  Le côté des carrés diminue de une unité à chaque étage.
# Votre programme doit lire deux entiers, représentant respectivement la largeur du socle au niveau du sol
#  et la largeur du socle au niveau de la face supérieure du socle. Il doit ensuite calculer et afficher
# le volume du socle.

# Demander à l'utilisateur d'entrer la longueur du premier étage
longueur_premier_étage = int(input())
# Demander à l'utilisateur d'entrer la longueur du dernier étage
longueur_dernier_étage = int(input())
# Calculer la différence entre la longueur du premier et du dernier étage
différence = longueur_premier_étage - longueur_dernier_étage
# Initialiser la variable du volume total des étages à 0
volume_total = 0
# Initialiser la variable longueur_étage à la longueur du premier étage
longueur_étage = longueur_premier_étage
# Utiliser une boucle pour calculer le volume total des étages ajouté 1 pour inclure le dernier étage
for étage in range(différence + 1):
    # Calculer le volume de l'étage
    volume_étage = longueur_étage * longueur_étage * 1
    # Ajouter le volume de l'étage au volume total
    volume_total = volume_total + volume_étage
    # Diminuer la longueur de l'étage pour la prochaine itération
    longueur_étage = longueur_étage - 1
# Afficher le volume total des étages
print(volume_total)
