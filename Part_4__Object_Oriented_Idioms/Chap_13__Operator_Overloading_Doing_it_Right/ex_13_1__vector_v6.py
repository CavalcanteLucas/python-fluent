import setup

from Chap_10__Sequence_Hacking_Hashing_and_Slicing.ex_10_16__vector_v5 import (
    Vector,
)

import math


class VectorV6(Vector):
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)
