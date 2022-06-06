import setup

import itertools
from Chap_10__Sequence_Hacking_Hashing_and_Slicing.ex_10_16__vector_v5 import (
    Vector,
)


class VectorV9(Vector):
    typecode = 'd'

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return VectorV9(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other
