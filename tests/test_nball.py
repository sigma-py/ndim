import random
from math import gamma, pi, sqrt

import pytest
from helpers import prod

import ndim


@pytest.mark.parametrize("n", range(10))
@pytest.mark.parametrize("lmbda", [-0.5, 0.0, 0.5, 1.0])
def test_volume(n, lmbda):
    ref = gamma(lmbda + 1) * sqrt(pi) ** n / gamma(lmbda + n / 2 + 1)
    tol = 1.0e-14
    assert abs(ref - ndim.nball.volume(n, lmbda)) < abs(ref) * tol


@pytest.mark.parametrize("n", range(1, 10))
@pytest.mark.parametrize("lmbda", [-0.5, 0.0, 0.5, 1.0])
def test_monomial(n, lmbda):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = (
        gamma(lmbda + 1)
        * prod(gamma((kk + 1) / 2) for kk in k)
        / gamma(1 + lmbda + sum((kk + 1) / 2 for kk in k))
    )

    tol = 1.0e-14
    assert abs(ref - ndim.nball.integrate_monomial(k, lmbda)) < abs(ref) * tol
