'''
*** Exo 1 ***
Demander à l'utilisateur de saisir un chiffre
Si le chiffre saisi est supérieur à guess_number
on affiche "c'est moins"
Si le chiffre saisi est inférieur à guess_number
on affiche "c'est plus"
Si le chiffre saisi est égal à guess_number
on affiche "Bravo, tu as deviné !"
'''
print("*** EXO 1: chiffre mystère à deviner ***")
guess_number = 42

# votre code ici

n = int(input("Saisir un chiffre : "))

if n == guess_number:
    print("Bravo, tu as deviné !")
elif n > guess_number:
    print("C'est moins")
else:
    print("C'est plus")
