# def possible_permutations(ls):
    # if len(ls) <= 1:
    #     yield ls
    #
    # else:
    #     for i in range(len(ls)):
    #         for permutation in possible_permutations(ls[:i] + ls[i+1:]):
    #             yield [ls[i]] + permutation

import itertools

def possible_permutations(ls):
    for permutation in itertools.permutations(ls):
        yield list(permutation)

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
