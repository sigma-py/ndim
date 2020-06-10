"""
exp(-(x_1^2 + ... + x_n^2))
"""
from math import pi, sqrt

import pytest

import ndim


def closed(n):
    return sqrt(pi) ** n


def cases(n):
    if n % 2 == 0:
        return pi ** (n / 2)
    return sqrt(pi) * pi ** ((n - 1) / 2)


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < abs(ref) * tol
    assert abs(ref - ndim.enr2.volume(n, "physicists")) < abs(ref) * tol
