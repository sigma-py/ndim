"""
\\int_-inf^inf x^k * exp(-x^2)
"""
from math import factorial, gamma, pi, sqrt

import pytest


def closed(k):
    if k % 2 == 1:
        return 0
    return gamma((k + 1) / 2)


def cases(k):
    if k % 2 == 0:
        return sqrt(pi) * factorial(k) / (2 ** k * factorial(k / 2))
    return 0


def recurrence(k):
    assert k >= 0
    if k == 0:
        return sqrt(pi)
    elif k == 1:
        return 0
    return recurrence(k - 2) * (k - 1) / 2


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < (1 + abs(ref)) * tol
    assert abs(ref - recurrence(n)) < (1 + abs(ref)) * tol
