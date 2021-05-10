import random
from math import gamma, pi, sqrt

import pytest
from helpers import prod

import ndim


@pytest.mark.parametrize("n", range(1, 10))
def test_volume(n):
    ref = n * sqrt(pi) ** n / gamma(n / 2 + 1)
    tol = 1.0e-14
    assert abs(ref - ndim.nsphere.volume(n)) < abs(ref) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_monomial(n):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = (
        2 * prod(gamma((kk + 1) / 2) for kk in k) / gamma(sum((kk + 1) / 2 for kk in k))
    )

    tol = 1.0e-14
    assert abs(ref - ndim.nsphere.integrate_monomial(k)) < abs(ref) * tol
