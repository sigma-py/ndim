def prod(iterable):
    import operator
    from functools import reduce

    return reduce(operator.mul, iterable, 1)
