# Votre programme devra lire deux entiers, la superficie d'un champ des Arignon et la superficie
#  d'un champ des Evaran. Si l'un des champs est plus grand d'au moins 10 m² (strictement) que l'autre champ,
#  alors il faudra afficher le texte « La famille X a un champ trop grand », « X » devant bien sûr être
#  remplacé par « Arignon » ou « Evaran » selon le cas.

# L'utilisateur entre la superficie d'un champ de la famille Arignon
champArignon = int(input())
# L'utilisateur entre la superficie d'un champ de la famille Everan
champEvaran = int(input())
# Vérifier si la superficie du champ des Arignon est supérieur de plus de 10 m² de celui des Everan
if champArignon > champEvaran + 10:
    # Afficher le message demandé avec le nom de la famille Arignon
    print("La famille Arignon a un champ trop grand")
# Vérifier si la superficie du champ des Everan est supérieur de plus de 10 m² de celui des Arignon
if champEvaran > champArignon + 10:
    # Afficher le message demandé avec le nom de la famille Everan
    print("La famille Evaran a un champ trop grand")
