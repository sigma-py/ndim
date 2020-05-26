from math import pi, gamma, sqrt, factorial

import pytest


def closed(n):
    return sqrt(pi) ** n / gamma(n / 2 + 1)


def cases(n):
    if n % 2 == 0:
        n2 = n // 2
        return pi ** n2 / factorial(n2)

    return (
        pi ** ((n - 1) // 2) * 2 ** (n + 1) * factorial((n + 1) // 2) / factorial(n + 1)
    )


def recurrence(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return recurrence(n - 2) * 2 * pi / n


@pytest.mark.parametrize("n", range(10))
def test_nball(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - recurrence(n)) < abs(ref) * tol
