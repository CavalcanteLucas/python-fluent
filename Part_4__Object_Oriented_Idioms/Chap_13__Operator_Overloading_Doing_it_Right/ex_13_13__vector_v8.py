import setup

from Chap_10__Sequence_Hacking_Hashing_and_Slicing.ex_10_16__vector_v5 import Vector

class VectorV8(Vector):
    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and
                    all(a == b for a, b in zip(self, other)))
        else:
            return NotImplemented
