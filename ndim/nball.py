import math

import sympy


def volume(n, lmbda=0, symbolic=False):
    pi = sympy.pi if symbolic else math.pi
    beta_one_half = (
        (lambda a: sympy.beta(a, sympy.Rational(1, 2)))
        if symbolic
        else (lambda a: math.gamma(a) * math.gamma(0.5) / math.gamma(a + 0.5))
    )

    def _recurrence(n):
        assert n >= 0
        if n == 0:
            return 1
        elif n == 1:
            return beta_one_half(lmbda + 1)
        return _recurrence(n - 2) * 2 * pi / (2 * lmbda + n)

    return _recurrence(n)


def integrate_monomial(exponents, lmbda=0, symbolic=False):
    n = len(exponents)
    n = sympy.S(n) if symbolic else n

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        return volume(n, lmbda, symbolic)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    # TODO -2?
    p = sum(exponents)
    return integrate_monomial(k2, lmbda, symbolic) * (k0 - 1) / (2 * lmbda + p + n)
