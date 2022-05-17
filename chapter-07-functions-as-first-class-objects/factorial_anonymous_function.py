from functools import reduce


def factorial(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
