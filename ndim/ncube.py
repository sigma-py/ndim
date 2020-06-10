import sympy


def volume(n):
    if n == 0:
        return 1
    return 2 * volume(n - 1)


def integrate_monomial(exponents, symbolic=False):
    frac = sympy.Rational if symbolic else lambda a, b: a / b

    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        n = len(exponents)
        return volume(n)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial(k2, symbolic) * frac(k0 - 1, k0 + 1)
