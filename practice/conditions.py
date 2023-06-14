
import random
if True:
    print("Ce message s'affichera troujours")
if False:
    print("Ce message ne s'affichera jamais")



# opérateurs logiques
# ou exclusif (xor)
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)

# truth table xor operator
# A      B       A xor B

# True   True    False
# True   False   True
# False  True    True
# False  False   False

# exercice course opérateur or
has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))
              
print(f'{has_cash = }')
print(f'{has_cb = }')

if has_cb or has_cash:
    print( "Je peux aller faire les courses")
else:
    print("Je suis trop pauvre")

# exercice courses opérateur and

has_cash = bool(random.randint(0, 1))
has_cb = bool(random.randint(0, 1))
              
print(f'{has_cash = }')
print(f'{has_cb = }')

if not has_cash and not has_cb:
    print("Je ne peux pas aller faire  les courses")
else:
    print("Je peux aller faire les courses")

# combinaison "and" "or"
user_level=30
user_po=143
user_credit=0

if user_credit>=10 or user_level>=25 and user_po>=100 :
    print("user can buy stuff")
else:
    print("user cannot buy stuff")

# exercice carte de réduction
#déterminer la carte de réduction à laquelle le voyageur à droit
#entre 0 et 11 ans, gratuit.
# entre 12 et 25 ans, -50%.
# entre 26 et 64 ans, -10%.
#au delà de 64 ans, -50%
age = random.randint(0, 99)
print(age)

if age<12:
    print("gratuit")
elif age>=26 and age<=64:
    print("-10%")
else:
    print("-50%")


#if 12<=age<=26 or age>64:
#  print("-50%")