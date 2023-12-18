# On peut considérer qu'il y a trois zones dans la grotte :
#     zone 1 : le fond, où se trouvent les quatre cylindres, empilés du plus large au plus étroit ;
#     zone 2 : le centre, où vous pouvez placer temporairement des disques les uns au-dessus des autres ;
#     zone 3 : l'entrée de la grotte, où vous devez reformer l'empilement complet.
# Le but est de déplacer tous les disques de la zone 1 à la zone 3 en respectant ces deux règles :
#     on ne peut déplacer qu'un disque à la fois, car ils sont très lourds ;
#     on ne peut jamais poser un disque sur un disque plus petit que lui, car sinon l'empilement s'effondrerait !
#          __
#         |__|
#        |____|
#       |______|
#      |________|
#     |  zone 1  |  zone 2  |  zone 3  |
# Commandes pour cet exercice
#     Le robot peut exécuter cette instruction :
#     Déplacer zoneSource -> zoneDestination
#     Lorsqu'il la reçoit, le robot prend le disque se situant au sommet de la zone désignée par zoneSource et le place au sommet de la zone désignée par zoneDestination (au sol si la zone est vide).
#     Pour identifier une zone, écrivez à la place de zoneSource et zoneDestination le numéro de la zone concernée.
# En Python, l'instruction s'écrit :
#     deplacer(zoneSource, zoneDestination)
# N'oubliez pas d'inclure la ligne suivante en haut de votre programme pour l'utiliser :
#     from robot import *

from robot import *

deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(1, 2)
deplacer(3, 1)
deplacer(3, 2)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
deplacer(2, 1)
deplacer(3, 1)
deplacer(2, 3)
deplacer(1, 2)
deplacer(1, 3)
deplacer(2, 3)
