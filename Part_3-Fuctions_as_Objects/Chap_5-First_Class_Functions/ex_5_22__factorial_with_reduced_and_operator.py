from functools import reduce
from operator import mul

def fact(n):
    return reduce(mul, range(1, n+1))