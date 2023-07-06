import pytest
from pig_latin import pig_latin


@pytest.mark.parametrize(
    ("word", "result"),
    (
        ("a", "away"),
        ("b", "bay"),
        ("air", "airway"),
        ("python", "ythonpay"),
        ("eat", "eatway"),
        ("computer", "omputercay"),
    ),
)
def test_pig_latin(word: str, result: str) -> None:
    assert pig_latin(word=word) == result
