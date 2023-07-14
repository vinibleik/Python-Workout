from typing import Any


def first_last(seq: Any) -> Any:
    """
    This function returns an object of the same type as the parameter
    seq with the first and last element. If seq is not subscriptable
    raise TypeError

    Args:
        seq (Any): An sequence obj

    Raise:
        TypeError: Is seq is not subscriptable

    Returns:
        Any: The first and last element from seq as the same type as seq
    """
    # try:
    #     return (
    #         seq[:1] + seq[-1:]
    #     )  # First ans Last elements with slice to retrieve the same obj as seq
    # except IndexError:
    #     return seq

    try:
        return seq[
            :: len(seq) - 1
        ]  # Retrieving slicing the first and last elements, if seq is empty so the result will be so. But if the len(seq) == 1, raises ValueError: slice step cannot be zero. Others lengths work perfectly well.
    except ValueError:
        return seq + seq
