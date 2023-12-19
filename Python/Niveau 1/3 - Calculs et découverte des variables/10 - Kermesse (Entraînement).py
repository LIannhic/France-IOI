# Toucher la cible au premier tir rapporte un bonbon, toucher la cible au deuxième tir rapporte deux bonbons
#  de plus, la toucher au troisième tir rapporte encore trois bonbons de plus, etc. Écrivez un programme qui
#  affiche sur la première ligne le nombre total de bonbons obtenus si l'on ne réussit qu'1 tir,
#  puis qui affiche sur la deuxième ligne le nombre de bonbons récupérés si l'on réussit 2 tirs de suite,
#  puis sur la troisième ligne le nombre de bonbons récupérés si l'on réussit 3 tirs de suite, etc.
#  jusqu'à la valeur que l'on peut récupérer si l'on réussit 50 tirs de suite.
#  Par exemple, si votre programme s'arrêtait à 5 et non à 50, il devrait afficher ceci :
#   ↳
#   1
#   3
#   6
#   10
#   15

# Déclarer la variable du total de bonbons gagnés
gain_cumulé = 0
# Déclarer la variable du nombre de bonbons gagnés à chaque tir avec la valeur de la première réussite
gain = 1
# Boucle 50 fois
for loop in range(50):
   # incrémenter les gains cumulés du nombre de gain à chaque tir réussi
   gain_cumulé = gain_cumulé + gain
   # afficher les gains cumulés
   print(gain_cumulé)
   # incrémenter les gains d'un tir réussi de 1
   gain = gain + 1
