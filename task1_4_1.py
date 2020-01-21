from urllib.request import urlopen, urlretrieve
import requests, datetime
from bs4 import BeautifulSoup


start_time = datetime.datetime.now()
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') # делаем суп
cnt = 0
for td in soup.find_all(['td', 'th']):
    cnt += int(td.text)
print(cnt, datetime.datetime.now()-start_time)

start_time = datetime.datetime.now()
resp = requests.get('https://stepik.org/media/attachments/lesson/209723/4.html') # скачиваем файл
soup = BeautifulSoup(resp.content, 'html.parser') # делаем суп
cnt = 0
for td in soup.find_all(['td', 'th']):
    cnt += int(td.text)
print(cnt, datetime.datetime.now()-start_time)

start_time = datetime.datetime.now()
resp = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html') # скачиваем файл
soup = BeautifulSoup(resp.content, 'html.parser') # делаем суп
cnt = 0
for td in soup.find_all(['td', 'th']):
    cnt += int(td.text)
print(cnt, datetime.datetime.now()-start_time)
