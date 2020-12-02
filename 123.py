<<<<<<< HEAD
def paper_dice(data):
    f, b, r, l, t, d = 1, 6, 2, 5, 3, 4
    sides = {(i, j): int(it) for i, line in enumerate(data) for j in range(len(line)) if (it := data[i][j]).isdigit()}
    valid = set(sides.keys())
    y, x = list(sides.keys())[0]
    busy = [(y, x)]
    used = {f: sides[(y, x)]}

    def wrap():
        nonlocal f, b, r, l, t, d, y, x
        remove = {(y + 1, x): (t, d, r, l, b, f),
                  (y - 1, x): (d, t, r, l, f, b),
                  (y, x + 1): (r, l, b, f, t, d),
                  (y, x - 1): (l, r, f, b, t, d)}
        neighbors = {(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)} & valid
        for item in (neighbors - set(busy)):
            busy.append(item)
            f, b, r, l, t, d = remove[item]
            used[f] = sides[item]
            y, x = item
            wrap()

    wrap()
    if len(used) != 6:
        return False
    for i in range(1,4):
        if used[i]+ used[7-i] != 7:
            return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(paper_dice(['  1  ',
                ' 235 ',
                '  6  ',
                '  4  ']))  # == True

    print(paper_dice(['    ',
                '12  ',
                ' 36 ',
                '  54',
                '    ']))  # == True

    print(paper_dice(['123456']))  # == False
    print(paper_dice(['123  ',
                '  456']))  # == False
=======
import re


# "nametxt","name[]txt" False
# "checkio","[c[]heckio"

def unix_match(filename: str, pattern: str) -> bool:
    pattern = pattern.replace( ".", "\.").replace( "*", ".*").replace(
        '[!', '[^').replace('[]', '[^.]').replace("[^]", "\[!\]")
    return bool(re.match(pattern, filename))



if __name__ == '__main__':
    print("Example:")
    print(unix_match('checkio', 'c[h[]eckio'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
>>>>>>> a62e676bbbb8a90ad4d0368d832cc16c8f6a25b1
