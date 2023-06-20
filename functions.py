#definition
def hello():
    print('hello Python!')

#call or execution
hello()

#
def hellobis(name):
    print(f'Hello {name}!')

hellobis('foo')

#parametres + retour de valeur
def addition(a, b):
    return a + b

resultat = addition(42, 123)
print (resultat)

#appel d'une fonction stockée dans un autree module.
# resultat = library.oui_non(False)
# print(resultat)
# print(library.oui_non(True))

#reverse lookup
my_list = [3.14, 42, 123]

def reverse_lookup(my_list, value):
    """cette fonction prend en paramètre une liste et une valeur à rechercher.
    Elle renvoie l'index de la valeur si elle n'est pas trouvée, ou none si la valeur n'est pas trouvée."""

    for i in range(len(my_list)):
        if my_list[i]==value:
            print(f'{i= }')

reverse_lookup(my_list, 3.14)