import sympy


def _volume(n):
    if n == 0:
        return 1
    return volume(n - 1) / n


def volume(n, symbolic=False):
    n = sympy.S(n) if symbolic else n
    return _volume(n)


def integrate_monomial(exponents, symbolic=False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b
    n = len(exponents)

    if all(k == 0 for k in exponents):
        return volume(n, symbolic)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    alpha = frac(k0, sum(exponents) + n)
    k2 = exponents.copy()
    k2[idx] -= 1
    return integrate_monomial(k2, symbolic) * alpha
