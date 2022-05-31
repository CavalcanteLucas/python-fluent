from array import array
import numbers
from copies.ex_10_16__vector_v5_copy import Vector


class VectorV7(Vector):
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return VectorV7(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar
