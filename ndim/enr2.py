"""
exp(-(x_1^2 + ... + x_n^2))
"""
import math

import sympy


def _volume(n, pi, sqrt):
    assert n >= 0

    if n == 0:
        return 1
    elif n == 1:
        return sqrt(pi)
    return _volume(n - 2, pi, sqrt) * pi


def volume_physicists(n, symbolic):
    pi = sympy.pi if symbolic else math.pi
    sqrt = sympy.sqrt if symbolic else math.sqrt
    return _volume(n, pi, sqrt)


def integrate_monomial_physicists(exponents, symbolic=False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        n = len(exponents)
        return volume_physicists(n, symbolic)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial_physicists(k2, symbolic) * frac(k0 - 1, 2)


def volume_probabilists(n):
    return 1


def integrate_monomial_probabilists(exponents):
    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        n = len(exponents)
        return volume_probabilists(n)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial_probabilists(k2) * (k0 - 1)


def volume(n, variant, symbolic=False):
    if variant == "physicists":
        return volume_physicists(n, symbolic)
    assert variant == "probabilists"
    return volume_probabilists(n)


def integrate_monomial(n, variant, symbolic=False):
    if variant == "physicsts":
        return integrate_monomial_physicists(n, symbolic)
    assert variant == "probabilists"
    return integrate_monomial_probabilists(n, symbolic)
