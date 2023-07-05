def triangle_name(name: str) -> None:
    if name:
        triangle_name(name[:-1])
    print(name)


if __name__ == "__main__":
    triangle_name("")
