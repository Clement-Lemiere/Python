import random

# opérateurs composés
b=0

# incrémentation
# b= b+1
b +=1
print(b)

# décrémentation
# b= b-1
b -=1
print(b)

# multiplication
c = 3
# c = c * 2
c *= 2
print(c)

# division
d= 10
# d = d / 3
d /= 3
print(d)

# division entière
d=10
d//=3
print(d)

# opérateur d'inclusion
text1 = "lorem ipsum"
"e" in text1
print("e" in text1)

# opérateur d'inculsion avec une liste
list1 = ['lorem', 'ipsum']
print ('e' in list1)
print ('ipsum' in list1)

#comparaison avec des nombres aléatoires
e = random.randint(0, 100)
f = random.randint(0, 100)

print(f'{e= }')
print(f'{f= }')

result = e == f
print(result)

result = e < f
print(result)

# expressions
# Une expression est une ligne de code qui génère un résultat.
# Exemple print() n'est pas une expression, elle affiche seulement le résultat.