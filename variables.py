# nombre entier, integer
number1= 42
number1= 123
print(number1)

# nombre décimal, float
number2 = 3.14
number2 = 2.71
print(number2)

# chaine de caractère
text1 = "foo bar baz"
print(text1)

text2 = "foo bar baz"
print(text2)

# boolean
python_is_cool= True
print(python_is_cool)

python_is_boring= False
print(python_is_boring)

# null
user_accepted_terms = None
print(None)

# types de données
print(type(number1))
print(type(number2))
print(type(text1))
print(type(text2))
print(type(python_is_cool))
print(type(python_is_boring))
print(type(user_accepted_terms))

# Vérification du type de données
print(type(number1) is int)
print(type(number1) is float)

# to do, ask other types
print(type(number1) is str)

# Transtypage
print(type(str(number1)))

number3= 0
print(bool(number3))

# TT str -> int
#error: print(type(int(text1)))

text3 = '123456789'
print(type(int(text3)))

