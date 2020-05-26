"""
\\int_-inf^inf x^k * exp(-x^2/2) / sqrt(2*pi)
"""
from math import factorial, gamma, pi, sqrt

import pytest


def closed(k):
    if k % 2 == 1:
        return 0
    return 2 ** ((k + 1) / 2) * gamma((k + 1) / 2) / sqrt(2 * pi)


def cases(k):
    if k % 2 == 0:
        return factorial(k) / (2 ** (k / 2) * factorial(k / 2))
    return 0


def recurrence(k):
    assert k >= 0
    if k == 0:
        return 1
    elif k == 1:
        return 0
    return recurrence(k - 2) * (k - 1)


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < (1 + abs(ref)) * tol
    assert abs(ref - recurrence(n)) < (1 + abs(ref)) * tol
