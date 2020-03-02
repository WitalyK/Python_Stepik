from itertools import product, combinations_with_replacement
from time import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pprint import pprint


def product_process(rest, first, m):
    return len(list((i for i in product(first, *rest) if sum(i) == m)))


def raschet():
    N = 10  # number of side
    k = 7  # number of dices
    m = 50  # target sum
    combinations_with_replacement()
    if N * k > m:
        lis = [n + 1 for n in range(m - k + 1) if n < N]
        llis = [lis for _ in range(k - 1)]
        with ProcessPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(product_process, llis, [elem_of_lis], m) for elem_of_lis in lis]
            count = sum([f.result() for f in as_completed(futures)])
        print(count)
        # print(round(count / (N ** k), 4))
    else:
        print(0)


if __name__ == '__main__':
    s = time()
    raschet()
    print(time() - s, 'секундов!!!')
