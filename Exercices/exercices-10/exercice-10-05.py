# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5

def compare(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Appel de la fonction avec les valeurs 5.6 et 2.3
resultat = compare(5.6, 2.3)
print(resultat)  # Affiche 1

# Appel de la fonction avec les valeurs 2.3 et 5.6
resultat = compare(2.3, 5.6)
print(resultat)  # Affiche -1

# Appel de la fonction avec les valeurs 3.14 et 3.14
resultat = compare(3.14, 3.14)
print(resultat)  # Affiche 0

