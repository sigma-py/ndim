import math

import sympy


def volume(n, r=1, symbolic=False):
    pi = sympy.pi if symbolic else math.pi

    def _recurrence(n):
        assert n >= 1
        if n == 1:
            return 2
        elif n == 2:
            return 2 * pi * r
        return _recurrence(n - 2) * 2 * pi / (n - 2) * r**2

    return _recurrence(n)


def integrate_monomial(exponents, symbolic=False):
    exponents = list(exponents)
    n = len(exponents)
    n = sympy.S(n) if symbolic else n

    if any(k % 2 == 1 for k in exponents):
        return 0

    def _recurrence(exponents):
        if all(k == 0 for k in exponents):
            return volume(n, symbolic=symbolic)

        # find first nonzero
        idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
        k2 = exponents.copy()
        k2[idx] -= 2
        return _recurrence(k2) * (k0 - 1) / (sum(exponents) + n - 2)

    return _recurrence(exponents)
