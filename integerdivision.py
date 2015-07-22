def divide(a, b):
    """
    >>> divide(3, 1)
    3
    >>> divide(100, 16)
    6
    >>> divide(10000, 17)
    588
    >>> divide(1, 17)
    0
    >>> divide(1, 1)
    1
    >>> divide(1000000000000, 2)
    500000000000
    """
    # Find the power of two that we're less than, ish.
    base = 2
    power = 0
    powerbases = [1]
    while b * powerbases[-1] < a:
        power += 1
        powerbases.append(powerbases[-1]*base)

    # Okay, now start adding up the decomposed multiplicands.
    q = 0
    while power >= 0:
        if b*powerbases[-1] <= a:
            q += powerbases[-1]
            a -= powerbases[-1]*b
        power -= 1
        powerbases.pop(-1)
    return q

import doctest
doctest.testmod()
