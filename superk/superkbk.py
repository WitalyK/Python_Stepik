# -*- coding: utf-8 -*-
from json import load, dump
from pprint import pprint
from itertools import combinations


class Line:
    """
    Строка содержит список, номер строки, признак заполненности непустыми значениями,
    а так же метод fit() для проверки возможности комбинирования строк.
    """

    def __init__(self, lis, n: list):
        self.l = lis
        self.n = n
        self.full = all(item for item in lis)

    def fit(self, other):
        for i, j in zip(self.l, other.l):
            if i and j:
                return False
        return True

    def __add__(self, other):
        """
        Метод для реализации суммирования строк
        """
        l = []
        for i, j in zip(self.l, other.l):
            if i:
                l.append(i)
            else:
                l.append(j)
        return Line(l, [self.n, other.n])

    # Следующие два метода для строкового представления объекта
    def __str__(self):
        return f'({self.l}, {self.n}, {self.full})'

    def __repr__(self):
        return f'({self.l}, {self.n}, {self.full})'


# don't run on import
if __name__ == "__main__":
    with open('input.json') as src:  # загрузка данных в список списков
        list1 = load(src)
    i = 1
    list_obj = []
    for item in list1:
        list_obj.append(Line(item, [i]))  # перевод строк в объекты
        i += 1
    list_res = []  # готовим итоговый список
    pprint(list_obj)  # вывод списка объектов для проверки
    print('*' * 45)
    lenitem = len(list1[0])  # определяем длину элемента загруженного списка (количество элементов в строке)
    for i in range(1, lenitem + 1):  # будем перебирать все возможные комбинации от одной строки (когда
        for item in combinations(list_obj, i):  # все элементы заполнены) до максимального количества элементов.
            if i == 1:  # используем готовую функцию (т.к.не силён в комбинаторике к сожалению) combinations(list_obj,i)
                if item[0].full:  # из библиотеки iterable, где list_obj - итерируемый объект, i - длина комбинации.
                    list_res.append(item[0])  # заполненные сразу заносим в итоговый список
            else:  # функция возвращает iterable объект, где элементы это комбинации без повторов
                temp = Line(item[0].l, item[0].n)  # запоминаем первую строку для сложения всех строк в цикле
                for m in range(1, i):
                    if temp.fit(item[m]):  # если следующая строка подходит для сложения (нет значимых элементов на
                        temp += item[m]  # одинаковых позициях) складываем все
                        if m == (i - 1) and temp.full:  # если сложили последний элемент и итоговый объект заполнен
                            list_res.append(temp)  # записываем объект в результирующий список
                    else:
                        break  # если строка не подходит для сложения выходим из цикла и проверяем следующую комбинацию
    if list_res:
        for line in list_res:  # если итоговый список не пустой выведем на экран в красивом виде)
            print(f'{line.l}  <- комбинация строк {line.n}')
        list_out = [line.l for line in list_res]
        with open('output.json', 'w') as dst:  # выгрузка данных в файл
            dump(list_out, dst)

# Для проверки использовал список списков из 18 строк по 5 элементов input1.json
