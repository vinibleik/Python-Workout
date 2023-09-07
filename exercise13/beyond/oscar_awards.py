import argparse
import csv
from collections import namedtuple
from operator import attrgetter
from typing import List

csv_file = "oscar_nominations_2018.csv"

Record = namedtuple("Record", "name, length, director")


class MovieRecord(Record):
    __slots__ = ()

    def __str__(self) -> str:
        return (
            f"Movie: {self.name}, Length: {self.length} minutes, Director:"
            f" {self.director}"
        )


RECORDS: List[MovieRecord] = []

with open(csv_file, newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skipping the header

    RECORDS = [
        MovieRecord(name, int(length), director) for name, length, director in reader
    ]

parser = argparse.ArgumentParser(
    description=(
        "Given a set of records movies, you can sort them by movie name, length or"
        " director"
    ),
    epilog="Sort default by name",
)

parser.add_argument(
    "-n", "--name", action="store_true", help="Sort by movie name"
)  # on/off flag
parser.add_argument(
    "-l", "--length", action="store_true", help="Sort by movie lenght"
)  # on/off flag
parser.add_argument(
    "-d", "--director", action="store_true", help="Sort by movie director"
)  # on/off flag


def getGetters(args: argparse.Namespace) -> list[str]:
    getters = []
    if args.name:
        getters.append("name")
    if args.length:
        getters.append("length")
    if args.director:
        getters.append("director")
    return getters or ["name"]


def print_sorted_records(records: List[MovieRecord], getterKey: attrgetter) -> None:
    for record in sorted(records, key=getterKey):
        print(record)


if __name__ == "__main__":
    args = parser.parse_args()
    getterKey = attrgetter(*getGetters(args))
    print_sorted_records(RECORDS, getterKey)
