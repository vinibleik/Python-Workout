def my_sum(numbers: list[int | float], start: int | float = 0) -> int | float:
    total = start
    for number in numbers:
        try:
            total += number
        except TypeError as e:
            raise ValueError("All the arguments must be numbers") from e
    return total
