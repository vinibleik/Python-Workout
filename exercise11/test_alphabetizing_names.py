from typing import Final

from alphabetizing_names import alphabetize_names

PEOPLE_SORTED: Final[list[dict[str, str]]] = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
]


def test_alphatize_names():
    result = alphabetize_names()
    assert result == PEOPLE_SORTED
