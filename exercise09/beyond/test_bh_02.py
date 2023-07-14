from typing import Any, Iterable

import pytest
from bh_02 import plus_minus


@pytest.mark.parametrize(
    ("iter", "result"),
    (
        ([], 0),
        ({}, 0),
        ([1], 1),
        ([1.0], 1.0),
        ({1: ""}, 1),
        ([1, 1], 0),
        ([1.0, 1.0], 0.0),
        ({1: "", 1.0: ""}, 1),
        ([1, 2], -1),
        ([1.0, 2.0], -1.0),
        ({1: "", 2: ""}, -1),
        ([10, 20, 30, 40, 50, 60], -30),
        ([10, 20, 30, 40, 50, 60.0], -30.0),
        ({10: "", 20: "", 30: "", 40: "", 50: "", 60.0: ""}, -30.0),
    ),
)
def test_plus_minus(iter: Iterable, result: int | float) -> None:
    assert plus_minus(iter=iter) == result


@pytest.mark.parametrize("iter", ("strings", {"str": 1}))
def test_exception_plus_minus(iter: Any) -> None:
    with pytest.raises(expected_exception=(ValueError, TypeError)):
        plus_minus(iter=iter)
