import math

import sympy


def _beta_one_half(a, b):
    return math.gamma(a) * math.gamma(b) / math.gamma(a + b)


def _volume(n, lmbda, pi, beta_one_half):
    assert n >= 0

    if n == 0:
        return 1
    elif n == 1:
        return beta_one_half(lmbda + 1)
    return volume(n - 2) * 2 * pi / (2 * lmbda + n)


def volume(n, lmbda=0, symbolic=False):
    pi = sympy.pi if symbolic else math.pi
    beta_one_half = (
        lambda x: sympy.beta(x, sympy.Rational(1, 2)) if symbolic else _beta_one_half
    )
    return _volume(n, lmbda, pi, beta_one_half)


def integrate_monomial(exponents, lmbda=0, symbolic=False):
    n = len(exponents)
    n = sympy.S(n) if symbolic else n

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        return volume(n, lmbda, symbolic)

    p = sum(exponents)
    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    # TODO -2?
    return integrate_monomial(k2, lmbda, symbolic) * (k0 - 1) / (2 * lmbda + p + n)
