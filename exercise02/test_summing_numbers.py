import pytest
from summing_numbers import my_sum


@pytest.mark.parametrize(
    ("numbers", "result"),
    (
        ([], 0),
        ([23], 23),
        (list(range(11)), 55),
        ([1, 2, 3, 4.0], 10.0),
        ([-1, 2, 3, -4.0], 0.0),
        ([-1, -2, -3, -4], -10),
    ),
)
def test_my_sum(numbers: list[int | float], result: int | float) -> None:
    assert my_sum(*numbers) == result


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
        my_sum(*numbers)

    assert exec_info.type is ValueError
    assert exec_info.value.args[0] == "All the arguments must be numbers"
