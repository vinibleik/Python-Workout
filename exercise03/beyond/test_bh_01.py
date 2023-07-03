import pytest
from bh_01 import format_float


@pytest.mark.parametrize(
    ("n", "before", "after", "result"),
    (
        (0.0, 2, 3, 0.000),
        (3.14159, 2, 3, 3.141),
        (3.14159, 10, 10, 3.14159),
        (3.14159, 0, 3, 0.141),
        (3.14159, 10, 0, 3.0),
        (10.123456, 1, 2, 0.12),
        (1234.5678, 2, 3, 34.567),
        (42.0, 2, 3, 42.0),
        (-3.14159, 2, 3, -3.141),
        (12345.0, 3, 1, 345.0),
        (987654.0, 10, 1, 987654.0),
    ),
)
def test_fomart_float(
    n: float, before: int, after: int, result: float
) -> None:
    assert format_float(n, before, after) == result


@pytest.mark.parametrize(
    ("n", "before", "after"),
    (
        (1234.5678, -2, 3),
        (1234.5678, 2, -3),
        (1234.5678, -2, -3),
    ),
)
def test_format_float_exception(n: float, before: int, after: int) -> None:
    with pytest.raises(ValueError) as exec_info:
        format_float(n, before, after)

    assert exec_info.value.args[0] == "Format numbers must be positives!"
