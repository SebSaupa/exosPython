'''
*** Exo 6: Générateur de mot de passe ***
Créer un programme qui génère un mot de passe de longueur variable
en concaténant des caractères de façon aléatoire.
Le mot de passe devra contenir:
- au moins une majuscule
- au moins une minuscule
- au moins une valeur numérique
- au moins au caractères spécial (/;|%, etc.)

La longeur sera donnée par une saisie utilisateur
ex: longueur: 8 => Hn_y9l2%
'''
print("*** EXO 6: Générateur de mot de passe ***")

import random
import string

lowerLetter = string.ascii_lowercase
upperLetter = string.ascii_uppercase
specialCharacters = string.punctuation

passwordLength = int(input("Saisir la longueur du mot de passe souhaité : "))

numCase = 0
password = []
counter = 0

while counter < passwordLength:
    if numCase == 0:
        password.append(random.choice(lowerLetter))
        numCase += 1
        counter += 1
    elif numCase == 1:
        password.append(random.choice(upperLetter))
        numCase += 1
        counter += 1
    elif numCase == 2:
        password.append(str(random.randint(0, 9)))
        numCase += 1
        counter += 1
    elif numCase == 3:
        password.append(random.choice(specialCharacters))
        numCase += 1
        counter += 1
    else:
        numCase = 0

random.shuffle(password)

txtPassword = ""

for c in password:
    txtPassword += c

print("Le mot de passe est : ", txtPassword)
