from json import load, dump
from pprint import pprint


class Line:
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
        l = []
        for i, j in zip(self.l, other.l):
            if i:
                l.append(i)
            else:
                l.append(j)
        return Line(l, [self.n, other.n])

    def __str__(self):
        return f'({self.l}, {self.n}, {self.full})'

    def __repr__(self):
        return f'({self.l}, {self.n}, {self.full})'


def recfun(item, i, num, list_obj):
    if i == num:
        return False
    else:
        if item.fit(list_obj[i]):
            l_ = item + list_obj[i]
            if l_.full:
                return Line(l_.l, l_.n)
            else:
                return recfun(item, i+1, num, list_obj)


# don't run on import
if __name__ == "__main__":
    with open('input.json') as src:
        l = load(src)
    i = 1
    list_obj = []
    for item in l:
        list_obj.append(Line(item, [i]))
        i += 1
    list_res = []
    pprint(list_obj)
    for item in list_obj:
        if item.full:
            list_res.append(Line(item.l, item.n))
        else:
            for i in range(item.n[0], len(list_obj)):
                a = recfun(item, i, len(list_obj), list_obj)
                if a:
                    list_res.append(a)
    if list_res:
        for line in list_res:
            print(f'{line.l}  <- комбинация строк {line.n}')
        list_out = [line.l for line in list_res]
        with open('output.json', 'w') as dst:
            dump(list_out, dst)

