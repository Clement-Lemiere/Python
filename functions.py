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

#type hinting
def mult(a: int, b: int) -> int:
    return a * b
    """ Cette fonction ...
    a ...
    b ...
    return ...
    """
result = mult(2, 5)
print(result)
#mais les autres types de données passent quand même
#result = mult('abc', 5)
#le nom de la fonction + ses paramètres + son type de retour = signature de la fonction
#def mult(a: int, b: int) -> int:
 

# copie d'une fonction comme si c'était une variable
mult_copy = mult
mult_copy(2, 5)

# Fonction de degré supérieur.
# Une fonction qui accepte une autre fonction comme paramètre
#ou qui renvoie une fonction
def operateur_binaire(a, b, fonction):
    return fonction(a, b)

#appel de la fonction de degé supérieur
resultat= operateur_binaire(2, 5,mult)

operations = []
operations.append(addition)
operations.append(mult)

a=2
b=5
resultat = None

for operation in operations:
    resultat = operations(a, b)
    print(resultat)

    my_list = ['foo', 'ipsum']
    text='toto'

    print(len(my_list))
    print(len(text))

    def my_len(value):
        return 42
    
    # sauvegarde de la fonction len() originale
    len_backup = len
    #surcharge de la fonction len() originale
    len = my_len

    print(len(my_list))
    print(len(text))

    #pass permet d'écrire du code python syntaxiquement valide, même quand on n'a pas encore le corps du if ou de la boucle for.
    if True:
        pass
