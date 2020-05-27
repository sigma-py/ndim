from math import factorial, gamma, pi, sqrt

import pytest


def closed(n):
    return n * sqrt(pi) ** n / gamma(n / 2 + 1)


def cases(n):
    if n % 2 == 0:
        return n * pi ** (n / 2) / factorial(n / 2)

    return (
        n
        * pi ** ((n - 1) / 2)
        * 2 ** (n + 1)
        * factorial((n + 1) / 2)
        / factorial(n + 1)
    )


def recurrence(n):
    assert n >= 1
    if n == 1:
        return 2
    elif n == 2:
        return 2 * pi
    return recurrence(n - 2) * 2 * pi / (n - 2)


@pytest.mark.parametrize("n", range(1, 10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - recurrence(n)) < abs(ref) * tol
