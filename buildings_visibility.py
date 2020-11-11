# class Build:
#     def __init__(self, z, y, line):
#         self.z = z
#         self.y = y
#         self.line = line
#
#     def __add__(self, other):
#         if self.y <= other.y:
#             set1 = self.line - other.line
#         else:
#             set1 = self.line
#         return Build(self.z, self.y, set1)
#
#     def __repr__(self):
#         return f'Build(z={self.z}, y={self.y}, set={self.line})'
#
#
# def checkio(buildings):
#     lis = []
#     for build in buildings:
#         x1, z, x2, _, y = build
#         line = {(x, x + 1) for x in range(x1, x2)}
#         lis.append(Build(z, y, line))
#     lis = sorted(lis, key=lambda bui: bui.z, reverse=True)
#     for i in range(len(lis) - 1):
#         for j in range(i + 1, len(lis)):
#             lis[i] += lis[j]
#     return len([x for x in lis if x.line])


# def checkio(b):
#     def v(d,r=False,z={}):
#         for x in range(d[0],d[2]):
#             if d[4]>z.get(x,0): r,z[x]=True,d[4]
#         return r
#     return sum(map(v,sorted(b,key=lambda d: d[1])))

def checkio(buildings):
    return sum(any(all(s[4] < f[4]
                       for s in buildings
                       if s != f
                       and s[0] <= x / 2 <= s[2]
                       and s[1] <= f[1])
                   for x in range(f[0] * 2, f[2] * 2 + 1))
               for f in buildings)


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [1, 1, 3, 3, 6],
        [4, 1, 7, 3, 6],
        [8, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third_1"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
