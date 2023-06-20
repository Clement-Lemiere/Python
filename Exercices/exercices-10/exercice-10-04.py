# exo 10.4
# Créer une fonction nommée `is_greater()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur booléenne
# - renvoie True si `a` est plus grand que `b`
# - renvoie False dans les autres cas
# Appelez la fonction et affichez le résultat

# réponse 10.4
# import random
# a = round(random.uniform(0, 100), 2)
# b = round(random.uniform(0, 100), 2)

# def is_greater(a:float, b:float):
#     if a > b:
#         print(True)
#     else:
#         print(False)


def is_greater(a, b):
    return a > b


resultat = is_greater(5.6, 2.3)
print(resultat)  # Affiche True

resultat = is_greater(25.64, 53.46)
print(resultat)  # Affiche False

