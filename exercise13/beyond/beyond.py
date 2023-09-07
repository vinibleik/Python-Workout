from collections import namedtuple
from operator import attrgetter

Record = namedtuple("Record", "fname, lname, time")

recordAttrGetter = attrgetter("lname", "fname")

PEOPLE = [
    ("Donald", "Trump", 7.85),
    ("Vladimir", "Putin", 3.626),
    ("Jinping", "Xi", 10.603),
]


def record_format_str(records: list[Record]) -> str:
    FORMAT_STR = "{lname:10} {fname:10} {time:5.2f}"
    return "\n".join(
        FORMAT_STR.format(**p._asdict()) for p in sorted(records, key=recordAttrGetter)
    )


if __name__ == "__main__":
    records = [Record(*p) for p in PEOPLE]
    print(record_format_str(records))
