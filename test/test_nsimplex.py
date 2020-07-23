import random
from math import factorial, gamma

import pytest
from helpers import prod

import ndim


@pytest.mark.parametrize("n", range(1, 10))
def test_volume(n):
    ref = 1 / factorial(n)
    tol = 1.0e-14
    assert abs(ref - ndim.nsimplex.volume(n)) < abs(ref) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_monomial(n):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = prod(gamma(kk + 1) for kk in k) / gamma(n + 1 + sum(k))

    tol = 1.0e-14
    assert abs(ref - ndim.nsimplex.integrate_monomial(k)) < abs(ref) * tol
