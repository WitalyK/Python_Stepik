from numpy.polynomial.polynomial import polypow
from time import time


def probability(dice_number, sides, target):
    powers = [0] + [1] * sides
    poly = polypow(powers, dice_number)
    try:
        return round(poly[target] / sides ** dice_number, 4)
    except IndexError:
        return 0


if __name__ == '__main__':
    s = time()
    print(probability(10, 10, 60))
    print(time() - s)
