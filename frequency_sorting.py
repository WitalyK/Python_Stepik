from collections import Counter


def frequency_sorting(haos):
    ords = sorted([[element] * count for element, count in Counter(haos).most_common()], key=lambda x: (-len(x), x))
    return sum(ords, [])


#  frequency_sorting = lambda numbers: sorted(sorted(numbers), key=numbers.count, reverse=True)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print(frequency_sorting(
        [3, 3, 3, 4, 4, 4, 4, 99, 110, 5, 2, 99, 55, 55, 21, 21, 10, 10]))  # == [5, 5, 5, 6, 6, 3, 8, 11]
