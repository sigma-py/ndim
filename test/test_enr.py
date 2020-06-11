import random
from math import gamma, pi, sqrt

import pytest

import ndim


@pytest.mark.parametrize("n", range(1, 10))
@pytest.mark.parametrize("alpha", [0, 1, 1.5])
def test_volume(n, alpha):
    ref = 2 * sqrt(pi) ** n * gamma(n + alpha) / gamma(n / 2)
    tol = 1.0e-14
    assert abs(ref - ndim.enr.volume(n, alpha)) < abs(ref) * tol


def prod(iterable):
    import operator
    from functools import reduce

    return reduce(operator.mul, iterable, 1)


@pytest.mark.parametrize("n", range(1, 10))
@pytest.mark.parametrize("alpha", [0, 1, 1.5])
def test_monomial(n, alpha):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = (
        2
        * gamma(alpha + n + sum(k))
        * prod(gamma((kk + 1) / 2) for kk in k)
        / gamma(sum((kk + 1) / 2 for kk in k))
    )

    tol = 1.0e-14
    assert abs(ref - ndim.enr.integrate_monomial(k, alpha)) < abs(ref) * tol
