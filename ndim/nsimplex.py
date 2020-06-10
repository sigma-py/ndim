import sympy


def volume(n, symbolic=False):
    n = sympy.S(n) if symbolic else n

    def _recurrence(n):
        if n == 0:
            return 1
        return _recurrence(n - 1) / n

    return _recurrence(n)


def integrate_monomial(exponents, symbolic=False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b
    n = len(exponents)

    def _recurrence(exponents):
        if all(k == 0 for k in exponents):
            return volume(n, symbolic)

        # find first nonzero
        idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
        k2 = exponents.copy()
        k2[idx] -= 1
        return _recurrence(k2) * frac(k0, sum(exponents) + n)

    return _recurrence(exponents)
