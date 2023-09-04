import pytest
from beyond import most_repeated_vowels


@pytest.mark.parametrize(
    "words, expected",
    [
        ([], ""),
        (["hello", "world"], "hello"),
        (["a", "b", "c", "d", "e"], "a"),
        (["aa", "bb", "cc", "dd", "ee"], "aa"),
        (["aaa", "bbb", "ccc", "ddd", "eee"], "aaa"),
    ],
)
def test_most_repeated_vowels(words: list[str], expected: str):
    assert most_repeated_vowels(words) == expected
