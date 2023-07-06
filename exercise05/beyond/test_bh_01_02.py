import pytest
from bh_01_02 import pig_latin


@pytest.mark.parametrize(
    ("word", "result"),
    (
        ("a", "away"),
        ("b", "bay"),
        ("air", "airway"),
        ("python", "ythonpay"),
        ("eat", "eatway"),
        ("computer", "omputercay"),
        ("A", "Away"),
        ("B", "Bay"),
        ("air.", "airway."),
        ("python!", "ythonpay!"),
        ("Eat?", "Eatway?"),
        ("Computer,", "Omputercay,"),
    ),
)
def test_pig_latin(word: str, result: str) -> None:
    assert pig_latin(word=word) == result
