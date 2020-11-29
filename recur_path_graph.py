from typing import Iterable, List, Tuple, Union

Node = Union[int, str]
Tree = Tuple[Node, List['Tree']]


def search(pair, tree, one=False):
    for key, value in tree:
        if key in pair:
            if one:
                return True
            else:
                if value and search(pair, value, True):
                    return True
                else:
                    return False
        else:
            if value and search(pair, value, (one == True)):
                return True
    return False


def on_same_path(tree: Tree, pairs: List[Tuple[Node, Node]]) -> Iterable[bool]:
    """For each given pair of tree's nodes, say if there are on a same path."""
    return [search(pair, [tree]) for pair in pairs]