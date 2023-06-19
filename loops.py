import random

# While :

while False:
    print("Ce message ne s'affiche pas")


#ctrl+c pour arrêter le programme.

# while True:
#    #Continue permet de reprendre au début de la boucle suivante
#    continue
#    print("Ce message est affiché en boucle")
# #    break permet de sorte d'une boucle.
#    break

# premier tirage
dice = random.randint(1, 6)

while dice!=6:
    print(f"Je n'ai pas tiré un six, mais un {dice}")
    print("Je recommence un nouveau tirage")
    dice = random.randint(1, 6)
print("dice number :", dice)

# recréation de la boucle for classique avec une bloucle while
i=0
while i<10:
    print(f'{i= }')
    i += 1

# boucle for classique/ en python
# 0 est inclu, 10 est exclu
for i in range(0, 10):
    print(f'{i= }')

#boucle à rebours
for i in range(10, 0, -1):
    print(f'{i = }')

#boucle for each
users = ['foo','bar', 'baz']

for user in users:
    print(user)

for i, user in enumerate(users):
    print(f"{i = }, {user = }")
# la première variable déclarée rapporre toujours à l'index de l'élément.

# boucle 'for' 
for i in range(0, len(users)):
    user = users[i]
    print(f"{i = }, {user = }")
