from typing import Iterable


def plus_minus(iter: Iterable) -> int | float:
    """
    plus_minus iterate over iter summing and subtracting alternately.

    Args:
        iter (Iterable): A iterable of numbers.

    Raises:
        TypeError: If the elements don't support mathematical addition

    Returns:
        int | float: Result of alternately adding and subtracting numbers from iter.
    """
    total, i = 0, 1

    for value in iter:
        total += value * i
        i *= -1

    return total
