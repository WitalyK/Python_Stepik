from urllib.request import urlopen
from re import findall
from collections import Counter
from pprint import pprint
from bs4 import BeautifulSoup


html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
s = str(html)
regex = '<code>(.*?)</code>'
l = sorted(findall(regex, s))
pprint(Counter(l), width=40)
# print(s.count('C++'))
# print(s.count('Python'))

# https://python-scripts.com/beautifulsoup-html-parsing - тут красиво написано как парсить