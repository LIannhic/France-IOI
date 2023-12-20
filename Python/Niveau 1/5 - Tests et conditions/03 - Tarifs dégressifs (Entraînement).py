# Votre programme lira un entier, l'heure d'arrivée, qui sera compris entre 0 et 12 inclus.
#  0 correspond à midi, 1 à 1h de l'après-midi, etc. et 12 à minuit.
# Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque heure après midi.
#  Il est donc de 15 pièces à 13h, etc. Il ne peut cependant pas dépasser 53 pièces.
# Votre programme devra afficher le prix à payer correspondant à l'heure d'arrivée donnée.

# Demander à l'utilisateur l'heure d'arrivée
heure_arrivée = int(input())
# Calculer le prix de la chambre avec la formule donnée
prix = 10 + heure_arrivée * 5
# Vérifier si le prix n'exéde pas 53, le prix maximum de la chambre
if prix >= 53:
    # Si vrai, modifier le prix à son maximum
    prix = 53
# Afficher le prix de la chambre
print(prix)
