def mean(numbers: list[int | float]) -> float:
    if not numbers:
        return 0.0

    total = 0.0
    for number in numbers:
        try:
            total += number
        except TypeError as e:
            raise ValueError("All the arguments must be numbers") from e
    return total / len(numbers)
