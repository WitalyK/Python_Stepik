from pprint import pprint


def unfair_districts(number, data):
    height, width = len(data), len(data[1])
    valid = {(x, y) for y in range(width) for x in range(height)}
    out = [['']*width for _ in range(height)]
    stack = [((0, 0), [((0,0),)])]
    while stack:
        (x, y), area = stack.pop()
        if len(sum(area, ())) == height*width:
            wins, loses = 0, 0
            for i in area:
                a = sum([data[x][y][0] for x, y in i])
                b = sum([data[x][y][1] for x, y in i])
                wins, loses = wins+(a > b), loses+(a < b)
            if wins <= loses: continue
            for k, i in enumerate(area):
                for a, b in i: out[a][b] = str(k)
            return [''.join(j) for j in out]
        last_group = area.pop()
        group_sum = sum(sum([data[i][j] for i, j in last_group], []))
        if group_sum > number: continue
        if group_sum == number: area, last_group = area+[last_group], ()
        neighbors = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} & valid
        for i in (neighbors - set(sum(area, ())+last_group)):
            stack += [(i, area+[last_group+(i,)])]
            if len(last_group) in [1, 2]:
                stack += [(last_group[-1], area+[last_group+(i,)])]


if __name__ == '__main__':
    pprint(unfair_districts(5, [[[2, 1], [1, 1], [1, 2]],
                                [[2, 1], [1, 1], [0, 2]]]))
#
# pprint(unfair_districts(9, [[[0, 3], [3, 3], [1, 1], [3, 3]],
#                             [[1, 2], [1, 0], [1, 1], [1, 1]],
#                             [[0, 3], [2, 1], [2, 2], [1, 0]]]))

# pprint(unfair_districts(9, [
#     [[0, 3], [3, 3], [1, 1]],
#     [[1, 2], [1, 0], [1, 1]],
#     [[0, 3], [2, 1], [2, 2]]]))
# from itertools import chain
# from collections import defaultdict
#
# def checker(solution, amount_of_people, grid, win_flg=True):
#
#     w, h = len(grid[0]), len(grid)
#     size = w * h
#     cell_dic = {}
#
#     # make cell_dic
#     def adj_cells(cell):
#         result = []
#         if cell % w != 1 and cell - 1 > 0:
#             result.append(cell - 1)
#         if cell % w and cell + 1 <= size:
#             result.append(cell + 1)
#         if (cell - 1) // w:
#             result.append(cell - w)
#         if (cell - 1) // w < h - 1:
#             result.append(cell + w)
#         return set(result)
#
#     for i, v in enumerate(chain(*grid)):
#         cell_dic[i + 1] = {'vote': v, 'adj': adj_cells(i + 1)}
#
#     answer = solution(amount_of_people, grid)
#
#     if answer == [] and not win_flg:
#         return True
#
#     if not isinstance(answer, list):
#         print('wrong data type :', answer)
#         return False
#     else:
#         if len(answer) != h:
#             print('wrong data length', answer)
#             return False
#         for an in answer:
#             if len(an) != w:
#                 print('wrong data length', an)
#                 return False
#
#     ds_dic = defaultdict(list)
#     for i, r in enumerate(''.join(answer), start=1):
#         ds_dic[r].append(i)
#
#     # answer check
#     def district_check(d):
#         all_cells = set(d[1:])
#         next_cells = cell_dic[d[0]]['adj'] & set(d)
#         for _ in range(len(d)):
#             all_cells -= next_cells
#             next_cells = set(chain(*[list(cell_dic[nc]['adj']) for nc in next_cells])) & set(d)
#         return not all_cells
#
#     for ch, cells in ds_dic.items():
#         dist_people = sum(sum(cell_dic[c]['vote']) for c in cells)
#         if not district_check(cells):
#             print('wrong district: ', ch)
#             return False
#         if dist_people != amount_of_people:
#             print('wrong people:', ch)
#             return False
#
#     # win check
#     win, lose = 0, 0
#     for part in ds_dic.values():
#         vote_a, vote_b = 0, 0
#         for p in part:
#             a, b = cell_dic[p]['vote']
#             vote_a += a
#             vote_b += b
#         win += vote_a > vote_b
#         lose += vote_a < vote_b
#
#     return win > lose
#
# assert checker(unfair_districts, 5, [
#     [[2, 1], [1, 1], [1, 2]],
#     [[2, 1], [1, 1], [0, 2]]]), '3x2grid'
#
# assert checker(unfair_districts, 9, [
#     [[0, 3], [3, 3], [1, 1]],
#     [[1, 2], [1, 0], [1, 1]],
#     [[0, 3], [2, 1], [2, 2]]]), '3x3gid'
#
# assert checker(unfair_districts, 8, [
#     [[1, 1], [2, 0], [2, 0], [3, 3]],
#     [[1, 1], [1, 2], [1, 1], [0, 3]],
#     [[1, 1], [1, 1], [1, 2], [0, 3]],
#     [[1, 1], [1, 1], [1, 1], [2, 0]]]), '4x4gid'
#
# print('check done')
