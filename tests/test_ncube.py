import random

import pytest
from helpers import prod

import ndim


@pytest.mark.parametrize("n", range(1, 10))
def test_volume(n):
    ref = 2**n
    tol = 1.0e-14
    assert abs(ref - ndim.ncube.volume(n)) < abs(ref) * tol


@pytest.mark.parametrize("n", range(1, 10))
def test_monomial(n):
    random.seed(0)
    k = [random.randrange(0, 11, 2) for _ in range(n)]

    ref = prod((1 + (-1) ** kk) / (kk + 1) for kk in k)

    tol = 1.0e-14
    assert abs(ref - ndim.ncube.integrate_monomial(k)) < abs(ref) * tol
