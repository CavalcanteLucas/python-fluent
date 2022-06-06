from array import array
import numbers
import setup
from Chap_10__Sequence_Hacking_Hashing_and_Slicing.ex_10_16__vector_v5 import Vector
import itertools

class VectorV10(Vector):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return VectorV10(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar


    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return VectorV10(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
