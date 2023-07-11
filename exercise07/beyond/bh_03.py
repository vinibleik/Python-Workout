def URL_encode(url: str) -> str:
    """
    Encode a full ASCII url replacing all non alphanumeric characters
    for their respective hex values.

    Args:
        url (str): URL to be encoded.

    Returns:
        str: URL encoded
    """
    return "".join(a if a.isalnum() else f"%{hex(ord(a))[2:]}" for a in url)
