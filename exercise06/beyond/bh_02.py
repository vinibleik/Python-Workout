def transpose_string(arr: list[str]) -> list[str]:
    return [" ".join(i) for i in zip(*(s.split() for s in arr))]
