import pytest

from bh_03 import myzip


@pytest.mark.parametrize(
    "iterables",
    (
        [[]],
        [(1, 2, 3, 4)],
        [(1, 2, 3, 4), []],
        [(1, 2, 3, 4), "abc", [0, 9, 8, 7, 6]],
        [(1, 2, 3, 4), "", [0, 9, 8, 7, 6]],
        [(1, 2, 3, 4), "abc", {1: "test", "test": 1}],
        [(1, 2, 3, 4), "abc", [0, 9, 8, 7, 6]],
        [{1: "test", "test": 1}],
    ),
)
def test_myzip(iterables) -> None:
    for zip_v, my_v in zip(zip(*iterables), myzip(*iterables)):
        assert zip_v == my_v
