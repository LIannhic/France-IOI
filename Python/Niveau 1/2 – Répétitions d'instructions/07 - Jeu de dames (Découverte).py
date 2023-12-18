# Un damier de dimension 4×4 peut se représenter sous la forme suivante :
#   ↳
#   OXOX
#   XOXO
#   OXOX
#   XOXO
# Votre programme doit afficher un damier de taille 40×40.
# Assurez-vous bien que la case tout en haut à gauche contienne un « O »,
# comme c'est le cas dans le damier ci-dessus.

# Créer une boucle se répétant 20 fois
# car la première ligne et la deuxième vont répéter d'autant pour un motif sur 40 lignes
for loop in range(20):
   # Indenter une première boucle fois 20 pour répéter le première motif à deux caractères d'un total de 40
   for loop in range(20):
        # Utiliser la fonction afficher le motif OX sans retour à la ligne
        print("OX", end = "")
    # Utiliser la fonction afficher vide pour retourner à la ligne
   print()
   # Indenter une deuxième boucle fois 20 pour répéter le deuxième motif à deux caractères d'un total de 40
   for loop in range(20):
      # Utiliser la fonction afficher le motif XO sans retour à la ligne
      print("XO", end = "")
    # Utiliser la fonction afficher vide pour retourner à la ligne
   print()