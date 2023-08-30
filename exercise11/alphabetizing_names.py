from operator import itemgetter
from typing import Final

PEOPLE: Final[list[dict[str, str]]] = [
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
]


def alphabetize_names():
    return sorted(PEOPLE, key=itemgetter("last", "first"))
