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


# def recfun(ite, i_, num, l_obj):
#     """
#     Рекурсия для реализации комбинации множества строк.
#     Пытался использовать рекурсию, пока не понял что надо применить
#     комбинаторику, в которой не силён. Рекурсия сработала только для
#     комбинаций по 2 строки и решала только основную задачу
#     """
#     if i_ == num:
#         return False
#     else:
#         if ite.fit(l_obj[i_]):
#             l_ = ite + l_obj[i_]
#             if l_.full:
#                 return Line(l_.l, l_.n)
#             else:
#                 return recfun(ite, i_ + 1, num, l_obj)


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
    # for item in list_obj:  # неудачная попытка использовать рекурсию
    #     if item.full:
    #         list_res.append(Line(item.l, item.n))   # заполненную строку сразу заносим в итоговый список
    #     else:
    #         for i in range(item.n[0], len(list_obj)):
    #             a = recfun(item, i, len(list_obj), list_obj)  # иначе проверяем и заполняем рекурсивно
    #             if a:
    #                 list_res.append(a)
    lenitem = len(list1[0])  # определяем длину элемента загруженного списка (количество элементов в строке)
    print(lenitem)
    for i in range(1, lenitem + 1):  # будем перебирать все возможные комбинации от одной строки (когда
        for item in combinations(list_obj, i):  # все элементы заполнены) до максимального количества элементов.
            if i == 1:  # используем готовую функцию (т.к. не силён в комбинаторике) combinations(list_obj, i)
                if item[0].full:  # из библиотеки iterable, где list_obj - итерируемый объект, i - длина комбинации.
                    list_res.append(item[0])  # заполненные сразу заносим в итоговый список
            else:
                temp = Line(item[0].l, item[0].n)
                print(temp)
                for m in range(1, i):
                    if temp.fit(item[m]):
                        temp = temp + item[m]
                        if m == i:
                            list_res.append(temp)
                    else:
                        break
    if list_res:
        for line in list_res:  # если итоговый список не пустой выведем на экран в красивом виде)
            print(f'{line.l}  <- комбинация строк {line.n}')
        list_out = [line.l for line in list_res]
        with open('output.json', 'w') as dst:  # выгрузка данных в файл
            dump(list_out, dst)
