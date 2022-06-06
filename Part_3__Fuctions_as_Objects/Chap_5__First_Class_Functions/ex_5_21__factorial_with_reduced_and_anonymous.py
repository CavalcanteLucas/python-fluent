from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))
