'''
*** EXO 8: Health Check ***
Créer un programme qui, à partir du fichier websites.txt
vérifie que chacun des sites listées répond
à raison d'une requête toutes les n secondes

la périodicité sera fournie en entrée par l'utilisateur

On produira en sortie un fichier de log "health.log" contiendra:
- la date de la requête
- l'url interrogée
- le status code obtenu ou une indication d'erreur en cas de non réponse
'''
print("*** EXO 8: Health Check ***")

# votre code ici

import requests
import time
# module time.sleep() pour la périodicité de n seconde
# input("Tout les n seconde : n = ")

# status Code
# boucle infiti

f = open("websites.txt", "r")
content = f.read()  #   Lecture du fichier et stockage de son contenu
f.close()

n = int(input("Saisir le temps en seconde pour une nouvelle itération : "))

websiteList = content.splitlines()

while True:
    for website in websiteList:
        fileLog = open("health.log", "a")
        try:
            response = requests.get(website)
            fileLog.write(website + " Status_code : " + str(response.status_code) + "\n")
        except:
            fileLog.write("Le site %s n'a pas été trouvé\n" % website)
        fileLog.close()
    print("Nouvelle itération")
    time.sleep(n)