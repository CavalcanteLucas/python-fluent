import setup
import itertools

from Chap_11__Interfaces_From_Protocols_to_ABCs.ex_11_9__tombola import Tombola
from Chap_11__Interfaces_From_Protocols_to_ABCs.ex_11_12__bingo import (
    BingoCage,
)

import random


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()


class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'right operand in += must be {!r} or an iterable'
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self
