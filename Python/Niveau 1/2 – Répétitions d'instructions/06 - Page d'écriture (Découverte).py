# Votre programme doit écrire 3 lignes, chacune contenant plusieurs fois de suite
#  une lettre suivie du caractère « _ » (sous-tiret en français) :
#  la lettre « a » sur la première ligne, la lettre « b » sur la deuxième et la lettre « c » sur la troisième.
# Vous disposez déjà d'un modèle où chaque ligne contient 4 lettres :
#   ↳
#   a_a_a_a_ 
#   b_b_b_b_
#   c_c_c_c_
# Cependant, vous vous dites qu'il serait mieux de mettre 30 lettres par ligne.
#  Écrivez un programme qui étend votre modèle. Bien sûr, vous utiliserez une boucle
#  pour ne pas vous fatiguer à écrire vous-même 30 fois chaque lettre.

# Créer un boucle fois 30
for loop in range(30):
   # Ajouter la fonction afficher a_ sans retour à la ligne
   print("a_", end = "")
# La fonction afficher vide sert à retourner à la ligne
print("")
# Répéter le processus avec les lettres b et c
for loop in range(30):
   print("b_", end = "")
print("")
for loop in range(30):
   print("c_", end = "")
print("")
