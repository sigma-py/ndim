"""
\\int_-1^1 x^k * sqrt(1 - x^2)
"""
from math import factorial, gamma, pi, sqrt

import pytest


def closed(k):
    return (
        ((-1) ** k + 1)
        / 2
        * (sqrt(pi) * gamma((k + 1) / 2) / ((k + 2) * gamma(k / 2 + 1)))
    )


def cases(k):
    if k % 2 == 0:
        return pi * factorial(k) / (2 ** k * (k + 2) * factorial(k / 2) ** 2)
    return 0


def recurrence(k):
    assert k >= 0
    if k == 0:
        return pi / 2
    elif k == 1:
        return 0
    return recurrence(k - 2) * (k - 1) / (k + 2)


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < (1 + abs(ref)) * tol
    assert abs(ref - recurrence(n)) < (1 + abs(ref)) * tol
