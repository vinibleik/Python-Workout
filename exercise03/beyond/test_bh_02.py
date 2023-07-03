from typing import Iterable

import pytest
from bh_02 import sum_decimal
from pytest import CaptureFixture, MonkeyPatch


@pytest.mark.parametrize(
    ("input_arr", "result"),
    (
        (iter(["0.1", "0.2"]), "0.1 + 0.2 = 0.3\n"),
        (iter(["1.23", "3.456"]), "1.23 + 3.456 = 4.686\n"),
        (iter(["0", "0"]), "0 + 0 = 0\n"),
        (iter(["0.99999", "0.00001"]), "0.99999 + 0.00001 = 1.00000\n"),
        (iter(["12", "12"]), "12 + 12 = 24\n"),
    ),
)
def test_sum_decimal(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
    input_arr: Iterable[str],
    result: str,
) -> None:
    monkeypatch.setattr("builtins.input", lambda x: next(input_arr))

    sum_decimal()

    captured = capsys.readouterr()

    assert captured.out == result


@pytest.mark.parametrize(
    "input_arr",
    (
        iter(["test", "0.2"]),
        iter(["1.23", "test"]),
    ),
)
def test_sum_decimal_exception(
    monkeypatch: MonkeyPatch,
    input_arr: Iterable[str],
) -> None:
    monkeypatch.setattr("builtins.input", lambda x: next(input_arr))

    with pytest.raises(ValueError) as e:
        sum_decimal()

    assert e.value.args[0] == "Enter an valid float as input"
