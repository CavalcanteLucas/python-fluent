from _collections_abc import Iterable
from abc import abstractmethod


class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        """Return the next item from the iterator. When exhausted, raise StopIteration"""
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if any('__next__' in B.__dict__ for B in C.__mro__) and any(
                '__iter__' in B.__dict__ for B in C.__mro__
            ):
                return True
        return NotImplemented
