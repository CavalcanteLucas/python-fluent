# pseudocode for:
# RESULT = yield from EXPR

"""
_i = iter(EXPR)
try:
    _y = next(_i)
except StopIteration as _e:
    _r = _e.value
else:
    while 1:
        _s = yield _y
        try:
            _y = _i.send(_s)
        except StopIteration as _e:
            _r = _e.value
            break

RESULT = _r
"""
