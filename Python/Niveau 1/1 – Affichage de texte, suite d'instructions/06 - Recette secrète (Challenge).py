# Vous vous trouvez devant une source d'eau qui jaillit de la montagne, et vous disposez de deux tonneaux 
# vides de capacités 5 litres et 3 litres. Écrivez un programme qui effectue une série de transvasements 
# permettant d'obtenir exactement 4 litres d'eau dans le plus grand tonneau.
# Arrêtez-vous bien dès que le grand tonneau contient exactement 4 litres.
#
#     |       |5
#     |       |4
#     |       |3     |       |3
#     |       |2     |       |2
#     |_______|1     |_______|1
#     
# Commandes pour cet exercice
#     Pour doser l'eau dans les tonneaux, vous disposez de ces trois instructions :
#         Remplir tonneau
#         Vider tonneau
#         Transférer tonneauSource -> tonneauDestination
# Pour identifier un tonneau à l'emplacement de tonneau, tonneauSource ou tonneauDestination,
#  utilisez sa contenance : 3 ou 5.
# Quand on transvase un tonneau dans l'autre, on s'arrête lorsque le tonneau source est vide ou 
#  lorsque le tonneau destination est plein à ras bord. Ainsi, après chaque opération,
#  on peut savoir exactement combien de litres d'eau se trouvent dans les deux tonneaux.
# En Python, les trois instructions s'écrivent comme suit :
#     remplir(tonneau)
#     vider(tonneau)
#     transferer(tonneauSource, tonneauDestination)

from robot import *

remplir(5)
transferer(5, 3)
vider(3)
transferer(5, 3)
remplir(5)
transferer(5, 3)
