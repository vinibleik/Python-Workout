import pytest
from bh_02 import transpose_string


@pytest.mark.parametrize(
    ("arr", "result"),
    (
        ([""], []),
        (["ab"], ["ab"]),
        (["ab ba"], ["ab", "ba"]),
        (["ab ba"], ["ab", "ba"]),
        (["ab ba cc"], ["ab", "ba", "cc"]),
        (["ab ba", "ab ba"], ["ab ab", "ba ba"]),
        (
            ["ab ba cc", "ab ba cc", "ab ba cc"],
            ["ab ab ab", "ba ba ba", "cc cc cc"],
        ),
        (["ab", "ba"], ["ab ba"]),
        (["ab", "ba", "cc"], ["ab ba cc"]),
        (["ab ba", "ee"], ["ab ee"]),
        (["ab ba cc", "dd ee", "ff"], ["ab dd ff"]),
    ),
)
def test_transpose_string(arr: list[str], result: list[str]) -> None:
    assert transpose_string(arr) == result
