import pytest
from beyond import sort_by_line_sum, sort_by_mod, sort_by_n_vowels


@pytest.mark.parametrize(
    ("numbers", "expected"),
    (
        ([], []),
        ([1], [1]),
        ([-1], [-1]),
        ([1, -1], [1, -1]),
        ([9, -3, 0, -17], [0, -3, 9, -17]),
    ),
)
def test_sort_by_mod(numbers: list[int], expected: list[int]):
    assert sort_by_mod(numbers) == expected


@pytest.mark.parametrize(
    ("strings", "expected"),
    (
        ([], []),
        (["hello"], ["hello"]),
        (
            ["apple", "banana", "orange", "grape"],
            ["apple", "grape", "banana", "orange"],
        ),
        (["grape", "banana", "hello", "apple"], ["grape", "hello", "apple", "banana"]),
        (
            ["apple", "Banana", "ORANGE", "grape"],
            ["apple", "grape", "Banana", "ORANGE"],
        ),
        (["cat", "dog", "rabbit", "snake"], ["cat", "dog", "rabbit", "snake"]),
    ),
)
def test_sort_by_n_vowels(strings: list[str], expected: list[str]):
    assert sort_by_n_vowels(strings) == expected


@pytest.mark.parametrize(
    "numbers_list, expected",
    [
        ([], []),
        ([[1, 2, 3], [4, 5], [6, 7, 8, 9]], [[1, 2, 3], [4, 5], [6, 7, 8, 9]]),
        ([[9, 8], [5, 5, 5], [1, 2, 3, 4]], [[1, 2, 3, 4], [5, 5, 5], [9, 8]]),
        ([[1, 1, 1], [2, 2], [3, 3, 3, 3]], [[1, 1, 1], [2, 2], [3, 3, 3, 3]]),
        ([[3, 6, 9], [2, 4, 8], [1, 5, 7]], [[1, 5, 7], [2, 4, 8], [3, 6, 9]]),
    ],
)
def test_sort_by_line_sum(numbers_list: list[list[int]], expected: list[list[int]]):
    assert sort_by_line_sum(numbers_list) == expected
