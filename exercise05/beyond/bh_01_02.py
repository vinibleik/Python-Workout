from string import punctuation


def pig_latin(word: str) -> str:
    if word[0].lower() in "aeiou":
        return (
            f"{word[:-1]}way{word[-1]}"
            if word[-1] in punctuation
            else f"{word}way"
        )

    if word[0].isupper() and len(word) > 1:
        word = f"{word[0].lower()}{word[1:].capitalize()}"

    if word[-1] in punctuation:
        return f"{word[1:-1]}{word[0]}ay{word[-1]}"

    return f"{word[1:]}{word[0]}ay"
