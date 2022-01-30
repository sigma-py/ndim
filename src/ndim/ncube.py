from typing import List

import sympy


def volume(n: int):
    return 2**n


def integrate_monomial(exponents: List[int], symbolic: bool = False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b
    exponents = list(exponents)
    n = len(exponents)

    if any(k % 2 == 1 for k in exponents):
        return 0

    def _recurrence(exponents):
        if all(k == 0 for k in exponents):
            return volume(n)

        # find first nonzero
        idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
        k2 = exponents.copy()
        k2[idx] -= 2
        return _recurrence(k2) * frac(k0 - 1, k0 + 1)

    return _recurrence(exponents)
