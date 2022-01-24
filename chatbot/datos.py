import requests
from bs4 import BeautifulSoup

url = 'https://www.frasess.net/frases-romanticas-para-enamorar-71.html'
pagina = requests.get(url)
bs = BeautifulSoup(pagina.content, 'html.parser')

mensajes = bs.find_all('div', class_='quote_text')

texto = open('mensajes.txt', 'w')

for i in mensajes:
    texto.write(i.text)
texto.close()