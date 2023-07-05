import pytest
from hexa_output import hex_output


@pytest.mark.parametrize(
    ("hex_number", "result"),
    (
        ("0", 0),
        ("0x", 0),
        ("0x0000000", 0),
        ("0XA", 10),
        ("c", 12),
        ("0x15", 21),
        ("2a45f", 173151),
        ("0xAfdEBc", 11525820),
        ("0x123456789abcdefABCDEF", 1375488932539311409843695),
        ("123456789abcdefABCDEF", 1375488932539311409843695),
    ),
)
def test_hex_output(hex_number: str, result: int) -> None:
    assert hex_output(hex_number=hex_number) == result


@pytest.mark.parametrize(
    "hex_number",
    (
        "h",
        "test",
        "1324g314",
        "0x123456789abcdefABCDEFg",
        "123456789abcdefABCDEFg",
        "0xfffffx",
        "xxxx",
    ),
)
def test_hex_output_error(hex_number: str) -> None:
    with pytest.raises(ValueError) as exc:
        hex_output(hex_number)

    assert str(exc.value).startswith("invalid literal for int() with base 16:")
