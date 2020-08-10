""" Lab 13: Final Review """

# Q3
def permutations(lst):
    if not lst:
        yield []
        return
    if len(lst) == 1:
        yield lst
    else:
        for perm in permutations(lst[1:]):
            # print(perm)
            for i in range(len(perm) + 1):
                yield perm[:i] + [lst[0]] + perm[i:]

# print(sorted(permutations([1, 2, 3])))


