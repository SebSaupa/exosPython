'''
*** EXO 7: CSV De Niro ***
Créer un programme qui, à partir du fichier deniro.csv,
produira en sortie un fichier deniro-report.txt" 
affichant les informations suivantes:

Nom du film le mieux noté
Nombre de films entre 2000 et 2010

'''
print("*** EXO 7: CSV De Niro ***")

import csv

bestFilm = ""
nbFilms = 0
year = []
score = []
title = []

with open("deniro.csv", "r") as csvFile:
    rows = csv.reader(csvFile, delimiter=",")
    for r in rows:
        year.append(r[0])
        score.append(r[1])
        title.append(r[2])
        
year.pop(0)
score.pop(0)
title.pop(0)
intScore = []

for s in score:
    intScore.append(int(s))

scoreMax = max(intScore)

for i in range(len(intScore)):
    if intScore[i] == scoreMax :
        bestFilm = title[i]

for y in year:
    if int(y) >= 2000 and int(y) <= 2010:
        nbFilms += 1

print("Le film le mieux noté est :%s" % bestFilm)
print("Le nombre de films entre 2000 et 2010 est :", nbFilms)

