def strsort(string: str) -> str:
    """Return the string sorted by its Unicode

    Args:
        string (str): string to be sorted

    Returns:
        str: string sorted
    """
    return "".join(sorted(string))
