import pytest
from bh_03 import pig_latin_2


@pytest.mark.parametrize(
    ("word", "result"),
    (
        ("a", "aay"),
        ("b", "bay"),
        ("ae", "aeway"),
        ("ab", "baay"),
        ("wine", "wineway"),
        ("wind", "indway"),
    ),
)
def test_pig_latin_2(word: str, result: str) -> None:
    assert pig_latin_2(word) == result
