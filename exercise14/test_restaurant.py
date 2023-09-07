from typing import Generator

import pytest
from pytest import CaptureFixture, MonkeyPatch
from restaurant import restaurant

input_values = [
    [""],
    ["Test", ""],
    ["Pizza", ""],
    ["Pizza", "Burger", "Test", "Sushi", "Test", "Ice Cream", ""],
]

result_format = "Your total is {0:.2f}\n"


@pytest.mark.parametrize(
    "inputarr, result",
    (
        [iter(input_values[0]), 0.0],
        [iter(input_values[1]), 0.0],
        [iter(input_values[2]), 10.99],
        [iter(input_values[3]), 35.96],
    ),
)
def test_restaurant(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
    inputarr: Generator[str, None, None],
    result: float,
):
    monkeypatch.setattr("builtins.input", lambda _: next(inputarr))

    restaurant()

    out, _ = capsys.readouterr()

    assert out.endswith(result_format.format(result))
