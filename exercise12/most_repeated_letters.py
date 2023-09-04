from collections import Counter


def get_most_letter(word: str):
    return Counter(word).most_common()[0][1]


# Write a function that takes a sequence of strings as input, and return
# the string that contains the greatest number of repeated letters.
def most_repeated_letters(strings: list[str]):
    return max(strings, default=None, key=get_most_letter)
