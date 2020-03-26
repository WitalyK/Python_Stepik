def steps_to_convert(s1, s2):
    """Расстояние Дамерау-Левенштейна"""
    d, len_s1, len_s2 = {}, len(s1), len(s2)
    for i in range(-1, len_s1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, len_s2 + 1):
        d[(-1, j)] = j + 1
    for i in range(len_s1):
        for j in range(len_s2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,
                d[(i, j - 1)] + 1,
                d[(i - 1, j - 1)] + cost)
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)
    return d[len_s1 - 1, len_s2 - 1]


if __name__ == "__main__":
    print(steps_to_convert('line1', '1enil'))
    # assert steps_to_convert('line1', 'line1') == 0, "eq"
    # assert steps_to_convert('line1', 'line2') == 1, "2"
    # assert steps_to_convert('line', 'line2') == 1, "none to 2"
    # assert steps_to_convert('ine', 'line2') == 2, "need two more"
    # assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    # assert steps_to_convert('', '') == 0, "two empty"
    # assert steps_to_convert('l', '') == 1, "one side"
    # assert steps_to_convert('', 'l') == 1, "another side"
    # print("You are good to go!")