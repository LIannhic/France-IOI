# Votre programme doit diriger le robot dans la rue schématisée ci-dessous :
#   #P-D-----------------------------M#
# La rue est représentée par 33 cases - entre deux murs # de briques. Votre robot se trouve au départ D
#  sur la 3e case. Votre programme doit le déplacer jusqu'à l'endroit où se trouve la personne âgée P,
#  au récipient d'eau en bleu, puis afficher précisément le texte "Bonjour, laissez-moi vous aider"
#  (avec un retour à la ligne à la fin de la phrase). Ensuite, il doit ramasser le récipient qui se trouve
#  sur cette même case, et avancer de 32 cases pour le déposer à la maison M. Il ne doit à aucun moment
#  se déplacer sur les cases contenant un mur # .
# Votre programme ne doit pas faire plus d'une vingtaine de lignes.
# Commandes pour cet exercice
#   Pour résoudre ce problème, le robot va devoir effectuer les opérations suivantes :
#       Aller à gauche
#       Aller à droite
#       Ramasser le récipient
#       Déposer le récipient
# Deux instructions permettent au robot de ramasser un objet qui se trouve au même emplacement que lui,
# et de déposer l'objet qu'il porte à l'endroit où il se trouve. Elles s'écrivent comme suit en Python :
#   ramasser()
#   deposer()
# Au final, vous devez donc utiliser ces quatre instructions pour résoudre ce problème :
#   gauche()
#   droite()
#   ramasser()
#   deposer()

from robot import *

# Boucle inutile, répéter la fonction aller à gauche deux fois
gauche()
gauche()
# Afficher le message demandé
print("Bonjour, laissez-moi vous aider")
# Ramasser le récipient
ramasser()
# Créer une boucle se répètant 32 fois
for loop in range(32):
   # Ajouter la fonction aller à droite
   droite()
# Sortir de la boucle ctrl + tab
deposer()
