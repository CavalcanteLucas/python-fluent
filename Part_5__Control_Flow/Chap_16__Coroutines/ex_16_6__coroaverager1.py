"""
A coroutine to compute a running average

    >>> coro_avg = averager()
    >>> from inspect import getgeneratorstate
    >>> getgeneratorstate(coro_avg)
    'GEN_SUSPENDED'
    >>> coro_avg.send(10)
    10.0
    >>> coro_avg.send(30)
    20.0
    >>> coro_avg.send(5)
    15.0

"""

from ex_16_5__coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    averager = None
    while True:
        term = yield averager
        total += term
        count += 1
        averager = total/count