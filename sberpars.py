from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
import re
import pandas as pd


def normal(list_item, start, end):
    list_item = iter(list_item)
    l = []
    while True:
        try:
            dat = next(list_item)
            dat = datetime.strptime(dat, '%d.%m.%Y')
            sum = next(list_item)
            sum = sum.replace('\xa0', '')
            if sum.startswith('+'):
                prih = True
            else:
                prih = False
            sum = sum.replace('+', '').replace(' RUB', '').replace(' ', '').replace(',', '.')
            opis2 = next(list_item)
            opis2 = re.sub(' +', ' ', opis2)
            *rest, opis1 = opis2.split('.')
            opis2 = opis2.replace(opis1, '')
            opis1 = opis1.lstrip()
            if start <= dat <= end:
                l.append((dat, prih, opis1, opis2, float(sum)))
        except StopIteration:
            break
    l = sorted(l, key=lambda x: (x[0], x[1], x[2], x[3]))
    l = [(item[0].strftime('%d.%m.%Y'), item[1], item[2], item[3], item[4]) for item in l]
    return l


def seter(list_norm):
    d = {}
    for line in list_norm:
        if d.get(line[0]):
            if d[line[0]].get(line[1]):
                if d[line[0]][line[1]].get(line[2]):
                    if d[line[0]][line[1]][line[2]].get(line[3]):
                        d[line[0]][line[1]][line[2]][line[3]] += line[4]
                    else:
                        d[line[0]][line[1]][line[2]][line[3]] = line[4]
                else:
                    d[line[0]][line[1]][line[2]] = {line[3]: line[4]}
            else:
                d[line[0]][line[1]] = {line[2]: {line[3]: line[4]}}
        else:
            d[line[0]] = {line[1]: {line[2]: {line[3]: line[4]}}}
    return d


def save_to_excel(array, sheet_name, headers):
    df = pd.DataFrame(array, columns=headers)
    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet_name, header=True, index=False)
    writer.save()


# don't run on import
if __name__ == "__main__":
    with open('26012020093451.html', encoding='utf-8') as resp:
        html = resp.read()  # считываем содержимое
    s = str(html).replace('&#034;', '"').replace('\t', ' ')
    soup = BeautifulSoup(s, 'html.parser')  # делаем суп
    table = soup.find('table', attrs={'id': 'rrr'})
    for tr in table.find_all('tbody'):
        td = [td.text for td in tr.find_all('td')]
    start_dt = datetime.strptime('01.01.2000', '%d.%m.%Y')
    end_dt = datetime.strptime('31.12.2050', '%d.%m.%Y')
    td = normal(td, start_dt, end_dt)
    zagolovki = ['Дата', 'прих/расх', 'категория', 'Вид', 'Сумма']
    save_to_excel(td, 'Общий', zagolovki)
    # pprint(td)
    slov = seter(td)
    pprint(slov)
    # regex = '\. ((?!\.).)+$'

# https://riptutorial.com/ru/python/example/17392/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%BE%D0%B2-excel-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-xlsxwriter
