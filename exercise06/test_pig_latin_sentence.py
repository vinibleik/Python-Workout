import pytest
from pig_latin_sentence import pl_sentence


@pytest.mark.parametrize(
    ("sentence", "result"),
    (
        ("", ""),
        ("a", "away"),
        ("b", "bay"),
        ("this", "histay"),
        ("is", "isway"),
        (
            "this is a test translation",
            "histay isway away esttay ranslationtay",
        ),
    ),
)
def test_pl_sentence(sentence: str, result: str) -> None:
    assert pl_sentence(sentence=sentence) == result
