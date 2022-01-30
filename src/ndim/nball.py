import math

import sympy


def volume(n, lmbda=0, r=1, symbolic=False):
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
            return beta_one_half(lmbda + 1) * r ** (1 + 2 * lmbda)
        return _recurrence(n - 2) * 2 * pi / (2 * lmbda + n) * r**2

    return _recurrence(n)


def integrate_monomial(exponents, lmbda=0, symbolic=False):
    exponents = list(exponents)
    n = len(exponents)
    n = sympy.S(n) if symbolic else n

    if any(k % 2 == 1 for k in exponents):
        return 0

    def _recurrence(exponents):
        if all(k == 0 for k in exponents):
            return volume(n, lmbda=lmbda, symbolic=symbolic)

        # find first nonzero
        idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
        k2 = exponents.copy()
        k2[idx] -= 2
        return _recurrence(k2) * (k0 - 1) / (2 * lmbda + sum(exponents) + n)

    return _recurrence(exponents)
