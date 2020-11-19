def power_supply(network: list[list], plant: dict, lis=None) -> set:
    if not lis: lis = []
    net = network.copy()
    for key, value in plant.items():
        for [a, b] in tuple(net):
            if key in [a, b]:
                net.remove([a, b])
                if value > 0:
                    lis.append(a if key == b else b)
                    if value > 1:
                        power_supply(net, {lis[-1]: value - 1}, lis)
    return set([item for net in network for item in net]) - set(lis) - set(plant.keys())

# def power_supply(network, power_plants):
#     out = {x for y in network for x in y}
#     queue = list(power_plants.items())
#     for k, v in ((x, y) for x, y in queue if y >= 0):
#         queue += [(j if k == i else i, v-1) for i, j in network if k in (i, j)]
#         out -= {k}
#     return out


if __name__ == '__main__':
    print(power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                        ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                        ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                        ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                       {'p0': 1, 'p12': 4, 'p8': 1}))  # set(['c0', 'c3']
