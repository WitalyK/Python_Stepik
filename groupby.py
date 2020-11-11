from itertools import groupby


def sum_consecutives(items):
    return (sum(grouper) for _, grouper in groupby(items))


if __name__ == '__main__':
    print(list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])))  # [9, 8, 5, 12]
