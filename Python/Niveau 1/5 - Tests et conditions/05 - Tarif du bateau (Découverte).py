# Votre programme doit lire l'âge d'une personne et afficher soit « Tarif réduit » si cette personne
#  a strictement moins de 21 ans, soit « Tarif plein » dans le cas contraire.

# Demander à l'utilisateur d'entrer un âge
âge = int(input())
# Vérifier si l'âge est strictement inférieur à 21 ans
if âge < 21:
   # Afficher la catégotrie de prix
   print("Tarif réduit")
# Sinon...
else:
   # ...afficher l'autre catégorie de prix
   print("Tarif plein")
