import math

import sympy


def _volume(n, alpha, pi, gamma):
    assert n >= 0
    if n == 1:
        return 2 * gamma(1 + alpha)
    elif n == 2:
        return 2 * pi * gamma(2 + alpha)
    return _volume(n - 2, alpha) * 2 * pi * (n + alpha - 1) * (n + alpha - 2) / (n - 2)


def volume(n, alpha=0, symbolic=False):
    pi = sympy.pi if symbolic else math.pi
    gamma = sympy.gamma if symbolic else math.gamma
    n = sympy.S(n) if symbolic else n
    return _volume(n, alpha, pi, gamma)


def integrate_monomial(exponents, alpha=0, symbolic=False):
    S = sympy.S if symbolic else lambda x: x
    n = S(len(exponents))

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        return volume(n, alpha, symbolic)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    p = sum(exponents)
    alpha = (alpha + n + p - 1) * (alpha + p + n - 2) * (k0 - 1) / (n + p - 2)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial(k2, alpha, symbolic) * alpha
