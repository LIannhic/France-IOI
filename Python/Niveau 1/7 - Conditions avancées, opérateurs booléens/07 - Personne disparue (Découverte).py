# On vous donne un entier, le numéro d'une personne recherchée, puis un entier tailleListe,
#  et enfin tailleListe entiers parmi lesquels vous devez chercher le numéro de la personne.
#  Si le numéro est présent dans la liste (il peut l'être plusieurs fois) vous devez afficher
#  le texte "Sorti de la ville" sinon "Encore dans la ville".

# On demande à l'utilisateur d'entrer le numéro de la personne recherchée
numéro_personne_recherchée = int(input())
# On demande à l'utilisateur d'entrer la taille de la liste
tailleListe = int(input())
# Variable pour indiquer si le numéro de la personne recherchée a été trouvé dans la liste
est_sortie = False
# On parcourt la liste des sorties
for sortie in range(tailleListe):
    # On demande à l'utilisateur d'entrer un numéro de personne de la liste
    numéro_personne = int(input())
    # On vérifie si le numéro de la personne recherchée est égal au numéro de la personne dans la liste
    if numéro_personne_recherchée == numéro_personne:
        # Si c'est le cas, on met la variable 'sorti' à True
        est_sortie = True
# On affiche le texte en fonction de si la variable 'sortie' est vrai
if est_sortie:
    print("Sorti de la ville")
else:
    print("Encore dans la ville")
