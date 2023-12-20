# Votre programme lira d'abord un entier représentant le nombre de montées et descentes
#  que vous avez réalisées. Pour chaque montée ou descente, il faut ensuite lire un entier représentant
#  la variation d'altitude, cet entier étant strictement positif dans le cas d'une montée et
#  strictement négatif dans le cas d'une descente (il n'y a rien à compter pour les tronçons
#  qui sont bien à plat). Votre programme devra afficher l'altitude totale montée
#  puis l'altitude totale descendue (ces deux nombres sont positifs).

# Entrer un entier représentant le nombre de montées et descentes
nombre_montées_descentes = int(input())
# Initier la variable des totaux de montées et de descentes à 0
montées = 0
descentes = 0
# Utiliser une boucle pour entrer les dénivelés entre chaque altitudes
for niveau in range(nombre_montées_descentes):
    dénivelé = int(input())
    # Vérifier si le dénivelé est supérieur à 0
    if dénivelé > 0:
        # Cumuler la valeur des dénivelés positifs
        montées = montées + dénivelé
    else:
        # Cumuler la valeur des dénivelés négatifs
        descentes = descentes - dénivelé
# Afficher les totaux 
print(montées)
print(descentes)
