from math import factorial, gamma, pi, sqrt

import pytest


def closed(n, alpha):
    return 2 * sqrt(pi) ** n * gamma(n + alpha) / gamma(n / 2)


def cases(n, alpha):
    if n % 2 == 0:
        return 2 * pi ** (n / 2) * gamma(n + alpha) / factorial(n / 2 - 1)

    return (
        pi ** ((n - 1) / 2)
        * 2 ** n
        * factorial((n - 1) / 2)
        * gamma(n + alpha)
        / factorial(n - 1)
    )


def recurrence(n, alpha):
    assert n >= 0
    if n == 1:
        return 2 * gamma(1 + alpha)
    elif n == 2:
        return 2 * pi * gamma(2 + alpha)
    return (
        recurrence(n - 2, alpha) * 2 * pi * (n + alpha - 1) * (n + alpha - 2) / (n - 2)
    )


@pytest.mark.parametrize("n", range(1, 10))
@pytest.mark.parametrize("alpha", [0, 1, 1.5])
def test(n, alpha):
    ref = closed(n, alpha)
    tol = 1.0e-14
    assert abs(ref - cases(n, alpha)) < abs(ref) * tol
    assert abs(ref - recurrence(n, alpha)) < abs(ref) * tol
