import json

MENU: dict[str, float]

with open("./foods.json") as file:
    MENU = json.load(file)


def restaurant() -> None:
    total: float = 0.0

    while True:
        order = input("Order: ").title().strip()

        if order == "":
            break

        price = MENU.get(order)

        if price is None:
            print(f"Sorry, we are fresh out of {order} today.")
        else:
            total += price
            print(f"Order {order} costs {price:.2f}, Your total is {total:.2f}.")

    print(f"Your total is {total:.2f}")


if __name__ == "__main__":
    restaurant()
