# Votre programme doit lire la description de plusieurs paires de zones rectangulaires, et pour chacune,
#  déterminer si les deux rectangles s'intersectent.
# Vous devez lire un premier entier, le nombre de paires de zones que votre programme devra tester.
#  Ensuite, pour chaque paire possible, deux zones rectangulaires et parallèles aux axes vous sont données
#  l'une après l'autre. Chaque zone est décrite par 4 entiers : son abscisse minimale et maximale puis
#  son ordonnée minimale et maximale.

# Entrer le nombre de rectangle à comparer dans une boucle pour entrer leurs coordonnées
nombre_paires = int(input())
for comparaison in range(nombre_paires):
   x1_min = int(input())
   x1_max = int(input())
   y1_min = int(input())
   y1_max = int(input())
   x2_min = int(input())
   x2_max = int(input())
   y2_min = int(input())
   y2_max = int(input())
   # Vérifier si que les rectangles se ne se chevauchent pas sur les axes du repère puis afficher NON  
   if (x1_max <= x2_min) or (x2_max <= x1_min) or (y1_max <= y2_min) or (y2_max <= y1_min):
      print("NON")
    # Sinon afficher OUI
   else:
      print("OUI")
