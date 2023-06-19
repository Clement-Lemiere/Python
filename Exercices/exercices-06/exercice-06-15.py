# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

# réponse 6.15
longest_string = ""

for i, string in enumerate(my_list):

    if len(string) > len(longest_string):
        position = i+1
        longest_string = string

print(longest_string,"Length:", len(longest_string), "Position:", position)
