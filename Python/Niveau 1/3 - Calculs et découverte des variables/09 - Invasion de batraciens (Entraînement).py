# Sachant qu'il y a actuellement 1337 crapauds et que leur nombre double chaque semaine,
# votre programme devra afficher le nombre de crapauds qu'il y aura après la 12e semaine.
# Important : vous devez utiliser une boucle pour calculer le nombre de crapauds.

# Déclarer la variable du nombre de crapauds avec la valeur actuelle connue
crapauds = 1337
# Création une Boucle se répétant autant que le nombre de semaine
for loop in range(12):
   # Multiplication de la variable, comme leur nombre double chaque semaine
   crapauds = crapauds * 2
# Afficher la valeur du nombre de crapauds après douze semaines
print(crapauds)
