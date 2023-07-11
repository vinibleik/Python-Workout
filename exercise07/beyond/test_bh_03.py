from bh_03 import URL_encode
import pytest


@pytest.mark.parametrize(
    ("url", "output"),
    (
        ("", ""),
        (
            "Noencodedcaracter",
            "Noencodedcaracter",
        ),
        (
            r"https://lingojam.com/Fancy Text Generator",
            r"https%3a%2f%2flingojam%2ecom%2fFancy%20Text%20Generator",
        ),
        (
            r"https://9anime.to/watch/made-in-abyss.582v/ep-5",
            r"https%3a%2f%2f9anime%2eto%2fwatch%2fmade%2din%2dabyss%2e582v%2fep%2d5",
        ),
        (
            r"https://docs.python.org/3/library/os.path.html#os.path.split",
            r"https%3a%2f%2fdocs%2epython%2eorg%2f3%2flibrary%2fos%2epath%2ehtml%23os%2epath%2esplit",
        ),
    ),
)
def test_URL_encode(url: str, output: str) -> None:
    assert URL_encode(url) == output
