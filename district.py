from pprint import pprint
import numpy as np


class Cell:
    def __init__(self, n, m, val=None, coord=None):
        self.n = n
        self.m = m
        self.neighbors = []
        if coord:
            self.coord = [coord]
            self.set_neighbors()
        if val:
            i, j = val
            self.count = i + j
            self.rate = i - j
        self.busy = False

    def set_neighbors(self):
        lis = []
        for it in self.coord:
            i, j = it
            if i != 0:
                if [i - 1, j] not in self.coord:
                    lis.append([i - 1, j])
            if j != 0:
                if [i, j - 1] not in self.coord:
                    lis.append([i, j - 1])
            if i < self.n-1:
                if [i + 1, j] not in self.coord:
                    lis.append([i + 1, j])
            if j < self.m-1:
                if [i, j + 1] not in self.coord:
                    lis.append([i, j + 1])
        lis1 = []
        for it in lis:
            if it not in lis1:
                lis1.append(it)
        self.neighbors = lis1

    def __add__(self, other):
        cel = Cell(self.n, self.m)
        cel.count = self.count + other.count
        cel.rate = self.rate + other.rate
        cel.coord = self.coord + other.coord
        cel.set_neighbors()
        cel.busy = True
        return cel

    def __repr__(self):
        return f'{self.coord=}, {self.count=}, {self.rate=}, {self.neighbors=}, {self.busy=}'


def poisk(cell, Z, count, lis):
    for ij in cell.neighbors:  # (i.rate >= 0) == rate
        i, j = ij
        if not Z[i, j].busy and Z[i, j].rate < 0 and (cell.count + Z[i, j].count) <= count:
            Z[i, j].busy = True
            cell = cell + Z[i, j]
            print(Z[i, j])
        if cell.count >= count:
            lis.append(cell)
            return
        else:
            poisk(cell, Z, count, lis)


def unfair_districts(count, grid):
    lis = []
    n = len(grid)
    m = len(grid[0])
    Z = np.zeros((n, m), dtype=Cell)
    for i in range(n):
        for j in range(m):
            Z[i, j] = Cell(n, m, grid[i][j], [i, j])
    while True:
        full = True
        for it in Z.flat:
            if not it.busy:
                full = False
                cell = it
                cell.busy = True
                rate = cell.rate >= 0
                # print(f'{rate=}')
                vyh = False
                while True:
                    for ij in cell.neighbors:  # (i.rate >= 0) == rate
                        i, j = ij
                        if not Z[i, j].busy and (Z[i, j].rate >= 0) == rate and (cell.count + Z[i, j].count) <= count:
                            Z[i, j].busy = True
                            cell = cell + Z[i, j]
                            print(Z[i, j])
                            if cell.count >= count:
                                print(vyh)
                                lis.append(cell)
                                vyh = True
                                print(vyh)
                                break
                    print(vyh)
                    if vyh:
                        break
        if full:
            break
    return lis


if __name__ == '__main__':
    pprint(unfair_districts(9, [[[0, 3], [3, 3], [1, 1], [3, 3]],
                                [[1, 2], [1, 0], [1, 1], [1, 1]],
                                [[0, 3], [2, 1], [2, 2], [0, 1]]]))
    # cell1 = Cell(3, 4, [3, 3], [1, 0])
    # print(cell1)
    # cell2 = Cell(3, 4, [1, 2], [1, 1])
    # print(cell2)
    # cell1 = cell1 + cell2
    # print(cell1)
    # c1 = cell1 + cell2
    # cell3 = Cell(3, 4, [1, 0], [1, 2])
    # c2 = c1 + cell3
    # cell5 = Cell(3, 4, [1, 0], [2, 2])
    # c3 = c2 + cell5
    # cell4 = cell1 + cell2 + cell3 + cell5
    # print(c3)
