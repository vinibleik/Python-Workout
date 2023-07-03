import pytest
from bh_03 import compare_words


@pytest.mark.parametrize(
    ("words", "result"),
    (
        ([], (0, 0, 0.0)),
        (["test"], (4, 4, 4.0)),
        (["test", "world"], (4, 5, 4.5)),
        (["one", "two", "three", "hi"], (2, 5, 3.25)),
        (
            ["test", "pytest", "random", "vinicius", "book", "hello world"],
            (4, 11, 6.5),
        ),
    ),
)
def test_compare_words(
    words: list[str], result: tuple[int, int, float]
) -> None:
    assert compare_words(words=words) == result


@pytest.mark.parametrize(
    ("words", "result"),
    (
        ([12, 3, 4, 5], (0, 0, 0.0)),
        (["test", 12, 3, 4], (4, 4, 4.0)),
        ([1, 3, "test", 13, "world"], (4, 5, 4.5)),
        (
            ["one", 3.0, (1, 3, 4), "two", "three", "hi", {"b": 23}],
            (2, 5, 3.25),
        ),
        (
            [
                {"vini", "baggio"},
                ("test",),
                "test",
                "pytest",
                "random",
                "vinicius",
                "book",
                "hello world",
            ],
            (4, 11, 6.5),
        ),
    ),
)
def test_compare_words_with_dummy_data(
    words, result: tuple[int, int, float]
) -> None:
    assert compare_words(words=words) == result
