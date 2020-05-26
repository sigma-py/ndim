from math import pi, sqrt, gamma, factorial
import pytest


def closed(n):
    return 2 * sqrt(pi) ** n * gamma(n) / gamma(n / 2)


def cases(n):
    if n % 2 == 0:
        n2 = n // 2
        return 2 * pi ** n2 * factorial(n - 1) / factorial(n2 - 1)

    return pi ** ((n - 1) // 2) * 2 ** n * factorial((n - 1) / 2)


def recurrence(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return recurrence(n - 2) * 2 * pi * (n - 1)


@pytest.mark.parametrize("n", range(1, 10))
def test_nball(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - recurrence(n)) < abs(ref) * tol
