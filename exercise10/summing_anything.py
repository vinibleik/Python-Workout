def mysum(*args):
    if not args:
        return args

    result = args[0]

    for arg in args[1:]:
        result += arg

    return result
