import random

# for when running from Chap 11:
# from ex_11_9__tombola import Tombola

# for when running from other chaps:
from Chap_11__Interfaces_From_Protocols_to_ABCs.ex_11_9__tombola import (
    Tombola,
)


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
