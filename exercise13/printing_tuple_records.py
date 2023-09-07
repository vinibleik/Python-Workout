from operator import itemgetter


def format_sort_records(records: list[tuple[str, str, float]]) -> str:
    format_str = "{lname:10} {fname:10} {time:-5.2f}\n"
    return "".join(
        format_str.format(fname=fname, lname=lname, time=time)
        for fname, lname, time in sorted(records, key=itemgetter(1, 0))
    )


if __name__ == "__main__":
    PEOPLE = [
        ("Donald", "Trump", 7.85),
        ("Vladimir", "Putin", 3.626),
        ("Jinping", "Xi", 10.603),
    ]
    print(format_sort_records(PEOPLE))
