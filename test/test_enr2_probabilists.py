"""
exp(-(x_1^2 + ... + x_n^2)/2) / sqrt(2*pi) ** n
"""
import pytest


def closed(n):
    return 1


def cases(n):
    if n % 2 == 0:
        return 1
    return 1


def recurrence(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return recurrence(n - 2)


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - recurrence(n)) < abs(ref) * tol
