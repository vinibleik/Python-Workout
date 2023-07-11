import re


def ubbi_dubbi(word: str) -> str:
    """
    This function translates a English word in Ubbi Dubbi language.
    That means each vowel will be preceded by "ub".

    Args:
        word (str): English word to be translated.

    Returns:
        str: word translated in Ubbi Dubbi

    Example:
        [in]  word
        [out] wubord
    """

    # Newbie solution...
    # ubbi_dubbi_word = ""
    # for letter in word:
    #     if letter in VOWELS:
    #         ubbi_dubbi_word += f"ub{letter}"
    #     else:
    #         ubbi_dubbi_word += letter
    # return ubbi_dubbi_word

    return "".join(f"ub{letter}" if letter in "aeiou" else letter for letter in word)
    # return re.sub(r"[aeiou]", r"ub\g<0>", word)  # It'll be so easy...
