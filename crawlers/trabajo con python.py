from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import requests
import csv

class PostCrawled():

    def __init__(self,titulo,emoji,contenido,imagen):

        self.titulo=titulo
        self.emoji=emoji
        self.contenido=contenido
        self.imagen=imagen



class postExtractor():

    def estraeInfo(self):

        urlBase="https://python.beispiel.programmierenlernen.io/index.php"

        #posts=[]

        while urlBase!="":

            midoc=requests.get(urlBase) 

            docFinal=BeautifulSoup(midoc.text, "html.parser")

            time.sleep(2)

            for card in docFinal.select(".card"):

                titulo=card.select(".card-title span")[1].text
                emoji=card.select_one(".emoji").text
                contenido=card.select_one(".card-text").text
                imagen=urlBase + card.select_one("img").attrs["src"]

                

                #post=PostCrawled(titulo,emoji,contenido,imagen)
                #posts.append(post)

                yield PostCrawled(titulo,emoji,contenido,imagen)
            
            boton_siguiente=docFinal.select_one(".navigation .btn")

            if boton_siguiente:
                
                web=urljoin(urlBase,boton_siguiente.attrs["href"])
                urlBase=web
                print(web)

            else:

                urlBase=""


        #return posts
    

unpost=postExtractor()

listaPosts=unpost.estraeInfo()

contador=0
for elPost in listaPosts:
    if contador==12:
        break
    contador+=1
    print(elPost.emoji)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print()




"""with open('posts.csv', 'w', newline='', encoding="utf-8") as csvfile:
    postwriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for mipost in listaPosts:

        postwriter.writerow([mipost.emoji,mipost.titulo,mipost.contenido,mipost.imagen])"""
    
