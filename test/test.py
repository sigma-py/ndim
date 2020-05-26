from math import gamma, pi, sqrt

import pytest

tol = 1.0e-10


# \int_-1^1 x^k * sqrt(1 - x^2)
@pytest.mark.parametrize("k", range(10))
def test_chebyshev2(k):
    def rec(k):
        assert k >= 0
        if k == 0:
            return 0.5 * pi
        elif k == 1:
            return 0
        return rec(k - 2) * (k - 1) / (k + 2)

    def closed(k):
        return (
            ((-1) ** k + 1)
            / 2
            * (sqrt(pi) * gamma((k + 1) / 2) / ((k + 2) * gamma(k / 2 + 1)))
        )

    assert abs(closed(k) - rec(k)) < (1 + closed(k)) * tol


# \int_-inf^inf x^k * exp(-x^2)
@pytest.mark.parametrize("k", range(10))
def test_hermite_physicist(k):
    def rec(k):
        assert k >= 0
        if k == 0:
            return sqrt(pi)
        elif k == 1:
            return 0
        return rec(k - 2) * (k - 1) / 2

    def closed(k):
        if k % 2 == 1:
            return 0.0
        return gamma((k + 1) / 2)

    assert abs(closed(k) - rec(k)) < (1 + closed(k)) * tol


# \int_-inf^inf x^k * exp(-x^2/2) / sqrt(2*pi)
@pytest.mark.parametrize("k", range(10))
def test_hermite_probabilist(k):
    def rec(k):
        assert k >= 0
        if k == 0:
            return 1
        elif k == 1:
            return 0
        return rec(k - 2) * (k - 1)

    def closed(k):
        if k % 2 == 1:
            return 0.0
        return 2 ** ((k + 1) / 2) * gamma((k + 1) / 2) / sqrt(2 * pi)

    assert abs(closed(k) - rec(k)) < (1 + closed(k)) * tol
