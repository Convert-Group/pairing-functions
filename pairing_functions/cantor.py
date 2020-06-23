# -*- coding: utf-8 -*-

from collections import deque
from math import pow, floor, sqrt


def pair(*numbers: int) -> int:
    """
    Maps a pair of non-negative integers to a uniquely associated single non-negative integer.
    Pairing also generalizes for `n` non-negative integers, by recursively mapping the first pair.
    For example, to map the following tuple:
    (n_1, n_2, n_3)
    the n_1, n_2 pair is mapped accordingly to a number n_p,
    and then the n_p, n3 pair is mapped to produce the final association.
    """
    if len(numbers) < 2:
        raise ValueError('Cantor pairing function needs at least 2 numbers as input')

    elif any((n < 0) or (not isinstance(n, int)) for n in numbers):
        raise ValueError('Cantor pairing function maps only non-negative integers')

    numbers = deque(numbers)

    # fetch the first two numbers
    n1 = numbers.popleft()
    n2 = numbers.popleft()

    mapping = (n1 + n2) * (n1 + n2 + 1) / 2 + n2

    mapping = int(mapping)

    if not numbers:
        # recursion concludes
        return mapping
    else:
        numbers.appendleft(mapping)
        return pair(*numbers)


def unpair(number: int, n: int = 2) -> tuple:
    """
    The inverse function outputs the pair associated with a non-negative integer.
    Unpairing also generalizes by recursively unpairing a non-negative integer to `n` non-negative integers.
    For example, to associate a `number` with three non-negative
    integers n_1, n_2, n_3, such that:

    pairing(n_1, n_2, n_3) = `number`

    the `number` will first be unpaired to n_p, n_3, then the n_p will be unpaired to n_1, n_2,
    producing the desired n_1, n_2 and n_3.
    """
    if (number < 0) or (not isinstance(number, int)):
        raise ValueError('Cantor unpairing function requires a non-negative integer')

    w = floor((sqrt(8 * number + 1) - 1) / 2)
    t = (pow(w, 2) + w) / 2

    n2 = int(number - t)
    n1 = int(w - n2)

    if n > 2:
        return unpair(n1, n - 1) + (n2,)
    else:
        # recursion concludes
        return n1, n2
