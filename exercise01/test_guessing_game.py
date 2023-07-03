import random

from guessing_game import guessing_game
from pytest import CaptureFixture, MonkeyPatch, raises


def test_correct_anser(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda x, y: 49)
    monkeypatch.setattr("builtins.input", lambda x: "49")

    guessing_game()

    captured = capsys.readouterr()

    assert captured.out == "Correct Answer!\n"


def test_low_answer(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda x, y: 49)
    it = iter(["10", "49"])
    monkeypatch.setattr("builtins.input", lambda x: next(it))

    guessing_game()

    captured = capsys.readouterr()

    assert captured.out.startswith("Too low\n")
    assert captured.out.endswith("Correct Answer!\n")


def test_high_answer(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda x, y: 49)
    it = iter(["100", "49"])
    monkeypatch.setattr("builtins.input", lambda x: next(it))

    guessing_game()

    captured = capsys.readouterr()

    assert captured.out.startswith("Too high\n")
    assert captured.out.endswith("Correct Answer!\n")


def test_low_high_answer(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda x, y: 49)
    it = iter(["10", "100", "49"])
    monkeypatch.setattr("builtins.input", lambda x: next(it))

    guessing_game()

    captured = capsys.readouterr()

    assert captured.out.startswith("Too low\n")
    assert "Too high" in captured.out
    assert captured.out.endswith("Correct Answer!\n")


def test_value_error(
    monkeypatch: MonkeyPatch, capsys: CaptureFixture[str]
) -> None:
    monkeypatch.setattr("random.randint", lambda x, y: 49)
    it = iter(["error", "49"])
    monkeypatch.setattr("builtins.input", lambda x: next(it))

    guessing_game()

    captured = capsys.readouterr()

    assert captured.out.startswith(
        "Invalid input! Please enter an valid Integer!\n"
    )
    assert captured.out.endswith("Correct Answer!\n")
