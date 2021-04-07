from itertools import permutations


def possible_permutations(values):
    for el in permutations(values):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]


