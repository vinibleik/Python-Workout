import pytest
from most_repeated_letters import most_repeated_letters


@pytest.mark.parametrize(
    "strings, expected",
    [
        ([], None),
        (["this"], "this"),
        (["this", "is"], "this"),
        (["this", "is", "an", "elementary", "test", "example"], "elementary"),
        (["this", "is", "an", "elementary", "test", "example", "test"], "elementary"),
        (
            ["this", "is", "an", "elementary", "test", "example", "test", "test"],
            "elementary",
        ),
        (
            [
                "this",
                "is",
                "an",
                "elementary",
                "test",
                "example",
                "test",
                "test",
                "test",
            ],
            "elementary",
        ),
        (
            [
                "this",
                "is",
                "an",
                "elementary",
                "test",
                "example",
                "test",
                "test",
                "test",
                "test",
            ],
            "elementary",
        ),
        (
            [
                "this",
                "is",
                "an",
                "elementary",
                "test",
                "example",
                "test",
                "test",
                "test",
                "test",
                "test",
            ],
            "elementary",
        ),
    ],
)
def test_most_repeated_letters(strings: list[str], expected: str):
    assert most_repeated_letters(strings) == expected
