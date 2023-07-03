import contextlib
from typing import Any


def sum_all_integers(arr: list[Any]) -> int:
    total = 0
    for item in arr:
        with contextlib.suppress(TypeError):
            total += int(item)
    return total
