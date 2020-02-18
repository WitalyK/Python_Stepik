from pprint import pprint


def is_covered(rect, circles):
    '''
    Охват камерами circles прямоугольной комнаты rect.
    '''
    w, h = rect
    s = set()
    for i in range(w + 1):
        for j in range(h + 1):
            s.add((i, j))
    for circ in circles:
        x0, y0, R = circ
        for item in tuple(s):
            x, y = item
            if (x - x0)**2 + (y - y0)**2 <= R**2:
                s.discard(item)
    if s:
        return False
    else:
        return True


if __name__=="__main__":
    print(is_covered([200, 150], [[100, 75, 130]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]))
    print(is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]))
