'''
*** Exo 4: somme de saisies ***
Créer un programme demandant à l'utilisateur se saisir
un chiffre. Tant que l'utilisateur ne saisit pas la valeur "0",
on lui redemande la saisie d'un chiffre.
En sortie de boucle, on affichera la somme des valeurs saisies ainsi qu'un
récapitulatif des valeurs saisies
Exemples de valeurs saisies par l'utilisateur:
15
2
3
0
=> Somme des valeurs saisies: 20 (15,2,3)
'''
print("*** EXO 4: somme de saisies ***")

inputNumber = int(input("Saisir un chiffre : "))
somme = 0
historyNumber = []

while inputNumber != 0:
    somme += inputNumber
    historyNumber.append(inputNumber)
    inputNumber = int(input("Saisir un autre chiffre : "))

print("Somme des valeurs saisies : ", somme, historyNumber)
    