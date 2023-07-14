from typing import Sequence


def even_odd_sums(iter: Sequence[int | float]) -> tuple[int | float, int | float]:
    """
    This function returns the a tuple containing the sum of even-indexed elements of iter and the sum of the odd-indexed elements of iter.

    Args:
        iter (Sequence[int  |  float]): A sequence of numbers that support the mathematical addition operation.

    Raises:
        TypeError: If the elements on iter does not support mathematical addition.

    Returns:
        tuple[int | float, int | float]: The sum of even-indexed elements of iter, sum of the odd-indexed elements of iter.
    """
    return (sum(iter[::2]), sum(iter[1::2]))
