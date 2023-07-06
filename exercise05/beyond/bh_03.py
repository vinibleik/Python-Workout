def pig_latin_2(word: str) -> str:
    if len(set(word).intersection("aeiou")) >= 2:
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"
