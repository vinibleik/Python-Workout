from typing import Any

import pytest
from bh_04 import sum_all_integers


@pytest.mark.parametrize(
    ("arr", "result"),
    (
        ([], 0),
        ([1, 2, 3, 4, 5], 15),
        ([[1, 2, 3], [1, 2, 3], {"1"}, "1"], 1),
        (["1", "10", "0", (1,)], 11),
        ([{"b": 2, "c": 3}, "123"], 123),
    ),
)
def test_sum_all_integers(arr: list[Any], result: int) -> None:
    assert sum_all_integers(arr) == result
