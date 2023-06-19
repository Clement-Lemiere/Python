users = ['foo', 'bar', 'baz']
mix = [True, 3.14, "lorem ipsum", None, [123, 42]]

mix = [
    True,
    3.14,
    "lorem ipsum",
    None,
    [123, 42]
]
# accès en lecture

print(users[0])
# len -1 est l'index du dernier élément. !!!!!!PYRATES LEVEL 8!!!!!!
i = len(users) - 1
print(users[i])

# l'index dépasse la taille de la liste: indexerror
# print(users[100 + 42 - i])

# accès en écriture
users[0] = "lorem"

# ajouter un nouvel élément
users.append('ipsum')

#ajouter un nouvel élément au début ou au milieu
users.insert(0, 'sit')
users.insert(2, 'dolores')
print(users)

# concaténation de liste
fruits = ["ananas", "banana", "cerise"]
legumes = ["artichaud", "brocolis", "carotte"]
ingredients = fruits + legumes
print(ingredients)
fruits += legumes
print(fruits)

letters = ["g", "z", "d", "b", "c", "Z"]
letters = sorted(letters)
print(letters)