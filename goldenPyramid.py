def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    work = list(list(row) for row in pyramid)  # из тупла туплов делаем список списков
    for i in range(len(work) - 2, -1, -1):      # идем снизу вверх с предпоследней строчки
        for j in range(len(work[i])):
            work[i][j] += max(work[i + 1][j], work[i + 1][j + 1])
    return work[0][0]


if __name__ == '__main__':
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
