def run_timing() -> None:
    total: float = 0.0

    runs = 0

    while user_input := input("Enter 10 km run time: "):
        try:
            total += float(user_input)
            runs += 1
        except ValueError:
            print("Enter an valid float number for minutes!")

    if runs:
        print(f"Average of {total/runs:.1f}, over {runs} runs!")
    else:
        print("You didn't run!")


if __name__ == "__main__":
    run_timing()
