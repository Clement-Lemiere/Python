# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`
my_list = [2.71, 42, 123, 2, 3.14, 1.61]
new_list = []

for item in my_list:
    if type(item) == int:
        new_list.append(item)

print(new_list)
