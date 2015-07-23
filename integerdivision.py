# How do you do integer division without actually using division? This
# is one answer. It's an extension of repeated subtraction, except
# that we start by finding the largest number n such that b*2^n <=
# a. Then we subtract b*2^n from a, and add 2^n to the quotient. And
# then we do the same for b*2^(n-1). And so on, all the way down to b
# itself.
#
# This process is very related to converting to binary (base 2). We're
# representing a as a polynomial of the form:
#
# a = b * x(n) * 2^n + b * x(n-1) * 2^(n-1) + ... + b * x(0) * 2^0 + R
#   = b * (x(n) * 2^n + x(n-1) * 2^(n-1) + ... + x(0) * 2^0) + R
#
# Then we get something pretty close to a/b with some algebra:
#
# (a - R) / b = x(n) * 2^n + x(n-1) * 2^(n-1) + ... + x(0) * 2^0
#
# If R is the remainder (and thus R < b and a - R is divisible by b),
# then
#
# floor(a / b) = (a - R) / b
#
# And floor(a/b) is what we're aiming for. We thus only need to find
# the sum
#
# x(n) * 2^n + x(n-1) * 2^(n-1) + ... + x(0) * 2^0
#
# that satisfies the equation, and can do that by simply subtracting
# the largest term (multiplied by b) from a, and keep a running total
# of the actual not-multiplied-by-b sum as we go.
#
# This is probably the clearest explanation you'll get here. The code
# itself is .... not well documented. Good luck!


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
