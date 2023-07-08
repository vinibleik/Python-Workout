def pig_latin(word: str) -> str:
    if word[0] in ("a", "e", "i", "o", "u"):
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


def pl_sentence(sentence: str) -> str:
    return " ".join(pig_latin(word) for word in sentence.split())
