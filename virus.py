import numpy as np


def da(z, i, j):
    if z[i, j] != 1:
        return False  # 1 in centre
    if len(np.unique(z[i, j - 1:j + 2])) != 1:
        return False  # odinak in horiz
    if len(np.unique(z[i - 1:i + 2, j])) != 1:
        return False  # odinak in vertikal
    if len(np.unique(z[i - 1:i + 2:2, j - 1:j + 2:2])) != 1:
        return False  # odinak in coner
    return True


def provvokr0(z, i, j, n, sha):
    x, y = sha
    if i - n - 1 >= 0:
        if z[i - n - 1, j] != 0:
            return False
    if i + n + 1 < x:
        if z[i + n + 1, j] != 0:
            return False
    if j - n - 1 >= 0:
        if z[i, j - n - 1] != 0:
            return False
    if j + n + 1 < y:
        if z[i, j + n + 1] != 0:
            return False
    for it in range(n, 0):
        if z[i - it, j - (n - it + 1)] != 0:
            return False
        if z[i - it, j + (n - it + 1)] != 0:
            return False
    for it in range(1, n + 1):
        if z[i + it, j - (n - it + 1)] != 0:
            return False
        if z[i + it, j + (n - it + 1)] != 0:
            return False
    return True


def provvokr1(z, i, j, n, sha):
    x, y = sha
    if i - n - 1 < 0 or z[i - n - 1, j] != 1:
        return False
    if i + n + 1 >= x or z[i + n + 1, j] != 1:
        return False
    if j - n - 1 < 0 or z[i, j - n - 1] != 1:
        return False
    if j + n + 1 >= y or z[i, j + n + 1] != 1:
        return False
    for it in range(n, 0):
        if z[i - it, j - (n - it + 1)] != 1:
            return False
        if z[i - it, j + (n - it + 1)] != 1:
            return False
    for it in range(1, n + 1):
        if z[i + it, j - (n - it + 1)] != 1:
            return False
        if z[i + it, j + (n - it + 1)] != 1:
            return False
    return True


def bigcolon(z, i, j, n, sha):
    if provvokr0(z, i, j, n, sha):
        return n, i, j
    else:
        if provvokr1(z, i, j, n, sha):
            return bigcolon(z, i, j, n+1, sha)
        return False


def colonies(z, lis, sha):
    total = []
    for it in lis:
        i, j = it
        if (tup := bigcolon(z, i, j, 1, sha)):
            total.append(tup)
    if total:
        _, i, j = sorted(total, reverse=True)[0]
        return [i, j]
    else:
        return [0, 0]


def healthy(grid):
    Z = np.array(grid)
    n, m = Z.shape
    lis = []
    for i in range(1, n - 1):
        for j in range(1, m - 1):  # for central cells
            if da(Z, i, j):        # check for christ
                lis.append((i, j))
    return colonies(Z, lis, (n, m))


if __name__ == '__main__':
    print(healthy(((0, 0, 0, 0, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (1, 1, 1, 1, 1, 0, 0, 0),
                   (0, 1, 1, 1, 0, 0, 1, 0),
                   (0, 0, 1, 0, 0, 1, 1, 1),
                   (0, 0, 0, 0, 0, 0, 1, 0),)))
