import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
COVID = 'https://www.worldometers.info/coronavirus/'

full_page = requests.get(COVID, headers=headers).text

soup = BeautifulSoup(full_page, 'html.parser')
lis = []
for div in soup.find_all("div", {"id": "maincounter-wrap"}):
    print(div.h1.text)
    print(div.span.text)
    lis.append(div.span.text)
    print('-'*50)
det = float(lis[1].replace(',', '.'))
vyg = float(lis[2].replace(',', '.'))
print('Процент умерших:')
print(round(det/(det+vyg)*100.0, 1))

input('Нажми Enter')