def mountain_scape(angles: list[tuple]) -> int:
    return len({(j, i, (i + j) % 2 == 0) for (x, y) in angles
                for i in range(y, 0, -1)
                for j in range(x - (y - i), x + (y - i) + 1)})


if __name__ == '__main__':
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))
