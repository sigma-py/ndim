from math import gamma, pi, sqrt

import pytest

tol = 1.0e-10


@pytest.mark.parametrize("n", range(10))
def test_nball(n):
    def rec(n):
        assert n >= 0
        if n == 0:
            return 1
        elif n == 1:
            return 2
        return rec(n - 2) * 2 * pi / n

    def closed(n):
        return sqrt(pi) ** n / gamma(n / 2 + 1)

    assert abs(closed(n) - rec(n)) < abs(closed(n)) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_nsphere(n):
    def rec(n):
        assert n >= 1
        if n == 1:
            return 2
        elif n == 2:
            return 2 * pi
        return rec(n - 2) * 2 * pi / (n - 2)

    def closed(n):
        return n * sqrt(pi) ** n / gamma(n / 2 + 1)

    assert abs(closed(n) - rec(n)) < abs(closed(n)) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_enr(n):
    def rec(n):
        assert n >= 0
        if n == 0:
            return 1
        elif n == 1:
            return 2
        return rec(n - 2) * 2 * pi * (n - 1)

    def closed(n):
        return 2 * sqrt(pi) ** n * gamma(n) / gamma(n / 2)

    assert abs(closed(n) - rec(n)) < closed(n) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_enr2(n):
    def rec(n):
        assert n >= 0
        if n == 0:
            return 1
        elif n == 1:
            return sqrt(2 * pi)
        return rec(n - 2) * 2 * pi

    def closed(n):
        return sqrt(2 * pi) ** n

    assert abs(closed(n) - rec(n)) < closed(n) * tol


# \int_-1^1 x^k / sqrt(1 - x^2)
@pytest.mark.parametrize("k", range(1, 10))
def test_int(k):
    def rec(k):
        assert k >= 0
        if k == 0:
            return pi
        elif k == 1:
            return 0
        return rec(k - 2) * (k - 1) / k

    def closed(k):
        if k == 0:
            return pi
        return sqrt(pi) * ((-1) ** k + 1) * gamma(0.5 * (k + 1)) / gamma(0.5 * k) / k

    assert abs(closed(k) - rec(k)) < (1 + closed(k)) * tol


if __name__ == "__main__":
    test_nsphere(5)
