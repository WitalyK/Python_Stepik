def intersect(x1, y1, r1, x2, y2, r2):
    if cen_len := ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5:
        return abs(r1 - r2) < cen_len < r1 + r2


def count_chains(circles: list[tuple[int, int, int]]) -> int:
    out = [[circles.pop(0)]]
    while circles:
        test = circles.pop(0)
        try:
            for i, it in enumerate(out):
                for item in it:
                    if intersect(*item, *test):
                        out[i] += (test,)
                        raise Exception()
        except:
            pass
        else:
            out.append([test])
    return len(out)


if __name__ == '__main__':
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))  # == 2
    print(count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]))  # == 1
    print(count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]))  # == 4
