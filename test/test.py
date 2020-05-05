from math import gamma, sqrt, pi
import pytest


def nsphere(n):
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return nsphere(n - 2) * 2 * pi / n


@pytest.mark.parametrize("n", range(1, 10))
def test_nsphere(n):
    closed = sqrt(pi) ** n / gamma(n / 2 + 1)
    assert (closed - nsphere(n)) < closed * 1.0e-10


if __name__ == "__main__":
    test_nsphere(5)
