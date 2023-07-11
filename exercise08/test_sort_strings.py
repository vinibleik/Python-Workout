from sort_strings import strsort

import pytest


@pytest.mark.parametrize(
    ("string", "result"),
    (
        ("", ""),
        ("cba", "abc"),
        ("1a2b", "12ab"),
        ("Aa", "Aa"),
        ("aA1", "1Aa"),
    ),
)
def test_strsort(string: str, result: str) -> None:
    assert strsort(string=string) == result
