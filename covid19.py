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
det = float(lis[1].replace(',', ''))
vyg = float(lis[2].replace(',', ''))
print('Процент умерших:')
print(round(det/(det+vyg)*100.0, 1))

lis = []
for tab in soup.find_all("table", {"id": "main_table_countries_today"}):
    for bod in tab.find_all("tbody"):
        for tr in bod.find_all("tr"):
            if 'Russia' in tr.text:
                for td in tr.find_all("td"):
                    lis.append(td.text)
                break
print('-'*50)
print('-'*50)
print(lis[0])
print('-'*50)
print('Total:')
print(lis[1])
print('-'*50)
print('Deaths:')
print(lis[3])
print('-'*50)
print('Recovered:')
print(lis[5])
print('-'*50)
det = float(lis[3].replace(',', ''))
vyg = float(lis[5].replace(',', ''))
print('Процент умерших:')
print(round(det/(det+vyg)*100.0, 1))
input('Нажми Enter')