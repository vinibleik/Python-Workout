from ubbi_dubbi import ubbi_dubbi

import pytest


@pytest.mark.parametrize(
    ("input", "output"),
    (
        ("", ""),
        ("a", "uba"),
        ("b", "b"),
        ("milk", "mubilk"),
        ("program", "prubogrubam"),
        ("octopus", "uboctubopubus"),
        ("elephant", "ubelubephubant"),
    ),
)
def test_ubbi_dubbi(input: str, output: str) -> None:
    assert ubbi_dubbi(input) == output
