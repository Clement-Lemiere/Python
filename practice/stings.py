text1="lorem"
text2="ipsum"
# Concaténation
text3= "citation:"+text1+" "+text2+", César"
print(text3)

#interpolation avec une f-string
text3=f"citation:{text1} {text2}, César"
print(text3)

#Attention: La concaténation ne fonctionne qu'avec des "str"s
#Solution: Convertir le "int" en "str"
mails=52
text4= "Vous avez "+ str(mails)+" non lus"
print(text4)

# Répétition de texte
text5="foo"*3
print(text5)
text6= text5*3
print(text6)

# Affichage de valeurs arrondies
number1=10/3
text7 = f"10/3 est à peu près {number1:.3}"
print(text7)

# Les focntions associées aux strings
text8="foo bar baz foo"
# longueur
print(len(text8))
#compter des éléments
print(text8.count("foo"))

#pour trouver l'occurrence suivante, il faut chercher une position plus loin.
position= text8.find("foo")
print(text8.find("foo", position+1))
