from pprint import pprint
from typing import Iterable, List, Tuple, Union

Node = Union[int, str]
Tree = Tuple[Node, List['Tree']]


def search(pair, tree, one=False):
    for item in tree:
        key, value = item
        if key in pair:
            if one: return True
            else: one = True
        if value:
            return search(pair, value, one)
    # return False


def on_same_path(tree: Tree, pairs: List[Tuple[Node, Node]]) -> Iterable[bool]:
    """For each given pair of tree's nodes, say if there are on a same path."""
    return [search(pair, [tree]) for pair in pairs]


if __name__ == '__main__':
    pprint(on_same_path(
        (0, [(1, [(2, []),
                  (3, [])]),
             (4, [(5, []),
                  (6, [])]),
             (7, [(8, []),
                  (9, [])])]),
        [(4, 2), (0, 5), (2, 3), (9, 2), (6, 4), (7, 8), (8, 1)],
    ))

    # [False, True, False, False, True, True, False]
    # print(list(example))
    #
    # TESTS = (
    #     (
    #         ('Me', [('Daddy', [('Grandpa', []),
    #                            ('Grandma', [])]),
    #                 ('Mom', [('Granny', []),
    #                          ('?', [])])]),
    #         [('Grandpa', 'Me'), ('Daddy', 'Granny')],
    #         [True, False],
    #     ),
    #     (
    #         (1, [(2, [(4, []),
    #                   (5, [(7, []),
    #                        (8, []),
    #                        (9, [])])]),
    #              (3, [(6, [])])]),
    #         [(1, 5), (2, 9), (2, 6)],
    #         [True, True, False],
    #     ),
