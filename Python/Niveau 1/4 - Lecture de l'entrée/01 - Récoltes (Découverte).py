# Votre programme doit lire un entier, qui représente la longueur du côté d'un champ carré en mètres.
#  Il doit ensuite afficher la masse que l'on pourra récolter de ce champ si l'on suppose que
#  la production sera de 23 kg par mètre carré.

# Demander à l'utilisateur d'entrer la longueur du champ
longueur_champ = int(input())
# Calculer l'aire du champ, l'aire d'un carré est côté par côté
aire_champ = longueur_champ * longueur_champ
# Déclarer la constante de rendement annuel par mètre carré
RENDEMENT = 23
# Calculer la production annuelle en multipliant l'aire du champ par le rendement annuel
production_annuelle = aire_champ * RENDEMENT
# Afficher la production annuelle
print(production_annuelle)
