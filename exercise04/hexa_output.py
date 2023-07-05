from string import hexdigits


def hex_output(hex_number: str) -> int:
    hex_number = hex_number.lower().removeprefix("0x")

    return sum(int(n, 16) * (16**i) for i, n in enumerate(hex_number[::-1]))


if __name__ == "__main__":
    print(hex_output("0x50"))
