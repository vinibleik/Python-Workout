def my_sum(*args: int | float) -> int | float:
    total = 0
    for value in args:
        try:
            total += value
        except TypeError as e:
            raise ValueError("All the arguments must be numbers") from e
    return total


if __name__ == "__main__":
    print(my_sum(*list(range(10))))
