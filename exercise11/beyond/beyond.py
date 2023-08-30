# Beyond 1
def sort_by_mod(numbers: list[int]):
    """
    Given a sequence of positive and negative numbers, sort them by absolute value.

    Args:
        numbers (list[int]): list of numbers to be sorted

    Return:
       list[int]: list of numbers ordered by absolute values
    """
    return sorted(numbers, key=abs)


# Beyond 2
def sort_by_n_vowels(strings: list[str]):
    """
    Given a list of strings, sort them according to how many vowels they contain.

    Args:
        strings (list[str]): list of strings.

    Returns:
        list[str]: list of strings sorted by how many vowels they contain.
    """

    def count_vowels(string: str):
        VOWELS: str = "aeiouAEIOU"
        return sum(1 for i in string if i in VOWELS)

    return sorted(strings, key=count_vowels)


# Beyond 3
def sort_by_line_sum(numbers_list: list[list[int]]):
    """
    Given a list of lists, with each list containing zero or more numbers, sort by the
    sum of each inner list’s numbers.

    Args:
        numbers_list (list[list[int]]): list containing list with zero or
        more numbers.

    Return:
        list[list[int]]: The paremeter sorted by the sum of each inside list.
    """
    return sorted(numbers_list, key=sum)
