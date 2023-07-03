from typing import Iterable

import pytest
from pytest import CaptureFixture, MonkeyPatch
from run_timing import run_timing


@pytest.mark.parametrize(
    ("input_arr", "result"),
    (
        (iter([""]), "You didn't run!\n"),
        (iter(["10", "20", "15", ""]), "Average of 15.0, over 3 runs!\n"),
        (
            iter(["test", "10", "test", "20", ""]),
            "Average of 15.0, over 2 runs!\n",
        ),
        (
            iter(
                [
                    "test",
                    "10",
                    "test",
                    "20",
                    "test",
                    "10",
                    "test",
                    "20",
                    "test",
                    "10",
                    "test",
                    "20",
                    "test",
                    "10",
                    "test",
                    "20",
                    "",
                ]
            ),
            "Average of 15.0, over 8 runs!\n",
        ),
    ),
)
def test_run_timing(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
    input_arr: Iterable[str],
    result: str,
) -> None:
    monkeypatch.setattr("builtins.input", lambda x: next(input_arr))
    run_timing()
    captured = capsys.readouterr()

    assert captured.out.endswith(result)
