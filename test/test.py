from math import gamma, sqrt, pi
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


if __name__ == "__main__":
    test_nsphere(5)
