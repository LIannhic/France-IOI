# Une chambre ne coûte rien si on a 60 ans (l'âge de l'aubergiste !) et 5 écus si on a strictement
#  moins de 10 ans. Pour les autres personnes c'est 30 écus plus un supplément de 10 écus
#  si on a au moins 20 kilos de bagages.
# Votre programme doit lire deux entiers, l'âge et le poids des bagages de la personne
#  et doit afficher le prix, sous la forme d'un entier.

# Déclarer les constantes
AGE_AUBERGISTE = 60
PRIX_AMI = 0
PRIX_RÉDUIT = 5
PRIX_NORMAL = 30
SUPPLÉMENT = 10
PRIX_MAJORÉ = PRIX_NORMAL + SUPPLÉMENT
# Entre l'âge et le poids des bagages
votre_age = int(input())
poids_de_vos_bagages = int(input())
# Vérifier si l'âge saisi est strictement inférieur à 10 ans
if votre_age < 10:
   # Si vrai, afficher le prix réduit
   print(PRIX_RÉDUIT)
# Sinon...
else:
   # ...comparer l'âge saisi à l'âge de l'aubergiste
   if votre_age == AGE_AUBERGISTE:
      # Si vrai, afficher le pris d'ami
      print(PRIX_AMI)
    # Sinon...
   else:
      #...vérifier le poids des bagages est supérieur ou égale à 20 kg et afficher le prix majoré
      if poids_de_vos_bagages >= 20:
         print(PRIX_MAJORÉ)
      else:
         # Sinon afficher le prix normal
         print(PRIX_NORMAL)
