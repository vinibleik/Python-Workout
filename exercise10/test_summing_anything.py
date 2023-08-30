import pytest
from summing_anything import mysum


@pytest.mark.parametrize(
    ("seq", "expected"),
    (
        (("abc", "def"), "abcdef"),
        (([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6]),
        ((1, 2, 3), 6),
    ),
)
def test_mysum(seq, expected) -> None:
    assert mysum(*seq) == expected
