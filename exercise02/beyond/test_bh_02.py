import pytest
from bh_02 import mean


@pytest.mark.parametrize(
    ("numbers", "result"),
    (
        ([], 0.0),
        ([23], 23.0),
        (list(range(1, 11)), 5.5),
        ([1, 2, 3, 4.0], 2.5),
        ([-1, 2, 3, -4.0], 0.0),
        ([-1, -2, -3, -4], -2.5),
    ),
)
def test_mean(numbers: list[int | float], result: float) -> None:
    assert mean(numbers) == result


@pytest.mark.parametrize(
    "numbers",
    (
        ["a"],
        [1, 3, 4, 5, 31, "dasffa"],
        [
            [1, 2, 3],
            [
                1,
                2,
                3,
            ],
        ],
        [{"a": 1}],
    ),
)
def test_my_sum_exception(numbers) -> None:
    with pytest.raises(ValueError) as exec_info:
        mean(numbers)

    assert exec_info.type is ValueError
    assert exec_info.value.args[0] == "All the arguments must be numbers"
