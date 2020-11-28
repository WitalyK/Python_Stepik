from typing import Iterable


# def mediana(data: list[int]) -> [int, float]:
#     l = sorted(data)
#     if len(l) % 2 != 0:
#         return l[int(len(l) / 2)]
#     else:
#         return (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2

# def mediana(data: list[int]) -> int:
#     l = sorted(data)
#     return l[int(len(l) / 2)]
#
#
# def median_three(els: Iterable[int]) -> Iterable[int]:
#     if len(els) < 3:
#         return els
#     return els[:2] + [mediana(els[i - 2:i + 1]) for i, _ in enumerate(els[2:], 2)]

def median_three(els):
    return (els[i] if i < 2 else sorted(els[i-2:i+1])[1] for i in range(len(els)))
    # els[:2] + [sorted(els[i:i + 3])[1] for i in range(len(els) - 2)]

if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
