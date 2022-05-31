from array import array
import reprlib
import math
import functools
import operator

from ex_10_10__vector_v3_b import VectorV3B


class VectorV4(VectorV3B):
    typecode = 'd'

    # Example 10-12
    # def __eq__(self, other):
    #     return tuple(self) == tuple(other)

    # Example 10-13
    # def __eq__(self, other):
    #     if len(self) != len(other):
    #         return False
    #     for a, b in zip(self, other):
    #         if a != b:
    #             return False
    #     return True

    # Example 10-14
    def __eq__(self, other):
        return len(self) == len(other) and all(
            a == b for a, b in zip(self, other)
        )

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)
