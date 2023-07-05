# hex_output without int funcion

from string import hexdigits

ALPHABET: dict[str, int] = {
    letter: integer for integer, letter in enumerate(hexdigits[:-6])
}


def hex_output(hex_number: str) -> int:
    try:
        return sum(
            ALPHABET[l] * (16**i)
            for i, l in enumerate(
                reversed(hex_number.lower().removeprefix("0x"))
            )
        )
    except KeyError as e:
        raise ValueError(f"'{e}' is not a valid hex digit!") from e
