import pytest
from bh_02 import triangle_name
from pytest import CaptureFixture


@pytest.mark.parametrize(
    ("name", "result"),
    (
        ("", "\n"),
        ("a", "\na\n"),
        ("test", "\nt\nte\ntes\ntest\n"),
        ("vinicius", "\nv\nvi\nvin\nvini\nvinic\nvinici\nviniciu\nvinicius\n"),
    ),
)
def test_triangle_name(capsys: CaptureFixture[str], name: str, result: str):
    triangle_name(name=name)

    captured_out, _ = capsys.readouterr()

    assert captured_out == result
