from typing import Any, Sequence

import pytest
from bh_01 import even_odd_sums


@pytest.mark.parametrize(
    ("iter", "result"),
    (
        ([], (0, 0)),
        ([1], (1, 0)),
        ([1.0], (1.0, 0)),
        ([0, 1], (0, 1)),
        ([0.0, 1.0], (0.0, 1.0)),
        ([10, 20, 30, 40, 50, 60], (90, 120)),
        ([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], (9.0, 12.0)),
    ),
)
def test_even_odd_sums(
    iter: Sequence[int | float], result: tuple[int | float, int | float]
) -> None:
    assert even_odd_sums(iter=iter) == result


@pytest.mark.parametrize(
    "iter",
    (
        "test",
        {"1": 1, "2": 2},
        {
            1: "",
            2: "",
        },
    ),
)
def test_exception_even_odd_sums(iter: Any) -> None:
    with pytest.raises(expected_exception=TypeError):
        even_odd_sums(iter=iter)
