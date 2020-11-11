def simple_areas(*args):
    from math import pi, sqrt

    def circle(diameter):
        return (diameter / 2) ** 2 * pi

    def rectangle(width, height):
        return width * height

    def triangle(a, b, c: 'sides') -> "get area using Heron's formula":
        s = (a + b + c) / 2  # semiperimeter
        return sqrt(s * (s - a) * (s - b) * (s - c))

    # area_function = {1: circle, 2: rectangle, 3: triangle}[len(args)]
    return {1: circle, 2: rectangle, 3: triangle}[len(args)](*args)  # area_function(*args)


if __name__ == '__main__':
    print(simple_areas(100, 200, 120))