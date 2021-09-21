'''
*** Exo 3 ***
Ecrire un script python, qui calculera et affichera pour
chacun des prix le prix TTC.
Créer une fonction qui calculera le prix TTC
du prix HT qu'on lui fournira en entrée
'''
print("*** Exo 3 ***")

prices = [14,100,30,10,8]   #   prix HT
vat = 20    #   20%

# def calculTtc(ht, taux):
#     ttc=[]
#     for i in ht:
#         ttc.append(i+taux*i/100)
#     return ttc

# pricesTtc = calculTtc(prices, vat)
# print(pricesTtc)

#   Correction

def getPriveWithVat(price, vat = 20):
    return round(price * (1 + vat/100), 2)

# print(getPriveWithVat(30,5))

for price in prices:
    print(getPriveWithVat(price, 7))
