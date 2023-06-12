# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
#
# ATTENTION : ne pas utiliser la fonction sum()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.10
total=0
for i in my_list:
    total += i
moyenne_item = total / len(my_list)
print(total)
print(moyenne_item)
