# L'algoréathlon se constitue de trois étapes à effectuer chaque jour :
#  2 km de natation, 34 km de cyclisme et 6 km de course à pied.
# Sachant qu'un sportif répète ces trois étapes pendant 3 jours de suite,
#  vous devez afficher la distance totale qu'il a parcourue à la fin du 1er jour,
#  à la fin du 2e jour, puis à la fin de l'algoréathlon complet.
# Afin de rendre l'affichage convivial sur l'écran du robot,
#  vous souhaitez mettre les trois valeurs sur une même ligne,
#  avec une espace entre chaque valeur et la suivante.
# Important : pour écrire ce programme, vous devez mémoriser la distance parcourue en un jour
# en lui donnant un nom, puis utiliser ce nom pour calculer les trois réponses.

# Attribuer des valeurs aux variables natation, cyclisme et course comme dans l'énoncer
natation = 2
cyclisme = 34
course = 6

# Nommer la distance parcourue pendant un jour et lui attribuer la somme des épreuves
parcours = natation + cyclisme + course

# Afficher la distance cumulée chaque jour à la suite
print(1 * parcours, end = " ")
print(2 * parcours, end = " ")
print(3 * parcours)
