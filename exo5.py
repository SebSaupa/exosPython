'''
*** Exo 5: flags => flagsBis ***
Créer un programme qui produira un dossier flagsBis
Ce dossier contiendra tous les fichier png d'origine mais
renommés en ne conservant que les deux premières lettres.
Ces lettres seront en masjuscule.
ex: 
  exos/flags/allemagne.png => exos/flagsBis/AL.png
  exos/flags/belgique.png => exos/flagsBis/BE.png

Le fichier missing.png devra être ignoré
'''
print("*** EXO 5: flags => flagsBis ***")
import os
import shutil

originalDir = "flags"
targetDir = "flagBis"

try :
  os.mkdir(targetDir)
  print("Dossier '%s' créé" % targetDir)
except FileExistsError:
  print("Le dossier '%s' existe déjà" % targetDir)

nameFiles = os.listdir(originalDir)
print(nameFiles)

for f in nameFiles:
  if f != "missing.png":
    newName = f[:2].upper()+f[-4:]
    shutil.copyfile(originalDir + "/" + f, targetDir + "/" + newName)