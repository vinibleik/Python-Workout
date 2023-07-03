from typing import Any


def compare_words(words: list[Any]) -> tuple[int, int, float]:
    if not words:
        return (0, 0, 0.0)

    if len_words := [len(word) for word in words if isinstance(word, str)]:
        return (
            min(len_words, default=0),
            max(len_words, default=0),
            sum(len_words) / len(len_words),
        )
    else:
        return (0, 0, 0.0)
