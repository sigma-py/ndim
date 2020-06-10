from math import factorial, gamma, pi, sqrt

import pytest

import ndim


def closed(n):
    return sqrt(pi) ** n / gamma(n / 2 + 1)


def cases(n):
    if n % 2 == 0:
        return pi ** (n / 2) / factorial(n / 2)

    return (
        pi ** ((n - 1) / 2) * 2 ** (n + 1) * factorial((n + 1) / 2) / factorial(n + 1)
    )


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - ndim.nball.volume(n)) < abs(ref) * tol
