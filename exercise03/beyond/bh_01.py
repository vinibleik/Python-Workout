def format_float(n: float, before: int, after: int) -> float:
    if before < 0 or after < 0:
        raise ValueError("Format numbers must be positives!")

    before_part, after_part = str(n).split(".")

    if not before:
        before_part = "0"

    if not after_part:
        after_part = "0"

    return float(f"{before_part[-before:]}.{after_part[:after]}")


if __name__ == "__main__":
    print(format_float(1234.5678, 2, 3))
