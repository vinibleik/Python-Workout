from typing import Any

import pytest
from first_last import first_last


@pytest.mark.parametrize(
    ("seq", "result"),
    (
        ("", ""),
        ([], []),
        ((), ()),
        ("a", "aa"),
        ([1], [1, 1]),
        (({"a": 1},), ({"a": 1}, {"a": 1})),
        ("ab", "ab"),
        ([3.4, 4.5], [3.4, 4.5]),
        (({"a": 1}, {"b": [1]}), ({"a": 1}, {"b": [1]})),
        ("abcdefg", "ag"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9]),
        (
            (
                {"a": 1},
                {"b": [1]},
                {"c": "test"},
                {"d": "test"},
                {"e": "name", 1: [0, 0]},
            ),
            ({"a": 1}, {"e": "name", 1: [0, 0]}),
        ),
    ),
)
def test_first_last(seq: Any, result: Any) -> None:
    output: Any = first_last(seq=seq)
    assert len(output) in {0, 2}
    assert type(output) == type(result)
    assert output == result


@pytest.mark.parametrize("seq", ({}, 2, 2.3))
def test_exception_first_last(seq: Any) -> None:
    with pytest.raises(expected_exception=TypeError):
        first_last(seq=seq)
