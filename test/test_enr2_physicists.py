"""
exp(-(x_1^2 + ... + x_n^2))
"""
from math import sqrt, pi
import pytest


def closed(n):
    return sqrt(pi) ** n


def cases(n):
    if n % 2 == 0:
        return pi ** (n // 2)
    return sqrt(pi) * pi ** (n // 2)


def recurrence(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return sqrt(pi)
    return recurrence(n - 2) * pi


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - recurrence(n)) < abs(ref) * tol
