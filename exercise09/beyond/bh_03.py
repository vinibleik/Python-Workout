def myzip(*iterables):
    """
    myzip yields a tuple of one element of each iterables given by parameter

    """
    max_length: int = min(map(len, iterables))
    iters = [iter(it) for it in iterables]
    for _ in range(max_length):
        yield tuple(next(it) for it in iters)
