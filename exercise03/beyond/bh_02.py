from decimal import Decimal, InvalidOperation


def sum_decimal() -> None:
    try:
        number1 = Decimal(input("Enter the first number: "))
        number2 = Decimal(input("Enter the second number: "))
    except InvalidOperation as e:
        raise ValueError("Enter an valid float as input") from e

    print(f"{number1} + {number2} = {number1 + number2}")
