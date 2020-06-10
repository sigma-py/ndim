"""
exp(-(x_1^2 + ... + x_n^2)/2) / sqrt(2*pi) ** n
"""
import pytest

import ndim


def closed(n):
    return 1


@pytest.mark.parametrize("n", range(10))
def test(n):
    ref = closed(n)
    tol = 1.0e-14
    assert abs(ref - ndim.enr2.volume(n, "probabilists")) < abs(ref) * tol
