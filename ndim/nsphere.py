import math

import sympy


def volume(n, symbolic):
    assert n >= 1

    pi = sympy.pi if symbolic else math.pi

    if n == 1:
        return 2
    elif n == 2:
        return 2 * pi
    return volume(n - 2) * 2 * pi / (n - 2)


def integrate_monomial(exponents, symbolic=False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b
    n = len(exponents)

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        return volume(n, symbolic)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    alpha = frac(k0 - 1, sum(exponents) + n - 2)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial(k2, symbolic) * alpha
