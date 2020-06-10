"""
\\int_-1^1 x^k / sqrt(1 - x^2)
"""
from math import factorial, gamma, pi, sqrt

import pytest

import ndim


def closed(k):
    return ((-1) ** k + 1) / 2 * (sqrt(pi) * gamma((k + 1) / 2) / gamma(k / 2 + 1))


def cases(k):
    if k % 2 == 0:
        return pi * factorial(k) / (2 ** k * factorial(k / 2) ** 2)
    return 0


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - cases(n)) < (1 + abs(ref)) * tol
    assert (
        abs(ref - ndim.nball.integrate_monomial([n], lmbda=-0.5)) < (1 + abs(ref)) * tol
    )
